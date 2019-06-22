
## PILER

PILER is public domain software for analyzing repetitive DNA found in genome sequences

### install PILER

```
$ conda install -c bioconda piler
```


### parameters
```
$ piler

PILER v1.0
http://www.drive5.com/piler
Written by Robert C. Edgar
This software is donated to the public domain.
Please visit web site for requested citation.

Usage:
  piler -trs <hitfile> -out <trsfile> [options]
  piler -trs2fasta <trsfile> -seq <fastafile> [-path <path>] [-maxfam <maxfam>]
  piler -cons <alnfile> -out <fastafile> -label <label>
  piler -annot <gff> -rep <repfile> -out <annotfile>
  piler -help
  piler -version

Use -quiet to suppress progress messages

-trs options:
  -mincover <n>
  -maxlengthdiffpct <n>
  -piles <pilefile>
  -images <imagefile>
  -multihit

```
