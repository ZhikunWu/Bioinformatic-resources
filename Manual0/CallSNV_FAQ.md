
### How to efficiently remove a list of reads from BAM file?

```
samtools view -h sample1.bam | grep -vf read_ids_to_remove.txt | samtools view -bS -o sample1_filter.bam -​
```


### [FilterSamReads](https://broadinstitute.github.io/picard/command-line-overview.html#FilterSamReads)
```
java -jar picard.jar FilterSamReads \
       I=input.bam \ 
       O=output.bam \
       READ_LIST_FILE=read_names.txt      FILTER=filter_value
```



```
java -Xmx30g -jar /home/wzk/anaconda3/envs/evolution/bin/GenomeAnalysisTK.jar -T UnifiedGenotyper -R /home/wzk/database/GENOME/Brassica_rapa/chrs/Brapa_sequence_v1.5_chrs.fa -I /home/wzk/Project/C100/mapping/R4/R4_realigned.bam -o /home/wzk/Project/C100/VCF/R4.vcf -nct 8 -glm BOTH -mbq 20 --genotyping_mode DISCOVERY  --filter_mismatching_base_and_quals  -rf DuplicateRead -rf FailsVendorQualityCheck -rf NotPrimaryAlignment \ -rf BadMate -rf  MappingQualityUnavailable -rf UnmappedRead -rf BadCigar 
```


### Call SNV by freebayes

```
freebayes -f /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa -L bam_files.txt > MT___Ler.vcf
```

### [samtools mpileup](http://samtools.sourceforge.net/mpileup.shtml)

### Call SNV by samtools
```
 samtools mpileup -ugf /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa -t AD -t DP -t SP /home/wzk/Project/C075/mapping/MT/MT_realigned.bam /home/wzk/Project/C075/mapping/Ler/Ler_realigned.bam  | bcftools call -vmO z -o  MT___Ler_samtools.vcf
```


### GATK ploidy

Set the parameter **ploidy** to 1 if it is a virus genome 
```
$ java -Xmx30g -jar /home/wzk/anaconda3/envs/evolution/bin/GenomeAnalysisTK.jar -T UnifiedGenotyper -R /home/genome/Bacillus_virus/GCF_000837685.1_ViralProj14034_genomic.fa -I mapping/DR1/DR1_realigned.bam  -ploidy 1  -o /home/wzk/DR1.vcf 
```




### sam to bam
```
$ samtools view -b -F 4 T01_dedupped.bam > T01.mapped.bam
$ samtools index T01.mapped.bam


samtools view -bS out.sam >out.bam
-b 意思使输出使BAM format
-S 意思使输入使SAM，如果@SQ 缺失， 要写-t

samtools faidx ref.fa
samtools view -bt ref.fa.fai out.sam > out.bam
```

### get paired mapped reads
```
samtools view -hf 0x2 T01_dedupped.fixed.bam > T01_dedupped.fixed-2.bam
```


### samtools function
```
$ samtools view -bt hg19.fa.fai unsorted.sam -o unsorted.bam
note that the unsorted.sam has no header @SQ

then I tried this,
$ samtools view -hbt hg19.fa.fai unsorted.sam -o unsorted.bam
the -h can include the header in the output

but I failed to merge the header into unsorted.bam



Perhaps you could try this approach, although it doesn't resolve the reason why you are losing your header. 

1) Get the header from your sam file by doing (although you have this header already, I believe)

samtools view -HS <yourfile.sam> > <yourheader.sam>

2) Then reheader your bam file:

samtools reheader <yourheader.sam> <yourfile.bam>

where yourfile.bam is the bam file lacking the header

```

### bwa mapping
```
bwa index <ref.fa>

bwa mem -R '@RG\tID:foo\tSM:bar\tLB:library1' <ref.fa> <read1.fa> <read1.fa> > lane.sam

```
Typically your reads will be supplied to you in two files written in the FASTQ format. It is particularly important to ensure that the @RG information here is correct as this information is used by later tools. The SM field must be set to the name of the sample being processed, and LB field to the library. The resulting mapped reads will be delivered to you in a mapping format known as SAM.


Because BWA can sometimes leave unusual FLAG information on SAM records, it is helpful when working with many tools to first clean up read pairing information and flags:
```
samtools fixmate -O bam <lane.sam> <lane_fixmate.bam>
```

