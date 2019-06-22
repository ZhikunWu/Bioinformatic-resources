#!/usr/bin/env python
import collections
import argparse
# import bisect

#usage: python CommonSpecificRegions.py --file1 KY131___WCY58_snp_index_number_win_sliding_sig_cont.xls --file2 WCY1___WCY58_snp_index_number_win_sliding_sig_cont.xls --common common_regions --specific1 specific_region1 --specific2 specific_region2

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.12.12"


def get_region_position(region_file):
    """
    Get the chronosome regions.

    argvs:
    Chr Start   End
    Chr1    22800000    23040000
    Chr10   18160000    18440000

    returns:
    ChrRegions: {"Chr1": [[22800000, 23040000]], "Chr10": [[18160000, 18440000]]}
    """
    ChrRegions = collections.defaultdict(list)
    ChrPositions = collections.defaultdict(set)
    in_h = open(region_file, "r")
    header = in_h.readline().strip()
    for line in in_h:
        lines = line.strip().split("\t")
        Chr, start, end = lines[:3]
        start = int(start)
        end = int(end)
        ChrRegions[Chr].append([start, end])
        ChrPositions[Chr].add(start)
        ChrPositions[Chr].add(end)
    in_h.close()
    return ChrRegions, ChrPositions

def combine_dict_set(dict1, dict2):
    """
    Combine two dicts which value is a set.

    argvs:
    dict1 = {"Chr1":{1,2,3}}
    dict2 = {"Chr1":{2,3,4}, "Chr2":{2,3}}

    retruns:
    {'Chr1': [1, 2, 3, 4], 'Chr2': [2, 3]}
    """
    keys = list(dict1.keys()) + list(dict2.keys())
    newDict = {}
    for c in keys:
        if c in dict1:
            value1 = dict1[c]
        else:
            value1 = set()

        if c in dict2:
            value2 = dict2[c]
        else:
            value2 = set()
        
        newValue = value1 | value2
        ### sort the values
        newDict[c] = sorted(list(newValue))
    return newDict


def split_region_to_fragment(ChrRegions, ChrPositions, Chrtile):
    """
    bisect test
    bisect.bisect_left([2,5], 2) : 0
    bisect.bisect_left([2,5], 5) : 1
    bisect.bisect_right([2,5], 2) : 1
    bisect.bisect_right([2,5], 5) : 2

    argvs:
    ChrRegions:
    {'Chr1': [[3, 8],[20, 30]]}

    ChrPositions:
    {'Chr1': {2, 22}}

    returns
    Chrtile:
    {'Chr1': {(3, 8): 1, (20, 22): 1, (22, 30): 1}}
    """
    for c in ChrRegions:
        regions = ChrRegions[c]
        for region in regions:
            start, end = region

            positionsSet = []
            if c in ChrPositions:
                postions = ChrPositions[c]
                for p in postions:
                    if p <= start:
                        continue
                    elif p >= end:
                        break
                    else:
                        positionsSet.append(p)

            ### now region may chop several fragments
            if positionsSet == []:
                Chrtile[c].add(tuple(region))
            else:
                pos = sorted(list(set(region) | set(positionsSet)))
                for i in range(len(pos)-1):
                    st = pos[i]
                    ed = pos[i+1]
                    Chrtile[c].add((st, ed))

def common_and_specific_values(Values1, Values2):
    """
    argvs:
    Values1 = {(1,2), (3, 4)}
    Values2 = {(3,4), (5, 6)}

    returns:
    spe1: {(1, 2)} 
    spe2: {(5, 6)}
    com: {(3, 4)}
    """
    spe1 = Values1 - Values2
    spe2 = Values2 - Values1
    com = Values1 & Values2
    return spe1, spe2, com


def common_and_specific(Chrtile1, Chrtile2):
    Spe1 = collections.defaultdict(set)
    Spe2 = collections.defaultdict(set)
    Common = collections.defaultdict(set)

    chroms = sorted(list(set(list(Chrtile1.keys())) | set(list(Chrtile2.keys()))))
    for c in chroms:
        if c in Chrtile1 and c in Chrtile2:
            Values1 = Chrtile1[c]
            Values2 = Chrtile2[c]
            ### get values specific for 1, specific for 2 and common
            spe1, spe2, com = common_and_specific_values(Values1, Values2)
            Spe1[c] = Spe1[c] | spe1
            Spe2[c] = Spe2[c] | spe2
            Common[c] = Common[c] | com
        elif c in Chrtile1 and c not in Chrtile2:
            Values1 = Chrtile1[c]
            Spe1[c] = Values1
        elif c not in Chrtile1 and c in Chrtile2:
            Values2 = Chrtile2[c]
            Spe2[c] = Values2
    return Spe1, Spe2, Common


def write_result(Common, out_file):
    out_h = open(out_file, "w")
    out_h.write("Chr\tStart\tEnd\n")
    chrs = sorted(list(Common.keys()))
    for c in chrs:
        values = sorted(list(Common[c]))
        for v in values:
            vv = map(str, list(v))
            out_h.write("%s\t%s\n" % (c, "\t".join(vv)))
    out_h.close()


def compare_two_files(file1, file2, common_file, spefile1, spefile2):
    """
    Get the common and specific regions for two files.

    argvs:
    file1:
    Chr Start   End
    Chr1    22760000    23160000

    file2:
    Chr Start   End
    Chr1    22800000    23040000
    Chr10   18160000    18440000


    returns:
    common_file:
    Chr Start   End
    Chr1    22800000    23040000

    spefile1:
    Chr Start   End
    Chr1    22760000    22800000
    Chr1    23040000    23160000

    spefile2:
    Chr Start   End
    Chr10   18160000    18440000
    """
    Chrtile1 = collections.defaultdict(set)
    Chrtile2 = collections.defaultdict(set)

    ChrRegions1, ChrPositions1 = get_region_position(file1)
    ChrRegions2, ChrPositions2 = get_region_position(file2)
    ### combine two dicts of sets
    ChrPositions = combine_dict_set(ChrPositions1, ChrPositions2)

    ### get the fragments based on the regions and the points
    split_region_to_fragment(ChrRegions1, ChrPositions, Chrtile1)
    split_region_to_fragment(ChrRegions2, ChrPositions, Chrtile2)


    ### get the common and specific regions of two dicts
    Spe1, Spe2, Common = common_and_specific(Chrtile1, Chrtile2)

    write_result(Spe1, spefile1)
    write_result(Spe2, spefile2)
    write_result(Common, common_file)

def main():
    parser = argparse.ArgumentParser(description="Get the specific and common regions for two files.")
    parser.add_argument("-f1", "--file1", help="The input file 1.")
    parser.add_argument("-f2", "--file2", help="The input file 2.")
    parser.add_argument("-c", "--common", help="The output file with common regions.")
    parser.add_argument("-s1", "--specific1", help="The output file with specific regions for file 1.")
    parser.add_argument("-s2", "--specific2", help="The output file with specific regions for file 2.")
    args = parser.parse_args()
    compare_two_files(args.file1, args.file2, args.common, args.specific1, args.specific2)

if __name__ == "__main__":
    main()





