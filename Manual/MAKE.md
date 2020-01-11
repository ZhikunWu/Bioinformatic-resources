



## maker

## [MAKER](https://www.yandell-lab.org/software/maker.html)
### [MAKER2 pipeline](https://reslp.github.io/blog/My-MAKER-Pipeline/)
### [Maker2 gene annotation pipeline](https://bioinformaticsworkbook.org/dataAnalysis/GenomeAnnotation/Intro_To_Maker.html)
### [MAKER Tutorial](http://weatherby.genetics.utah.edu/MAKER/wiki/index.php/MAKER_Tutorial_for_WGS_Assembly_and_Annotation_Winter_School_2018#Ab_Initio_Gene_Prediction)
### [Genome Annotation using MAKER](https://gist.github.com/darencard/bb1001ac1532dd4225b030cf0cd61ce2)



```
$ maker2zff

maker2zff [options] <gff3_file> <gff3_file> ...
maker2zff [options] -d <datastore_index>

OPTIONS
For determining which genes are High Confidence for Retraining, there are 7 criteria.
-c fraction  The fraction of splice sites confirmed by an EST alignment, default 0.5
-e fraction  The fraction of exons that overlap an EST alignment, default 0.5
-o fraction  The fraction of exons that overlap any evidence (EST or Protein), default 0.5
-a fraction  The fraction of splice sites confirmed by an ab-initio prediction, default 0
-t fraction  The fraction of exons that overlap an ab-initio prediction, default 0
-l number    The min length of the protein sequence produced by the mRNA
-x number    Max AED to allow 0.5 is default
-n           No filtering.  Accept all.

```



```
$ fathom

FATHOM - sequence and annotation tool (version 2006-07-28)

usage: fathom <ann> <dna> <commands>
commands:
  -help           report useful information
  -validate [-quiet]
  -gene-stats [-errors-ok -nucleotide -dinucleotide]
  -categorize <int>
  -export <int> [-plus -errors-ok]
  -extract <feature> -length <int> -offset <int>
  -exon-intron
  -split <-number <int> | -training <float> | -GC <float> | -repeat <float>>
  -ace-format <-gene-method <string> [-dna -extra <string>]>
  -compare-genes <predictions> [-details]
  -score-genes <hmm> [-errors-ok]
  -filter-genes <hmm> -min-score <float> -min-length <int>

```


```
$ forge

FORGE - training program for SNAP (version 2006-07-28)

usage: forge [options] <ann> <dna> [options]
options:
  -help
  -verbose
  -pseudocount <float>  [1]   (absolute number for all models)
  -pseudoCoding <float> [0.0] (eg. 0.05)
  -pseudoIntron <float> [0.0]
  -pseudoInter <float>  [0.0]
  -min-counts           [0]
  -lcmask [-fragmentN]
  -utr5-length <int>    [50]
  -utr5-offset <int>    [10]
  -utr3-length <int>    [50]
  -utr3-offset <int>    [10]
  -explicit <int>       [250]
  -min-intron <int>     [30]
  -boost <file>  (file of ID <int>)

```


```
$ hmm-assembler.pl

usage: hmm-assembler.pl <name> <directory of files from forge>
options:
  -i  <length>       [500]
  -e  <length>       [1000]
  -A  <order:length> [0:30]
  -D  <order:length> [0:9]
  -M  <order:length> [0:15]
  -S  <order:length> [0:9]
  -C  <order>        [4]
  -I  <order>        [4]
  -N  <order>        [4]
  -3  <order:length> []  include 3'UTR model, requires -a
  -a  <order:length> []  include PolyA model, requires -3
  -5  <order:length> []  include 5'UTR moel, requires -p
  -p                     include generic promoter model, requires -5
  -r                     include generic repeat model
  -o                     include reverse ORF model
  -x                     use explicit duration intron model
  -t                     include C.elegans trans-splicing, requires -p, -5
  -Z  <clade>            sets clade-specific values (worm, fly, plant)
  -1                     single gene model
  -c <score>             include GC-AG splice donor model

```


```
git clone https://github.com/hyphaltip/genome-scripts.git
```



```
$  etraining 
AUGUSTUS (3.2.2) is a gene prediction tool
written by M. Stanke, O. Keller, S. König, L. Gerischer and L. Romoth.

usage:
etraining --species=SPECIES trainfilename

'trainfilename' is the filename (including relative path) to the file in genbank format containing the training sequences. These can be multi-gene sequences.
SPECIES is a name for your species.

parameters:
--/genbank/verbosity=n
  Choose one of 0,1,2 or 3. The larger the verbosity, the more (error) messages you get.



```


