## [rMETL](https://github.com/tjiangHIT/rMETL)


### install rMETL

```
conda install -c bioconda rmetl
```

### rMETL parameters

```
$ rMETL --help
usage: rMETL [-h] STAGE ...

           _  ___  _   _____   _______   _
     _ _  | ^_   _^ | |  ___| |__   __| | |
    | ^_| | | | | | | | |__      | |    | |
    | |   | | | | | | |  __|     | |    | |
    | |   | | | | | | | |___     | |    | |___
    |_|   |_| |_| |_| |_____|    |_|    |_____|

    rMETL - realignment-based Mobile Element insertion detection Tool for Long read

  STAGE is one of
    detection    Inference of putative MEI loci.
    realignment  Realignment of chimeric read parts.
    calling      Mobile Element Insertion/Deletion calling.
    
  See README.md for documentation or --help for details
  Strongly recommend making output directory manually at first.
  
  rMETL V1.0.4
  Author: Jiang Tao
  Contact: tjiang@hit.edu.cn

positional arguments:
  STAGE       Stage to execute
  OPTIONS     Options to pass to the stage

optional arguments:
  -h, --help  show this help message and exit

```


### detecting
```
$ rMETL detection --help
usage: rMETL detection [-h] [-s MIN_SUPPORT] [-l MIN_LENGTH] [-d MIN_DISTANCE]
                       [-t THREADS] [-x PRESETS]
                       [SAM,BAM,FASTA,FASTQ] REFERENCE temp_dir output_dir

           _  ___  _   _____   _______   _
     _ _  | ^_   _^ | |  ___| |__   __| | |
    | ^_| | | | | | | | |__      | |    | |
    | |   | | | | | | |  __|     | |    | |
    | |   | | | | | | | |___     | |    | |___
    |_|   |_| |_| |_| |_____|    |_|    |_____|

    rMETL - realignment-based Mobile Element insertion detection Tool for Long read

	Support reads aligned with Ngmlr and sorted with Samtools

	If input is a fastq or fasta format file, rMETL generates
	alignments with Ngmlr at first;

	If input is a sam format file, rMETL converts and sorts it
	to be a bam format file;

	If your input is a bam format file with index, rMETL extracts
	the ME signatures and collects the sub-sequence of them.

	The output is a fasta format file called 'potential.fa' 
	contains potentials non-reference ME clusters.

	rMETL V1.0.4
	Author: Jiang Tao
	Contact: tjiang@hit.edu.cn

positional arguments:
  [SAM,BAM,FASTA,FASTQ]
                        Input reads with/without alignment.
  REFERENCE             The reference genome in fasta format.
  temp_dir              Temporary directory to use for distributed jobs.
  output_dir            Directory to output potential ME loci.

optional arguments:
  -h, --help            show this help message and exit
  -s MIN_SUPPORT, --min_support MIN_SUPPORT
                        Mininum number of reads that support a ME.[5]
  -l MIN_LENGTH, --min_length MIN_LENGTH
                        Mininum length of ME to be reported.[50]
  -d MIN_DISTANCE, --min_distance MIN_DISTANCE
                        Mininum distance of two ME signatures to be
                        intergrated.[20]
  -t THREADS, --threads THREADS
                        Number of threads to use.[8]
  -x PRESETS, --presets PRESETS
                        The sequencing platform <pacbio,ont> of the
                        reads.[pacbio]

```


### run rMETL

