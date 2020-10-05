## lordfast
### index for reference genome
```
$ lordfast  --index  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa
[NOTE] (bwt_index) building the index...
[bwa_index] Pack FASTA... 2.65 sec
[bwa_index] Construct BWT for the packed sequence...
[BWTIncCreate] textLength=497912844, availableWord=47034604
[BWTIncConstructFromPacked] 10 iterations done. 76325452 characters processed.
[BWTIncConstructFromPacked] 20 iterations done. 142216380 characters processed.
[BWTIncConstructFromPacked] 30 iterations done. 200776364 characters processed.
[BWTIncConstructFromPacked] 40 iterations done. 252820604 characters processed.
[BWTIncConstructFromPacked] 50 iterations done. 299073676 characters processed.
[BWTIncConstructFromPacked] 60 iterations done. 340179500 characters processed.
[BWTIncConstructFromPacked] 70 iterations done. 376710428 characters processed.
[BWTIncConstructFromPacked] 80 iterations done. 409175164 characters processed.
[BWTIncConstructFromPacked] 90 iterations done. 438025868 characters processed.
[BWTIncConstructFromPacked] 100 iterations done. 463664428 characters processed.
[BWTIncConstructFromPacked] 110 iterations done. 486447996 characters processed.
[bwt_gen] Finished constructing BWT in 116 iterations.
[bwa_index] 222.88 seconds elapse.
[bwa_index] Update BWT... 1.51 sec
[bwa_index] Pack forward-only FASTA... 1.48 sec
[bwa_index] Construct SA from BWT and Occ... 64.45 sec
[NOTE] (bwt_index) index was built in 302.56 seconds (294.90 CPU seconds)
```

output files:

```
-rw-rw-r-- 1 2.5K Mar 13 09:10 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.amb
-rw-rw-r-- 1   42 Mar 13 09:10 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.ann
-rw-rw-r-- 1 238M Mar 13 09:10 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.bwt
-rw-rw-r-- 1 257M Mar 13 09:11 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.cache
-rw-rw-r-- 1  60M Mar 13 09:10 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.pac
-rw-rw-r-- 1 119M Mar 13 09:11 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.sa

```

md5 values of bwa index files:
```
6739d5324c62df1f2eb2111ec7805883  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.amb
be6c479b42a059dd2f0e1ef22c3dab99  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.ann
4bb7ca0c4e6e83affbbdce8e9f167ab3  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.bwt
769ff3056818188574e7b28c7278747b  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.cache
51eb8221d49a2feed5014be302712f1c  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.pac
f246f56edc0e66ed9d233d8184d86776  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.sa
```


note: lordfast 建立的索引比bwa的索引多一个后缀为**.cache**的文件


### lordfast parameters
```

$ lordfast --help
lordFAST(1)                     lordfast Manual                    lordFAST(1)



NAME
       lordfast


DESCRIPTION
       lordFAST  is  a  sensitive  tool for mapping long reads with high error
       rates. lordFAST is specially designed for aligning  reads  from  PacBio
       sequencing  technology  but  provides  the  user  the ability to change
       alignment parameters depending on the reads and application.


INSTALLATION
       lordFast can be installed using conda  package  manager  (via  bioconda
       channel) using the following command:
       $ conda install -c bioconda lordfast

       In order to build from source, please download the latest release from
       https://github.com/vpc-ccg/lordfast/releases
       or alternatively clone the repository by running the following command:
       $ git clone https://github.com/vpc-ccg/lordfast.git

       Now the code can be compiled easily  by  running  "make"  command  line
       which builds the binary file "lordfast".
       $ cd lordfast
       $ make


SYNOPSIS
       lordfast --index FILE [OPTIONS]
       lordfast --search FILE --seq FILE [OPTIONS]


OPTIONS
   Indexing options
       -I, --index STR
              Path  to the reference genome file in FASTA format which is sup-
              posed to be indexed. [required]

   Mapping options
       -S, --search STR
              Path to the reference genome file in FASTA format. [required]

       -s, --seq STR
              Path to the file containing read sequences in  FASTA/FASTQ  for-
              mat. [required]

       -o, --out STR
              Write output to STR file rather than standard output. [stdout]

       -t, --threads INT
              Use  INT  number  of  CPU cores. Pass 0 to use all the available
              cores. [1]

   Advanced options
       -k, --minAnchorLen INT
              Minimum required length of anchors to be considered. [14]

       -n, --numMap INT
              Perform alignment for at most INT candidates. [10]

       -l, --minReadLen INT
              Do not try to map any read shorter than INT bp and  report  them
              as unmapped. [1000]

       -c, --anchorCount INT
              Consider INT anchoring positions on the long read. [1000]

       -m, --maxRefHit INT
              Ignore  anchoring  positions  with more than INT reference hits.
              [1000]

       -R, --readGroup STR
              SAM read group line in a format like '@RGID:fooSM:bar'. []

       -a, --chainAlg INT
              Chaining algorithm to use. Options are "dp-n2" and "clasp". [dp-
              n2]

       --noSamHeader
              Do not print sam header in the output.

   Other options
       -h, --help
              Print this help file.

       -v, --version
              Print the version of software.


EXAMPLES
       Indexing the reference genome:
       $ ./lordfast --index gen.fa

       Mapping to the reference genome:
       $ ./lordfast --search gen.fa --seq reads.fastq > map.sam
       $ ./lordfast --search gen.fa --seq reads.fastq --threads 4 > map.sam


BUGS
       Please report the bugs through lordfast's issues page at
       https://github.com/vpc-ccg/lordfast/issues


CONTACT
       Ehsan Haghshenas (ehaghshe@sfu.ca)


COPYRIGHT AND LICENSE
       This software is released under  GNU General Public License (v3.0)
       Copyright (c) 2018 Simon Fraser University, All rights reserved.

```




### run lordfast
```
$ lordfast --search /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa --seq  FAB45321_sub.fastq  --threads 20 --readGroup '@RGID:FAB45321SM:FAB45321'  >  FAB45321_lordfast-1.sam
[NOTE] number of threads: 20
[NOTE] (bwt_load) loading the index... 
[NOTE] (bwt_load) index was loaded in 0.35 seconds (0.34 CPU seconds)
Reading input... loaded 2968 reads in 0.09 seconds (0.09 CPU seconds)
	mapping... done in 14.47 seconds (269.89 CPU seconds)
Reading input... no more reads
[NOTE] processed 2968 reads in 14.97 seconds (270.38 CPU seconds)
```



