#!/usr/bin/env python
import os
import collections
import sys
import argparse


__author__ = "Zhikun Wu"
__date__ = "2018.09.13"
__email__ = "598466208@qq.com"

#usage: python CombineDirFiles.py --indir1 dir1 --indir2 dir2 --outdir outdir

def get_list_files(indir):
    if os.path.isdir(indir):
        files = os.listdir(indir)
        return files
    else:
        print("Please check whether the %s is a directory." % indir)
        sys.exit(1)

def add_slash(indir):
    if not indir.endswith("/"):
        indir += "/"
    return indir
    
def combine_dir_files(indir1, indir2, outdir):
    indir1 = add_slash(indir1)
    indir2 = add_slash(indir2)
    outdir = add_slash(outdir)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    files1 = get_list_files(indir1)
    files2 = get_list_files(indir2)
    common = list(set(files1) & set(files2))
    for c in common:
        infile1 = indir1 + c
        infile2 = indir2 + c
        outfile = outdir + c
        cmd = "zcat %s %s | gzip > %s" % (infile1, infile2, outfile)
        os.system(cmd)

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
    parser = argparse.ArgumentParser(description="combine two file with same names in two dirs to one file.")
    parser.add_argument("-i", "--indir1", help="The input directory 1.")
    parser.add_argument("-j", "--indir2", help="The input directory 2.")
    parser.add_argument("-o", "--outdir", help="The output directory.")
    parser.add_argument("-s", "--stats", help="The stats for the reads and bases of the fastq file.")
    args = parser.parse_args()
    combine_dir_files(args.indir1, args.indir2, args.outdir)
    # dir_file_reads(args.outdir, args.stats)

if __name__ == "__main__":
    main()

