

## [SomaticSniper](http://gmt.genome.wustl.edu/packages/somatic-sniper/install.html)


### SomaticSniper  pipeline

1.Call SomaticSniper from the command line
```
bam-somaticsniper –f ref.fa tumor.bam normal.bam
output.txt
```

2.Examine the output available in output.txt.

3. Generate a samtools pileup indel file for indel filtering
```
samtools pileup –cvi –f ref.fa tumor.bam indel.pileup
```

4. Filter out low quality indels called by samtools.
```
perl samtools/misc/samtools.pl varFilter indel.pileup
> indel.pileup.filtered
```

5. Filter SomaticSniper’s predictions by quality and proximity to indels using the provided filtering script.
```
perl snpfilter.pl --snp-file output.txt --indel-file
indel.pileup.filtered --out-file output.SNPfilter.txt
```

6. Adapt the remaining unfiltered SNVs for use with bam-readcount.
```
perl prepare_for_readcount.pl --snp-file
output.SNPfilter.txt --out-file output.SNPfilter.pos
```

7. Run bam-readcount using the same mapping quality (-q) setting as used for SomaticSniper.
```
bam-readcount -b 15 -f ref.fa –l output.SNPfilter.pos
tumor.bam > output.SNPfilter.rc
```

8. Run the false positive filter to eliminate likely incorrect calls.
```
perl fpfilter.pl --snp-file output.SNPfilter.txt --
readcount-file output.SNPfilter.rc
```

9. Lastly, run the "high confidence" filter which filters based on the somatic score and mapping quality.

```
perl highconfidence.pl --snp-file
output.SNPfilter.txt.fp_pass --out-file
output.SNPfilter.txt.fp_pass.hc
```



### SomaticSniper parameters
```
$ perl /home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/src/scripts/snpfilter.pl --help
snpfilter - Basic filtering for SomaticSniper

SYNOPSIS
snpfilter [options] [file ...]

OPTIONS
--snp-file              the input bam-somaticsniper output file (requires v1.0.0 or greater output)
--lq-output             this is an optional place to stick sn(p|v)s which have failed to pass this filter
--min-mapping-quality   min mapping quality of the reads covering the SNP, default 40 
--min-cns-qual          minimum consensus quality, default 20
--min-read-depth        minimum read depth to call a SNP, default 3
--max-read-depth        maximum read depth to call a SNP, default 100000000
--snp-win-size          window size for filtering dense SNPs, default 10
--max-snp-per-win       maximum number of SNPs in a sized window, default 2
--min-snp-qual          check minimum snp quality if consensus qual is lower than min_cns_qual, default 20
--out-file              snp output file after filter
--indel-file            path of samtools *pileup* format indel file to be used as a filter to screen out snps close to indel
--indel-win-size        window size of indel position in which SNPs should be filtered out, default 10
--min-indel-score       minimum samtools indel score, default 50
--tumor-variant-only    whether or not to pass homozygous ref calls in the tumor (off by default)
--include-loh           whether or not to pass sites likely to be loss of heterozygosity (on by default)
--help                  this message

DESCRIPTION
This program will filter bam-somaticsniper output with some basic filters inspired by maq.pl SNPfilter

AUTHORS
Dave Larson     Extraction from standard TGI framework and modification specifically for bam-somaticsniper
Feiyu Du        Original code

SUPPORT
For user support please mail genome-dev@genome.wustl.edu.

```






### example

```
java -jar Seurat.jar -T Seurat -R ref.fasta -I:dna_normal DNA_normal.BAM -I:dna_tumor DNA_tumor.BAM -I:rna_tumor RNA_tumor.BAM -o somatic_variants.vcf -go large_events.txt -Q 15 -refseq refseq.rod
```





