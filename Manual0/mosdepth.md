
## [mosdepth](https://github.com/brentp/mosdepth)

fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing

### install mosdepth
```
$ conda install -c bioconda mosdepth
```


### mosdepth parameters

```
$ mosdepth -help
mosdepth 0.2.4

  Usage: mosdepth [options] <prefix> <BAM-or-CRAM>

Arguments:

  <prefix>       outputs: `{prefix}.mosdepth.dist.txt`
                          `{prefix}.per-base.bed.gz` (unless -n/--no-per-base is specified)
                          `{prefix}.regions.bed.gz` (if --by is specified)
                          `{prefix}.quantized.bed.gz` (if --quantize is specified)
                          `{prefix}.thresholds.bed.gz` (if --thresholds is specified)

  <BAM-or-CRAM>  the alignment file for which to calculate depth.

Common Options:

  -t --threads <threads>     number of BAM decompression threads [default: 0]
  -c --chrom <chrom>         chromosome to restrict depth calculation.
  -b --by <bed|window>       optional BED file or (integer) window-sizes.
  -n --no-per-base           dont output per-base depth. skipping this output will speed execution
                             substantially. prefer quantized or thresholded values if possible.
  -f --fasta <fasta>         fasta file for use with CRAM files [default: ].

Other options:

  -F --flag <FLAG>              exclude reads with any of the bits in FLAG set [default: 1796]
  -i --include-flag <FLAG>      only include reads with any of the bits in FLAG set. default is unset. [default: 0]
  -x --fast-mode                dont look at internal cigar operations or correct mate overlaps (recommended for most use-cases).
  -q --quantize <segments>      write quantized output see docs for description.
  -Q --mapq <mapq>              mapping quality threshold [default: 0]
  -T --thresholds <thresholds>  for each interval in --by, write number of bases covered by at
                                least threshold bases. Specify multiple integer values separated
                                by ','.
  -R --read-groups <string>     only calculate depth for these comma-separated read groups IDs.
  -h --help                     show help

```


output file:
```
$ tree mosdepth
mosdepth
├── ERR2631603.mosdepth.global.dist.txt
├── ERR2631603.mosdepth.region.dist.txt
├── ERR2631603.regions.bed.gz
└── ERR2631603.regions.bed.gz.csi
```

detail for output:
```
$ tail ERR2631603.mosdepth.global.dist.txt
X   2   0.00
X   1   0.04
X   0   1.00
Y   2   0.00
Y   1   0.00
Y   0   1.00
total   3   0.00
total   2   0.00
total   1   0.04
total   0   1.00

$ tail ERR2631603.mosdepth.region.dist.txt
X   2   0.00
X   1   0.04
X   0   1.00
Y   2   0.00
Y   1   0.00
Y   0   1.00
total   3   0.00
total   2   0.00
total   1   0.04
total   0   1.00

$ less ERR2631603.regions.bed
10      4900000 4900500 0.00
10      4900500 4901000 0.00
10      4901000 4901500 0.00
10      4901500 4902000 0.00
10      4902000 4902500 0.00
10      4902500 4903000 0.49
10      4903000 4903500 0.90
10      4903500 4904000 0.92
10      4904000 4904500 0.91
10      4904500 4905000 0.92
10      4905000 4905500 0.93
10      4905500 4906000 0.92
10      4906000 4906500 0.94
10      4906500 4907000 0.94

```


### plot
```
$ python /home/wzk/github/nano-snakemake/scripts/mosdepth_plot-dist.py  -o ERR2631603.mosdepth.global.dist_hist.html ERR2631603.mosdepth.global.dist.txt

```
