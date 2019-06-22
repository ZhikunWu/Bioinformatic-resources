## [sniffles](https://github.com/fritzsedlazeck/Sniffles)
### install sniffles
```
$ conda install -c bioconda sniffles
```

tools:
```
lrwxrwxrwx 1 wzk KC   14 Dec 26 06:16 bamtools -> bamtools-2.4.1
-rwxrwxr-x 1 wzk KC 9.6M Dec 26 06:16 sniffles-debug
-rwxrwxr-x 1 wzk KC 6.4M Dec 26 06:16 sniffles
-rwxrwxr-x 1 wzk KC 850K Dec 26 06:16 bamtools-2.4.1

```




### sniffles
```
$ sniffles --help

Usage: sniffles [options] -m <sorted.bam> -v <output.vcf> 
Version: 1.0.10
Contact: fritz.sedlazeck@gmail.com

Input/Output:
    -m <string>,  --mapped_reads <string>
        (required)  Sorted bam File
    -v <string>,  --vcf <string>
        VCF output file name []
    -b <string>,  --bedpe <string>
         bedpe output file name []
    --Ivcf <string>
        Input VCF file name. Enable force calling []
    --tmp_file <string>
        path to temporary file otherwise Sniffles will use the current directory. []

General:
    -s <int>,  --min_support <int>
        Minimum number of reads that support a SV. [10]
    --max_num_splits <int>
        Maximum number of splits per read to be still taken into account. [7]
    -d <int>,  --max_distance <int>
        Maximum distance to group SV together. [1000]
    -t <int>,  --threads <int>
        Number of threads to use. [3]
    -l <int>,  --min_length <int>
        Minimum length of SV to be reported. [30]
    -q <int>,  --minmapping_qual <int>
        Minimum Mapping Quality. [20]
    -n <int>,  --num_reads_report <int>
        Report up to N reads that support the SV in the vcf file. -1: report all. [0]
    -r <int>,  --min_seq_size <int>
        Discard read if non of its segment is larger then this. [2000]
    -z <int>,  --min_zmw <int>
        Discard SV that are not supported by at least x zmws. This applies only for PacBio recognizable reads. [0]
    --cs_string
        Enables the scan of CS string instead of Cigar and MD.  [false]

Clustering/phasing and genotyping:
    --genotype
        Enables Sniffles to compute the genotypes. [false]
    --cluster
        Enables Sniffles to phase SVs that occur on the same reads [false]
    --cluster_support <int>
        Minimum number of reads supporting clustering of SV. [1]
    -f <float>,  --allelefreq <float>
        Threshold on allele frequency (0-1).  [0]
    --min_homo_af <float>
        Threshold on allele frequency (0-1).  [0.8]
    --min_het_af <float>
        Threshold on allele frequency (0-1).  [0.3]

Advanced:
    --report_BND
        Dont report BND instead use Tra in vcf output.  [true]
    --report_seq
        Report sequences for indels in vcf output. (Beta version!)  [false]
    --ignore_sd
        Ignores the sd based filtering.  [false]
    --report_read_strands
        Enables the report of the strand categories per read. (Beta)  [false]

Parameter estimation:
    --skip_parameter_estimation
        Enables the scan if only very few reads are present.  [false]
    --del_ratio <float>
        Estimated ration of deletions per read (0-1).  [0.0458369]
    --ins_ratio <float>
        Estimated ratio of insertions per read (0-1).  [0.049379]
    --max_diff_per_window <int>
        Maximum differences per 100bp. [50]
    --max_dist_aln_events <int>
        Maximum distance between alignment (indel) events. [4]

```


### run sniffles

```
$ sniffles --mapped_reads ERR2631603_MD.bam --vcf ERR2631603_MD.vcf --threads 10
```

```
Estimating parameter...
No MD string detected! Check bam file! Otherwise generate using e.g. samtools.
MD: TESTERR2631603.234537
```

when using minimap2 to align the reads, add tag **--MD**

of fix the MD tags using samtools

