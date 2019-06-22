# Merge paired-end reads

## [vsearch](https://github.com/torognes/vsearch)

### install vsearch
```
$ conda install -c bioconda vsearch
```

### run vsearch
```
$ vsearch --fastq_mergepairs LGE0-AB-1_Consensus.R1.fastq --reverse LGE0-AB-1_Consensus.R2.fastq --fastq_minmergelen 180 --fastq_maxdiffs 2 --fastq_minovlen 10 --fastaout LGE0-AB-1_merge.fasta --fastaout_notmerged_fwd LGE0-AB-1_unmerge.R1.fasta --fastaout_notmerged_rev LGE0-AB-1_unmerge.R2.fasta --fasta_width 0
vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Merging reads 100%  
    147659  Pairs
     41592  Merged (28.2%)
    106067  Not merged (71.8%)

Pairs that failed merging due to various reasons:
     21389  too few kmers found on same diagonal
       408  potential tandem repeat
         5  too many differences
     13415  alignment score too low, or score drop to high
       293  overlap too short
     35251  merged fragment too short
     35306  staggered read pairs

Statistics of merged reads:
    211.80  Mean fragment length
     20.62  Standard deviation of fragment length
      0.02  Mean expected error in forward sequences
      0.01  Mean expected error in reverse sequences
      0.02  Mean expected error in merged sequences
      0.01  Mean observed errors in merged region of forward sequences
      0.00  Mean observed errors in merged region of reverse sequences
      0.01  Mean observed errors in merged region

```

## Pear
### install pear
```
$ conda install -c bioconda pear
```

Zhang, J., Kobert, K., Flouri, T. & Stamatakis, A.PEAR: a fast and accurate Illumina Paired-End reAd mergeRBioinformatics 30,
614–620 (2014)

### Run pear
```
$ pear -f Dendrophyllia1.R1.fq -r Dendrophyllia1.R2.fq -o  Dendrophyllia1_merge.fq
 ____  _____    _    ____ 
|  _ \| ____|  / \  |  _ \
| |_) |  _|   / _ \ | |_) |
|  __/| |___ / ___ \|  _ <
|_|   |_____/_/   \_\_| \_\

PEAR v0.9.6 [January 15, 2015]

Citation - PEAR: a fast and accurate Illumina Paired-End reAd mergeR
Zhang et al (2014) Bioinformatics 30(5): 614-620 | doi:10.1093/bioinformatics/btt593

Forward reads file.................: Dendrophyllia1.R1.fq
Reverse reads file.................: Dendrophyllia1.R2.fq
PHRED..............................: 33
Using empirical frequencies........: YES
Statistical method.................: OES
Maximum assembly length............: 999999
Minimum assembly length............: 50
p-value............................: 0.010000
Quality score threshold (trimming).: 0
Minimum read size after trimming...: 1
Maximal ratio of uncalled bases....: 1.000000
Minimum overlap....................: 10
Scoring method.....................: Scaled score
Threads............................: 1

Allocating memory..................: 200,000,000 bytes
Computing empirical frequencies....: DONE
  A: 0.235725
  C: 0.274860
  G: 0.267334
  T: 0.222081
  539 uncalled bases
Assemblying reads: 100%
Assembled reads ...................: 37,033 / 37,529 (98.678%)
Discarded reads ...................: 0 / 37,529 (0.000%)
Not assembled reads ...............: 496 / 37,529 (1.322%)
Assembled reads file...............: Dendrophyllia1_merge.fq.assembled.fastq
Discarded reads file...............: Dendrophyllia1_merge.fq.discarded.fastq
Unassembled forward reads file.....: Dendrophyllia1_merge.fq.unassembled.forward.fastq
Unassembled reverse reads file.....: Dendrophyllia1_merge.fq.unassembled.reverse.fastq
```

output file
```
@1
NGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGTGTGCTAGACGTTGGGGGTCTTAGGCCCTGGGTGTCGCAGCTAACGCGTTAAGCACACCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCAACGCGCAGAACTTTACCAGCCCTTGACATCCCGGTCGCGCGGATCAGAGATGAACCGCTTCAGTTCGGCTGGACCGGTGACAGGTGCTGCATGGCCGTCGTCAGCTCGTGCCN
+
#8ACCGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG9FGIIGGIIIIGIIIIIIIIIIIIIGGIDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIGIIIIIIIIIIIGIIIIIIIIIIIIGIIIIIIIIIIIIGIIIIDIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIGFIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIGIIIIIIIIIIIIIIF@GGGGGGGGGGGGGGGGGGGGGGGGGGGGFGGGGGGGGGGGGCCA8#

```

The assembly file discards the original ID for fastq file


### Other parameters
```
--p-value
--min-overlap
--max-assembly-length
--min-assembly-length
--min-trim-length
--quality-threshold
--max-uncalled-base
--test-method
--empirical-freqs
--score-method
--phred-base
--memory
--cap
--threads
--nbase
```



## flash

### Install flash
```
$ conda install -c bioconda flash
```

