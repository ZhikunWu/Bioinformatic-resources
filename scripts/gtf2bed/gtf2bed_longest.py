#!/usr/bin/env python3
import os 
import sys
import collections
import re
import optparse

'''
Convert the gene annotation file with '.gtf' format to the '.bed' format, and just output the longest transcript for each  gene
'''

#usage: python gtf2bed_longest.py --gtf Homo_sapiens.GRCh38.gtf  --bed Homo_sapiens.GRCh38.bed

def parse_gtf(gtf_file):
	GeneTrans = collections.defaultdict(set)
	TransFeature = collections.defaultdict(dict)
	gtf_h = open(gtf_file, 'r')
	for line in gtf_h:
		lines = line.strip().split("\t")
		Chr = lines[0]
		#Type: 'exon', 'CDS', 'start_codon', 'end_codon'
		Type, Start, End = lines[2:5]
		Strand = lines[6]
		Feature = lines[8]
		gene_id, trans_id, exon_num, gene_name = Feature.split(";")[:-1]
		Gene = re.match(r'gene:(\w+)', gene_id.split()[-1].strip('"')).group(1)
		Trans = re.match(r'transcript:(\w+)', trans_id.split()[-1].strip('"')).group(1)
		GeneTrans[Gene].add(Trans)
		St_ed = '%s_%s' % (Start, End)
		TransFeature[Trans]['Chr'] = Chr
		TransFeature[Trans]['Strand'] = Strand
		if Type == 'exon':
			if 'exon' not in TransFeature[Trans].keys():
				TransFeature[Trans]['exon'] = St_ed
			else:
				TransFeature[Trans]['exon'] +=  '__' + St_ed
		elif Type == 'CDS':
			if 'CDS' not in TransFeature[Trans].keys():
				TransFeature[Trans]['CDS'] = St_ed
			else:
				TransFeature[Trans]['CDS'] += '__' + St_ed
	gtf_h.close()
	return GeneTrans, TransFeature
	#print(GeneTrans, TransFeature)

def longest_exon(exon_string):
	'''The exons string format is ex1start_ex1end__ex2start_ex2end, and it is end with "__", and return the sum of each exon. '''
	'''test: exon_string = '57706629_57708714__57711984_57714536', result: 4639 57706628 57714536 2 2086,2553, 0,5355, '''
	exons = exon_string.split('__')
	lengths = [int(e.split('_')[1]) - int(e.split('_')[0]) + 1  for e in exons]
	sum_len = sum(lengths)
	all_exons = [[e.split('_')[0], e.split('_')[1]] for e in exons]
	exon_num = len(all_exons)
	exon_start = [e[0] for e in all_exons]
	exon_end = [e[1] for e in all_exons]
	#the start position should minus one base then converting the gtf to bed format
	Start_min = str(min(map(int,exon_start)) - 1)
	End_max = max(exon_end) 
	#build the index of exon start position based on the length value
	sorted_exon_start = sorted(exon_start)
	indexs = [sorted_exon_start.index(s) for s in sorted_exon_start]
	each_len = ','.join(map(str, [int(exon_end[i]) - int(exon_start[i]) + 1 for i in indexs])) + ','
	each_distance = ','.join(map(str, [int(exon_start[i]) - int(exon_start[0]) for i in indexs])) + ','
	#return the sum of all exon length, start, end position, exon number, exon length and exon position relativate to first exon
	return sum_len, Start_min, End_max, exon_num, each_len, each_distance

def add_lens2trans(trans_hash):
	'''Add the sum of exon length to coresponding transcript which build with a hash (two level hash) with trans_id as key'''
	trans = trans_hash.keys()
	for t in trans:
		sum_len = longest_exon(trans_hash[t]['exon'])[0]
		trans_hash[t]['length'] = sum_len
	return trans_hash

def convert_bed(gtf_file,bed_file):
	GeneLongestTrans = collections.defaultdict()
	GeneTrans, TransFeature = parse_gtf(gtf_file)
	NewTransFeature = add_lens2trans(TransFeature)
	Genes = GeneTrans.keys()
	#build the hash with gene to transcript with longest exon
	for g in Genes:
		#convert set to list
		all_trans = list(GeneTrans[g])
		try:
			all_length = [NewTransFeature[a]['length'] for a in all_trans]
		except:
			print('Pleash check the transcript id for gene %s, it cannot get the sum of exon length for this transcript.' % g)
		#get the index of transcript with max exon length
		max_index = all_length.index(max(all_length))
		longest_trans = all_trans[max_index]
		GeneLongestTrans[g] = longest_trans
	#output the longest transcript with bed format
	LongestTrans = GeneLongestTrans.values()
	temp_file = bed_file+'temp'
	bed_h = open(temp_file,'w')
	for t in LongestTrans:
		CHR = NewTransFeature[t]['Chr']
		STRAND = NewTransFeature[t]['Strand']
		if 'CDS' in NewTransFeature[t].keys():
			sum_len, Start_min, End_max, exon_num, each_len, each_distance = longest_exon(NewTransFeature[t]['exon'])
			cds_sum_len, cds_Start_min, cds_End_max, cds_exon_num, cds_each_len, cds_each_distance = longest_exon(NewTransFeature[t]['CDS'])
		else:
			sum_len, Start_min, End_max, exon_num, each_len, each_distance = longest_exon(NewTransFeature[t]['exon'])
			cds_Start_min = Start_min
			cds_End_max = End_max
		bed_h.write('%s\t%s\t%s\ttranscript:%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (CHR, Start_min, End_max, t, '0', STRAND, cds_Start_min, cds_End_max, '0', exon_num, each_len, each_distance))
	bed_h.close()

	cmd1 = 'sort -k 1,1 -k 2,2n %s > %s' % (temp_file, bed_file)
	cmd2 = 'rm %s' % temp_file
	os.system(cmd1)
	os.system(cmd2)

def main():
	parser = optparse.OptionParser(description='Convert the gtf file to bed file with the longest transcript.')
	parser.add_option('-g', '--gtf', dest='gtf', help='The input file with gtf format.')
	parser.add_option('-b', '--bed', dest='bed', help='The output file with bed format, and just the longest transcript for each gene.')
	(options, args) = parser.parse_args()
	convert_bed(options.gtf, options.bed)

if __name__ == '__main__':
	main()
