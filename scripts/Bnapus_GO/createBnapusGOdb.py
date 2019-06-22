#!/usr/bin/env python
import sqlite3
import collections
import argparse
import re

#usage: python createBnapusGOdb.py --GO Brassica_napus_GO  --gff Brassica_napus.annotation_v5.gff3 --term term.txt --database BnapusGeneGO.db

__author__ = 'Zhikun Wu'
__email__ = '598466208@qq.com'
__date__ = '2018.04.28'

def create_napus_GO_db(GO_file, gff3_file, term_file, GeneGO_db):
    """
    GO_file:
    BnaC09g12820D GO:0046983
    BnaC09g12810D GO:0003922

    term_file:
    33      reproduction    biological_process      GO:0000003      0       0       0
    34      alt_id  synonym_type    alt_id  0       0       0
    35      obsolete ribosomal chaperone activity   molecular_function      GO:0000005      1       0       0

    gff3_file:
    chrC09  GazeA2  mRNA    9318184 9322857 214.6819    -   .   ID=BnaC09g12820D;Name=BnaC09g12820D;Alias=GSBRNA2T00000001001
    chrC09  GazeA2  CDS 9322739 9322857 23.0574 -   0   Parent=BnaC09g12820D;Name=BnaC09g12820D;Alias=GSBRNA2T00000001001
    """
    conn = sqlite3.connect(GeneGO_db)
    cursor = conn.cursor()

    ### create the gene and GO table
    cursor.execute("""
        CREATE TABLE GeneGO
        (gene_name text,
        GO_id text)
    """)
    in_h = open(GO_file, 'r')
    for line in in_h:
        lines = line.strip().split()
        Gene, GO = lines
        cursor.execute("""
            INSERT INTO GeneGO
            (gene_name, GO_id)
            VALUES
            (?, ?);
        """,
        (Gene, GO))
    in_h.close()

    ### create the information table based on gff3 file.
    GeneTrans = collections.defaultdict(list)
    gff_h = open(gff3_file, 'r')
    Annotations = []
    for line in gff_h:
        line = line.strip()
        if line.startswith('#') or line == '':
            continue
        else:
            lines = line.split('\t')
            Chr = lines[0]
            Type, Start, End = lines[2:5]
            Strand = lines[6]
            Feature = lines[8]
            if Type == 'mRNA':
                Genes = re.findall('ID=(.*);?', Feature)
                Names = re.findall('Name=(.*);?', Feature)
                Alias = re.findall('Alias=(.*);?', Feature)
                # Biotypes = re.findall('biotype=(\w+);', Feature)
                # Descs = re.findall('description=(.*)\s?\[', Feature)
                Gene = Genes[0].split(';')[0]
                Symbol = Names[0].split(';')[0]
                Alia = Alias[0].split(';')[0]
                # if Biotypes == []:
                #     Biotype = 'NULL'
                # else:
                #     Biotype = Biotypes[0]
                # if Descs == []:
                #     Desc = 'NULL'
                # else:
                #     Desc = Descs[0]
                # Annotations.append((Gene, Chr, Start, End, Strand, Symbol, Biotype, Desc))
                Annotations.append((Gene, Chr, Start, End, Strand, Symbol, Alia))
            # elif Type == 'mRNA':
            #     Trans = re.findall('ID=(\w+\d+\.?\d?);?', Feature)
            #     Genes = re.findall('Parent=(\w+\d+\.?\d?);?', Feature)
            #     Names = re.findall('Name=(.*);?', Feature)
            #     Tran = Trans[0]
            #     Gene = Genes[0]
            #     Symbol = Names[0].split(';')[0]
            #     GeneTrans[Gene].append(Tran)
    gff_h.close()
    ### output the gene description to a database
    cursor.execute("""
        CREATE TABLE GeneAnno
        (gene_id text,
        chr_id text,
        start_pos integer,
        end_pos integer,
        strand text,
        symbol text,
        alias text)
    """)
    for a in Annotations:
        cursor.execute("""
            INSERT INTO GeneAnno
            (gene_id, chr_id, start_pos, end_pos, 
            strand, symbol, alias)
            VALUES
            (?, ?, ?, ?, ?, ?, ?);
        """
        , a)

    ### create the term table contain GO information
    cursor.execute("""
        CREATE TABLE GOInfor
        (GO_id text,
        GO_category text,
        GO_term text)
    """)
    term_h = open(term_file, 'r')
    for line in term_h:
        lines = line.strip().split('\t')
        description, category, GO_id = lines[1:4]
        if GO_id.startswith('GO:'):
            cursor.execute("""
                INSERT INTO GOInfor
                (GO_id, GO_category, GO_term)
                VALUES
                (?, ?, ?); """,
            (GO_id, category, description))
    term_h.close()
    cursor.close()
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Parse the gff file, gene name file and GO file to merge them to a database with separate tables.')
    parser.add_argument('-g', '--gff', help='The input gff file.')
    # parser.add_argument('-n', '--name', help='The corresponding name file.')
    parser.add_argument('-G', '--GO', help='The GO file.')
    parser.add_argument('-t', '--term', help='The GO term file.')
    parser.add_argument('-d', '--database', help='The database.')
    args = parser.parse_args()
    create_napus_GO_db(args.GO, args.gff, args.term, args.database)

if __name__ == '__main__':
    main()


