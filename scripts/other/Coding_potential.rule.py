
rule filt_gtf:
	input:
		down = expand(IN_PATH + '/supp/novel_transcript/DEG/{group}/sig_Down_genes.xls',group=GROUPS),
		up = expand(IN_PATH + '/supp/novel_transcript/DEG/{group}/sig_UP_genes.xls',group=GROUPS),
	output:
		IN_PATH + '/supp/novel_transcript/DEG/all_sig_diff_gene.xls',
	log:
		IN_PATH + '/log/novel_transcript/DEG/filt_gtf.log',
	run:
		INPUT = '%s\t%s' % ('\t'.join(input.up)	,'\t'.join(input.down))
		cmd = 'cat %s | sort | uniq > %s' % (INPUT, output)
		os.system(cmd)

rule select_gtf:
	input:
		gene = IN_PATH + '/supp/novel_transcript/DEG/all_sig_diff_gene.xls',
		gtf = IN_PATH + '/cuffcompare/All_gtf.combined.gtf',
	output:
		IN_PATH + '/supp/coding_potential/sig_diff.gtf',
	params:	
		select_sig_diff_trans = SRC_DIR + '/select_sig_diff_trans.py',
	log:
		IN_PATH + '/log/coding_potential/select_gtf.log',
	run:
		shell('source activate kcmRNA  && python {params.select_sig_diff_trans} --input {input.gene} --gtf {input.gtf} --output {output} > {log} 2>&1')
		#/home/wzk/anaconda3/bin/tools/x86_64/faToTwoBit /home/genome/human/Homo_sapiens.GRCh38.fa /home/wzk/database/human/Homo_sapiens.GRCh38.fa.2bit


rule CNCI:
	#get CNCI.index and the .bed, .fa files for the gtf file
	input:
		gtf = IN_PATH + '/supp/coding_potential/sig_diff.gtf',
	output:
		index = IN_PATH + '/supp/coding_potential/CNCI/CNCI_index.xls',
		fasta = IN_PATH + '/supp/coding_potential/sig_diff.gtf.fa',
		bed = IN_PATH + '/supp/coding_potential/sig_diff.gtf.bed',
	threads:
		10
	params:
		CNCI = kcmRNA_BIN + '/CNCI-master/CNCI.py',
		odir = IN_PATH + '/supp/coding_potential/CNCI',
		index = IN_PATH + '/supp/coding_potential/CNCI/CNCI.index',
		REF_2bit = config['REF_2bit'],
		CNCI_type = config['CNCI_type'],
	log:
		IN_PATH + '/log/coding_potential/CNCI_fasta_bed.log',
	run:
		#it will output two additional files with suffix of .bed and .fa in the input dir
		shell('source activate kcmRNA  && python {params.CNCI} --gtf -f {input.gtf} -o {params.odir}  -d {params.REF_2bit} -p {threads} -m {params.CNCI_type} > {log} 2>&1 ')
		#python /home/soft/CNCI-master/CNCI.py --gtf -f /home/wzk/test_cufflinks/cuffcompare/CNCI_test/compared.combined-1.gtf -o /home/wzk/test_cufflinks/cuffcompare/CNCI_test/CNCI  -d /home/wzk/test_cufflinks/cuffcompare/CNCI_test/Homo_sapiens.GRCh38.fa.2bit  -p 10 -m ve
		os.system('mv %s %s' % (params.index, output.index))

rule CPAT:
	input:
		bed = IN_PATH + '/supp/coding_potential/sig_diff.gtf.bed',
	output:
		ind = IN_PATH + '/supp/coding_potential/CPAT/CPAT_result.xls',
	params:
		CPAT = kcmRNA_BIN + '/CPAT-1.2.1/bin/cpat.py',
		CPAT_tsv = config['CPAT_tsv'],
		CPAT_Rdata = config['CPAT_Rdata'],
		REF = config['REF'],
	log:
		ind = IN_PATH + '/log/coding_potential/CPAT.log',
	run:
		#python /home/wzk/software/CPAT-1.2.1/bin/cpat.py -r /home/genome/human/Homo_sapiens.GRCh38.fa -g /home/wzk/software/CPAT-1.2.1/test/broad_lincRNAs.hg19.bed  -x /home/wzk/software/CPAT-1.2.1/database/Human_Hexamer.tsv -d /home/wzk/software/CPAT-1.2.1/database/Human_logitModel.RData  -o /home/wzk/test_cufflinks/test_CPAT/CPAT_out
		shell('source activate kcmRNA  && python {params.CPAT} -r {params.REF} -g {input.bed} -x {params.CPAT_tsv} -d {params.CPAT_Rdata} -o {output.ind} > {log.ind} 2>&1 ')