To sort them from name order into coordinate order:
```
samtools sort -O bam -o <lane_sorted.bam> -T </tmp/lane_temp> <lane_fixmate.sam>
```


### realign the indels and BQSR

In order to reduce the number of miscalls of INDELs in your data it is helpful to realign your raw gapped alignment with the Broad’s GATK Realigner.
```
java -Xmx2g -jar GenomeAnalysisTK.jar -T RealignerTargetCreator -R <ref.fa> -I <lane.bam> -o <lane.intervals> --known <bundle/b38/Mills1000G.b38.vcf>
java -Xmx4g -jar GenomeAnalysisTK.jar -T IndelRealigner -R <ref.fa> -I <lane.bam> -targetIntervals <lane.intervals> --known <bundle/b38/Mills1000G.b38.vcf> -o <lane_realigned.bam>
```

BQSR from the Broad’s GATK allows you to reduce the effects of analysis artefacts produced by your sequencing machines. It does this in two steps, the first analyses your data to detect covariates and the second compensates for those covariates by adjusting quality scores.
```
java -Xmx4g -jar GenomeAnalysisTK.jar -T BaseRecalibrator -R <ref.fa> -knownSites >bundle/b38/dbsnp_142.b38.vcf> -I <lane.bam> -o <lane_recal.table>
java -Xmx2g -jar GenomeAnalysisTK.jar -T PrintReads -R <ref.fa> -I <lane.bam> --BSQR <lane_recal.table> -o <lane_recal.bam>
```





It is helpful at this point to compile all of the reads from each library together into one BAM, which can be done at the same time as marking PCR and optical duplicates. To identify duplicates we currently recommend the use of either the `Picard` or `biobambam`’s mark duplicates tool.
```
java -Xmx2g -jar MarkDuplicates.jar VALIDATION_STRINGENCY=LENIENT INPUT=<lane_1.bam> INPUT=<lane_2.bam> INPUT=<lane_3.bam> OUTPUT=<library.bam>
```


Once this is done you can perform another merge step to produce your sample BAM files.
```
samtools merge <sample.bam> <library1.bam> <library2.bam> <library3.bam>
samtools index <sample.bam>
```

If you have the computational time and resources available it is helpful to realign your INDELS again:
```
java -Xmx2g -jar GenomeAnalysisTK.jar -T RealignerTargetCreator -R <ref.fa> -I <sample.bam> -o <sample.intervals> --known >bundle/b38/Mills1000G.b38.vcf>
java -Xmx4g -jar GenomeAnalysisTK.jar -T IndelRealigner -R <ref.fa> -I <sample.bam> -targetIntervals <sample.intervals> --known >bundle/b38/Mills1000G.b38.vcf> -o <sample_realigned.bam>
```

Lastly we index our BAM using samtools:
```
samtools index <sample_realigned.bam>
```

### Variant Calling
To convert your BAM file into genomic positions we first use mpileup to produce a BCF file that contains all of the locations in the genome. We use this information to call genotypes and reduce our list of sites to those found to be variant by passing this file into bcftools call.

You can do this using a pipe as shown here:
```
bcftools mpileup -Ou -f <ref.fa> <sample1.bam> <sample2.bam> <sample3.bam> | bcftools call -vmO z -o <study.vcf.gz>
```


Alternatively if you need to see why a specific site was not called by examining the BCF, or wish to spread the load slightly you can break it down into two steps as follows:

```
bcftools mpileup -Ob -o <study.bcf> -f <ref.fa> <sample1.bam> <sample2.bam> <sample3.bam>
bcftools call -vmO z -o <study.vcf.gz> <study.bcf>
```

To prepare our VCF for querying we next index it using tabix:
```
tabix -p vcf <study.vcf.gz>
```

###  graphs and statistics
Additionally you may find it helpful to prepare graphs and statistics to assist you in filtering your variants:
```
bcftools stats -F <ref.fa> -s - <study.vcf.gz> > <study.vcf.gz.stats>
mkdir plots
plot-vcfstats -p plots/ <study.vcf.gz.stats>
```

Finally you will probably need to filter your data using commands such as:
```
bcftools filter -O z -o <study_filtered..vcf.gz> -s LOWQUAL -i'%QUAL>10' <study.vcf.gz>
```

Variant filtration is a subject worthy of an article in itself and the exact filters you will need to use will depend on the purpose of your study and quality and depth of the data used to call the variants.






