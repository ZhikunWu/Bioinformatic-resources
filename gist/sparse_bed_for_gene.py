#!/usr/bin/env python
import collections

def sparse_bed_for_gene(bed_file, out_file):
    """
    Get four columns for bed file, and get the min and max position for each gene.
    argv:
    1   3630    3759    AT1G01010   .   +   araport11   five_prime_utr  .   gene_id "AT1G01010"; transcript_id "AT1G01010.1"; gene_name "NAC001"; gene_source "araport11"; gene_biotype "protein_coding"; transcript_source "araport11"; transcript_biotype "protein_coding";
    1   3630    3913    AT1G01010   .   +   araport11   exon    .   gene_id "AT1G01010"; transcript_id "AT1G01010.1"; exon_number "1"; gene_name "NAC001"; gene_source "araport11"; gene_biotype "protein_coding"; transcript_source "araport11"; transcript_biotype "protein_coding"; exon_id "AT1G01010.1.exon1";
    1   3630    5899    AT1G01010   .   +   araport11   gene    .   gene_id "AT1G01010"; gene_name "NAC001"; gene_source "araport11"; gene_biotype "protein_coding"; transcript_id "";

    return:  
    1       3630    5630    AT1G01010
    1       6787    8666    AT1G01020
    1       11100   11100   AT1G03987
    """
    GeneChr = collections.defaultdict()
    GenePos = collections.defaultdict(list)
    in_h = open(bed_file, "r")
    for line in in_h:
        lines = line.strip().split("\t")
        Chr, Start, End, Gene = lines[:4]
        Start = int(Start)
        End = int(End)
        GeneChr[Gene] = Chr
        GenePos[Gene].append(Start)
    out_h = open(out_file, "w")
    for g in GenePos:
        postions = GenePos[g]
        start = min(postions)
        end = max(postions)
        if end > satrt:
            try:
                c = GeneChr[g]
            except:
                print("Please check the chromosome of gene %s is %s." %(g, c))
            out_h.write("%s\t%d\t%d\t%s\n" % (c, start, end, g))
