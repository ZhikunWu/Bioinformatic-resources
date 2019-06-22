## samtools

### split bam files
view header of bam
```
samtools view -H T01.sorted.bam
```

eidt the header
```
for BAM in *.bam
do
     samtools view -H $BAM > header.sam
     sed "s/Solid5500XL/Solid/" header.sam > header_corrected.sam
     samtools reheader  header_corrected.sam $BAM
done
```
or 
```
samtools view -H $BAM | sed "s/Solid5500XL/Solid/" | samtools reheader - $BAM
```


```
samtools view in.bam chr1 -b > out.bam
```

```
bamtools split -in file.bam -reference
```


### samtools functions
```
samtools view -bt ref_list.txt -o aln.bam aln.sam.gz

samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam

samtools index aln.sorted.bam

samtools idxstats aln.sorted.bam

samtools flagstat aln.sorted.bam

samtools stats aln.sorted.bam

samtools bedcov aln.sorted.bam

samtools depth aln.sorted.bam

samtools view aln.sorted.bam chr2:20,100,000-20,200,000

samtools merge out.bam in1.bam in2.bam in3.bam

samtools faidx ref.fasta

samtools tview aln.sorted.bam ref.fasta

samtools split merged.bam

samtools quickcheck in1.bam in2.cram

samtools dict -a GRCh38 -s "Homo sapiens" ref.fasta

samtools fixmate in.namesorted.sam out.bam

samtools mpileup -C50 -gf ref.fasta -r chr3:1,000-2,000 in1.bam in2.bam

samtools flags PAIRED,UNMAP,MUNMAP

samtools fastq input.bam > output.fastq

samtools fasta input.bam > output.fasta

samtools addreplacerg -r 'ID:fish' -r 'LB:1334' -r 'SM:alpha' -o output.bam input.bam

samtools collate aln.sorted.bam aln.name_collated.bam

samtools depad input.bam

samtools markdup in.algnsorted.bam out.bam
```




### samtools mpileup

```
$ samtools mpileup

Usage: samtools mpileup [options] in1.bam [in2.bam [...]]

Input options:
  -6, --illumina1.3+      quality is in the Illumina-1.3+ encoding
  -A, --count-orphans     do not discard anomalous read pairs
  -b, --bam-list FILE     list of input BAM filenames, one per line
  -B, --no-BAQ            disable BAQ (per-Base Alignment Quality)
  -C, --adjust-MQ INT     adjust mapping quality; recommended:50, disable:0 [0]
  -d, --max-depth INT     max per-file depth; avoids excessive memory usage [250]
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
  -g, --BCF               generate genotype likelihoods in BCF format
  -v, --VCF               generate genotype likelihoods in VCF format

Output options for mpileup format (without -g/-v):
  -O, --output-BP         output base positions on reads
  -s, --output-MQ         output mapping quality

Output options for genotype likelihoods (when -g/-v is used):
  -t, --output-tags LIST  optional tags to output:
               DP,AD,ADF,ADR,SP,INFO/AD,INFO/ADF,INFO/ADR []
  -u, --uncompressed      generate uncompressed VCF/BCF output

SNP/INDEL genotype likelihoods options (effective with -g/-v):
  -e, --ext-prob INT      Phred-scaled gap extension seq error probability [20]
  -F, --gap-frac FLOAT    minimum fraction of gapped reads [0.002]
  -h, --tandem-qual INT   coefficient for homopolymer errors [100]
  -I, --skip-indels       do not perform indel calling
  -L, --max-idepth INT    maximum per-file depth for INDEL calling [250]
  -m, --min-ireads INT    minimum number gapped reads for indel candidates [1]
  -o, --open-prob INT     Phred-scaled gap open seq error probability [40]
  -p, --per-sample-mF     apply -m and -F per-sample for increased sensitivity
  -P, --platforms STR     comma separated list of platforms for indels [all]
      --input-fmt-option OPT[=VAL]
               Specify a single input file format option in the form
               of OPTION or OPTION=VALUE
      --reference FILE
               Reference sequence FASTA FILE [null]

Notes: Assuming diploid individuals.

```

### merge vcf
```
bcftools merge  -m both -o merged.vcf.gz A.vcf.gz B.vcf.gz ...


$ bcftools merge

About:   Merge multiple VCF/BCF files from non-overlapping sample sets to create one multi-sample file.
         Note that only records from different files can be merged, never from the same file. For
         "vertical" merge take a look at "bcftools norm" instead.
Usage:   bcftools merge [options] <A.vcf.gz> <B.vcf.gz> [...]

Options:
        --force-samples                resolve duplicate sample names
        --print-header                 print only the merged header and exit
        --use-header <file>            use the provided header
    -0  --missing-to-ref               assume genotypes at missing sites are 0/0
    -f, --apply-filters <list>         require at least one of the listed FILTER strings (e.g. "PASS,.")
    -F, --filter-logic <x|+>           remove filters if some input is PASS ("x"), or apply all filters ("+") [+]
    -g, --gvcf <-|ref.fa>              merge gVCF blocks, INFO/END tag is expected. Implies -i QS:sum,MinDP:min,I16:sum,IDV:max,IMF:max
    -i, --info-rules <tag:method,..>   rules for merging INFO fields (method is one of sum,avg,min,max,join) or "-" to turn off the default [DP:sum,DP4:sum]
    -l, --file-list <file>             read file names from the file
    -m, --merge <string>               allow multiallelic records for <snps|indels|both|all|none|id>, see man page for details [both]
        --no-version                   do not append version and command line to the header
    -o, --output <file>                write output to a file [standard output]
    -O, --output-type <b|u|z|v>        'b' compressed BCF; 'u' uncompressed BCF; 'z' compressed VCF; 'v' uncompressed VCF [v]
    -r, --regions <region>             restrict to comma-separated list of regions
    -R, --regions-file <file>          restrict to regions listed in a file
        --threads <int>                number of extra output compression threads [0]

```



### get partial bam file
```
samtools view T01.sorted.bam TGACv1_scaffold_576745_7BL -b > /home/wzk/BSA_wheat/mapping/partial/T01_partial.sorted.bam
```



### call snp
```
$ samtools mpileup -ugf /home/wzk/database/GENOME/wheat/161010_Chinese_Spring_v1.0_pseudomolecules.fasta  -t AD -t DP -t SP T01_dedupped.bam |bcftools call -vmO z -o T01_dedupped.vcf.gz
```
