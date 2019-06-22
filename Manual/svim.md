## SVIM

### install SVIM
```
conda install -c bioconda svim
```


### svim parameters
```
$ svim
Please choose one of the two modes ('reads' or 'alignment'). See --help for more information.
```

```
$ svim alignment --help
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

### manuals

```
$ svim alignment  svim nanopore_test.bam

2019-03-19 15:28:35,341 [INFO   ]  ****************** Start SVIM, version 0.4.4 ******************
2019-03-19 15:28:35,341 [INFO   ]  CMD: python3 /home/wuzhikun/anaconda3/envs/NanoSV/bin/svim alignment svim nanopore_test_querysorted.bam
2019-03-19 15:28:35,341 [INFO   ]  WORKING DIR: /home/wuzhikun/Project/Nano_Pac_compare/mapping/Nanopore/svim
2019-03-19 15:28:35,342 [INFO   ]  PARAMETER: sub, VALUE: alignment
2019-03-19 15:28:35,342 [INFO   ]  PARAMETER: working_dir, VALUE: /home/wuzhikun/Project/Nano_Pac_compare/mapping/Nanopore/svim
2019-03-19 15:28:35,342 [INFO   ]  PARAMETER: bam_file, VALUE: nanopore_test_querysorted.bam
2019-03-19 15:28:35,342 [INFO   ]  PARAMETER: min_mapq, VALUE: 20
2019-03-19 15:28:35,342 [INFO   ]  PARAMETER: min_sv_size, VALUE: 40
2019-03-19 15:28:35,342 [INFO   ]  PARAMETER: max_sv_size, VALUE: 100000
2019-03-19 15:28:35,343 [INFO   ]  PARAMETER: skip_indel, VALUE: False
2019-03-19 15:28:35,343 [INFO   ]  PARAMETER: skip_segment, VALUE: False
2019-03-19 15:28:35,343 [INFO   ]  PARAMETER: segment_gap_tolerance, VALUE: 10
2019-03-19 15:28:35,343 [INFO   ]  PARAMETER: segment_overlap_tolerance, VALUE: 5
2019-03-19 15:28:35,343 [INFO   ]  PARAMETER: partition_max_distance, VALUE: 5000
2019-03-19 15:28:35,343 [INFO   ]  PARAMETER: distance_normalizer, VALUE: 900
2019-03-19 15:28:35,344 [INFO   ]  PARAMETER: cluster_max_distance, VALUE: 0.7
2019-03-19 15:28:35,344 [INFO   ]  PARAMETER: del_ins_dup_max_distance, VALUE: 1.0
2019-03-19 15:28:35,344 [INFO   ]  PARAMETER: trans_destination_partition_max_distance, VALUE: 1000
2019-03-19 15:28:35,344 [INFO   ]  PARAMETER: trans_partition_max_distance, VALUE: 200
2019-03-19 15:28:35,344 [INFO   ]  PARAMETER: trans_sv_max_distance, VALUE: 500
2019-03-19 15:28:35,344 [INFO   ]  PARAMETER: sample, VALUE: Sample
2019-03-19 15:28:35,344 [INFO   ]  ****************** STEP 1: COLLECT ******************
2019-03-19 15:28:35,345 [INFO   ]  MODE: alignment
2019-03-19 15:28:35,345 [INFO   ]  INPUT: /home/wuzhikun/Project/Nano_Pac_compare/mapping/Nanopore/nanopore_test_querysorted.bam
2019-03-19 15:28:35,349 [WARNING]  Input BAM file is coordinate-sorted. SVIM can process it but will be less accurate than for queryname-sorted input. It is highly recommended to sort the BAM file by queryname using samtools sort -n.
```


```
$ samtools sort -n -@ 20  -o nanopore_test_querysorted.bam nanopore_test.bam
```


```

