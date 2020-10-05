
# Download SRA data of Project

## Download softwares

### Download edirect
```
$ wget ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.zip
unzip edirect && cd edirect/
```

### Construct the links for tools to the PATH
```
$ ln -s /home/wzk/anaconda3/envs/evolution/bin/edirect/esearch /home/wzk/anaconda3/envs/evolution/bin/esearch
$ ln -s /home/wzk/anaconda3/envs/evolution/bin/edirect/edirect.pl  /home/wzk/anaconda3/envs/evolution/bin/edirect.pl
$ ln -s /home/wzk/anaconda3/envs/evolution/bin/edirect/efetch  /home/wzk/anaconda3/envs/evolution/bin/efetch
```

or set the **PATH** enviroment


### Download **sratoolkit**

First you should create the [**anaconda**](https://www.anaconda.com) environment

```
$ conda install -c daler sratoolkit
```

**fastq-dump** is in the tool suit **sratoolkit**

## Get the SRA data associated with the project

### Get the information for the project
```
$ /home/wzk/anaconda3/envs/evolution/bin/edirect/esearch -db sra -query PRJNA328296  | /home/wzk/anaconda3/envs/evolution/bin/edirect/efetch --format runinfo > PRJNA328296
```

### Get the download links of SRA files
```
$ cut -d "," -f 10 PRJNA328296 | sed '1d' > PRJNA328296_run

https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005356/SRR5484651
https://sra-download.ncbi.nlm.nih.gov/traces/sra48/SRR/005426/SRR5556563
https://sra-download.ncbi.nlm.nih.gov/traces/sra48/SRR/005426/SRR5556590
https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005450/SRR5581542
https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005356/SRR5484652
https://sra-download.ncbi.nlm.nih.gov/traces/sra48/SRR/005356/SRR5484653
https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005450/SRR5581543
https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005450/SRR5581544
https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005356/SRR5484654
https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005356/SRR5484655
https://sra-download.ncbi.nlm.nih.gov/traces/sra63/SRR/005490/SRR5621803
https://sra-download.ncbi.nlm.nih.gov/traces/sra2/SRR/004623/SRR4734730
https://sra-download.ncbi.nlm.nih.gov/traces/sra4/SRR/004623/SRR4734731
https://sra-download.ncbi.nlm.nih.gov/traces/sra1/SRR/004623/SRR4734732
```

### Download the SRA data
```
$ sed 's/^/wget  /g' PRJNA328296_run > PRJNA328296_download.sh
$ chmod +x PRJNA328296_download.sh
$ ./PRJNA328296_download.sh
```


## Download SRA data parallelly

### Download [parallel](http://www.gnu.org/software/parallel/) in anaconda environment


```
$ conda install -c bioconda parallel
```

#### [Rust parallel and tutorial](https://github.com/mmstick/parallel)

### To get the SRR numbers associated with the project
```
$ esearch -db sra -query PRJNA301162 | efetch --format runinfo | sed '1d' | cut -d "," -f 1 > SRR.numbers
```

```
$ head -n 3 SRR.numbers

SRR2927328
SRR2927329
SRR2927330
```

### To download them all in parallel 

Download 2 files at the same time using parallel

```
$ parallel --jobs 2 "fastq-dump --split-files --origfmt --gzip {}" ::: SRR2927328 SRR2927329
```



## Convert SRA data to fastq data 

### Convert data using **fastq-dump**
```
$ fastq-dump SRR5484651.sra  --split-files --origfmt --gzip
```


### something wrong with fastq-dump

```
$ fastq-dump ERR1016541.sra --split-files --origfmt --gzip 
2018-10-24T06:53:56 fastq-dump.2.8.2 warn: too many reads 37 at spot id 11424, maximum 32 supported, skipped
Rejected 52 SPOTS because of to many READS
Read 163482 spots for ERR1016541
Written 163427 spots for ERR1016541
```

### Split reads with parameter **split-3**
```
$  fastq-dump ERR1016541.sra --split-3 --origfmt --gzip ERR1016541

Rejected 8955 READS because of filtering out non-biological READS
Read 163482 spots for ERR1016541
Written 163401 spots for ERR1016541
```

output files
```
-rw-r--r-- 1 17M Oct 24 03:08 ERR1016541_1.fastq.gz
-rw-r--r-- 1 11M Oct 24 03:08 ERR1016541_2.fastq.gz
-rw-r--r-- 1 99M Oct 24 03:08 ERR1016541.fastq.gz

```

## Downloading all SRA files related to a BioProject/study

To get the SRR numbers associated with the project:
```
esearch -db sra -query PRJNA301162 | efetch --format runinfo |cut -d "," -f 1 > SRR.numbers
```

To download them all in parallel (limit the number to 3 concurrent downloads)
```
parallel --jobs 3 "fastq-dump --split-files --origfmt --gzip {}" ::: SRR.numbers
```
