## [svtools](https://github.com/hall-lab/svtools)

### install svtools

It need the python 2 environment
```
$ conda install -c bioconda svtools
Solving environment: done

## Package Plan ##

  environment location: /home/wuzhikun/anaconda3/envs/Assembly

  added / updated specs: 
    - svtools


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    svtools-0.1.1              |           py27_2        49.7 MB  bioconda

The following NEW packages will be INSTALLED:

    svtools: 0.1.1-py27_2 bioconda

```

### parameters
```
$ svtools
svtools: comprehensive utilities to explore structural variations in genomes.

	Hall-lab
	$Revision: 0.0.1 $
	$Date: 2015-10-14 14:31 $

usage:    svtools <subcommand> [options]
The svtools sub-commands include:
[ general utilities ]
  vcftobedpe      converts vcf file into bedpe.
  bedpetovcf      converts bedpe file to vcf.
  bedpetobed12    converts bedpe file to bed12.
  vcfsort         sorts a vcf file.
  bedpesort       sorts a bedpe file.


[ callset generation ]
  prune           cluster a BEDPE file by position based on allele frequency.
  varlookup       look for variants common between two bedpe files.
  afreq           add allele frequency information to a VCF file.
  lsort           sorts a vcf file by type.
  lmerge          merges multiple sorted vcf files.
  genotype        return a vcf file with genotype information added by svtyper.
  copynumber      add cn information using cnvnator.
  vcfpaste        combine multiple vcf files produced by genotype command.
  classify        classify structural variants


[ General help ]
  --help          print this help menu.
  --version       what version of svtools are you using?.
  --contact       feature requests, bugs, mailing lists, etc.

```