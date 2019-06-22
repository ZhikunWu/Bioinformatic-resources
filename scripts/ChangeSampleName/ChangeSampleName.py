#!/usr/bin/env python
import argparse
import sys
import os

#usage: python ChangeSampleName.py --indir test/ --outdir test_out --split .

__author__ = "Zhikun Wu"
__date__ = "2018.10.12"
__email__ = "598466208@qq.com"

Samples = {
    "ZW": "AB",
    "TB": "RE",
    "TF": "RE",
    "YD": "VA",
    "TP": "PL",
    "YS": "AM",
    "FB": "ST",
    "CR": "MI",
    "LW": "RU"
}

Species = {
    "LSS": "LSE",
    "LSP": "LSC",
    "LGS": "LGE",
    "LGP": "LGC",
    "HS": "HSE",
    "HSG": "HGE"
}

def is_dir_exist(indir):
    if not os.path.exists(indir):
        os.makedirs(indir)
    if not indir.endswith("/"):
        indir += "/"
    return indir

def rename_for_dir(indir, splitStr, outdir):
    """
    name:
    LSS3-YD-3.R1.fq.gz
    LSS3-YD-3.R2.fq.gz
    """
    indir = is_dir_exist(indir)
    outdir = is_dir_exist(outdir)
    files = os.listdir(indir)
    for f in files:
        ### split the name to prefix and suffix
        parts = f.split(splitStr)
        prefix = parts[0]
        suffix = ".".join(parts[1:])
        names = prefix.split("-")
        species, sample, number = names
        if sample in Samples:
            resample = Samples[sample]
        else:
            print("Please check whether the sample name %s exists." % sample)
        speName = species[:-1]
        speNum = species[-1]
        if speName in Species:
            respecies = Species[speName]
        else:
            print("Please check whether the species name %s exists." % speName)
        newName = respecies + speNum + "-" + resample + "-" + number + splitStr  + suffix
        ### change name
        inName = indir + f
        outName = outdir + newName

        cmd = "cp %s %s" % (inName, outName)
        print(cmd)
        os.system(cmd)

def main():
    parser = argparse.ArgumentParser(description="Change the names in targte directory to another directory.")
    parser.add_argument("-i", "--indir", help="The input directory.")
    parser.add_argument("-s", "--split", help="The split for prefix and suffix, such as '.' or '_'.")
    parser.add_argument("-o", "--outdir", help="The output directory.")
    args = parser.parse_args()
    rename_for_dir(args.indir, args.split, args.outdir)

if __name__ == "__main__":
    main()


