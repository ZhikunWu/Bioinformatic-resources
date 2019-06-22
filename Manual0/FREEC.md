## FREEC

### [FREEC Example](http://boevalab.com/FREEC/tutorial.html#Example)
### [FREEC config](http://boevalab.com/FREEC/tutorial.html#CONFIG)
### [FREEC manual: not human](http://boevalab.com/FREEC/tutorial.html#notHuman)

### repare the length information of reference fasta
```
perl get_fasta_lengths.pl all.con.fasta
```

for reference **all.con.fasta** (rice ref)it will creat the file **res_all.con.fasta**
```
$ cat res_all.con.fasta

Chr1    43270923
Chr2    35937250
Chr3    36413819
Chr4    35502694
Chr5    29958434
Chr6    31248787
Chr7    29697621
Chr8    28443022
Chr9    23012720
Chr10   23207287
Chr11   29021106
Chr12   27531856
ChrUn   633585
ChrSy   592136
```
note: the file should be separated with tab

##### [get_fasta_lengths.pl](https://github.com/BoevaLab/FREEC/tree/master/scripts/get_fasta_lengths.pl) can be download from the web http://boevalab.com/FREEC/tutorial.html#CONFIG


### config file
```
$cat ZH.config

[general]
bedtools = /home/wzk/anaconda3/envs/evolution/bin/bedtools
BedGraphOutput = FALSE
breakPointThreshold = 0.7
breakPointType = 2
chrFiles = /home/wzk/database/GENOME/rice/O_sativa_v7/Chr/
chrLenFile = /home/wzk/database/GENOME/rice/O_sativa_v7/res_all.con.fasta
contamination = 0
contaminationAdjustment = FALSE
degree = 2
forceGCcontentNormalization = 0
minCNAlength = 1
maxThreads = 20
outputDir = /home/wzk/Project/B137/FREEC/ZH
ploidy = 2
readCountThreshold = 10
sambamba = /home/wzk/anaconda3/envs/evolution/bin/sambamba
SambambaThreads = 20
samtools = /home/wzk/anaconda3/envs/evolution/bin/samtools
window = 10000
step = 2000

[sample]

mateFile = /home/wzk/Project/B137/mapping/ZH_realigned.bam
inputFormat = BAM
mateOrientation=0

```
**note**
* when the directory of **chrFiles** contain the separated sequences of chromosomes it works. If the sequences were in one file (**all.con.fasta**) of this directory, there is something wrong with it. 
```
$ ls /home/wzk/database/GENOME/rice/O_sativa_v7/Chr/
Chr10.fasta  Chr12.fasta  Chr2.fasta  Chr4.fasta  Chr6.fasta  Chr8.fasta  ChrSy.fasta
Chr11.fasta  Chr1.fasta   Chr3.fasta  Chr5.fasta  Chr7.fasta  Chr9.fasta  ChrUn.fasta
```

* because the input bam file is sorted, so mateOrientation was set to be 0. For paired end Illumina reads this parameter should be "FR"


### usage:
#### run freec
```
freec -conf  ZH.config
```

#### output files:
```
└── ZH
    ├── GC_profile.10000bp.cnp
    ├── ZH_realigned.bam_CNVs
    ├── ZH_realigned.bam_info.txt
    ├── ZH_realigned.bam_ratio.txt
    └── ZH_realigned.bam_sample.cpn
```
#### GC content file was used to control
```
$ head GC_profile.10000bp.cnp
Chr1	0	0.401111	1
Chr1	2000	0.4081	1
Chr1	4000	0.4329	1
Chr1	6000	0.4499	1
Chr1	8000	0.4687	1
Chr1	10000	0.4713	1
Chr1	12000	0.4381	1
Chr1	14000	0.4162	1
Chr1	16000	0.4079	1
Chr1	18000	0.4064	1
```

#### the CNV results:
```
$ head ZH_realigned.bam_CNVs
Chr1	974000	997999	1	loss
Chr1	2612000	2639999	0	loss
Chr1	2934000	2951999	1	loss
Chr1	3138000	3177999	1	loss
Chr1	3192000	3263999	1	loss
Chr1	3256000	3285999	0	loss
Chr1	4592000	4615999	1	loss
Chr1	4928000	4949999	1	loss
Chr1	7220000	7237999	3	gain
Chr1	7752000	7761999	4	gain
```

#### information and parameters for bam file
```
$ head ZH_realigned.bam_info.txt
Program_Version	v10.6
Sample_Name	ZH_realigned.bam
Control_Used	False
CGcontent_Used	True
Mappability_Used	False
Looking_For_Subclones	False
Breakpoint_Threshold	0.7
Window	10000
Number_Of_Reads|Pairs_In_Sample	128865086
Number_Of_Reads|Pairs_In_Control	0
```

#### the ragio file 
```
$ head F2_realigned.bam_ratio.txt
Chromosome	Start	Ratio	MedianRatio	CopyNumber
Chr1	1	1.09613	1.01155	2
Chr1	2001	1.04637	1.01155	2
Chr1	4001	1.08311	1.01155	2
Chr1	6001	1.07326	1.01155	2
Chr1	8001	1.08656	1.01155	2
Chr1	10001	1.08941	1.01155	2
Chr1	12001	1.05037	1.01155	2
Chr1	14001	1.0303	1.01155	2
Chr1	16001	1.01864	1.01155	2

```

### change the ragio file to bed format
```
$ freec2bed.pl -f F2_realigned.bam_ratio.txt -p 2 > F2_realigned.bam_ratio_bed.txt
```

output file:
```
$ head F2_realigned.bam_ratio_bed.txt
chrChr1 1 974001 2.0231
chrChr1 976001 988001 1.439602
chrChr1 990001 2610001 1.992946
chrChr1 2612001 2630001 1.003518
chrChr1 2632001 2792001 1.95504
chrChr1 2794001 2804001 2.76088
chrChr1 2806001 2898001 2.0493
chrChr1 2900001 3022001 1.822482
chrChr1 3024001 3134001 2.09452
chrChr1 3136001 3254001 1.503768
```


#### change the retio file to circos format
```
$ freec2circos.pl -f F2_realigned.bam_ratio.txt -p 2 > F2_realigned.bam_ratio_circos.txt
```
outpu file
```
$ head F2_realigned.bam_ratio_circos.txt
hsChr1 1 1000 2.0231
hsChr1 1 21000 2.0231
hsChr1 21000 41000 2.0231
hsChr1 41000 61000 2.0231
hsChr1 61000 81000 2.0231
hsChr1 81000 101000 2.0231
hsChr1 101000 121000 2.0231
hsChr1 121000 141000 2.0231
hsChr1 141000 161000 2.0231
hsChr1 161000 181000 2.0231

```
It is special for human

Because our reference have 'Chr' for the description title of fasta, it may have something wrong with first column.


### [the definition of BAF](http://cnvkit.readthedocs.io/en/stable/baf.html)

In this context, the “B” allele is the non-reference allele observed in a germline heterozygous SNP, i.e. in the normal/control sample. Since the tumor cells’ DNA originally derived from normal cells’ DNA, most of these SNPs will also be present in the tumor sample. But due to allele-specific copy number alterations, loss of heterozygosity or allelic imbalance, the allelic frequency of these SNPs may be different in the tumor, and that’s evidence that one (or both) of the germline copies was gained or lost during tumor evolution. The shift in b-allele frequency is calculated relative to the expected heterozygous frequency 0.5, and minor allele frequencies are “mirrored” above and below 0.5 so that it does not matter which allele is considered the reference – the relative shift from 0.5 will be the same either way. (Multiple alternate alleles are not considered here.)