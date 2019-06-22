
## [LTR_retriever](https://github.com/oushujun/LTR_retriever): LTR_retriever accurately identifies and annotates LTR retrotransposons; LAI evaluates the continuity of genome assemblies.

### [LAI: 评估基因组质量一个标准](https://www.jianshu.com/p/7d794d22e0a0)

### install LTR_retriever
```
$ git clone https://github.com/oushujun/LTR_retriever.git
```

tools
```
$ cd LTR_retriever/  && tree
.
├── bin
│   ├── Age_est.pl
│   ├── align_flanking.pl
│   ├── annotate_gff.pl
│   ├── annotate_lib.pl
│   ├── annotate_TE.pl
│   ├── call_seq_by_list.pl
│   ├── cleanOutput.pl
│   ├── cleanPro.pl
│   ├── cleanup.pl
│   ├── combine_overlap.pl
│   ├── convert_ltr_finder.pl
│   ├── convert_MGEScan.pl
│   ├── count_base.pl
│   ├── count_fam_size.pl
│   ├── fam_coverage.pl
│   ├── fam_summary.pl
│   ├── fasta-reformat.pl
│   ├── get_range.pl
│   ├── intact_finder_coarse.pl
│   ├── LAI_calc3.pl
│   ├── LTR.identifier.pl
│   ├── LTR_sum.pl
│   ├── make_gff3.pl
│   ├── make_gff3_with_RMout.pl
│   ├── make_lib.pl
│   ├── output_by_list.pl
│   ├── PacBio_processor.pl
│   ├── purger.pl
│   ├── run_MGEScan.pl
│   ├── simulate_mutation.pl
│   ├── Six-frame_translate.pl
│   ├── solo_finder.pl
│   ├── solo_intact_ratio.pl
│   ├── trf409.legacylinux64
│   ├── trf409.linux64
│   └── trf409.macosx
├── database
│   ├── alluniRefprexp082813
│   ├── dummy060817.fa
│   ├── TEfam.hmm
│   ├── Tpases020812DNA
│   └── Tpases020812LINE
├── LAI
├── LICENSE
├── LTR_retriever
├── Manual.pdf
├── paths
└── README.md
```


### parameters

LTR_retriever
```
$ ./LTR_retriever -h

###########################
###### LTR_retriever ######
###########################

A program for accurate identification of LTR-RTs from outputs of LTRharvest, LTR_FINDER, and 
    MGEScan-LTR and generating non-redundant LTR-RT library for genome annotations.

Shujun Ou, Depeatment of Horticulture, Michigan State University, East Lansing, MI, 48824
05/12/2017

Usage: LTR_retriever -genome genomefile -inharvest LTRharvest_input [options]

【Input Options】
-genome      [File] specify the genome sequence file (FASTA)
-inharvest   [File] LTR-RT candidates from LTRharvest
-infinder    [File] LTR-RT candidates from LTR_FINDER
-inmgescan   [File] LTR-RT candidates from MGEScan_LTR
-nonTGCA     [File] Non-canonical LTR-RT candidates from LTRharvest

【Output options】
-verbose/-v     retain intermediate outputs (developer mode)
-noanno         disable whole genome LTR-RT annotation (no GFF output)

【Filter options】
-misschar    [CHR]  specify the ambiguous character (default N)
-Nscreen        disable filtering ambiguous sequence in candidates
-missmax     [INT]  maximum number of ambiguous bp allowed in a candidate (default 10)
-missrate    [0-1]  maximum percentage of ambiguous bp allowed in a candidate (default 0.8)
-minlen      [INT]  minimum bp of the LTR region (default 100)
-max_ratio   [FLOAT]    maximum length ratio of internal region/LTR region (default 50)
-minscore    [INT]  minimum alignment length (INT/2) to identify tandem repeats (default 1000)
-flankmiss   [1-60] maximum ambiguous length (bp) allowed in 60bp-flanking sequences (default 25)
-flanksim    [0-100]    minimum percentage of identity for flanking sequence alignment (default 60)
-flankaln    [0-1]  maximum alignment portion allowed for 60bp-flanking sequences (default 0.6)
-motif       [[STRING]] specify non-canonical motifs to search for
            (default -motif [TCCA TGCT TACA TACT TGGA TATA TGTA TGCA])
-notrunc        Discard truncated LTR-RTs and nested LTR-RTs (will dampen sensitivity)
-procovTE     [0-1] maximum portion of allowed for cumulated DNA TE database and LINE database 
            lignments (default 0.7)
-procovPL     [0-1] maximum portion allowed for cumulated plant protein database alignments (default 0.7)
-prolensig   [INT]  minimum alignment length (aa) for LINE/DNA transposase/plant protein alignment (default 30)

【Library options】
-blastclust  [[STRING]] trigger to use blastclust and customize parameters 
            (default -blastclust [-L .9 -b T -S 80])
-cdhit       [[STRING]] trigger to use cd-hit-est (default) and customize parameters 
            (default -cdhit [-c 0.8 -G 0.8 -s 0.9 -T 20 -aL 0.9 -aS 0.9])
-linelib     [FASTA]    provide LINE transposase database for LINE TE exclusion 
            (default /database/Tpases020812LINE)
-dnalib      [FASTA]    provide DNA TE transposase database for DNA TE exclusion 
            (default /database/Tpases020812DNA)
-plantprolib [FASTA]    provide plant protein database for coding sequence exclusion 
            (default /database/alluniRefprexp082813)
-TEhmm       [Pfam] provide Pfam database for TE identification 
            (default /database/TEfam.hmm)

【Miscellaneous】
-u           [FLOAT]    neutral mutation rate (per bp per ya) (default 1.3e-8 (from rice))
-threads     [INT]  number of threads (≤ total available threads, default 4)
-help/-h        display this help information

######Questions and Issues Please See: https://github.com/oushujun/LTR_retriever ######

```



