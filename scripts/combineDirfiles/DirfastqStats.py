#!/usr/bin/env python
import os
import collections
import argparse
import gzip
import itertools

#usage: python ~/github/zkwu/kc16SRNA/pipeline/DirfastqStats.py --indir raw/ --out raw_fastq_stats.xls

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.09.13"

def fastq_read_base(fastq_file):
    """
    Get the read number and base number for the fastq file.
    """
    BaseNumber = 0
    if fastq_file.strip().endswith('gz'):
        in_h = gzip.open(fastq_file, 'r')
    else:
        in_h = open(fastq_file, 'r')
    i = 0
    lines = in_h.readlines()
    seqNumber = len(lines)
    ReadNumber = int(seqNumber/4)
    for line in itertools.islice(lines, 0, None, 4):
        seq = lines[i+1].strip()
        seqLen = len(seq)
        BaseNumber += seqLen
        i += 4
    in_h.close()
    return ReadNumber, BaseNumber

def dir_file_reads(indir, out_file):
    FileReads = collections.defaultdict(list)
    files = os.listdir(indir)
    if not indir.endswith("/"):
        indir += "/"

    for f in files:
        f_base = f.split(".")[0]
        ff = indir + f
        reads, bases = fastq_read_base(ff)
        FileReads[f_base].append([reads, bases])
    
    out_h = open(out_file, "w")
    out_h.write("Sample\tReads\tBases\n")
    for f in FileReads:
        records = FileReads[f]
        reads = sum([r[0] for r in records])
        bases = sum([r[1] for r in records])
        out_h.write("%s\t%d\t%d\n" % (f, reads, bases))
    out_h.close()


def main():
    parser = argparse.ArgumentParser(description="Get the read and base stats for the fastq files of a dir.")
    parser.add_argument("-i", "--indir", help="The input directory.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()
    dir_file_reads(args.indir, args.out)

if __name__ == "__main__":
    main()



