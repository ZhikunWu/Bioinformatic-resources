## [pinfish]()

```
$ cluster_gff  --help
Usage of cluster_gff:
  -V	Print out version.
  -a string
    	Write clusters in tabular format in this file.
  -c int
    	Minimum cluster size. (default 10)
  -d int
    	Exon boundary tolerance. (default 10)
  -e int
    	Terminal exons boundary tolerance. (default 30)
  -h	Print out help message.
  -p float
    	Minimum isoform percentage. (default 1)
  -prof string
    	Write out CPU profiling information.
  -t int
    	Number of cores to use. (default 4)

```

```
$ spliced_bam2gff --help
Usage of spliced_bam2gff:
  -M	Input is from minimap2.
  -V	Print out version.
  -g	Use strand tag as feature orientation then read strand if not available.
  -h	Print out help message.
  -s	Use read strand (from BAM flag) as feature orientation.
  -t int
    	Number of cores to use. (default 4)

```


```
$ collapse_partials --help
Usage of collapse_partials:
  -M	Discard monoexonic transcripts.
  -U	Discard transcripts which are not oriented.
  -V	Print out version.
  -d int
    	Internal exon boundary tolerance. (default 5)
  -e int
    	Three prime exons boundary tolerance. (default 30)
  -f int
    	Five prime exons boundary tolerance. (default 5000)
  -h	Print out help message.
  -prof string
    	Write out CPU profiling information.
  -t int
    	Number of cores to use. (default 4)

```

```
$ polish_clusters --help
Usage of polish_clusters:
  -V	Print out version.
  -a string
    	Read cluster memberships in tabular format.
  -c int
    	Minimum cluster size. (default 1)
  -d string
    	Location of temporary directory.
  -h	Print out help message.
  -m	Do not load all reads in memory (slower).
  -o string
    	Output fasta file.
  -t int
    	Number of cores to use. (default 4)
  -x string
    	Arguments passed to minimap2.
  -y string
    	Arguments passed to racon.

```