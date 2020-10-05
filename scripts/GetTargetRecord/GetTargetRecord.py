#!/usr/bin/env python
import sys
import argparse

#usage: python GetTargetRecord.py --record Merged.coverage.xls --target gene --column Target --out gene_coverage

__author__ = "Zhikun Wu"
__date__ = "2018.10.29"
__email__ = "598466208@qq.com"


def get_target_records(cov_file, col_name):
    """
    cov_file:
    Target  J1-08   J2-08   J3-08   J4-08   J5-08   J6-08   J7-08   J8-08   J9-08
    Gene000092      4.738030        0       0       0.575183        2.062612        0       0       0       0
    Gene000096      8.291553        5.287974        2.300579        9.443939        3.970686        0.909465        0.646150

    col_name:
    Target
    """
    TargetRecord = {}
    in_h = open(cov_file, "r")
    header = in_h.readline().strip()
    headers = header.split("\t")

    ### find the index of given column
    try:
        target_index = headers.index(col_name)
    except ValueError:
        print("Please check the target column name %s exists in the file %s." % (col_name, cov_file))
        sys.exit(1)

    ### deal with the record
    for line in in_h:
        line = line.strip()
        lines = line.split("\t")
        ### get the key value
        target = lines[target_index]
        TargetRecord[target] = line
    in_h.close()
    return header, TargetRecord


def target_genes(cov_file, col_name, target_gene, out_file):
    """
    target_gene:
    Gene000092
    Gene000096
    Gene000111
    """
    header, TargetRecord = get_target_records(cov_file, col_name)
    ### deal with the target gene
    target_h = open(target_gene, "r")
    out_h = open(out_file, "w")
    out_h.write("%s\n" % header)
    for line in target_h:
        lines = line.strip().split("\t")
        gene = lines[0]
        if gene in TargetRecord:
            record = TargetRecord[gene]
            out_h.write("%s\n" % record)
        else:
            print("Please check whether the gene %s is in the file %s." % (gene, cov_file))
            # sys.exit(1)
    target_h.close()
    out_h.close()

def main():
    parser = argparse.ArgumentParser(description="Get the target record.")
    parser.add_argument("-r", "--record", help="All input records.")
    parser.add_argument("-t", "--target", help="The target genes.")
    parser.add_argument("-c", "--column", help="The target column.")
    parser.add_argument("-o", "--out", help="The out file.")
    args = parser.parse_args()
    target_genes(args.record, args.column, args.target, args.out)

if __name__ == "__main__":
    main()



