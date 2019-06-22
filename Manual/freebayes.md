

### freebayes parameters
```
$ freebayes --help
usage: freebayes [OPTION] ... [BAM FILE] ... 

Bayesian haplotype-based polymorphism discovery.

citation: Erik Garrison, Gabor Marth
          "Haplotype-based variant detection from short-read sequencing"
          arXiv:1207.3907 (http://arxiv.org/abs/1207.3907)

overview:

    To call variants from aligned short-read sequencing data, supply BAM files and
    a reference.  FreeBayes will provide VCF output on standard out describing SNPs,
    indels, and complex variants in samples in the input alignments.

    By default, FreeBayes will consider variants supported by at least 2
    observations in a single sample (-C) and also by at least 20% of the reads from
    a single sample (-F).  These settings are suitable to low to high depth
    sequencing in haploid and diploid samples, but users working with polyploid or
    pooled samples may wish to adjust them depending on the characteristics of
    their sequencing data.

    FreeBayes is capable of calling variant haplotypes shorter than a read length
    where multiple polymorphisms segregate on the same read.  The maximum distance
    between polymorphisms phased in this way is determined by the
    --max-complex-gap, which defaults to 3bp.  In practice, this can comfortably be
    set to half the read length.

    Ploidy may be set to any level (-p), but by default all samples are assumed to
    be diploid.  FreeBayes can model per-sample and per-region variation in
    copy-number (-A) using a copy-number variation map.

    FreeBayes can act as a frequency-based pooled caller and describe variants
    and haplotypes in terms of observation frequency rather than called genotypes.
    To do so, use --pooled-continuous and set input filters to a suitable level.
    Allele observation counts will be described by AO and RO fields in the VCF output.


examples:

    # call variants assuming a diploid sample
    freebayes -f ref.fa aln.bam >var.vcf

    # call variants assuming a diploid sample, providing gVCF output
    freebayes -f ref.fa --gvcf aln.bam >var.gvcf

    # require at least 5 supporting observations to consider a variant
    freebayes -f ref.fa -C 5 aln.bam >var.vcf

    # use a different ploidy
    freebayes -f ref.fa -p 4 aln.bam >var.vcf

    # assume a pooled sample with a known number of genome copies
    freebayes -f ref.fa -p 20 --pooled-discrete aln.bam >var.vcf

    # generate frequency-based calls for all variants passing input thresholds
    freebayes -f ref.fa -F 0.01 -C 1 --pooled-continuous aln.bam >var.vcf

    # use an input VCF (bgzipped + tabix indexed) to force calls at particular alleles
    freebayes -f ref.fa -@ in.vcf.gz aln.bam >var.vcf

    # generate long haplotype calls over known variants
    freebayes -f ref.fa --haplotype-basis-alleles in.vcf.gz \ 
                        --haplotype-length 50 aln.bam

    # naive variant calling: simply annotate observation counts of SNPs and indels
    freebayes -f ref.fa --haplotype-length 0 --min-alternate-count 1 \ 
        --min-alternate-fraction 0 --pooled-continuous --report-monomorphic >var.vcf


parameters:

   -h --help       Prints this help dialog.
   --version       Prints the release number and the git commit id.

input:

   -b --bam FILE   Add FILE to the set of BAM files to be analyzed.
   -L --bam-list FILE
                   A file containing a list of BAM files to be analyzed.
   -c --stdin      Read BAM input on stdin.
   -f --fasta-reference FILE
                   Use FILE as the reference sequence for analysis.
                   An index file (FILE.fai) will be created if none exists.
                   If neither --targets nor --region are specified, FreeBayes
                   will analyze every position in this reference.
   -t --targets FILE
                   Limit analysis to targets listed in the BED-format FILE.
   -r --region <chrom>:<start_position>-<end_position>
                   Limit analysis to the specified region, 0-base coordinates,
                   end_position not included (same as BED format).
                   Either '-' or '..' maybe used as a separator.
   -s --samples FILE
                   Limit analysis to samples listed (one per line) in the FILE.
                   By default FreeBayes will analyze all samples in its input
                   BAM files.
   --populations FILE
                   Each line of FILE should list a sample and a population which
                   it is part of.  The population-based bayesian inference model
                   will then be partitioned on the basis of the populations.
   -A --cnv-map FILE
                   Read a copy number map from the BED file FILE, which has
                   either a sample-level ploidy:
                      sample name, copy number
                   or a region-specific format:
                      reference sequence, start, end, sample name, copy number
                   ... for each region in each sample which does not have the
                   default copy number as set by --ploidy.

output:

   -v --vcf FILE   Output VCF-format results to FILE. (default: stdout)
   --gvcf
                   Write gVCF output, which indicates coverage in uncalled regions.
   --gvcf-chunk NUM
                   When writing gVCF output emit a record for every NUM bases.
   -@ --variant-input VCF
                   Use variants reported in VCF file as input to the algorithm.
                   Variants in this file will included in the output even if
                   there is not enough support in the data to pass input filters.
   -l --only-use-input-alleles
                   Only provide variant calls and genotype likelihoods for sites
                   and alleles which are provided in the VCF input, and provide
                   output in the VCF for all input alleles, not just those which
                   have support in the data.
   --haplotype-basis-alleles VCF
                   When specified, only variant alleles provided in this input
                   VCF will be used for the construction of complex or haplotype
                   alleles.
   --report-all-haplotype-alleles
                   At sites where genotypes are made over haplotype alleles,
                   provide information about all alleles in output, not only
                   those which are called.
   --report-monomorphic
                   Report even loci which appear to be monomorphic, and report all
                   considered alleles, even those which are not in called genotypes.
                   Loci which do not have any potential alternates have '.' for ALT.
   -P --pvar N     Report sites if the probability that there is a polymorphism
                   at the site is greater than N.  default: 0.0.  Note that post-
                   filtering is generally recommended over the use of this parameter.
   --strict-vcf
                   Generate strict VCF format (FORMAT/GQ will be an int)

population model:

   -T --theta N    The expected mutation rate or pairwise nucleotide diversity
                   among the population under analysis.  This serves as the
                   single parameter to the Ewens Sampling Formula prior model
                   default: 0.001
   -p --ploidy N   Sets the default ploidy for the analysis to N.  default: 2
   -J --pooled-discrete
                   Assume that samples result from pooled sequencing.
                   Model pooled samples using discrete genotypes across pools.
                   When using this flag, set --ploidy to the number of
                   alleles in each sample or use the --cnv-map to define
                   per-sample ploidy.
   -K --pooled-continuous
                   Output all alleles which pass input filters, regardles of
                   genotyping outcome or model.

reference allele:

   -Z --use-reference-allele
                   This flag includes the reference allele in the analysis as
                   if it is another sample from the same population.
   --reference-quality MQ,BQ
                   Assign mapping quality of MQ to the reference allele at each
                   site and base quality of BQ.  default: 100,60

allele scope:

   -I --no-snps    Ignore SNP alleles.
   -i --no-indels  Ignore insertion and deletion alleles.
   -X --no-mnps    Ignore multi-nuceotide polymorphisms, MNPs.
   -u --no-complex Ignore complex events (composites of other classes).
   -n --use-best-n-alleles N
                   Evaluate only the best N SNP alleles, ranked by sum of
                   supporting quality scores.  (Set to 0 to use all; default: all)
   -E --max-complex-gap N
      --haplotype-length N
                   Allow haplotype calls with contiguous embedded matches of up
                   to this length. Set N=-1 to disable clumping. (default: 3)
   --min-repeat-size N
                   When assembling observations across repeats, require the total repeat
                   length at least this many bp.  (default: 5)
   --min-repeat-entropy N
                   To detect interrupted repeats, build across sequence until it has
                   entropy > N bits per bp. Set to 0 to turn off. (default: 1)
   --no-partial-observations
                   Exclude observations which do not fully span the dynamically-determined
                   detection window.  (default, use all observations, dividing partial
                   support across matching haplotypes when generating haplotypes.)

indel realignment:

   -O --dont-left-align-indels
                   Turn off left-alignment of indels, which is enabled by default.

input filters:

   -4 --use-duplicate-reads
                   Include duplicate-marked alignments in the analysis.
                   default: exclude duplicates marked as such in alignments
   -m --min-mapping-quality Q
                   Exclude alignments from analysis if they have a mapping
                   quality less than Q.  default: 1
   -q --min-base-quality Q
                   Exclude alleles from analysis if their supporting base
                   quality is less than Q.  default: 0
   -R --min-supporting-allele-qsum Q
                   Consider any allele in which the sum of qualities of supporting
                   observations is at least Q.  default: 0
   -Y --min-supporting-mapping-qsum Q
                   Consider any allele in which and the sum of mapping qualities of
                   supporting reads is at least Q.  default: 0
   -Q --mismatch-base-quality-threshold Q
                   Count mismatches toward --read-mismatch-limit if the base
                   quality of the mismatch is >= Q.  default: 10
   -U --read-mismatch-limit N
                   Exclude reads with more than N mismatches where each mismatch
                   has base quality >= mismatch-base-quality-threshold.
                   default: ~unbounded
   -z --read-max-mismatch-fraction N
                   Exclude reads with more than N [0,1] fraction of mismatches where
                   each mismatch has base quality >= mismatch-base-quality-threshold
                   default: 1.0
   -$ --read-snp-limit N
                   Exclude reads with more than N base mismatches, ignoring gaps
                   with quality >= mismatch-base-quality-threshold.
                   default: ~unbounded
   -e --read-indel-limit N
                   Exclude reads with more than N separate gaps.
                   default: ~unbounded
   -0 --standard-filters  Use stringent input base and mapping quality filters
                   Equivalent to -m 30 -q 20 -R 0 -S 0
   -F --min-alternate-fraction N
                   Require at least this fraction of observations supporting
                   an alternate allele within a single individual in the
                   in order to evaluate the position.  default: 0.05
   -C --min-alternate-count N
                   Require at least this count of observations supporting
                   an alternate allele within a single individual in order
                   to evaluate the position.  default: 2
   -3 --min-alternate-qsum N
                   Require at least this sum of quality of observations supporting
                   an alternate allele within a single individual in order
                   to evaluate the position.  default: 0
   -G --min-alternate-total N
                   Require at least this count of observations supporting
                   an alternate allele within the total population in order
                   to use the allele in analysis.  default: 1
   --min-coverage N
                   Require at least this coverage to process a site. default: 0
   --max-coverage N
                   Do not process sites with greater than this coverage. default: no limit

population priors:

   -k --no-population-priors
                   Equivalent to --pooled-discrete --hwe-priors-off and removal of
                   Ewens Sampling Formula component of priors.

mappability priors:

   -w --hwe-priors-off
                   Disable estimation of the probability of the combination
                   arising under HWE given the allele frequency as estimated
                   by observation frequency.
   -V --binomial-obs-priors-off
                   Disable incorporation of prior expectations about observations.
                   Uses read placement probability, strand balance probability,
                   and read position (5'-3') probability.
   -a --allele-balance-priors-off
                   Disable use of aggregate probability of observation balance between alleles
                   as a component of the priors.

genotype likelihoods:

   --observation-bias FILE
                   Read length-dependent allele observation biases from FILE.
                   The format is [length] [alignment efficiency relative to reference]
                   where the efficiency is 1 if there is no relative observation bias.
   --base-quality-cap Q
                   Limit estimated observation quality by capping base quality at Q.
   --prob-contamination F
                   An estimate of contamination to use for all samples.  default: 10e-9
   --legacy-gls    Use legacy (polybayes equivalent) genotype likelihood calculations
   --contamination-estimates FILE
                   A file containing per-sample estimates of contamination, such as
                   those generated by VerifyBamID.  The format should be:
                       sample p(read=R|genotype=AR) p(read=A|genotype=AA)
                   Sample '*' can be used to set default contamination estimates.

algorithmic features:

   --report-genotype-likelihood-max
                   Report genotypes using the maximum-likelihood estimate provided
                   from genotype likelihoods.
   -B --genotyping-max-iterations N
                   Iterate no more than N times during genotyping step. default: 1000.
   --genotyping-max-banddepth N
                   Integrate no deeper than the Nth best genotype by likelihood when
                   genotyping. default: 6.
   -W --posterior-integration-limits N,M
                   Integrate all genotype combinations in our posterior space
                   which include no more than N samples with their Mth best
                   data likelihood. default: 1,3.
   -N --exclude-unobserved-genotypes
                   Skip sample genotypings for which the sample has no supporting reads.
   -S --genotype-variant-threshold N
                   Limit posterior integration to samples where the second-best
                   genotype likelihood is no more than log(N) from the highest
                   genotype likelihood for the sample.  default: ~unbounded
   -j --use-mapping-quality
                   Use mapping quality of alleles when calculating data likelihoods.
   -H --harmonic-indel-quality
                   Use a weighted sum of base qualities around an indel, scaled by the
                   distance from the indel.  By default use a minimum BQ in flanking sequence.
   -D --read-dependence-factor N
                   Incorporate non-independence of reads by scaling successive
                   observations by this factor during data likelihood
                   calculations.  default: 0.9
   -= --genotype-qualities
                   Calculate the marginal probability of genotypes and report as GQ in
                   each sample field in the VCF output.

debugging:

   -d --debug      Print debugging output.
   -dd             Print more verbose debugging output (requires "make DEBUG")


author:   Erik Garrison <erik.garrison@bc.edu>, Marth Lab, Boston College, 2010-2014
version:  v1.2.0-dirty
```