```
$ git clone git://github.com/genome/somatic-sniper.git
$ mkdir somatic-sniper/build
$ cd somatic-sniper/build
$ cmake ../
$ make deps
Scanning dependencies of target samtools-lib
[ 12%] Creating directories for 'samtools-lib'
[ 25%] Performing download step (verify and extract) for 'samtools-lib'
CMake Warning at src/samtools-lib-stamp/verify-samtools-lib.cmake:15 (message):
  File will not be verified since no URL_HASH specified


-- extracting...
     src='/home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/vendor/samtools-0.1.6.tar.gz'
     dst='/home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/build/vendor/samtools'
-- extracting... [tar xfz]
-- extracting... [analysis]
-- extracting... [rename]
-- extracting... [clean up]
-- extracting... done
[ 37%] Performing patch step for 'samtools-lib'
patching file Makefile
[ 50%] No update step for 'samtools-lib'
[ 62%] Performing configure step for 'samtools-lib'
Building samtools, build log at /home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/build/vendor/samtools/build.log
[ 75%] Performing build step for 'samtools-lib'
[ 87%] No install step for 'samtools-lib'
[100%] Completed 'samtools-lib'
[100%] Built target samtools-lib
Scanning dependencies of target deps
[100%] Built target deps


$ make -j
Scanning dependencies of target gtest160
Scanning dependencies of target doc
Scanning dependencies of target sniper
[ 25%] Built target doc
[ 29%] Built target samtools-lib
[ 29%] Creating directories for 'gtest160'
[ 29%] Built target deps
[ 32%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/allele_util.c.o
[ 38%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/output_bed.c.o
[ 38%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/dqstats.c.o
[ 41%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/output_classic.c.o
[ 51%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/output_vcf.c.o
[ 51%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/output_format.c.o
[ 54%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/sniper_maqcns.c.o
[ 54%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/sniper_pileup.c.o
[ 58%] Building C object build/src/lib/sniper/CMakeFiles/sniper.dir/somatic_sniper.c.o
[ 61%] Performing download step (verify and extract) for 'gtest160'
CMake Warning at gtest160-stamp/verify-gtest160.cmake:15 (message):
  File will not be verified since no URL_HASH specified


-- extracting...
     src='/home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/build-common/vendor/gtest-1.6.0.tar.gz'
     dst='/home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/build/vendor/src/gtest160'
-- extracting... [tar xfz]
/home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/src/lib/sniper/sniper_maqcns.c: In function ‘sniper_cal_het’:
/home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/src/lib/sniper/sniper_maqcns.c:32:19: warning: variable ‘p3’ set but not used [-Wunused-but-set-variable]
  double p1 = 0.0, p3 = 0.0; // just for testing
                   ^
/home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/src/lib/sniper/sniper_maqcns.c:32:9: warning: variable ‘p1’ set but not used [-Wunused-but-set-variable]
  double p1 = 0.0, p3 = 0.0; // just for testing
         ^
[ 64%] Linking C static library libsniper.a
-- extracting... [analysis]
-- extracting... [rename]
-- extracting... [clean up]
-- extracting... done
[ 70%] No patch step for 'gtest160'
[ 70%] No update step for 'gtest160'
[ 70%] Built target sniper
Scanning dependencies of target bam-somaticsniper
[ 74%] Performing configure step for 'gtest160'
[ 77%] Building C object build/src/exe/bam-somaticsniper/CMakeFiles/bam-somaticsniper.dir/main.c.o
-- The CXX compiler identification is GNU 4.8.5
[ 80%] Linking C executable ../../../../bin/bam-somaticsniper
-- The C compiler identification is GNU 4.8.5
[ 80%] Built target bam-somaticsniper
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Found PythonInterp: /home/wuzhikun/anaconda3/envs/WGS/bin/python (found version "3.6.7") 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - found
-- Found Threads: TRUE  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/build/vendor/gtest160-build
[ 83%] Performing build step for 'gtest160'
Scanning dependencies of target gtest
[ 25%] Building CXX object CMakeFiles/gtest.dir/src/gtest-all.cc.o
[ 50%] Linking CXX static library libgtest.a
[ 50%] Built target gtest
Scanning dependencies of target gtest_main
[ 75%] Building CXX object CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
[100%] Linking CXX static library libgtest_main.a
[100%] Built target gtest_main
[ 87%] No install step for 'gtest160'
[ 90%] Completed 'gtest160'
[ 90%] Built target gtest160
Scanning dependencies of target SniperUnitTests
[ 96%] Building CXX object build/test/lib/sniper/CMakeFiles/SniperUnitTests.dir/TestAlleleUtil.cpp.o
[ 96%] Building CXX object build/test/lib/sniper/CMakeFiles/SniperUnitTests.dir/TestDqStats.cpp.o
[100%] Linking CXX executable SniperUnitTests
[100%] Built target SniperUnitTests


$ make test
Running tests...
Test project /home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/build
    Start 1: SniperUnitTests
1/2 Test #1: SniperUnitTests ..................   Passed    0.01 sec
    Start 2: Sniper
2/2 Test #2: Sniper ...........................***Failed    0.28 sec

50% tests passed, 1 tests failed out of 2

Label Time Summary:
integration    =   0.28 sec*proc (1 test)
unit           =   0.01 sec*proc (1 test)

Total Test time (real) =   0.33 sec

The following tests FAILED:
	  2 - Sniper (Failed)
Errors while running CTest
make: *** [test] Error 8

```

