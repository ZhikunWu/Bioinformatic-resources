## repeatscout

### [Repeat finding](https://openwetware.org/wiki/Wikiomics:Repeat_finding)

### repeatscout manual
```
$ conda install -c bioconda repeatscout
```

### creat the table of frequency of lmers
```
$ build_lmer_table -l 14 -sequence pomegranate.fa.fasta -freq pomegranate_seq_freq.txt
```

output file:
```
$ head pomegranate_seq_freq.txt
AAAAAAAAGCGGGA  19  279540494
AAAAAAAATACCCG  12  252234347
ATTCAAGCGAAGCC  3   242537071
AATTCAAGTAGACT  3   79349189
GGCTTCGGCTTGAA  4   173350572
CATACATATGTATG  26  318031163
AATTCAATTGAATT  83  311651996
ACTGGACCTTGAAT  3   139655078
AATTCAATCATGCA  5   308090115
AAAAAAACTGTATG  12  270707718
```


### find repeats based on the frequency of lmers and genome

```
$ RepeatScout
RepeatScout Version 1.0.5

Usage: 
RepeatScout -sequence <seq> -output <out> -freq <freq> -l <l> [opts]
     -L # size of region to extend left or right (10000) 
     -match # reward for a match (+1)  
     -mismatch # penalty for a mismatch (-1) 
     -gap  # penalty for a gap (-5)
     -maxgap # maximum number of gaps allowed (5) 
     -maxoccurrences # cap on the number of sequences to align (10,000) 
     -maxrepeats # stop work after reporting this number of repeats (10000)
     -cappenalty # cap on penalty for exiting alignment of a sequence (-20)
     -tandemdist # of bases that must intervene between two l-mers for both to be counted (500)
     -minthresh # stop if fewer than this number of l-mers are found in the seeding phase (3)
     -minimprovement # amount that a the alignment needs to improve each step to be considered progress (3)
     -stopafter # stop the alignment after this number of no-progress columns (100)
     -goodlength # minimum required length for a sequence to be reported (50)
     -maxentropy # entropy (complexity) threshold for an l-mer to be considered (-.7)
     -v[v[v[v]]] How verbose do you want it to be?  -vvvv is super-verbose.

```

```
$ RepeatScout -sequence pomegranate.fa.fasta  -freq pomegranate_seq_freq.txt  -l 14  -output  pomegranate_repeat.txt
```

### filt result

```
$ cd /home/wzk/anaconda3/envs/evolution/share && \
git clone https://github.com/mmcco/RepeatScout.git 
```


```
$ /home/wzk/anaconda3/envs/evolution/share/RepeatScout/filter-stage-1.prl seq_repeat.txt > seq_repeat_filt.txt
```

this prints tons of messages

### run RepeatMasker on your genome of interest using filtered RepeatScout library

```
$ RepeatMasker  input_genome_sequence.fas -lib seq_repeat_filt.txt
```

This is a very long step.

### filtering putative repeats by copy number

By default only sequences occurring > 10 times in the genome are kept

```
$ cat seq_repeat_filt.txt | filter-stage-2.prl --cat=input_genome_sequence.fas.out > output_repeats.fas.filtered_2
```