### run freebayes to get gvcf
```
freebayes -f /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --region 1:1-100000 --gvcf  /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam > temp.gvcf
```


### run freebayes to get vcf file
```
freebayes -f chr20.fa --region 20:1000000-2000000 \
    NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam >NA12878.chr20.1mb_2mb.freebayes.vcf
```


#### error for the RG ID of multiple samples

```
$ freebayes  -f /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -r 1:1-300000 -v temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam
ERROR(freebayes): multiple samples (SM) map to the same read group (RG)

samples M625-0 and M625-1 map to 1

As freebayes operates on a virtually merged stream of its input files,
it will not be possible to determine what sample an alignment belongs to
at runtime.

To resolve the issue, ensure that RG ids are unique to one sample
across all the input files to freebayes.

See bamaddrg (https://github.com/ekg/bamaddrg) for a method which can
add RG tags to alignments.

```


```
$ samtools view -H /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam  | grep ^@RG
@RG	ID:1	LB:M625-0	PL:Illumina	SM:M625-0	PU:M625-0

$ samtools view -H /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam  | grep ^@RG
@RG	ID:1	LB:M625-1	PL:Illumina	SM:M625-1	PU:M625-1

```


#### change RG ID
```
$ java -jar /home/wuzhikun/anaconda3/envs/WGS/bin/picard.jar  AddOrReplaceReadGroups INPUT=M625-0.bqsr.bam OUTPUT=M625-0.bqsr_temp.bam SORT_ORDER=coordinate RGID=M625-0  RGPL=Illumina RGLB=M625-0 RGPU=M625-0  RGSM=M625-0

$ samtools view -H /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr_temp.bam  | grep ^@RG
@RG	ID:M625-0	LB:M625-0	PL:Illumina	SM:M625-0	PU:M625-0

```



#### freebayes for multiple samples
```
$ freebayes  -f /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -r 1:1-300000 -v temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr_temp.bam

```


