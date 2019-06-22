## [denovogear](https://github.com/denovogear/denovogear)

A program to detect denovo-variants using next-generation sequencing data.

### install denovogear
```
wget https://github.com/denovogear/denovogear/releases/download/v1.1.1/denovogear-v1.1.1-Linux-x86_64.tar.bz2
```


```
$ dng call
Usage:
  dng call [options] input1 input2 input3 ...

Allowed Options:
  -f [ --fasta ] arg                 faidx indexed reference sequence file
  -l [ --min-qlen ] arg (=0)         minimum query length
  -m [ --min-prob ] arg (=0.1)       minimum probability for reporting a 
                                     mutation
  --mu arg (=1e-9)                   the germline mutation rate
  --mu-somatic arg (=0)              the somatic mutation rate
  --mu-library arg (=0)              the library prep mutation rate
  --nuc-freqs arg (=0.3,0.2,0.2,0.3) nucleotide frequencies in ACGT order
  -p [ --ped ] arg                   the pedigree file
  -q [ --min-basequal ] arg (=0)     minimum base quality
  -Q [ --min-mapqual ] arg (=0)      minimum mapping quality
  -r [ --region ] arg                chromosomal region
  -R [ --ref-weight ] arg (=1)       weight given to reference base for 
                                     population prior
  -s [ --sam-files ] arg             file containing a list of input filenames,
                                     one per line
  --theta arg (=0.001)               the population diversity
  -o [ --output ] arg (=-)           Output VCF/BCF file
  --version                          display version information
  --help                             display usage informaiton
  --arg-file arg                     read command-line arguments from a file

```


```
$ dng dnm
DeNovoGear v1.1.1

Usage:
Autosomes:
	dng dnm auto --bcf bcf_f --ped ped_f [OR] dng dnm auto --vcf vcf_f --ped ped_f
X chromosome in male offspring:
	dng dnm XS --bcf bcf_f --ped ped_f [OR] dng dnm XS --vcf vcf_f --ped ped_f
X chromosome in female offspring:
	dng dnm XD --bcf bcf_f --ped ped_f [OR] dng dnm XD --vcf vcf_f --ped ped_f

Input:
DNM:
--ped:	 Ped file to describe relationship between the samples.
--bcf:	 BCF file, contains per-sample read depths and genotype likelihoods.
--vcf:	 VCF file, contains per-sample read depths and genotype likelihoods.
Phaser:
--dnm: Tab delimited list of denovo mutations to be phased, format: chr pos inherited_base denovo_base.[example: 1 2000 A C]
--pgt: Tab delimited genotypes of child and parents at SNP sites near denovo sites, format: chr pos GT_child GT_parent1 GT_parent2.[example: 1 2000 AC AC AA]
--bam: alignment file (.bam) of the child.
--window: optional argument which is the maximum distance between the DNM and a phasing site. The default value is 1000.

Output:
--output_vcf:	 vcf file to write the output to.

Parameters:
--snp_mrate:	 Mutation rate prior for SNPs. [1e-8]
--indel_mrate:	 Mutation rate prior for INDELs. [1e-9]
--pair_mrate:	 Mutation rate prior for paired sample analysis. [1e-9]
--indel_mu_scale:	 Scaling factor for indel mutation rate. [1]
--pp_cutoff:	 Posterior probability threshold. [0.0001]
--rd_cutoff:	 Read depth filter, sites where either one of the sample have read depth less than this threshold are filtered out. [10]
--region:	 Region of the BCF file to perform denovo calling. [string of the form "chr:start-end"]

```


### split bam files
```
$ samtools view -@ 8  -b M625-0_sorted.bam 1 > ../../denovogear/M625-0_sorted_chr1.bam
$ samtools view -@ 8  -b M625-1_sorted.bam 1 > ../../denovogear/M625-1_sorted_chr1.bam
$ samtools view -@ 8  -b M625-2_sorted.bam 1 > ../../denovogear/M625-2_sorted_chr1.bam
```


/home/wuzhikun/Project/Illumina_Trio/denovogear/bam/M625-0_sorted_chr1.bam
/home/wuzhikun/Project/Illumina_Trio/denovogear/bam/M625-1_sorted_chr1.bam
/home/wuzhikun/Project/Illumina_Trio/denovogear/bam/M625-2_sorted_chr1.bam


