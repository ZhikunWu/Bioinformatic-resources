## Shimmer

### install Shimmer
```
git clone https://github.com/nhansen/Shimmer.git

cd Shimmer/printCompCounts && make
cp  printCompCounts /home/wuzhikun/anaconda/envs/WGS/bin
```

```
-rw-rw-r-- 1 1.2K Jun  1 10:53 Build.PL
-rw-rw-r-- 1  100 Jun  1 10:53 check_statmod.R
-rw-rw-r-- 1 8.4K Jun  1 10:53 DOCUMENTATION
-rw-rw-r-- 1 1.1K Jun  1 10:53 INSTALL
-rw-rw-r-- 1  996 Jun  1 10:53 LEGAL
-rw-rw-r-- 1  136 Jun  1 10:53 Makefile
-rw-rw-r-- 1  302 Jun  1 10:53 MANIFEST
-rw-rw-r-- 1   38 Jun  1 10:53 MANIFEST.SKIP
-rw-rw-r-- 1  397 Jun  1 10:53 META.yml
-rw-rw-r-- 1  415 Jun  1 10:53 MYMETA.yml
drwxrwxr-x 1 4.0K Jun  1 10:53 printCompCounts
-rw-rw-r-- 1  960 Jun  1 10:53 README
-rw-rw-r-- 1  996 Jun  1 10:53 README.textile
drwxrwxr-x 1 4.0K Jun  1 10:53 scripts
-rwxrwxr-x 1  49K Jun  1 10:53 shimmer.pl
drwxrwxr-x 1 4.0K Jun  1 10:53 sim_scripts
drwxrwxr-x 1 4.0K Jun  1 10:53 t

```



### parameters


```
$ perl shimmer.pl 
Usage: shimmer.pl <--region chr1:1000-2000> <--bedfile bed file of regions> <--ref reference fasta> <bam file from normal sample> <bam file from mutated sample>
For more information, type "perldoc shimmer.pl". at shimmer.pl line 49.

```


```
NAME
    shimmer.pl - call somatic single base changes from matched tumor and
    normal next generation sequences.

SYNOPSIS
    Tally counts of alleles in two BAM files, and write out data for sites
    with unexpectedly large deviations in allele frequencies, controlling the
    false discovery rate (FDR) using the Benjamini-Hochberg procedure:

      shimmer.pl [options] <normal_bam_file> <tumor_bam_file> --ref <ref_fasta_file>

    Run shimmer.pl -man for a detailed description of options and the output
    files.

DESCRIPTION
    The script creates a randomly named directory (run_shimmer_XXXXXX) in the
    user's current working directory, and reads through the two BAM files
    provided as options with samtools mpileup, recording the normal sample's
    genotype, as well as the counts of the two most frequently seen alleles at
    each site. It then uses the R "statmod" library to calculate p-values with
    the Fisher's exact test on each site where a minimum threshold of
    alternate allele copies are seen (see --min_som_reads option).

    Once all p-values have been calculated, shimmer.pl uses the
    Benjamini-Hochberg procedure to report only changes with a false discovery
    rate below the specified maximum FDR (see --max_q option). The
    single-nucleotide variants are reported in VarSifter and VCF formats in
    the files "somatic_diffs.vs" and "somatic_diffs.vcf", respectively.

INPUT
    The first and second arguments to shimmer are the paths of two
    BAM-formatted files of aligned sequencing reads. These files must be
    sorted using samtools prior to running shimmer, and indexed if the
    --region option wil be used.

    The path of a valid, fasta-formatted file for the reference sequence must
    be passed with the option --ref. This fasta file must have a corresponding
    samtools index file with the same name except for an appended ".fai" if
    the --region option will be used.

OPTIONS
    --region chr or
    --region chr:start-end
         This option specifies a region as a reference entry (chromosome),
         optionally followed by a position range, and causes the program to
         limit somatic call to only that region. By default, the program calls
         variants in all regions that covered by reads in both BAM files.
    --bedfile bedfilename
         This option specifies the path of a BED formatted file containing
         regions to be tested for somatic variants. Limiting regions with this
         option can increase power to detect somatic variation by reducing the
         number of tests performed.

    --ref reference_fasta_file
         This option specifies the reference file to which the reads in the
         BAM files were aligned. It is a required option.

    --minqual min_base_quality_score
         This option specifies a minimum phred quality score to be required
         for read bases to be included in the counts for the Fisher's exact
         tests. By default, all bases are included.

    --mapqual min_mapping_quality_score
         This option specifies a minimum read mapping quality score to be
         required for a read's bases to be included in the counts for the
         Fisher's exact tests. By default, all reads' bases are included.

    --max_q max_acceptable_FDR
         This option specifies the maximum FDR level to be set for the
         Benjamini-Hochberg procedure for multiple testing correction. A value
         of 0 will cause shimmer to report all tests including those with q
         values equal to 1. (Default=0.05)

    --annovardb path_to_annovar_db_directory
         This option allows the user to specify an ANNOVAR database directory
         against which to annotate variants (see Wang et al, "ANNOVAR:
         functional annotations of genetic variants from high-throughput
         sequencing data". Nucl. Acids Res. 38, 2010).

    --buildver <hg18, hg19, etc.>
         This option is passed directly to ANNOVAR.

    --annovar path_to_annovar
         This option allows the user to specify a particular path to the
         "annotate_variants.pl" script from ANNOVAR. As a default, if the
         annovardb option has been specified (see above), Shimmer will call
         the first copy of "annotate_variation.pl" in the user's path.

    --outdir <path_to_output_directory>
         This option specifies a directory in which to place result files for
         this run. If the directory doesn't exist, it will be created. By
         default, Shimmer will create a randomly named directory called
         "run_shimmer_XXXXXX" within the current working directory (where
         "XXXXXX" is a random string of length 6).
    --testall
         This option causes the Fisher's Exact Test to be performed on all
         sites with the specified minimum number of alternate alleles, not
         just sites at which the normal sample has homozygous reference
         genotype.

OUTPUT
    The single nucleotide variants (sSNVs) are written in both VarSifter and
    VCF formats.

    The fields in the VarSifter file (see Teer et al., "VarSifter: Visualizing
    and analyzing exome-scale sequence variation data on a desktop computer".
    Bioinformatics 28, 2012) are as follows:

    Index
         A numerical identifier for each variant.

    Chr  The entry name of the reference sequence in the BAM files and
         reference fasta file.

    LeftFlank
         Position one base to the left of the variant base.

    RightFlank
         Position one base to the right of the variant base.

    ref_allele
         Reference base.

    var_allele
         Variant base.

    muttype
         Type of mutation. In this version of shimmer.pl, all variants are of
         type "SNP". Future versions of shimmer.pl will also call somatic
         variants of type "INDEL".

    normal_covg
         Number of reads covering this position in the normal BAM file. If the
         --minqual option has been used, only reads with the required base
         quality at this position will be counted.

    tumor_covg
         Number of reads covering this position in the tumor BAM file. If the
         --minqual option has been used, only reads with the required base
         quality at this position will be counted.

    normal_ratio
         Ratio of reads with the alternate base to total reads covering this
         position in the normal BAM file. If the --minqual option has been
         used, only reads with the required base quality at this position will
         be counted.

    tumor_ratio
         Ratio of reads with the alternate base to total reads covering this
         position in the tumor BAM file. If the --minqual option has been
         used, only reads with the required base quality at this position will
         be counted.

    q_value
         The expected value of the false discovery rate if all variants with
         q_value values higher than this value were excluded.

    The VCF file conforms to the standards in VCFv4.0, but doesn't include as
    much information as the VarSifter file does. In particular, for each
    somatic SNV predicted, it reports the reference and alternate allele, the
    q-value (as described above in the VarSifter file description), and the
    genotype (always 0/0 for the normal and 0/1 for the tumor) and depth of
    coverage for each sample. Suggestions are welcome for how to best utilize
    VCF format for these data, as it's a work in progress!

```

