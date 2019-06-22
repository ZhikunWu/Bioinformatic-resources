## [DaPars](http://lilab.research.bcm.edu/dldcc-web/lilab/zheng/DaPars_Documentation/html/DaPars.html#step-1-generate-region-annotation-python-dapars-extract-anno-py-b-gene-bed-s-symbol-map-txt-o-extracted-3utr-bed)

```
#A comma-separated list of BedGraph files of samples from condition 1

Group1_Tophat_aligned_Wig=Condition_A_chrX.wig
#Group1_Tophat_aligned_Wig=Condition_A_chrX_r1.wig,Condition_A_chrX_r2.wig if multiple files in one group

#A comma-separated list of BedGraph files of samples from condition 2

Group2_Tophat_aligned_Wig=Condition_B_chrX.wig

Output_directory=DaPars_Test_data/

Output_result_file=DaPars_Test_data

#At least how many samples passing the coverage threshold in two conditions
Num_least_in_group1=1

Num_least_in_group2=1

Coverage_cutoff=30

#Cutoff for FDR of P-values from Fisher exact test.

FDR_cutoff=0.05


PDUI_cutoff=0.5

Fold_change_cutoff=0.59

```


```
$ less hg38_ref_all.txt
DDX11L1 NR_046018       chr1    +       11873   14409   14409   14409   3       11873,12612,13220,      12227,12721
,14409,
MIR6859-1       NR_106918       chr1    -       17368   17436   17436   17436   1       17368,  17436,
MIR6859-2       NR_107062       chr1    -       17368   17436   17436   17436   1       17368,  17436,
MIR6859-3       NR_107063       chr1    -       17368   17436   17436   17436   1       17368,  17436,
MIR6859-4       NR_128720       chr1    -       17368   17436   17436   17436   1       17368,  17436,
MIR1302-2       NR_036051       chr1    +       30365   30503   30503   30503   1       30365,  30503,


$ head hg19_4_19_2012_Refseq_id_from_UCSC.txt
#name   name2
NM_032291   SGIP1
NM_052998   ADC
NM_001145278    NECAP2
NM_001145277    NECAP2
NM_001080397    SLC45A1
NM_018090   NECAP2
NM_013943   CLIC4
NM_032785   AGBL4
NM_001195684    TGFBR3



$ head hg19_refseq_extracted_3UTR.bed
chr14   50792327    50792946    NM_001003805|ATP5S|chr14|+  0   +
chr9    95473645    95477745    NM_001003800|BICD2|chr9|-   0   -
chr11   92623657    92629635    NM_001008781|FAT3|chr11|+   0   +
chr6    137245023   137246776   NM_001008783|SLC35D3|chr6|+ 0   +
chr16   90061167    90063028    NR_003227|AFG3L1P|chr16|+   0   +
chr16   90061101    90063028    NR_003226|AFG3L1P|chr16|+   0   +
chr14   55611834    55612148    NR_003225|LGALS3|chr14|+    0   +
chr14   101459573   101459646   NR_003224|SNORD114-31|chr14|+   0   +
chr14   101458256   101458326   NR_003223|SNORD114-30|chr14|+   0   +
chr14   101456428   101456496   NR_003222|SNORD114-29|chr14|+   0   +

```


```
$ grep 'NM_001003805' hg19_refseq_genes.txt
ATP5S   NM_001003805    chr14   +   50779046    50792946    50779738    50792349    4   50779046,50788200,50789228,50792326,    50779778,50788312,50789437,50792946,

chr14   50792327        50792946        NM_001003805|ATP5S|chr14|+      0       +


$ grep 'NM_001003800' hg19_refseq_genes.txt
BICD2   NM_001003800    chr9    -   95473644    95527083    95477435    95527026    7   95473644,95480078,95480820,95482581,95484937,95491305,95526786, 95477745,95480230,95481864,95483037,95485090,95491518,95527083,

chr9    95473645        95477745        NM_001003800|BICD2|chr9|-       0       -

```



### DaPars APA test data
CFIm25 links alternative polyadenylation to glioblastoma tumour suppression
```
SRP017305 

SRX517304 SRR1238549 ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/sralite/ByExp/litesra/SRX/SRX517/SRX517304/SRR1238549/SRR1238549.sra
SRX517305 SRR1238550 ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/sralite/ByExp/litesra/SRX/SRX517/SRX517305/SRR1238550/SRR1238550.sra
SRX517306 SRR1238551 ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/sralite/ByExp/litesra/SRX/SRX517/SRX517306/SRR1238551/SRR1238551.sra
SRX517307 SRR1238552 ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/sralite/ByExp/litesra/SRX/SRX517/SRX517307/SRR1238552/SRR1238552.sra
```

