#!/usr/bin/env python
from tinyfasta import FastaParser
import argparse
import re
import sqlite3

#usage: python ~/github/zkwu/kc16SRNA/pipeline/unipritSeqDB.py --fasta uniprot-carbon+cycle.fasta --database uniprot-carbon.db --out uniprot-carbon_out.txt > temp

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.12.17"

def get_records(fa_file, out_file, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE GeneFunction
        (gene_id text,
        protein text,
        organism text,
        taxonomy integer,
        gene_name text);
    """)


    out_h = open(out_file, "w")
    for record in FastaParser(fa_file):
        desc = str(record.description)
        seq = str(record.sequence)
        descs = desc.lstrip(">").split()
        gene = descs[0]
        others = " ".join(descs[1:])
        match_protein = re.findall("(.*)OS=", others)
        match_OS = re.findall("OS=(.*)OX=", others)
        match_OX = re.findall("OX=(\d+) ", others)
        match_GN = re.findall("OX=\d+ (.*)PE=", others)
        protein = match_protein[0].strip()
        OS = match_OS[0].strip()
        OX = match_OX[0].strip()
        OX = int(OX)
        ### the description may not have the item "GN"
        GNs = match_GN[0].strip()
        if "GN" in GNs:
            GN = GNs.lstrip("GN=")
        else:
            GN = "None"
            print(desc)

        ### output the record with plain text
        out_h.write("%s\t%s\t%s\t%d\t%s\n" % (gene, protein, OS, OX, GN))

        ### insert the result to database
        cursor.execute("""
            INSERT INTO GeneFunction
            (gene_id, protein, 
            organism, taxonomy,
            gene_name) 
            VALUES
            (?, ?, ?, ?, ?);
        """, (gene, protein, OS, OX, GN))
        
    out_h.close()
    cursor.close()
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Get the records of uniprot sequence and convert th sqlite3 database.")
    parser.add_argument("-f", "--fasta", help="The input fasta file.")
    parser.add_argument("-o", "--out", help="The output file with plain text format.")
    parser.add_argument("-d", "--database", help="The output records with sqlite3 format.")
    args = parser.parse_args()
    get_records(args.fasta, args.out, args.database)


if __name__ == "__main__":
    main()




