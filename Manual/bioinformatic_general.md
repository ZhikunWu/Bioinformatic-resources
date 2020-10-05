### stats for fastx

```
$ seqstats Ashkenazim_son_pacbio_test.fasta.gz 
Total n:	132367
Total seq:	821421633 bp
Avg. seq:	6205.64 bp
Median seq:	5006.00 bp
N 50:		9864 bp
Min seq:	1 bp
Max seq:	56673 bp

```



### get sub reads randomly
```
$ seqtk sample -s100 combined_2018-05-18.fastq.gz 132367 > combined_2018-05-18_sub.fastq
```

### combine fastq .gz files
```
zcat combined_2018-05-18.fastq.gz combined_2018-08-10.fastq.gz | gzip > Ashkenazim_son.fastq.gz
```



### flag values
```
$ samtools view minimap_Ashkenazim_son_mapped.bam | cut -f 2 | uniq  | sort | uniq > flag.txt
$ less flag.txt

0
16    Read reverse strand
2048  Supplementary alignment
2064  Supplementary alignment & Read reverse strand
256   Not primary alignment
272   Not primary alignment & Read reverse strand

```

### get .bam  and .fastq file of given chromosome

```
sambamba view -t 10 M628-1.bqsr.bam 1 > M628-1.bqsr_chr1.bam

bedtools bamtofastq -i M625-0.bqsr_chr1.bam.bam -fq M625-0.R1.fastq -fq2 M625-0.R2.fastq
```



### get mapped reads with sam format:
```

$ samtools view -@ 20 -o minimap_Ashkenazim_son_mapped.bam  minimap_Ashkenazim_son_mapped.sam
$ samtools view --threads 20 -F 4 -b minimap_Ashkenazim_son.bam > minimap_Ashkenazim_son_mapped.bam
```


### extract multiple regions from bam
```
$ samtools view -@ 10 -b -L M625_denovo_SV_proband_test.bed /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M625-0.bam > M625_denovo_SV_proband_test.bam
```


### get fasta from genome based on bed file
```
$ head target_test.bed
1	143189266	143267809
1	240083084	247736007
```

```
$ bedtools getfasta -fi /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna_sm.chromosome.1.fa -bed target_test.bed > target_test_mask.fasta
```


### bam to fastq

#### picard:
```
java -jar /usr/local/tools/picard-tools-1.114/SamToFastq.jar \
VALIDATION_STRINGENCY=SILENT \
INPUT=HI.1965.007.Index_1.FL_K562-110k-A.bam \
FASTQ=HI.1965.007.Index_1.FL_K562-110k-A_R1.fastq \
SECOND_END_FASTQ=HI.1965.007.Index_1.FL_K562-110k-A_R2.fastq \
&> bamtofastq.sh.log
```


#### bam2fastx in Tophat:
```
bam2fastx -q -Q -A -o output.fastq input.bam
```


#### bamtools:
```
bamtools convert -in file1.bam -in file2.bam ... -format fastq >reads.fq
```

bedtools:
```
bedtools bamtofastq [OPTIONS] -i <BAM> -fq <FASTQ>
```

#### bam2fasx
```
conda install -c bioconda bam2fastx
```


```
$ bam2fastq --help
$ bam2fasta --help
Usage: bam2fasta [options] INPUT
Converts multiple BAM and/or DataSet files into into gzipped FASTA file(s).

Options:
  -h,--help          Output this help.
  --version          Output version info.
  -o,--output        Prefix of output filenames
  -c                 Gzip compression level [1-9] [1]
  -u                 Do not compress. In this case, we will not add .gz, and we ignore any -c setting.
  --split-barcodes   Split output into multiple FASTA files, by barcode pairs.
  -p,--seqid-prefix  Prefix for sequence IDs in headers

Arguments:
  input              Input file.

```



### filt genotype
```
vcffilter -f "QUAL > 20" NA12878.chr20.freebayes.vcf | vcfstats | grep "ts\|bial"
```


First, we should either use tabix to extract just chr20 from the NA12878-K.B.:
```
tabix -h NA12878.chr20.broad_truth_set.20131119.snps_and_indels.genotypes.vcf.gz 20
```



### sra to fastq
```
fastq-dump --split-3 --gzip --outdir ./  SRR645759.sra
```

```
pfastq-dump --threads 30 --split-3 --gzip --outdir ./ SRR123456.sra 
```



### merge fastq file

```
zcat SRR645761.R1.fastq.gz SRR645762.R1.fastq.gz | gzip > SRR62.R1.fastq.gz
```


### call MD tag
```
samtools calmd -@ num_threads -b alignment.bam reference.fasta  > alignment.md.bam 
samtools index alignment.md.bam

```



### bcf filting vcf files
```
bcftools view -O b  probands_denovo_common.vcf  > probands_denovo_common.bcf
```


F](https://www.biostars.org/p/141156/)

if you want to filter out indels and multiallelic, you would need something like this:
```
bcftools view --max-alleles 2 --exclude-types indels input.vcf.gz
```


A typical command to filter out anything but biallelic SNPs:
```
bcftools view -m2 -M2 -v snps input.vcf.gz
```
### sub sample of fastq sequence
```
$ seqtk sample -s100 FAB39088.fastq 10000  > FAB39088_sub.fastq
```

```
$ seqtk sample -s100 read1.fq 0.1 > sub1.fq
```

### Extract sub fasta sequence
```
$ samtools faidx Homo_sapiens.GRCh38.dna.primary_assembly.fa

$ samtools faidx Homo_sapiens.GRCh38.dna.primary_assembly.fa 1 > Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa
```


### intersection of regions using bedtools
```
intersectBed -a cnvs.bed -b refseq_exons.bed -wb
```



### Extract Sub-Set Of Regions From Vcf File
#### using tabix
```
bgzip your.vcf
tabix -p vcf your.vcf
tabix your.vcf.gz chr1:10,000,000-20,000,000
```
or 
```
tabix -R region.txt my.vcf.gz
```

#### using vcftools
```
vcftools --vcf input.vcf --bed bed_file_describing_the_range.bed --out output_prefix --recode --keep-INFO-all
```

#### using GATK
```
#Select a sample and restrict the output vcf to a set of intervals:     
java -Xmx2g -jar GenomeAnalysisTK.jar \
       -R ref.fasta \
       -T SelectVariants \
       --variant input.vcf \
       -o output.vcf \
       -L /path/to/my.interval_list \
       -sn SAMPLE_1_ACTG
```

#### using bedtools intersect
```
intersectBed -a input.vcf -b /path/to/my.interval.bed -header > output.vcf
```


