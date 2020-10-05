
### lastdb

```
$ lastdb --help
Usage: lastdb [options] output-name fasta-sequence-file(s)
Prepare sequences for subsequent alignment with lastal.

Main Options:
-h, --help: show all options and their default settings, and exit
-p: interpret the sequences as proteins
-R: repeat-marking options (default=10)
-c: soft-mask lowercase letters (in reference *and* query sequences)
-u: seeding scheme (default: YASS for DNA, else exact-match seeds)

Advanced Options (default settings):
-w: use initial matches starting at every w-th position in each sequence (1)
-W: use "minimum" positions in sliding windows of W consecutive positions (1)
-S: strand: 0=reverse, 1=forward, 2=both (1)
-s: volume size (unlimited)
-Q: input format: 0=fasta or fastq-ignore,
                  1=fastq-sanger, 2=fastq-solexa, 3=fastq-illumina (fasta)
-P: number of parallel threads (1)
-m: seed pattern
-a: user-defined alphabet
-i: minimum limit on initial matches per query position (0)
-b: bucket depth
-C: child table type: 0=none, 1=byte-size, 2=short-size, 3=full (0)
-x: just count sequences and letters
-v: be verbose: write messages about what lastdb is doing
-V, --version: show version information, and exit

Report bugs to: last-align (ATmark) googlegroups (dot) com
LAST home page: http://last.cbrc.jp/

```


```
$ lastdb -v -P 4 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa
lastdb: reading Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa...
lastdb: writing...
lastdb: gathering...
lastdb: sorting...
lastdb: bucketing...
lastdb: writing...
lastdb: done!

```

output files:
```
-rw-rw-r-- 1 184M Mar 21 17:02 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb.bck
-rw-rw-r-- 1    2 Mar 21 17:01 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb.des
-rw-rw-r-- 1  474 Mar 21 17:02 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb.prj
-rw-rw-r-- 1    8 Mar 21 17:01 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb.sds
-rw-rw-r-- 1    8 Mar 21 17:01 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb.ssp
-rw-rw-r-- 1 880M Mar 21 17:02 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb.suf
-rw-rw-r-- 1 238M Mar 21 17:01 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb.tis

```


### lastal
```
$ lastal
lastal: please give me a database name and sequence file(s)

Usage: lastal [options] lastdb-name fasta-sequence-file(s)
Find and align similar sequences.

Cosmetic options:
-h, --help: show all options and their default settings, and exit
-V, --version: show version information, and exit
-v: be verbose: write messages about what lastal is doing
-f: output format: TAB, MAF, BlastTab, BlastTab+ (default=MAF)
```




### picky tools

```
$ /home/Nicolas/SV/Picky-master/src/picky.pl
Please specify the command.

/home/Nicolas/SV/Picky-master/src/picky.pl <command> -h

<command> [hashFq, selectRep, callSV]
hashFq    : hash read uuids to friendly ids
lastParam : Last parameters for alignment
selectRep : select representative alignments for read
callSV    : call structural variants
xls2vcf   : convert Picky sv xls file to vcf
sam2align : convert sam to align format
preparepbs: chunk last fastq file and write pbs script for cluster submission
script    : write a bash-script for single fastq processing


      License = JACKSON LABORATORY NON-COMMERCIAL LICENSE AGREEMENT
                https://github.com/TheJacksonLaboratory/Picky/blob/master/LICENSE.md
Documentation = https://github.com/TheJacksonLaboratory/Picky/wiki
   Repository = https://github.com/TheJacksonLaboratory/Picky/

```


#### Call SV
```
$ /home/Nicolas/SV/Picky-master/src/picky.pl callSV
Please specify the prefix for output files

/home/Nicolas/SV/Picky-master/src/picky.pl callSV --in <alignFile> --fastq <fqFile> --lastpara <last parameters> [--genome <genomeFastaFile> --removehomopolymerdeletion] [--sam] [--exlucde <chromosomeToExeclude> [--exlucde <anotherChromosomeToExeclude>]]

  --oprefix STR   prefix for output files
  --fastq STR     .fastq file
  --lastpara STR  lastal parameters used
  --removehomopolymerdeletion
                  exclude DEL and INDEL possibly affected by homopolymer
  --genome STR    genome sequence in .fasta file
  --sam           flag to output .sam file
  --exclude STR   exclude SV invovling specified chromosome
                  (specify each chromosome with --exclude individually)
  --multiloci     report SVs on best alignment of multi-loci aligments
```




#### lastal alignment
```
$ time lastal -C2 -K2 -r1 -q3 -a2 -b1 -v -P 8 -Q 1 /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb  ../clean/nano_test.fastq.gz | /home/Nicolas/SV/Picky-master/src/picky.pl  selectRep --thread  8 --preload 6 > nano_test.align  2>error.log
```

