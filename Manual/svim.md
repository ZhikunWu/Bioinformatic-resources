## [SVIM](https://github.com/facebookresearch/visdom)

### SVIM parameters
```
$ svim alignment  --help
usage: svim alignment [-h] [--min_mapq MIN_MAPQ] [--min_sv_size MIN_SV_SIZE]
                      [--max_sv_size MAX_SV_SIZE] [--skip_indel]
                      [--skip_segment]
                      [--segment_gap_tolerance SEGMENT_GAP_TOLERANCE]
                      [--segment_overlap_tolerance SEGMENT_OVERLAP_TOLERANCE]
                      [--partition_max_distance PARTITION_MAX_DISTANCE]
                      [--distance_normalizer DISTANCE_NORMALIZER]
                      [--cluster_max_distance CLUSTER_MAX_DISTANCE]
                      [--del_ins_dup_max_distance DEL_INS_DUP_MAX_DISTANCE]
                      [--trans_destination_partition_max_distance TRANS_DESTINATION_PARTITION_MAX_DISTANCE]
                      [--trans_partition_max_distance TRANS_PARTITION_MAX_DISTANCE]
                      [--trans_sv_max_distance TRANS_SV_MAX_DISTANCE]
                      [--sample SAMPLE]
                      working_dir bam_file

positional arguments:
  working_dir           working directory
  bam_file              SAM/BAM file with aligned long reads (sorted,
                        preferentially on queryname with 'samtools sort -n')

optional arguments:
  -h, --help            show this help message and exit

COLLECT:
  --min_mapq MIN_MAPQ   Minimum mapping quality of reads to consider
  --min_sv_size MIN_SV_SIZE
                        Minimum SV size to detect
  --max_sv_size MAX_SV_SIZE
                        Maximum SV size to detect
  --skip_indel          disable signature collection from within read
                        alignments
  --skip_segment        disable signature collection from between read
                        alignments
  --segment_gap_tolerance SEGMENT_GAP_TOLERANCE
                        Maximum tolerated gap between adjacent alignment
                        segments
  --segment_overlap_tolerance SEGMENT_OVERLAP_TOLERANCE
                        Maximum tolerated overlap between adjacent alignment
                        segments

CLUSTER:
  --partition_max_distance PARTITION_MAX_DISTANCE
                        Maximum distance in bp between SVs in a partition
  --distance_normalizer DISTANCE_NORMALIZER
                        Distance normalizer used for span-position distance
  --cluster_max_distance CLUSTER_MAX_DISTANCE
                        Maximum span-position distance between SVs in a
                        cluster

COMBINE:
  --del_ins_dup_max_distance DEL_INS_DUP_MAX_DISTANCE
                        Maximum span-position distance between the origin of
                        an insertion and a deletion to be flagged as a
                        potential cut&paste insertion
  --trans_destination_partition_max_distance TRANS_DESTINATION_PARTITION_MAX_DISTANCE
                        Maximum distance in bp between translocation
                        breakpoint destinations in a partition
  --trans_partition_max_distance TRANS_PARTITION_MAX_DISTANCE
                        Maximum distance in bp between translocation
                        breakpoints in a partition
  --trans_sv_max_distance TRANS_SV_MAX_DISTANCE
                        Maximum distance in bp between a translocation
                        breakpoint and an SV signature to be combined
  --sample SAMPLE       Sample ID to include in output vcf (default: Sample)

```

### SV result of SVIM 
```
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  M625-0
1       46038   .       N       <DEL>   11      q30     SVTYPE=DEL;END=46478;SVLEN=-440;STD_SPAN=None;STD_POS=None      GT      ./.
1       52449   .       N       <DEL>   11      q30     SVTYPE=DEL;END=52503;SVLEN=-54;STD_SPAN=None;STD_POS=None       GT      ./.
1       59031   .       N       <DEL>   11      q30     SVTYPE=DEL;END=59468;SVLEN=-437;STD_SPAN=None;STD_POS=None      GT      ./.
1       59750   .       N       <DEL>   11      q30     SVTYPE=DEL;END=59807;SVLEN=-57;STD_SPAN=None;STD_POS=None       GT      ./.

```

```
$ grep -cv '^#' final_results.vcf
775988
```


some results
```
$ wc -l *bed
   693809 del.bed
     2024 dup_tan_dest.bed
     2024 dup_tan_source.bed
    87854 ins.bed
        0 ins_dup.bed
      154 inv.bed
     9192 trans.bed
   795057 total

```

```
$ grep -cv '^#' all.vcf 
783841

```

```
>>> 693809 + 2024 + 87854 + 154
783841
```





