# -*-coding:utf-8-*-
from __future__ import division
import random
import collections
import sys

#usage: python /home/wzk/get_top_kegg.py sig_UP_genes.xls KEGG.sig_UP/sig_UP_genes_kegg.xls sig_UP_genes_fc.xls
def median(l):
	l = sorted(l)
	if len(l)%2 ==1:
		return l[len(l/2)]
	else:
		#if l[len(l)/2 -1] >= l[len(l)/2] :
		#	return l[len(l)/2 -1]
		#else:
		#	return l[len(l)/2]
		return (l[len(l)/2 -1] + l[len(l)/2])/2
		
def average(l):
	return float(sum(l)/len(l))
	
def get_fc_hash(in_handle): #sig_UP_genes.xls
	gene_fc =  collections.defaultdict()
	for line in in_handle:
		if line.strip().startswith("Geneid"):
			continue
		else:
			lines = line.strip().split("\t")
			gene = lines[0]
			fc = lines[-5]
			if gene:
				gene_fc[gene] = fc
	return gene_fc
	

def main():
	in_h = open(sys.argv[1],'r')
	get_gene_fc = get_fc_hash(in_h)
	in_h.close()
	in_handle = open(sys.argv[2],'r')
	out_handle = open(sys.argv[3],'w')
	for line in in_handle:
		lines = line.strip().split("\t")
		term = lines[0]
		genes = lines[7]
		if term == "Term":
			continue
			out_handle.write("%s\t%s\n" % (line,"logFC"))
		else:
			all_genes = genes.split("|")
			fc_vs = []
			for g in all_genes:
				fc_v = get_gene_fc[g]
				fc_vs.append(fc_v)	
			fc_vs_value = map(float, fc_vs)
			fc_ave = average(fc_vs_value)
			out_handle.write("%s\t%.3f\n" % (line.strip(),fc_ave))
			
			
if __name__ == "__main__":
	main()
	
