#!/usr/bin/env python
#-*-coding:utf-8 -*-
import collections
import sys
import argparse
import bisect

#usage: python LncRNANearGene.py --gtf /home/wzk/database/RNAEditor/mouse/GRCM38/Mus_musculus.GRCm38.83.gtf --noncoding /home/wzk/B78/supp/coding_potential/noncoding.xls --expression /home/wzk/B78/supp/novel_transcript/DEG/All_samples_rpkm.xls --distance 1000 --out /home/wzk/B78/supp/coding_potential/noncoding_up_down_stream.xls

#Author: Zhikun Wu
#Date: 2018.01.23



def parser_gene(gtf_file):
    """
    Get the gene information based on the gtf file.
    argv:
        gtf_file
    return:
        ChrGeneRegion (dict): Chr -> Gene -> [Start, End, Strand]
    """
    ChrGeneRegion = collections.defaultdict(dict)
    in_h = open(gtf_file, 'r')
    for line in in_h:
        line = line.strip()
        if line.startswith("#"):
            continue
        else:
            lines = line.split('\t')
            Chr = lines[0]
            Type, Start, End = lines[2:5]
            Strand = lines[6]
            Gene = lines[8].split(';')[0].split()[-1]
            if Type == 'gene':
                ChrGeneRegion[Chr][Gene] = [Start, End, Strand]
    in_h.close()
    return ChrGeneRegion

def get_common_gene(nocoding_gene):
    """
    Get the common genes that exist in all columns
    argv:
        noncodig_gene: the file containning gene without coding protential
        example:
        CNCI    CPC     CPAT
        TCONS_00039516  TCONS_00039516  TCONS_00039516
        NA      TCONS_00066075  TCONS_00066075
    return:
        Genes (list)
    """
    Genes = []
    in_h = open(nocoding_gene, 'r')
    header = in_h.readline()
    for line in in_h:
        lines = line.strip().split('\t')
        if not "NA" in lines:
            gene = lines[0]
            Genes.append(gene)
    in_h.close()
    return Genes

def gene_information(rpkm_file):
    """
    Read the rpkm  file to get the gene inforation
    argv:
        rpfm_file
        example:
        Geneid  Chr     Start   End     Strand  Length  Model_16_4      Model_16_5      Model_16_6      Model_Stem_17_4 Model_Stem_17_5 Mo
        TCONS_00000025  1       4851631 4852406 +       776     0.890004197352925       0.339913731759782       0.277410218901883       0.
        TCONS_00000101  1;1     9235031;9236099 9236060;9240383 +;+ 
    return:
        GeneInfor (dict): Chr -> Gene -> [Start, End]
    """
    GeneInfor = collections.defaultdict()
    in_h = open(rpkm_file, 'r')
    header = in_h.readline()
    for line in in_h:
        lines = line.strip().split('\t')
        Gene, Chr, Start, End, Strand = lines[:5]
        Strand = Strand.split(';')[0]
        GeneInfor[Gene] = [Chr, Start, End, Strand]
    in_h.close()
    return GeneInfor