```
GSM1369391: Hela cell CFIm25 knock down rep2; Homo sapiens; RNA-Seq
1 ILLUMINA (Illumina HiSeq 2000) run: 165.2M spots, 33.4G bases, 22.6Gb downloads
Accession: SRX517307
Select item 716953
2.
GSM1369390: Hela cell CFIm25 knock down rep1; Homo sapiens; RNA-Seq
1 ILLUMINA (Illumina HiSeq 2000) run: 160.1M spots, 32.3G bases, 22Gb downloads
Accession: SRX517306
Select item 716952
3.
GSM1369389: Hela cell wild type rep2; Homo sapiens; RNA-Seq
1 ILLUMINA (Illumina HiSeq 2000) run: 161.2M spots, 32.6G bases, 21.9Gb downloads
Accession: SRX517305
Select item 716951
4.
GSM1369388: Hela cell wild type rep1; Homo sapiens; RNA-Seq
1 ILLUMINA (Illumina HiSeq 2000) run: 164.8M spots, 33.3G bases, 22.5Gb downloads
Accession: SRX517304
```

#### extract fastq files
```
nohup fastq-dump --split-files -I SRR1238549.sra &
```




### run DaPars

python 2 environment

```
$ python /home/wzk/anaconda3/envs/kcmRNA/bin/dapars/src/DaPars_main.py DaPars_test_data_configure.txt
```

or

```
$ python DaPars_main.py --wig1 /home/wzk/APA_test/coverage/SRR1238549.wig --wig2 /home/wzk/APA_test/coverage/SRR1238551.wig --annotation Homo_sapiens.GRCh38.85.3UTR_final  --outdir PDUI/SRR1238551___SRR1238549  --prefix Compare  --coverage 30 --number1 1 --number2 1 --foldchange 0.59 --FDR 0.05 --PDUI 0.2
```

output file:
```

[Tue 07 Nov 2017 04:46:41 AM ] Start Analysis ...
[Tue 07 Nov 2017 04:46:41 AM ] Loading coverage ...
[Tue 07 Nov 2017 04:47:00 AM ] Loading coverage finished ...
[Tue 07 Nov 2017 05:59:34 AM ] Filtering the result ...
[Tue 07 Nov 2017 05:59:45 AM ] Finished!


$ less /home/wzk/APA_test/test/test_All_Prediction_Results.txt
Gene    fit_value       Predicted_Proximal_APA  Loci    A_1_long_exp    A_1_short_exp   A_1_PDUI        B_1_long_exp    B_1_short_exp   B_1_PDUI        Group_A_Mean_PDUI       Group_B_Mean_PDUI       PDUI_Group_diff P_val   adjusted.P_val  Pass_Filter
uc064pcz.1|YWHAZ|chr8|- 71.6    100948699       chr8:100948614-100948900        75.47   0.00    1.00    50.30   0.00    1.00    1.0     1.0
     0.0     1.0     1.0     N
ENST00000615597|TMEM106C|chr12|+        14.9    47966165        chr12:47965964-47967192 NA      NA      NA      NA      NA      NA      NA
      NA      NA      NA      NA      N
ENST00000309268|EEF1A1|chr6|-   52528.5 73517733        chr6:73517515-73517934  540.22  434.72  0.55    301.59  323.74  0.48    0.55    0.48    0.07    0.00554131958729        0.0364436508162 N

```

### Generate region annotation

```bash
$ python /home/wzk/anaconda3/envs/kcmRNA/bin/dapars/src/DaPars_Extract_Anno.py -b hg19_refseq_whole_gene.bed -s hg19_4_19_2012_Refseq_id_from_UCSC.txt -o hg19_refseq_extracted_3UTR-1.bed
```