## Using CRAM within Samtools

CRAM is primarily a reference-based compressed format, meaning that only differences between the stored sequences and the reference are stored.

For a workflow this has a few fundamental effects:

Alignments should be kept in chromosome/position sort order.
The reference must be available at all times. Losing it may be equivalent to losing all your read sequences.
Technically CRAM can work with other orders but it can become inefficient due to a large amount of random access across the reference genome. The current implementation of CRAM in htslib 1.0 is also inefficient in size for unsorted data, although this will be rectified in upcoming releases.

In CRAM format the reference sequence is linked to by the md5sum (M5 auxiliary tag) in the CRAM header (@SQ tags). This is mandatory and part of the CRAM specification. In SAM/BAM format, these M5 tags are optional. Therefore converting from SAM/BAM to CRAM requires some additional overhead to link the CRAM to the correct reference sequence.





### Obtain some public data

We will use the first 100,000 read-pairs from a yeast data set.

```
curl ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/SRR507778/SRR507778_1.fastq.gz | gzip -d | head -100000 > y1.fastq
curl ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/SRR507778/SRR507778_2.fastq.gz | gzip -d | head -100000 > y2.fastq
curl ftp://ftp.ensembl.org/pub/current_fasta/saccharomyces_cerevisiae/dna/Saccharomyces_cerevisiae.R64-1-1.dna_sm.toplevel.fa.gz | gzip -d > yeast.fasta
```


### Prepare the BWA indices
We need to ensure there exists a .fai fasta index and also indices for whichever aligner we are using (Bwa-mem in this example).
```
samtools faidx yeast.fasta
bwa index yeast.fasta
```


### Produce the alignments
The aligner is likely to output SAM in the same order or similar order to the input fastq files. It won’t be outputting in chromosome position order, so the output is typically not well suited to CRAM.
```
bwa mem -R '@RG\tID:foo\tSM:bar\tLB:library1' yeast.fasta y1.fastq y2.fastq > yeast.sam
```
The -R option adds a read-group line and applies that read-group to all aligned sequence records. It is not necessary, but a recommended practice.

### Sort into chromosome/positon order
Ideally at this point we would be outputting CRAM directly, but at present samtools 1.0 does not have a way to indicate the reference on the command line. We can output to BAM instead and convert (below), or modify the SAM @SQ header to include MD5 sums in the M5: field.
```
samtools sort -O bam -T /tmp -l 0 -o yeast.bam yeast.sam
```
The “-l 0” indicates to use no compression in the BAM file, as it is transitory and will be replaced by CRAM soon. We may wish to use -l 1 if disk space is short and we wish to reduce temporary file size.

### Convert to CRAM format
```
samtools view -T yeast.fasta -C -o yeast.cram yeast.bam
```
Note that since the BAM file did not have M5 tags for the reference sequences, they are computed by Samtools and added to the CRAM. In a production environment, this step can be avoided by ensuring that the M5 tags are already in the SAM/BAM header.


The last 3 steps can be combined into a pipeline to reduce disk I/O:
```
bwa mem yeast.fasta y1.fastq y2.fastq | \
samtools sort -O bam -l 0 -T /tmp - | \
samtools view -T yeast.fasta -C -o yeast.cram -
```

### Viewing in alignment and pileup format
See the variant calling workflow for more advanced examples.
```
samtools view yeast.cram
samtools mpileup -f yeast.fasta yeast.cram
```




### [Decoding SAM flags](https://broadinstitute.github.io/picard/explain-flags.html)

```
$ samtools view -b -f 147 T02_dedupped.bam > T02_mapped.bam

$ samtools view -b -F 113 -F 177 T01_dedupped.fixed.bam > T01_dedupped.fixed-2.bam
```





## [ValidateSamFile](https://gatkforums.broadinstitute.org/gatk/discussion/5633/mapping-processing-and-duplicate-marking-with-picard-tools-validatesamfile-errors)