#### picky call SV 
```
$  /home/Nicolas/SV/Picky-master/src/picky.pl callSV  --oprefix nano_test --fastq ../clean/nano_test.fastq --genome /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa  --sam  nano_test.align
Genome sequence fasta file is needed for homopolymer detection only.
```




## last
last-train

```
$ last-train -h
Usage: last-train [options] lastdb-name sequence-file(s)

Try to find suitable score parameters for aligning the given sequences.

Options:
  -h, --help           show this help message and exit
  -v, --verbose        show more details of intermediate steps

  Training options:
    --revsym           force reverse-complement symmetry
    --matsym           force symmetric substitution matrix
    --gapsym           force insertion/deletion symmetry
    --pid=PID          skip alignments with > PID% identity (default: 100)
    --postmask=NUMBER  skip mostly-lowercase alignments (default=1)
    --sample-number=N  number of random sequence samples (default: 500)
    --sample-length=L  length of each sample (default: 2000)

  Initial parameter options:
    -r SCORE           match score (default: 6 if Q>0, else 5)
    -q COST            mismatch cost (default: 18 if Q>0, else 5)
    -p NAME            match/mismatch score matrix
    -a COST            gap existence cost (default: 21 if Q>0, else 15)
    -b COST            gap extension cost (default: 9 if Q>0, else 3)
    -A COST            insertion existence cost
    -B COST            insertion extension cost

  Alignment options:
    -D LENGTH          query letters per random alignment (default: 1e6)
    -E EG2             maximum expected alignments per square giga
    -s STRAND          0=reverse, 1=forward, 2=both (default: 2 if DNA, else
                       1)
    -S NUMBER          score matrix applies to forward strand of: 0=reference,
                       1=query (default: 1)
    -C COUNT           omit gapless alignments in COUNT others with > score-
                       per-length
    -T NUMBER          type of alignment: 0=local, 1=overlap (default: 0)
    -m COUNT           maximum initial matches per query position (default:
                       10)
    -k STEP            use initial matches starting at every STEP-th position
                       in each query (default: 1)
    -P THREADS         number of parallel threads
    -Q NUMBER          input format: 0=fasta or fastq-ignore, 1=fastq-sanger
                       (default=fasta)

```


```
$ seqtk sample nano_test.fastq 5000 > nano_test_tain.fastq
```


```
$ last-train -Q 1  -P 10 /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb nano_test_tain.fastq  > last/parameter.txt

```

detail for output file

```
$ less  last/parameter.txt

# lastal version: 963
# maximum percent identity: 100
# scale of score parameters: 4.36661
# scale used while training: 87.3322

# lastal -j7 -S1 -P10 -Q1 /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb /tmp/tmpd0p5us57

# aligned letter pairs: 205129.3
# deletes: 10993.93568
# inserts: 3274.94465
# delOpens: 6242.84218
# insOpens: 2185.31172
# alignments: 373
# mean delete size: 1.76105
# mean insert size: 1.49862
# delOpenProb: 0.0291815
# insOpenProb: 0.010215
# delExtendProb: 0.432156
# insExtendProb: 0.332718

# delExistCost: 285
# insExistCost: 340
# delExtendCost: 73
# insExtendCost: 96

# substitution percent identity: 98.2156

# count matrix (query letters = columns, reference letters = rows):
#   A              C              G              T             
# A 57947.741986   243.0131975    402.879312194  331.51063764  
# C 204.3656891    41858.939757   145.339899     555.4589594   
# G 474.835329666  195.194999824  41544.3490353  301.375123621 
# T 213.382556501  427.867794962  164.705117004  60097.5722701 

# probability matrix (query letters = columns, reference letters = rows):
#   A              C              G              T             
# A 0.282522       0.0011848      0.00196423     0.00161627    
# C 0.000996378    0.204082       0.0007086      0.00270812    
# G 0.00231504     0.000951667    0.202548       0.00146934    
# T 0.00104034     0.00208606     0.000803014    0.293004      

# score matrix (query letters = columns, reference letters = rows):
#        A      C      G      T
# A    108   -343   -297   -347
# C   -358    135   -358   -274
# G   -283   -333    136   -327
# T   -385   -296   -378    104

```




```
$ time lastal -Q 1 -P 20  -p last/parameter.txt /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.lastdb nano_test.fastq  | last-split > last/read.maf

real	174m5.071s
user	1097m29.279s
sys	8m6.924s

```


```
$ java -jar /home/wuzhikun/anaconda3/envs/WGS/bin/picard.jar  CreateSequenceDictionary REFERENCE=/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa OUTPUT=/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.dict
```


