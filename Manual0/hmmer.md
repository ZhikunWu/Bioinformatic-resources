
## hmmer

### install hmmer
```
conda install -c bioconda hmmer
```

### prepare an HMM database for faster hmmscan searches

```
$ hmmpress -h
# hmmpress :: prepare an HMM database for faster hmmscan searches
# HMMER 3.2 (June 2018); http://hmmer.org/
# Copyright (C) 2018 Howard Hughes Medical Institute.
# Freely distributed under the BSD open source license.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Usage: hmmpress [-options] <hmmfile>

Options:
  -h : show brief help on version and usage
  -f : force: overwrite any previous pressed files

```

```
$ cat bactNOG_hmm/*.hmm > bactDB.hmmer
$ hmmpress bactDB.hmmer

Working...    done.
Pressed and indexed 144498 HMMs (144498 names).
Models pressed into binary file:   bactDB.hmmer.h3m
SSI index for binary model file:   bactDB.hmmer.h3i
Profiles (MSV part) pressed into:  bactDB.hmmer.h3f
Profiles (remainder) pressed into: bactDB.hmmer.h3p
```

### hmmscan parameters

```
$ hmmscan -h
# hmmscan :: search sequence(s) against a profile database
# HMMER 3.2 (June 2018); http://hmmer.org/
# Copyright (C) 2018 Howard Hughes Medical Institute.
# Freely distributed under the BSD open source license.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Usage: hmmscan [-options] <hmmdb> <seqfile>

Basic options:
  -h : show brief help on version and usage

Options controlling output:
  -o <f>           : direct output to file <f>, not stdout
  --tblout <f>     : save parseable table of per-sequence hits to file <f>
  --domtblout <f>  : save parseable table of per-domain hits to file <f>
  --pfamtblout <f> : save table of hits and domains to file, in Pfam format <f>
  --acc            : prefer accessions over names in output
  --noali          : don't output alignments, so output is smaller
  --notextw        : unlimit ASCII text output line width
  --textw <n>      : set max width of ASCII text output lines  [120]  (n>=120)

Options controlling reporting thresholds:
  -E <x>     : report models <= this E-value threshold in output  [10.0]  (x>0)
  -T <x>     : report models >= this score threshold in output
  --domE <x> : report domains <= this E-value threshold in output  [10.0]  (x>0)
  --domT <x> : report domains >= this score cutoff in output

Options controlling inclusion (significance) thresholds:
  --incE <x>    : consider models <= this E-value threshold as significant
  --incT <x>    : consider models >= this score threshold as significant
  --incdomE <x> : consider domains <= this E-value threshold as significant
  --incdomT <x> : consider domains >= this score threshold as significant

Options for model-specific thresholding:
  --cut_ga : use profile's GA gathering cutoffs to set all thresholding
  --cut_nc : use profile's NC noise cutoffs to set all thresholding
  --cut_tc : use profile's TC trusted cutoffs to set all thresholding

Options controlling acceleration heuristics:
  --max    : Turn all heuristic filters off (less speed, more power)
  --F1 <x> : MSV threshold: promote hits w/ P <= F1  [0.02]
  --F2 <x> : Vit threshold: promote hits w/ P <= F2  [1e-3]
  --F3 <x> : Fwd threshold: promote hits w/ P <= F3  [1e-5]
  --nobias : turn off composition bias filter

Other expert options:
  --nonull2     : turn off biased composition score corrections
  -Z <x>        : set # of comparisons done, for E-value calculation
  --domZ <x>    : set # of significant seqs, for domain E-value calculation
  --seed <n>    : set RNG seed to <n> (if 0: one-time arbitrary seed)  [42]
  --qformat <s> : assert input <seqfile> is in format <s>: no autodetection
  --cpu <n>     : number of parallel CPU workers to use for multithreads  [2]

```



### search sequence(s) against a profile database

