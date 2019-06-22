#!/usr/bin/env python

import itertools
import sys

def cut_fastq(fq, out_file, length, position="start"):
    """
    Cut the given length for the fastq sequence and quality.

    argv:
    @MIG.2578489 R1 UMI:ACTTCTGGTAGCCAGGGC:3
    ACTTCTGGATGCTATCTGGTTAGCCAGGGCGTGTCTCGGGCTCGGTCCTTTCTGCGGGAGGAAAGTGCTTCCCCGCCGGGCTGGGCAGCGCCCTGTGCGGCAGGTGGGCGACGTGGGGGACCGGCTAGGCCCCGGGCTCGGGGGGACTTTG
    +
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    
    cut_fastq("test", "test-1", 21)

    retrun:
    @MIG.2578489 R1 UMI:ACTTCTGGTAGCCAGGGC:3
    AGCCAGGGCGTGTCTCGGGCTCGGTCCTTTCTGCGGGAGGAAAGTGCTTCCCCGCCGGGCTGGGCAGCGCCCTGTGCGGCAGGTGGGCGACGTGGGGGACCGGCTAGGCCCCGGGCTCGGGGGGACTTTG
    +
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


    cut_fastq("test", "test-1", 19, "end")

    retrun:
    @MIG.2578489 R1 UMI:ACTTCTGGTAGCCAGGGC:3
    ACTTCTGGATGCTATCTGGTTAGCCAGGGCGTGTCTCGGGCTCGGTCCTTTCTGCGGGAGGAAAGTGCTTCCCCGCCGGGCTGGGCAGCGCCCTGTGCGGCAGGTGGGCGACGTGGGGGACCGGCTAGGCCC
    +
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    """
    length = int(length)
    in_h = open(fq, "r")
    out_h = open(out_file, "w")
    lines = in_h.readlines()
    i = 0
    for line in itertools.islice(lines, 0, None, 4):
        desc = line.strip()
        seq = lines[i+1].strip()
        qual = lines[i+3].strip()
        if position == "start":
            seq = seq[length:]
            qual = qual[length:]
        elif position == "end":
            seq = seq[:-length]
            qual = qual[:-length]
        else:
            print("Please make sure that the parameter 'position' should be 'start' or 'end'.")
            sys.exit(1)
        out_h.write("%s\n%s\n+\n%s\n" % (desc, seq, qual))
        i += 4
    in_h.close()
    out_h.close()