### rMETL detection
```
(longshot) wuzhikun@fat02 11:39:00 ^_^ /home/wuzhikun/Project/NanoTrio/mapping/minimap2 
$ rMETL detection --min_support 3 --min_length 50 --threads 20 --presets ont M671-1.bam /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa M671-1_temp M671-1_out
2019-10-19 11:40:38,464 [INFO] Running /home/wuzhikun/anaconda3/envs/longshot/bin/rMETL detection --min_support 3 --min_length 50 --threads 20 --presets ont M671-1.bam /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa M671-1_temp M671-1_out
2019-10-19 11:40:38,464 [INFO] The bam file is legal.
2019-10-19 11:40:38,526 [INFO] Loading reference genome...
2019-10-19 11:41:37,570 [INFO] The total number of chromsomes: 194
2019-10-19 11:41:37,886 [INFO] Resolving chromsome 5.
2019-10-19 11:41:37,886 [INFO] Resolving chromsome 15.
2019-10-19 11:41:37,886 [INFO] Resolving chromsome 16.
2019-10-19 11:41:37,886 [INFO] Resolving chromsome 4.
2019-10-19 11:41:37,886 [INFO] Resolving chromsome 1.
2019-10-19 11:41:37,886 [INFO] Resolving chromsome 8.
2019-10-19 11:41:37,886 [INFO] Resolving chromsome 2.
2019-10-19 11:41:37,887 [INFO] Resolving chromsome 3.
2019-10-19 11:41:37,889 [INFO] Resolving chromsome 14.
2019-10-19 11:41:37,890 [INFO] Resolving chromsome 13.
2019-10-19 11:41:37,890 [INFO] Resolving chromsome 18.
2019-10-19 11:41:37,893 [INFO] Resolving chromsome 10.
2019-10-19 11:41:37,894 [INFO] Resolving chromsome 11.
2019-10-19 11:41:37,896 [INFO] Resolving chromsome 17.
2019-10-19 11:41:37,897 [INFO] Resolving chromsome 12.
2019-10-19 11:41:37,897 [INFO] Resolving chromsome 9.
2019-10-19 11:41:37,901 [INFO] Resolving chromsome 22.
2019-10-19 11:41:37,901 [INFO] Resolving chromsome X.
2019-10-19 11:41:37,901 [INFO] Resolving chromsome 7.
2019-10-19 11:41:37,901 [INFO] Resolving chromsome 6.
2019-10-19 11:42:53,332 [INFO] 1064 MEI/MED signal loci in the chromsome 22.
2019-10-19 11:43:24,114 [INFO] 1010 MEI/MED signal loci in the chromsome X.

2019-10-19 11:54:48,884 [INFO] Cleaning temporary files.
2019-10-19 11:54:49,378 [INFO] Finished in 850.91 seconds.

```

output file:

```
$ tree M671-1_out
M671-1_out
└── potential_ME.fa
```



### realignment
```
$ rMETL realignment --help
usage: rMETL realignment [-h] [-t THREADS] [-x PRESETS]
                         [--subread_length SUBREAD_LENGTH]
                         [--subread_corridor SUBREAD_CORRIDOR]
                         FASTA ME_Ref output

           _  ___  _   _____   _______   _
     _ _  | ^_   _^ | |  ___| |__   __| | |
    | ^_| | | | | | | | |__      | |    | |
    | |   | | | | | | |  __|     | |    | |
    | |   | | | | | | | |___     | |    | |___
    |_|   |_| |_| |_| |_____|    |_|    |_____|

    rMETL - realignment-based Mobile Element insertion detection Tool for Long read

	Realignment of chimeric read parts.

	Aligner: NGMLR version 0.2.6
	TE refs: Alu concensus
		 L1 concensus
		 SVA concensus
	The output is a sam format file called 'cluster.sam'.

	rMETL V1.0.4
	Author: Jiang Tao
	Contact: tjiang@hit.edu.cn

positional arguments:
  FASTA                 Input potential_ME.fa on STAGE detection.
  ME_Ref                The transposable element concensus in fasta format.
  output                Directory to output realignments.

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        Number of threads to use.[8]
  -x PRESETS, --presets PRESETS
                        The sequencing platform <pacbio,ont> of the
                        reads.[pacbio]
  --subread_length SUBREAD_LENGTH
                        Length of fragments reads are split into [128]
  --subread_corridor SUBREAD_CORRIDOR
                        Length of corridor sub-reads are aligned with [20]

```



### rMETL
```
$ rMETL realignment --threads 20 --presets ont --subread_length 128 --subread_corridor 20  M671-1_out/potential_ME.fa  /home/wuzhikun/software/rMETL/Concensus/super_TE.fa M671-1_out/M671-12019-10-19 12:42:33,836 [INFO] Running /home/wuzhikun/anaconda3/envs/longshot/bin/rMETL realignment --threads 20 --presets ont --subread_length 128 --subread_corridor 20 M671-1_out/potential_ME.fa /home/wuzhikun/software/rMETL/Concensus/super_TE.fa M671-1_out/M671-1
2019-10-19 12:42:33,836 [INFO] Running NGMLR...
2019-10-19 12:43:32,136 [INFO] Finished NGMLR mapping.
2019-10-19 12:43:32,138 [INFO] Finished in 58.30 seconds.
```

