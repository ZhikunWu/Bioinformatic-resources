## history for 16S rDNA anslysis

### test the experiment design

```
$ mkdir temp result
$ validate_mapping_file.py -m mappingfile.txt
No errors or warnings were found in mapping file.

```

creat tree files
```
-rw-r--r-- 1 2.4K Sep  3 22:49 mappingfile_corrected.txt
-rw-r--r-- 1 8.1K Sep  3 22:49 mappingfile.html
-rw-r--r-- 1   44 Sep  3 22:49 mappingfile.log
```

### combine paired-end reads

```
$ join_paired_ends.py -f PE250_1.fq.gz -r PE250_2.fq.gz -m fastq-join -o temp/PE250_join

burrito.util.ApplicationNotFoundError: Cannot find fastq-join. Is it installed? Is it in your path?
```
answer
```
su root
sudo apt install ea-utils
```
rerun
```
$ join_paired_ends.py -f PE250_1.fq.gz -r PE250_2.fq.gz -m fastq-join -o temp/PE250_join
```
creat three files
```
$ tree temp/
temp/
└── PE250_join
    ├── fastqjoin.join.fastq
    ├── fastqjoin.un1.fastq
    └── fastqjoin.un2.fastq
```

### extract barcodes

``` 
extract_barcodes.py -f temp/PE250_join/fastqjoin.join.fastq -m mappingfile.txt -o temp/PE250_barcode -c barcode_paired_stitched --bc1_len 0 --bc2_len 6 -a --rev_comp_bc2
```
creat file files
```
temp/
├── PE250_barcode
│   ├── barcodes.fastq
│   ├── barcodes_not_oriented.fastq
│   ├── reads1_not_oriented.fastq
│   ├── reads2_not_oriented.fastq
│   └── reads.fastq

```

### split samples

```
$ split_libraries_fastq.py -i temp/PE250_barcode/reads.fastq -b temp/PE250_barcode/barcodes.fastq -m mappingfile.txt -o temp/PE250_split -q 20 --max_bad_run_length 3 --min_per_read_length_fraction 0.75 --max_barcode_errors 0 --barcode_type 6
```

creat three files

```
└── temp
    └── PE250_split
        ├── histograms.txt
        ├── seqs.fna
        └── split_library_log.txt

```

### remove adapter

```
$ cutadapt -g AACMGGATTAGATACCCKG -a GGAAGGTGGGGATGACGT -e 0.15 -m 300 --discard-untrimmed temp/PE250_split/seqs.fna -o temp/PE250_P5.fa
This is cutadapt 1.13 with Python 2.7.12
Command line parameters: -g AACMGGATTAGATACCCKG -a GGAAGGTGGGGATGACGT -e 0.15 -m 300 --discard-untrimmed temp/PE250_split/seqs.fna -o temp/PE250_P5.fa
Trimming 2 adapters with at most 15.0% errors in single-end mode ...
Finished in 28.67 s (22 us/read; 2.67 M reads/minute).

=== Summary ===

Total reads processed:               1,277,436
Reads with adapters:                 1,277,194 (100.0%)
Reads that were too short:               8,849 (0.7%)
Reads written (passing filters):     1,268,345 (99.3%)

Total basepairs processed:   522,379,897 bp
Total written (filtered):    495,607,409 bp (94.9%)

=== Adapter 1 ===

Sequence: GGAAGGTGGGGATGACGT; Type: regular 3'; Length: 18; Trimmed: 202757 times.

No. of allowed errors:
0-5 bp: 0; 6-12 bp: 1; 13-18 bp: 2

Bases preceding removed adapters:
  A: 96.3%
  C: 1.5%
  G: 0.8%
  T: 1.3%
  none/other: 0.0%
WARNING:
    The adapter is preceded by "A" extremely often.
    The provided adapter sequence may be incomplete.
    To fix the problem, add "A" to the beginning of the adapter sequence.

Overview of removed sequences
length	count	expect	max.err	error counts
3	3	19959.9	0	3
4	4	4990.0	0	4
6	2	311.9	0	2
8	1	19.5	1	1
11	1	0.3	1	1
13	1	0.0	1	1
15	9	0.0	2	9
17	42	0.0	2	42
18	202626	0.0	2	202626
19	56	0.0	2	56
20	1	0.0	2	1
21	1	0.0	2	1
32	1	0.0	2	1
38	1	0.0	2	1
39	1	0.0	2	1
41	1	0.0	2	1
309	2	0.0	2	2
310	1	0.0	2	1
311	3	0.0	2	3

=== Adapter 2 ===

Sequence: AACMGGATTAGATACCCKG; Type: regular 5'; Length: 19; Trimmed: 1074437 times.

No. of allowed errors:
0-5 bp: 0; 6-12 bp: 1; 13-19 bp: 2

Overview of removed sequences
length	count	expect	max.err	error counts
3	2	19959.9	0	2
7	1	78.0	1	0 1
8	2	19.5	1	1 1
10	6	1.2	1	4 2
11	1	0.3	1	1
12	3	0.1	1	2 1
13	5	0.0	1	3 2
14	24	0.0	2	17 7
15	51	0.0	2	32 14 5
16	71	0.0	2	56 12 3
17	134	0.0	2	92 30 12
18	327	0.0	2	189 117 21
19	1059175	0.0	2	1056863 2069 243
20	13846	0.0	2	1817 10955 1074
21	744	0.0	2	5 10 729
22	1	0.0	2	1
23	2	0.0	2	2
24	1	0.0	2	1
25	2	0.0	2	2
27	5	0.0	2	5
28	2	0.0	2	2
29	2	0.0	2	2
30	1	0.0	2	1
31	2	0.0	2	2
32	10	0.0	2	10
49	1	0.0	2	1
51	1	0.0	2	1
166	1	0.0	2	1
291	6	0.0	2	6
401	2	0.0	2	2
409	1	0.0	2	1
443	1	0.0	2	1
460	2	0.0	2	2
465	2	0.0	2	2

WARNING:
    One or more of your adapter sequences may be incomplete.
    Please see the detailed output above.

```
creat one file
```
temp/PE250_P5.fa
```