### ValidateSamFile
```
$ java -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar  ValidateSamFile I=T01_dedupped.bam MODE=SUMMARY
[Mon Dec 18 03:20:00 EST 2017] picard.sam.ValidateSamFile INPUT=T01_dedupped.bam MODE=SUMMARY    MAX_OUTPUT=100 IGNORE_WARNINGS=false VALIDATE_INDEX=true INDEX_VALIDATION_STRINGENCY=EXHAUSTIVE IS_BISULFITE_SEQUENCED=false MAX_OPEN_TEMP_FILES=8000 VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
[Mon Dec 18 03:20:00 EST 2017] Executing as wzk@ubuntu on Linux 4.4.0-62-generic amd64; OpenJDK 64-Bit Server VM 1.8.0_121-b15; Picard version: 2.8.2-SNAPSHOT


## HISTOGRAM    java.lang.String
Error Type  Count
ERROR:MISMATCH_FLAG_MATE_NEG_STRAND 185

[Mon Dec 18 03:20:03 EST 2017] picard.sam.ValidateSamFile done. Elapsed time: 0.05 minutes.
Runtime.totalMemory()=2058354688
To get help, see http://broadinstitute.github.io/picard/index.html#GettingHelp

```


### FixMateInformation

```
$ java -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar FixMateInformation INPUT=T01_dedupped.bam OUTPUT=T01_dedupped.fixed.bam  VALIDATION_STRINGENCY=LENIENT
[Mon Dec 18 03:24:52 EST 2017] picard.sam.FixMateInformation INPUT=[T01_dedupped.bam] OUTPUT=T01_dedupped.fixed.bam VALIDATION_STRINGENCY=LENIENT    ASSUME_SORTED=false ADD_MATE_CIGAR=true IGNORE_MISSING_MATES=true VERBOSITY=INFO QUIET=false COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
[Mon Dec 18 03:24:52 EST 2017] Executing as wzk@ubuntu on Linux 4.4.0-62-generic amd64; OpenJDK 64-Bit Server VM 1.8.0_121-b15; Picard version: 2.8.2-SNAPSHOT
WARNING: BAM index file /home/wzk/BSA_wheat/Picard/T01_dedupped.bam.bai is older than BAM /home/wzk/BSA_wheat/Picard/T01_dedupped.bam
INFO    2017-12-18 03:24:52 FixMateInformation  Sorting input into queryname order.
Ignoring SAM validation error: ERROR: Record 1722, Read name E00528:81:HHWKFALXX:1:1101:21856:1766, Insert size out of range
Ignoring SAM validation error: ERROR: Record 1854, Read name E00528:81:HHWKFALXX:1:1101:21856:1766, Insert size out of range
INFO    2017-12-18 03:24:52 FixMateInformation  Sorting by queryname complete.
INFO    2017-12-18 03:24:52 FixMateInformation  Output will be sorted by coordinate
INFO    2017-12-18 03:24:52 FixMateInformation  Traversing query name sorted records and fixing up mate pair information.
INFO    2017-12-18 03:24:52 FixMateInformation  Finished processing reads; re-sorting output file.
[Mon Dec 18 03:24:52 EST 2017] picard.sam.FixMateInformation done. Elapsed time: 0.01 minutes.
Runtime.totalMemory()=2058354688

```


### After fix
```
$ java -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar  ValidateSamFile I=T01_dedupped.fixed.bam  MODE=SUMMARY
[Mon Dec 18 03:26:10 EST 2017] picard.sam.ValidateSamFile INPUT=T01_dedupped.fixed.bam MODE=SUMMARY    MAX_OUTPUT=100 IGNORE_WARNINGS=false VALIDATE_INDEX=true INDEX_VALIDATION_STRINGENCY=EXHAUSTIVE IS_BISULFITE_SEQUENCED=false MAX_OPEN_TEMP_FILES=8000 VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
[Mon Dec 18 03:26:10 EST 2017] Executing as wzk@ubuntu on Linux 4.4.0-62-generic amd64; OpenJDK 64-Bit Server VM 1.8.0_121-b15; Picard version: 2.8.2-SNAPSHOT


## HISTOGRAM    java.lang.String
Error Type  Count
ERROR:INVALID_INSERT_SIZE   2

[Mon Dec 18 03:26:10 EST 2017] picard.sam.ValidateSamFile done. Elapsed time: 0.00 minutes.
Runtime.totalMemory()=2058354688
To get help, see http://broadinstitute.github.io/picard/index.html#GettingHelp


```

### samtoos index
```
$ samtools index T01_dedupped_fixed.bam
```


