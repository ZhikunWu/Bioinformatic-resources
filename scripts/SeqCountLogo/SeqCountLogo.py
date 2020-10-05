#!/usr/bin/env python
from tinyfasta import FastaParser
import collections
import argparse
import os

#usage: python ~/github/zkwu/kc16SRNA/src/kc16SRNA/SeqCountLogo.py --fasta NCBI_accession_16SrRNA.fasta --target GTGCCAGCAGCCGCG --length 25 --out out.fa --prefix out

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.07.02"

def get_seq_count(fa_file, target_seq, length, out_fa, png_prefix):
    """
    fa_file: fasta file

    target_seq: GTGCCAGCAGCCGCG (V4 515F primer)

    length: flanking length of target_seq

    out_fa: output fasta

    png_prefix: prefix of output png
    """
    length = int(length)
    SeqCount = collections.Counter()
    target_seq = str(target_seq).strip()
    for record in FastaParser(fa_file):
        seq = str(record.sequence)
        targetLen = len(target_seq)
        target_index = seq.find(target_seq)
        if target_index != -1:
            new_seq = seq[(target_index-length) : (target_index + targetLen + length)]
            SeqCount[new_seq] += 1
    ### output target seq
    out_h = open(out_fa, "w")
    summary = 0
    for seq in SeqCount:
        count = SeqCount[seq]
        for i in range(count):
            out_h.write(">%d\n%s\n" % (summary, seq))
            summary += 1
    out_h.close()
    ### output seq log
    cmd = "seqlogo -a -S -f %s -F PNG -c -h 5 -w 35 -o %s" % \
        (out_fa, png_prefix)
    try:
        os.system(cmd)
    except:
        print("Please check whether the software seqlogo of package weblogo exist in ENV PATH.")
        os.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Get the given sequence of a fasta and output the \
        logo picture. ")
    parser.add_argument("-f", "--fasta", help="The input fatsa file.")
    parser.add_argument("-t", "--target", help="The input target sequence.")
    parser.add_argument("-l", "--length", help="The length flanking the given sequence.")
    parser.add_argument("-o", "--out", help="The output sequence.")
    parser.add_argument("-p", "--prefix", help="The output prefix of picture.")
    args = parser.parse_args()
    get_seq_count(args.fasta, args.target, args.length, args.out, args.prefix)

if __name__ == "__main__":
    main()