LAI

```
$ ./LAI
Input file(s) not exist!

The LTR Assembly Index (LAI) is developed to evaluate the assembly continunity of repetitive sequences
Usage: ./LAI -genome genome.fa -intact intact.pass.list -all genome.out [options]
Options:
    -genome [file]  The genome file that is used to generate everything.
    -intact [file]  A list of intact LTR-RTs generated by LTR_retriever (genome.fa.pass.list).
    -all [file] RepeatMasker annotation of all LTR sequences in the genome (genome.fa.out).
    -window [int]   Window size for LAI estimation. Default: 3000000 (3 Mb)
    -step [int] Step size for the estimation window to move forward. Default: 300000 (300 Kb)
            Set step size = window size if prefer non-overlapping outputs.
    -q      Quick estimation of LTR identity (much faster for large genomes, may sacrifice ~0.5% of accuracy).
    -qq     No estimation of LTR identity, only output raw LAI for within species comparison (very quick).
    -mono [file]    This parameter is mainly for ployploid genomes. User provides a list of sequence names that represent a monoploid (1x).
            LAI will calculated only on these sequences if provided. So user can also specify sequence of interest for LAI calculation.
    -iden [0-100]   Mean LTR identity (%) in the monoploid (1x) genome. This parameter will inactivate de novo estimation (same speed to -qq).
    -totLTR [0-100] Specify the total LTR sequence content (%) in the genome instead of estimating from the -all RepeatMasker file.
    -blast [path]   The path to the blastn program. If left unspecified, then blastn must be accessible via shell ENV.
    -t [number] Number of threads to run blastn.
    -h      Display this help info.


```


### run LTRFinder

```
$ ltr_finder -D 20000 -d 1000 -L 700 -l 100 -p 20 -C -M 0.9 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa >  arabidopsis_finder.scn
```