### call somatic variants
```
$ perl ~/anaconda3/envs/WGS/bin/Shimmer/shimmer.pl --outdir /home/wuzhikun/Project/WGSSomatic/Shimmer  --ref /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam /home/wuzhikun/Project/WGSSomatic/mapping/SRR60/SRR60.bqsr.bam
```

#### Error
```
/home/wuzhikun/anaconda3/envs/WGS/bin/Shimmer/shimmer.pl --counts --ref /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam /home/wuzhikun/Project/WGSSomatic/mapping/SRR60/SRR60.bqsr.bam --min_som_reads 10 --som_file /home/wuzhikun/Project/WGSSomatic/Shimmer/som_counts.txt --het_file /home/wuzhikun/Project/WGSSomatic/Shimmer/het_counts.txt --indel_file /home/wuzhikun/Project/WGSSomatic/Shimmer/indel_counts.txt --minindel 10
Calling printCompCounts -bam1 /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam -bam2 /home/wuzhikun/Project/WGSSomatic/mapping/SRR60/SRR60.bqsr.bam -fasta /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa
[mpileup] 2 samples in 2 input files
Error in library("statmod") : there is no package called ‘statmod’
Execution halted
Error in library("statmod") : there is no package called ‘statmod’
Execution halted
Error in library("statmod") : there is no package called ‘statmod’
Execution halted
/home/wuzhikun/anaconda3/envs/WGS/bin/Shimmer/shimmer.pl --max_q 0.05 --test_fof /home/wuzhikun/Project/WGSSomatic/Shimmer/som_counts.fof --bh --vs_file /home/wuzhikun/Project/WGSSomatic/Shimmer/somatic_diffs.vs --vcf_file /home/wuzhikun/Project/WGSSomatic/Shimmer/somatic_diffs.vcf --outfile /home/wuzhikun/Project/WGSSomatic/Shimmer/som_counts.bh.txt /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam /home/wuzhikun/Project/WGSSomatic/mapping/SRR60/SRR60.bqsr.bam
Applying Benjamini-Hochberg correction to somatic change predictions with 0 tests.  Results in /home/wuzhikun/Project/WGSSomatic/Shimmer/som_counts.bh.txt.
Applying Benjamini-Hochberg correction to somatic change predictions with 0 tests.  Results in /home/wuzhikun/Project/WGSSomatic/Shimmer/indel_counts.bh.txt.

```


