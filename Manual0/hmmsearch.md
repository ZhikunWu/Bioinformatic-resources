## hmmsearch


### [hmmscan vs. hmmsearch speed: the numerology](https://cryptogenomicon.org/2011/05/27/hmmscan-vs-hmmsearch-speed-the-numerology/)

#### hmmscan
```
$ hmmscan --cpu 10 --tblout test.tblout --domtblout test.domtblout --pfamtblout test.pfamtblout  -o test_hmm_out.txt /home/wzk/database/dbCAN/dbcan/dbCAN-fam-HMMs.txt.v6  representive_test.faa

```

#### hmmsearch
```
$ hmmsearch  --cpu 10 --tblout test.tblout --domtblout test.domtblout --pfamtblout test.pfamtblout  -o test_hmm_out.txt /home/wzk/database/dbCAN/dbcan/dbCAN-fam-HMMs.txt.v6  representive_test.faa
```

#### hmmsearch running with mutiple threads

```
$ head test.domtblout
#                                                                            --- full sequence --- -------------- this domain -------------   hmm coord   ali coord   env coord
# target name        accession   tlen query name           accession   qlen   E-value  score  bias   #  of  c-Evalue  i-Evalue  score  bias  from    to  from    to  from    to  acc description of target
#------------------- ---------- ----- -------------------- ---------- ----- --------- ------ ----- --- --- --------- --------- ------ ----- ----- ----- ----- ----- ----- ----- ---- ---------------------
OKCLIJEO_34990       -             45 CBM10.hmm            -             28      0.15   14.6   0.1   1   1   4.4e-06      0.22   14.1   0.1     4    24    17    39    15    40 0.90 hypothetical protein
OKCLIJEO_99017       -             70 CBM10.hmm            -             28      0.93   12.1   0.7   1   1   2.6e-05       1.3   11.6   0.7     1    16    19    34    19    36 0.91 hypothetical protein
OKCLIJEO_59858       -             72 CBM11.hmm            -            163      0.33   13.3   0.0   1   1   3.6e-06      0.36   13.2   0.0    28    70    15    57     6    67 0.90 hypothetical protein
OKCLIJEO_40133       -            114 CBM12.hmm            -             34      0.34   12.9   0.7   1   2   1.1e-05       1.1   11.2   0.3    10    19    49    58    49    59 0.90 Quinone oxidoreductase 1
OKCLIJEO_40133       -            114 CBM12.hmm            -             34      0.34   12.9   0.7   2   2      0.18   1.8e+04   -2.1   0.0    13    17    80    84    79    85 0.80 Quinone oxidoreductase 1
OKCLIJEO_43405       -             58 CBM15.hmm            -            146     0.038   16.2   0.2   1   1   1.4e-06     0.045   15.9   0.2    27    57    14    44     9    48 0.91 hypothetical protein
OKCLIJEO_46760       -            123 CBM15.hmm            -            146      0.72   12.0   0.1   1   2       0.4   1.3e+04   -1.8   0.0    31    39    21    29    16    38 0.81 Elongation factor Tu
```

```
$ head test.pfamtblout
# Sequence scores
# ---------------
#
# name                  bits   E-value   n   exp  bias    description
# ------------------- ------ --------- --- ----- -----    ---------------------
OKCLIJEO_34990          14.6      0.15   1   1.2   0.1    hypothetical protein
OKCLIJEO_99017          12.1      0.93   1   1.3   0.7    hypothetical protein

# Domain scores
# -------------

```

```
$ head test.tblout
#                                                               --- full sequence ---- --- best 1 domain ---- --- domain number estimation ----
# target name        accession  query name           accession    E-value  score  bias   E-value  score  bias   exp reg clu  ov env dom rep inc description of target
#------------------- ---------- -------------------- ---------- --------- ------ ----- --------- ------ -----   --- --- --- --- --- --- --- --- ---------------------
OKCLIJEO_34990       -          CBM10.hmm            -               0.15   14.6   0.1      0.22   14.1   0.1   1.2   1   0   0   1   1   1   0 hypothetical protein
OKCLIJEO_99017       -          CBM10.hmm            -               0.93   12.1   0.7       1.3   11.6   0.7   1.3   1   0   0   1   1   1   0 hypothetical protein
OKCLIJEO_59858       -          CBM11.hmm            -               0.33   13.3   0.0      0.36   13.2   0.0   1.0   1   0   0   1   1   1   0 hypothetical protein
OKCLIJEO_40133       -          CBM12.hmm            -               0.34   12.9   0.7       1.1   11.2   0.3   2.0   2   0   0   2   2   2   0 Quinone oxidoreductase 1
OKCLIJEO_43405       -          CBM15.hmm            -              0.038   16.2   0.2     0.045   15.9   0.2   1.1   1   0   0   1   1   1   0 hypothetical protein
OKCLIJEO_46760       -          CBM15.hmm            -               0.72   12.0   0.1       1.7   10.8   0.0   1.6   2   0   0   2   2   2   0 Elongation factor Tu
OKCLIJEO_47769       -          CBM15.hmm            -               0.79   11.9   0.0        46    6.2   0.0   2.1   2   0   0   2   2   2   0 Elongation factor Tu
```

```
$ head -n 20 test_hmm_out.txt

# hmmsearch :: search profile(s) against a sequence database
# HMMER 3.1b2 (February 2015); http://hmmer.org/
# Copyright (C) 2015 Howard Hughes Medical Institute.
# Freely distributed under the GNU General Public License (GPLv3).
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# query HMM file:                  /home/wzk/database/dbCAN/dbcan/dbCAN-fam-HMMs.txt.v6
# target sequence database:        representive_test.faa
# output directed to file:         test_hmm_out.txt
# per-seq hits tabular output:     test.tblout
# per-dom hits tabular output:     test.domtblout
# pfam-style tabular hit output:   test.pfamtblout
# number of worker threads:        10
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Query:       CBM10.hmm  [M=28]
Scores for complete sequences (score includes all domains):
   --- full sequence ---   --- best 1 domain ---    -#dom-
    E-value  score  bias    E-value  score  bias    exp  N  Sequence       Description
    ------- ------ -----    ------- ------ -----   ---- --  --------       -----------
  ------ inclusion threshold ------
```