```
Program    : LTR_FINDER
Version    : 1.07

Predict protein Domains 2.505 second
>Sequence: 1 Len:30427671
[1] 1 Len:30427671
Location : 3780765 - 3785720 Len: 4956 Strand:+
Score    : 6 [LTR region similarity:1]
Status   : 11111010000
5'-LTR   : 3780765 - 3781204 Len: 440
3'-LTR   : 3785281 - 3785720 Len: 440
5'-TG    : TG , TG
3'-CA    : CA , CA
TSR      : 3780760 - 3780764 , 3785721 - 3785725 [CTTGT]
Sharpness: 0.457,0.5
Strand + :
PPT   : [12/15] 3785266 - 3785280

Details of exact match pairs:
3785281-3785720[440]
3780765-3781204[440]

Details of the LTR alignment(5'-end):
                                       |3785281
-TG-GA-GTA-GCAAAATCAAGTTT-----AAGAGGGGGTGTTGAAAGTTAAACTTGATTTTGAATCAAGTTTAATTATTG
 || ||  || | || | ||| |||     | |    | |*||||||||||||||||||||||||||||||||||||||||
GTGAGATCTATGGAACA-CAA-TTTCTTCCATGTCTTGTTGTTGAAAGTTAAACTTGATTTTGAATCAAGTTTAATTATTG
                                  *****|3780765

Details of the LTR alignment(3'-end):
                                3785720|**-***
ACACTTTCTCCATTACCTCTAAAAGAATTTTACTCTAACACT-TGTTGCC---GCCTGAAGAATCC--AAG--GACCA-TA
|||||||||||||||||||||||||||||||||||||||*   || |  |   || |||||| |||  |||  | | | ||
ACACTTTCTCCATTACCTCTAAAAGAATTTTACTCTAACAAAGTGGTATCAGAGCTTGAAGA-TCCTAAAGATGGCGAGTA
                                3781204|

Details of PPT(+):
AAGTTTAAGAGGGGG
|3785266

```


### LTR_retriever
```
$ /home/wzk/anaconda3/envs/evolution/bin/LTR_retriever/LTR_retriever -threads 10 -genome Arabidopsis_thaliana.TAIR10.dna.toplevel.fa  -infinder arabidopsis_finder.scn

##########################
### LTR_retriever v1.8.0 ###
##########################

Contributors: Shujun Ou, Ning Jiang

Please cite: Ou S, Jiang N: LTR_retriever: a highly accurate and sensitive program for identification of long terminal repeat retrotransposons. Plant Physiology 2018, 176:1410-1422
Parameters: -threads 10 -genome Arabidopsis_thaliana.TAIR10.dna.toplevel.fa -infinder arabidopsis_finder.scn


Mon Dec  3 04:27:25 EST 2018    Dependency checking: All passed!
Mon Dec  3 04:27:43 EST 2018    The longest sequence ID in the genome contains 54 characters, which is longer than the limit (15)
                Trying to reformat seq IDs...
                Attempt 1...
Mon Dec  3 04:27:45 EST 2018    Seq ID conversion successful!

Mon Dec  3 04:27:45 EST 2018    Start to convert inputs...
                Total candidates: 138
                Total uniq candidates: 138

Mon Dec  3 04:28:00 EST 2018    Module 1: Start to clean up candidates...
                Sequences with 10 missing bp or 0.8 missing data rate will be discarded.
                Sequences containing tandem repeats will be discarded.

Mon Dec  3 04:28:03 EST 2018    131 clean candidates remained

Mon Dec  3 04:28:03 EST 2018    Modules 2-5: Start to analyze the structure of candidates...
                The terminal motif, TSD, boundary, orientation, age, and superfamily will be identified in this step.

Mon Dec  3 04:28:29 EST 2018    Intact LTR-RT found: 99

Mon Dec  3 04:28:52 EST 2018    Module 6: Start to analyze truncated LTR-RTs...
                Truncated LTR-RTs without the intact version will be retained in the LTR-RT library.
                Use -notrunc if you don't want to keep them.

Mon Dec  3 04:28:52 EST 2018    6 truncated LTR-RTs found
Mon Dec  3 04:29:12 EST 2018    5 truncated LTR sequences have added to the library

Mon Dec  3 04:29:12 EST 2018    Module 5: Start to remove DNA TE and LINE transposases, and remove plant protein sequences...
                Total library sequences: 144
Mon Dec  3 04:30:42 EST 2018    Retained clean sequence: 140

Mon Dec  3 04:30:42 EST 2018    Sequence clustering for Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.ltrTE ...
Mon Dec  3 04:30:42 EST 2018    Unique lib sequence: 140

Mon Dec  3 04:30:43 EST 2018    Module 6: Start to remove nested insertions in internal regions...
Mon Dec  3 04:30:52 EST 2018    Raw internal region size (bit): 414728
                Clean internal region size (bit): 414051

Mon Dec  3 04:30:52 EST 2018    Sequence number of the redundant LTR-RT library: 296
                The redundant LTR-RT library size (bit): 585283

Mon Dec  3 04:30:52 EST 2018    Module 8: Start to make non-redundant library...

Mon Dec  3 04:30:54 EST 2018    Final LTR-RT library entries: 138
                Final LTR-RT library size (bit): 432213

Mon Dec  3 04:30:54 EST 2018    Total intact LTR-RTs found: 97
                Total intact non-TGCA LTR-RTs found: 0

Mon Dec  3 04:30:56 EST 2018    Start to annotate whole-genome LTR-RTs...
                Use -noanno if you don't want whole-genome LTR-RT annotation.


######################################
### LTR Assembly Index (LAI) beta3 ###
######################################

Developer: Shujun Ou
Parameters: -genome Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod -intact Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list -all Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out -t 10 -q -blast /home/wzk/anaconda3/envs/evolution/bin/


Mon Dec  3 04:40:50 EST 2018    Dependency checking: Passed!
Mon Dec  3 04:40:50 EST 2018    Calculation of LAI will be based on the whole genome.
                Please use the -mono parameter if your genome is a recent ployploid, for high identity between homeologues will overcorrect raw LAI scores.
Mon Dec  3 04:40:50 EST 2018    Estimate the identity of LTR sequences in the genome: quick mode
Mon Dec  3 04:42:38 EST 2018    The identity of LTR sequences: 94.108740102171%
Mon Dec  3 04:42:38 EST 2018    Calculate LAI:
                【Error】 Total LTR sequence content (4.79%) is too low for accurate LAI calculation (min 5% required)

                Sorry, LAI is not applicable on the current genome assembly.

Mon Dec  3 04:42:45 EST 2018    All analyses were finished!

##############################
####### Result files #########
##############################

Table output for intact LTR-RTs (detailed info)
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list (All LTR-RTs)
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.nmtf.pass.list (Non-TGCA LTR-RTs)
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list.gff3 (GFF3 format for intact LTR-RTs)

LTR-RT library
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.LTRlib.redundant.fa (All LTR-RTs with redundancy)
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.LTRlib.fa (All non-redundant LTR-RTs)
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.nmtf.LTRlib.fa (Non-TGCA LTR-RTs)

Whole-genome LTR-RT annotation by the non-redundant library
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.gff (GFF format)
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.fam.size.list (LTR family summary)
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.superfam.size.list (LTR superfamily summary)
```