#### install R package
```
> install.packages("/home/wuzhikun/software/statmod_1.4.32.tar.gz", repos=NULL, type="source")
* installing *source* package ‘statmod’ ...
** package ‘statmod’ successfully unpacked and MD5 sums checked
** libs
gfortran   -fpic  -I/home/wuzhikun/anaconda3/envs/WGS/include -L/home/wuzhikun/anaconda3/envs/WGS/lib  -c gaussq2.f -o gaussq2.o
gcc -std=gnu99 -I/home/wuzhikun/anaconda3/envs/WGS/lib/R/include -DNDEBUG  -I/home/wuzhikun/anaconda3/envs/WGS/include    -fpic  -I/home/wuzhikun/anaconda3/envs/WGS/include  -c init.c -o init.o
gcc -std=gnu99 -shared -L/home/wuzhikun/anaconda3/envs/WGS/lib/R/lib -L/home/wuzhikun/anaconda3/envs/WGS/lib -lgfortran -o statmod.so gaussq2.o init.o -lgfortran -lm -lquadmath -L/home/wuzhikun/anaconda3/envs/WGS/lib/R/lib -lR
installing to /home/wuzhikun/anaconda3/envs/WGS/lib/R/library/statmod/libs
** R
** data
** inst
** preparing package for lazy loading
** help
*** installing help indices
** building package indices
** testing if installed package can be loaded
* DONE (statmod)

```


#### re-run to call somatic variants
```
perl ~/anaconda3/envs/WGS/bin/Shimmer/shimmer.pl --outdir /home/wuzhikun/Project/WGSSomatic/Shimmer --ref /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam /home/wuzhikun/Project/WGSSomatic/mapping/SRR60/SRR60.bqsr.bam
```



output file:
```
-rw-rw-r-- 1 9.8M Jun  1 14:56 het_counts.tests.txt
-rw-rw-r-- 1 8.7M Jun  1 12:20 het_counts.txt
-rw-rw-r-- 1 1.4K Jun  1 14:55 het_counts.txt.r
-rw-rw-r-- 1 1.7K Jun  1 14:56 indel_counts.bh.txt
-rw-rw-r-- 1   65 Jun  1 14:56 indel_counts.fof
-rw-rw-r-- 1 261K Jun  1 14:56 indel_counts.tests.txt
-rw-rw-r-- 1 241K Jun  1 12:20 indel_counts.txt
-rw-rw-r-- 1 1.4K Jun  1 14:56 indel_counts.txt.r
-rw------- 1 1.3K Jun  1 14:56 nohup.out
-rw-rw-r-- 1  17K Jun  1 14:56 somatic_diffs.vcf
-rw-rw-r-- 1  31K Jun  1 14:56 somatic_diffs.vs
-rw-rw-r-- 1 1.8K Jun  1 14:56 somatic_indels.vs
-rw-rw-r-- 1  28K Jun  1 14:56 som_counts.bh.txt
-rw-rw-r-- 1   63 Jun  1 14:56 som_counts.fof
-rw-rw-r-- 1  10M Jun  1 14:55 som_counts.tests.txt
-rw-rw-r-- 1 7.3M Jun  1 12:20 som_counts.txt
-rw-rw-r-- 1 1.4K Jun  1 14:51 som_counts.txt.r

```



#### detail for output file
```
$ head indel_counts.txt
#Indels	1	258768	C	258	299	-1G	8	14	hom
#Indels	1	874372	G	144	141	+1T	4	6	hom
#Indels	1	939570	T	8	7	+12CCCTGGAGGACC	6	5	und
#Indels	1	1043223	C	12	3	-2CT	7	4	het
#Indels	1	1223154	G	22	13	+2AC	14	12	het
#Indels	1	1223182	A	23	14	-2AC	17	19	het
#Indels	1	1228431	G	17	10	+4GACA	13	7	het
#Indels	1	1341550	G	2	1	-2CA	16	16	und
#Indels	1	1341593	G	6	1	+4ACAC	29	22	und
#Indels	1	1353987	C	2	1	-2TG	38	32	und

```


```
$ head  somatic_diffs.vcf
##fileformat=VCFv4.1
##fileDate=20190601
##source=Shimmer
##INFO=<ID=RM,Number=0,Type=Flag,Description="Lower-case reference (probably masked for repeat)">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	NORMAL	TUMOR
1	11073899	.	A	G	21	.	.	GT:DP	0/0:10	0/1:13
1	13780432	.	G	C	185	.	.	GT:DP	0/0:243	0/1:155
1	16294728	.	C	G	59	.	.	GT:DP	0/0:71	0/1:59

```