```
samtools mpileup -gDf /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa  bam/M625-0_sorted_chr1.bam bam/M625-1_sorted_chr1.bam bam/M625-2_sorted_chr1.bam  | dng dnm auto --ped ../M625.ped --vcf M625.vcf -
```


#### dng call
```
$ nohup dng call --ped  ../M625.ped  --output M625_dng.vcf  /home/wuzhikun/Project/Illumina_Trio/denovogear/bam/M625-0_sorted_chr1.bam /home/wuzhikun/Project/Illumina_Trio/denovogear/bam/M625-1_sorted_chr1.bam /home/wuzhikun/Project/Illumina_Trio/denovogear/bam/M625-2_sorted_chr1.bam >dng.log 2>&1 &
```









## [denovogear](https://github.com/denovogear/denovogear)

A program to detect denovo-variants using next-generation sequencing data

### install denovogear
```
conda install -c bioconda denovogear
```


Autosomes:
./denovogear dnm auto --bcf bcf_f --ped ped_f
X chromosome in male offspring:
./denovogear dnm XS --bcf bcf_f --ped ped_f
X chromosome in female offspring:
./denovogear dnm XD --bcf bcf_f --ped ped_f
Phaser:
./denovogear phaser --dnm dnm_f --pgt pgt_f --bam bam_f --window INT[1000]

Input:
DNM:
--ped: Ped file to describe relationship between the samples.
--bcf: BCF file from samtools, contains per-sample read depths and genotype likelihoods.
Phaser:
--dnm_f: Tab delimited list of denovo mutations to be phased, format: chr pos inherited_base denovo_base.[example: 1 2000 A C]
--pgt_f: Tab delimited genotypes of child and parents at SNP sites near denovo sites, format: chr pos GT_child GT_parent1 GT_parent2.[example: 1 2000 AC AC AA]

Output:
--output_vcf: vcf file to store the output.

Parameters:

