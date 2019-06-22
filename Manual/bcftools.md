


### samtools  mpileup
```
$ samtools  mpileup

Usage: samtools mpileup [options] in1.bam [in2.bam [...]]

Input options:
  -6, --illumina1.3+      quality is in the Illumina-1.3+ encoding
  -A, --count-orphans     do not discard anomalous read pairs
  -b, --bam-list FILE     list of input BAM filenames, one per line
  -B, --no-BAQ            disable BAQ (per-Base Alignment Quality)
  -C, --adjust-MQ INT     adjust mapping quality; recommended:50, disable:0 [0]
  -d, --max-depth INT     max per-file depth; avoids excessive memory usage [8000]
  -E, --redo-BAQ          recalculate BAQ on the fly, ignore existing BQs
  -f, --fasta-ref FILE    faidx indexed reference sequence file
  -G, --exclude-RG FILE   exclude read groups listed in FILE
  -l, --positions FILE    skip unlisted positions (chr pos) or regions (BED)
  -q, --min-MQ INT        skip alignments with mapQ smaller than INT [0]
  -Q, --min-BQ INT        skip bases with baseQ/BAQ smaller than INT [13]
  -r, --region REG        region in which pileup is generated
  -R, --ignore-RG         ignore RG tags (one BAM = one sample)
  --rf, --incl-flags STR|INT  required flags: skip reads with mask bits unset []
  --ff, --excl-flags STR|INT  filter flags: skip reads with mask bits set
                                            [UNMAP,SECONDARY,QCFAIL,DUP]
  -x, --ignore-overlaps   disable read-pair overlap detection

Output options:
  -o, --output FILE       write output to FILE [standard output]
  -O, --output-BP         output base positions on reads
  -s, --output-MQ         output mapping quality
      --output-QNAME      output read names
  -a                      output all positions (including zero depth)
  -a -a (or -aa)          output absolutely all positions, including unused ref. sequences

Generic options:
      --input-fmt-option OPT[=VAL]
               Specify a single input file format option in the form
               of OPTION or OPTION=VALUE
      --reference FILE
               Reference sequence FASTA FILE [null]

Note that using "samtools mpileup" to generate BCF or VCF files is now
deprecated.  To output these formats, please use "bcftools mpileup" instead.
```


### bcftools mpileup
```
$ bcftools mpileup

Usage: bcftools mpileup [options] in1.bam [in2.bam [...]]

Input options:
  -6, --illumina1.3+      quality is in the Illumina-1.3+ encoding
  -A, --count-orphans     do not discard anomalous read pairs
  -b, --bam-list FILE     list of input BAM filenames, one per line
  -B, --no-BAQ            disable BAQ (per-Base Alignment Quality)
  -C, --adjust-MQ INT     adjust mapping quality; recommended:50, disable:0 [0]
  -d, --max-depth INT     max per-file depth; avoids excessive memory usage [250]
  -E, --redo-BAQ          recalculate BAQ on the fly, ignore existing BQs
  -f, --fasta-ref FILE    faidx indexed reference sequence file
      --no-reference      do not require fasta reference file
  -G, --read-groups FILE  select or exclude read groups listed in the file
  -q, --min-MQ INT        skip alignments with mapQ smaller than INT [0]
  -Q, --min-BQ INT        skip bases with baseQ/BAQ smaller than INT [13]
  -r, --regions REG[,...] comma separated list of regions in which pileup is generated
  -R, --regions-file FILE restrict to regions listed in a file
      --ignore-RG         ignore RG tags (one BAM = one sample)
  --rf, --incl-flags STR|INT  required flags: skip reads with mask bits unset []
  --ff, --excl-flags STR|INT  filter flags: skip reads with mask bits set
                                            [UNMAP,SECONDARY,QCFAIL,DUP]
  -s, --samples LIST      comma separated list of samples to include
  -S, --samples-file FILE file of samples to include
  -t, --targets REG[,...] similar to -r but streams rather than index-jumps
  -T, --targets-file FILE similar to -R but streams rather than index-jumps
  -x, --ignore-overlaps   disable read-pair overlap detection

Output options:
  -a, --annotate LIST     optional tags to output; '?' to list []
  -g, --gvcf INT[,...]    group non-variant sites into gVCF blocks according
                          to minimum per-sample DP
      --no-version        do not append version and command line to the header
  -o, --output FILE       write output to FILE [standard output]
  -O, --output-type TYPE  'b' compressed BCF; 'u' uncompressed BCF;
                          'z' compressed VCF; 'v' uncompressed VCF [v]
      --threads INT       number of extra output compression threads [0]

SNP/INDEL genotype likelihoods options:
  -e, --ext-prob INT      Phred-scaled gap extension seq error probability [20]
  -F, --gap-frac FLOAT    minimum fraction of gapped reads [0.002]
  -h, --tandem-qual INT   coefficient for homopolymer errors [100]
  -I, --skip-indels       do not perform indel calling
  -L, --max-idepth INT    maximum per-file depth for INDEL calling [250]
  -m, --min-ireads INT    minimum number gapped reads for indel candidates [1]
  -o, --open-prob INT     Phred-scaled gap open seq error probability [40]
  -p, --per-sample-mF     apply -m and -F per-sample for increased sensitivity
  -P, --platforms STR     comma separated list of platforms for indels [all]

Notes: Assuming diploid individuals.

```