### SplitNCigarReads
```
$ java -jar /home/wzk/anaconda3/envs/evolution/bin/GenomeAnalysisTK.jar -T SplitNCigarReads -R /home/wzk/database/GENOME/wheat/161010_Chinese_Spring_v1.0_pseudomolecules.fasta -I T01_dedupped_fixed.bam -o T01_split.bam -rf ReassignOneMappingQuality -RMQF 255 -RMQT 60 -U ALLOW_N_CIGAR_READS
INFO  00:40:23,202 HelpFormatter - -------------------------------------------------------------------------------- 
INFO  00:40:23,204 HelpFormatter - The Genome Analysis Toolkit (GATK) v3.7-0-gcfedb67, Compiled 2016/12/12 11:21:18 
INFO  00:40:23,204 HelpFormatter - Copyright (c) 2010-2016 The Broad Institute 
INFO  00:40:23,204 HelpFormatter - For support and documentation go to https://software.broadinstitute.org/gatk 
INFO  00:40:23,204 HelpFormatter - [Mon Dec 18 00:40:23 EST 2017] Executing on Linux 4.4.0-62-generic amd64 
INFO  00:40:23,204 HelpFormatter - OpenJDK 64-Bit Server VM 1.8.0_121-b15 
INFO  00:40:23,207 HelpFormatter - Program Args: -T SplitNCigarReads -R /home/wzk/database/GENOME/wheat/161010_Chinese_Spring_v1.0_pseudomolecules.fasta -I /home/wzk/BSA_wheat/result_20171218/Picard/T01_dedupped.bam -o /home/wzk/BSA_wheat/result_20171218/Picard/T01_split.bam -rf ReassignOneMappingQuality -RMQF 255 -RMQT 60 -U ALLOW_N_CIGAR_READS 
INFO  00:40:23,210 HelpFormatter - Executing as wzk@ubuntu on Linux 4.4.0-62-generic amd64; OpenJDK 64-Bit Server VM 1.8.0_121-b15. 
INFO  00:40:23,210 HelpFormatter - Date/Time: 2017/12/18 00:40:23 
INFO  00:40:23,210 HelpFormatter - -------------------------------------------------------------------------------- 
INFO  00:40:23,211 HelpFormatter - -------------------------------------------------------------------------------- 
INFO  00:40:23,445 GenomeAnalysisEngine - Strictness is SILENT 
INFO  00:40:23,712 GenomeAnalysisEngine - Downsampling Settings: No downsampling 
INFO  00:40:23,717 SAMDataSource$SAMReaders - Initializing SAMRecords in serial 
INFO  00:40:23,743 SAMDataSource$SAMReaders - Done initializing BAM readers: total time 0.02 
INFO  00:40:23,886 GenomeAnalysisEngine - Preparing for traversal over 1 BAM files 
INFO  00:40:23,890 GenomeAnalysisEngine - Done preparing for traversal 
INFO  00:40:23,890 ProgressMeter - [INITIALIZATION COMPLETE; STARTING PROCESSING] 
INFO  00:40:23,890 ProgressMeter -                 | processed |    time |    per 1M |           |   total | remaining 
INFO  00:40:23,890 ProgressMeter -        Location |     reads | elapsed |     reads | completed | runtime |   runtime 
INFO  00:40:23,900 ReadShardBalancer$1 - Loading BAM index data 
INFO  00:40:23,901 ReadShardBalancer$1 - Done loading BAM index data 
##### ERROR ------------------------------------------------------------------------------------------
##### ERROR AN INPUT FILE ERROR has occurred (version 3.7-0-gcfedb67): 
##### ERROR
##### ERROR This means that there is something wrong with the input file(s) you provided.
##### ERROR The error message below tells you what is the problem.
##### ERROR
##### ERROR Visit our website and forum for extensive documentation and answers to 
##### ERROR commonly asked questions https://software.broadinstitute.org/gatk
##### ERROR
##### ERROR Please do NOT post this error to the GATK forum until you have followed these instructions:
##### ERROR - Make sure that your BAM file is well-formed by running Picard's validator on it
##### ERROR (see http://picard.sourceforge.net/command-line-overview.shtml#ValidateSamFile for details)
##### ERROR - Ensure that your BAM index is not corrupted: delete the current one and regenerate it with 'samtools index'
##### ERROR - Ensure that your CRAM index is not corrupted: delete the current one and regenerate it with
##### ERROR 'java -jar cramtools-3.0.jar index --bam-style-index --input-file <input cram file> --reference-fasta-file <reference fasta file>'
##### ERROR (see https://github.com/enasequence/cramtools/tree/v3.0 for details)
##### ERROR
##### ERROR MESSAGE: Exception when processing alignment for BAM index E00528:81:HHWKFALXX:1:1101:24454:2364 2/2 150b aligned read.
##### ERROR ------------------------------------------------------------------------------------------

```




