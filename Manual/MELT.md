
## [MELT](http://melt.igs.umaryland.edu/manual.php)

### parameters
```
$ java -jar MELT.jar

MELTv2.1.5 - Perform transposon analysis.

java -jar MELT.jar <Runtime>

Possible options for <Runtime>:
BuildTransposonZIP  Create an MEI.zip file for input into other MELT Runtimes.
Preprocess          Process .bam files for MELT analysis.
Single              Run a single .bam file through MELT analysis.
SGE                 Run multiple .bam files through MELT analysis using SGE.
IndivAnalysis       Step 1 of MELT-SPLIT -- Discover Putative MEIs.
GroupAnalysis       Step 2 of MELT-SPLIT -- Determine MEI Breakpoint and Information.
Genotype            Step 3 of MELT-SPLIT -- Genotype Putative MEIs.
MakeVCF             Step 4 of MELT-SPLIT -- Perform final filtering and output VCF.
Source              Build a source L1 file for input to Transduction.
TransductionFind    Preprocess bam files for L1 3' Transduction discovery in already run MELT data.
TransductionMerge   Search for L1 3' Transductions in already run MELT data using preprocessed .trans files.
Deletion-Genotype   Genotype a .bam file for reference MEI deletions.
Deletion-Merge      Merge multiple reference deletion genotypes into final VCF.
CALU                CAlu Alu analysis. Classify Alu according to family and subfamily.
LINEU               LineU L1 analysis. Classify L1 according to family and subfamily.
GENERIC             Determine differences between a consensus ME sequence and additional copies.

--help/-help/-h will print this message and exit

```


```
$ java -jar /home/wuzhikun/software/MELTv2.1.5/MELT.jar Single

Command Line:
MELT.jar Single 

Start time: Dec 24, 2019 4:49:47 PM

Performing MELT analysis...


Missing required options: bamfile, h, w, t, n, c

usage: java -jar MELT.jar Single <options>
MELTv2.1.5 - MELT-Single - Perform transposon analysis on a single sample.

 -a               Reads have been aligned with bwa-aln. [false]
 -ac              Remove ac0 sites from final VCF file. [false]
 -b <arg>         Exclusion list for chromosomes. A '/' seperated list: i.e. to exclude chromosomes 1,2, and 4, put -b 1/2/4. [null]
 -bamfile <arg>   Bam file for MEI analysis.
 -bowtie <arg>    Path to the bowtie2 algorithm if not in PATH [null].
 -c <arg>         Coverage level of supplied bam file.
 -cov <arg>       Standard deviation cutoff when calling final sites in integer format. [35]
 -d <arg>         Minumum length of chromosome/contig size for calling elements. [1000000]
 -e <arg>         Expected insert size between reads. [500]
 -h <arg>         Path to the reference sequence used to align reads.
 -j <arg>         Total percentage of sites allowed to be no call (in integer form i.e. 25 percent would be -i 25, not .25). [25]
 -k               BAM file(s) have already been processed for discordant pairs (suffixes .fq, .disc, and .disc.bai are already present for the bam file in -l). [false]
 -n <arg>         Path to the genome annotation.
 -nocleanup       Do not cleanup MELT intermediate files after running. [false]
 -q               Alignments are phred+64 quality encoding. [false]
 -r <arg>         Read length of the supplied bam file(s). [100]
 -s <arg>         Standard deviation cutoff for excluding sites with improper balance of readpairs in double format. [2.0]
 -sr <arg>        Filter sites with less than X SRs during breakpoint ascertainment. Default, -1, is to not filter any such sites. [-1]
 -t <arg>         Path to the transposon ZIP file(s) to be used for this analysis.
 -w <arg>         Path to the working root directory.
 -z <arg>         Maximum reads to load into memory when iterating over sequence files. Setting higher increases run time, but may increase sensitivity in large (>60X coverage) bam files. Setting lower may decrease sensitivity in all bam files. [5000]

-help will print this message and exit

```