### format to Usearch
```
sed 's/ .*/;/g;s/>.*/&&/g;s/;>/;barcodelabel=/g;s/_[0-9]*;$/;/g' temp/PE250_P5.fa > temp/seqs_usearch.fa
```

### dereplication

```
$ usearch10 -derep_fulllength temp/seqs_usearch.fa -fastaout temp/seqs_unique.fa -minuniquesize 2 -sizeout
usearch v10.0.240_i86linux32, 4.0Gb RAM (264Gb total), 40 cores
(C) Copyright 2013-17 Robert C. Edgar, all rights reserved.
http://drive5.com/usearch

License: yxliu@genetics.ac.cn



usearch10 -derep_fulllength temp/seqs_usearch.fa -fastaout temp/seqs_unique.fa -minuniquesize 2 -sizeout

---Fatal error---
-derep_fulllength obsolete, use -fastx_uniques

```
rerun
```
$ usearch10 -fastx_uniques  temp/seqs_usearch.fa -fastaout temp/seqs_unique.fa -minuniquesize 2 -sizeout
usearch v10.0.240_i86linux32, 4.0Gb RAM (264Gb total), 40 cores
(C) Copyright 2013-17 Robert C. Edgar, all rights reserved.
http://drive5.com/usearch

License: yxliu@genetics.ac.cn

00:03 607Mb   100.0% Reading temp/seqs_usearch.fa
00:03 574Mb  CPU has 40 cores, defaulting to 10 threads
00:04 915Mb   100.0% DF
00:05 935Mb  1268345 seqs, 686530 uniques, 624363 singletons (90.9%)
00:05 935Mb  Min size 1, median 1, max 18774, avg 1.85
62167 uniques written, 182874 clusters size < 2 discarded (26.6%)
```
creat one file 
```
temp/seqs_unique.fa
```

### cluster OTU

```
$ usearch10 -cluster_otus temp/seqs_unique.fa -otus temp/otus.fa -uparseout temp/uparse.txt -relabel Otu
usearch v10.0.240_i86linux32, 4.0Gb RAM (264Gb total), 40 cores
(C) Copyright 2013-17 Robert C. Edgar, all rights reserved.
http://drive5.com/usearch

License: yxliu@genetics.ac.cn

02:46 84Mb    100.0% 5486 OTUs, 9187 chimeras
```

output two files

```
temp/otus.fa
temp/uparse.txt
```

