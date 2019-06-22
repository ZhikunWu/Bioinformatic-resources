#!/usr/bin/env python

import sys
import argparse
import os

try:
    import commands
except ModuleNotFoundError:
    import subprocess as commands

#usage: python SpeciesKegg.py --species species_abbr.txt --directory species_kegg_dir
#note: firstly you should install kg using command 'pip install kg' (https://github.com/endrebak/kg)

#Author: Zhikun Wu
#Date: 2018.01.04
#Function: Get the entrez id of gene and corresponding kegg pathway based on species name.

def species_entrezgene_kegg(species_file, file_dir):
    """
    species file:
    hsa Homo sapiens (human)
    mmu Mus musculus (mouse)
    """
    if not file_dir.endswith('/'):
        file_dir = file_dir + '/'
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    in_h = open(species_file, 'r')
    for line in in_h:
        species = line.strip().split('\t')[0]
        cmd = 'kg -s %s -d  >  %s%s_gene_kegg.xls' % (species, file_dir, species)
        (status, output) = commands.getstatusoutput(cmd)
        if status != 0:
            print(output)
            print('We do not find the record for species %s when using the tool kg (https://github.com/endrebak/kg), please install kg firstly by "pip install kg".' % species)
    in_h.close()

def main(argv):
    parser = argparse.ArgumentParser(description='Get the entrez id of gene and corresponding kegg pathway based on species name.')
    parser.add_argument('-s', '--species', help='The input file containing species name.')
    parser.add_argument('-d', '--directory', help='The output directory.')
    args = parser.parse_args(argv)
    species_entrezgene_kegg(args.species, args.directory)

if __name__ == '__main__':
    main(sys.argv[1:])