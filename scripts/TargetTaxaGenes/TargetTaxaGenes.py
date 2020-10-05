#!/usr/bin/env python
import collections
import argparse

#usage: python TargetTaxaGenes.py --gene /home/wzk/Project/C128/NCyc/representive.faa.annotation.xls  --taxonomy /home/wzk/Project/C128/NR/representive.faa.diamond_taxonomy_species.txt --out representive.faa.diamond_taxonomy_species_NCyc.txt

def get_NCyc_gene(gene_file):
    Genes = {}
    in_h = open(gene_file, "r")
    header = in_h.readline()
    for line in in_h:
        lines = line.strip().split("\t")
        gene = lines[0]
        target = lines[1]
        Genes[gene] = target
    in_h.close()
    return Genes

def taxonomy_gene(gene_file, taxonomy_file, out_file):
    Genes = get_NCyc_gene(gene_file)
    TaxaGenes = collections.defaultdict(set)
    in_h = open(taxonomy_file, "r")
    for line in in_h:
        lines = line.strip().split("\t")
        gene = lines[0]
        taxa = lines[-1]
        if gene in Genes:
            target = Genes[gene]
            TaxaGenes[taxa].add(target)
    in_h.close()
    out_h = open(out_file, "w")
    for t in TaxaGenes:
        genes = TaxaGenes[t]
        sortGenes = sorted(list(genes))
        out_h.write("%s\t%s\n" % (t, "|".join(sortGenes)))
    out_h.close()

def main():
    parser = argparse.ArgumentParser(description="Get the genes of the taxonomy.")
    parser.add_argument("-g", "--gene", help="The file contain genes.")
    parser.add_argument("-t", "--taxonomy", help="The file contain gene and taxonomy.")
    parser.add_argument("-o","--out", help="The output file.")
    args = parser.parse_args()
    taxonomy_gene(args.gene, args.taxonomy, args.out)

if __name__ == "__main__":
    main()

