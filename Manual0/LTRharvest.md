
## [LTRharvest and LTRdigest](https://avrilomics.blogspot.com/2015/09/ltrharvest.html)

### [GenomeTools](http://genometools.org): The versatile open source genome analysis software

The GenomeTools genome analysis system is a free collection of bioinformatics tools (in the realm of genome informatics) combined into a single binary named **gt**. It is based on a C library named “libgenometools” which consists of several modules.


### install genometools

```
$ conda install -c bioconda genometools-genometools
```

tools
```
$ gt --help
Usage: gt [option ...] [tool | script] [argument ...]
The GenomeTools genome analysis system.

-i       enter interactive mode after executing 'tool' or 'script'
-q       suppress warnings
-test    perform unit tests and exit
-seed    set seed for random number generator manually.
         0 generates a seed from current time and process id
-help    display help and exit
-version display version information and exit

Tools:

bed_to_gff3
cds
chain2dim
chseqids
clean
compreads
condenseq
congruence
convertseq
csa
dot
dupfeat
encseq
encseq2spm
eval
extractfeat
extractseq
fastq_sample
featureindex
fingerprint
genomediff
gff3
gff3_to_gtf
gff3validator
gtf_to_gff3
hop
id_to_md5
inlineseq_add
inlineseq_split
interfeat
loccheck
ltrclustering
ltrdigest
ltrharvest
matchtool
matstat
md5_to_id
merge
mergefeat
mgth
mkfeatureindex
mkfmindex
mmapandread
orffinder
packedindex
prebwt
readjoiner
repfind
scriptfilter
seed_extend
select
seq
seqfilter
seqids
seqmutate
seqorder
seqstat
seqtransform
seqtranslate
sequniq
shredder
shulengthdist
simreads
sketch
sketch_page
snpper
speck
splicesiteinfo
splitfasta
stat
suffixerator
tagerator
tallymer
tirvish
uniq
uniquesub
wtree

Set the environment variable `GT_MEM_BOOKKEEPING=on` to enable memory
bookkeeping (e.g., like this: `env GT_MEM_BOOKKEEPING=on gt`).

Set the environment variable `GT_ENV_OPTIONS=-spacepeak` to show a spacepeak
after program run.
Set the environment variable `GT_ENV_OPTIONS=-showtime` to show processing times
for some program parts if implemented.

Set the environment variable `GT_SEED` to an integer value to supply a seed for
the random number generator. Can be overridden by the `-seed` option.

Combinations are possible. Running the `gt` binary with `GT_ENV_OPTIONS=-help`
shows all possible "environment options".

Report bugs to https://github.com/genometools/genometools/issues.

```



### generate suffix array

```
$ gt suffixerator --help
Usage: gt suffixerator [option ...] (-db file [...] | -ii index)
Compute enhanced suffix array.

-ssp          output sequence separator positions to file
              default: yes
-des          output sequence descriptions to file
              default: yes
-sds          output sequence description separator positions to file
              default: yes
-md5          output MD5 sums to file
              default: yes
-clipdesc     clip descriptions after first whitespace
              default: no
-sat          specify kind of sequence representation
              by one of the keywords direct, bytecompress, eqlen, bit, uchar,
              ushort, uint32
              default: undefined
-dna          input is DNA sequence
              default: no
-protein      input is protein sequence
              default: no
-indexname    specify name for index to be generated
              default: undefined
-db           specify database files
-smap         specify file containing a symbol mapping
              default: undefined
-lossless     allow lossless original sequence retrieval
              default: no
-mirrored     virtually append the reverse complement of each sequence
              default: no
-pl           specify prefix length for bucket sort
              recommendation: use without argument;
              then a reasonable prefix length is automatically determined.
              default: 0
-dc           specify difference cover value
              default: 0
-spmopt       optimize esa-construction for suffix-prefix matching
              default: 0
-memlimit     specify maximal amount of memory to be used during index
              construction (in bytes, the keywords 'MB' and 'GB' are allowed)
              default: undefined
-kys          output/sort according to keys of the form |key| in fasta header
              default: nosort
-dir          specify reading direction (fwd, cpl, rev, rcl)
              default: fwd
-suf          output suffix array (suftab) to file
              default: no
-lcp          output lcp table (lcptab) to file
              default: no
-bwt          output Burrows-Wheeler Transformation (bwttab) to file
              default: no
-bck          output bucket table to file
              default: no
-v            be verbose
              default: no
-showprogress show a progress bar
              default: no
-ii           specify existing encoded sequence
              default: undefined
-help         display help for basic options and exit
-help+        display help for all options and exit
-version      display version information and exit

Report bugs to <kurtz@zbh.uni-hamburg.de>.

```


