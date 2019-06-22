## [GenomeTools](http://genometools.org): The versatile open source genome analysis software

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