rule CPC:
	input:
		fasta = IN_PATH + '/supp/coding_potential/sig_diff.gtf.fa',
	output:
		table = IN_PATH + '/supp/coding_potential/CPC/CPC_potential',
	threads:
		THREADS
	params:
		CPC_predict_local = kcmRNA_BIN + '/cpc-master/bin/run_predict_local.sh',
		odir = IN_PATH + '/supp/coding_potential/CPC',
	log:
		IN_PATH + '/log/coding_potential/CPC_predict.log',
	run:
		#/home/wzk/anaconda3/bin/tools/cpc-master/bin/run_predict_local.sh /home/wzk/KC_B20/coding_potentiata/filted_record.gtf.fasta  /home/wzk/KC_B20/coding_potential/CPC/coding_potential  /home/wzk/KC_Botential/CPC  /home/wzk/KC_B20/coding_potential/CPC/coding_potential_frame 10
		#output five files: blastx.bls blastx.feat1 blastx.table ff.fa1 ff.feat ambiguous_genes.table(in the path of running the command)
		#The output file 'table' is in the dir 'odir', it will output two file with suffix of .homo and .orf
		makefiledir(output.table)
		shell('{params.CPC_predict_local} {input.fasta} {output.table} {params.odir} {output.table} {threads} > {log} 2>&1 ')

# rule PhyloCSF:
# 	input:
# 		bed = IN_PATH + '/supp/coding_potential/sig_diff.gtf.bed',
# 	output:
# 		odir = IN_PATH + '/supp/coding_potential/PhyloCSF',
# 		file = IN_PATH + '/supp/coding_potential/PhyloCSF/PhyloCSF_conservation_score.txt',
# 	threads:
# 		10
# 	params:
# 		Parse_PhyloCSF = SRC_DIR + '/PhyloCSF_batch.py',
# 		PhyloCSF = kcmRNA_BIN + '/PhyloCSF/PhyloCSF',
# 		phast = kcmRNA_BIN + '/phast/bin/maf_parse',
# 		phastConsDatabase = config['phastConsDatabase'],
# 		phast_species = config['phast_species'] ,
# 	log:
# 		IN_PATH + '/log/coding_potential/PhyloCSF.log',
# 	run:
# 		#python ../../script/PhyloCSF.py --bed /home/wzk/KC_B20/coding_potential/sig_diff.gtf.bed --phast /home/wzk/anaconda3/bin/tools/phast --database /home/wzk/database/phastConsDatabase --csf /home/wzk/anaconda3/bin/tools/PhyloCSF --outdir /home/wzk/KC_B20/coding_potential/PhyloCSF --species /home/wzk/database/phastConsDatabase/hg38.20way.nh  --threads 20
# 		makedir(output.odir)
# 		shell('source activate kcmRNA  && python {params.Parse_PhyloCSF} --bed {input.bed} --phast {params.phast} --database {params.phastConsDatabase} --csf {params.PhyloCSF} --outdir {output.odir} --species {params.phast_species} --threads {threads} > {log} 2>&1 ')
# 		#cmd = ('rm %s' % input.bed + '_sorted')
# 		#os.system(cmd)


rule combine_coding:
	input:
		CNCI = IN_PATH + '/supp/coding_potential/CNCI/CNCI_index.xls',
		CPC = IN_PATH + '/supp/coding_potential/CPC/CPC_potential',
		CPAT = IN_PATH + '/supp/coding_potential/CPAT/CPAT_result.xls',
		# PhyloCSF = IN_PATH + '/supp/coding_potential/PhyloCSF/PhyloCSF_conservation_score.txt',
	output:
		coding = IN_PATH + '/supp/coding_potential/coding.xls',
		noncoding = IN_PATH + '/supp/coding_potential/noncoding.xls',
	params:
		combine_coding_prediction = IN_PATH + '/combine_coding_prediction.py', 
		# PhyCSF_threshold = config['PhyCSF_threshold'], 
		CPAT_threshold = config['CPAT_threshold'],
	log:
		IN_PATH + '/log/coding_potential/combind_coding.log',
	run:
		shell('source activate kcmRNA  && python {params.combine_coding_prediction} --cnci {input.CNCI} --cpc {input.CPC} --cpat {input.CPAT} --cpatval {params.CPAT_threshold} --coding {output.coding} --noncoding {output.noncoding} ') #--phylocsf {input.PhyloCSF} --threshold {params.PhyCSF_threshold} 

