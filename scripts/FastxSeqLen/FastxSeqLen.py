#!/usr/bin/env python
import itertools
from tinyfasta import FastaParser
import collections
import argparse
import sys

#usage: python ../../src/kc16SRNA/FastxSeqLen.py --fastx fastq --input FastaSeqLen.fastq --out Seq_count.txt
#usage: python ../../src/kc16SRNA/FastxSeqLen.py --fastx fasta --input FastaSeqLen.fasta --out Seq_count.txt

#Author: Zhikun Wu
#Date: 2018.02.08
#Function: Counter the number for each length of sequence.

def write_count(SeqCounter, out_file):
    out_h = open(out_file, 'w')
    out_h.write('Length\tCount\n')
    countNum = sorted(list(SeqCounter.keys()))
    for c in countNum:
        number = SeqCounter[c]
        out_h.write('%s\t%s\n' % (str(c), str(number)))
    out_h.close()    

def fasta_length_count(in_file, out_file):
    """
    Summary sequence length for fasta file
    """
    SeqCounter = collections.Counter()
    for record in FastaParser(in_file):
        desc = str(record.description)
        seq = str(record.sequence).strip()
        seqLength = len(seq)
        SeqCounter[seqLength] += 1 
    write_count(SeqCounter, out_file)


def fastq_length_count(in_file, out_file):
    SeqCounter = collections.Counter()
    in_h = open(in_file, "r")
    i = 0
    lines = in_h.readlines()
    for line in itertools.islice(lines, 0, None, 4):
        seq = lines[i+1].strip()
        seqLen = len(seq)
        SeqCounter[seqLen] += 1
        i += 4
    write_count(SeqCounter, out_file)   


def main(argv):
    parser = argparse.ArgumentParser(description='Counter the number for each length of sequence.')
    parser.add_argument('-f', '--fastx', help='Argument "fasta" or "fastq".')
    parser.add_argument('-i', '--input', help='The input file.')
    parser.add_argument('-o', '--out', help='The output file.')
    args = parser.parse_args(argv)
    if args.fastx == "fasta":
        fasta_length_count(args.input, args.out)
    elif args.fastx == "fastq":
        fastq_length_count(args.input, args.out)


if __name__ == '__main__':
    main(sys.argv[1:])