### remove chimeras

```
$ usearch10 -uchime2_ref temp/otus.fa -db rdp_gold.fa -chimeras temp/otus_chimeras.fa -notmatched temp/otus_rdp.fa -uchimeout temp/otus_rdp.uchime -strand plus -mode sensitive -threads 30
usearch v10.0.240_i86linux32, 4.0Gb RAM (264Gb total), 40 cores
(C) Copyright 2013-17 Robert C. Edgar, all rights reserved.
http://drive5.com/usearch

License: yxliu@genetics.ac.cn

00:00 43Mb    100.0% Reading temp/otus.fa
00:01 75Mb    100.0% Reading rdp_gold.fa 
00:01 42Mb    100.0% Converting to upper case
00:01 43Mb    100.0% Word stats              
00:01 43Mb    100.0% Alloc rows
00:03 156Mb   100.0% Build index
01:03 697Mb   100.0% Chimeras 2651/5486 (48.3%), in db 53 (1.0%), not matched 2782 (50.7%)

WARNING: Input has lower-case masked sequences
```
output thee files
```
temp/otus_chimeras.fa
temp/otus_rdp.fa
temp/otus_rdp.uchime
```

and then
```
grep '>' temp/otus_chimeras.fa | sed 's/>//g' > temp/otus_chimeras.id
filter_fasta.py -f temp/otus.fa -o temp/otus_non_chimera.fa -s temp/otus_chimeras.id -n
```


### 去除非细菌序列
```
align_seqs.py -i temp/otus_non_chimera.fa -t /home/wzk/database/greengenes_release/gg_13_5/gg_13_8_otus/rep_set_aligned/97_otus.fasta -o temp/aligned/
```
output three files

```
└── temp
    ├── aligned
    │   ├── otus_non_chimera_aligned.fasta
    │   ├── otus_non_chimera_failures.fasta
    │   └── otus_non_chimera_log.txt

```

### 获得不像细菌的OTU ID

```
grep '>' temp/aligned/otus_non_chimera_failures.fasta | cut -f 1 -d ' ' | sed 's/>//g' > temp/aligned/otus_non_chimera_failures.id

filter_fasta.py -f temp/otus_non_chimera.fa -o temp/otus_rdp_align.fa -s temp/aligned/otus_non_chimera_failures.id -n

```

### 重命名OTU，这就是最终版的代表性序列，即Reference

```
awk 'BEGIN {n=1}; />/ {print ">OTU_" n; n++} !/>/ {print}' temp/otus_rdp_align.fa > result/rep_seqs.fa
```

### 生成OTU表
```
usearch10 -usearch_global temp/seqs_usearch.fa -db result/rep_seqs.fa -otutabout temp/otu_table.txt -biomout temp/otu_table.biom -strand plus -id 0.97 -threads 10
```
output 2 files
```
temp/otu_table.txt
temp/otu_table.biom
```

### 物种注释Taxonomy assignment

```
$ assign_taxonomy.py -i result/rep_seqs.fa -r /home/wzk/database/greengenes_release/gg_13_5/gg_13_8_otus/rep_set/97_otus.fasta -t /home/wzk/database/greengenes_release/gg_13_5/gg_13_8_otus/taxonomy/97_otu_taxonomy.txt -m rdp -o result

Error in assign_taxonomy.py: RDP classifier is not installed or not accessible to QIIME. See install instructions here: http://qiime.org/install/install.html#rdp-install

If you need help with QIIME, see:
http://help.qiime.org

```

answer
```
wget https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/rdp_classifier_2.2.zip/download


export RDP_JAR_PATH=/home/wzk/anaconda3/envs/kc16SRNA/bin/rdp_classifier_2.2/rdp_classifier-2.2.jar:$RDP_JAR_PATH
```