output file:
```
M671-1_out/M671-1cluster.sam
```


### calling

```
$ rMETL calling --help
usage: rMETL calling [-h] [-hom HOMOZYGOUS] [-het HETEROZYGOUS] [-q MIN_MAPQ]
                     [-c CLIPPING_THRESHOLD] [--sample SAMPLE] [--MEI MEI]
                     SAM REFERENCE [BED,VCF] output

           _  ___  _   _____   _______   _
     _ _  | ^_   _^ | |  ___| |__   __| | |
    | ^_| | | | | | | | |__      | |    | |
    | |   | | | | | | |  __|     | |    | |
    | |   | | | | | | | |___     | |    | |___
    |_|   |_| |_| |_| |_____|    |_|    |_____|

    rMETL - realignment-based Mobile Element insertion detection Tool for Long read

	Generate final MEI/MED callset in bed or vcf file.
	
	The output file called 'calling.bed' or 'calling.vcf'
	stores in output directory.
	
	rMETL V1.0.4
	Author: Jiang Tao
	Contact: tjiang@hit.edu.cn

positional arguments:
  SAM                   Input cluster.sam on STAGE realignment.
  REFERENCE             The reference genome in fasta format.
  [BED,VCF]             The format of the output file. [bed]
  output                Directory to output final callset.

optional arguments:
  -h, --help            show this help message and exit
  -hom HOMOZYGOUS, --homozygous HOMOZYGOUS
                        The mininum score of a genotyping reported as a
                        homozygous.[0.8]
  -het HETEROZYGOUS, --heterozygous HETEROZYGOUS
                        The mininum score of a genotyping reported as a
                        heterozygous.[0.3]
  -q MIN_MAPQ, --min_mapq MIN_MAPQ
                        Mininum mapping quality.[20]
  -c CLIPPING_THRESHOLD, --clipping_threshold CLIPPING_THRESHOLD
                        Mininum threshold of realignment clipping.[0.5]
  --sample SAMPLE       Sample description
  --MEI MEI             Enables rMETL to display MEI/MED only.[True]

```




#### run calling

```
$ rMETL calling  --sample M671-1 --MEI False  M671-1_out/M671-1cluster.sam  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  vcf   M671-1_out_MET
2019-10-19 14:02:50,200 [INFO] Running /home/wuzhikun/anaconda3/envs/longshot/bin/rMETL calling --sample M671-1 --MEI False M671-1_out/M671-1cluster.sam /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa vcf M671-1_out_MET
2019-10-19 14:02:50,200 [INFO] Loading reference genome...
2019-10-19 14:03:39,635 [INFO] Loading ME realignmets...
2019-10-19 14:03:50,764 [INFO] Writing results into disk...
2019-10-19 14:03:51,303 [INFO] Finished in 61.10 seconds.

```

output file:
```
M671-1_out_METcalling.vcf
```

```
1       10204   0       T       <INS>   .       PASS    IMPRECISE;SVTYPE=INS;SVLEN=1710;END=11913;SAMPLE=M671-1;STRAND=+-       GT:DV:DR        1/0:4:54
1       10317   1       A       <INS>   .       PASS    IMPRECISE;SVTYPE=INS;SVLEN=596;END=10912;SAMPLE=M671-1;STRAND=+-        GT:DV:DR        1/0:4:54
1       90130   2       A       <INS>   .       PASS    IMPRECISE;SVTYPE=INS;SVLEN=92;END=90221;SAMPLE=M671-1;STRAND=+- GT:DV:DR        1/0:5:34
1       90255   3       C       <INS>   .       PASS    IMPRECISE;SVTYPE=INS;SVLEN=80;END=90334;SAMPLE=M671-1;STRAND=+- GT:DV:DR        1/0:5:34
1       90323   4       T       <INS>   .       PASS    IMPRECISE;SVTYPE=INS;SVLEN=63;END=90385;SAMPLE=M671-1;STRAND=+- GT:DV:DR        1/0:9:31
1       90382   5       T       <INS>   .       PASS    IMPRECISE;SVTYPE=INS;SVLEN=115;END=90496;SAMPLE=M671-1;STRAND=+-        GT:DV:DR        1/0:3:37

```


