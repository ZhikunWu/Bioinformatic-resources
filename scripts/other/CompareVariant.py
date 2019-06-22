#!/usr/bin/env python
from __future__ import division
import argparse
import re

#usage: python ../CompareVariant.py --vcf ../bulk_compare/T01___T02_snp_index.vcf --index T01___T02_compare_pre_index --out T01___T02_compare_index.xls --threshold 0.5 --redNum 1

#Author: Zhikun Wu
#Email: 598466208@qq.com
#Date: 2018.3.8
#Function: Get the read coverage for reference and alternative alleles for the vcf file.

def alt_value(sample_value, AD_index):
    """
    It is just for two alleles
    sample value examle:
    0/1:2,12:14:99:498,0,310
    """
    if sample_value == './.' or sample_value == '':
        return ['NA', 'NA']
    else:
        values = sample_value.split(':')
        if len(values) > AD_index and values[AD_index] != '':
            # GT, AD, DP, GQ, PL = values
            # GT, AD = values[0], values[1]
            # ADs = AD.split(',')
            ADs = values[AD_index].split(',')
            ref, alt = ADs[0], ADs[1]
            ref_alt = ref + '_' + alt
            if int(alt) == 0 and int(ref) == 0:
                return ['NA', 'NA']
            else:
                alt_ratio = int(alt) / (int(ref) + int(alt))
                alt_ratio = '%.3f' % alt_ratio
                return [str(alt_ratio), ref_alt]
        else:
            return ['NA', 'NA']

def get_variant(vcf_file, pre_file, out_file, threshold=0.5, readNum=5):
    threshold = float(threshold)
    readNum = int(readNum)
    in_h = open(vcf_file, 'r')
    pre_h = open(pre_file, 'w')
    out_h = open(out_file, 'w')
    for line in in_h:
        line = line.strip()
        if line.startswith('##'):
            continue
        elif line.startswith('#'):
            headers = line.split('\t')
            names = [s.split('.')[0] for s in headers[9:]]
            sample_head = [n + '_ratio' + '\t' + n + '_reads' for n in names]
            pre_h.write('Chr\tPos\tRef\tAlt\t%s\tDelta_index\n' % '\t'.join(sample_head))
            out_h.write('Chr\tPos\tRef\tAlt\t%s\tDelta_index\n' % '\t'.join(sample_head))
        else:
            lines = line.split('\t')
            Chr, Pos, Id, Ref, Alt, Qual, Filter, Info, Format = lines[:9]
            Formats = Format.split(':')
            #select the feature 'AD', which mean reference and alterbative allele reads
            # print(Formats)
            print(line)
            if 'AD' in Formats:
                AD_index = Formats.index('AD')
                altLen = len(Alt.split(','))
                samples = lines[9:]
                Samples = [s.split('.')[0] for s in samples]
                if float(Qual) >= 10 and altLen == 1: #Filter == 'PASS'
                    #fetch the maf and reads value for each sample
                    sample_stat = ['\t'.join(alt_value(S, AD_index)) for S in Samples]
                    ratios = [alt_value(S, AD_index)[0] for S in Samples]
                    sample_stat_string = '\t'.join(sample_stat)
                    if not re.findall('NA', sample_stat_string):
                        if ratios[0] == ratios[1] and (float(ratios[0]) == 1 or float(ratios[0]) == 0):
                            continue
                        else:
                            # print(sample_stat_string)
                            delt_index = abs(float(ratios[0]) - float(ratios[1]))
                            delt_index = '%.3f' % delt_index
                            reads = [s.split('\t')[1] for s in (sample_stat)]
                            total_reads = [sum(map(int, r.split('_'))) for r in reads]
                            pre_h.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (Chr, Pos, Ref, Alt, sample_stat_string, str(delt_index)))
                            ###extract the record whose total length for each sample >= 5
                            threshold_reads = [s  for s in total_reads if int(s) >= readNum] # if int(s) >= 1
                            if len(threshold_reads) == len(total_reads):
                                # if (float(delt_index) > threshold):
                                nor = float(ratios[0])
                                mut = float(ratios[1])
                                if mut > 0.4 and mut < 0.6 and float(delt_index) > threshold:
                                    out_h.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (Chr, Pos, Ref, Alt, sample_stat_string, str(delt_index)))

def main():
    parser = argparse.ArgumentParser(description='Get the ratio of reference allele and reads numer for each sample.')
    parser.add_argument('-v', '--vcf', help='The input vcf file.')
    parser.add_argument('-d', '--index', help='The output file without filting of index.')
    parser.add_argument('-o', '--out', help='The output file.')
    parser.add_argument('-t', '--threshold', default=0.5, help='The threshold for Delta_index')
    parser.add_argument('-r', '--readNum', default=5, help='The threshold for total reads number of two samples.')
    args = parser.parse_args()
    get_variant(args.vcf, args.index, args.out, args.threshold, args.readNum)


if __name__ == '__main__':
    main()