### run MELT
```
(NanoSV) wuzhikun@fat02 16:54:30 O_O /home/wuzhikun/Project/Illumina_Trio/mapping/delly 
$ java -jar /home/wuzhikun/software/MELTv2.1.5/MELT.jar  Single  -c 15 -h /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  -bamfile M446-0.bqsr_chr16.bam -w melt  -t /home/wuzhikun/software/MELTv2.1.5/me_refs/Hg38/ALU_MELT.zip  -n /home/wuzhikun/software/MELTv2.1.5/add_bed_files/Hg38/Hg38.genes.bed


Command Line:
MELT.jar Single -c 15 -h /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -bamfile M446-0.bqsr_chr16.bam -w melt -t /home/wuzhikun/software/MELTv2.1.5/me_refs/Hg38/ALU_MELT.zip -n /home/wuzhikun/software/MELTv2.1.5/add_bed_files/Hg38/Hg38.genes.bed 

Start time: Dec 24, 2019 4:57:40 PM

Performing MELT analysis...
--------------------------------------------------------------------
Extracting discordant pairs.
Current time: Dec 24, 2019 4:57:44 PM
All BAM Reference sequences are present in the provided reference.
Total reads processed: 17685526
Total proper pairs: 17325998
Supp reads filtered: 0
Percent discordant: 1.7
BAM has within the expected tolerance for improper pairs, safe to proceed with MELT analysis.
--------------------------------------------------------------------
Performing initial MEI discovery on the 1 mobile elements in provided list.
Current time: Dec 24, 2019 5:00:32 PM
--------------------------------------------------------------------
Determining statistics about each mobile element type.
Current time: Dec 24, 2019 5:01:20 PM
--------------------------------------------------------------------
Calling final genotypes in M446-0.bqsr_chr16.bam.
Current time: Dec 24, 2019 5:01:22 PM
--------------------------------------------------------------------
Merging all genotype calls and statistics into final VCF output.
Current time: Dec 24, 2019 5:01:23 PM
--------------------------------------------------------------------
Cleaning up intermediate files
Current time: Dec 24, 2019 5:01:23 PM
--------------------------------------------------------------------
End time: Dec 24, 2019 5:01:23 PM


```

#### output files:
```
-rw-rw-r-- 1   86 Dec 24 17:01 ALU.bed.list
-rw-rw-r-- 1 3.1K Dec 24 17:01 ALU.final_comp.vcf
-rw-rw-r-- 1   82 Dec 24 17:01 ALU.hum.list
-rw-rw-r-- 1   31 Dec 24 17:01 ALU.master.bed
-rw-rw-r-- 1  23K Dec 24 17:01 ALU.merged.hum_breaks.sorted.bam
-rw-rw-r-- 1  38K Dec 24 17:01 ALU.merged.hum_breaks.sorted.bam.bai
-rw-rw-r-- 1  141 Dec 24 17:01 ALU.pre_geno.tsv
-rw-rw-r-- 1 1.7M Dec 24 17:01 M446-0.bqsr_chr16.ALU.aligned.final.sorted.bam
-rw-rw-r-- 1   96 Dec 24 17:01 M446-0.bqsr_chr16.ALU.aligned.final.sorted.bam.bai
-rw-rw-r-- 1  24K Dec 24 17:01 M446-0.bqsr_chr16.ALU.hum_breaks.sorted.bam
-rw-rw-r-- 1  38K Dec 24 17:01 M446-0.bqsr_chr16.ALU.hum_breaks.sorted.bam.bai
-rw-rw-r-- 1  85K Dec 24 17:01 M446-0.bqsr_chr16.ALU.pulled.sorted.bam
-rw-rw-r-- 1  50K Dec 24 17:01 M446-0.bqsr_chr16.ALU.pulled.sorted.bam.bai
-rw-rw-r-- 1   31 Dec 24 17:01 M446-0.bqsr_chr16.ALU.tmp.bed
-rw-rw-r-- 1   28 Dec 24 17:01 M446-0.bqsr_chr16.ALU.tsv
drwxrwxr-x 1 4.0K Dec 24 17:00 M446-0.bqsr_chr16tmp

```