$ svim alignment  svim nanopore_test_querysorted.bam
2019-03-19 15:33:09,074 [INFO   ]  ****************** Start SVIM, version 0.4.4 ******************
2019-03-19 15:33:09,075 [INFO   ]  CMD: python3 /home/wuzhikun/anaconda3/envs/NanoSV/bin/svim alignment svim nanopore_test_querysorted.bam
2019-03-19 15:33:09,075 [INFO   ]  WORKING DIR: /home/wuzhikun/Project/Nano_Pac_compare/mapping/Nanopore/svim
2019-03-19 15:33:09,075 [INFO   ]  PARAMETER: sub, VALUE: alignment
2019-03-19 15:33:09,076 [INFO   ]  PARAMETER: working_dir, VALUE: /home/wuzhikun/Project/Nano_Pac_compare/mapping/Nanopore/svim
2019-03-19 15:33:09,076 [INFO   ]  PARAMETER: bam_file, VALUE: nanopore_test_querysorted.bam
2019-03-19 15:33:09,076 [INFO   ]  PARAMETER: min_mapq, VALUE: 20
2019-03-19 15:33:09,076 [INFO   ]  PARAMETER: min_sv_size, VALUE: 40
2019-03-19 15:33:09,076 [INFO   ]  PARAMETER: max_sv_size, VALUE: 100000
2019-03-19 15:33:09,077 [INFO   ]  PARAMETER: skip_indel, VALUE: False
2019-03-19 15:33:09,077 [INFO   ]  PARAMETER: skip_segment, VALUE: False
2019-03-19 15:33:09,077 [INFO   ]  PARAMETER: segment_gap_tolerance, VALUE: 10
2019-03-19 15:33:09,078 [INFO   ]  PARAMETER: segment_overlap_tolerance, VALUE: 5
2019-03-19 15:33:09,078 [INFO   ]  PARAMETER: partition_max_distance, VALUE: 5000
2019-03-19 15:33:09,078 [INFO   ]  PARAMETER: distance_normalizer, VALUE: 900
2019-03-19 15:33:09,078 [INFO   ]  PARAMETER: cluster_max_distance, VALUE: 0.7
2019-03-19 15:33:09,079 [INFO   ]  PARAMETER: del_ins_dup_max_distance, VALUE: 1.0
2019-03-19 15:33:09,079 [INFO   ]  PARAMETER: trans_destination_partition_max_distance, VALUE: 1000
2019-03-19 15:33:09,079 [INFO   ]  PARAMETER: trans_partition_max_distance, VALUE: 200
2019-03-19 15:33:09,079 [INFO   ]  PARAMETER: trans_sv_max_distance, VALUE: 500
2019-03-19 15:33:09,080 [INFO   ]  PARAMETER: sample, VALUE: Sample
2019-03-19 15:33:09,080 [INFO   ]  ****************** STEP 1: COLLECT ******************
2019-03-19 15:33:09,080 [INFO   ]  MODE: alignment
2019-03-19 15:33:09,080 [INFO   ]  INPUT: /home/wuzhikun/Project/Nano_Pac_compare/mapping/Nanopore/nanopore_test_querysorted.bam
2019-03-19 15:33:21,305 [INFO   ]  Found 5223 signatures for deleted regions.
2019-03-19 15:33:21,305 [INFO   ]  Found 2097 signatures for inserted regions.
2019-03-19 15:33:21,306 [INFO   ]  Found 0 signatures for inverted regions.
2019-03-19 15:33:21,306 [INFO   ]  Found 16 signatures for tandem duplicated regions.
2019-03-19 15:33:21,306 [INFO   ]  Found 122 signatures for translocation breakpoints.
2019-03-19 15:33:21,306 [INFO   ]  Found 0 signatures for inserted regions with detected region of origin.
2019-03-19 15:33:21,306 [INFO   ]  ****************** STEP 2: CLUSTER ******************
2019-03-19 15:33:21,557 [INFO   ]  Clustered deleted regions: 2705 partitions and 4301 clusters
2019-03-19 15:33:22,100 [INFO   ]  Clustered inserted regions: 514 partitions and 1301 clusters
2019-03-19 15:33:22,311 [INFO   ]  Clustered inverted regions: 0 partitions and 0 clusters
2019-03-19 15:33:22,312 [INFO   ]  Clustered tandem duplicated regions: 8 partitions and 10 clusters
2019-03-19 15:33:22,313 [INFO   ]  Clustered inserted regions with detected region of origin: 0 partitions and 0 clusters
2019-03-19 15:33:22,314 [INFO   ]  Finished clustering. Writing signature clusters..
/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/matplotlib/ticker.py:2207: UserWarning: Data has no positive values, and therefore cannot be log-scaled.
  "Data has no positive values, and therefore cannot be "
2019-03-19 15:33:24,332 [INFO   ]  ****************** STEP 3: COMBINE ******************
2019-03-19 15:33:24,332 [INFO   ]  Cluster translocation breakpoints..
2019-03-19 15:33:24,334 [INFO   ]  Combine inserted regions with translocation breakpoints..
2019-03-19 15:33:24,337 [INFO   ]  Create interspersed duplication candidates and flag cut&paste insertions..
2019-03-19 15:33:24,349 [INFO   ]  Cluster interspersed duplication candidates one more time..
2019-03-19 15:33:24,349 [INFO   ]  Clustered interspersed duplication candidates: 0 partitions and 0 clusters
2019-03-19 15:33:24,350 [INFO   ]  Write SV candidates..
2019-03-19 15:33:24,350 [INFO   ]  Final deletion candidates: 4301
2019-03-19 15:33:24,350 [INFO   ]  Final inversion candidates: 0
2019-03-19 15:33:24,350 [INFO   ]  Final interspersed duplication candidates: 0
2019-03-19 15:33:24,350 [INFO   ]  Final tandem duplication candidates: 10
2019-03-19 15:33:24,351 [INFO   ]  Final novel insertion candidates: 1284

