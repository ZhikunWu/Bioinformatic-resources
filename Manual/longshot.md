## [longshot](https://github.com/pjedge/longshot)

### longshot parameters
```
$ longshot

error: The following required arguments were not provided:
    --bam <BAM>
    --ref <FASTA>
    --out <VCF>

USAGE:
    longshot --anchor_length <int> --band_width <Band width> --density_params <string> --hap_converge_delta <float> --hap_assignment_qual <float> --het_snv_rate <float> --hom_snv_rate <float> --bam <BAM> --ref <FASTA> --max_cigar_indel <int> --max_cov <int> --max_window <int> --min_allele_qual <float> --min_cov <int> --min_mapq <int> --out <VCF> --potential_snv_cutoff <float> --min_alt_count <int> --min_alt_frac <float> --sample_id <string> --strand_bias_pvalue_cutoff <float> --max_snvs <int> --ts_tv_ratio <float>

For more information try --help

```



```
$ longshot --help

Longshot 0.3.5
Peter Edge <edge.peterj@gmail.com>
SNV caller for Third-Generation Sequencing reads

USAGE:
    longshot [FLAGS] [OPTIONS] --bam <BAM> --ref <FASTA> --out <VCF>

FLAGS:
    -A, --auto_max_cov        Automatically calculate mean coverage for region and set max coverage to mean_coverage +
                              5*sqrt(mean_coverage). (SLOWER)
    -S, --stable_alignment    Use numerically-stable (logspace) pair HMM forward algorithm. Is significantly slower but
                              may be more accurate. Tests have shown this not to be necessary for highly error prone
                              reads (PacBio CLR).
    -F, --force_overwrite     If output files (VCF or variant debug directory) exist, delete and overwrite them.
    -x, --max_alignment       Use max scoring alignment algorithm rather than pair HMM forward algorithm.
    -n, --no_haps             Don't call HapCUT2 to phase variants.
    -h, --help                Prints help information
    -V, --version             Prints version information

OPTIONS:
    -b, --bam <BAM>                            sorted, indexed BAM file with error-prone reads
    -f, --ref <FASTA>                          indexed FASTA reference that BAM file is aligned to
    -o, --out <VCF>                            output VCF file with called variants.
    -r, --region <string>                      Region in format <chrom> or <chrom:start-stop> in which to call variants
                                               (1-based, inclusive).
    -p, --hap_bam_prefix <BAM>                 Write haplotype-separated reads to 3 bam files using this prefix:
                                               <prefix>.hap1.bam, <prefix>.hap2.bam, <prefix>.unassigned.bam
    -c, --min_cov <int>                        Minimum coverage (of reads passing filters) to consider position as a
                                               potential SNV. [default: 6]
    -C, --max_cov <int>                        Maximum coverage (of reads passing filters) to consider position as a
                                               potential SNV. [default: 8000]
    -q, --min_mapq <int>                       Minimum mapping quality to use a read. [default: 30]
    -a, --min_allele_qual <float>              Minimum estimated quality (Phred-scaled) of allele observation on read to
                                               use for genotyping/haplotyping. [default: 7.0]
    -y, --hap_assignment_qual <float>          Minimum quality (Phred-scaled) of read->haplotype assignment (for read
                                               separation). [default: 20.0]
    -Q, --potential_snv_cutoff <float>         Consider a site as a potential SNV if the original PHRED-scaled QUAL
                                               score for 0/0 genotype is below this amount (a larger value considers
                                               more potential SNV sites). [default: 20.0]
    -e, --min_alt_count <int>                  Require a potential SNV to have at least this many alternate allele
                                               observations. [default: 3]
    -E, --min_alt_frac <float>                 Require a potential SNV to have at least this fraction of alternate
                                               allele observations. [default: 0.125]
    -L, --hap_converge_delta <float>           Terminate the haplotype/genotype iteration when the relative change in
                                               log-likelihood falls below this amount. Setting a larger value results in
                                               faster termination but potentially less accurate results. [default:
                                               0.0001]
    -l, --anchor_length <int>                  Length of indel-free anchor sequence on the left and right side of read
                                               realignment window. [default: 6]
    -m, --max_snvs <int>                       Cut off variant clusters after this many variants. 2^m haplotypes must be
                                               aligned against per read for a variant cluster of size m. [default: 3]
    -W, --max_window <int>                     Maximum "padding" bases on either side of variant realignment window
                                               [default: 50]
    -I, --max_cigar_indel <int>                Throw away a read-variant during allelotyping if there is a CIGAR indel
                                               (I/D/N) longer than this amount in its window. [default: 20]
    -B, --band_width <Band width>              Minimum width of alignment band. Band will increase in size if sequences
                                               are different lengths. [default: 20]
    -D, --density_params <string>              Parameters to flag a variant as part of a "dense cluster". Format
                                               <n>:<l>:<gq>. If there are at least n variants within l base pairs with
                                               genotype quality >=gq, then these variants are flagged as "dn" [default:
                                               10:500:50]
    -s, --sample_id <string>                   Specify a sample ID to write to the output VCF [default: SAMPLE]
        --hom_snv_rate <float>                 Specify the homozygous SNV Rate for genotype prior estimation [default:
                                               0.0005]
        --het_snv_rate <float>                 Specify the heterozygous SNV Rate for genotype prior estimation [default:
                                               0.001]
        --ts_tv_ratio <float>                  Specify the transition/transversion rate for genotype grior estimation
                                               [default: 0.5]
    -P, --strand_bias_pvalue_cutoff <float>    Remove a variant if the allele observations are biased toward one strand
                                               (forward or reverse) according to Fisher's exact test. Use this cutoff
                                               for the two-tailed P-value. [default: 0.01]
    -d, --variant_debug_dir <path>             write out current information about variants at each step of algorithm to
                                               files in this directory

```



### run longshot

```
longshot --auto_max_cov  --bam M671-2.bam --ref /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --out  M671-2_chr1.vcf --region 1

2019-10-19 09:41:11 Automatically determining max read coverage.
2019-10-19 09:41:11 Estimating mean read coverage...
2019-10-19 09:48:25 Total reference positions: 248956422
2019-10-19 09:48:25 Total bases in bam: 6824551296
2019-10-19 09:48:25 Mean read coverage: 27.41
2019-10-19 09:48:25 Min read coverage set to 6.
2019-10-19 09:48:25 Max read coverage set to 53.
2019-10-19 09:48:25 Estimating alignment parameters...
2019-10-19 09:52:08 Done estimating alignment parameters.

                    Transition Probabilities:
                    match -> match:          0.942
                    match -> insertion:      0.026
                    match -> deletion:       0.032
                    deletion -> match:       0.648
                    deletion -> deletion:    0.352
                    insertion -> match:      0.635
                    insertion -> insertion:  0.365

                    Emission Probabilities:
                    match (equal):           0.956
                    match (not equal):       0.015
                    insertion:               1.000
                    deletion:                1.000

                    GENOTYPE PRIORS:
                    REF G1/G2 PROB
                    C D/I 0
                    G A/A 0.00016666692910805806
                    G D/I 0
                    T T/T 0.9985001541646916


```