```
$ maf-convert -f /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.dict sam -r 'ID:1\tPL:NANOPORE\tSM:nano' last/read.maf  > last/read.sam
```


```
$ sambamba view -h -S --format=bam last/read.sam > last/read.bam
```



### picky sam to align

```
$ cat nano_test.sam | /home/husong/ActiveState/ActivePerl-5.24.3.2404/perl/bin/src/picky.pl sam2align | /home/husong/ActiveState/ActivePerl-5.24.3.2404/perl/bin/src/picky.pl callSV --oprefix picky
```

output files:
```
-rw-rw-r--. 1  500 Mar 26 16:22 picky.profile.CTLC.xls
-rw-rw-r--. 1 2.0M Mar 26 16:22 picky.profile.DEL.xls
-rw-rw-r--. 1 1.9K Mar 26 16:22 picky.profile.exclude
-rw-rw-r--. 1 2.0M Mar 26 16:22 picky.profile.INDEL.xls
-rw-rw-r--. 1  17K Mar 26 16:22 picky.profile.INS.xls
-rw-rw-r--. 1  52K Mar 26 16:22 picky.profile.INV.xls
-rw-rw-r--. 1 1.2M Mar 26 16:22 picky.profile.NONE.xls
-rw-rw-r--. 1  41K Mar 26 16:22 picky.profile.TDC.xls
-rw-rw-r--. 1 3.8M Mar 26 16:22 picky.profile.TDSR.xls
-rw-rw-r--. 1  500 Mar 26 16:22 picky.profile.TTLC.xls
-rw-rw-r--. 1  33M Mar 26 16:22 picky.profile.xls
```

```
$ head picky.profile.DEL.xls
#SVType	SVChrom	SVStart	SVEnd	SVSpan	qDiff	sDiff	ReadId	ReadLen	ftotal	fid1	fid2	score_1	EG2_1	E_1	Identity_1	IdentityP_1	Mismatch_1MismatchP_1	Deletion_1	DeletionP_1	Insertion_1	InsertionP_1	qStart_1	qEnd_1	qStrand_1	qALen_1	qP_1	refId_1	refStart_1	refEnd_1	refStrand_1	refALen_1	score_2	EG2_2	E_2	Identity_2	IdentityP_2	Mismatch_2	MismatchP_2	Deletion_2	DeletionP_2	Insertion_2	InsertionP_2	qStart_2	qEnd_2	qStrand_2	qALen_2	qP_2	refId_2	refStart_2	refEnd_2	refStrand_2	refALen_2
DEL	1	97072553	158024386	60951834	-6698	60951834	b655dc0b-6298-4801-8209-180d9fec099a	9871	7	2	3	. 8664	8747	+	.	.	1	97072470	97072552	+	.	.	.	.	.	.	.	.	.	. 2049	2181	+	.	.	1	158024387	158024520	+	.
DEL	1	74700826	212408516	137707691	-10126	137707691	8b5ef0f8-9a11-430d-a047-d4b91c8908e0	14465	4	1	2	. 13207	13314	+	.	.	1	212408517	212408624	-	.	.	.	.	.	.	.	.	.	. 3188	3275	+	.	.	1	74700738	74700825	-	.
DEL	1	91087709	109835815	18748107	-2107	18748107	b6060a5c-d19d-4157-9d7a-b681549719d1	16625	10	2	3	. 4114	4722	+	.	.	1	91087098	91087708	+	.	.	.	.	.	.	.	.	.	. 2615	2856	+	.	.	1	109835816	109836062	+	.
DEL	1	212396147	223279014	10882868	-4587	10882868	16a1d09b-f75f-4842-bc60-80fae6b66f8d	13531	4	1	2	. 1855	5941	+	.	.	1	212391922	212396146	+	.	.	.	.	.	.	.	.	.	. 1354	1506	+	.	.	1	223279015	223279175	+	.
DEL	1	218668778	244126296	25457519	-789	25457519	6564a107-b74c-49be-a5c2-25b0d88aa6bc	16951	8	2	3	. 2569	2661	+	.	.	1	244126297	244126388	-	.	.	.	.	.	.	.	.	.	. 1872	2059	+	.	.	1	218668583	218668777	-	.
DEL	1	7353714	39875364	32521651	-1143	32521651	6564a107-b74c-49be-a5c2-25b0d88aa6bc	16951	8	4	5	.	. 6286	6387	+	.	.	1	39875365	39875468	-	.	.	.	.	.	.	.	.	.	. 5244	5452	+	.	.	1	7353501	7353713	-	.
DEL	1	157255433	162746207	5490775	-1234	5490775	85a081fb-9cdf-4d5e-b7ab-ede55528d4da	11976	5	4	5	.	.	. 2763	2824	+	.	.	1	157255372	157255432	+	.	.	.	.	.	.	.	.	.	. 1590	1692	+	.	.	1	162746208	162746314	+	.
DEL	1	210930911	234191819	23260909	-1948	23260909	ea08abb1-90db-4e9c-a8be-25d9031682fe	10218	7	1	2	. 1594	2182	+	.	.	1	234191820	234192429	-	.	.	.	.	.	.	.	.	.	. 234	625	+	.	.	1	210930510	210930910	-	.
DEL	1	147227110	169534489	22307380	-1007	22307380	68fe82a5-3b36-4e65-ab22-a244f7ed1768	22006	6	5	6	. 1659	1731	+	.	.	1	147227038	147227109	+	.	.	.	.	.	.	.	.	.	. 724	847	+	.	.	1	169534490	169534614	+	.

```