### bam2wig
```
$ git clone https://github.com/MikeAxtell/bam2wig.git

$ ./bam2wig 
bam2wig
Version 1.4

USAGE:
bam2wig [options] [.bam]

DEPENDENCIES:
samtools [in PATH]
wigToBigWig [in PATH -- optional]

OPTIONS:
-t [float] : Threshold for reporting. Defaults to 0 (all depths reported)
-s [top/bottom/both] : Strand to report. Defaults to both. 'bottom' will quantify in negative numbers. Used in conjunction with option -g will subset the loci to those on the indicated strand.
-r [string] : Limit analysis to specified read group
-l [integer] : Minimum size of read to report. Default: no minimum.
-L [integer] : Maximum size of read to report. Default: no maximum.
-c [chr:start-stop] : Limit analysis to the indicated locus. 
-g [string] : Path to a GFF3 file. Loci in the GFF3 will be reported. Negates any setting of -c.
-F [integer] : Argument to be passed to samtools view's -F option ... which alignments will be ignored. Defaults to 3844
-m : Normalize reads to reads per million before calculating depths
-d : Treat as degradome/PARE data .. tally only the depths of 5' ends. Option -s must be either 'bottom' or 'top'
-D : Name of output directory. Defaults to [/YourBamsPath/YourBamsBasename_bam2wig/].
-i : Instead of abundance, instead report fraction of reads meeting the size requirements given by -l and/or -L
-h : Get help (print this message)
-v : Print version number and quit

```

#### run bam2wig
```
$ /home/wzk/anaconda3/envs/py35/bin/bam2wig/bam2wig  Aligned.sortedByCoord.out.bam

bam2wig version 1.4
Tue Nov  7 02:15:52 EST 2017
Host: ubuntu
Working Directory: /home/wzk/APA_test/mapping/SRR1238549
Checking dependencies
    samtools: present at /home/wzk/anaconda3/envs/py35/bin/samtools
    wigToBigWig: present at /home/soft/wigToBigWig
BAM file: Aligned.sortedByCoord.out.bam
Output Directory: ./Aligned.sortedByCoord.out_bam2wig
Ignored alignment types (sum of bits for samtools view -F): 3844
BAM index Aligned.sortedByCoord.out.bam.bai was not found. Generating using samtools index
    Chromosomes in genome from chr1 to chrY_KI270740v1_random
    Read Groups in BAM file: None
Threshold: 0 read depth
Strand: both
Read Group: None -- all reads used
Min read size: No minimum
Max read size: No maximum
Locus/Loci: None (whole genome)

Phase One: Generating depths

Phase Two: Processing depths

Wiggle file written to ./Aligned.sortedByCoord.out_bam2wig/Aligned.sortedByCoord.out.wig

Phase Three: Writing bigwig file
line 3898324 of ./Aligned.sortedByCoord.out_bam2wig/Aligned.sortedByCoord.out.wig: chromosome chrM has 16569 bases, but item ends at 16572
bigwig file at ./Aligned.sortedByCoord.out_bam2wig/Aligned.sortedByCoord.out.bigwig

Completed at Tue Nov  7 02:19:48 EST 2017
```

outfile:
```
$ head  Aligned.sortedByCoord.out.wig 
variableStep chrom=chr1 span=2
14553 1
variableStep chrom=chr1 span=12
14555 2
variableStep chrom=chr1 span=45
14567 3
variableStep chrom=chr1 span=42
14612 5
variableStep chrom=chr1 span=2
14654 4

```


#### bedGraphToBigWig
```
$ bedGraphToBigWig
bedGraphToBigWig v 4 - Convert a bedGraph file to bigWig format.
usage:
   bedGraphToBigWig in.bedGraph chrom.sizes out.bw
where in.bedGraph is a four column file in the format:
      <chrom> <start> <end> <value>
and chrom.sizes is a two-column file/URL: <chromosome name> <size in bases>
and out.bw is the output indexed big wig file.
If the assembly <db> is hosted by UCSC, chrom.sizes can be a URL like
  http://hgdownload.cse.ucsc.edu/goldenPath/<db>/bigZips/<db>.chrom.sizes
or you may use the script fetchChromSizes to download the chrom.sizes file.
If not hosted by UCSC, a chrom.sizes file can be generated by running
twoBitInfo on the assembly .2bit file.
The input bedGraph file must be sorted, use the unix sort command:
  sort -k1,1 -k2,2n unsorted.bedGraph > sorted.bedGraph
options:
   -blockSize=N - Number of items to bundle in r-tree.  Default 256
   -itemsPerSlot=N - Number of data points bundled at lowest level. Default 1024
   -unc - If set, do not use compression.
```


```
$ genomeCoverageBed -i SRR1238549.bed -bg -g /home/wzk/database/hg38/hg38.fa > SRR1238549.cov
Less than the req'd two fields were encountered in the genome file (/home/wzk/database/hg38/hg38.fa) at line 1.  Exiting.
```


