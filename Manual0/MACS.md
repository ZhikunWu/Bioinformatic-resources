## MACS2


### Install MACS2

```
conda install -c bioconda macs2 
```

### MACS functions
```
macs2 --help

usage: macs2 [-h] [--version]
             {callpeak,bdgpeakcall,bdgbroadcall,bdgcmp,bdgopt,cmbreps,bdgdiff,filterdup,predictd,pileup,randsample,refinepeak}
             ...

macs2 -- Model-based Analysis for ChIP-Sequencing

positional arguments:
  {callpeak,bdgpeakcall,bdgbroadcall,bdgcmp,bdgopt,cmbreps,bdgdiff,filterdup,predictd,pileup,randsample,refinepeak}
    callpeak            Main MACS2 Function: Call peaks from alignment
                        results.
    bdgpeakcall         Call peaks from bedGraph output. Note: All regions on
                        the same chromosome in the bedGraph file should be
                        continuous so only bedGraph files from MACS2 are
                        accpetable.
    bdgbroadcall        Call broad peaks from bedGraph output. Note: All
                        regions on the same chromosome in the bedGraph file
                        should be continuous so only bedGraph files from MACS2
                        are accpetable.
    bdgcmp              Deduct noise by comparing two signal tracks in
                        bedGraph. Note: All regions on the same chromosome in
                        the bedGraph file should be continuous so only
                        bedGraph files from MACS2 are accpetable.
    bdgopt              Operations on score column of bedGraph file. Note: All
                        regions on the same chromosome in the bedGraph file
                        should be continuous so only bedGraph files from MACS2
                        are accpetable.
    cmbreps             Combine BEDGraphs of scores from replicates. Note: All
                        regions on the same chromosome in the bedGraph file
                        should be continuous so only bedGraph files from MACS2
                        are accpetable.
    bdgdiff             Differential peak detection based on paired four
                        bedgraph files. Note: All regions on the same
                        chromosome in the bedGraph file should be continuous
                        so only bedGraph files from MACS2 are accpetable.
    filterdup           Remove duplicate reads at the same position, then save
                        the rest alignments to BED or BEDPE file. If you use
                        '--keep-dup all option', this script can be utilized
                        to convert any acceptable format into BED or BEDPE
                        format.
    predictd            Predict d or fragment size from alignment results.
                        *Will NOT filter duplicates*
    pileup              Pileup aligned reads with a given extension size
                        (fragment size or d in MACS language). Note there will
                        be no step for duplicate reads filtering or sequencing
                        depth scaling, so you may need to do certain pre/post-
                        processing.
    randsample          Randomly sample number/percentage of total reads.
    refinepeak          (Experimental) Take raw reads alignment, refine peak
                        summits and give scores measuring balance of
                        waston/crick tags. Inspired by SPP.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

For command line options of each command, type: macs2 COMMAND -h

```

### MACS call peaks
```
macs2 callpeak --verbose 3 --treatment /home/wzk/Project/Other/sc/mapping/SRR5635513/SRR5635513_sorted.bam -g mm -B -q 0.05  --nomodel --shift -100 --extsize 200 --nolambda --keep-dup all -f BAM --outdir /home/wzk/Project/Other/sc/peaks/SRR5635513 --call-summits
```

output files:
```
-rw-r--r-- 1  952 Nov 18 07:47 NA_control_lambda.bdg
-rw-r--r-- 1 1.8K Nov 18 07:47 NA_peaks.narrowPeak
-rw-r--r-- 1 3.2K Nov 18 07:47 NA_peaks.xls
-rw-r--r-- 1 1.1K Nov 18 07:47 NA_summits.bed
-rw-r--r-- 1 986K Nov 18 07:47 NA_treat_pileup.bdg

```

```
$ head NA_summits.bed
1   172633116   172633117   NA_peak_1   6.49632
10  28013621    28013622    NA_peak_2   3.34450
11  109011850   109011851   NA_peak_3   13.09489
17  39843685    39843686    NA_peak_4   9.73292
17  39844509    39844510    NA_peak_5   16.56518
17  39845454    39845455    NA_peak_6   13.09489
17  39846330    39846331    NA_peak_7   16.56518
17  39847244    39847245    NA_peak_8   6.49632
17  39847553    39847554    NA_peak_9   9.73292
17  39848199    39848200    NA_peak_10  13.09489


$ less NA_peaks.xls
chr     start   end     length  abs_summit      pileup  -log10(pvalue)  fold_enrichment -log10(qval
ue)  name
1       172632995       172633194       200     172633117       3.00    12.29255        3.99253 6.4
9632 NA_peak_1
10      28013523        28013722        200     28013622        2.00    8.96253 2.99440 3.34450 NA_
peak_2
11      109011627       109011999       373     109011851       5.00    19.22556        5.98879 13.
09489        NA_peak_3

```


### MACS using bed file
```
samtools view -h  <BAM>  |  SAMtoBED  -i -  -o <BED>  -x  -v

macs2 callpeak  -t <BED>  -f BEDPE  -n NAME  -g ce  --keep-dup all
```


### Call peaks for group
```
$ macs2 callpeak --verbose 3 --treatment  /home/wzk/Project/Other/sc/mapping/SRR5635513/SRR5635513_final.bam --control /home/wzk/Project/Other/sc/mapping/SRR5635516/SRR5635516_final.bam -g mm -B -q 0.05  --nomodel --shift -100 --extsize 200 -nolambda --keep-dup all -f BAM --outdir peaks/compare --call-summits

```

```
├── compare
│   ├── olambda_control_lambda.bdg
│   ├── olambda_peaks.narrowPeak
│   ├── olambda_peaks.xls
│   ├── olambda_summits.bed
│   └── olambda_treat_pileup.bdg
```