```
$ gt suffixerator -db  assembly/ERR2259150/assembly.fasta  -indexname  assembly_index  -tis -suf -lcp -des -ssp -sds -dna

```

output files:

```
-rw-r--r-- 1   60 Dec  3 04:35 assembly_index.des
-rw-r--r-- 1 196K Dec  3 04:35 assembly_index.esq
-rw-r--r-- 1 782K Dec  3 04:35 assembly_index.lcp
-rw-r--r-- 1  19K Dec  3 04:35 assembly_index.llv
-rw-r--r-- 1   33 Dec  3 04:35 assembly_index.md5
-rw-r--r-- 1  451 Dec  3 04:35 assembly_index.prj
-rw-r--r-- 1    0 Dec  3 04:35 assembly_index.sds
-rw-r--r-- 1 6.2M Dec  3 04:35 assembly_index.suf
```


### run LTRharvest
```
$ gt ltrharvest -index assembly_index > assembly_ltrharvest
```

output file:

```
$ cat assembly_ltrharvest
# args=-index assembly_index
# predictions are reported in the following way
# s(ret) e(ret) l(ret) s(lLTR) e(lLTR) l(lLTR) s(rLTR) e(rLTR) l(rLTR) sim(LTRs) seq-nr 
# where:
# s = starting position
# e = ending position
# l = length
# ret = LTR-retrotransposon
# lLTR = left LTR
# rLTR = right LTR
# sim = similarity
# seq-nr = sequence number
96320  98005  1686  96320  96466  147  97861  98005  145  85.03  0
111000  116174  5175  111000  111343  344  115814  116174  361  89.20  0
162944  175993  13050  162944  163139  196  175798  175993  196  99.49  0
206566  210122  3557  206566  207082  517  209591  210122  532  91.17  0
225814  232429  6616  225814  226191  378  232044  232429  386  94.04  0
234911  237338  2428  234911  235098  188  237153  237338  186  86.17  0
284237  289630  5394  284237  284913  677  288954  289630  677  99.56  0
430443  434269  3827  430443  430776  334  433934  434269  336  94.94  0
453707  464603  10897  453707  453874  168  464443  464603  161  86.31  0
610309  617245  6937  610309  610647  339  616906  617245  340  94.12  0
675327  676564  1238  675327  675483  157  676409  676564  156  92.36  0
742771  748051  5281  742771  743342  572  747487  748051  565  98.60  0

```


#### The -out option makes an output fasta file of the predicted LTR retrotransposon sequences
```
$ gt ltrharvest -index assembly_index -out assembly_seq > assembly_ltrharvest
```

output sequence file
```
$ head assembly_seq
>Lachesis_group0 44_contigs__length_55558335 (dbseq-nr 0) [96320,98005]
acaccgttagacggagtttaacggtgtgctagatccaggaataaaatggtgattcgtgct
agatcgtgacaacttttaaaaatgtgctaggaagtgaaaataaggtaaaaattgtgctac
atggggctattttccctttaaaaaatatttaccactcttttcggtgttctgattttgata
attttagtgaaccgtataagcacaaaatgaggtgaaacttttaccccatgttcctgatgt
tattataaagctgcacacaaattttcagatttttctagatggtgaattttcagataaaaa
atatttacctctttttttggtgttgtgatttaggtagcttttgtgaatcattcgatctca
aaataaggtgaaactttttccccacgtttctaatattattataaaactccacacaaattt
tcaaatttttctgaacggtgaatcttcaaaataaaaaataattaccattcttttttatgc
tctgattttaatagtttttgtgaaccgtcaaatctaaaaacgagatgaaaattttcccca

```

#### A useful option is the -gff3 option, which makes an output file in gff3 format

```
$ gt ltrharvest -index assembly_index -out assembly_seq -gff3 assembly_ltrharvest.gff > assembly_ltrharvest.log

```

