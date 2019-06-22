#!/usr/bin/env python 
import collections
import argparse

#usage: python ~/github/zkwu/kc16SRNA/pipeline/ChrVariationDistribution.py --input Track1_snp_test.txt  --length 10000 --out Track1_snp_distribution.txt

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.12.19"


def read_variant_file(in_file):
    """
    in_file:

    Chr snp pos
    Chr0    1   55
    Chr0    1   92
    Chr0    1   129
    Chr0    1   212
    Chr0    1   1300
    """
    ChrPositions = collections.defaultdict(list)
    ChrPosNumber = collections.defaultdict(dict)
    in_h = open(in_file, "r")
    header = in_h.readline().strip()

    for line in in_h:
        lines = line.strip().split("\t")
        Chr, Number, Pos = lines[:3]
        Number = int(Number)
        Pos = int(Pos)
        ChrPositions[Chr].append(Pos)
        ChrPosNumber[Chr][Pos] = Number
    in_h.close()
    return ChrPositions, ChrPosNumber


def calculate_snp_counts(in_file, winLength, out_file):
    ChrRegionNumber = collections.defaultdict(dict)

    winLength = int(winLength)
    ChrPositions, ChrPosNumber = read_variant_file(in_file)

    for c in ChrPositions:
        positions = ChrPositions[c]
        maxPos = max(positions)
        ### the window number
        if maxPos % winLength == 0:
            winNumber = maxPos // winLength
        else:
            winNumber = maxPos // winLength + 1

        ### iniate the dict of chr -> region -> number
        Regions = []
        for n in range(winNumber):
            region = (n * winLength, (n + 1) * winLength)
            ChrRegionNumber[c][region] = 0
            Regions.append(region)

        for pos in positions:
            if pos % winLength == 0:
                PosAssign = pos // winLength
            else:
                PosAssign = pos // winLength + 1

            assignRegion = Regions[PosAssign-1]
            number = ChrPosNumber[c][pos]
            ChrRegionNumber[c][assignRegion] += number

    ### output the file
    out_h = open(out_file, "w")
    chrs = sorted(list(ChrRegionNumber.keys()))
    for c in chrs:
        regions = ChrRegionNumber[c]
        sortedRegions = sorted(regions)
        for r in sortedRegions:
            number = ChrRegionNumber[c][r]
            start = r[0]+1
            end = r[1]
            out_h.write("%s\t%d\t%d\t%d\n" % (c, start, end, number))
    out_h.close()

def main():
    parser = argparse.ArgumentParser(description="Calculate the snp number for each window through genome.")
    parser.add_argument("-i", "--input", help="The input file.")
    parser.add_argument("-l", "--length", default=100000, help="The setted length of each window.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()

    calculate_snp_counts(args.input, args.length, args.out)

if __name__ == "__main__":
    main()
