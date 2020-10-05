
## [NanoVar](https://github.com/benoukraflab/NanoVar)

Structural variant caller for low-depth Nanopore Sequencing.


### install nanovar
```
$ git clone https://github.com/benoukraflab/NanoVar.git 
$ cd NanoVar 
$ ./configure
$ make && make check

make[1]: Leaving directory `/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar'
Testing unit...
Pre-testing...
Pre-testing passed
Post-testing...
NanoVar initiated --- Wed Jun 19 17:59:20 CST 2019
Progress: [ #################### ]  (100%)
NanoVar finished successfully --- Wed Jun 19 18:02:24 CST 2019
<Reference> ---------: Checked
<longfa>    ---------: Checked
<shortfa1>  ---------: Checked
<shortfa2>  ---------: Checked
<fai>       ---------: Passed
<nhr>       ---------: Passed
<nsq>       ---------: Passed
<bwt>       ---------: Passed
<sa>        ---------: Passed
<sequence>  ---------: Passed
<counts>    ---------: Passed
<obinary>   ---------: Passed
<align>     ---------: Passed
<parse>     ---------: Passed
<overlap>   ---------: Passed
<ANN>       ---------: Failed
python2.7 failed, please ensure python2.7 is in PATH and functional


```

It need the environment of python2, the author is can support python3 later


### parameters
```
$ nanovar --help
NanoVar - Structural variant caller for low-depth Nanopore Sequencing.
Author: Tham Cheng Yong
Version 1.0
Usage:
    ./nanovar [OPTIONS] -r reference_genome.fa -l longread.fa -t num_threads -o <Output_Dir> -f hg38

Options:
    -h, --help          Show this help menu
    -v, --version       Print NanoVar version
    -q, --quiet         Disable progress bar verbose
    -r FILE             Reference genome in FASTA
    -l FILE             Long reads (ONT/PacBio/etc) in FASTQ/FASTA or gzip/zip-compressed FASTQ/FASTA
    -s1 FILE            NGS paired-end short read first mates in FASTQ/FASTA or gzip-compressed FASTQ/FASTA (Optional)
    -s2 FILE            NGS paired-end short read second mates in FASTQ/FASTA or gzip-compressed FASTQ/FASTA (Optional)
    -o DIR              Output directory
    -t INT              Number of threads available for use. (<=53) [Default=1]
    -f, --filter FILE   BED file with genomic regions to be excluded (e.g. telomeres and centromeres). Either specify name of 
                        supported reference genome filter (i.e. hg38, hg19, mm10, mm9) or provide FULL path to own BED file. [Default=None]
    -w, --SVlen INT     Minimum length estimation of SV to be detected, >=100 bases recommended. [Default=100]
    -n, --mincov INT    Minimum coverage of short reads spanning over SV breakpoint region on long read [Default=0]
    -m, --maxcov INT    Maximum coverage of short reads spanning over SV breakpoint region on long read [Default=100]
    -p FLOAT            Minimum percentage of unmapped bases within a long read to be considered as a split-read (0.05 to 0.50) [Default=0.05]
    -S FLOAT            SV threshold score, increasing this will increase precision but decrease recall (<=0) [Default=2.6]

```


### run nanovar

Set the path of python
```
$ export PATH=/usr/bin:$PATH
```


```
$ nanovar -r /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -l M625-0_test.fastq -t 20 -o /home/wuzhikun/Project/nanoVar 
NanoVar initiated --- Thu Jun 20 08:53:12 CST 2019
<WARNING: Long read sequencing depth is below recommended depth of more than 4x, output may not be comprehensive>
Traceback (most recent call last):  (32%)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_lcov_outlier.py", line 186, in <module>
    print main()
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_lcov_outlier.py", line 177, in main
    curve(data2, n, round((medad*6) + med, 0))
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_lcov_outlier.py", line 136, in curve
    smooth = spline(c,y,xnew)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/nv_virtualenv/lib/python2.7/site-packages/numpy/lib/utils.py", line 101, in newfunc
    return func(*args, **kwds)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/nv_virtualenv/lib/python2.7/site-packages/scipy/interpolate/interpolate.py", line 2918, in spline
    return spleval(splmake(xk, yk, order=order, kind=kind, conds=conds), xnew)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/nv_virtualenv/lib/python2.7/site-packages/numpy/lib/utils.py", line 101, in newfunc
    return func(*args, **kwds)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/nv_virtualenv/lib/python2.7/site-packages/scipy/interpolate/interpolate.py", line 2827, in splmake
    coefs = func(xk, yk, order, conds, B)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/nv_virtualenv/lib/python2.7/site-packages/scipy/interpolate/interpolate.py", line 2743, in _find_smoothest
    J = _fitpack._bspldismat(order, xk)
ValueError: too few samples (0)
awk: cmd. line:1: {if (>$11+$13 && $11+$13>=1) print $0}
awk: cmd. line:1:      ^ syntax error
awk: cmd. line:1: {if (>$11+$13 && $11+$13>=1) print $0}
awk: cmd. line:1:                            ^ syntax error
***** WARNING: File bed2.sort has inconsistent naming convention for record:
chr1	8695050	8695150	8eba26d1-af9a-41f8-b59d-7c178244812e~D9JRT-l	Inter

***** WARNING: File bed2.sort has inconsistent naming convention for record:
chr1	8695050	8695150	8eba26d1-af9a-41f8-b59d-7c178244812e~D9JRT-l	Inter

***** WARNING: File bed4.sort has inconsistent naming convention for record:
chr1	8695100	8695101	8eba26d1-af9a-41f8-b59d-7c178244812e~D9JRT

***** WARNING: File bed4.sort has inconsistent naming convention for record:
chr1	8695100	8695101	8eba26d1-af9a-41f8-b59d-7c178244812e~D9JRT

Traceback (most recent call last):
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_lr_overlap.py", line 468, in <module>
    main()
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_lr_overlap.py", line 465, in main
    print ''.join(output)
IOError: [Errno 32] Broken pipe
***SV Overlap file required***


```


```
$ cat hsblastsavecmd.txt

/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/blast/hs-blastn-src/hs-blastn align -db /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -window_masker_db Homo_sapiens.GRCh38.dna.primary_assembly.fa.counts.obinary -query <(cat /home/wuzhikun/Project/nanoVar/M625-0_test.fastq) -out M625-0_test.hsblast-Homo_sapiens -outfmt 6 -num_threads 20 -max_target_seqs 3 -gapopen 0 -gapextend 4 -penalty -3 -reward 2
```


```
$ cat 20-Jun~08-53-12_NanoVar.commandlog

NanoVar Command Log
Thu Jun 20 08:53:12 CST 2019
/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/blast/makeblastdb -in /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -input_type fasta -dbtype nucl
/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/blast/windowmasker -in /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -infmt blastdb -mk_counts -out Homo_sapiens.GRCh38.dna.primary_assembly.fa.counts
/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/blast/windowmasker -in Homo_sapiens.GRCh38.dna.primary_assembly.fa.counts -sformat obinary -out Homo_sapiens.GRCh38.dna.primary_assembly.fa.counts.obinary -convert
/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/blast/hs-blastn-src/hs-blastn index /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa
/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/blast/hs-blastn-src/hs-blastn align -db /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -window_masker_db Homo_sapiens.GRCh38.dna.primary_assembly.fa.counts.obinary -query <(cat /home/wuzhikun/Project/nanoVar/M625-0_test.fastq) -out M625-0_test.hsblast-Homo_sapiens -outfmt 6 -num_threads 20 -max_target_seqs 3 -gapopen 0 -gapextend 4 -penalty -3 -reward 2
python /home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_hsblast_parse.py M625-0_test.hsblast-Homo_sapiens <(cat /home/wuzhikun/Project/nanoVar/M625-0_test.fastq) ../../20-Jun~08-53-12_NanoVar.log > M625-0_test.hsblast-Homo_sapiens.tsv
python /home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_hsblast_SV_detector.py M625-0_test.hsblast-Homo_sapiens.tsv 0.95 0 ../../20-Jun~08-53-12_NanoVar.log > M625-0_test.hsblast-Homo_sapiens.SV0.95.tsv
python /home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_breakpoint_parser.py M625-0_test.hsblast-Homo_sapiens.SV0.95.tsv 50 ../../20-Jun~08-53-12_NanoVar.log | /home/wuzhikun/anaconda3/envs/NanoSV/bin/bedtools sort -i - > M625-0_test.hsblast-Homo_sapiens.SV0.95.parse50.tsv
python /home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar/scripts/nv_lr_overlap.py M625-0_test.hsblast-Homo_sapiens.SV0.95.parse50.tsv M625-0_test.hsblast-Homo_sapiens.tsv 50 /home/wuzhikun/anaconda3/envs/NanoSV/bin/bedtools 1 | awk -F'\t' "{if (>$11+$13 && $11+$13>=1) print $0}" > M625-0_test.hsblast-Homo_sapiens.SV0.95.parse50.1-.overlap.tsv1
/home/wuzhikun/anaconda3/envs/NanoSV/bin/bedtools sort -i M625-0_test.hsblast-Homo_sapiens.SV0.95.parse50.1-.overlap.tsv1 > M625-0_test.hsblast-Homo_sapiens.SV0.95.parse50.1-.overlap.tsv
rm M625-0_test.hsblast-Homo_sapiens.SV0.95.parse50.1-.overlap.tsv1
***SV Overlap file required***

```


### Run using at least 4X fastq file


```
$ ls -lh /home/wuzhikun/Project/NanoTrio/clean/M625-0.fastq.gz
-rw-rw-r-- 1 wuzhikun wuzhikun 39G Mar 29 02:37 /home/wuzhikun/Project/NanoTrio/clean/M625-0.fastq.gz

```

```
nanovar -r /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -l M625-0.fastq -t 20 -o /home/wuzhikun/Project/nanoVar > nanovar.log 2>&1
```



### log file
```
Log file for NanoVar-1.0.
Thu Jun 20 12:47:52 CST 2019
Command /home/wuzhikun/anaconda3/envs/NanoSV/bin/nanovar -r /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -l M625-0.fastq -t 20 -o /home/wuzhikun/Project/nanoVar
<Long read fasta file contains no spaces> --- PASSED
<Long read fasta file contains no wraped lines> --- PASSED
create nanovar_run directory
create nanovar_results directory
create figures directory
create bowtie2_shortreads directory
create hsblast_longreads directory

Inputs and parameters:
main=/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoVar
refgenome=/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa
longread=/home/wuzhikun/Project/nanoVar/M625-0.fastq
shortread1=NIL
shortread2=NIL
Short paired-end reads not provided, only long reads will be used for SV characterization
output_dir=/home/wuzhikun/Project/nanoVar
no_of_threads=20
Genomic_region_excluded_file=0
Neural_network_threshold=0
SV_threshold_score=2.6
SV_alignment_threshold=0.95
Buffered_SV_length_threshold=50
minimum_short_cov=NA
maximum_short_cov=NA
Total_long_reads=2468218

Starting run...
SKIPPING - Build BLAST DB
[Thu-20-Jun 12:47:52] Generate freq counts file
[Thu-20-Jun 13:17:30] Convert frequency counts file to obinary
SKIPPING - Build FMD index
[Thu-20-Jun 13:19:23] HS-BLAST read alignment search
[Thu-20-Jun 17:03:04] HS-BLAST Parse

Longread_overlap_upper_limit=41.7
Genome_size=3099750718 bases
Mapped_bases=41240133780 bases
Seq_depth=13.3043388104 x
Number_of_splits=1
Splitted_coverage=13.3043388104

```


### output results

```
$ tree nanovar_run
nanovar_run
├── bowtie2_shortreads
└── hsblast_longreads
    ├── Homo_sapiens.GRCh38.dna.primary_assembly.fa.counts
    ├── Homo_sapiens.GRCh38.dna.primary_assembly.fa.counts.obinary
    ├── M625-0.hsblast-Homo_sapiens
    ├── M625-0.hsblast-Homo_sapiens.SV0.95.parse50.1-41.7.overlap.ANN0.cov.tsv
    ├── M625-0.hsblast-Homo_sapiens.SV0.95.parse50.1-41.7.overlap.ANN0.tsv
    ├── M625-0.hsblast-Homo_sapiens.SV0.95.parse50.1-41.7.overlap.ANN.tsv
    ├── M625-0.hsblast-Homo_sapiens.SV0.95.parse50.1-41.7.overlap.tsv
    ├── M625-0.hsblast-Homo_sapiens.SV0.95.parse50.tsv
    ├── M625-0.hsblast-Homo_sapiens.SV0.95.tsv
    ├── M625-0.hsblast-Homo_sapiens.tsv
    └── readcovcounts.txt
```

```
$ tree nanovar_results
nanovar_results
├── css
│   ├── bootstrap.min.css
│   ├── buttons.dataTables.min.css
│   ├── font-awesome.min.css
│   ├── jquery.dataTables.min.css
│   └── mdb.min.css
├── figures
│   ├── depth_of_coverage.png
│   ├── read_length_dist.png
│   ├── scatter1.png
│   ├── scatter2.png
│   ├── sv_lengths.png
│   └── sv_type_donut.png
├── js
│   ├── bootstrap.min.js
│   ├── buttons.flash.min.js
│   ├── buttons.html5.min.js
│   ├── dataTables.buttons.min.js
│   ├── jquery-3.3.1.min.js
│   ├── jquery.dataTables.min.js
│   ├── jszip.min.js
│   ├── mdb.min.js
│   └── popper.min.js
├── M625-0.output.filtered-2.6.vcf
├── M625-0.output.report.html
├── M625-0.output.total.vcf
└── M625-0.svread-overlap.tsv

```



#### detail of vcf
```
$ grep -v '^#' M625-0.output.total.vcf | head 
1	10472	ABO08~e5c5dcc5-b66c-4846-b093-4da1b38e9bad	.	BND	3.0	PASS	SVTYPE=BND;CHR2=.;END=.;SCOV=0.0;LCOV=10.0;NCOV=0.0;SVRATIO=1.0;PROB=0.5037;SVLEN=6857;
1	10536	GZ4YO~48d7785b-12fc-424d-9159-40f565fed25f	.	BND	1.7	PASS	SVTYPE=BND;CHR2=.;END=.;SCOV=0.0;LCOV=3.0;NCOV=0.0;SVRATIO=1.0;PROB=0.3312;SVLEN=5555;
1	10628	GWT78~c88dd8fb-2f7d-4c27-ac9b-f29e31ce1e00	.	INV	1.8	PASS	SVTYPE=INV;CHR2=1;END=248944831;SCOV=0.0;LCOV=1.0;NCOV=0.0;SVRATIO=1.0;PROB=0.3342;SVLEN=7111;
1	10642	JCELG~c0f82cd4-8251-4c46-b01e-6e27d874bd9a	.	INV	4.2	PASS	SVTYPE=INV;CHR2=1;END=248944937;SCOV=0.0;LCOV=10.0;NCOV=0.0;SVRATIO=1.0;PROB=0.617;SVLEN=7233;
1	10706	N852X~0295de4f-4962-44f0-bfec-da381e1f0093	.	BND	0.8	PASS	SVTYPE=BND;CHR2=.;END=.;SCOV=0.0;LCOV=1.0;NCOV=0.0;SVRATIO=1.0;PROB=0.1595;SVLEN=4663;
1	10769	364QP~ecf7a79e-9d50-4ec5-82ad-4e6a025680e1	.	BND	0.8	PASS	SVTYPE=BND;CHR2=.;END=.;SCOV=0.0;LCOV=1.0;NCOV=0.0;SVRATIO=1.0;PROB=0.1629;SVLEN=17225;
1	10906	FO52N~60d91ee4-c3d5-4722-9f2c-0a0f85958dc0	.	BND	1.8	PASS	SVTYPE=BND;CHR2=1;END=180420;SCOV=0.0;LCOV=1.0;NCOV=0.0;SVRATIO=1.0;PROB=0.343;SVLEN_UNKN;
1	10906	3KE9Z~60d91ee4-c3d5-4722-9f2c-0a0f85958dc0	.	INS	1.8	PASS	SVTYPE=INS;CHR2=.;END=.;SCOV=0.0;LCOV=1.0;NCOV=0.0;SVRATIO=1.0;PROB=0.343;SVLEN=537;
1	11068	M0H6I~3a976bc5-0599-45c2-b571-87e16c2f7b29	.	DEL	0.7	PASS	SVTYPE=DEL;CHR2=1;END=11292;SCOV=0.0;LCOV=1.0;NCOV=1.0;SVRATIO=0.5;PROB=0.1561;SVLEN=224;
1	11125	FK6QP~addd4ba6-f130-4590-814d-dec6b37b7bdf	.	BND	2.4	PASS	SVTYPE=BND;CHR2=1;END=181294;SCOV=0.0;LCOV=2.0;NCOV=0.0;SVRATIO=1.0;PROB=0.4245;SVLEN_UNKN;

```

#### overlap file
```
$ head M625-0.svread-overlap.tsv
Lead_idx~readnames	Supporting_readnames~idx
6CXPI~000008ea-9bcf-40ae-be59-f85aab57e36d	a74a2592-4467-4efe-aeab-4ffb9f013f36~TFD0M,d9ea6b21-932b-4d4b-a97a-f0dc7eaac5d4~B14GW,460f3918-a95d-464a-9629-dd635bad7fdb~ZUTBC,ad9b837d-fc3a-4fdd-9249-f65e4de49f51~B5NOX,70946e80-afd6-47a3-b188-04b435ddf8fd~5WLV8,c057f1e9-2548-4e71-ada6-691e0221fdff~FDIWZ,a2fdf8ad-e21c-4d43-90e5-d5caf6b95733~58Z0W,fac77d2e-9761-48df-b884-27b390670ec8~67FPE,85649ca3-df91-4e6e-94ab-7fde7f6ac4a5~R6S7E,211a02b1-6494-4012-ab36-8641dea14f8d~M78KL,5935d1e9-a630-42f0-a768-457a19d6a743~EARZY,ce1a9d1e-022f-47e7-9090-5c2f4b91c1f9~XR36Q,845ad272-fad9-4864-9857-d7b9ec04ff7c~59TUI
6CXPI~000008ea-9bcf-40ae-be59-f85aab57e36d	a74a2592-4467-4efe-aeab-4ffb9f013f36~TFD0M,d9ea6b21-932b-4d4b-a97a-f0dc7eaac5d4~B14GW,460f3918-a95d-464a-9629-dd635bad7fdb~ZUTBC,ad9b837d-fc3a-4fdd-9249-f65e4de49f51~B5NOX,70946e80-afd6-47a3-b188-04b435ddf8fd~5WLV8,c057f1e9-2548-4e71-ada6-691e0221fdff~FDIWZ,a2fdf8ad-e21c-4d43-90e5-d5caf6b95733~58Z0W,fac77d2e-9761-48df-b884-27b390670ec8~67FPE,85649ca3-df91-4e6e-94ab-7fde7f6ac4a5~R6S7E,211a02b1-6494-4012-ab36-8641dea14f8d~M78KL,5935d1e9-a630-42f0-a768-457a19d6a743~EARZY,ce1a9d1e-022f-47e7-9090-5c2f4b91c1f9~XR36Q,845ad272-fad9-4864-9857-d7b9ec04ff7c~59TUI
JKEOC~00001838-8a24-48e6-b0cc-8e30d046baa4	.
JKEOC~00001838-8a24-48e6-b0cc-8e30d046baa4	.

```


#### filt vcf
```
$ grep -v '^#' M625-0.output.filtered-2.6.vcf | head 
1	10472	ABO08~e5c5dcc5-b66c-4846-b093-4da1b38e9bad	.	BND	3.0	PASS	SVTYPE=BND;CHR2=.;END=.;SCOV=0.0;LCOV=10.0;NCOV=0.0;SVRATIO=1.0;PROB=0.5037;SVLEN=6857;
1	10642	JCELG~c0f82cd4-8251-4c46-b01e-6e27d874bd9a	.	INV	4.2	PASS	SVTYPE=INV;CHR2=1;END=248944937;SCOV=0.0;LCOV=10.0;NCOV=0.0;SVRATIO=1.0;PROB=0.617;SVLEN=7233;
1	34045	OMAY2~e9aa6166-c25a-472a-b77f-772f3c1e47b9	.	BND	3.1	PASS	SVTYPE=Ins;CHR2=1;END=204557;SCOV=0.0;LCOV=11.0;NCOV=7.0;SVRATIO=0.611;PROB=0.5048;SVLEN=17029;
1	90441	Z9YAV~bca9e182-1186-449e-9bb2-012ae5332694	.	BND	6.8	PASS	SVTYPE=Ins;CHR2=1;END=585990;SCOV=0.0;LCOV=5.0;NCOV=0.0;SVRATIO=1.0;PROB=0.7929;SVLEN=2008;
1	90441	4DFZO~a02d8182-fb15-4825-b826-8bb269b5ebe9	.	DEL	8.0	PASS	SVTYPE=DEL;CHR2=1;END=585990;SCOV=0.0;LCOV=4.0;NCOV=0.0;SVRATIO=1.0;PROB=0.8416;SVLEN=495549;
1	136208	0HCOS~d9e3812a-ee77-4eb4-9c63-9f787766f3fd	.	BND	8.1	PASS	SVTYPE=Ins;CHR2=1;END=492490;SCOV=0.0;LCOV=6.0;NCOV=2.0;SVRATIO=0.75;PROB=0.8443;SVLEN=10662;
1	180088	J2VRA~f6d7a460-fc12-4e43-87ef-b9dbcca38d30	.	INV	3.3	PASS	SVTYPE=INV;CHR2=1;END=248945550;SCOV=0.0;LCOV=10.0;NCOV=0.0;SVRATIO=1.0;PROB=0.5271;SVLEN_UNKN;
1	181980	CJMLF~47b962fa-a329-468e-a98f-43bc0179af7c	.	INV	3.9	PASS	SVTYPE=INV;CHR2=1;END=248943099;SCOV=0.0;LCOV=4.0;NCOV=0.0;SVRATIO=1.0;PROB=0.5909;SVLEN=1666;
1	181982	1FUOP~349d39ed-cb07-4ebb-9597-2fba0cefeb15	.	DEL	3.4	PASS	SVTYPE=DEL;CHR2=1;END=350194;SCOV=0.0;LCOV=2.0;NCOV=0.0;SVRATIO=1.0;PROB=0.5437;SVLEN=168212;
1	204557	C1RM8~7671c429-e17a-4a41-a659-2ed8d2245178	.	INS	6.0	PASS	SVTYPE=INS;CHR2=.;END=.;SCOV=0.0;LCOV=3.0;NCOV=0.0;SVRATIO=1.0;PROB=0.7497;SVLEN=2946;

```



### warning information

There are output results, however it still had the warning information, such as:
```
$ cat nanovar.log
nohup: ignoring input
***** WARNING: File bed2.sort has inconsistent naming convention for record:
chr1  10576 10676 20d2af44-9ca2-4321-9b65-530378a38993~SRKME-l  Inter

***** WARNING: File bed2.sort has inconsistent naming convention for record:
chr1  10576 10676 20d2af44-9ca2-4321-9b65-530378a38993~SRKME-l  Inter

***** WARNING: File bed4.sort has inconsistent naming convention for record:
chr1  10626 10627 20d2af44-9ca2-4321-9b65-530378a38993~SRKME

***** WARNING: File bed4.sort has inconsistent naming convention for record:
chr1  10626 10627 20d2af44-9ca2-4321-9b65-530378a38993~SRKME

***** WARNING: File hsblast_longreads/bed1.sort has inconsistent naming convention for record:
chr1  10626 10627 SRKME~20d2af44-9ca2-4321-9b65-530378a38993  1.6

***** WARNING: File hsblast_longreads/bed1.sort has inconsistent naming convention for record:
chr1  10626 10627 SRKME~20d2af44-9ca2-4321-9b65-530378a38993  1.6

Progress: [ #################### ]  (100%)
NanoVar finished successfully --- Thu Jun 20 19:30:03 CST 2019

```




## docker of nanovar

```
$ docker run --rm -v /home/wuzhikun:/home 192.168.11.102:5000/nanoval:1.0
Unable to find image '192.168.11.102:5000/nanoval:1.0' locally
1.0: Pulling from nanoval
898c46f3b1a1: Pull complete 
63366dfa0a50: Pull complete 
041d4cd74a92: Pull complete 
6e1bee0f8701: Pull complete 
53230d58f5a3: Pull complete 
Digest: sha256:c3bd90a5a881471cfb5b8d84abdb05d5351e1b9385103944ad7b011597b70cb9
Status: Downloaded newer image for 192.168.11.102:5000/nanoval:1.0

```


```

nohup: ignoring input
NanoVar initiated --- Thu Jun 20 12:17:42 UTC 2019
Progress: [ -------------------- ]  (0%)^MProgress: [ #------------------- ]  (2%)^MProgress: [ #------------------- ]  (5%)^MProgress: [ ##------------------ ]  (10%)^MProgress: [ ######-------------- ]  (30%)^M^MTraceback (most recent call last):
  File "/home/NanoVar/scripts/nv_hsblast_parse.py", line 156, in <module>
    main()
  File "/home/NanoVar/scripts/nv_hsblast_parse.py", line 91, in main
    tmp.append(info(line))
  File "/home/NanoVar/scripts/nv_hsblast_parse.py", line 71, in info
    sid = line.split('\t')[1]
IndexError: list index out of range
<WARNING: Long read sequencing depth is below recommended depth of more than 4x, output may not be comprehensive>
Progress: [ ######-------------- ]  (32%)^MTraceback (most recent call last):
  File "/home/NanoVar/scripts/nv_lcov_outlier.py", line 186, in <module>
    print main()
  File "/home/NanoVar/scripts/nv_lcov_outlier.py", line 177, in main
    curve(data2, n, round((medad*6) + med, 0))
  File "/home/NanoVar/scripts/nv_lcov_outlier.py", line 136, in curve
    smooth = spline(c,y,xnew)
  File "/home/NanoVar/nv_virtualenv/local/lib/python2.7/site-packages/numpy/lib/utils.py", line 101, in newfunc
    return func(*args, **kwds)
  File "/home/NanoVar/nv_virtualenv/local/lib/python2.7/site-packages/scipy/interpolate/interpolate.py", line 2918, in spline
    return spleval(splmake(xk, yk, order=order, kind=kind, conds=conds), xnew)
  File "/home/NanoVar/nv_virtualenv/local/lib/python2.7/site-packages/numpy/lib/utils.py", line 101, in newfunc
    return func(*args, **kwds)
  File "/home/NanoVar/nv_virtualenv/local/lib/python2.7/site-packages/scipy/interpolate/interpolate.py", line 2827, in splmake
    coefs = func(xk, yk, order, conds, B)
  File "/home/NanoVar/nv_virtualenv/local/lib/python2.7/site-packages/scipy/interpolate/interpolate.py", line 2743, in _find_smoothest
    J = _fitpack._bspldismat(order, xk)
ValueError: too few samples (0)
***HS-BLAST parsed file required!***

```


