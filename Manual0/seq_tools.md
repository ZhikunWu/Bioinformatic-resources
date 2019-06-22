
### [FASTX-Toolkit](http://hannonlab.cshl.edu/fastx_toolkit/)
```
$ conda install -c biobuilds fastx-toolkit
```


#### complement and reverse sequence
```
$ fastx_reverse_complement -i LGC0-ST-1_test_merge.fasta -o LGC0-ST-1_test_merge_reverse.fasta
fastx_reverse_complement: Invalid input: This looks like a multi-line FASTA file.
Line 3 contains a nucleotides string instead of a '>' prefix.
FASTX-Toolkit can't handle multi-line FASTA files.
Please use the FASTA-Formatter tool to convert this file into a single-line FASTA.

```


```
$ fasta_formatter -w 0 -i  LGC0-ST-1_test_merge.fasta  -o LGC0-ST-1_test_merge_oneline.fasta
$ fastx_reverse_complement -i LGC0-ST-1_test_merge_oneline.fasta  -o LGC0-ST-1_test_merge_reverse.fasta
```

get 150 bp length
```
$ fastx_trimmer -f 1 -l 150 -i LGC0-ST-1_test_merge_reverse.fasta  -o LGC0-ST-1_test_merge_reverse_150.fasta
```


### [seqkit](https://bioinf.shenwei.me/seqkit/)

stats

```
$ seqkit stats LGC0-ST-1_test_merge_reverse.fasta
file                                format  type  num_seqs    sum_len  min_len  avg_len  max_len
LGC0-ST-1_test_merge_reverse.fasta  FASTA   DNA     31,777  5,718,715      131      180      251


$ seqkit stats LGC0-ST-1_test_merge_reverse_150.fasta
file                                    format  type  num_seqs    sum_len  min_len  avg_len  max_len
LGC0-ST-1_test_merge_reverse_150.fasta  FASTA   DNA     31,777  4,705,123      131    148.1      150

```



### fastq_quality_filter

Quality cut-off value (0-100) [20]

Minimum percent of bases that must have that quality (1-100) [90]

The quality value of every base in the read is compared to the quality value cut-off, and the percentage of bases having a quality score equal or higher than the cut-off value is calculated. If the percentage is not sufficient, the read is discarded. For example, if you set the percentage to 100, the quality value in every position must be equal or higher than the cut-off.

```
$ fastq_quality_filter -q 20 -p 90 -i LGC0-ST-1_test.R1.fq -o LGC0-ST-1_trim.R1.fq 
```


output file
```

$ grep -c '^@' LGC0-ST-1_test.R1.fq
100000

$ grep -c '^@' LGC0-ST-1_trim.R1.fq
90776

```

it can not conduct PE reads