def get_near_gene(gtf_file, nocoding_gene, rpkm_file, out_file, distance=1000):
    out_h = open(out_file, 'w')
    out_h.write('Noncoding_gene\tNoncoding_Start\tNoncoding_End\tNoncoding_Strand\tGene\tGene_Start\tGene_End\tGene_Strand\tRelationship\n')
    distance = int(distance)
    TargetGene = collections.defaultdict(dict)
    GenePair = collections.defaultdict(list)
    ChrGeneRegion = parser_gene(gtf_file)
    Genes = get_common_gene(nocoding_gene)
    GeneInfor = gene_information(rpkm_file)
    ### get the target gene and their information
    possible_genes = list(GeneInfor.keys())
    for g in Genes:
        if g in possible_genes:
            Chr, Start, End, Strand = GeneInfor[g]
            TargetGene[Chr][g] = [Start, End, Strand]
    ### compare the genes in TargetGene to ChrGeneRegion derived from gtf file
    for C in TargetGene:
        target_genes = list(TargetGene[C].keys())
        if C in ChrGeneRegion:
            objectGenes = ChrGeneRegion[C]
            for gt in target_genes:
                targetStart, targetEnd, targetStrand = TargetGene[C][gt]
                targetStart = int(targetStart)
                targetEnd = int(targetEnd)
                for go in objectGenes:
                    objectStart, objectEnd, objectStrand = ChrGeneRegion[C][go]
                    objectRegion = [int(objectStart), int(objectEnd)]
                    extendStart = int(objectStart) - distance
                    extendEnd = int(objectEnd) + distance
                    extendRegion = [extendStart, extendEnd]
                    ### compare the start and end of two genes
                    left_index = bisect.bisect(objectRegion, targetStart)
                    right_index = bisect.bisect(objectRegion, targetEnd)
                    left_extend = bisect.bisect(extendRegion, targetStart)
                    right_extend = bisect.bisect(extendRegion, targetEnd)
                    target_gene_infor = '%s\t%s\t%s\t%s' % (gt, targetStart, targetEnd, targetStrand)
                    object_gene_infor = '%s\t%s\t%s\t%s' % (go, objectStart, objectEnd, objectStrand)
                    coord = 'NA'
                    if left_index == 0 and right_index == 2:
                        # print('The gene %s from gtf file is in the noncodig gene %s, please check it.' % (go, gt))
                        coord = 'Include'
                        out_h.write('%s\t%s\t%s\n' % (target_gene_infor, object_gene_infor, coord))
                    elif left_index == 1 and right_index == 1:
                        # print('The noncodig gene %s is in the gene %s from gtf file, please check it.' % (gt, go))
                        coord = 'IN'
                        out_h.write('%s\t%s\t%s\n' % (target_gene_infor, object_gene_infor, coord))
                    elif (left_index == 0 and right_index == 1) or (left_index == 1 and right_index == 2):
                        # print('The noncoding gene %s and the gene %s from gtf file are overlaped, please check it.' % (gt, go))
                        coord = 'Overlap'
                        out_h.write('%s\t%s\t%s\n' % (target_gene_infor, object_gene_infor, coord))
                    elif (left_index == 2 and right_index == 2) or (left_index == 0 and right_index == 0):
                        if left_extend == 0 and right_extend == 1:
                            coord = 'UpStream'
                        elif left_extend == 1 and right_extend == 2:
                            coord = 'DownStream'
                    if coord == 'UpStream' or coord == 'DownStream':
                        if objectStrand == '-':
                            if coord == 'UpStream':
                                coord = 'DownStream'
                            elif coord == 'DownStream':
                                coord = 'UpStream'
                        GenePair[target_gene_infor].append("%s\t%s" % (object_gene_infor, coord))
    ### write the gene pair
    for gene in GenePair:
        object_gene = GenePair[gene]
        if len(object_gene) == 1:
            out_h.write('%s\t%s\n' % (gene, object_gene[0]))
        else:
            for i in range(len(object_gene)):
                out_h.write('%s\t%s\n' % (gene, object_gene[i]))
    out_h.close()


def main(argv):
    parser = argparse.ArgumentParser(description='Find the up or download stream genes of the noncoding genes based on the gtf file, rpkm file and the common noncoding file.')
    parser.add_argument('-e', '--expression', help='The expression file from Sample_rpkm.txt.')
    parser.add_argument('-n', '--noncoding', help='The input noncoding file.')
    parser.add_argument('-g', '--gtf', help='The annotation file with gtf format.')
    parser.add_argument('-d', '--distance', default=1000, help='The distance threshold for the noncoding gene and the up or down stream genes.')
    parser.add_argument('-o', '--out', help='The output file.')
    args = parser.parse_args(argv)
    get_near_gene(args.gtf, args.noncoding, args.expression, args.out, args.distance)

if __name__ == "__main__":
    main(sys.argv[1:])








