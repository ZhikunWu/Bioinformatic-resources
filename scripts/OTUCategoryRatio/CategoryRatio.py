#!/usr/bin/env python
from __future__ import division
import collections
import numpy
import sys
import argparse

#usage: python  CategoryRatio.py --otu otu_table.txt --number 3 --out otu_table_category.txt

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.05.17"

def category_ratio(otu_file, number, out_file):
    SampleList = collections.defaultdict(lambda: collections.defaultdict(list))
    STDList = collections.defaultdict(lambda: collections.defaultdict(list))
    number = int(number)
    in_h = open(otu_file, 'r')
    out_h = open(out_file, 'w')
    out_h.write("Group\tRatio\tValue\tSTDEV\n")
    headers = in_h.readline().strip().split("\t")
    samples = (len(headers) - 1) // number
    # for j in range(samples):
    #     sub_names = headers[(i*3+2):((i+1)*3+2)]

    for line in in_h:
        line = line.strip()
        if line.startswith("#"):
            continue
        else:
            lines = line.split("\t")
            OTU = lines[0]
            total = float(lines[1])
            for i in range(samples):
                ave_list = lines[(i*3+2):((i+1)*3+2)]
                ave_list = [float(s) for s in ave_list]
                cat_ratio = sum(ave_list) / number / total
                if total < 10:
                    SampleList["10"][i].append(cat_ratio)
                    STDList["10"][i].append(cat_ratio)
                elif total >=10 and total < 20:
                    SampleList["20"][i].append(cat_ratio)
                    STDList["20"][i].append(cat_ratio)
                elif total >= 20 and total < 50:
                    SampleList["50"][i].append(cat_ratio)
                    STDList["50"][i].append(cat_ratio)
                elif total >= 50 and total < 100:
                    SampleList["100"][i].append(cat_ratio)
                    STDList["100"][i].append(cat_ratio)
                elif total >= 100 and  total < 500:
                    SampleList["500"][i].append(cat_ratio)
                    STDList["500"][i].append(cat_ratio)
                elif total >= 500 and total < 1000:
                    SampleList["1000"][i].append(cat_ratio)
                    STDList["1000"][i].append(cat_ratio)
                elif total >= 1000 and total < 5000:
                    SampleList["5000"][i].append(cat_ratio)
                    STDList["5000"][i].append(cat_ratio)
                elif total >= 5000:
                    SampleList[">5000"][i].append(cat_ratio)
                    STDList[">5000"][i].append(cat_ratio)
    in_h.close()
    for s in SampleList:
        for j in SampleList[s]:
            values = SampleList[s][j]
            ave = numpy.mean(values)
            std = numpy.std(values)
            if j == 0:
                k = '0.005'
            elif j == 1:
                k = '0.01'
            elif j == 2:
                k = '0.05'
            elif j == 3:
                k = '0.1'
            elif j == 4:
                k = '0.2'
            elif j == 5:
                k = '0.3'
            elif j == 6:
                k = '0.4'
            elif j == 7:
                k = '0.5'
            out_h.write("%s\t%s\t%s\t%s\n" % (s, k, ave, std))

def main():
    parser = argparse.ArgumentParser(description="Get the category ratio for OTU table.")
    parser.add_argument("-t", "--otu", help="The input OTU table.")
    parser.add_argument("-n", "--number", help="The number of repliaction.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()
    category_ratio(args.otu, args.number, args.out)
            
if __name__ == "__main__":
    main()