--snp_mrate: Mutation rate prior for SNPs. [1e-8]
--indel_mrate: Mutation rate prior for INDELs. [1e-9]
--pair_mrate: Mutation rate prior for paired sample analysis. [1e-9]
--indel_mu_scale: Scaling factor for indel mutation rate. [1]
--pp_cutoff: Posterior probability threshold. [0.0001]
--rd_cutoff: Read depth filter, sites where either one of the sample have read depth less than this threshold are filtered out. [10




RUNNING THE CODE
Input requires a PED file and a BCF file. 
usage: ./denovogear --ped sample.ped --bcf sample.bcf 
about sample.bcf: BCF files can be generated from the alignment files using the samtools mpileup command. 
For example the command to generate a bcf file from sample.bam is: 
```
samtools mpileup -gDf reference.fa sample.bam > sample.bcf 
```
The -D option of the samtools mpileup command retains the per-sample read depth which is preferred by denovogear (but note that DNG will work without per-sample RD information). The -g option specifies a compressed output and the -f option is used to indicate the reference. 
about sample.ped: 
The PED file contains information about the trios present in the BCF file. Please make sure that all the members of the trios specified in the PED file are present in the BCF file. The PED file can be used to specify a subset of individuals for analysis from the BCF (that is not every sample in the BCF need be represented in the PED file). 
The PED file is a tab delimited file. The first six columns of the PED file are mandatory, these are Family ID, Individual ID, Paternal ID, Maternal ID, Sex (1 = male; 2 = female; other = unknown) and Phenotype. The sample ID's in the PED file need to be exactly the same as they appear in the BCF file header. Sample order within the PED file does not matter, as family relationships are completely specified by the value of the child/mother/father fields in each row. 
For example, a single line in the PED file that specifies a trio looks like: 
CEU NA12878_vald-sorted.bam.bam NA12891_vald-sorted.bam.bam NA12892_vald-sorted.bam.bam 2 2 
An example PED file, CEU.ped, is included in the distribution directory.

about "snp_lookup.txt" and "indel_lookup.txt": These are tables with precomputed priors (and other useful numbers) for all possible trio configurations, under the null (no mutation present) and alternative (true de novo). The default tables are generated during each program run using a prior of 1 x 10 ^-8 /bp/generation on the haploid germline point mutation rate, and 1 x 10 ^-9 /bp/generation on the haploid germline indel mutation rate. 
If you wish to change the default point or indel mutation rates use the --snp_mrate or --indel_mrate switches respectively. 
For example ./denovogear --ped sample.ped --bcf sample.bcf --snp_mrate 2e-10 --indel_mrate 1e-11

The indel mutation rate varies according to the length of the insertion or deletion, separate models are used for insertions and deletions. The two models were calibrated based on the indel observations from the 1000Genomes phase 1 data. 
The insertion mutation rate is modeled using the function log (mrate) = mu_scale * (-22.8689 - (0.2994 * insertionLength)) 
The deletion mutation rate is modeled using the function log (mrate) = mu_scale * (-21.9313 - (0.2856 * deletionLength)) 
Note that a constant factor is used to scale the mutation rate, it is set to 1.0 by default and can be set using the switch --mu_scale. 
For example, ./denovogear --ped sample.ped --bcf sample.bcf --mu_scale 3 
OUTPUT FORMAT
The output format is a single row for each putative de novo mutation (DNM), with the following fields. 

1. Event type (POINT MUTATION or INDEL) 
2. Sample ID of offspring with the DNM 
3. Chromosome 
4. Physical Position 
5. Base present in reference sequence at this position 
6. ALT - Comma separated list of alternate non-reference alleles called on at-least one sample. 
7. maxlike_null - likelihood of the most likely mendelian-compatible config. 
8. pp_null - posterior probability of most likely mendelian configuration 
9. tgt - genotypes of the most likely mendelian configuration 
10. Code that indicates whether the configuration shown in field 6 is monomorphic (1) or contains variation (2) 
11. This field seems to be redundant to field 7, except the codes are (6) and (9). 
12. maxlike_DNM -11, 12 and 13 are analogous to 6,7,8, but for a de novo mutation 
13. posterior_probability_DNM 
14. tgt: DNM_configuration 
15. Code that indicates if the most likely DNM is a transition (4) or transversion (5) 
16. This is a flag that indicates whether the data for the site passed internal QC thresholds (for development use only). 
17-19. Read depth of child, parent 1 and parent 2. 
20-22. Root mean square of the mapping qualities of all reads mapping to the site for child, parent 1 and parent 2. Currently these values are the same for all samples when using BCF as the input format. 

Fields 17-22 are meant for filtering out low quality sites.



### manual

```
$ cat M625.ped 
M625  M625-0  M625-1  M625-2  0 2
M625  M625-1  0 0 1 1
M625  M625-2  0 0 2 1

```

de novo mutation
```
$ dng dnm auto --vcf Trio/M625_test.vcf  --ped M625.ped 
DeNovoGear v1.1.1

Created SNP lookup table
 First mrate: 1 last: 1
 First code: 6 last: 6
 First target string: AA/AA/AA last: TT/TT/TT
 First tref: 0.0002388 last: 0.99301

Created indel lookup table First code: 6 last: 6
 First target string: RR/RR/RR last: DD/DD/DD
 First prior: 0.05 last: 0.114

Created paired lookup table
 First target string: AA/AA last: TT/TT
 First prior 1 last: 1

Total number of SNP sites interrogated: 425
Total number of SNP sites passing read-depth filters: 404
Total number of INDEL sites interrogated: 43
Total number of INDEL sites passing read-depth filters: 31
Total number of Paired sample sites interrogated: 0
Total number of Paired sample sites passing read-depth filters: 0
Done !

```


```
samtools mpileup -gDf /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa mapping/M625-0/M625-0_realigned.bam mapping/M625-1/M625-1_realigned.bam mapping/M625-2/M625-2_realigned.bam  > samtools/M625.vcf
```


```
bcftools view -bvcg samtools/M625.vcf >  samtools/M625.bcf

bcftools view samtools/M625.bcf | vcfutils.pl varFilter -D100 > SNPs.flt.vcf
```


seqstats M625-0.R1.fastq.gz > reads_num/M625-0.stats
seqstats M625-1.R1.fastq.gz > reads_num/M625-1.stats
seqstats M625-2.R1.fastq.gz > reads_num/M625-2.stats

seqstats M628-0.R1.fastq.gz > reads_num/M628-0.stats
seqstats M628-1.R1.fastq.gz > reads_num/M628-1.stats
seqstats M628-2.R1.fastq.gz > reads_num/M628-2.stats
