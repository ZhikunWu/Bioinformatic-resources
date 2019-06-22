#!/usr/bin/env python

import collections
import re
import argparse
import sys

#usage: python ../../CompareEditing.py --names Model_Stem_17_4__Model_Stem_17_5__Model_Stem_17_6___Model_16_4__Model_16_5__Model_16_6 --files Model_16_4/Model_16_4.editingSites.Alu.gvf,Model_16_5/Model_16_5.editingSites.Alu.gvf,Model_16_6/Model_16_6.editingSites.Alu.gvf,Model_Stem_17_4/Model_Stem_17_4.editingSites.Alu.gvf,Model_Stem_17_5/Model_Stem_17_5.editingSites.Alu.gvf,Model_Stem_17_6/Model_Stem_17_6.editingSites.Alu.gvf --out out

#Author: Zhikun Wu
#Email: wuzhikun86@163.com
#Date: 2018.01.24
#Function: Get the record thich is special to group1 or group2.

def parse_gvf(gvf_file):
    ChrPosRecords = collections.defaultdict()
    in_h = open(gvf_file, 'r')
    header = in_h.readline()
    for line in in_h:
        line = line.strip()
        lines = line.split('\t')
        Chr = lines[3]
        Pos, Ref, Alt = lines[7:10]
        # Chr_pos = '%s\t%s\t%s\t%s' % (Chr, Pos, Ref, Alt)
        Chr_pos = '\t'.join(lines[:10])
        A, C, G, T = lines[-7:-3]
        ratio = lines[-1]
        ChrPosRecords[Chr_pos] = '%s_%s_%s_%s_%s' % (A, C, G, T, ratio)
    in_h.close()
    return ChrPosRecords

def common_keys(mutiple_dicts_list):
    """
    >>> a = [{1: '455', 2: 'dfdsdd', 'df':'feeewe'}, {2: 'dfd', 'df':'fewer'}]
    >>> common_keys(a)
    [2, 'df']
    """
    CommonKeys = []
    dict_number = len(mutiple_dicts_list)
    keys = [list(d.keys()) for d in mutiple_dicts_list]
    all_keys = []
    for k in keys:
        all_keys.extend(k)
    uniq_key = list(set(all_keys))
    for u in uniq_key:
        u_number = all_keys.count(u)
        if u_number == dict_number:
            CommonKeys.append(u)
    return CommonKeys
    

