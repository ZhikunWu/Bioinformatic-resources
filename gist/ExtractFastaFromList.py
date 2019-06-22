#!/usr/bin/env python
from tinyfasta import FastaParser
import sys

def get_target_seq(fa_file, seq_list, out_fa):
    """
    Extract fasta sequence based on the description list
    and a reference fasta sequence
    """
    Seqs = {}
    with open(seq_list, "r") as in_h:
        for line in in_h:
            line = line.strip()
            if line.startswith(">"):
                line = line.lstrip(">")
            Seqs[line] = 1
    ### read fasta file
    out_h = open(out_fa, "w")
    for record in FastaParser(fa_file):
        desc = str(record.description)
        desc = desc.lstrip(">")
        seq = str(record.sequence)
        if desc in Seqs:
            out_h.write(">%s\n%s\n" % (desc, seq))
    out_h.close()


if __name__ == "__main__":
    get_target_seq(sys.argv[1], sys.argv[2], sys.argv[3])

    