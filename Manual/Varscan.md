
## Varscan

### [VarScan User's Manual](http://varscan.sourceforge.net/using-varscan.html)

### [VarScan FAQ](http://varscan.sourceforge.net/support-faq.html#error-resetting-file)

```

$ java -jar ~/anaconda3/envs/WGS/bin/VarScan.jar 
VarScan v2.3

USAGE: java -jar VarScan.jar [COMMAND] [OPTIONS] 

COMMANDS:
	pileup2snp		Identify SNPs from a pileup file
	pileup2indel		Identify indels a pileup file
	pileup2cns		Call consensus and variants from a pileup file
	mpileup2snp		Identify SNPs from an mpileup file
	mpileup2indel		Identify indels an mpileup file
	mpileup2cns		Call consensus and variants from an mpileup file

	somatic			Call germline/somatic variants from tumor-normal pileups
	copynumber			Determine relative tumor copy number from tumor-normal pileups
	readcounts		Obtain read counts for a list of variants from a pileup file

	filter			Filter SNPs by coverage, frequency, p-value, etc.
	somaticFilter		Filter somatic variants for clusters/indels
	fpfilter		Apply the false-positive filter

	processSomatic		Isolate Germline/LOH/Somatic calls from output
	copyCaller		GC-adjust and process copy number changes from VarScan copynumber output
	compare			Compare two lists of positions/variants
	limit			Restrict pileup/snps/indels to ROI positions

```

```
$ java -jar ~/anaconda3/envs/WGS/bin/VarScan.jar  somatic --help
USAGE: VarScan somatic [normal_pileup] [tumor_pileup] [Opt: output] OPTIONS
	normal_pileup - The SAMtools pileup file for Normal
	tumor_pileup - The SAMtools pileup file for Tumor
	output - Output base name for SNP and indel output

OPTIONS:
	--output-snp - Output file for SNP calls [output.snp]
	--output-indel - Output file for indel calls [output.indel]
	--min-coverage - Minimum coverage in normal and tumor to call variant [8]
	--min-coverage-normal - Minimum coverage in normal to call somatic [8]
	--min-coverage-tumor - Minimum coverage in tumor to call somatic [6]
	--min-var-freq - Minimum variant frequency to call a heterozygote [0.10]
	--min-freq-for-hom	Minimum frequency to call homozygote [0.75]
	--normal-purity - Estimated purity (non-tumor content) of normal sample [1.00]
	--tumor-purity - Estimated purity (tumor content) of tumor sample [1.00]
	--p-value - P-value threshold to call a heterozygote [0.99]
	--somatic-p-value - P-value threshold to call a somatic site [0.05]
	--strand-filter - If set to 1, removes variants with >90% strand bias [0]
	--validation - If set to 1, outputs all compared positions even if non-variant
	--output-vcf - If set to 1, output VCF instead of VarScan native format

```

### samtools mpileup
```
$ samtools mpileup

Usage: samtools mpileup [options] in1.bam [in2.bam [...]]

Input options:
  -6, --illumina1.3+      quality is in the Illumina-1.3+ encoding
  -A, --count-orphans     do not discard anomalous read pairs
  -b, --bam-list FILE     list of input BAM filenames, one per line
  -B, --no-BAQ            disable BAQ (per-Base Alignment Quality)
  -C, --adjust-MQ INT     adjust mapping quality; recommended:50, disable:0 [0]
  -d, --max-depth INT     max per-file depth; avoids excessive memory usage [8000]
  -E, --redo-BAQ          recalculate BAQ on the fly, ignore existing BQs
  -f, --fasta-ref FILE    faidx indexed reference sequence file
  -G, --exclude-RG FILE   exclude read groups listed in FILE
  -l, --positions FILE    skip unlisted positions (chr pos) or regions (BED)
  -q, --min-MQ INT        skip alignments with mapQ smaller than INT [0]
  -Q, --min-BQ INT        skip bases with baseQ/BAQ smaller than INT [13]
  -r, --region REG        region in which pileup is generated
  -R, --ignore-RG         ignore RG tags (one BAM = one sample)
  --rf, --incl-flags STR|INT  required flags: skip reads with mask bits unset []
  --ff, --excl-flags STR|INT  filter flags: skip reads with mask bits set
                                            [UNMAP,SECONDARY,QCFAIL,DUP]
  -x, --ignore-overlaps   disable read-pair overlap detection

Output options:
  -o, --output FILE       write output to FILE [standard output]
  -O, --output-BP         output base positions on reads
  -s, --output-MQ         output mapping quality
      --output-QNAME      output read names
  -a                      output all positions (including zero depth)
  -a -a (or -aa)          output absolutely all positions, including unused ref. sequences

Generic options:
      --input-fmt-option OPT[=VAL]
               Specify a single input file format option in the form
               of OPTION or OPTION=VALUE
      --reference FILE
               Reference sequence FASTA FILE [null]

Note that using "samtools mpileup" to generate BCF or VCF files is now
deprecated.  To output these formats, please use "bcftools mpileup" instead.
```


#### get mpileup file
```
samtools mpileup -f /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa M625-0/M625-0.bqsr.bam > M625-0/M625-0.bqsr.mpileup

```


#### varscan calling somatic variants
```
$ java -jar ~/anaconda3/envs/WGS/bin/VarScan.jar  somatic  M625-1/M625-1.bqsr.mpileup  M625-0/M625-0.bqsr.mpileup M625_varscan.vcf --output-snp sample.snp --output-indel sample.indel --output-vcf 1
Normal Pileup: M625-1/M625-1.bqsr.mpileup
Tumor Pileup: M625-0/M625-0.bqsr.mpileup
Min coverage:	8x for Normal, 6x for Tumor
Min reads2:	2
Min strands2:	1
Min var freq:	0.2
Min freq for hom:	0.75
Normal purity:	1.0
Tumor purity:	1.0
Min avg qual:	15
P-value thresh:	0.99
Somatic p-value:	0.05

Not resetting normal file because KI270385.1 < KI270539.1
Not resetting normal file because KI270385.1 < KI270539.1


2932461495 positions in tumor
2932446151 positions shared in normal
2745075215 had sufficient coverage for comparison
2739761956 were called Reference
0 were mixed SNP-indel calls and filtered
3314993 were called Germline
1081426 were called LOH
825762 were called Somatic
91078 were called Unknown
0 were called Variant

```



#### mpileup tumor and normal bam to one file

```
samtools mpileup -q 10 -f hg19.fasta -B normal.bam tumor.bam > normal-tumor.pileup

java -XX:ParallelGCThreads=16 -Xmx16g -jar /usr/local/packages/VarScan/2.3.6/VarScan.jar somatic normal-tumor.pileup sample.out --output-vcf 1 --mpileup 1
```


### germline variants
```
samtools mpileup -f ref bamfile.bam > output_mpileup

java -Xmx6g -Djava.io.tmpdir=temp -jar ~/VarScan_2_3_2/VarScan.v2.3.2.jar
mpileup2snp output_mpileup \
--min-coverage 4 \
--min-reads2 4 \
--min-avg-qual 20 \
--min-var-freq 0.05 \
--p-value 0.05 \
--output-vcf 1 > output_varscan_snp.vcf

java -Xmx6g -Djava.io.tmpdir=temp -jar ~/VarScan_2_3_2/VarScan.v2.3.2.jar
mpileup2indel output_mpileup \
--min-coverage 4 \
--min-reads2 4 \
--min-avg-qual 20 \
--min-var-freq 0.05 \
--p-value 0.05 \
--output-vcf 1 > output_varscan_indel.vcf
```