```
$ head picky.profile.xls
read	rlen	fid	ftotal	type	FragSV	TDSR	TDC	INV	DEL	INS	INDEL	CTLC	TTLC	score	EG2	E	Identity	IdentityP Mismatch	MismatchP	Deletion	DeletionP	Insertion	InsertionP	qStart	qEnd	qStrand	qALen	qP	refId	refStart	refEnd	refStrand	refALen	notes	sdiff	qdiff	diffclass
0884e006-47e7-4ab5-9a00-5ea7afb10f22	17592	1	2	SCMFSL	N	N	N	N	N	N	N	N	N	.	.	. 12824	17495	+	.	.	1	212391282	212396081	+	.		n.a.	n.a.	n.a.
0884e006-47e7-4ab5-9a00-5ea7afb10f22	17592	2	2	SCMFSL	N	N	N	N	N	N	N	N	N	.	.	. 4907	5262	+	.	.	1	167319512	167319882	-	.		n.a.	n.a.	n.a.
a0ec73fc-65ed-4785-ba64-9432f2715081	28735	1	2	SCMFSL	INDEL	N	N	N	N	N	Y	N	N	.	.	. 824	881	+	.	.	1	108100278	108100335	+	.	INDEL=f1_2(rgap=64684320,span=64684320,loc=1:108100335-172784655) 64684320	6467	>>
a0ec73fc-65ed-4785-ba64-9432f2715081	28735	2	2	SCMFSL	N	N	N	N	N	N	Y	N	N	.	.	. 7348	7424	+	.	.	1	172784655	172784731	+	.	INDEL=f1_2(rgap=64684320,span=64684320,loc=1:108100335-172784655) n.a.	n.a.	n.a.
37f7a446-9437-4a18-a5a1-deee08007a32	7781	1	3	SCMFSL	N	N	N	N	N	N	Y	N	N	.	.	. 1729	1939	+	.	.	1	240677445	240677655	-	.	INDEL=f2_3(rgap=27889388,span=27889388,loc=1:67556956-95446344)	n.a.	n.a.	n.a.
37f7a446-9437-4a18-a5a1-deee08007a32	7781	2	3	SCMFSL	INDEL	N	N	N	N	N	Y	N	N	.	.	. 67	212	+	.	.	1	67556813	67556956	+	.	INDEL=f2_3(rgap=27889388,span=27889388,loc=1:67556956-95446344)	27889388	3787	>>
37f7a446-9437-4a18-a5a1-deee08007a32	7781	3	3	SCMFSL	N	N	N	N	N	N	Y	N	N	.	.	. 3999	4083	+	.	.	1	95446344	95446426	+	.	INDEL=f2_3(rgap=27889388,span=27889388,loc=1:67556956-95446344)	n.a.	n.a.	n.a.
4ff800f5-de58-4c0e-8493-9ac59b82a055	6786	1	1	SCSF	.	.	.	.	.	.	.	.	.	.	.	. 5622	5720	+	.	.	1	230740689	230740790	+	.		n.a.	n.a.	n.a.
8b90318d-58f7-4f07-b509-1ae931a2860a	8814	1	1	SCSF	.	.	.	.	.	.	.	.	.	.	.	. 7529	7592	+	.	.	1	150200455	150200518	-	.		n.a.	n.a.	n.a.

```


#### xls2vcf
```
$ /home/husong/ActiveState/ActivePerl-5.24.3.2404/perl/bin/src/picky.pl  xls2vcf --xls picky.profile.DEL.xls --xls picky.profile.INS.xls --xls picky.profile.INDEL.xls --xls picky.profile.INV.xls --xls picky.profile.TTLC.xls --xls picky.profile.TDSR.xls --xls picky.profile.TDC.xls > picky.allsv.vcf
```