
## [JELLYFISH - Fast, Parallel k-mer Counting for DNA](http://www.cbcb.umd.edu/software/jellyfish/)

Jellyfish is a tool for fast, memory-efficient counting of k-mers in DNA. A k-mer is a substring of length k, and counting the occurrences of all such substrings is a central step in many analyses of DNA sequence

### [jellyfish github](https://github.com/gmarcais/Jellyfish)

### install jellyfish
```
$ conda install -c bioconda jellyfish 
```


### run jellyfish

#### jellyfish parameters
```
$ jellyfish
Too few arguments
Usage: jellyfish <cmd> [options] arg...
Where <cmd> is one of: count, bc, info, stats, histo, dump, merge, query, cite, mem, jf.
Options:
  --version        Display version
  --help           Display this message

```


#### count kmers
```
$ jellyfish count -C -m 21 -s 20000000000 -t 20 -o ERR2173372.jf ERR2173372.fasta
```
Note you should adjust the memory (-s) and threads (-t) parameter according to your server. This example will use 10 threads and 1GB of RAM. The kmer length (-m) may need to be scaled if you have low coverage or a high error rate. You should always use "canonical kmers" (-C)

#### Export the kmer count histogram
```
$ jellyfish histo -t 20 ERR2173372  > ERR2173372.histo

$ head  ERR2173372.histo
1 105592919
2 2718015
3 644646
4 273383
5 142148
6 86095
7 57336
8 42597
9 32255
10 24965

```