output file
```
$ head  assembly_ltrharvest.gff
##gff-version 3
##sequence-region   seq0 1 799920
seq0    LTRharvest  repeat_region   96316   98009   .   ?   .   ID=repeat_region1
seq0    LTRharvest  target_site_duplication 96316   96319   .   ?   .   Parent=repeat_region1
seq0    LTRharvest  LTR_retrotransposon 96320   98005   .   ?   .   ID=LTR_retrotransposon1;Parent=repeat_region1;ltr_similarity=85.03;seq_number=0
seq0    LTRharvest  long_terminal_repeat    96320   96466   .   ?   .   Parent=LTR_retrotransposon1
seq0    LTRharvest  long_terminal_repeat    97861   98005   .   ?   .   Parent=LTR_retrotransposon1
seq0    LTRharvest  target_site_duplication 98006   98009   .   ?   .   Parent=repeat_region1
###
seq0    LTRharvest  repeat_region   110996  116178  .   ?   .   ID=repeat_region2

```

#### Sascha suggested an even better way to run LTRharvest is to run
```
$ gt ltrharvest -index assembly_index -seqids yes -tabout no  -out assembly_seq > assembly_ltrharvest

```

output table file
```
$ head assembly_ltrharvest
##gff-version 3
##sequence-region   Lachesis_group0 1 799920
Lachesis_group0 LTRharvest  repeat_region   96316   98009   .   ?   .   ID=repeat_region1
Lachesis_group0 LTRharvest  target_site_duplication 96316   96319   .   ?   .Parent=repeat_region1
Lachesis_group0 LTRharvest  LTR_retrotransposon 96320   98005   .   ?   .ID=LTR_retrotransposon1;Parent=repeat_region1;ltr_similarity=85.03;seq_number=0
Lachesis_group0 LTRharvest  long_terminal_repeat    96320   96466   .   ?   .Parent=LTR_retrotransposon1
Lachesis_group0 LTRharvest  long_terminal_repeat    97861   98005   .   ?   .Parent=LTR_retrotransposon1
Lachesis_group0 LTRharvest  target_site_duplication 98006   98009   .   ?   .Parent=repeat_region1
###
Lachesis_group0 LTRharvest  repeat_region   110996  116178  .   ?   .   ID=repeat_region2

```


## LTRdigest
The LTRdigest software can be used to post-process LTRharvest, to weed out potential false positives. LTRharvest just gives you the positions of LTR retrotransposons, but LTRdigest annotates internal features of LTR retrotransposons.

```
$ gt ltrdigest assembly_ltrharvest.gff assembly_index  > assembly_ltrharvest_ltrdigest
```

**assembly_ltrharvest.gff** is the result of **LTRharvest**


out file:
```
$ less assembly_ltrharvest_ltrdigest

##gff-version 3
##sequence-region   seq0 1 799920
seq0    LTRharvest      repeat_region   96316   98009   .       +       .       ID=repeat_region1
seq0    LTRharvest      target_site_duplication 96316   96319   .       +       .       Parent=repeat_region1
seq0    LTRharvest      LTR_retrotransposon     96320   98005   .       +       .       ID=LTR_retrotransposon1;Parent=repeat_region1;ltr_similarity=85.03;seq_number=0
seq0    LTRharvest      long_terminal_repeat    96320   96466   .       +       .       Parent=LTR_retrotransposon1
seq0    LTRharvest      long_terminal_repeat    97861   98005   .       +       .       Parent=LTR_retrotransposon1
seq0    LTRdigest       RR_tract        97863   97870   .       +       .       Parent=LTR_retrotransposon1
seq0    LTRharvest      target_site_duplication 98006   98009   .       +       .       Parent=repeat_region1
###
seq0    LTRharvest      repeat_region   110996  116178  .       -       .       ID=repeat_region2
seq0    LTRharvest      target_site_duplication 110996  110999  .       -       .       Parent=repeat_region2
seq0    LTRharvest      LTR_retrotransposon     111000  116174  .       -       .       ID=LTR_retrotransposon2;Par

```


#### The input gff file must be sorted by position

```
$ gt gff3 -sort assembly_ltrharvest.gff > assembly_ltrharvest_sorted.gff
```

