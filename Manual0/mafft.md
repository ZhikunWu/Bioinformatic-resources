## mafft mamual

### install mafft
```
$ conda install -c bioconda mafft 
```



### mafft parameters
```
------------------------------------------------------------------------------
  MAFFT v7.313 (2017/Nov/15)
  http://mafft.cbrc.jp/alignment/software/
  MBE 30:772-780 (2013), NAR 30:3059-3066 (2002)
------------------------------------------------------------------------------
High speed:
  % mafft in > out
  % mafft --retree 1 in > out (fast)

High accuracy (for <~200 sequences x <~2,000 aa/nt):
  % mafft --maxiterate 1000 --localpair  in > out (% linsi in > out is also ok)
  % mafft --maxiterate 1000 --genafpair  in > out (% einsi in > out)
  % mafft --maxiterate 1000 --globalpair in > out (% ginsi in > out)

If unsure which option to use:
  % mafft --auto in > out

--op # :         Gap opening penalty, default: 1.53
--ep # :         Offset (works like gap extension penalty), default: 0.0
--maxiterate # : Maximum number of iterative refinement, default: 0
--clustalout :   Output: clustal format, default: fasta
--reorder :      Outorder: aligned, default: input order
--quiet :        Do not report progress
--thread # :     Number of threads (if unsure, --thread -1)

```

### run mafft

```
mafft --auto --thread 20 --reorder --clustalout --op 1.50 B123.fa > B123.MSA




Leaf  108496 / 108520                                                                                                                               d
Leaf  108497 / 108520                                                                                                                               d
Done.gnment 107912-608                                                                                                                              d
  Alignment 583-25                                                                                                                                  d
  Alignment 24-1                                                                                                                                    d
  Alignment 23-1                                                                                                                                    d
----------------------------------------------------------------------------                                                                        d
  Alignment 21-1                                                                                                                                    d
nseq = 1085200-1                                                                                                                                    d
groupsize = 108521, partsize=50                                                                                                                     d
The order of sequences has been changed according to estimated similarity.                                                                          d
  Alignment 5-5                                                                                                                                     d
----------------------------------------------------------------------------                                                                        d
splittbfast (nuc) Version 7.313 alg=A, model=DNA200 (2), 1.50 (4.50), -0.00 (-0.00), noshift, amax=0.0                                              d
1 thread(s) 4-1                                                                                                                                     d
  Alignment 6-1                                                                                                                                     d
  Alignment 2-2                                                                                                                                     d
Strategy:nt 5-1                                                                                                                                     d
 FFT-NS-DPPartTree-1 (Not tested.)                                                                                                                  d
 ?Alignment 1-1                                                                                                                                     d
  Alignment 4-1                                                                                                                                     d
If unsure which option to use, try 'mafft --auto input > output'.                                                                                   d
For more information, see 'mafft --help', 'mafft --man' and the mafft page.                                                                         d
  Alignment 1-1                                                                                                                                     d
The default gap scoring scheme has been changed in version 7.110 (2013 Oct).                                                                        d
It tends to insert more gaps into gap-rich regions than previous versions.                                                                          d
To disable this change, add the --leavegappyregion option.

```