install packargs
```

wget https://pypi.python.org/packages/79/e8/3d5474a4a4b324e19dc95f09c97409dd4ed6a5b7c17eb854158d47f95d5d/burrito-fillings-0.1.1.tar.gz#md5=ea65051e674aedfad8bbfdfa63f2c4d8
tar -zxf burrito-fillings-0.1.1.tar.gz
cd burrito-fillings-0.1.1/
python setup.py install

cp -r bfillings/ build/ /home/wzk/anaconda3/envs/kc16SRNA/lib/python2.7/site-packages


wget https://pypi.python.org/packages/b1/d1/b405ff6547f5826c1aea1ee09a89f634a146b6decda74a6016ba0519a780/burrito-0.9.1.tar.gz#md5=ef2b0bee1e8c037a535627a33e304d61
tar -zxf burrito-0.9.1.tar.gz
cd burrito-0.9.1/
python setup.py install



```
rerun
```
assign_taxonomy.py -i result/rep_seqs.fa -r /home/wzk/database/greengenes_release/gg_13_5/gg_13_8_otus/rep_set/97_otus.fasta -t /home/wzk/database/greengenes_release/gg_13_5/gg_13_8_otus/taxonomy/97_otu_taxonomy.txt  -o result
```
output three files
```
result/
├── rep_seqs.fa
├── rep_seqs_tax_assignments.log
└── rep_seqs_tax_assignments.txt
```

### OTU格式转换，添加信息
```
biom convert -i temp/otu_table.txt -o result/otu_table.biom --table-type="OTU table" --to-json
```


```
biom add-metadata -i result/otu_table.biom --observation-metadata-fp result/rep_seqs_tax_assignments.txt -o result/otu_table_tax.biom --sc-separated taxonomy --observation-header OTUID,taxonomy
```
output one file
```
otu_table_tax.biom
```

### OTU表数据筛选

按样品数据量过滤：选择counts>3000的样品
```
filter_samples_from_otu_table.py -i result/otu_table_tax.biom -o result/otu_table2.biom -n 3000
```

查看过滤后结果：只有25个样品，975个OTU
```
biom summarize-table -i result/otu_table2.biom
```

按OTU丰度过滤：选择相对丰度均值大于万分之一的OTU
```
filter_otus_from_otu_table.py --min_count_fraction 0.0001 -i result/otu_table2.biom -o result/otu_table3.biom
```

查看过滤后结果：只有25个样品，346个OTU
```
biom summarize-table -i result/otu_table3.biom
```
按物种筛选OTU表：去除p__Chloroflexi菌门
```
filter_taxa_from_otu_table.py -i result/otu_table3.biom -o result/otu_table4.biom -n p__Chloroflexi
```
查看过滤后结果：只有25个样品，307个OTU
```
biom summarize-table -i result/otu_table4.biom
```
转换最终biom格式OTU表为文本OTU表格
```
biom convert -i result/otu_table4.biom -o result/otu_table4.txt --table-type="OTU table" --to-tsv
```
OTU表格式调整方便R读取
```
sed -i '/# Const/d;s/#OTU //g;s/ID.//g' result/otu_table4.txt
```
筛选最终OTU表中对应的OTU序列
```
filter_fasta.py -f result/rep_seqs.fa -o temp/tax_rep4.fa -b result/otu_table4.biom
```

### 进化

```
clustalo -i result/rep_seqs.fa -o temp/rep_seqs_align.fa --seqtype=DNA --full --force --threads=30
```

```
filter_alignment.py -i temp/rep_seqs_align.fa -o temp/
```
output one file
```
temp/rep_seqs_align_pfiltered.fasta
```

### Alpha多样性

```
biom summarize-table -i result/otu_table4.biom
single_rarefaction.py -i result/otu_table4.biom -o temp/otu_table_rare.biom -d 2797
alpha_diversity.py -i temp/otu_table_rare.biom -o result/alpha.txt -t result/rep_seqs.tree -m shannon,chao1,observed_otus,PD_whole_tree
```

two files
```
temp/otu_table_rare.biom
result/alpha.txt
```

### Beta diversity

firstly install R packages
```
install.packages("optparse")
install.packages(c("biom","RColorBrewer")
```
run beta diversity
```
normalize_table.py -i result/otu_table4.biom -o temp/otu_table_css.biom -a CSS
biom convert -i temp/otu_table_css.biom -o result/otu_table_css.txt --table-type="OTU table" --to-tsv
sed -i '/# Const/d;s/#OTU //g;s/ID.//g' result/otu_table_css.txt
beta_diversity.py -i temp/otu_table_css.biom -o result/beta/ -t result/rep_seqs.tree -m bray_curtis,weighted_unifrac,unweighted_unifrac
sed -i 's/^\t//g' result/beta/*
```