### bcftools call
```
$ bcftools call

About:   SNP/indel variant calling from VCF/BCF. To be used in conjunction with samtools mpileup.
         This command replaces the former "bcftools view" caller. Some of the original
         functionality has been temporarily lost in the process of transition to htslib,
         but will be added back on popular demand. The original calling model can be
         invoked with the -c option.
Usage:   bcftools call [options] <in.vcf.gz>

File format options:
       --no-version                do not append version and command line to the header
   -o, --output <file>             write output to a file [standard output]
   -O, --output-type <b|u|z|v>     output type: 'b' compressed BCF; 'u' uncompressed BCF; 'z' compressed VCF; 'v' uncompressed VCF [v]
       --ploidy <assembly>[?]      predefined ploidy, 'list' to print available settings, append '?' for details
       --ploidy-file <file>        space/tab-delimited list of CHROM,FROM,TO,SEX,PLOIDY
   -r, --regions <region>          restrict to comma-separated list of regions
   -R, --regions-file <file>       restrict to regions listed in a file
   -s, --samples <list>            list of samples to include [all samples]
   -S, --samples-file <file>       PED file or a file with an optional column with sex (see man page for details) [all samples]
   -t, --targets <region>          similar to -r but streams rather than index-jumps
   -T, --targets-file <file>       similar to -R but streams rather than index-jumps
       --threads <int>             number of extra output compression threads [0]

Input/output options:
   -A, --keep-alts                 keep all possible alternate alleles at variant sites
   -f, --format-fields <list>      output format fields: GQ,GP (lowercase allowed) []
   -F, --prior-freqs <AN,AC>       use prior allele frequencies
   -g, --gvcf <int>,[...]          group non-variant sites into gVCF blocks by minimum per-sample DP
   -i, --insert-missed             output also sites missed by mpileup but present in -T
   -M, --keep-masked-ref           keep sites with masked reference allele (REF=N)
   -V, --skip-variants <type>      skip indels/snps
   -v, --variants-only             output variant sites only

Consensus/variant calling options:
   -c, --consensus-caller          the original calling method (conflicts with -m)
   -C, --constrain <str>           one of: alleles, trio (see manual)
   -m, --multiallelic-caller       alternative model for multiallelic and rare-variant calling (conflicts with -c)
   -n, --novel-rate <float>,[...]  likelihood of novel mutation for constrained trio calling, see man page for details [1e-8,1e-9,1e-9]
   -p, --pval-threshold <float>    variant if P(ref|D)<FLOAT with -c [0.5]
   -P, --prior <float>             mutation rate (use bigger for greater sensitivity), use with -m [1.1e-3]


```


### [bcftools HOWTO](https://github.com/samtools/bcftools/wiki/HOWTOs)


### example
```
$ bcftools mpileup  --fasta-ref   /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa  bam/M625-0_sorted_chr1.bam bam/M625-1_sorted_chr1.bam bam/M625-2_sorted_chr1.bam  | bcftools call --output-type  v --consensus-caller --variants-only  --constrain trio > M625.vcf
```


```
$ bcftools mpileup -O u  --fasta-ref   /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa  bam/M625-0_sorted_chr1.bam bam/M625-1_sorted_chr1.bam bam/M625-2_sorted_chr1.bam  | bcftools call --output-type  v --consensus-caller --variants-only  --constrain trio > M625.vcf
```


### extract bam
```
$ samtools view -b --threads 10 -o M625-0_chr21.bam  M625-0/M625-0.bqsr.bam   21
```

```
$ bcftools mpileup -O u --threads 10   --fasta-ref   /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa   bam/M625-0_chr21.bam bam/M625-1_chr21.bam bam/M625-2_chr21.bam  | bcftools call --output-type  v --consensus-caller --variants-only  --constrain trio > M625_chr21.vcf
```


### bcftools target regions
```
bcftools mpileup -O u --threads 10  --regions 21:10-6020119  --fasta-ref   /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  M625-2_chr21.bam   | bcftools call --output-type  v --consensus-caller --variants-only  --constrain trio --format-fields GQ  > M625_chr21.vcf 
```

```
$ bcftools mpileup -O u --threads 10  --targets-file /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all.dnm.filtCentromere_sites.bed   --fasta-ref   /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  M625-2_chr21.bam   | bcftools call --output-type  v --consensus-caller --variants-only  --constrain trio --format-fields GQ   > M625_chr21.vcf
```


```
bcftools filter -i 'FORMAT/GT=="1/1"' ./mysnps.bcf | less

bcftools filter -i "%QUAL>30" ./mysnps.bcf 
```


```
##### ERROR MESSAGE: Could not read file /home/wuzhikun/Project/Illumina_Trio/Trio/temp_regions.txt because The interval file temp_regions.txt does not have one of the supported extensions (.bed, .list, .picard, .interval_list, or .intervals). Please rename your file with the appropriate extension. If temp_regions.txt is NOT supposed to be a file, please move or rename the file at location /home/wuzhikun/Project/Illumina_Trio/Trio/temp_regions.txt
```