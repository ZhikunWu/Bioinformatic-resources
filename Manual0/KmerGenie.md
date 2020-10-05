
### [KmerGenie](http://kmergenie.bx.psu.edu/)
 estimates the best k-mer length for genome de novo assembly
 
### [KmerGenie report](http://kmergenie.bx.psu.edu/sample_report.html#advhelp)

### install KmerGenie
```
$ conda install -c bioconda kmergenie 
```
or

```
$ wget http://kmergenie.bx.psu.edu/kmergenie-1.7048.tar.gz
$ tar -zxf kmergenie-1.7048.tar.gz
$ cd kmergenie-1.7048/

$ make
cd ntCard && ./configure && make
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for gawk... (cached) gawk
checking for gcc... /usr/bin/gcc:
checking whether the C compiler works... no
configure: error: in `/home/wzk/anaconda3/envs/evolution/bin/kmergenie-1.7048/ntCard':
configure: error: C compiler cannot create executables
See `config.log' for more details
makefile:75: recipe for target 'ntCard/ntcard' failed
make: *** [ntCard/ntcard] Error 77

```

install **ntcard**
```
$ conda install -c bioconda ntcard
$ cp /home/wzk/anaconda3/envs/evolution/bin/ntcard /home/wzk/anaconda3/envs/evolution/bin/kmergenie-1.7048/ntCard/
```


### parameters
```
$ ./kmergenie 
KmerGenie 1.7048

Usage:
    kmergenie <read_file> [options]

Options:
    --diploid    use the diploid model (default: haploid model)
    --one-pass   skip the second pass to estimate k at 2 bp resolution (default: two passes)
    -k <value>   largest k-mer size to consider (default: 121)
    -l <value>   smallest k-mer size to consider (default: 15)
    -s <value>   interval between consecutive kmer sizes (default: 10)
    -e <value>   k-mer sampling value (default: auto-detected to use ~200 MB memory/thread)
    -t <value>   number of threads (default: number of cores minus one)
    -o <prefix>  prefix of the output files (default: histograms)
    --debug      developer output of R scripts
    --orig-hist  legacy histogram estimation method (slower, less accurate)

```

### run kmergenie
```
$ kmergenie -o ERR2173372 ERR2173372.fasta
running histogram estimation
Setting maximum kmer length to: 9239942 bp
computing histograms (from k=21 to k=121): 71 121 51 91 61 81 31 111 101 21 41 
ntCard wall-clock time over all k values: 10 seconds 
fitting model to histograms to estimate best k
could not fit ERR2173372-k121.histo
could not fit ERR2173372-k81.histo
could not fit ERR2173372-k111.histo
could not fit ERR2173372-k91.histo
could not fit ERR2173372-k71.histo
could not fit ERR2173372-k101.histo
could not fit ERR2173372-k61.histo
could not fit ERR2173372-k41.histo
could not fit ERR2173372-k51.histo
could not fit ERR2173372-k31.histo
estimation of the best k so far: 21
refining estimation around [15; 27], with a step of 2
running histogram estimation
Setting maximum kmer length to: 9239942 bp
computing histograms (from k=17 to k=27): 17 23 27 19 25 21 
ntCard wall-clock time over all k values: 9 seconds 
fitting model to histograms to estimate best k
could not fit ERR2173372-k111.histo
could not fit ERR2173372-k101.histo
could not fit ERR2173372-k81.histo
could not fit ERR2173372-k71.histo
could not fit ERR2173372-k91.histo
could not fit ERR2173372-k121.histo
could not fit ERR2173372-k61.histo
could not fit ERR2173372-k41.histo
could not fit ERR2173372-k51.histo
could not fit ERR2173372-k25.histo
could not fit ERR2173372-k31.histo
table of predicted num. of genomic k-mers: ERR2173372.dat
recommended coverage cut-off for best k: 4
best k: 19

```

### output a series of reports
most imortant:
ERR2173372_report.html and ERR2173372.dat
```
$ cat  ERR2173372.dat
k genomic.kmers cov.cutoff
17 19630 26
19 89863 4
21 2447 24
23 738 49
27 353 40


```



### kmergenie example
```
$ kmergenie file_list -l 21 -k 141
running histogram estimation
list of reads:
/home/wzk/Project/C128/clean/J1-08/J1-08.clean.paired.R1.fq.gz
/home/wzk/Project/C128/clean/J1-08/J1-08.clean.paired.R2.fq.gz
Setting maximum kmer length to: 150 bp
computing histograms (from k=21 to k=141): 
ntCard wall-clock time over all k values: 212 seconds 
fitting model to histograms to estimate best k
table of predicted num. of genomic k-mers: histograms.dat
recommended coverage cut-off for best k: 2
best k: 101
```


output:
```
histograms_report.html
histograms.dat.pdf
histograms.dat
```

```
$cat histograms.dat

k genomic.kmers cov.cutoff
21 10837842 6
31 831900 21
41 3698744 6
51 2668375 6
61 2199876 6
71 1371561 6
81 845647 6
91 10794119 3
97 5862463 3
99 62597 15
101 13935560 2
103 107152 11
105 55919 13
107 27584 18
111 10760980 2
121 7403374 2
131 8786 12
141 24230 7
```