```
$ augustus
AUGUSTUS (3.2.2) is a gene prediction tool
written by M. Stanke, O. Keller, S. König, L. Gerischer and L. Romoth.

usage:
augustus [parameters] --species=SPECIES queryfilename

'queryfilename' is the filename (including relative path) to the file containing the query sequence(s)
in fasta format.

SPECIES is an identifier for the species. Use --species=help to see a list.

parameters:
--strand=both, --strand=forward or --strand=backward
--genemodel=partial, --genemodel=intronless, --genemodel=complete, --genemodel=atleastone or --genemodel=exactlyone
  partial      : allow prediction of incomplete genes at the sequence boundaries (default)
  intronless   : only predict single-exon genes like in prokaryotes and some eukaryotes
  complete     : only predict complete genes
  atleastone   : predict at least one complete gene
  exactlyone   : predict exactly one complete gene
--singlestrand=true
  predict genes independently on each strand, allow overlapping genes on opposite strands
  This option is turned off by default.
--hintsfile=hintsfilename
  When this option is used the prediction considering hints (extrinsic information) is turned on.
  hintsfilename contains the hints in gff format.
--AUGUSTUS_CONFIG_PATH=path
  path to config directory (if not specified as environment variable)
--alternatives-from-evidence=true/false
  report alternative transcripts when they are suggested by hints
--alternatives-from-sampling=true/false
  report alternative transcripts generated through probabilistic sampling
--sample=n
--minexonintronprob=p
--minmeanexonintronprob=p
--maxtracks=n
  For a description of these parameters see section 4 of README.TXT.
--proteinprofile=filename
  When this option is used the prediction will consider the protein profile provided as parameter.
  The protein profile extension is described in section 7 of README.TXT.
--progress=true
  show a progressmeter
--gff3=on/off
  output in gff3 format
--predictionStart=A, --predictionEnd=B
  A and B define the range of the sequence for which predictions should be found.
--UTR=on/off
  predict the untranslated regions in addition to the coding sequence. This currently works only for a subset of species.
--noInFrameStop=true/false
  Do not report transcripts with in-frame stop codons. Otherwise, intron-spanning stop codons could occur. Default: false
--noprediction=true/false
  If true and input is in genbank format, no prediction is made. Useful for getting the annotated protein sequences.
--uniqueGeneId=true/false
  If true, output gene identifyers like this: seqname.gN

For a complete list of parameters, type "augustus --paramlist".
An exhaustive description can be found in the file README.TXT.

```


```
$ locate optimize_augustus.pl
/home/wuzhikun/anaconda3/envs/Assembly/scripts/optimize_augustus.pl
/home/wuzhikun/anaconda3/envs/NanoSV/bin/augustus-3.3.2/scripts/optimize_augustus.pl
/home/wuzhikun/anaconda3/envs/NanoSV/scripts/optimize_augustus.pl
/home/wuzhikun/anaconda3/pkgs/augustus-3.1-0/scripts/optimize_augustus.pl
/home/wuzhikun/anaconda3/pkgs/augustus-3.2.2-0/scripts/optimize_augustus.pl

```

```
$ locate gmes_petap.pl
/home/wuzhikun/anaconda3/envs/Assembly/bin/quast-5.0.2/build/lib/quast_libs/genemark-es/linux_32/gmes_petap.pl
/home/wuzhikun/anaconda3/envs/Assembly/bin/quast-5.0.2/build/lib/quast_libs/genemark-es/linux_64/gmes_petap.pl
/home/wuzhikun/anaconda3/envs/Assembly/bin/quast-5.0.2/build/lib/quast_libs/genemark-es/macosx/gmes_petap.pl
/home/wuzhikun/anaconda3/envs/Assembly/bin/quast-5.0.2/quast_libs/genemark-es/linux_32/gmes_petap.pl
/home/wuzhikun/anaconda3/envs/Assembly/bin/quast-5.0.2/quast_libs/genemark-es/linux_64/gmes_petap.pl
/home/wuzhikun/anaconda3/envs/Assembly/bin/quast-5.0.2/quast_libs/genemark-es/macosx/gmes_petap.pl

```


```
$ purge --help
### Use at your own risk! No guarantees whatsoever. You were warned. ###

Usage:  purge   [-a] [-c cf] [-d l] [-(f|F) fn | -(e|E) re] [-p h[:p]]
        [-P #] [-s] [-v] [-C dir [-H]] [-n]

 -a display a little rotating thingy to indicate that I am alive (tty only).
 -c c   squid.conf location, default "/usr/local/squid/etc/squid.conf".
 -C dir base directory for content extraction (copy-out mode).
 -d l   debug level, an OR mask of different debug options.
 -e re  single regular expression per -e instance (use quotes!).
 -E re  single case sensitive regular expression like -e.
 -f fn  name of textfile containing one regular expression per line.
 -F fn  name of textfile like -f containing case sensitive REs.
 -H prepend HTTP reply header to destination files in copy-out mode.
 -n do not fork() when using more than one cache_dir.
 -p h:p cache runs on host h and optional port p, default is localhost:3128.
 -P #   if 0, just print matches; otherwise OR the following purge modes:
       0x01 really send PURGE to the cache.
       0x02 remove all caches files reported as 404 (not found).
       0x04 remove all weird (inaccessible or too small) cache files.
    0 and 1 are recommended - slow rebuild your cache with other modes.
 -s show all options after option parsing, but before really starting.
 -v show more information about the file, e.g. MD5, timestamps and flags.


```