### 按物种分类级别分类汇总

```
summarize_taxa.py -i result/otu_table4.biom -o result/sum_taxa # summary each level percentage
rm result/sum_taxa/*.biom
sed -i '/# Const/d;s/#OTU ID.//g' result/sum_taxa/* # format for R read
```
output .biom and .txt
```
result/sum_taxa/
├── otu_table4_L2.biom
├── otu_table4_L2.txt
├── otu_table4_L3.biom
├── otu_table4_L3.txt
├── otu_table4_L4.biom
├── otu_table4_L4.txt
├── otu_table4_L5.biom
├── otu_table4_L5.txt
├── otu_table4_L6.biom
└── otu_table4_L6.txt
```


### PCA
```

$ principal_coordinates.py -i result/beta/weighted_unifrac_otu_table_css.txt  -o result/beta/weighted_unifrac_PCoA.txt


/home/wzk/anaconda3/envs/kc16SRNA/lib/python2.7/site-packages/skbio/stats/ordination/_principal_coordinate_analysis.py:107: RuntimeWarning: The result contains negative eigenvalues. Please compare their magnitude with the magnitude of some of the largest positive eigenvalues. If the negative ones are smaller, it's probably safe to ignore them, but if they are large in magnitude, the results won't be useful. See the Notes section for more details. The smallest eigenvalue is -5.88628219644e-05 and the largest is 0.00202699395034.
  RuntimeWarning
```
output file
```

Eigvals 25
0.00202699395034        0.000463196603383       0.000418545305402       0.000259866407228

Proportion explained    25
0.487247652876  0.111342936066  0.100609682454  0.0624665391635 0.0449173905979 0.0422705

Species 0       0

Site    25      25
KO6     0.00491019250479        0.00182821497988        -0.00328239360036       -0.002216
KO3     0.0123288977616 0.0016032888779 0.00740019597842        0.00182985423353        0
KO5     0.0033829558839 0.00130963954608        -0.0002621523053        -0.00330791814193
WT8     0.0079423405696 -0.0112247560853        0.000594258604656       0.00581381674237
WT6     0.00334793618085        -0.00896057020676       -0.00126369315686       -0.006887
KO2     0.00738696131578        0.00520481461834        0.0018577681168 -0.00176352719135
KO7     -0.000351388838802      0.00435784860869        -0.00641732772608       0.0013151
OE2     -0.0169486681454        0.000201546061602       -0.00125429390877       0.0085312
WT1     0.00828723934505        -0.00133168132886       -0.00300218849252       0.0027230
WT2     0.00432188088306        0.0034574896084 -0.00345976289363       -3.85674036184e-0
WT4     0.00383719574246        0.000138059439093       -0.00255945260732       -0.004198
KO9     0.00485943835744        -0.000828610930193      -0.00240025660749       -0.000924
WT3     0.00424132918454        0.00143567522159        -0.00261513200588       -0.000865
KO4     0.00318283329076        0.00579561070978        -0.0019182669749        0.0002576
KO1     0.00767784524472        0.00257730123269        0.00435094111676        0.0019816
KO8     0.00208742254547        0.00380450940297        0.00230625686017        0.0002184
WT5     0.00157139778644        -0.0012604430242        -0.00444870561263       0.0023019
OE6     -0.0105130407353        -0.00543606423175       1.73484029802e-05       -0.003121
OE5     -0.0152913964394        0.00372892111478        0.0126415308179 -0.00217046967029
WT7     0.00610852920751        0.00307460565717        0.00267704409936        -0.000395
OE7     -0.011564263263 0.00034042797653        -0.000377406669145      0.00369241026989
WT9     0.00975655050679        -0.00426277340555       0.00384838556422        0.0026127
OE1     -0.0174624116227        0.00235872080598        -0.00351618297001       -0.001005
OE8     -0.0148123143817        -0.000615725413696      -0.0027786780398        -0.002449
OE9     -0.00828746288448       -0.00729604923517       0.00386216400939        -0.001932

Biplot  0       0

Site constraints        0       0
```

### PCA plot
```
make_2d_plots.py -i result/beta/weighted_unifrac_PCoA.txt  -o result/beta/weighted_unifrac_PCoA_plot -m mappingfile.txt


sed 's/#//g' mappingfile.txt > mappingfile-1.txt
```