rule venn_plot:
	input:
		coding = IN_PATH + '/supp/coding_potential/coding.xls',
		noncoding = IN_PATH + '/supp/coding_potential/noncoding.xls',
	output:
		coding = IN_PATH + '/supp/coding_potential/coding.svg',
		noncoding = IN_PATH + '/supp/coding_potential/noncoding.svg',
		coding_png = IN_PATH + '/supp/coding_potential/coding.png',
		noncoding_png = IN_PATH + '/supp/coding_potential/noncoding.png',
	params:
		venn_4categories = IN_PATH + '/venn_3categories.R', # SCRIPT_DIR +
	log:
		IN_PATH + '/log/coding_potential/venn_plot.log',
	run:
		shell('Rscript {params.venn_4categories} {input.coding} {output.coding} svg 15 15 2.5  > {log} 2>&1')
		shell('Rscript {params.venn_4categories} {input.coding} {output.coding_png} png 3000 3000 1  >> {log} 2>&1')
		shell('Rscript {params.venn_4categories} {input.noncoding} {output.noncoding} svg 15 15 2.5  >> {log} 2>&1')
		shell('Rscript {params.venn_4categories} {input.noncoding} {output.noncoding_png} png 3000 3000 1  >> {log} 2>&1')

def open_temp(file, string):
	cpc_h = open(file,'w')
	cpc_h.write(string)
	cpc_h.close()

def phylocsf_head(in_file, out_file):
	in_h = open(str(in_file), 'r')
	out_h = open(str(out_file), 'w')
	out_h.write('Transcript_id\tScore\tOFR_start\tOFR_end\tStrand\tOFR_pep\n')
	for line in in_h:
		lines = line.strip().split("\t")
		trans_id = lines[0].split("/")[-1]
		out_h.write("%s\t%s\n" % (trans_id,'\t'.join(lines[2:])))
	in_h.close()
	out_h.close()

rule add_head1:
	input:
		cufflinks = IN_PATH + '/cufflinks/{sample}/transcripts.gtf',		
	output:
		cufflinks = IN_PATH + '/cufflinks/{sample}/transcripts.gtf.xls',
	run:
		#add head for result of cufflinks 
		#cmd1 = " sed -i '1i\Chr\tSource\tType\tStart_site\tEnd_site\tScore\tStrand\tFrame\tAttributes' %s " % input.gtf
		open_temp('cpc_temp','Chr\tSource\tType\tStart_site\tEnd_site\tScore\tStrand\tFrame\tAttributes\n')
		os.system('cat %s  %s > %s' % ('cpc_temp', input.cufflinks, output.cufflinks))	

rule add_head2:
	input:
		cpc = IN_PATH + '/supp/coding_potential/CPC/CPC_potential',
		# phylocsf = IN_PATH + '/supp/coding_potential/PhyloCSF/PhyloCSF_conservation_score.txt',
	output:
		cpc = IN_PATH + '/supp/coding_potential/CPC/CPC_potential.xls',
		# phylocsf = IN_PATH + '/supp/coding_potential/PhyloCSF/PhyloCSF_potential.xls',
	run:
		#add head for result of CPC
		open_temp('cpc_temp','Transcript_id\tLength\tCoding/Noncoding\tCoding_score\n')
		os.system('cat cpc_temp %s > %s ' % (input.cpc, output.cpc))
		os.system('rm cpc_temp')
		#add head for result of PhyloCSF
		# phylocsf_head(input.phylocsf, output.phylocsf)



rule FetchResult:
	input:
		expression = IN_PATH + '/supp/novel_transcript/expression/All_reads_counts.xls',
	output:
		expression = IN_PATH + '/result/novel_transcript/DEG/All_reads_counts.xls',
	params:
		in_dir = IN_PATH + '/supp',
		out_dir = IN_PATH + '/result',
	run:
		shell('cp {input.expression} {output.expression}')
		shell('cp -r {params.in_dir}/novel_transcript/DEG/* {params.out_dir}/novel_transcript/DEG')
		shell('cp -r {params.in_dir}/coding_potential/CNCI/*  {params.in_dir}/coding_potential/*xls {params.in_dir}/coding_potential/*png {params.in_dir}/coding_potential/*svg {params.in_dir}/coding_potential/CPAT/CPAT_result.xls {params.in_dir}/coding_potential/CPC/CPC_potential.xls {params.out_dir}/coding_potential')
		shell("echo 'cp -r {params.in_dir}/../cuffcompare/*.gtf {params.in_dir}/../cuffcompare/*.bed {params.in_dir}/../cuffcompare/mode_stat*  {params.out_dir}/novel_transcript/cuffcompare' ")
		shell('mkdir -p {params.out_dir}/novel_transcript/cuffcompare')
		shell('cp -r {params.in_dir}/../cuffcompare/*.gtf {params.in_dir}/../cuffcompare/*.bed {params.in_dir}/../cuffcompare/mode_stat*  {params.out_dir}/novel_transcript/cuffcompare')

rule FetchSample:
	input:
		cufflinks = rules.add_head1.output.cufflinks,
	output:
		cufflinks = IN_PATH + '/result/novel_transcript/cufflinks/{sample}/transcripts.gtf.xls',
	run:
		shell('cp {input.cufflinks} {output.cufflinks}')

