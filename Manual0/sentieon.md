
## sentieon

### install sentieon
```bash
$ conda install -c bioconda sentieon
```

### run sentieon
```
Your GATK pipleline may run 10-30 times faster (depending on the genome) thanks to this commercial solution by Sentieon.
To use the software, please contact us at cbsu@cornell.edu. 
Once your access has been set up, prepare a bash script containing the following lines in the beginning:

#!/bin/bash
license=cbsulogin2.tc.cornell.edu:8990
export SENTIEON_LICENSE=$license
RELEASE=/programs/sentieon-genomics-201704.01
The rest of the script will contain calls to Sentieon's executables, e.g.,the following command will run Haplotyper (an equivalent of GATK's HaplotypeCaller) on alignments in BAM file alignments.bam and reference genome genome.fa, on 8 threads, with output (in.g.vcf format) written to file output-hc.g.vcf:
$RELEASE/bin/sentieon driver -r genome.fa  -t 8 -i alignments.bam --algo Haplotyper --emit_mode gvcf output-hc.g.vcf
Consult the program's manual (/programs/sentieon-genomics-201704/Sentieon_genomics_Manual_201704.pdf) for other options and syntax of other pipeline steps.
```


#### sentieon parameters
```
$ sentieon
Thank you for using Sentieon software. sentieon supported commands are driver,util,plot
```

driver
```
$ /home/wzk/anaconda3/envs/evolution/bin/sentieon driver
Usage: /home/wzk/anaconda3/envs/evolution/share/sentieon-201704.03-0/libexec/driver [options] --algo <algo_name> [algo_options]

Options:
  -r, --reference       Reference file (FASTA)
  -i, --input           Read sequence input file (BAM/CRAM)
  -q, --qual_cal        Base quality calibration table
  -t, --thread_count    Number of threads
      --interval        Interval string or file (BED/Picard)
      --interval_padding
                        Amount to pad all intervals
      --skip_no_coor    Skip unmapped reads
      --temp_dir        Directory for temporary files
      --cram_read_options
                        CRAM read options
      --version         Display version string
  -h, --help            Display help information
      --read_filter     Read filter name and params
      --list_read_filter
                        List read filters

For algo specific help information, type
    /home/wzk/anaconda3/envs/evolution/share/sentieon-201704.03-0/libexec/driver --help --algo <algo_name>

Available algos:
  AlignmentStat
  ApplyVarCal
  CNV
  CollectVCMetrics
  ContaminationAssessment
  CoverageMetrics
  Dedup
  GCBias
  GVCFtyper
  Genotyper
  Haplotyper
  HsMetricAlgo
  InsertSizeMetricAlgo
  LocusCollector
  MeanQualityByCycle
  QualCal
  QualDistribution
  RNASplitReadsAtJunction
  ReadWriter
  Realigner
  TNhaplotyper
  TNscope
  TNsnv
  VarCal
```

util
```
$ sentieon util
Usage: /home/wzk/anaconda3/envs/evolution/share/sentieon-201704.03-0/libexec/util <command> [options]

Commands:
  util sort -o out.bam in1.bam 
  util stream -i in.bam -o out.bam -q recal.table
  util index bam1 [bam2 ...]
  util vcfindex in1.vcf[.gz] [in2.vcf[.gz]] ...
  util vcfconvert src.vcf[.gz] dst.vcf[.gz]

Common options:
  -r, --reference       Reference file (FASTA)
  -i, --input           Input file
  -t, --thread_count    Number of threads
  -o, --output          Output file
      --interval        Contig:start-end, 1-based
      --verbose         Verbose
      --skip_no_coor    Skip unmapped reads
      --bam_compression BAM compression: 0-9, 0-faster, 9-better (default: 6)
      --output_format   Output file format: BAM or CRAM (default: BAM)
      --cram_read_options
                        CRAM input options
      --cram_write_options
                        CRAM output options
      --temp_dir        Directory for temporary files
```

plot

```
$ sentieon plot
Syntax: create plot in pdf format
    /home/wzk/anaconda3/envs/evolution/share/sentieon-201704.03-0/libexec/plot.py bqsr -o output.pdf input.csv
    /home/wzk/anaconda3/envs/evolution/share/sentieon-201704.03-0/libexec/plot.py vqsr -o output.pdf plot_file [tranches_file=tranchesFile] [target_titv=2.15] [min_fp_rate=0.001] [point_size=0.5]'
    /home/wzk/anaconda3/envs/evolution/share/sentieon-201704.03-0/libexec/plot.py metrics -o output.pdf gc=gc.txt mq=mq.txt qd=qd.txt isize=insert_size.txt
```