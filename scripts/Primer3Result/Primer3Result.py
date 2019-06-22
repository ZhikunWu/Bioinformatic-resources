#!/usr/bin/env python
import requests
import lxml
from lxml import etree
import argparse
import sys

#usage: python Primer3Result.py --url /home/wzk/Project/C100/Candidate/C100_primer_report.html --out /home/wzk/Project/C100/Candidate/C100_primer_report.xls

__author__ = "ZhikunWu"
__email__ = "598466208@qq.com"
__date__ = "2018.10.22"

def parse_primer_result(result_html, out_file):
    """
    out_file:
    Seq_id  Orientation     Start   Len     Tm      GC%     Any compl       3' compl        Primer Seq      Product Size    Seq Size        Included Size   Pair_any        Pair_3'
    A04_8228028     FORWARD 142     20      58.72   45.00   2.00    0.00    TATTGACGCAGACGATTTCC    398     603     603     3.00    0.00
    A04_8228028     REVERSE 539     21      60.10   47.62   4.00    1.00    TTGTTCATCCAGACGACTTCC
    """
    # ### parser the url
    # r = requests.get(result_html)
    # status_code = r.status_code
    # text = r.text
    # html = etree.HTML(text)

    ### parser the html file
    html = etree.parse(result_html, etree.HTMLParser())
    seq_ids = html.xpath("//p/b/a/text()")
    header =html.xpath("//table[1]/thead/tr/th/text()")
    Primers = []
    Products = []
    for i in range(2,10):
        values = html.xpath("//tbody/tr//td[%d]/text()" % i)
        Primers.append(values)
    for j in range(10,15):
        values = html.xpath("//tbody/tr//td[%d]/text()" % j)
        Products.append(values)

    PrimersLens = len(Primers[0])
    ProductsLens = len(Products[0])
    seqIDLen = len(seq_ids)
    out_h = open(out_file, "w")
    out_h.write("Seq_id\t%s\n" % "\t".join(header))
    if PrimersLens == ProductsLens * 2 and ProductsLens == seqIDLen:
        for i in range(ProductsLens):
            seq_id = seq_ids[i]
            forward = [Primers[j][i*2] for j in range(len(Primers))]
            reverse = [Primers[j][i*2 +1] for j in range(len(Primers))]
            product = [Products[j][i] for j in range(len(Products))]
            out_h.write("%s\t%s\t%s\n%s\t%s\n\n" % (seq_id, "\t".join(forward), "\t".join(product), seq_id, "\t".join(reverse)))
    else:
        print(PrimersLens)
        print(ProductsLens)
        print(seqIDLen)
        print("Please check whether the length of primers and products is identical.")
        sys.exit(1)



def main():
    parser = argparse.ArgumentParser(description="Get the batch reuslts derived from the website of primer3.")
    parser.add_argument("-u", "--url", help="The url site of result.")
    parser.add_argument("-o", "--out", help="The output file.")
    args = parser.parse_args()
    parse_primer_result(args.url, args.out)

if __name__ == "__main__":
    main()

