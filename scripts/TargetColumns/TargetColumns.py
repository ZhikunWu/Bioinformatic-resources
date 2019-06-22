#!/usr/bin/env python
import argparse
import collections
import sys
import re

#usage: python ~/github/zkwu/kc16SRNA/src/kc16SRNA/TargetColumns.py --input test --number 2 --target LGC0-AB-1,LGC0-AB-2,LGC0-AB-4,LGC0-AM-1,LGC0-AM-2 --out test.out

#or

#usage: python ~/github/zkwu/kc16SRNA/src/kc16SRNA/TargetColumns.py --input test --number 2 --target '-1' --ismatch True --out test.out

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.12.11"


def matched_columns(samples, matchStr):
    matchIndex = []
    targetSamples = []
    for i in range(len(samples)):
        s = samples[i]
        match = re.findall(matchStr, s)
        if match:
            index = i
            matchIndex.append(index)
            targetSamples.append(s)
    return targetSamples, matchIndex
    

def columns_index(samples, targetStr):
    targets = targetStr.split(",")
    targets = [t.strip() for t in targets]
    try:
        sampleIndex = [samples.index(t) for t in targets]
    except ValueError:
        print("Please check that the target sample %s is in the list %s." % (targets, samples))
    return targets, sampleIndex


def get_column_values(in_file, numberThreshold, targetStr, out_file, ismatch="False"):
    """
    in_file:
    Sequence    LGC0-AB-1   LGC0-AB-2   LGC0-AB-4   LGC0-AM-1   LGC0-AM-2   LGC0-AM-4   LGC0-PL-1   LGC0-PL-2   LGC0-PL-4   LGC0-RE-1   LGC0-RE-2   LGC0-RE-4   LGC0-RU-2   LGC0-ST-1   LGC0-ST-2   LGC0-ST-4   LGC0-VA-1   LGC0-VA-2   LGC0-VA-4   LGE0-AB-1   LGE0-AB-2   LGE0-AB-4   LGE0-AM-1   LGE0-AM-2   LGE0-MI-1   LGE0-MI-2   LGE0-MI-4   LGE0-PL-1   LGE0-PL-2   LGE0-PL-4   LGE0-RE-1   LGE0-RE-4   LGE0-RU-2   LGE0-RU-4   LGE0-ST-1   LGE0-ST-2   LGE0-ST-4   LGE0-VA-1   LGE0-VA-2   LGE0-VA-4   LGE3-AB-1   LGE3-AB-2   LGE3-AB-4   LGE3-MI-1   LGE3-MI-4   LGE3-RE-1   LGE3-RE-2   LGE3-RE-4   LGE3-RU-1   LGE3-RU-2   LGE3-RU-4   LGC0-RU-1   LGE0-RE-2   LGC0-RU-4   LGE0-AM-4   LGE0-RU-1   LGE3-MI-2
    TACAAGTAAGACTAGTGTTATTCATCTTTATTAGGTTTAAAGGGTACCTAGACAGTATATCTAGCCTCAAAAGGGAACAGATTTACTAGAGTTTTATGTGAGAGGAAAATATTAGAACCA    10  3   0   24  14  6   0   1   0   1   36  22  4   1   0   0   3   0   1   1   0   0   0   21  38  11  1   0
    GACCCCACGCCGGCGCTCTCCAGTCGCGAACCGGACAAGGCTGCGAGCCGCGCAAACTTCGGAAGGCCGGCCGCCGCGATCCCTGGCCAGCGCGGGTCGCCACCTGGAGCGCACCTTAGG    2   0   9   0   1   13  0   0   8   0   17  0   0   0   0   0   0   0   0   4   0   0   6   13  0   0   0   0   0   0   0   0   0   0   0   0   10

    """
    ### the number threshold of samples with abundnace value above zero
    numberThreshold = int(numberThreshold)

    in_h = open(in_file, "r")
    out_h = open(out_file, "w")
    ### get the sample names and index
    headers = in_h.readline().strip().split("\t")
    samples = headers[1:]

    ### the targets may be exact column names or match strings
    if ismatch == "False":
        targetSample, sampleIndex = columns_index(samples, targetStr)
    elif ismatch == "True":
        targetSample, sampleIndex = matched_columns(samples, targetStr)
    else:
        print("Please make sure the parameter 'ismatch' is 'False' or 'True'.")
        sys.exit(1)


    out_h.write("%s\t%s\n" % (headers[0], "\t".join(targetSample)))

    for line in in_h:
        lines = line.strip().split("\t")
        seq = lines[0]
        
        abundance = lines[1:]
        count = 0
        targetAbundance = [abundance[i] for i in sampleIndex]
        ### the number of targets with aundance > 0
        targetAbundance = map(float, targetAbundance)
        for j in targetAbundance:
            if j > 0:
                count += 1
        
        if count >= numberThreshold:
            targets = "\t".join(map(str, targetAbundance))
            out_h.write("%s\t%s\n" % (seq, targets))
    in_h.close()
    out_h.close()



def main():
    parser = argparse.ArgumentParser(description="Get the target records based on the column names.")
    parser.add_argument("-i", "--input", help="The input file.")
    parser.add_argument("-n", "--number", help="The number threshold of samples with vlaue above zero.")
    parser.add_argument("-t", "--target", help="The target column names.")
    parser.add_argument("-m", "--ismatch", help="Math the string or the selected accurate columns.")
    # parser.add_argument("-s", "--string", help="The match string.")
    parser.add_argument("-o", "--out", help="The out file.")
    args = parser.parse_args()


    if not args.ismatch:
        get_column_values(args.input, args.number, args.target, args.out)
    else:
        get_column_values(args.input, args.number, args.target, args.out, args.ismatch)

if __name__ == "__main__":
    main()