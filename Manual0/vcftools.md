## vcftools
```
$ conda install -c bioconda vcftools
```

```
$ vcftools

VCFtools (0.1.16)
© Adam Auton and Anthony Marcketta 2009

Process Variant Call Format files

For a list of options, please go to:
    https://vcftools.github.io/man_latest.html

Alternatively, a man page is available, type:
    man vcftools

Questions, comments, and suggestions should be emailed to:
    vcftools-help@lists.sourceforge.net
```


## vcfanno
```
$ conda install -c bioconda vcfanno
```

```
$ vcfanno

=============================================
vcfanno version 0.3.1 [built with go1.11]

see: https://github.com/brentp/vcfanno
=============================================
Usage:
vcfanno config.toml input.vcf > annotated.vcf

  -base-path string
        optional base-path to prepend to annotation files in the config
  -ends
        annotate the start and end as well as the interval itself.
  -lua string
        optional path to a file containing custom javascript functions to be used as ops
  -p int
        number of processes to use. (default 2)
  -permissive-overlap
        annotate with an overlapping variant even it doesn't share the same ref and alt alleles. Default is to require exact match between variants.
```

