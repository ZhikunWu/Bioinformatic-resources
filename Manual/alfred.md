## [alfred](https://github.com/tobiasrausch/alfred)

BAM Statistics, Feature Counting and Annotation

### install alfred

```
git clone --recursive https://github.com/tobiasrausch/alfred.git
cd alfred/
make all
make install
./bin/alfred -h
```

### parameters

```
$ alfred
           _  __              _ 
     /\   | |/ _|            | |
    /  \  | | |_ _ __ ___  __| |
   / /\ \ | |  _| '__/ _ \/ _` |
  / ____ \| | | | | |  __/ (_| |
 /_/    \_\_|_| |_|  \___|\__,_|

**********************************************************************
Program: Alfred
This is free software, and you are welcome to redistribute it under
certain conditions (GPL); for license details use '-l'.
This program comes with ABSOLUTELY NO WARRANTY; for details use '-w'.

Alfred (Version: 0.1.17)
Contact: Gear Genomics Team (gear_genomics@embl.de)
Web Application: https://gear.embl.de/alfred/
Documentation: https://gear.embl.de/docs/alfred/
**********************************************************************

Usage: alfred <command> <arguments>

Commands:

    qc           alignment quality control
    count_dna    counting DNA reads in windows
    count_rna    counting RNA reads in features
    count_jct    counting RNA split-reads at exon junctions
    tracks       create browser tracks
    annotate     annotate peaks
    spaced_motif find spaced motifs
    split        split BAM into haplotypes
    consensus    consensus computation for error-prone reads
    pwalign      pairwise alignment using dynamic programming
    ase          allele-specific expression
    replication  replication timing (Repli-Seq)

```

### [alfred manual](https://gear.embl.de/docs/alfred/)