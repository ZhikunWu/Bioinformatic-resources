#!/usr/bin/env python
import collections
import argparse

__author__ = "Zhikun Wu"
__email__ = "598466208@qq.com"
__date__ = "2018.0917"

#usage: python Annotation2GeneGO.py --annotation /home/wzk/database/GENOME/Solanum_tuberosum/Annotation/result/Solanum_tuberosum_GeneAnno_description.xls --gene /home/wzk/database/GENOME/Solanum_tuberosum/Annotation/result/Solanum_tuberosum_gene_GO.xls --GO /home/wzk/database/GENOME/Solanum_tuberosum/Annotation/result/Solanum_tuberosum_GO_gene.xls

def get_gene_GO(annotation_file):
    """
    Gene    Chr     Start   End     Strand  Symbol  Biotype Description     uniprotAc       Refseq  pfam    interpro        eggNOG  GO(GO_term,class,description)   KEGG(KO,pathway,description)
    PGSC0003DMG400000005    1       71314568        71319702        +       None    protein_coding  Shrunken seed protein [Source:PGSC_GENE;Acc:PGSC0003DMG400000005]       M0ZFY7,Uncharacterized protein;M0ZFY5,Uncharacterized protein;M0ZFY6,Uncharacterized protein    XP_006339496.1,peroxisome biogenesis protein 16 isoform X3;XP_006339495.1,peroxisome biogenesis protein 16 isoform X1   PF08610,Peroxisomal membrane protein (Pex16)    IPR013919,Peroxisome membrane protein, Pex16    KOG4546,Peroxisomal biogenesis protein (peroxin 16);ENOG4111GEA,-       GO:0007031,biological_process,peroxisome organization;GO:0005777,cellular_component,peroxisome;GO:0005778,cellular_component,peroxisomal membrane       K13335,ko04146,Peroxisome
    """
    GeneGOS = {}
    in_h = open(annotation_file, "r")
    ### get GO index
    headers = in_h.readline().strip().split("\t")
    for i in range(len(headers)):
        if headers[i].startswith("GO"):
            GO_index = i
    ### parse the record
    for line in in_h:
        lines = line.strip().split("\t")
        gene = lines[0]
        GOS = lines[GO_index].split(";")
        GOList = [g.split(",")[0] for g in GOS]
        GeneGOS[gene] = GOList
    in_h.close()
    return GeneGOS

def out_gene_GO(annotation_file, gene_GO, GO_gene):
    """
    gene_GO:
    PGSC0003DMG400000001    GO:0016020
    PGSC0003DMG400000001    GO:0016021
    PGSC0003DMG400000001    GO:0055085
    PGSC0003DMG400000002    GO:0016020
    
    GO_gene:
    GO:0000002  PGSC0003DMG400007998    PGSC0003DMG400008143
    GO:0000014  PGSC0003DMG400026214
    """
    GOSGene = collections.defaultdict(list)
    GeneGOS = get_gene_GO(annotation_file)
    gene_h = open(gene_GO, "w")
    sortedGenes = sorted(list(GeneGOS.keys()))
    for gene in sortedGenes:
        GOS = GeneGOS[gene]
        # ### output mutiple GO per line
        # gene_h.write("%s\t%s\n" % (gene, "\t".join(GOS)))
        ### GO and genes dict
        for GO in GOS:
            if GO != "-":
                GOSGene[GO].append(gene)
                ### output one GO per line
                gene_h.write("%s\t%s\n" % (gene, GO))
    gene_h.close()
    ### output GO and genes
    GO_h = open(GO_gene, "w")
    sortedGOS = sorted(list(GOSGene.keys()))
    for GO in sortedGOS:
        genes = GOSGene[GO]
        ### output mutiple genes per line
        GO_h.write("%s\t%s\n" % (GO, "\t".join(genes)))
        # ### output one gene per line
        # for gene in genes:
        #     GO_h.write("%s\t%s\n" % (GO, gene))
    GO_h.close()

def main():
    parser = argparse.ArgumentParser(description="Output the gene to GO and GO to genes based on the annotation file.")
    parser.add_argument("-a", "--annotation", help="The input annotation file.")
    parser.add_argument("-g", "--gene", help="The output file containing the gene to GO.")
    parser.add_argument("-G", "--GO", help="The output file containing the GO to genes.")
    args = parser.parse_args()
    out_gene_GO(args.annotation, args.gene, args.GO)

if __name__ == "__main__":
    main()



