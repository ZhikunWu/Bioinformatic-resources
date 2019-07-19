## pomoxis

### install pomoxis
```
Installing assess_assembly script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing mini_align script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing mini_assemble script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing intersect_assembly_errors script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing align_serve script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing catalogue_errors script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing common_errors_from_bam script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing coverage_from_bam script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing coverage_from_fastx script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing fast_convert script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing long_fastx script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing pomoxis_path script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing qscores_from_summary script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing read_until_filter script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing ref_seqs_from_bam script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing simulate_calls script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing split_fastx script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing stats_from_bam script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing subsample_bam script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing summary_from_stats script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
Installing trim_alignments script to /home/wuzhikun/anaconda3/envs/NanoSV/bin
```



### pomoxis tools
```
$ mini_assemble
mini_assemble [-h] -i <fastq>

Assemble fastq/fasta formatted reads and perform POA consensus.

    -h  show this help text.
    -i  fastx input reads (required).
    -r  reference fasta for reference-guided consensus (instead of de novo assembly)
    -o  output folder (default: assm).
    -p  output file prefix (default: reads).
    -t  number of minimap and racon threads (default: 1).
    -m  number of racon rounds (default: 4).
    -n  number of racon shuffles (default: 1. If not 1, should be >10).
    -w  racon window length (default: 500).
    -k  keep intermediate files (default: delete).
    -K  minimap -K option (default: 500M).
    -c  trim adapters from reads prior to everything else.
    -e  error correct longest e% of reads prior to assembly, or an estimated coverage (e.g. 2x).
        For an estimated coverage, the -l option must be a fastx or a length (e.g. 4.8mb).
    -l  Reference length, either as a number (e.g. 4.8mb) or fastx from which length will be calculated.
    -x  log all commands before running.
-i must be specified.

```

### assess_assembly
```
$ assess_assembly
assess_assembly [-h] -r <reference> -i <fastq>

Calculate accuracy statistics for an assembly. 

    -h  show this help text.
    -r  reference, should be a fasta file. If correspondng bwa indices
        do not exist they will be created. (required).
    -i  fastq/a input assembly (required).
    -c  chunk size. Input reads/contigs will be broken into chunks
        prior to alignment, 0 will not chunk (default 100000).
    -C  catalogue errors. 
    -t  alignment threads (default: 1).
    -p  output file prefix (default: assm).
    -T  trim consensus to primary alignments of truth to assembly.
    -b  .bed file of reference regions to assess.
-i and -r must be specified.

```

### simulate_calls

```
$ simulate_calls
usage: simulate_calls [-h] [--mu MU] [--sigma SIGMA] [--noise NOISE]
                      [--threads THREADS]
                      fasta ncalls
simulate_calls: error: the following arguments are required: fasta, ncalls

```

### subsample_bam

```
$ subsample_bam -h
usage: subsample bam to uniform or proportional depth [-h] [-o OUTPUT_PREFIX]
                                                      [-r REGIONS [REGIONS ...]]
                                                      [-p PROFILE]
                                                      [-O {fwd,rev}]
                                                      [-t THREADS]
                                                      [-q QUALITY]
                                                      [-a ACCURACY]
                                                      [-c COVERAGE]
                                                      [--any_fail | --all_fail]
                                                      [-x PATIENCE]
                                                      [-s STRIDE] [-P]
                                                      [-S SEED]
                                                      bam depth [depth ...]

positional arguments:
  bam                   input bam file.
  depth                 Target depth.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_PREFIX, --output_prefix OUTPUT_PREFIX
                        Output prefix (default: sub_sampled)
  -r REGIONS [REGIONS ...], --regions REGIONS [REGIONS ...]
                        Only process given regions. (default: None)
  -p PROFILE, --profile PROFILE
                        Stride in genomic coordinates for depth profile.
                        (default: 1000)
  -O {fwd,rev}, --orientation {fwd,rev}
                        Sample only forward or reverse reads. (default: None)
  -t THREADS, --threads THREADS
                        Number of threads to use. (default: -1)
  -q QUALITY, --quality QUALITY
                        Filter reads by mean qscore. (default: None)
  -a ACCURACY, --accuracy ACCURACY
                        Filter reads by accuracy. (default: None)
  -c COVERAGE, --coverage COVERAGE
                        Filter reads by coverage (what fraction of the read
                        aligns). (default: None)
  --any_fail            Exit with an error if any region has insufficient
                        coverage. (default: False)
  --all_fail            Exit with an error if all regions have insufficient
                        coverage. (default: False)

Uniform sampling options:
  -x PATIENCE, --patience PATIENCE
                        Maximum iterations with no change in median coverage
                        before aborting. (default: 5)
  -s STRIDE, --stride STRIDE
                        Stride in genomic coordinates when searching for new
                        reads. Smaller can lead to more compact pileup.
                        (default: 1000)

Proportional sampling options:
  -P, --proportional    Activate proportional sampling, thus keeping depth
                        variations of the pileup. (default: False)
  -S SEED, --seed SEED  Random seed for proportional downsampling of reads.
                        (default: None)

```

