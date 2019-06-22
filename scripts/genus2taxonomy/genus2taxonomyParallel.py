#!/usr/bin/env python
import sqlite3
import argparse
import collections
import sys
import multiprocessing

#usage: python ~/github/zkwu/kcMeta/src/kcMeta/genus2taxonomy.py --genus /home/wzk/database/taxonomy/SILVA_Greengene_16SrRNA_dereplication_taxas_genus.txt  --input /home/wzk/Project/C128/NR/representive.faa.diamond_taxonomy_test.txt --database /home/wzk/database/taxonomy/taxanomy.db --out /home/wzk/Project/C128/NR/representive.faa.diamond_taxonomy_test_out.txt > temp

__author__ = "Zhikun Wu"
__date__ = "2018.10.10"
__email__ = "598466208@qq.com"

def genus_high_levels(genus_file):
    """
    >HM808042.1.1372        k__Bacteria; p__Firmicutes; c__Bacilli; o__Bacillales; f__Staphylococcaceae; g__Staphylococcus; s__
    >GQ001287.1.1372        k__Bacteria; p__Firmicutes; c__Bacilli; o__Bacillales; f__Staphylococcaceae; g__Staphylococcus; s__
    """
    genusTaxas = {}
    in_h = open(genus_file, "r")
    for line in in_h:
        lines = line.strip().split("\t")
        taxa = lines[-1]
        taxas = taxa.split("; ")
        newTaxa = "|".join(taxas[:-1])
        for t in taxas:
            if "g__" in t:
                genus = t.split("g__")[-1]
                genusTaxas[genus] = newTaxa
    in_h.close()
    return genusTaxas


def get_taxonomy_name(records, cursor, taxa_ids):
    """
    records:
    [(212743,)]

    cursor:
    sqlite3 handle

    taxa_ids: list
    """
    for r in records:
        taxa_id = r[0]
        taxa_ids.append(taxa_id)
        if taxa_id == 1:
            break
        else:
            cursor.execute("""
                SELECT parent_id 
                from  TaxaParent 
                where taxa_id = ? ;
            """, (taxa_id,))
            records = cursor.fetchall()
            get_taxonomy_name(records, cursor, taxa_ids)

def taxa_full_name(TaxaName, number):
    levels = ["superkingdom", "phylum", "class", "order", "family", "genus"]
    tt = []
    for i in range(number):
        ii = levels[i]
        t = TaxaName[ii]
        if ii == "superkingdom":
            tt.append("k__%s" % t)
        elif ii == "phylum":
            tt.append("p__%s" % t)
        elif ii == "class":
            tt.append("c__%s" % t)
        elif ii == "order":
            tt.append("o__%s" % t)
        elif ii == "family":
            tt.append("f__%s" % t)
        elif ii == "genus":
            tt.append("g__%s" % t)
    return "|".join(tt)

def parse_level_taxas(TaxaName):
    levels = ["superkingdom", "phylum", "class", "order", "family", "genus"]
    missing = []
    ### get last index
    last = None
    for l in range(len(levels)):
        ll = levels[l]
        if ll not in TaxaName:
            missing.append(l)
        else:
            last = l
    ### check the missing
    # print(last, missing)
    taxonomy = None
    TaName = None
    if last != None:
        if missing == []:
            taxonomy = taxa_full_name(TaxaName, 6)
        else:
            missingFirst = missing[0]
            if last + 1 == missingFirst:
                taxonomy = taxa_full_name(TaxaName, missingFirst)
            else:
                lastTaxa = levels[last]
                TaxaName = TaxaName[lastTaxa]
                TaName = lastTaxa + "__" + TaxaName
    # else:   
    #     print("Please check whether the dict of taxa is correct: ")
    #     print(TaxaName)
    #     sys.exit(1)
    return taxonomy, TaName

def get_query_taxonomy(genus_file, anno_file, database, out_file):
    genusTaxas = genus_high_levels(genus_file)
    # print(genusTaxas)
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    in_h = open(anno_file, "r")
    out_h = open(out_file, "w")
    records = []
    for line in in_h:
        line = line.strip()
        records.append(line)
    in_h.close()

    ### mutiple threads to deal with the records
    PROCESS = []
    for i in range(len(records)):
        record = records[i]
        process = multiprocessing.Process(target=get_query_taxonomy_one, args=(genusTaxas, cursor, record, out_h))
        PROCESS.append(process)
    for p in PROCESS:
        p.start()
    for p in PROCESS:
        p.join()
    out_h.close()