output files:

```
-rw-r--r-- 1 117M Dec  3 04:27 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod
-rw-r--r-- 1  39K Dec  3 04:28 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.defalse
-rw-r--r-- 1 423K Dec  3 04:30 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.LTRlib.fa
-rw-r--r-- 1 572K Dec  3 04:30 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.LTRlib.redundant.fa
-rw-r--r-- 1 117M Dec  3 04:40 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.masked
-rw-r--r-- 1  100 Dec  3 04:30 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.nmtf.pass.list
-rw-r--r-- 1 1.1M Dec  3 04:40 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out
-rw-r--r-- 1  14K Dec  3 04:40 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.fam.size.list
-rw-r--r-- 1 592K Dec  3 04:40 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.gff
-rw-r--r-- 1 2.3M Dec  3 04:42 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.LAI.LTR.ava.out
-rw-r--r-- 1  17K Dec  3 04:40 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.LTR.distribution.txt
-rw-r--r-- 1  101 Dec  3 04:42 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.q.LAI.LTR.ava.age
-rw-r--r-- 1  374 Dec  3 04:40 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.superfam.size.list
-rw-r--r-- 1  13K Dec  3 04:30 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list
-rw-r--r-- 1  56K Dec  3 04:30 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list.gff3
-rw-r--r-- 1  23K Dec  3 04:30 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.retriever.all.scn
-rw-r--r-- 1 2.0K Dec  3 04:40 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.tbl

```



