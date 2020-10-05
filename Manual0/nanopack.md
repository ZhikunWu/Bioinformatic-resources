## [nanopack](https://pypi.python.org/pypi/nanopack)

### [NanoPlot](https://github.com/wdecoster/NanoPlot)
### [NanoComp](https://github.com/wdecoster/nanocomp)
### [nanostat](https://github.com/wdecoster/nanostat)

### install nanostat
```
$ conda install -c bioconda nanostat

The following NEW packages will be INSTALLED:

    bcftools:  1.6-1                   bioconda
    nanoget:   1.2.2-py36_0            bioconda
    nanomath:  0.20.0-py36_0           bioconda
    nanostat:  1.1.0-py36_0            bioconda
    pysam:     0.14.0-py36_htslib1.7_2 bioconda
    samtools:  1.7-2                   bioconda



```

### run NanoStat
```
$ NanoStat --fasta Correction/ERR2173373_racon3.fasta  > test_out
```

out file:
```
$ cat test_out
General summary:     
Mean read length:   947900.3
Median read length: 787.0
Number of reads:    124
Read length N50:    11188488
Total bases:    117539636

```

