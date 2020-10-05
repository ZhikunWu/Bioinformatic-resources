
## [lordfast](https://github.com/vpc-ccg/lordfast)
 Sensitive and Fast Alignment Search Tool for Long Read sequencing Data

### install loadfast
```
conda install -c bioconda lordfast
```


### loadfast parameter
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



lordFAST                  Last Updated: June 26, 2018              lordFAST(1)

```


### run lordfast

#### Indexing the reference genome
```
lordfast --index gen.fa
```

#### map to reference genome

```
lordfast --search gen.fa --seq reads.fastq --threads 4 > map.sam
```