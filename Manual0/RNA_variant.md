# Calling variants in RNAseq

The whole practice is based on the workflow: [Calling variants in RNAseq](https://software.broadinstitute.org/gatk/documentation/article.php?id=3891)

Some steps perform using mutiple tools


## The workflow for calling variants from RNA-seq
* Quality control for RNA sequence
* Build the index for reference genome
* Align sequence to reference genome
* Add or replace the group name for sample (especially for followed GATK)
* Mark duplicated sequences
* Make `.fai` and `.dict` file of reference (especially for followed GATK)
* Split 'N' or bad cigar for reads
* Realign the InDel region
* Call SNPs and InDels using GATK
* Filt SNPs and InDels 

### 1. Quality control for RNA sequence

```
java -jar Trimmomatic-0.36/trimmomatic-0.36.jar  PE -threads 20 -phred33  293TW1_control.R1.fq.gz 293TW1_control.R2.fq.gz 293TW1_control_clean.R1.fq.gz   293TW1_control_clean_unpaired.R1.fq.gz   293TW1_control_clean.R2.fq.gz  293TW1_control_clean_unpaired.R2.fq.gz ILLUMINACLIP:/home/Adapters/mRNA.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 HEADCROP:0 MINLEN:36
```

`/home/Adapters/mRNA.fa` is the file containing the adapter information of the sequences


### 2. Build the index for reference genome
#### 2.1. Build the index using `hisat2`

```
$ hisat2-build Fusarium_graminearum.RR1.fa Fusarium_graminearum.RR1
```

output files:
```
Fusarium_graminearum.1.ht2
Fusarium_graminearum.2.ht2
Fusarium_graminearum.3.ht2
Fusarium_graminearum.4.ht2
Fusarium_graminearum.5.ht2
Fusarium_graminearum.6.ht2
Fusarium_graminearum.7.ht2
Fusarium_graminearum.8.ht2
```


#### 2.2. Build the index using `STAR`

```
mkdir STAR_ref
STAR --runMode genomeGenerate --runThreadN 10 --genomeFastaFiles Fusarium_graminearum.RR1.fa --genomeDir STAR_ref  --sjdbGTFfile Fusarium_graminearum.RR1.36.gtf  --sjdbOverhang 149
```

* Firstly we should create the directory `STAR_ref` that need for the followed command
* It need the `.gtf` annotation file because the `STAR` need junction information of transcriptome  based on the feature `exon`
* Parameter `sjdbOverhang` is the numeric of read length minus 1. If read length is 150 (each end of PE reads), it should be 149

output files:
```
STAR_ref/
├── chrLength.txt
├── chrNameLength.txt
├── chrName.txt
├── chrStart.txt
├── exonGeTrInfo.tab
├── exonInfo.tab
├── geneInfo.tab
├── Genome
├── genomeParameters.txt
├── SA
├── SAindex
├── sjdbInfo.txt
├── sjdbList.fromGTF.out.tab
├── sjdbList.out.tab
└── transcriptInfo.tab
```


### 3. Align sequence to reference genome

#### 3.1. Align reads using `STAR`

```
STAR --runThreadN 20 --genomeDir  STAR_ref --readFilesIn T01.R1.fq.gz T01.R1.fq.gz --readFilesCommand gunzip -c --outSAMtype BAM SortedByCoordinate --outFileNamePrefix T01/  
```

* For best the output prefix should ends with '/' when conducting mutiple samples, then it is the prefix of the directory
* Parameter `--readFilesCommand gunzip -c ` is for the compressed `.gz` files
* The result just contain mapped reads, if you need extract unmapped reads you should add parameter `--outReadsUnmapped Fastx`

example of STAR alignment:
```
STAR --genomeDir mouse84.STARIndex/ \
--readFilesIn <sample_id>.fastq.gz \
--outFileNamePrefix <sample_id>/osample_id>.fastq.gz. \
--runThreadN 8 \
--limitBAMsortRAM 60000000000 \
--outSAMattrRGline ID:osample_id>.fastq.gz SM:osample_id>.fastq.gz \
--outBAMsortingThreadN 8 \
--outSAMtype BAM SortedByCoordinate \
--outSAMunmapped Within \
--outSAMstrandField intronMotif \
--readFilesCommand zcat \
--chimSegmentMin 20 \
--genomeLoad NoSharedMemory
```

#### 3.2. Align reads using `hisat2`
```
hisat2 -x Fusarium_graminearum.RR1  -p 10 -1 T01.R1.fq.gz -2 T01.R1.fq.gz  -S T01.sam
```

* Parameter `-p` is the number of threads used
* Parameter `-x` is the prefix of built index for hisat2


#### 3.3. Convert `.sam` to `.bam` (for hisat2)
```
samtools view -hbS T01.sam > T01.bam
```


### 4. Add or replace the group name for sample using [PICARD](https://broadinstitute.github.io/picard/command-line-overview.html)

```
java -jar picard-2.8.2.jar AddOrReplaceReadGroups I=T01.bam O=T01.sorted.bam SORT_ORDER=coordinate  RGID=T01  RGLB=1  RGPL=illumina RGPU=1  RGSM=T01
```

* RGID (String): Read Group ID Default value: 1. This option can be set to 'null' to clear the default value
* RGLB (String): Read Group library Required
* RGPL (String): Read Group platform (e.g. illumina, solid) Required
* RGSM (String): Read Group sample name Required

example:
```
java -jar picard.jar AddOrReplaceReadGroups \
      I=input.bam \
      O=output.bam \
      RGID=4 \
      RGLB=lib1 \
      RGPL=illumina \
      RGPU=unit1 \
      RGSM=20
```

### 5. Mark duplicated sequences
```
java -jar picard-2.8.2.jar MarkDuplicates I=T01.sorted.bam  O=T01.sorted_deduplicated.bam CREATE_INDEX=true VALIDATION_STRINGENCY=SILENT M=duplicate_metrics.txt
```

- Validation stringency for all SAM files read by this program. Setting stringency to SILENT can improve performance when processing a BAM file in which variable-length data (read, qualities, tags) do not otherwise need to be decoded. Default value: STRICT. This option can be set to 'null' to clear the default value. Possible values: {STRICT, LENIENT, SILENT}
- Whether to create a BAM index when writing a coordinate-sorted BAM file. Default value: false. This option can be set to 'null' to clear the default value. Possible values: {true, false}


### 6. Make `.fai` and `.dict` file of reference

#### 6.1. Build `fai` file using `samtools`
```
$ samtools faidx Fusarium_graminearum.RR1.fa
```
output file
```
$ head Fusarium_graminearum.RR1.fa.fai
1   11760891    52  60  61
2   8997558 11957009    60  61
3   7792947 21104578    60  61
4   9395062 29027459    60  61
Mt  95638   38579157    60  61
HG970330    5846    38676453    60  61
```

#### 6.2. Build `dict` file using `PICARD`

```
$ java -jar picard-2.8.2.jar CreateSequenceDictionary REFERENCE=Fusarium_graminearum.RR1.fa OUTPUT=Fusarium_graminearum.RR1.dict
```

output:
```
$ head Fusarium_graminearum.RR1.dict
@HD VN:1.5
@SQ SN:1    LN:11760891 M5:cc988f15b8c5ea82b1267cd4651ec8a4 UR:file:/home/wzk/database/GENOME/Fusarium_graminearum/Fusarium_graminearum.RR1.fa
@SQ SN:2    LN:8997558  M5:12e5b95e24f75fe4dcf5de14fcad513a UR:file:/home/wzk/database/GENOME/Fusarium_graminearum/Fusarium_graminearum.RR1.fa
@SQ SN:3    LN:7792947  M5:c7f2269dfd303d309beabb6b1cf6d7a7 UR:file:/home/wzk/database/GENOME/Fusarium_graminearum/Fusarium_graminearum.RR1.fa
@SQ SN:4    LN:9395062  M5:12139fcd3f1d1b06e4aed20f090982db UR:file:/home/wzk/database/GENOME/Fusarium_graminearum/Fusarium_graminearum.RR1.fa
@SQ SN:Mt   LN:95638    M5:c1f9428ce9004f4abab56c1752742085 UR:file:/home/wzk/database/GENOME/Fusarium_graminearum/Fusarium_graminearum.RR1.fa
@SQ SN:HG970330 LN:5846 M5:4f0aeea0dd96a9f497c44c2e380e7bc9 UR:file:/home/wzk/database/GENOME/Fusarium_graminearum/Fusarium_graminearum.RR1.fa
```

* Note: output should delete the suffix `.fa` for input, and then add the suffix `.dict`




### 7. Split 'N' or bad cigar for reads

using GATK version 3.7
```
java -jar GenomeAnalysisTK.jar -T SplitNCigarReads -R Fusarium_graminearum.RR1.fa  -I T01.sorted_deduplicated.bam -o T01.sorted_deduplicated_split.bam -rf ReassignOneMappingQuality -RMQF 255 -RMQT 60 -U ALLOW_N_CIGAR_READS
```


### 8. Realign the InDel region

#### 8.1. Get InDel region that need realignment

 The GATK people recommend a few quality control steps before you run the SNP calling. In particular, they recommend local re-alignment around indels, because reads whose ends map to the location of an indel can sometimes lead to false positive SNP calls. I’ll try to illustrate this with a simplified example. Suppose the reference sequence is GGGGTTTT and there’s an alternate allele with a 4-bp insertion of C’s: GGGGCCCCTTTT. Now if a read carries the entire insertion, the aligner can figure things out without a problem. However, if the end of the read overlaps the insertion, you could run into problems. For example:

```
Reference : GGGG----TTTT
Read 1    :    GCCCCT
Read 2    : GGGG----C
```

Read 1 looks fine, but read 2 is probably mis-aligned; rather than counting the C as an insertion, which is probably better, the aligner has placed it after the indel, making it look like there is a SNP there. In GATK we can account for this problem by doing local re-alignment around potential indel sites, in which we incorporate information about all the reads in that region simultaneously, rather than mapping each read individually. First, GATK needs to figure out which regions are in need of re-alignment:

```
$ java -Xmx10g -jar GenomeAnalysisTK.jar -T RealignerTargetCreator -R  Fusarium_graminearum.RR1.fa -I Input.sorted_group_dup_splitN.bam -L 1:1-135835  -o  unified_1_135835.realign.intervals
```

output files
```
$ head  unified_1_135835.realign.intervals
1:2518-2519
1:8152
1:9944
1:16132-16134
1:16853-16854
1:26019-26020
1:26762-26763
1:28047
1:31307-31310
1:39354

```

#### 8.2. Realign the file based on the InDel region
```
$ java -Xmx10g -jar GenomeAnalysisTK.jar  -T HaplotypeCaller -R Fusarium_graminearum.RR1.fa  -nct 5 -I 1_135835.realigned.bam    --genotyping_mode DISCOVERY -L 1:1-135835  -o 1_135835_realign.vcf
```




### 9. Call SNPs and InDels using GATK

#### 9.1. Call SNPs using GATK
```
java -Xmx50g -jar GenomeAnalysisTK.jar -T HaplotypeCaller -R Fusarium_graminearum.RR1.fa -nct 20 -I T01.sorted_deduplicated_split.bam -dontUseSoftClippedBases  --genotyping_mode DISCOVERY   -stand_call_conf 20  -o T01.vcf
```

##### [Use HaplotypeCaller!](https://gatkforums.broadinstitute.org/gatk/discussion/3151/should-i-use-unifiedgenotyper-or-haplotypecaller-to-call-variants-on-my-data)

The HaplotypeCaller is a more recent and sophisticated tool than the UnifiedGenotyper. Its ability to call SNPs is equivalent to that of the UnifiedGenotyper, its ability to call indels is far superior, and it is now capable of calling non-diploid samples. It also comprises several unique functionalities such as the reference confidence model (which enables efficient and incremental variant discovery on ridiculously large cohorts) and special settings for RNAseq data.

**As of GATK version 3.3, we recommend using HaplotypeCaller in all cases, with no exceptions.**


If you are limited to older versions for project continuity, you may opt to use UnifiedGenotyper in the following cases:

- If you are working with non-diploid organisms (UG can handle different levels of ploidy while older versions of HC cannot)
- If you are working with pooled samples (also due to the HC’s limitation regarding ploidy)
- If you want to analyze more than 100 samples at a time (for performance reasons) (versions 2.x)


##### Call SNP for the given region
```
java -Xmx20g -jar GenomeAnalysisTK.jar  -T HaplotypeCaller -R Triticum_aestivum.TGACv1.dna.toplevel.fa  -nct 20 -I T01.sorted.bam   --genotyping_mode DISCOVERY -L Pt:1-135835  -o T01_Pt.vcf
```



#### 9.2. Call SNPs using samtools
```
samtools mpileup -ugf Fusarium_graminearum.RR1.fa -t AD -t DP -t SP T01.sorted_deduplicated.bam |bcftools call -vmO z -o T01.sorted_deduplicated.vcf.gz
```


#### 9.3. Call SNPs using freebayes
```
freebayes -f Fusarium_graminearum.RR1.fa T01.sorted_deduplicated.bam > T01.sorted_deduplicated.vcf

```

freebayes产生的VCF文件中INFO一列有专门的一个tag来注释是snp、ins（插入）、del（缺失）、mnp（连续两个snp位点，如ref为AT， alt为CG）以及complex（composite insetion and substitution events）
所以只要用下面的shell命令即可提取SNP
```
grep 'TYPE=snp' freebayes_raw.vcf > freebayes_snp_raw.vcf
```



### 10. Filt variants

#### 10.1. filt using GATK
```
java -Xmx20g  -jar GenomeAnalysisTK.jar  -T VariantFiltration -R Fusarium_graminearum.RR1.fa  -V T01.vcf --filterExpression  "QD < 2.0 || FS > 60.0 || ReadPosRankSum < -8.0" --filterName "vcf_filter" -o T01_filt.vcf
```


[VariantFiltration usage example](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_gatk_tools_walkers_filters_VariantFiltration.php)

```
java -jar GenomeAnalysisTK.jar \
   -T VariantFiltration \
   -R reference.fasta \
   -o output.vcf \
   --variant input.vcf \
   --filterExpression "AB < 0.2 || MQ0 > 50" \
   --filterName "SomeFilterName"
```

#### 10.2. filt using bcftools
下面就简单的过滤QUAL小于10，DP值小于5，INDEL附近的位点
```
bcftools filter -O v -o bcftools_filter.vcf -s LOWQUAL -e 'QUAL<10 || FMT/DP <5' --SnpGap 5 --set-GTs . bcftools_raw.vcf.gz
```

提取过滤后的SNP位点
```
bcftools view -v snps bcftools_filter.vcf >bcftools_snp_filter.vcf
```

或者在vcf文件中INFO列里，如果是INDEL的话，会标注出INDEL，因此提取SNP也可以：
```
grep -v 'INDEL' bcftools_fiter.vcf >bcftools_snp_filter.vcf 
```

注意：

- &&与& 区别：两者都表示“与”运算，但是&&运算符第一个表达式不成立的话，后面的表达式不运算，直接返回。而&对所有表达式都得判断。
- || 与| 区别：两者都表示“或”运算，但是||运算符第一个表达式成立的话，后面的表达式不运算，直接返回。而|对所有表达式都得判断。

### 11. Combine variants from mutiple samples
```
java -Xmx20g -jar GenomeAnalysisTK.jar -T CombineVariants -R  Fusarium_graminearum.RR1.fa --variant T01_filt.vcf  --variant T02_filt.vcf -o T01_T02.vcf -genotypeMergeOptions UNIQUIFY
```

- parameter [genotypeMergeOptions](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_gatk_tools_walkers_variantutils_CombineVariants.php):

Determines how we should merge genotype records for samples shared across the ROD files
The --genotypemergeoption argument is an enumerated type (GenotypeMergeType), which can have one of the following values:

* UNIQUIFY
  Make all sample genotypes unique by file. Each sample shared across RODs gets named sample.ROD.
* PRIORITIZE
  Take genotypes in priority order (see the priority argument).
* UNSORTED
  Take the genotypes in any order.
* REQUIRE_UNIQUE
  Require that all samples/genotypes be unique between all inputs.