### samtools add MD tag
```
$ samtools calmd -b ERR2631603.bam /home/wzk/database/GENOME/human/Homo_sapiens.GRCh38.fa > ERR2631603_MD.bam

[bam_fillmd1] different NM for read 'ERR2631603.1117809': 2959 -> 6950
[bam_fillmd1] different NM for read 'ERR2631603.779272': 853 -> 1181
[bam_fillmd1] different NM for read 'ERR2631603.479136': 71 -> 206
[bam_fillmd1] different NM for read 'ERR2631603.835896': 488 -> 2319
[bam_fillmd1] different NM for read 'ERR2631603.17927': 87 -> 212


$ samtools index ERR2631603_MD.bam
```

```
$ sniffles --mapped_reads ERR2631603_MD.bam --vcf ERR2631603_MD.vcf --threads 10
Estimating parameter...
    Max dist between aln events: 5
    Max diff in window: 50
    Min score ratio: 2
    Avg DEL ratio: 0.073094
    Avg INS ratio: 0.0271722
Start parsing... 10
        # Processed reads: 10000

```


output file
```
##ALT=<ID=DEL,Description="Deletion">
##ALT=<ID=DUP,Description="Duplication">
##ALT=<ID=INV,Description="Inversion">
##ALT=<ID=INVDUP,Description="InvertedDUP with unknown boundaries">
##ALT=<ID=TRA,Description="Translocation">
##ALT=<ID=INS,Description="Insertion">
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=DR,Number=1,Type=Integer,Description="# high-quality reference reads">
##FORMAT=<ID=DV,Number=1,Type=Integer,Description="# high-quality variant reads">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  ERR2631603_MD.bam
10      367946  0       N       <DEL>   .       PASS    IMPRECISE;SVMETHOD=Snifflesv1.0.10;CHR2=10;END=368121;STD_quant_start=2
6.521689;STD_quant_stop=30.732719;Kurtosis_quant_start=0.912632;Kurtosis_quant_stop=-0.051291;SVTYPE=DEL;SUPTYPE=AL;SVLEN=-175;
STRANDS=+-;RE=12  GT:DR:DV        ./.:.:12
11      20233138        21      N       <INS>   .       PASS    IMPRECISE;SVMETHOD=Snifflesv1.0.10;CHR2=11;END=20233227;STD_quant_start=15.565989;STD_quant_stop=19.659603;Kurtosis_quant_start=-0.915712;Kurtosis_quant_stop=-0.411913;SVTYPE=INS;SUPTYPE=AL;SVLEN=84;STRANDS=+-;RE=11 GT:DR:DV        ./.:.:11
16      46387659        119     N       <DUP>   .       PASS    IMPRECISE;SVMETHOD=Snifflesv1.0.10;CHR2=16;END=46401496;STD_quant_start=265.209728;STD_quant_stop=148.992282;Kurtosis_quant_start=-1.199113;Kurtosis_quant_stop=-0.672207;SVTYPE=DUP;SUPTYPE=SR;SVLEN=13837;STRANDS=-+;RE=14    GT:DR:DV        ./.:.:14
22      11215487        713     N       N[4:49709080[   .       PASS    PRECISE;SVMETHOD=Snifflesv1.0.10;STD_quant_start=2.590468;STD_quant_stop=4.454448;Kurtosis_quant_start=10.027405;Kurtosis_quant_stop=-1.288220;SVTYPE=BND;SUPTYPE=SR;SVLEN=0;STRANDS=+-;RE=76   GT:DR:DV        ./.:.:76
22      11211033        712     N       ]3:93470362]N   .       PASS    PRECISE;SVMETHOD=Snifflesv1.0.10;STD_quant_start=0.766356;STD_quant_stop=0.000000;Kurtosis_quant_start=14.439894;Kurtosis_quant_stop=27.622305;SVTYPE=BND;SUPTYPE=SR;SVLEN=0;STRANDS=--;RE=126  GT:DR:DV        ./.:.:126

```
