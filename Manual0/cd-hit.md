## cd-hit manual

It is mainly designed for alignment of amono acid

### install cd-hit
```bash
$ conda install -c bioconda cd-hit 
```

### make for the binary
```bash
$ make MAX_SEQ=500000
```

### [CDHIT to FASTA](https://github.com/LeeBergstrand/CDHITtoFASTA)
Extracts CD-Hit clusters which contain reference proteins and stores them in FASTA format.

CD-HIT is a widely used program for clustering biological sequences to reduce sequence redundancy and improve the performance of other sequence analyses. CD-HIT was originally developed to cluster protein sequences to create reference databases with reduced redundancy and was then extended to support clustering nucleotide sequences and comparing two datasets.

CD-Hit can also be used to cluster sequences and outputs a cluster file (extension .clstr) contains the accessions of clustered sequence from an input FASTA file.

CDHITtoFASTA uses this cluster file to filter input FASTA files by extracting sequences from the file which CD-Hit finds to cluster with reference sequences.
```
$ python ~/PATH_TO_DIR/CDHITtoFASTA -h
usage: CDHITtoFASTA [-h] [-i CLUSTER] [-s FASTA] [-r LIST]

Extracts CD-Hit clusters which contain reference proteins and stores them in
FASTA format.

optional arguments:
  -h, --help            show this help message and exit
  -i CLUSTER, --cluster_file CLUSTER
                        CD-Hit cluster file which provides clustering
                        information.
  -s FASTA, --sequence_file FASTA
                        FASTA file which provides sequences to be extracted.
  -r LIST, --reference_list LIST
                        File of sequence identifiers (one per line) who's CD-
                        HIT clusters should turned into FASTA files.
```



### run cd-hit
```
$ cd-hit -i MetaContig.faa -o hit -c 0.95 -s 0.9  -n 5  -T 8
```

output files
```
-rw-r--r-- 1 3.3K Oct 19 03:28 hit
-rw-r--r-- 1  900 Oct 19 03:28 hit.clstr
```

### [common use](https://github.com/weizhongli/cdhit/wiki/3.-User%27s-Guide)
```
$ cd-hit -i nr -o nr100 -c 1.00 -n 5 -M 16000 -T 8
$ cd-hit -i db -o db90 -c 0.9 -n 5 -M 16000 -T 8
```
  
where
```
  db is the filename of input,
  db90 is output, 
  -c 1.0, means 100% identity, is the clustering threshold
  -c 0.9, means 90% identity, is the clustering threshold
  -n 5 is the word size
  -M 16000, to use 16GB RAM
  -T 8, to use 8 threads
```

### example
```
$ cd-hit -i /home/wzk/metagenome_data/annotate/MetaContig.faa -o /home/wzk/metagenome_data/ORFCluster/representive.faa -c 0.95 -aL 0.9  -n 5  -T 16
```