```


output files:
```
$ tree svim/
svim/
├── candidates
│   ├── candidates_deletions.bed
│   ├── candidates_int_duplications_dest.bed
│   ├── candidates_int_duplications_source.bed
│   ├── candidates_inversions.bed
│   ├── candidates_novel_insertions.bed
│   ├── candidates_tan_duplications_dest.bed
│   └── candidates_tan_duplications_source.bed
├── final_results.vcf
├── signatures
│   ├── all.vcf
│   ├── del.bed
│   ├── dup_tan_dest.bed
│   ├── dup_tan_source.bed
│   ├── ins.bed
│   ├── ins_dup.bed
│   ├── inv.bed
│   ├── signature_cluster_histograms.pdf
│   └── trans.bed
└── SVIM_190319_153309.log
```



```
$ less svim/final_results.vcf

##fileformat=VCFv4.2
##source=SVIMV0.4.4
##contig=<ID=1,length=248956422>
##ALT=<ID=DEL,Description="Deletion">
##ALT=<ID=INV,Description="Inversion">
##ALT=<ID=DUP,Description="Duplication">
##ALT=<ID=DUP:TANDEM,Description="Tandem Duplication">
##ALT=<ID=DUP:INT,Description="Interspersed Duplication">
##ALT=<ID=INS,Description="Insertion">
##ALT=<ID=INS:NOVEL,Description="Novel Insertion">
##INFO=<ID=SVTYPE,Number=1,Type=String,Description="Type of structural variant">
##INFO=<ID=CUTPASTE,Number=0,Type=Flag,Description="Genomic origin of interspersed duplication seems to be deleted">
##INFO=<ID=END,Number=1,Type=Integer,Description="End position of the variant described in this record">
##INFO=<ID=SVLEN,Number=1,Type=Integer,Description="Difference in length between REF and ALT alleles">
##INFO=<ID=STD_SPAN,Number=1,Type=Float,Description="Standard deviation in span of merged SV signatures">
##INFO=<ID=STD_POS,Number=1,Type=Float,Description="Standard deviation in position of merged SV signatures">
##FILTER=<ID=q20,Description="Quality below 20">
##FILTER=<ID=q30,Description="Quality below 30">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  Sample
1       57165   .       N       <DEL>   11      q30     SVTYPE=DEL;END=57208;SVLEN=-43;STD_SPAN=None;STD_POS=None       GT      ./.
1       66370   .       N       <INS:NOVEL>     11      q30     SVTYPE=INS:NOVEL;END=66370;SVLEN=89;STD_SPAN=None;STD_POS=None  GT      ./.
1       80769   .       N       <DEL>   11      q30     SVTYPE=DEL;END=80847;SVLEN=-78;STD_SPAN=None;STD_POS=None       GT      ./.
1       88739   .       N       <INS:NOVEL>     11      q30     SVTYPE=INS:NOVEL;END=88739;SVLEN=70;STD_SPAN=None;STD_POS=None  GT      ./.
1       90361   .       N       <INS:NOVEL>     11      q30     SVTYPE=INS:NOVEL;END=90361;SVLEN=116;STD_SPAN=None;STD_POS=None GT      ./.
1       95077   .       N       <INS:NOVEL>     11      q30     SVTYPE=INS:NOVEL;END=95077;SVLEN=96;STD_SPAN=None;STD_POS=None  GT      ./.
1       111594  .       N       <DEL>   11      q30     SVTYPE=DEL;END=111675;SVLEN=-81;STD_SPAN=None;STD_POS=None      GT      ./.
1       116367  .       N       <DEL>   11      q30     SVTYPE=DEL;END=116435;SVLEN=-68;STD_SPAN=None;STD_POS=None      GT      ./.
1       117442  .       N       <DEL>   11      q30     SVTYPE=DEL;END=117519;SVLEN=-77;STD_SPAN=None;STD_POS=None      GT      ./.
1       121062  .       N       <INS:NOVEL>     11      q30     SVTYPE=INS:NOVEL;END=121062;SVLEN=105;STD_SPAN=None;STD_POS=None        GT      ./.
1       127714  .       N       <DEL>   11      q30     SVTYPE=DEL;END=129924;SVLEN=-2210;STD_SPAN=None;STD_POS=None    GT      ./.

```

```
$ svim alignment --min_sv_size 50 --sample nanopore   svim nanopore_test_querysorted.bam

```