#### create the soft link

```
$ ln -s /home/wuzhikun/anaconda3/envs/WGS/bin/somatic-sniper/build/bin/bam-somaticsniper /home/wuzhikun/anaconda3/envs/WGS/bin/somaticsniper
```

### parameters

```
$ ./bam-somaticsniper 


bam-somaticsniper [options] -f <ref.fasta> <tumor.bam> <normal.bam> <snp_output_file>

Required Option: 
        -f FILE   REQUIRED reference sequence in the FASTA format

Options: 
        -v        Display version information

        -q INT    filtering reads with mapping quality less than INT [0]
        -Q INT    filtering somatic snv output with somatic quality less than  INT [15]
        -L FLAG   do not report LOH variants as determined by genotypes
        -G FLAG   do not report Gain of Reference variants as determined by genotypes
        -p FLAG   disable priors in the somatic calculation. Increases sensitivity for solid tumors
        -J FLAG   Use prior probabilities accounting for the somatic mutation rate
        -s FLOAT  prior probability of a somatic mutation (implies -J) [0.010000]
        -T FLOAT  theta in maq consensus calling model (for -c/-g) [0.850000]
        -N INT    number of haplotypes in the sample (for -c/-g) [2]
        -r FLOAT  prior of a difference between two haplotypes (for -c/-g) [0.001000]
        -n STRING normal sample id (for VCF header) [NORMAL]
        -t STRING tumor sample id (for VCF header) [TUMOR]
        -F STRING select output format [classic]
           Available formats:
             classic
             vcf
             bed

```


#### notes

Minimally, you must provide the program the reference fasta the bams were aligned against (passed with the -f option), a tumor bam, a normal bam, and the filename of the resulting output file. We recommend filtering out reads with a mapping quality of 0 (i.e. use -q 1) as they are typically randomly placed in the genome. We have also found that few variants with a somatic score less than 15 validate, but you may decrease the minimum score or increase it to a higher threshold (eg -Q 40). To obtain high confidence sites, we recommend also thresholding the minimum average mapping quality for the variant base to 40 for reads aligned with BWA or 70 for reads aligned with MAQ. We have not tested other aligners at this time. Disabling priors is not recommended, but may increase sensitivity at the cost of a decrease in specificity.


#### Current Recommended Settings

We recommend that you utilize both the -G and -L options when running in order to reduce likely false positives with little impact on sensitivity. An example command-line is below:
```
bam-somaticsniper -Q 40 -G -L -f reference.fa tumor.bam normal.bam output.txt
```

#### Basic filtering with provided Perl scripts

