#!/usr/bin/env python
import sys
import random
import HTSeq
import argparse

#usage: python subsample.py --fq1 HS0-LW-2-30.R1.fq --fq2 HS0-LW-2-30.R2.fq --ratio 0.3 --out1 HS0-LW-2-30_0.3.R1.fq --out2 HS0-LW-2-30_0.3.R2.fq

#Function: randomly get the reads from the pair end fastq files for the given ratio.

def sub_fraction_reads(fq1, fq2, fraction, fq1_out, fq2_out):
    fraction = float(fraction)
    in1 = iter( HTSeq.FastqReader(fq1) )
    in2 = iter( HTSeq.FastqReader(fq2) )
    out1 = open( fq1_out, "w" )
    out2 = open( fq2_out, "w" )

    while True:
        try:
            read1 = next( in1 )
            read2 = next( in2 )
            if random.random() < fraction:
                read1.write_to_fastq_file( out1 )
                read2.write_to_fastq_file( out2 )
        except StopIteration:
           sys.exit()
    out1.close()
    out2.close()


def main():
    parser = argparse.ArgumentParser(description="Get the sub sequences for the PE fastq reads.")
    parser.add_argument("-f1", "--fq1", help="The input fastq 1.")
    parser.add_argument("-f2", "--fq2", help="The input fastq 2.")
    parser.add_argument("-r", "--ratio", help="The ratio for the sub sequence.")
    parser.add_argument("-o1", "--out1", help="The out fastq file 1.")
    parser.add_argument("-o2", "--out2", help="The out fastq file 2.")
    args = parser.parse_args()
    sub_fraction_reads(args.fq1, args.fq2, args.ratio, args.out1, args.out2)

if __name__ == "__main__":
    main()
