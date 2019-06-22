#!/usr/bin/env python
import collections
import argparse
import numpy as np

#usage: python ../../C022/MergeNumber.py --files M097___Ler_snp_index_win.xls,M110___Ler_snp_index_win.xls --percentile 0.99 --out merge_out

__author__ = 'Zhikun Wu'
__email__ = '598466208@qq.com'
__date__ = '2018.04.25'

def get_sig_record(delta_win, percent):
    NumberRecord = collections.defaultdict(list)
    SigRecord = []
    SigNumber = {}
    percent = float(percent)
    in_h = open(delta_win, 'r')
    header = in_h.readline().strip()
    NumList = []
    for line in in_h:
        line = line.strip()
        lines = line.split('\t')
        number = int(lines[3])
        NumList.append(number)
        NumberRecord[number].append(line)
    in_h.close()
    percentThr = int(percent * 100)
    NumThreshold = np.percentile(NumList, percentThr)
    for k in NumberRecord:
        if k >= NumThreshold:
            record = NumberRecord[k]
            # SigRecord is a two level list
            SigRecord.append(record)
    for r in SigRecord:
        for rr in r:
            rrr = rr.split('\t')
            Chr, Start, End, Number = rrr[:4]
            Infor = '\t'.join(rrr[:3])
            SigNumber[Infor] = Number
    return SigNumber

def merge_sig_number(file_string, percent, out_file):
    files = file_string.split(',')
    out_h = open(out_file, 'w')
    MergOut = []
    if len(files) == 2:
        file1, file2 = files
        fbase1 = file1.split('/')[-1]
        fbase2 = file2.split('/')[-1]
        out_h.write('Chr\tStart\tEnd\t%s\t%s\n' % (fbase1, fbase2))
        SigNumber1 = get_sig_record(file1, percent)
        SigNumber2 = get_sig_record(file2, percent)
        for s in SigNumber1:
            if s in SigNumber2:
                n1 = SigNumber1[s]
                n2 = SigNumber2[s]
                MergOut.append('%s\t%s\t%s' % (s, n1, n2))
        out_h.write('%s\n' % '\n'.join(sorted(MergOut)))
    out_h.close()

def main():
    parser = argparse.ArgumentParser(description='Merge files with significant number.')
    parser.add_argument('-f', '--files', help='The input files which are separated with comma.')
    parser.add_argument('-p', '--percentile', default=0.99, help='The threshold of the percentile.')
    parser.add_argument('-o', '--out', help='The output file.')
    args =parser.parse_args()
    merge_sig_number(args.files, args.percentile, args.out)

if __name__ == '__main__':
    main()

