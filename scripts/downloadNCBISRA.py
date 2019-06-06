#!/usr/bin/env python
import os
import sys
import argparse
import subprocess

#usage: python downloadNCBISRA.py --name PRJNA246220   --outdir /home/wuzhikun/github/Bioinformatic-resources/scripts

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2019.06.06"


def file_items(file):
    items = []
    in_h = open(file, "r")
    for line in in_h:
        lines = line.strip().split("\t")
        items.append(lines[0])
    in_h.close()
    return items


def download_NCBI_SRA(projectName, outdir):
    ### get project names
    if os.path.isfile(projectName):
        projects = file_items(projectName)
    elif isinstance(projectName, str):
        projects = projectName.strip().split(",")
    else:
        print("Please make sure the input project is string with one project name or projects which are separated with ',', or a file containing one project name per line.")
        sys.exit(1)
    
    ### download projects
    if not outdir.endswith("/"):
        outdir +=  "/"
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    for project in projects:
        projectFile = outdir + project + ".txt"
        cmd = "wget 'http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&rettype=runinfo&db=sra&term=%s' -O  %s" % (project, projectFile)
        # result = subprocess.getstatusoutput(cmd)
        # exit, value = result
        os.system(cmd)

        ### get just the sra data
        cleanFile = projectFile.rstrip("txt") + "clean_sra.txt"
        cmd2 = "sed '1d'  %s | cut -d ',' -f 1 > %s" % (projectFile, cleanFile)
        os.system(cmd2)



def main():
    parser = argparse.ArgumentParser(description="Download the project information based on the project name or file.")
    parser.add_argument("-n", "--name", help="The input project name or file file.")
    parser.add_argument("-o", "--outdir", help="The output directory.")
    args = parser.parse_args()
    download_NCBI_SRA(args.name, args.outdir)

if __name__ == "__main__":
    main()