detail for output file:
```
$ head Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list
#LTR_loc        Category        Motif   TSD     5_TSD 3_TSD       Internal        Identity      Strand  SuperFamily  TE_type     Insertion_Time
1:3780765..3785720  pass    motif:TGCA  TSD:CTTGT   3780760..3780764    3785721..3785725    IN:3781205..3785280 1   +   unknown LTR 0
1:4406006..4411120  pass    motif:TGCA  TSD:ATTAA   4406001..4406005    4411121..4411125    IN:4406168..4410958 0.96914 +   unknown NA  1212033
1:6538415..6543535  pass    motif:TGCA  TSD:TTTTT   6538407..6538411    6543537..6543541    IN:6538580..6543370 1   -   unknown NA  0
1:7717356..7722547  pass    motif:TGCA  TSD:GACTG   7717351..7717355    7722548..7722552    IN:7717796..7722107 0.97273 +   Copia   LTR 1068389
1:11148091..11152835    pass    motif:TGCA  TSD:GCAAT   11148086..11148090  11152836..11152840  IN:11148387..11152539   0.99662 -   unknown LTR 130294
1:11789452..11794077    pass    motif:TGCA  TSD:GTCAT   11789447..11789451  11794078..11794082  IN:11789723..11793806   1   +   Copia   LTR 0
1:13334466..13339870    pass    motif:TGCA  TSD:CAATG   13334461..13334465  13339871..13339875  IN:13334861..13339478   0.92405 +   Gypsy   LTR 3079873
1:13439445..13448523    pass    motif:TGCA  TSD:TATGT   13439440..13439444  13448524..13448528  IN:13440014..13447955   0.96309 +   unknown LTR 1455738
1:13818567..13823888    pass    motif:TGCA  TSD:ATGTT   13818562..13818566  13823889..13823893  IN:13818943..13823512   1   +   Gypsy   LTR 0

```

### calculate LAI
```
$ /home/wzk/anaconda3/envs/evolution/bin/LTR_retriever/LAI -t 10 -genome Arabidopsis_thaliana.TAIR10.dna.toplevel.fa  -intact Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list -all Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out

######################################
### LTR Assembly Index (LAI) beta3 ###
######################################

Developer: Shujun Ou
Parameters: -t 10 -genome Arabidopsis_thaliana.TAIR10.dna.toplevel.fa -intact Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.pass.list -all Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out


Mon Dec  3 05:40:45 EST 2018    Dependency checking: Passed!
Mon Dec  3 05:40:45 EST 2018    Calculation of LAI will be based on the whole genome.
                Please use the -mono parameter if your genome is a recent ployploid, for high identity between homeologues will overcorrect raw LAI scores.
Mon Dec  3 05:40:45 EST 2018    Estimate the identity of LTR sequences in the genome: standard mode
Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.LAI.LTR.fa is empty, please check the Arabidopsis_thaliana.TAIR10.dna.toplevel.fa file and the Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.LAI.LTRlist file
Mon Dec  3 05:40:48 EST 2018    The identity of LTR sequences: %
Argument "" isn't numeric in numeric lt (<) at /home/wzk/anaconda3/envs/evolution/bin/LTR_retriever/LAI line 127.

                【Warning】 The identity drops below the safe limit. Instead, identity of 92% will be used for LAI adjustment.

Mon Dec  3 05:40:48 EST 2018    Calculate LAI:
Illegal division by zero at /home/wzk/anaconda3/envs/evolution/bin/LTR_retriever/bin/LAI_calc3.pl line 123.
Use of uninitialized value $int in multiplication (*) at /home/wzk/anaconda3/envs/evolution/bin/LTR_retriever/LAI line 150.
Use of uninitialized value $total in multiplication (*) at /home/wzk/anaconda3/envs/evolution/bin/LTR_retriever/LAI line 150.

                【Error】Intact LTR-RT content (0%) is too low for accurate LAI calculation (min 0.1% required)
                【Error】 Total LTR sequence content (0%) is too low for accurate LAI calculation (min 5% required)

                Sorry, LAI is not applicable on the current genome assembly.

```


If total LTR sequence content, it will creat the out file 
**Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.mod.out.LAI**


### clasffication level of assembled genome


```
Category
LAI
Examples


Draft
0 ≤ LAI < 10
Apple (v1.0), Cacao (v1.0)


Reference
10 ≤ LAI < 20
Arabidopsis (TAIR10), Grape (12X)


Gold
20 ≤ LAI
Rice (MSUv7), Maize (B73 v4)

```