def get_query_taxonomy_one(genusTaxas, cursor, line, out_h):
    lines = line.split("\t")
    query = lines[0]
    taxa = lines[-1]
    # genus = taxa.split()[0]
    genus = taxa
    ### get taxa id
    cursor.execute("""
        SELECT taxa_id 
        from  TaxaNameLevel 
        where taxa_name = ? ;
    """, (genus,))
    records = cursor.fetchall()
    taxa_ids = []
    ### records: [(212743,)]
    get_taxonomy_name(records, cursor, taxa_ids)
    ### taxa_ids: [212743, 224471, 119065, 80840, 28216, 1224, 2, 131567, 1]

    
    ### get the taxa level and name
    ### reverse the taxa_ids
    reversedIds = taxa_ids[::-1]

    ###example:
    # Gene000022  Mastigocladus laminosus UU774   superkingdom_Bacteria   phylum_Cyanobacteria    order_Nostocales    family_Hapalosiphonaceae    genus_Mastigocladus species_Mastigocladus laminosus 
    # Gene000026  Rhodobacter sp. CACIA14H1   superkingdom_Bacteria   phylum_Proteobacteria   class_Alphaproteobacteria   order_Rhodobacterales   family_Rhodobacteraceae genus_Rhodobacter   species_Rhodobacter sp. CACIA14H1
    # Gene000028  Firmicutes bacterium CAG:552    superkingdom_Bacteria   phylum_Firmicutes   species_Firmicutes bacterium CAG:552                
    # Gene000029  Nitrospira cf. moscoviensis SBR1015 superkingdom_Bacteria   phylum_Nitrospirae  class_Nitrospira    order_Nitrospirales family_Nitrospiraceae   genus_Nitrospira    species_Nitrospira cf. moscoviensis SBR1015

    # LevelName = []
    TaxaName = {}
    for taxa_id in reversedIds:
        cursor.execute("""
            SELECT taxa_name, taxa_level 
            from TaxaNameLevel 
            where taxa_id = ? ;
        """, (taxa_id,))
        taxas = cursor.fetchall()

        for t in taxas:
            name, level = t
            if level != "no rank":
                # LevelName.append("%s_%s" % (level, name))
                TaxaName[level] = name
    ### output 
    taxonomy, TaName = parse_level_taxas(TaxaName)
    if taxonomy != None:
        ### species
        if "g__" in taxonomy:
            species = delete_sp_cf(genus)
            out_h.write("%s\t%s\t%s|s__%s\n" % (query, genus, taxonomy, species))
        else:
            out_h.write("%s\t%s\t%s\n" % (query, genus, taxonomy))
    ### missing in the middle
    else:
        if TaName != None:
            gs = genus.split()
            ### usually genus is one string, it also be two, such as "Candidatus Accumulibacter"
            if len(gs) == 1:
                g = gs[0]
            else:
                if gs[1][0].isupper():
                    g = " ".join(gs[:1])
                else:
                    g = gs[0]
            if g in genusTaxas:
                newTaxa = genusTaxas[g]
                species = delete_sp_cf(genus)
                out_h.write("%s\t%s\t%s|s__%s\n" % (query, genus, newTaxa, species))
            else:
                out_h.write("%s\t%s\t%s\n" % (query, genus, TaName))
        else:
            print(line)
    # print("%s\t%s\t%s" % (query, genus, "\t".join(TaxaName)))


def delete_sp_cf(taxa):
    """
    taxa:
    Nitrospira sp. ST-bin4
    Nitrospira cf. moscoviensis SBR1015

    return:
    Nitrospira_ST-bin4
    Nitrospira_moscoviensis
    """
    taxas = taxa.split()
    newTaxa = []
    for t in taxas:
        if "sp." == t or "cf." == t:
            pass
        else:
            newTaxa.append(t)
    if len(newTaxa) == 1:
        return newTaxa[0]
    else:
        return "_".join(newTaxa[:2])

def main():
    parser = argparse.ArgumentParser(description="Get the taxa id and names for the genus.")
    parser.add_argument("-i", "--input", help="The input file.")
    parser.add_argument("-d", "--database", help="The input database.")
    parser.add_argument("-g", "--genus", help="The genus and high lebel taxonomy file.")
    parser.add_argument("-t", "--threads", help="The threads number.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()
    get_query_taxonomy(args.genus, args.input, args.database, args.out)


if __name__ == "__main__":
    main()