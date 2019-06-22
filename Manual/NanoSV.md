## [NanoSV](https://github.com/mroosmalen/nanosv)

### NanoSV parameters

```
$ NanoSV -h 
usage: NanoSV [-h] [-t THREADS] [-s SAMBAMBA] [-c CONFIG] [-b BED] [-o OUTPUT]
              [-f SNP_FILE] [-v]
              bam

Put here a description.

positional arguments:
  bam                   /path/to/file.bam

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        Number of threads [default: 4]
  -s SAMBAMBA, --sambamba SAMBAMBA
                        Give the full path to the sambamba or samtools
                        executable [default: sambamba ]
  -c CONFIG, --config CONFIG
                        Give the full path to your own ini file [ default:
                        config.ini ]
  -b BED, --bed BED     Give the full path to your own bed file, used for
                        coverage depth calculations [default: human_hg19.bed ]
  -o OUTPUT, --output OUTPUT
                        Give the full path to the output vcf file [default:
                        <stdout> ]
  -f SNP_FILE, --snp_file SNP_FILE
                        Give full path to the SNP variant file for phasing.
                        Supporting file formats: BED and VCF
  -v, --version         show program's version number and exit

```


### config file
```
#Reads segments options
[Filter options]
# Maximum number of segments per read resulting from the mapping of the read to the reference sequence
max_split = 10
# Minimum percentage of identical bases of the mapped segment relative to the reference sequence
min_pid = 0.7
# Minimum mapping quality of the segment
min_mapq = 20

#Parameters for tuning detection and clustering of breakpoints:
[Detection options]
# Maximum distance between two adjacent break-end positions
cluster_distance = 10
# Minimum number of breakpoint-junctions (i.e. split-read junctions) for clustering
cluster_count = 2
# Minimum flanking length, to consider a read a reference read
refreads_distance = 100
# Minimum length of unmapped sequence for hanging reads that overlap a break-end
hanging_length = 20
# Maximum distance to search for the MATEID, i.e. a reciprocal breakpoint-junction, for example an inversion consist of two breakpoint-junctions (3’-to-3’ and 5’-to-5’)
mate_distance = 300
# If True, NanoSV will check the depth of coverage for possible breakpoint-junctions with orientations that indicate a possible deletion or duplication (3’-to-5’ and 5’-to-3’)
depth_support = False
# Minimum indel size to call gap and create subsegments
min_indel_size = 30

#Parameters for setting the FILTER flag in the vcf output:
[Output filter options]
# Filter flag: LowQual, if the QUAL score is lower
qual_flag = 20
# Filter flag: SVcluster, if there are more SVs within a window size, they will be marked as SVcluster
window_size = 1000
# Filter flag: SVcluster, indicating the number of SVs within a certain window size (set by window_size above)
svcluster = 2
# Filter flag: MapQual, if the median mapq is lower than specified by this parameter
mapq_flag = 80
# Filter flag: PID, if the median percentage identity is lower than specified by this parameter
pid_flag = 0.80
# Filter flag: Gap, if the median GAP is higher than specified by this parameter
gap_flag = 100
# Filter flag: CIPOS|CIEND, if the CIPOS|CIEND bigger than specified by this parameter
ci_flag = 30
```



Note:

* should change the parameter **min_indel_size** to 50, and make sure the SV length is larger than 50 bp




### [nanosv parameters](https://github.com/mroosmalen/nanosv/issues/29)

```
$ NanoSV --help
usage: NanoSV [-h] [-t THREADS] [-s SAMBAMBA] [-c CONFIG] [-b BED] [-o OUTPUT]
              [-f SNP_FILE] [-v]
              bam

Put here a description.

positional arguments:
  bam                   /path/to/file.bam

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        Number of threads [default: 4]
  -s SAMBAMBA, --sambamba SAMBAMBA
                        Give the full path to the sambamba or samtools
                        executable [default: sambamba ]
  -c CONFIG, --config CONFIG
                        Give the full path to your own ini file [ default:
                        config.ini ]
  -b BED, --bed BED     Give the full path to your own bed file, used for
                        coverage depth calculations [default: human_hg19.bed ]
  -o OUTPUT, --output OUTPUT
                        Give the full path to the output vcf file [default:
                        <stdout> ]
  -f SNP_FILE, --snp_file SNP_FILE
                        Give full path to the SNP variant file for phasing.
                        Supporting file formats: BED and VCF
  -v, --version         show program's version number and exit

```

### run  NanoSV

NanoSV need SM tag
```
time NanoSV --threads 4 -o /home/wuzhikun/Project/NanoBenchmark/SVCall/NanoSV/minialign/nano_test.vcf 
/home/wuzhikun/Project/NanoBenchmark/mapping/minialign/nano_test.bam >/home/wuzhikun/Project/NanoBenchmark/log/NanoSV_minialign_nan
o_test.log 2>&1


Fri Mar 22 08:22:43 2019 Busy with calculating the coverage distribution...
Fri Mar 22 08:22:58 2019 Busy with parsing bam file...
Traceback (most recent call last):
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/NanoSV", line 11, in <module>
    sys.exit(main())
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/nanosv/NanoSV.py", line 71, in main
    utils.parse_bam.parse_bam()
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/nanosv/utils/../utils/parse_bam.py", line 39, in parse_bam
    sample_name = header['RG'][0]['SM']
KeyError: 'SM'

```


```
$ NanoSV --threads 20 -o pacbio_test.vcf pacbio_test.bam
Mon Mar 18 10:56:24 2019 Busy with calculating the coverage distribution...
Mon Mar 18 10:57:37 2019 Busy with parsing bam file...
Mon Mar 18 10:59:22 2019 Busy with parsing read segments...
Mon Mar 18 10:59:23 2019 Busy with parsing breakpoints...
Mon Mar 18 10:59:23 2019 Busy with reference reads...
Mon Mar 18 10:59:24 2019 Busy with printing to vcf...

```

output file:
```
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  pacbio_test
1       180697  17      C       <INS>   59      MapQual SVTYPE=INS;SVMETHOD=NanoSV_v1.2.3;END=180698;CIPOS=0,0;CIEND=0,
0;SVLEN=52;RT=0;GAP=52;MAPQ=36,36;PID=5.237,11.617;PLENGTH=0.134,0.06;RLENGTH=6711;ALT_READ_IDS=m140612_020550_42156_c1
00652082550000001823118110071460_s1_p0/81103/285_10632,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/73
53/0_9456;REF_READ_IDS_1=m140612_020550_42156_c100652082550000001823118110071460_s1_p0/7353/0_9456,m140612_020550_42156
_c100652082550000001823118110071460_s1_p0/7353/0_9456,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/735
3/9501_19102,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/80701/3786_15726,m140612_020550_42156_c10065
2082550000001823118110071460_s1_p0/81103/285_10632,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/98049/
23833_27657,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/7353/0_9456,m140612_020550_42156_c10065208255
0000001823118110071460_s1_p0/132262/953_11346;REF_READ_IDS_2=m140612_020550_42156_c100652082550000001823118110071460_s1
_p0/7353/0_9456,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/7353/0_9456,m140612_020550_42156_c1006520
82550000001823118110071460_s1_p0/7353/9501_19102,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/80701/37
86_15726,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/81103/285_10632,m140612_020550_42156_c1006520825
50000001823118110071460_s1_p0/98049/23833_27657,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/7353/0_94
56,m140612_020550_42156_c100652082550000001823118110071460_s1_p0/132262/953_11346    GT:DR:DV:GQ:HR:PL       0/1:8,8:2,
2:59:0,0:59,0,101
```


