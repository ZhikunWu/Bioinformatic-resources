#!/usr/bin/env python
import tinyfasta
import os
import argparse

#usage: python /home/wzk/github/Manuals/script/SplitGenome2Chrs/SplitGenome2Chrs.py --fasta Brapa_sequence_v3.0_chr.fasta --outdir chrs

__author__ = "Zhikun Wu"
__date__ = "2018.10.22"
__email__ = "598466208@qq.com"

def detect_dir(indir):
    if not os.path.exists(indir):
        os.makedirs(indir)
    if not indir.endswith("/"):
        indir += "/"
    return indir


def split_genome_to_chrs(fa_file, outdir):
    for record in tinyfasta.FastaParser(fa_file):
        desc = str(record.description).strip()
        desc = desc.lstrip(">")
        seq = str(record.sequence).strip()
        
        outdir = detect_dir(outdir)
        infile = outdir + desc
        in_h = open(infile, "w")
        in_h.write(">%s\n%s\n" % (desc, seq))
        in_h.close()

def main():
    parser = argparse.ArgumentParser(description="Split the genome to chrmosomes.")
    parser.add_argument("-f", "--fasta", help="The genome with fasta format.")
    parser.add_argument("-o", "--outdir", help="The out directory.")
    args = parser.parse_args()
    split_genome_to_chrs(args.fasta, args.outdir)

if __name__ == "__main__":
    main()

