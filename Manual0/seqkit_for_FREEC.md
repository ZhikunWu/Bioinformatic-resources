# [seqkit](https://github.com/shenwei356/seqkit) for [FREEC](http://boevalab.com/FREEC/)

## [seqkit usage and examples](https://bioinf.shenwei.me/seqkit/usage/#usage-and-examples)

## seqkit function

* **seq**: Validating and transforming sequences
* **subseq**: Getting subsequences by region/GTF/BED
* **sliding**: Sliding sequences
* **stat**: Simple statistics
* **faidx**: Creating FASTA index files
* **fx2tab**: Converting FASTA/Q to tabular format with extra information
* **tab2fx**: Converting tabular format to FASTA/Q format
* **fq2fa**: Converting FASTQ format to FASTA
* **grep**: Searching sequences by patterns/IDs/motifs
* **locate**: Locating subsequences/motifs
* **rmdup**: Removing duplicated sequences by ID/name/seq
* **common**: Finding common sequences of multiple files by ID/name/seq
* **split**: Splitting sequences into files by ID/seq region/size/parts
* **sample**: Sampling sequences by number or proportion
* **head**: Printing the first N FASTA/Q records
* **replace**: Editing name/sequence by regular expression
* **rename**: Renaming duplicated IDs
* **shuffle**: Shuffling sequences
* **sort**: Sorting sequences by ID/name/sequence/length


## install seqkit

```
$ conda install -c bioconda seqkit
```

## Stats for fasta

```
$ seqkit stat -a -T Arabidopsis_thaliana.TAIR10.dna.toplevel.fa  -o Arabidopsis_thaliana.TAIR10.dna.toplevel_summary.txt
```

output file

```
$ cat Arabidopsis_thaliana.TAIR10.dna.toplevel_summary.txt
file    format  type    num_seqs    sum_len min_len avg_len max_len Q1  Q2  Q3  sum_gap N50
Arabidopsis_thaliana.TAIR10.dna.toplevel.fa FASTA   DNA 7   119667750   154478  17095392.9  30427671    366924  19698289    26975502    0   23459830
```




## Split the genome into seq with each chromosome

```
$ seqkit split --by-id -O temp Arabidopsis_thaliana.TAIR10.dna.toplevel.fa
[INFO] split by ID. idRegexp: ^([^\s]+)\s?
[INFO] read sequences ...
[INFO] read 7 sequences
[INFO] write 1 sequences to file: temp/Arabidopsis_thaliana.TAIR10.dna.toplevel.id_2.fa
[INFO] write 1 sequences to file: temp/Arabidopsis_thaliana.TAIR10.dna.toplevel.id_3.fa
[INFO] write 1 sequences to file: temp/Arabidopsis_thaliana.TAIR10.dna.toplevel.id_4.fa
[INFO] write 1 sequences to file: temp/Arabidopsis_thaliana.TAIR10.dna.toplevel.id_5.fa
[INFO] write 1 sequences to file: temp/Arabidopsis_thaliana.TAIR10.dna.toplevel.id_Mt.fa
[INFO] write 1 sequences to file: temp/Arabidopsis_thaliana.TAIR10.dna.toplevel.id_Pt.fa
[INFO] write 1 sequences to file: temp/Arabidopsis_thaliana.TAIR10.dna.toplevel.id_1.fa
```

**--by-id** means split the genome using seq id, **-O** means the out directory


## Create fasta index file

```
$ seqkit faidx Arabidopsis_thaliana.TAIR10.dna.toplevel.fa
[INFO] create FASTA index for Arabidopsis_thaliana.TAIR10.dna.toplevel.fa
```

output file
```
$ cat Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.fai
1	30427671	55	60	61
2	19698289	30934909	60	61
3	23459830	50961558	60	61
4	18585056	74812441	60	61
5	26975502	93707303	60	61
Mt	366924	121132452	60	61
Pt	154478	121505547	60	61
```



## The files for FREEC

### Fasta file of each chromosome
We need split the reference genome to fasta file with each chromosome:

```
$ seqkit split --by-id -O Chr Arabidopsis_thaliana.TAIR10.dna.toplevel.fa

$ tree /home/wzk/database/GENOME/arabidopsis/Chr

├── 1.fasta
├── 2.fasta
├── 3.fasta
├── 4.fasta
├── 5.fasta
├── Mt.fasta
└── Pt.fasta
```



### Length of each chromosome

Get the seqeunce id and length:
```
$ seqkit faidx Arabidopsis_thaliana.TAIR10.dna.toplevel.fa

$ cut -f 1-2 Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.fai > Arabidopsis_thaliana_chr_length.txt
```

output file:

```
$ cat  Arabidopsis_thaliana_chr_length.txt
1   30427671
2   19698289
3   23459830
4   18585056
5   26975502
Mt  366924
Pt  154478
```
