## prefetch

### [Downloading SRA data using command line utilities](https://www.ncbi.nlm.nih.gov/books/NBK158899/)

### install sra-tools

**prefetch** is tool in sra-tools suit

```
$ conda install -c bioconda sra-tools
```

### prefetch parameters
```
$ prefetch --help

Usage:
  prefetch [options] <SRA accession | kart file> [...]
  Download SRA or dbGaP files and their dependencies

  prefetch [options] <SRA file> [...]
  Check SRA file for missed dependencies and download them

  prefetch --list <kart file> [...]
  List the content of a kart file


Options:
  -f|--force <value>               force object download one of: no, yes, 
                                   all. no [default]: skip download if the 
                                   object if found and complete; yes: download 
                                   it even if it is found and is complete; all: 
                                   ignore lock files (stale locks or it is 
                                   being downloaded by another process: use at 
                                   your own risk!) 

  -t|--transport <value>           transport: one of: fasp; http; both. (fasp 
                                   only; http only; first try fasp (ascp), use 
                                   http if cannot download using fasp). 
                                   Default: both 
  -l|--list                        list the content of kart file 
  -n|--numbered-list               list the content of kart file with kart 
                                   row numbers 
  -s|--list-sizes                  list the content of kart file with target 
                                   file sizes 
  -R|--rows <rows>                 kart rows (default all). row list should be 
                                   ordered 
  -N|--min-size <size>             minimum file size to download in KB 
                                   (inclusive). 
  -X|--max-size <size>             maximum file size to download in KB 
                                   (exclusive). Default: 20G 
  -o|--order <value>               kart prefetch order: one of: kart, size. (in 
                                   kart order, by file size: smallest first), 
                                   default: size 
  -a|--ascp-path <ascp-binary|private-key-file>  path to ascp program and 
                                   private key file (asperaweb_id_dsa.putty) 
  --ascp-options <value>           arbitrary options to pass to ascp command 
                                   line 
  -p|--progress <value>            time period in minutes to display download 
                                   progress (0: no progress), default: 1 
  --eliminate-quals                don't download QUALITY column 

  -c|--check-all                   double-check all refseqs 

  -h|--help                        Output brief explanation for the program. 
  -V|--version                     Display the version of the program then 
                                   quit. 
  -L|--log-level <level>           Logging level as number or enum string. One 
                                   of (fatal|sys|int|err|warn|info|debug) or 
                                   (0-6) Current/default is warn 
  -v|--verbose                     Increase the verbosity of the program 
                                   status messages. Use multiple times for more 
                                   verbosity. Negates quiet. 
  -q|--quiet                       Turn off all status messages for the 
                                   program. Negated by verbose. 
  --option-file <file>             Read more options and parameters from the 
                                   file. 

prefetch : 2.8.1


```


### download data
```
$ prefetch SRR7346978

2018-12-29T02:34:15 prefetch.2.8.1 warn: Maximum file size download limit is 20GB 
2018-12-29T02:34:15 prefetch.2.8.1: 1) 'SRR7346978' (154GB) is larger than maximum allowed: skipped 
2018-12-29T02:34:22 prefetch.2.8.1: 'SRR7346978' has no remote vdbcache

Download of some files was skipped because they are too large
You can change size download limit by setting
--min-size and --max-size command line arguments
```

set the larger value for **--max-size**
```
prefetch SRR7346978  --max-size 200000000000
```

### convert sra to fastq

```
/usr/local/sratoolkit/bin/fastq-dump --outdir fastq --gzip --skip-technical --readids --dumpbase --split-files --clip SRRxxxxxx
```

