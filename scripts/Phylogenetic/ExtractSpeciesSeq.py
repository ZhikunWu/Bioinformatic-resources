#!/usr/bin/env python 
from tinyfasta import FastaParser
import argparse
import re

#usage: python  ExtractSpeciesSeq.py  --fasta SILVA_Greengene_16SrRNA_dereplication_taxas_species.fasta --level genus  --name Acinetobacter --out Acinetobacter.fasta

__author__ = "Zhikun Wu"
__date__ = "2018.09.10"
_email__ = "598466208@qq.com"

def get_genus_sequence(taxa_fa, level, name, out_file):
    Species = {}
    ### taxa level
    level = level.lower()
    if level == "genus":
        starts = "g__"
    elif level == "family":
        starts = "f__"
    elif level == "order":
        starts = "o__"
    elif level == "class":
        starts = "c__"
    elif level == "phylum":
        starts = "p__"
    ### parse the input fasta file
    out_h = open(out_file, "w")
    for record in FastaParser(taxa_fa):
        seq = str(record.sequence)
        desc = str(record.description)
        descs = desc.split("\t")
        taxa = descs[-1]
        taxas = taxa.split(";")
        taxas = [t.strip() for t in taxas]
        genus = ""
        species = ""
        for t in taxas:
            if t.startswith(starts):
                tt = t.lstrip(starts)
                if tt == name:
                    genus = taxas[-2].lstrip("g__")
                    species = taxas[-1].lstrip("s__").strip("'")
                    ### filt the species contain A-Z, 0-9, _ and -
                    match1 = re.findall("[A-Z\d_-]", species)
                    genusSpecies = '%s_%s' % (genus, species)
                    ### get one uniq seqeunce for each species
                    if genusSpecies not in Species and not match1:
                        Species[genusSpecies] = 1
                        out_h.write(">%s %s\n%s\n" % (genus, species, seq))
    out_h.close()

def main():
    parser = argparse.ArgumentParser(description="Get the taxa and sequence for the given level and name.")
    parser.add_argument("-f", "--fasta", help="The input fasta containing the taxa and sequence.")
    parser.add_argument("-l", "--level", help="The taxa level, such as phylum, class, order, family, genus and species.")
    parser.add_argument("-n", "--name", help="The name of the given taxa level.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()
    get_genus_sequence(args.fasta, args.level, args.name, args.out)

if __name__ == "__main__":
    main()