def compare_gvf(group_name, group_files, out_file, sig_file):
    """
    argv:
        group_name: 
            sample:
                Model_Stem_17_4__Model_Stem_17_5__Model_Stem_17_6___Model_16_4__Model_16_5__Model_16_6
        group_files:
            sample:
                Model_16_4/Model_16_4.editingSites.Alu.gvf,Model_16_5/Model_16_5.editingSites.Alu.gvf,Model_16_6/Model_16_6.editingSites.Alu.gvf,Model_Stem_17_4/Model_Stem_17_4.editingSites.Alu.gvf,Model_Stem_17_5/Model_Stem_17_5.editingSites.Alu.gvf,Model_Stem_17_6/Model_Stem_17_6.editingSites.Alu.gvf
        out_file 
    """
    files = group_files.split(',')
    files = [f.strip() for f in files]
    groups = group_name.split('___')
    samples1 = groups[0].split('__')
    samples2 = groups[1].split('__')
    samples = samples1 + samples2
    LenSamples = collections.defaultdict(list)
    name_length = [len(s) for s in samples]
    for k,v in zip(name_length, samples):
        LenSamples[k].append(v)
    decreasing_len = sorted(list(LenSamples.keys()), reverse=True)
    ### get the file name for corresponding sample name
    SampleFile = collections.defaultdict()
    for d in decreasing_len:
        ss = LenSamples[d]
        for i in range(len(ss)):
            for f in files:
                match_file = re.findall(ss[i], f)
                if len(match_file) == 0:
                    continue
                else:
                    SampleFile[ss[i]] = f
                    break
    group1_dicts = []
    ### buil the dict sample_name -> record_dict
    SampleFileDict = collections.defaultdict()
    for s in samples1:
        try:
            s_file = SampleFile[s]
            s_dict = parse_gvf(s_file)
            group1_dicts.append(s_dict)
            SampleFileDict[s] = s_dict
        except KeyError:
            print('It did not find the corresponding file name for this sample %s, Please check it.' % s)
    group2_dicts = []
    for s in samples2:
        try:
            s_file = SampleFile[s]
            s_dict = parse_gvf(s_file)
            group2_dicts.append(s_dict)
            SampleFileDict[s] = s_dict
        except KeyError:
            print('It did not find the corresponding file name for this sample %s, Please check it.' % s)
    group1_common_keys = common_keys(group1_dicts)
    group2_common_keys = common_keys(group2_dicts)
    group1_special = list(set(group1_common_keys) - set(group2_common_keys))
    group2_special = list(set(group2_common_keys) - set(group1_common_keys))
    out_h = open(out_file, 'w')
    samples1_header = ['%s(A_C_G_T_editingRatio)' % s for s in samples1]
    samples2_header = ['%s(A_C_G_T_editingRatio)' % s for s in samples2]
    out_h.write('Gene_ID\tName\tSEGMENT\tCHROM\tGENE_START\tGENE_STOP\tVAR_ID\tVAR_POS\tREF\tALT\t%s\t%s\n' % ('\t'.join(samples1_header), '\t'.join(samples2_header)))
    sig_h = open(sig_file, 'w')
    sig_h.write('Gene_ID\tName\tSEGMENT\tCHROM\tGENE_START\tGENE_STOP\tVAR_ID\tVAR_POS\tREF\tALT\t%s\t%s\n' % ('\t'.join(samples1_header), '\t'.join(samples2_header)))    
    for g in group1_special:
        try:
            record = []
            for s in samples1:
                s_dict = SampleFileDict[s]
                r = s_dict[g]
                record.append(r)
            count1 = 0
            for s in samples2:
                s_dict = SampleFileDict[s]
                if g in s_dict:
                    r = s_dict[g]
                else:
                    r = '0_0_0_0_0'
                    count1 += 1
                record.append(r)
            if count1 == len(samples2):
                sig_h.write('%s\t%s\n' % (g, '\t'.join(record)))
            out_h.write('%s\t%s\n' % (g, '\t'.join(record)))
        except KeyError:
            print('Please check whether the sample %s is in dict SampleFileDict or the record key %s is in dict s_dict' % (s, g))
    for g in group2_special:
        try:
            record = []
            count2 = 0
            for s in samples1:
                s_dict = SampleFileDict[s]
                if g in s_dict:
                    r = s_dict[g]
                else:
                    r = '0_0_0_0_0'
                    count2 += 1
                record.append(r)
            for s in samples2:
                s_dict = SampleFileDict[s]
                r = s_dict[g]
                record.append(r)
            if count2 == len(samples1):
                sig_h.write('%s\t%s\n' % (g, '\t'.join(record)))
            out_h.write('%s\t%s\n' % (g, '\t'.join(record)))
        except KeyError:
            print('Please check whether the sample %s is in dict SampleFileDict or the record key %s is in dict s_dict' % (s, g))
    out_h.close()
    sig_h.close()


def main(argv):
    parser = argparse.ArgumentParser(description='Get the record thich is special to group1 or group2.')
    parser.add_argument('-n', '--names', help='The samples names which are separated with "___" between groups and "__" between samples within each group.')
    parser.add_argument('-f', '--files', help='The files for all samples which are separated with ",".')
    parser.add_argument('-o', '--out', help='The output file.')
    parser.add_argument('-s', '--significant', help='The significant out file.')
    args = parser.parse_args(argv)
    compare_gvf(args.names, args.files, args.out, args.significant)

if __name__ == '__main__':
    main(sys.argv[1:])

