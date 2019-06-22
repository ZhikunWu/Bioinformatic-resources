### docker of edirect 

#### [NCBI docker](https://github.com/ncbi/docker/tree/master/edirect)

```
$ docker run --rm -it ncbi/edirect efetch -db nucleotide -id u00001 -format fasta
Unable to find image 'ncbi/edirect:latest' locally
latest: Pulling from ncbi/edirect


$ docker run --rm -it ncbi/edirect /bin/sh -c " esearch -db nucleotide -query u00001 | efetch -format fasta"
```


### sra-toolkit
```
$ docker pull inutano/sra-toolkit
$ docker run --rm -v "$(pwd)":/data -w /data inutano/sra-toolkit fastq-dump /data/mydata.sra
```


