
## [sourmash](https://github.com/dib-lab/sourmash)

### install sourmash (both for python2 and python3)
```bash
$ conda install -c bioconda sourmash 
```

### Generate a signature for Illumina reads

Compute a scaled MinHash signature from our reads:
```bash
$ sourmash compute --scaled 10000 /home/wzk/metagenome_data/raw/HMP_GUT_SRS052697.25M.*.fastq.gz -o HMP_GUT_SRS052697.25M.sig -k 31
```
output file
```
$ head -n 20 HMP_GUT_SRS052697.25M.sig
[
    {
        "class": "sourmash_signature", 
        "email": "", 
        "filename": "/home/wzk/metagenome_data/raw/HMP_GUT_SRS052697.25M.2.fastq.gz", 
        "hash_function": "0.murmur64", 
        "signatures": [
            {
                "ksize": 31, 
                "max_hash": 1844674407370955, 
                "md5sum": "4ec33393312e29e31e3c7a2e57e25c30", 
                "mins": [
                    19089288576910, 
                    30202890984715, 
                    56643530363443, 
                    66484998380324, 
                    86499437302286, 
                    86651389579685, 
                    95528205715438, 
                    108082001389912, 

```

### Compare reads to assemblies
how much of the read content is contained in the reference genome?

Build a signature for an E. coli genome:
```bash
$ sourmash compute --scaled 10000 -k 31 /home/wzk/metagenome_data/assembly/Meta.contigs_cut.fa  -o HMP_GUT_SRS052697.25M_genome.sig
```

now evaluate containment, that is, what fraction of the read content is contained in the genome:
```bash
$ sourmash search -k 31 --containment HMP_GUT_SRS052697.25M.sig HMP_GUT_SRS052697.25M_genome.sig

```

