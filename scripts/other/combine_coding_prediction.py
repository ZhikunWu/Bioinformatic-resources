#!/usr/bin/env python
# -*- coding:utf-8 -*-

import collections
import os
import optparse

#usage: python combine_coding_prediction.py --cnci data/CNCI.index  --cpc data/CPC_potential.xls  --cpat data/CPAT_result  --cpatval 0.364    --coding  data/coding.xls  --noncoding data/noncoding.xls #--phylocsf data/PhyloCSF_potential.xls  --threshold 80

def is_coding(hash_file, key, gene):
	if gene in hash_file[key]:
		new_gene = gene
	else:
		new_gene = 'NA'
	return new_gene

def venn_input(NoncodingParse, venn_file):
	'''Output the file for venn plot'''
	venn_h = open(venn_file,'w')
	venn_h.write("CNCI\tCPC\tCPAT\n") #\tPhyloCSF
	CNCI_list = []
	CPC_list = []
	CPAT_list = []
	PhyloCSF_list = []
	NoncodingList = list(NoncodingParse['CNCI'].union(NoncodingParse['CPC'],  NoncodingParse['CPAT'])) #NoncodingParse['PhyloCSF'],
	for gene in NoncodingList:
		each_gene = []
		each_gene.append(is_coding(NoncodingParse, 'CNCI', gene))
		each_gene.append(is_coding(NoncodingParse, 'CPC', gene))
		each_gene.append(is_coding(NoncodingParse, 'CPAT', gene))
		# each_gene.append(is_coding(NoncodingParse, 'PhyloCSF', gene))
		venn_h.write("%s\n" % '\t'.join(each_gene))
	venn_h.close()
	
def parse_coding_file(cnci_file, cpc_file, cpat_file, cpat_threshold,  noncoding_file, coding_file): #phylocsf_file, phylocsf_threshold,
	CodingParse = collections.defaultdict(set)
	NoncodingParse = collections.defaultdict(set)
	#parse the CNCI file
	cnci_f = open(cnci_file,'r')
	cnci_f.readline()
	for line0 in cnci_f:
		trans_id = line0.strip().split('\t')[0]
		is_coding = line0.strip().split('\t')[1]
		if is_coding == 'noncoding':
			NoncodingParse['CNCI'].add(trans_id)
		elif is_coding == 'coding':
			CodingParse['CNCI'].add(trans_id)
	cnci_f.close()
	#parse the CPC file with no header
	cpc_h = open(cpc_file,'r')
	for line1 in cpc_h:
		trans_id = line1.strip().split('\t')[0]
		is_coding = line1.strip().split('\t')[2]		
		if is_coding == 'noncoding':
			NoncodingParse['CPC'].add(trans_id)
		elif is_coding == 'coding':
			CodingParse['CPC'].add(trans_id)
	cpc_h.close()
	# #parse the phylocsf file with no header
	# phylocsf_h = open(phylocsf_file,'r')
	# for line2 in phylocsf_h:
	# 	trans_id = line2.strip().split('\t')[0]
	# 	trans_id = os.path.basename(trans_id)
	# 	conservation_score = line2.strip().split('\t')[2]
	# 	if conservation_score.startswith('Failure'):
	# 		continue
	# 	if float(conservation_score) <= float(phylocsf_threshold):
	# 		NoncodingParse['PhyloCSF'].add(trans_id)
	# 	elif float(conservation_score) > float(phylocsf_threshold):
	# 		CodingParse['PhyloCSF'].add(trans_id)
	# phylocsf_h.close()
	#parse the CPAT file
	cpat_h = open(cpat_file,'r')
	cpat_h.readline()
	for line3 in cpat_h:
		trans_id = line3.strip().split('\t')[0]
		cpat_score = line3.strip().split('\t')[4]
		if float(cpat_score) <= float(cpat_threshold):
			NoncodingParse['CPAT'].add(trans_id)
		elif float(cpat_score) > float(cpat_threshold):
			CodingParse['CPAT'].add(trans_id)
	cpat_h.close()

	#output the stat that for venn plot
	venn_input(NoncodingParse, noncoding_file)
	venn_input(CodingParse, coding_file)

def main():
	parser = optparse.OptionParser(description='Combine the results from CNCI, CPC, CPAT, PhyloCSF.')
	parser.add_option('-i', '--cnci',dest='cnci',help='The result file of CNCI.')
	parser.add_option('-p','--cpc',dest='cpc',help='The result file of CPC.')
	parser.add_option('-t','--cpat',dest='cpat',help='The result file of CPAT.')
	parser.add_option('-v','--cpatval',dest='cpatval',help='The threshold for CPAT.')
	# parser.add_option('-f','--phylocsf',dest='phylocsf',help='The result file of PhyloCSF.')
	# parser.add_option('-r','--threshold',dest='threshold',help='The threshold for PhyloCSF.')
	parser.add_option('-c','--coding',dest='coding',help='The output file with coding transcript.')
	parser.add_option('-n','--noncoding',dest='noncoding',help='The output file with noncoding transcript.')
	(options, args) = parser.parse_args()
	parse_coding_file(options.cnci, options.cpc, options.cpat, options.cpatval,  options.noncoding, options.coding) #options.phylocsf, options.threshold,

if __name__ == '__main__':
	main()