### add group header
```
$ java -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar  AddOrReplaceReadGroups I=T01.bam  O=T01_group.bam  SORT_ORDER=coordinate  RGID=T01  RGLB=1  RGPL=illumina RGPU=1  RGSM=T01
[Mon Dec 18 02:40:08 EST 2017] picard.sam.AddOrReplaceReadGroups INPUT=T01.bam OUTPUT=T01_group.bam SORT_ORDER=coordinate RGID=T01 RGLB=1 RGPL=illumina RGPU=1 RGSM=T01    VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
[Mon Dec 18 02:40:08 EST 2017] Executing as wzk@ubuntu on Linux 4.4.0-62-generic amd64; OpenJDK 64-Bit Server VM 1.8.0_121-b15; Picard version: 2.8.2-SNAPSHOT
INFO    2017-12-18 02:40:08 AddOrReplaceReadGroups  Created read group ID=T01 PL=illumina LB=1 SM=T01

[Mon Dec 18 02:40:09 EST 2017] picard.sam.AddOrReplaceReadGroups done. Elapsed time: 0.00 minutes.
Runtime.totalMemory()=2058354688
```


```
$ java -jar ~/anaconda3/envs/evolution/bin/picard-2.8.2.jar  AddOrReplaceReadGroups I=../../mapping_hisat2/T01.bam  O=T01_group.bam  SORT_ORDER=coordinate  RGID=T01  RGLB=1  RGPL=illumina RGPU=1  RGSM=T01
[Mon Dec 18 02:42:52 EST 2017] picard.sam.AddOrReplaceReadGroups INPUT=../../mapping_hisat2/T01.bam OUTPUT=T01_group.bam SORT_ORDER=coordinate RGID=T01 RGLB=1 RGPL=illumina RGPU=1 RGSM=T01    VERBOSITY=INFO QUIET=false VALIDATION_STRINGENCY=STRICT COMPRESSION_LEVEL=5 MAX_RECORDS_IN_RAM=500000 CREATE_INDEX=false CREATE_MD5_FILE=false GA4GH_CLIENT_SECRETS=client_secrets.json
[Mon Dec 18 02:42:52 EST 2017] Executing as wzk@ubuntu on Linux 4.4.0-62-generic amd64; OpenJDK 64-Bit Server VM 1.8.0_121-b15; Picard version: 2.8.2-SNAPSHOT
INFO    2017-12-18 02:42:52 AddOrReplaceReadGroups  Created read group ID=T01 PL=illumina LB=1 SM=T01

[Mon Dec 18 02:42:53 EST 2017] picard.sam.AddOrReplaceReadGroups done. Elapsed time: 0.01 minutes.
Runtime.totalMemory()=2058354688
To get help, see http://broadinstitute.github.io/picard/index.html#GettingHelp
Exception in thread "main" htsjdk.samtools.SAMFormatException: SAM validation error: ERROR: Record 106036, Read name E00528:81:HHWKFALXX:1:1101:21085:11963, Insert size out of range
    at htsjdk.samtools.SAMUtils.processValidationErrors(SAMUtils.java:448)
    at htsjdk.samtools.BAMFileReader$BAMFileIterator.advance(BAMFileReader.java:665)
    at htsjdk.samtools.BAMFileReader$BAMFileIterator.next(BAMFileReader.java:650)
    at htsjdk.samtools.BAMFileReader$BAMFileIterator.next(BAMFileReader.java:620)
    at htsjdk.samtools.SamReader$AssertingIterator.next(SamReader.java:569)
    at htsjdk.samtools.SamReader$AssertingIterator.next(SamReader.java:543)
    at picard.sam.AddOrReplaceReadGroups.doWork(AddOrReplaceReadGroups.java:140)
    at picard.cmdline.CommandLineProgram.instanceMain(CommandLineProgram.java:205)
    at picard.cmdline.PicardCommandLine.instanceMain(PicardCommandLine.java:94)
    at picard.cmdline.PicardCommandLine.main(PicardCommandLine.java:104)
```