### NMDS
```
$ less result/beta/weighted_unifrac_coords.txt

samples NMDS1   NMDS2   NMDS3
KO6     -0.43585143665  0.189556845948  0.153549623367
KO3     -1.36662374002  0.280553984672  -0.649466921073
KO5     -0.320029547689 0.0398982168044 -0.0101692828868
WT8     -1.04052566631  -1.14320412004  -0.354365923939
WT6     -0.409683376457 -0.845772088167 0.615573301124
KO2     -0.704940446193 0.417841257351  -0.0752590111632
KO7     0.0547675944354 0.459173955072  0.363746742056
OE2     2.01303908273   -0.14358512237  -0.226735081315
WT1     -0.869328668064 0.0998279096363 0.264427845079
WT2     -0.4565013477   0.475281372895  0.252510073255
WT4     -0.468622311175 -0.0468851396372        0.462829242984
KO9     -0.502791710853 -0.0675476966577        0.117396755263
WT3     -0.483262967858 0.152637678468  0.274189629079
KO4     -0.284804383152 0.391048786045  0.0389316760208
KO1     -0.741735355055 0.154181266075  -0.412676860938
KO8     -0.202571210693 0.306487922457  -0.208257216085
WT5     -0.104975706539 -0.0100726107321        0.141089128205
OE6     1.0740312821    -0.676352359747 0.249424002997
OE5     1.62148311477   0.168211691164  -1.17777182912
WT7     -0.623998220023 0.265509721259  -0.209738542534
OE7     1.20378521196   0.216404330924  -0.0234671175935
WT9     -1.1190673612   -0.296363158267 -0.178558062627
OE1     1.81455542116   0.495424976952  0.374423008134
OE8     1.51157745887   -0.0288247119729        0.523218761951
OE9     0.842074289627  -0.853432908128 -0.304843940243

stress  0.0606801337048 0       0
% variation explained   0       0       0
````




### hclust

```
library('ggdendro')
library('mefa')
otu_table <- read.table("result/beta/weighted_unifrac_otu_table_css-1.txt", header=T, sep= '\t', quote= '')
otu_table <- otu_table[, 2:ncol(otu_table)]
sample_num <- ncol(otu_table)
samples <- colnames(otu_table)
otu_table[upper.tri(otu_table)]="0"
otu_vector  <- as.numeric(as.vector(as.matrix(otu_table)))
otu_nozero <- otu_vector[otu_vector != 0]
new_otu <- vec2dist(otu_nozero, sample_num, labels=samples)
hc <-  hclust(new_otu, method="average") #"average" (= UPGMA)
ggdendrogram(hc, rotate = TRUE, size = 4, theme_dendro = TRUE, color = "red")
```


### adonis

```
compare_categories.py --method adonis -i result/beta/unweighted_unifrac_otu_table_css.txt  -m mappingfile.txt  -c genotype -o result/brad_adonis_out -n 999
```
output file
```
result/brad_adonis_out/adonis_results.txt
```

### anosim

```
compare_categories.py --method anosim -i result/beta/unweighted_unifrac_otu_table_css.txt  -m mappingfile.txt  -c genotype -o result/brad_adonis_out -n 999
```
output file
```
result/brad_adonis_out/anosim_results.txt
```

### run LEfSe
```
python LEfSeFormat.py --taxonomy  result/sum_taxa/otu_table4_L2.txt,result/sum_taxa/otu_table4_L3.txt --metadata  mappingfile.txt --classId  genotype --subclassId None --subjectId None --output result/sum_taxa/sum_taxa.txt

python /home/wzk/anaconda3/envs/qiime/bin/nsegata_lefse/format_input.py result/sum_taxa/sum_taxa.txt  hmp_aerobiosis_small.in -c 1 -s -1 -u -1 -o 1000000

python /home/wzk/anaconda3/envs/qiime/bin/nsegata_lefse/run_lefse.py hmp_aerobiosis_small.in hmp_aerobiosis_small.res


python /home/wzk/anaconda3/envs/qiime/bin/nsegata_lefse/plot_res.py hmp_aerobiosis_small.res hmp_aerobiosis_small.png


plot_cladogram.py hmp_aerobiosis_small.res hmp_aerobiosis_small.cladogram.pdf --format pdf
```



