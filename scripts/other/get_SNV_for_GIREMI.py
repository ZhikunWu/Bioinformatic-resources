#!/usr/bin/env python
#-*-coding:utf-8 -*-

from collections import defaultdict
from optparse import OptionParser
import sys
import os
import re

def get_vcf(vcf_file):
	'''Parse the vcf file and get the snv information.
	sort -k 1,1n -k 2,2n  293TW2_virus_SNP_filted_chr10.vcf > 293TW2_virus_SNP_filted_chr10_sorted.vcf
	
	Args:
		vcf_file (input vcf file)
	Returns:
		CHR_POS_SNV (two level dict containing chromosome -> position -> snv)
	'''
	CHR_POS_SNV = defaultdict(list)
	vcf_h = open(vcf_file, 'r')
	for line in vcf_h:
		line = line.strip()
		if line.startswith("#"):
			continue
		else:
			lines = line.split("\t")
			Chr, Pos, Id, Ref, Alt = lines[:5]
			CHR_POS_SNV[Chr].append('%s_%s_%s' % (Pos, Ref, Alt))
	return CHR_POS_SNV
	vcf_h.close()

def get_gtf(gtf_file):
	'''Parse the gtf file which was sorted for the records with only the 'exon' feature:
	awk '{if ($3 == "exon"){print $0}}' Homo_sapiens.GRCh38.gtf | sort -k 1,1n -k 4,4n > Homo_sapiens.GRCh38_exon_sorted.gtf,
	and the then get the dict: Chromosome -> Start_end

	Args: 
		gtf_file
	Returns:
		dict: Chr -> Satrt_End
	'''
	Chr_region = defaultdict(list)
	gtf_h = open(gtf_file, 'r')
	for line in gtf_h:
		lines = line.strip().split('\t')
		Chr = lines[0]
		Start, End = lines[3:5]
		Strand = lines[6]
		feature = lines[8]
		gene = re.findall('gene_name\W+(\w+\.?\d?)\W+', feature)[0]
		Chr_region[Chr].append('%s/%s/%s/%s' % (Start, End, Strand, gene))
	return Chr_region
	gtf_h.close()


def get_dbsnp(avsnp):
	'''Parse the dbsnp file which wae sorted based on the chromosome and position.
	sort -k 1,1n -k 2,2n  hg38_avsnp147_chr10.txt > hg38_avsnp147_chr10_sorted.txt

	Args:
		dbsnp_file
	Return:
		vcf_dict； Chr -> Pos_Start_Ref_Alt
	'''
	dbSNP_dict = defaultdict(list)
	avsnp_h = open(avsnp, 'r')
	for line in avsnp_h:
		lines = line.strip().split("\t")
		Chr, Start, End, Ref, Alt, snv = lines
		if Chr.startswith('chr'):
			Chr = Chr[3:]
		dbSNP_dict[Chr].append('%s_%s_%s' % (Start, Ref, Alt))
	return dbSNP_dict
	avsnp_h.close()

def main():
	parser = OptionParser(description='Get the file for GIREMI from the vcf file coupled the gtf and dbsnp information.')
	parser.add_option('-g', '--gtf', dest='gtf', help='The input file with .gtf format.')
	parser.add_option('-v', '--vcf', dest='vcf', help='The input file with .vcf format.')
	parser.add_option('-d', '--dbsnp', dest='dbsnp', help='The dbsnp file.')
	parser.add_option('-o', '--out', dest='out', help='The output file.')
	(options, args) = parser.parse_args()
	VCF_dict = get_vcf(options.vcf)
	GTF_dict = get_gtf(options.gtf)
	dbSNP_dict = get_dbsnp(options.dbsnp)
	fianl_dict = defaultdict(list)
	for k in VCF_dict.keys():
		gtf_index = 0
		dbsnp_index = 0
		if k in dbSNP_dict.keys() and k in GTF_dict.keys():
			for i in range(len(VCF_dict[k])):
				vcf_item = VCF_dict[k][i]
				vcf_start, vcf_ref, vcf_alt = vcf_item.split('_')
				snp_flag = '0'
				final_strand = '#'
				final_gene = 'Inte'

				#parse the dbsnp information and get the snp_flag values
				for j in range(dbsnp_index, len(dbSNP_dict[k])):
					snp_item = dbSNP_dict[k][j]
					snp_start, snp_ref, snp_alt = snp_item.split('_')
					if int(snp_start) > int(vcf_start):
						dbsnp_index = j
						break
					if snp_item == vcf_item:
						snp_flag = '1'
				
				#parse the gtf information and get the gene name and strand values
				for m in range(gtf_index, len(GTF_dict[k])):
					gtf_item = GTF_dict[k][m]
					print(gtf_item)
					gtf_start, gtf_end, gtf_strand, gtf_gene = gtf_item.split('/')
					if int(gtf_start) > int(vcf_start):
						gtf_index = m
						break
					if int(gtf_start) <= int(vcf_start) and int(gtf_end) >= int(vcf_start):
						final_strand = gtf_strand
						final_gene = gtf_gene
				snv_start = int(vcf_start) - 1
				snv_end = int(vcf_start)
				fianl_dict[k].append('%s\t%d\t%d\t%s\t%s\t%s' % (k, snv_start, snv_end, final_gene, snp_flag, final_strand))
	out_h = open(options.out, 'w')
	for kk in fianl_dict.keys():
		for ii in range(len(fianl_dict[kk])):
			out_h.write('%s\n' % fianl_dict[kk][ii])
	out_h.close()

if __name__ == '__main__':
	main()