### Run flash
```
$ flash  --output-prefix merge  Dendrophyllia1.R1.fq Dendrophyllia1.R2.fq
[FLASH] Starting FLASH v1.2.11
[FLASH] Fast Length Adjustment of SHort reads
[FLASH]  
[FLASH] Input files:
[FLASH]     Dendrophyllia1.R1.fq
[FLASH]     Dendrophyllia1.R2.fq
[FLASH]  
[FLASH] Output files:
[FLASH]     ./merge.extendedFrags.fastq
[FLASH]     ./merge.notCombined_1.fastq
[FLASH]     ./merge.notCombined_2.fastq
[FLASH]     ./merge.hist
[FLASH]     ./merge.histogram
[FLASH]  
[FLASH] Parameters:
[FLASH]     Min overlap:           10
[FLASH]     Max overlap:           65
[FLASH]     Max mismatch density:  0.250000
[FLASH]     Allow "outie" pairs:   false
[FLASH]     Cap mismatch quals:    false
[FLASH]     Combiner threads:      40
[FLASH]     Input format:          FASTQ, phred_offset=33
[FLASH]     Output format:         FASTQ, phred_offset=33
[FLASH]  
[FLASH] Starting reader and writer threads
[FLASH] Starting 40 combiner threads
[FLASH] Processed 25000 read pairs
[FLASH] Processed 37529 read pairs
[FLASH]  
[FLASH] Read combination statistics:
[FLASH]     Total pairs:      37529
[FLASH]     Combined pairs:   34652
[FLASH]     Uncombined pairs: 2877
[FLASH]     Percent combined: 92.33%
[FLASH]  
[FLASH] Writing histogram files.
[FLASH]  
[FLASH] FLASH v1.2.11 complete!
[FLASH] 0.275 seconds elapsed
[FLASH] Finished with 1 warning (see above)

```

output fastq file **merge.extendedFrags.fastq**
```
@921
AGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGGGCACTAGATGTTGGTTTCATCGTAAGATGGGATCAGTGTCGCAGCTAACGCATTAAGTGCCCCGCCTGGGGAGTACGCTCGCAAGGGTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGATGCAACGCGCAGAACCTTACCGGGGCTTAAACTGTCAGGTAAACCCTGTGAAAGCAGGGCTGTTCCTTCGGGGACAATCTGATAGAGGTGCTGCATGGCTGTCGTCAGCTCGTGCCG
+
CCCCCGGGGCGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGFFGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGFFGGGGGGFGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGCCCCC
```
It also discards the original ID

file with histogram of length **merge.hist**
```
286     139
287     955
288     639
289     403
290     466
291     1464
292     765
293     2564
294     9754
295     4232
296     3980
297     3704
298     1553
299     764
300     369
301     232
302     724
303     1407
304     178

```

Other parameters:
```
--min-overlap=NUM
--max-overlap=NUM
--max-mismatch-density=NUM
--allow-outies
--phred-offset=OFFSET
--read-len=LEN
--fragment-len=LEN
--fragment-len-stddev=LEN
--cap-mismatch-quals
--interleaved-input
--interleaved-output
--interleaved
--tab-delimited-input
--tab-delimited-output
--output-prefix=PREFIX
--output-directory=DIR
--to-stdout
--compress
--compress-prog=PROG
--compress-prog-args=ARGS
--output-suffix=SUFFIX
--threads=NTHREADS
--quiet
```


## join_paired_ends.py

**join_paired_ends.py** is in the package **qiime** 

### install [qiime](https://github.com/biocore/qiime)

qiime version 1.9
```
$ conda install -c bioconda qiime 
```

qiime version 2
```
$ conda install -c qiime2/label/r2018.8 qiime2
```

### Run join_paired_ends.py
```
$ join_paired_ends.py -f Dendrophyllia1.R1.fq -r Dendrophyllia1.R2.fq -o Dendrophyllia1_qiime_merged
```

output three files in the dir of **Dendrophyllia1_qiime_merged**:
```
$ tree Dendrophyllia1_qiime_merged
.
├── fastqjoin.join.fastq
├── fastqjoin.un1.fastq
└── fastqjoin.un2.fastq
```

fastqjoin.join.fastq file:
```
@1
NGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGTGTGCTAGACGTTGGGGGTCTTAGGCCCTGGGTGTCGCAGCTAACGCGTTAAGCACACCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCAACGCGCAGAACTTTACCAGCCCTTGACATCCCGGTCGCGCGGATCAGAGATGAACCGCTTCAGTTCGGCTGGACCGGTGACAGGTGCTGCATGGCCGTCGTCAGCTCGTGCCN
+1
#8ACCGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG9FGGFGGGGGGGGGGGGGGGGGGGGGGGDGGGGGFGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG+GEGGGGGGGGGGGGGFBD9GGGGGGGGGGGGGFGGGGGGGGGGGGGGGGGGGGGGGFDEFFGGGGGGGGDGGGGGGGGGGGGGGGEFCFGGDGEGGGGGGGGGGF@GGGGGGGGGGGGGGGGGGGGGGGGGGGGFGGGGGGGGGGGGCCA8#

```

### Other parameters
```
--pe_join_method=PE_JOIN_METHOD
--index_reads_fp=INDEX_READS_FP
--min_overlap=MIN_OVERLAP
--perc_max_diff=PERC_MAX_DIFF
--max_ascii_score=MAX_ASCII_SCORE
--min_frac_match=MIN_FRAC_MATCH
--max_good_mismatch=MAX_GOOD_MISMATCH
--phred_64=PHRED_64
```