#!/usr/bin/env python
from multiprocessing import Pool
import os
import argparse


def check_out_dir(out_dir):
    if os.path.exists(out_dir):
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
    else:
        os.makedirs(out_dir)
    if not out_dir.endswith("/"):
        out_dir += "/"
    return out_dir

def download_file(file, out_dir):
    fileBase = os.path.basename(file)
    out_dir = check_out_dir(out_dir)
    newFile = out_dir + fileBase
    cmd = "wget %s -O %s" % (file, newFile)
    os.system(cmd)

def download_bacterial_genome_batch(file, threads, out_dir):
    files = []
    in_h = open(file, "r")
    for line in in_h:
        files.append(line.strip())
    in_h.close()
    ### mutiple threads
    threads = int(threads)
    print("@Start to download the genome.")
    pool = Pool(threads)
    for i in files:
        result = pool.apply_async(download_file, (i, out_dir))
    pool.close()
    pool.join()
    if result.successful():
        print("Successfully download the taget genomes in file %s." % file)

def main():
    parser = argparse.ArgumentParser(description="Download the genomes.")
    parser.add_argument("-f", "--file", help="The input file containing the url of target genome.")
    parser.add_argument("-t", "--threads", help="The cpu numbers used.")
    parser.add_argument("-o", "--outdir", help="The output directory.")
    args = parser.parse_args()
    download_bacterial_genome_batch(args.file, args.threads, args.outdir)

if __name__ == "__main__":
    main()