A small number of basic Perl scripts are included in the SomaticSniper package (located in src/scripts of the source code release) to aid in filtering out likely false positives. In order to get the recommended filtering you should do the following. Defaults are set assuming that BWA short is the aligner used. Other aligners have not been tested and recommendations are not available. Before proceeding you will need to obtain and compile bam-readcount (https://github.com/genome/bam-readcount). You will also need to generate a samtools pileup (not mpileup) indel file. Handling of indel containing VCFs is not implemented.

Filter on standard filters using the indel file. This will also remove LOH calls e.g. perl snpfilter.pl –snp-file your_sniper_file –indel-file your_indel_pileup

Adapt the remainder for use with bam-readcount e.g. perl prepare_for_readcount.pl –snp-file your_sniper_file.SNPfilter

Run bam-readcount (I’d recommend using the same mapping quality -q setting as you ran SomaticSniper with) e.g. bam-readcount -b 15 -f your_ref.fasta -l your_sniper_file.SNPfilter.pos your_tumor.bam > your_readcounts.rc Run the false positive filter e.g. perl fpfilter.pl –snp-file your_sniper_file.SNPfilter –readcount-file your_readcounts.rc

Lastly, run the “high confidence” filter which filters based on the Somatic Score and mapping quality e.g. perl highconfidence.pl –snp-file your_sniper_file.SNPfilter.fp_pass

Your final set of high confidence and highly filtered indels is now in the file your_sniper_file.SNPfilter.fp_pass.hc


### File Formats
The output by SomaticSniper consists of line for all sites whose consensus differs from the reference base. Each of the three available output formats is described below

#### Classic

Each line contains the following tab-separated values:
```
Chromosome
Position
Reference base
IUB genotype of tumor
IUB genotype of normal
Somatic Score
Tumor Consensus quality
Tumor variant allele quality
Tumor mean mapping quality
Normal Consensus quality
Normal variant allele quality
Normal mean mapping quality
Depth in tumor (# of reads crossing the position)
Depth in normal (# of reads crossing the position)
Mean base quality of reads supporting reference in tumor
Mean mapping quality of reads supporting reference in tumor
Depth of reads supporting reference in tumor
Mean base quality of reads supporting variant(s) in tumor
Mean mapping quality of reads supporting variant(s) in tumor
Depth of reads supporting variant(s) in tumor
Mean base quality of reads supporting reference in normal
Mean mapping quality of reads supporting reference in normal
Depth of reads supporting reference in normal
Mean base quality of reads supporting variant(s) in normal
Mean mapping quality of reads supporting variant(s) in normal
Depth of reads supporting variant(s) in normal
```

#### VCF

VCF output from SomaticSniper conforms to version 4.1 of the VCF specification. Hence, each non-header output line contains the following fields:

```
Chromosome
Position
ID (unused)
Reference base
Alternate bases (comma separated)
Quality (unused)
Filters (unused)
INFO (unused)
FORMAT specification for each sample
NORMAL sample data
TUMOR sample data
```


The following FORMAT fields will be populated for each of NORMAL and TUMOR.

```

ID  Number  Type    Description
GT  1   String  Genotype
IGT 1   String  Genotype when called independently (only filled if called in joint prior mode)
DP  1   Integer Total read depth
DP4 4   Integer Number of high-quality ref-forward bases, ref-reverse, alt-forward and alt-reverse bases
BCOUNT  4   Integer Occurrence count for each base at this site (A,C,G,T)
GQ  1   Integer Genotype quality
JGQ 1   Integer Joint genotype quality (only filled if called in joint prior mode)
VAQ 1   Integer Variant quality
BQ  .   Integer Average base quality of each base in the call, reported in alphabetical order (A,C,G,T)
MQ  1   Integer Average mapping quality across all reads.
AMQ .   Integer Average mapping quality of each base in the call, reported in alphabetical order (A,C,G,T)
SS  1   Integer Variant status relative to non-adjacent normal: 0=wildtype, 1=germline, 2=somatic, 3=LOH, 4=unknown
SSC 1   Integer Somatic Score
```

### run somaticsniper
```
$ somaticsniper -n M625-1 -t M625-0 -F vcf -Q 30 -L -G   -f /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa M625-0/M625-0.bqsr.bam  M625-1/M625-1.bqsr.bam  M625_somaticsniper.vcf 
Preparing to snipe some somatics
Using prior probabilities
Normal bam is M625-1/M625-1.bqsr.bam
Tumor bam is M625-0/M625-0.bqsr.bam
```