```
$ hmmscan -o /home/wzk/Project/metagenome/ORFCluster/representive-1_hmmer.txt --cpu 20  bactDB.hmmer /home/wzk/Project/metagenome/ORFCluster/representive-1.faa


# hmmscan :: search sequence(s) against a profile database
# HMMER 3.2 (June 2018); http://hmmer.org/
# Copyright (C) 2018 Howard Hughes Medical Institute.
# Freely distributed under the BSD open source license.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# query sequence file:             /home/wzk/Project/metagenome/ORFCluster/representive-1.faa
# target HMM database:             bactDB.hmmer
# output directed to file:         /home/wzk/Project/metagenome/ORFCluster/representive-1_hmmer.txt
# number of worker threads:        20
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Query:       HAMCNDLH_00001  [L=97]
Description: hypothetical protein
Scores for complete sequence (score includes all domains):
   --- full sequence ---   --- best 1 domain ---    -#dom-
    E-value  score  bias    E-value  score  bias    exp  N  Model    Description
    ------- ------ -----    ------- ------ -----   ---- --  -------- -----------

   [No hits detected that satisfy reporting thresholds]


Domain annotation for each model (and alignments):

   [No targets detected that satisfy reporting thresholds]


Internal pipeline statistics summary:
-------------------------------------
Query sequence(s):                         1  (97 residues searched)
Target model(s):                      144498  (45998434 nodes)
Passed MSV filter:                      2657  (0.0183878); expected 2890.0 (0.02)
Passed bias filter:                     2203  (0.0152459); expected 2890.0 (0.02)
Passed Vit filter:                       126  (0.000871984); expected 144.5 (0.001)
Passed Fwd filter:                         0  (0); expected 1.4 (1e-05)
Initial search space (Z):             144498  [actual number of targets]
Domain search space  (domZ):               0  [number of targets reported over threshold]
# CPU time: 4.26u 3.65s 00:00:07.91 Elapsed: 00:00:42.17
# Mc/sec: 105.80
//
Query:       HAMCNDLH_00002  [L=77]
Description: hypothetical protein
Scores for complete sequence (score includes all domains):
   --- full sequence ---   --- best 1 domain ---    -#dom-
    E-value  score  bias    E-value  score  bias    exp  N  Model                        Description
    ------- ------ -----    ------- ------ -----   ---- --  --------                     -----------
    1.1e-20   77.6   0.0    1.2e-20   77.5   0.0    1.0  1  bactNOG.ENOG41090JH.meta_raw  
      3e-12   49.3   0.0    3.2e-12   49.2   0.0    1.0  1  bactNOG.ENOG410628R.meta_raw  
    3.2e-09   39.4   0.0    3.2e-09   39.4   0.0    1.1  1  bactNOG.ENOG4108KJV.meta_raw  
    1.8e-07   33.7   0.0    1.9e-07   33.6   0.0    1.0  1  bactNOG.ENOG4108NBH.meta_raw  
  ------ inclusion threshold ------
      0.094   15.7   0.0       0.15   15.0   0.0    1.2  1  bactNOG.ENOG4105Y9J.meta_raw  
      0.098   14.0   0.0        0.1   14.0   0.0    1.0  1  bactNOG.ENOG4108PCT.meta_raw  
       0.13   15.1   0.0       0.16   14.9   0.0    1.1  1  bactNOG.ENOG4105ZA7.meta_raw  
       0.79   12.6   0.0          1   12.3   0.0    1.1  1  bactNOG.ENOG4106RGU.meta_raw  
       0.85   11.3   0.0       0.85   11.3   0.0    1.1  1  bactNOG.ENOG4108RMP.meta_raw  
       0.85   11.9   0.0       0.91   11.8   0.0    1.1  1  bactNOG.ENOG4108KC4.meta_raw  
          1   11.3   0.0          1   11.3   0.0    1.0  1  bactNOG.ENOG4105X44.meta_raw  


Domain annotation for each model (and alignments):
>> bactNOG.ENOG41090JH.meta_raw  
   #    score  bias  c-Evalue  i-Evalue hmmfrom  hmm to    alifrom  ali to    envfrom  env to     acc
 ---   ------ ----- --------- --------- ------- -------    ------- -------    ------- -------    ----
   1 !   77.5   0.0   9.1e-25   1.2e-20     284     360 .]       2      77 .]       1      77 [] 0.96

  Alignments for each domain:
  == domain 1  score: 77.5 bits;  conditional E-value: 9.1e-25
  bactNOG.ENOG41090JH.meta_raw 284 medlwklifelakklnvQvFaTTHSkeciealqkaleeeeeddiklfrlekkkgkikaveyseeeleialergiEvR 360
                                   ++ +w +if+la+kl+vQvFaTTHS++c+ a+q+a+ e+ + + +l+rl +k++ + ++++se++l+ +++++iEvR
                HAMCNDLH_00002   2 QPLVWGTIFQLAQKLDVQVFATTHSRDCVLAFQQAAAES-PVEGRLIRLTRKDDWVLPTVFSEDKLQFIADNDIEVR 77 
                                   789***********************************9.6666********************************9 PP

```