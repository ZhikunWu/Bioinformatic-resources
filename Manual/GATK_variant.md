
## [Tumor Variant Calling](https://www.cell.com/cancer-cell/fulltext/S1535-6108(18)30306-4)

We have used Picard (version 1.87) and the Genome Analysis Toolkit (GATK, version 3.4.46) (McKenna et al., 2010) for variant calling. We followed the good-practice guidelines for variant calling with GATK (Van der Auwera et al., 2013). We omitted a duplicate-marking of the input files as the alignment versions downloaded from CGHub already had duplicates marked. Each alignment file was then stripped of all unmapped reads and re-indexed using samtools (version 1.2).
Utilizing the capture-region information for the exome capture procedure of each file and dbSNP (version 138), the 1000 Genome Project Phase 1 and the Mills and 1000G gold standard set as compendium of known sites, we used GATK for base quality score re-calibration.

### Re-calibration Step 1

```
java -jar GenomeAnalysisTK.jar -T BaseRecalibrator -R <genome.fasta> -I <alignment.bam> -knownSites <known_sites> -L <capture_region> -o <outfile1> -nct <threads>
```

### Re-calibration Step 2
```
java -jar GenomeAnalysisTK.jar -T PrintReads -R <genome.fasta> -I <alignment.bam> -BQSR <outfile1> -o <outfile2> -nct <threads>
```

Variant calling was then performed using the GATK Haplotype Caller. The calling limit was defined as a +/− 1kb window around all genes in the GENCODE annotation (v19), including all intron regions.


### Variant Calling

```
java -Xmx4g -Xms512m -Djava.io.tmpdir=<TMPDIR> -jar GenomeAnalysisTK.jar -T HaplotypeCaller -R <genome.fasta> -I <alignment.bam> --dbsnp <dbsnp_v138.vcf> -o <outfile> --output_mode EMIT_ALL_CONFIDENT_SITES -ERC GVCF --variant_index_type LINEAR --variant_index_parameter 128000 -pairHMM VECTOR_LOGLESS_CACHING -mbq 15 --minPruning 5 -S STRICT --activeRegionOut <outfile_region> --activityProfileOut <outfile_profile> -L <calling_limit.bed> -nct <threads>
```

The gVCF files created in the previous step for each sample were then merged in an iterative process until less than 100 merged files remained:
```
java -jar GenomeAnalysisTK.jar -T CombineGVCFs -R <genome.fasta> --variant <s1> … --variant <sN> -o <outfile_merged1>
```

The merged gVCF files were then used for joint variant calling on each chromosome independently using the GATK:
```
java -Xmx16g -jar GenomeAnalysisTK.jar -T GenotypeGVCFs -L <chr> -nt <threads> --dbsnp <dbsnp_v138.vcf> -R <genome.fasta> --variant <outfile_merged1> … --variant <outfile_mergedN> -o <outfile_final>
```


### Tumor Variant Filtering
Tumor variant calls have been filtered in the following way: Variants that have less than 100 samples with valid calls, quality of less than 100, are multi-allelic or indels have been removed from analysis. We further required more than 5 alternate alleles for each polymorphic position. All variants have been encoded into an additive scheme with 0 representing the homozygous reference state, 1 the heterozygous state and 2 the homozygous alternate allele. In this study, we ignore the existence of variants that appear sub-clonally. For somatic variant calls the unfiltered MC3 calls from PanCanAtlas have been used (version 0.2.8; Synapse ID: syn7834470). From that variant call set we extracted single nucleotide variants (SNVs) but excluded variants tagged by the following criteria:
```
StrandBias
contest
oxog
ndp
pcadontuse
nonpreferredpair
badseq
gapfiller
common_in_exac
PoN
```

We also required that at least three variant callers agree on a variant call and excluded variants which have a higher than 5% minor allele frequency in the 1,000 genomes cohort. Non-recurrent variant calls (variants which appear in only one sample) have also been excluded from further analysis. This filtering ensures a high-quality variant call set which includes intronic variants at exon boundaries.
The somatic and tumor variant calls have subsequently been intersected, resulting in a total of 4,041 variant calls considered in this analysis.


