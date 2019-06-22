#!/usr/bin/env python
import sys

#usage: python ../AdjustDeltaValue.py M097___Ler_snp_index_sig.xls M097___Ler_snp_index_sig-1.xls

def adjust_delta_value(in_file, out_file):
    in_h = open(in_file, 'r')
    out_h = open(out_file, 'w')
    header = in_h.readline().strip()
    out_h.write('%s\n' % header)
    for line in in_h:
        line = line.strip()
        lines = line.split('\t')
        delta = float(lines[-1])
        if delta > 0.5:
            new_delta = 1 - delta
            new_delta = '%.3f' % new_delta
            new_line = '%s\t%s' % ('\t'.join(lines[:-1]), str(new_delta))
            out_h.write('%s\n' % new_line)
        else:
            out_h.write('%s\n' % line)
    in_h.close()
    out_h.close()

if __name__ == "__main__":
    adjust_delta_value(sys.argv[1], sys.argv[2])