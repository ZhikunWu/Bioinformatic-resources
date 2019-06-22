#!/usr/bin/env python
import bisect
import argparse
import collections

#usage: python SeqLensDistribute.py --input representive_gene_length.txt --minLen 100 --maxLen 1000 --step 100  --out representive_gene_length_hist.txt

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.08.06"

def length_distribution(length_file, minLen, maxLen, step, out_file):
    """
    length_file:
    Length  Count
    100 1
    101 1
    102 678
    103 2
    104 2
    105 742
    106 4


    Test:
    List: [0, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1000]
    length: 100
    leftIndex, rightIndex: 1, 1

    List: [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    length: 100
    leftIndex, rightIndex: 1, 2

    List: [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    length: 14124
    leftIndex, rightIndex: 11, 11
    """
    ### Set min length, max length and step
    RegionCount = collections.Counter()
    minLen = int(minLen)
    maxLen = int(maxLen)
    step = int(step)
    Lists = []
    if minLen != 0:
        Lists.append(0)
    for i in range(minLen, maxLen, step):
        Lists.append(i)
    Lists.append(maxLen)
    ### max index for the list
    MaxIndex = len(Lists) - 1
    ### Parse the input length count file
    in_h = open(length_file, "r")
    header = in_h.readline()
    for line in in_h:
        lines = line.strip().split("\t")
        length, count = lines
        length = int(length)
        count = int(count)
        leftIndex = bisect.bisect_left(Lists, length)
        rightIndex = bisect.bisect_right(Lists, length)
        ### It is based on the left index
        if leftIndex > MaxIndex:
            assignLength = ">" + str(Lists[MaxIndex])
        else:
            assignLength = Lists[leftIndex]
        RegionCount[assignLength] += count
    ### output the file
    out_h = open(out_file, "w")
    out_h.write("Region\tCount\tLength\n")
    for i in range(1, len(Lists)):
        try:
            Count = RegionCount[Lists[i]]
            if i == 1:
                region = "0" + "-" + str(Lists[i])
                init = Lists[i] - step
                out_h.write("%s\t%d\t%d\n" % (region, Count, init))
            else:
                region = str(Lists[i-1] + 1) + "-" + str(Lists[i])
                out_h.write("%s\t%d\t%d\n" % (region, Count, Lists[i-1]))
        except KeyError:
            print("Please chech whether the length cut %d is in the given list." % Lists[i])
    keys = map(str, list(RegionCount.keys()))
    for k in keys:
        if k.startswith(">"):
            Count = RegionCount[k]
            out_h.write("%s\t%d\t%d\n" % (k, Count, maxLen))
    out_h.close()

def main():
    parser = argparse.ArgumentParser(description="Get the distribution for sequence length.")
    parser.add_argument("-i", "--input", help="The input file.")
    parser.add_argument("-n", "--minLen", help="The min length given.")
    parser.add_argument("-x", "--maxLen", help="The max length given.")
    parser.add_argument("-s", "--step", help="The step for seqeunce length.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()
    length_distribution(args.input, args.minLen, args.maxLen, args.step, args.out)

if __name__ == "__main__":
    main()


