### [denovogear](https://github.com/denovogear/denovogear): A program to detect denovo-variants using next-generation sequencing data

### [COBASI](https://github.com/Laura-Gomez/COBASI): accurate identification of de novo Single Nucleotide Variants from sequencing data

### [denovo-db](http://denovo-db.gs.washington.edu)

### GATK de novo

#### [Discover variants with GATK](https://gatkforums.broadinstitute.org/gatk/discussion/7869/howto-discover-variants-with-gatk-a-gatk-workshop-tutorial)

#### [PossibleDeNovo](https://software.broadinstitute.org/gatk/documentation/tooldocs/3.8-0/org_broadinstitute_gatk_tools_walkers_annotator_PossibleDeNovo.php)




### [Trio Calling for de novo Mutations](http://varscan.sourceforge.net/trio-calling-de-novo-mutations.html)
```
Trio Calling Syntax
Trio calling with VarScan 2 is a two-step process.
1. Generate a three-sample mpileup
Here's an example command:
samtools mpileup -B -q 1 -f ref.fasta dad.bam mom.bam child.bam >trio.mpileup

2. Run VarScan trio
Here's the syntax for the VarScan subcommand:
java -jar VarScan.jar trio trio.mpileup trio.mpileup.output \
      --min-coverage 10 --min-var-freq 0.20 --p-value 0.05 \ 
      -adj-var-freq 0.05 -adj-p-value 0.15
```




### [Finding de novo variants from trio](https://gatkforums.broadinstitute.org/gatk/discussion/1233/finding-de-novo-variants-from-trio)
```
java -jar GenomeAnalysisTK.jar -T PhaseByTransmission -l INFO -R $ngs_reference_seq.fasta -ped $pedfile -V $trio_name.raw.vcf.gz -o $trio_name.phased.by.transmission.vcf.gz 
# log file prints : "Number of remaining single mendelian violations in trios: 81"

java GenomeAnalysisTK.jar -T ReadBackedPhasing -l INFO -R $ngs_reference_seq.fasta -ped $pedfile -V $trio_name.phased.by.transmission.vcf.gz -L $trio_name.phased.by.transmission.vcf.gz -o $trio_name.read.backed.phasing.vcf.gz $bam_args 

java -jar GenomeAnalysisTK.jar -T SelectVariants -l INFO -R $ngs_reference_seq.fasta -ped $pedfile -V $trio_name.read.backed.phasing.vcf.gz --mendelianViolation -o $trio_name.mendelian.violations.vcf.gz 
```

TK de novo variants

#### [PossibleDeNovo](https://software.broadinstitute.org/gatk/documentation/tooldocs/3.8-0/org_broadinstitute_gatk_tools_walkers_annotator_PossibleDeNovo.php)


#### [PhaseByTransmission](https://software.broadinstitute.org/gatk/documentation/tooldocs/3.8-0/org_broadinstitute_gatk_tools_walkers_phasing_PhaseByTransmission.php)
```
 java -jar GenomeAnalysisTK.jar \
   -T PhaseByTransmission \
   -R reference.fasta \
   -V input.vcf \
   -ped input.ped \
   -o output.vcf
```

### Filt of de novo variants
We called de novo variants using a combination of PLINK/SEQ (Fromer et al., 2014) and in-house scripts (see https://bitbucket.org/willseylab/tourette_phase1 for example commands). Empirically validated filters identified high confidence de novo SNVs and indels (see Sanders et al., 2012). Briefly, we called a de novo variant if:

* The child was heterozygous for a variant with alternate allele frequency (AB) between 0.3 and 0.7 in the child and % 0.05 in the parents (i.e., not present)
* Minimum sequencing depth >= 20 in all family members at the variant position
* Allelic depth for the alternate allele (AD) >= 8
* Observed allele frequency in the respective cohort <= 0.001
* Minimum map quality >= 30
* Minimum phred-scaled genotype likelihood >= 20