As others already pointed out, `bedtools` genome file is also known as `chrom.sizes` file. If you can't download it, you can generate it yourself from an indexed FASTA file:
```
$ samtools faidx /home/wzk/database/hg38/hg38.fa
$ cut -f 1,2 /home/wzk/database/hg38/hg38.fa.fai > /home/wzk/database/hg38/hg38.chrom.size
$ genomeCoverageBed -i SRR1238549.bed -bg -g /home/wzk/database/hg38/hg38.chrom.size > SRR1238549.cov

$ head SRR1238549.cov
chr1    14478   14552   1
chr1    14552   14554   2
chr1    14554   14566   3
chr1    14566   14579   4
chr1    14579   14611   3
chr1    14611   14653   5
chr1    14653   14655   4
chr1    14655   14667   3
chr1    14667   14712   2
chr1    14713   14737   1
```


```
$ bedGraphToBigWig SRR1238549.cov /home/wzk/database/hg38/hg38.chrom.size SRR1238549.bw
SRR1238549.cov is not case-sensitive sorted at line 644332.  Please use "sort -k1,1 -k2,2n" with LC_COLLATE=C,  or bedSort and try again.
```

```
$ wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedSort
$ bedSort SRR1238549.cov SRR1238549_sorted.cov
$ bedGraphToBigWig SRR1238549_sorted.cov /home/wzk/database/hg38/hg38.chrom.size SRR1238549.bw
```



```
$ gff3ToGenePred Homo_sapiens.GRCh38.85.gff3 Homo_sapiens.GRCh38.85.GenePred
```

out file
```
$ tail  Homo_sapiens.GRCh38.85.GenePred
transcript:ENST00000420190  1   +   923927  939291  924431  939291  7   923927,925921,930154,931038,935771,939039,939274,   924948,926013,930336,931089,935896,939129,939291,   0   gene:ENSG00000187634    cmpl    cmpl    0,1,0,2,2,1,1,
transcript:ENST00000422528  1   +   760910  761989  761989  761989  2   760910,761777,  761154,761989,  0   gene:ENSG00000229905    none    none    -1,-1,
transcript:ENST00000332831  1   -   685715  686654  685715  686654  1   685715, 686654, 0   gene:ENSG0000027354cmpl cmpl    0,
transcript:ENST00000426406  1   -   450739  451678  450739  451678  1   450739, 451678, 0   gene:ENSG0000027856cmpl cmpl    0,
transcript:ENST00000624735  1   -   184926  200322  184926  200086  15  184926,184976,185528,186316,187128,187269,187379,187754,188101,188129,188438,188488,188790,195258,200049,   184971,185049,185559,186469,187267,187287,187577,187886,188105,188266,188486,188584,188889,195416,200322,   0   gene:ENSG00000279457    cmpl    cmpl    0,2,1,1,0,0,0,0,2,0,0,0,0,1,0,
transcript:ENST00000623083  1   -   184924  195411  185216  195411  11  184924,185490,186316,187128,187375,187754,188125,188438,188488,188790,195262,   185350,185559,186469,187287,187577,187886,188266,188486,188584,188902,195411,   0   gene:ENSG00000279457    cmpl    cmpl    1,1,1,1,0,0,0,0,0,2,0,
transcript:ENST00000623834  1   -   184922  195411  185216  195411  10  184922,185490,187375,187754,188021,188129,188438,188488,188790,195258,  185350,185559,187577,187886,188028,188266,188486,188584,188892,195411,  0   gene:ENSG0000027945cmpl cmpl    1,1,0,0,2,0,0,0,0,0,
transcript:ENST00000624431  1   +   182392  184158  182708  184158  3   182392,183113,183921,   182746,183240,184158,   0   gene:ENSG00000279928    cmpl    cmpl    0,2,0,
transcript:ENST00000493797  1   -   139789  140339  140339  140339  2   139789,140074,  139847,140339,  0   gene:ENSG00000239906    none    none    -1,-1,
transcript:ENST00000335137  1   +   69090   70008   69090   70008   1   69090,  70008,  0   gene:ENSG0000018609cmpl cmpl    0,

```


### draw plot

```
$ python draw_gene_coverage_new.py --gff_file Homo_sapiens.GRCh38.85.gff3-1   --gene_list_file /home/wzk/APA_test/gene_list --bam_files mapping/SRR1238549/Aligned.sortedByCoord.out.bam,mapping/SRR1238551/Aligned.sortedByCoord.out.bam --out_dir plot

```
