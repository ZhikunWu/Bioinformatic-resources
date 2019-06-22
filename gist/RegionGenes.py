#!/usr/bin/env python
import sys
import collections
import argparse
import bisect
import re

#usage: python  ../../CandidateRegionGenes.py --input ZH___F2.Gstats_index.xls --gff /home/wzk/database/GENOME/rice/O_sativa_v7/all.gff3  --out ZH___F2.Gstats_index_annottaion.xls 

#Author: Zhikun Wu
#Date: 2018.02.05
#Function: Add function and GO annotation for the candidate region.

def read_candidate_region(candidate_file):
    InforRecord = collections.defaultdict()
    in_h = open(candidate_file, 'r')
    header = line.readline().strip()
    for line in in_h:
        lines = line.strip().split('\t')
        Chr, Pos = lines[:2]
        ChrPos = '%s\t%s' % (Chr, Pos)
        InforRecord[ChrPos] = line
    in_h.close()
    return header, InforRecord

def get_gene_from_gff(gff_file):
    """
    Chr1    MSU_osa1r7      gene    2903    10817   .       +       .       ID=LOC_Os01g01010;Name=LOC_Os01g01010;Note=TBC%20domain%20containing%20protein%2C%
    Chr1    MSU_osa1r7      mRNA    2903    10817   .       +       .       ID=LOC_Os01g01010.1;Name=LOC_Os01g01010.1;Parent=LOC_Os01g01010
    """
    ChrPosGene = collections.defaultdict(dict)
    in_h = open(gff_file, 'r')
    for line in in_h:
        line = line.strip()
        if line.startswith('#') or line == '':
            continue
        else:
            lines = line.split('\t')
            Chr = lines[0]
            Type, Start, End = lines[2:5]
            Strand = lines[6]
            feature = lines[8]
            if Type == 'gene':
                ID = re.findall('GeneID:(\w.*);Name', feature)
                Gene = ID[0]
                PosInfor = '%s\t%s\t%s' % (Start, End, Strand)
                ChrPosGene[Chr][PosInfor] = Gene
    in_h.close()
    return ChrPosGene


def candidate_gene(candidate_file, gff_file, out_file):
    """
    Chr     Start   End     Delta_index     G_Stats
    Chr1    20300000        20800000        0.693   0.646
    Chr1    20400000        20900000        0.693   0.646
    """
    ChrPosGene = get_gene_from_gff(gff_file)
    in_h = open(candidate_file, 'r')
    out_h = open(out_file, 'w')
    header = in_h.readline().strip()
    for line in in_h:
        line = line.strip()
        lines = line.split('\t')
        Chr, qStart, qEnd = lines[0:3]
        qStart = int(qStart)
        qEnd = int(qEnd)
        try:
            PosGene = ChrPosGene[Chr]
            for k in PosGene:
                Start, End, Strand = k.split('\t')
                Start = int(Start)
                End = int(End)
                region = [qStart, qEnd]
                left_index = bisect.bisect(region, Start)
                right_index = bisect.bisect(region, End)
                if left_index == 1 and right_index == 1:
                    Gene = PosGene[k]
                    position = 'In'
                    out_h.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (line, position, Gene, Start, End, Strand))
                elif (left_index != 1 and right_index == 1) or (left_index == 1 and right_index != 1):
                    Gene = PosGene[k]
                    position = 'Overlap'
                    out_h.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (line, position, Gene, Start, End, Strand))
        except KeyError:
            print('Please check whether the chromosome name of gff file %s is identical to the input file %s.' % (gff_file, candidate_file))
    in_h.close()
    out_h.close()

def main(argv):
    parser = argparse.ArgumentParser('Add function and GO annotation for the candidate region.')
    parser.add_argument('-i', '--input', help='The input file.')
    parser.add_argument('-g', '--gff', help='The input gff3 file.')
    parser.add_argument('-o', '--out', help='The output file.')
    args = parser.parse_args(argv)
    candidate_gene(args.input, args.gff, args.out)

if __name__ == '__main__':
    main(sys.argv[1:])