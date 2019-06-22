#!/usr/bin/env python
import gzip
from Bio import SeqIO
import argparse
import os

#usage: python ~/github/zkwu/kcMeta/pipeline/CombineDirFasta.py --indir test --out test.fasta

__author__ = "Zhikun Wu"
__date__ = "2018.09.22"
__email__ = "598466208@qq.com"


def read_fasta(fa_handle, sep):
    seqs = []
    for record in SeqIO.parse(fa_handle, "fasta"):
        seq = str(record.seq)
        seqs.append(seq)
    return sep.join(seqs)


def combine_genome_to_one(fa_file, out_handle):
    suffix = ["fa", "fna", "fasta"]
    sep = "N" * 50
    
    fa_base = os.path.basename(fa_file)
    sequence = ""
    if fa_file.endswith(".gz"):
        fa_base = fa_base.rstrip(".gz")
        if fa_base.split(".")[-1] in suffix:
            with gzip.open(fa_file, "rt") as fa_handle:
                sequence = read_fasta(fa_handle, sep)
        else:
            pass
    else:
        if fa_file.split(".")[-1] in suffix:
            with open(fa_file, "r") as fa_handle:
                sequence = read_fasta(fa_handle, sep)
        else:
            pass
    
    for s in suffix:
        if fa_base.endswith(s):
            fa_base = fa_base.rstrip("." + s)
            break

    if sequence != "":
        out_handle.write(">%s\n%s\n" % (fa_base, sequence))



def combine_dir_fasta(indir, out_file):
    out_handle = open(out_file, "w")
    files = os.listdir(indir)
    if not indir.endswith("/"):
        indir = indir + "/"
    for f in files:
        file = indir + f
        combine_genome_to_one(file, out_handle)
    out_handle.close()


def main():
    parser = argparse.ArgumentParser(description="Combine the fasta files in one directory.")
    parser.add_argument("-i", "--indir", help="The input directory.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()
    combine_dir_fasta(args.indir, args.out)

if __name__ == "__main__":
    main()

