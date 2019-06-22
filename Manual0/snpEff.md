## snpEff manual

### install snpEff

```
$ source activate envolution
$ conda install -c bioconda snpeff 
```

First activate the anaconda environment **evolution**

And then the tool **snpEff** was installed in the directory **~/anaconda3/envs/evolution/bin**

```
~/anaconda3/envs/evolution/bin/snpEff
```

The tree of snpEff
```
$ tree ~/anaconda3/envs/evolution/bin/snpEff -L 1
./
├── data/
├── examples/
├── galaxy/
├── history.sh
├── scripts/
├── snpEff.config
├── snpEff.jar
└── SnpSift.jar
```

In this directory, **snpEff.jar** is a main executor, file **snpEff.config** contains parameters, 
and  directory **data** contains the reference genomes and annotation files.

### Config of parameters for given genome

The tree of directory **data**

```
$ tree ~/anaconda3/envs/evolution/bin/snpEff/data -L 2
data
├── Brassica_napus_v4.1
│   ├── genes.gff
│   └── snpEffectPredictor.bin
├── Chinese_Spring_v1.0
│   ├── genes.gff
│   └── snpEffectPredictor.bin
├── Fragaria_vesca_v4.0.a1
│   ├── genes.gff
│   ├── genes.gtf
│   └── snpEffectPredictor.bin
├── genomes
│   ├── Brassica_napus_v4.1.fa
│   ├── Chinese_Spring_v1.0.fa
│   ├── Fragaria_vesca_v4.0.a1.fa
│   ├── GRCm38.fa
│   ├── O_sativa_v7.fa
│   ├── TAIR10.fa
├── GRCm38
│   ├── genes.gff
│   └── snpEffectPredictor.bin
├── O_sativa_v7
│   ├── genes.gff
│   └── snpEffectPredictor.bin
├── TAIR10
    ├── genes.gff
    └── snpEffectPredictor.bin

```

There were six genomes for what we had finished the config in this directory, and the annotation files were mainly **.gff**.


```
$ mkdir -p data/ViralProj14034 && cd data

$ cp /home/wzk/database/GENOME/ViralProj14034/GCF_000837685.1_ViralProj14034_genomic.fna ViralProj14034.fa
$ cp /home/wzk/database/GENOME/ViralProj14034/GCF_000837685.1_ViralProj14034_genomic_with_GENE.gff genes.gff

$ mv ViralProj14034.fa genomes/ 
$ mv genes.gff ViralProj14034/
```

And then write followed content in the file **snpEff.config**:
```
ViralProj14034.genome: ViralProj14034
```


### build the annotation

Build the annotation
```
$ cd ../
$ java -jar ./snpEff.jar build -gff3 -v ViralProj14034
```

The warnings:
```
$ java -jar ./snpEff.jar build -gff3 -v ViralProj14034
00:00:00	SnpEff version SnpEff 4.3t (build 2017-11-24 10:18), by Pablo Cingolani
00:00:00	Command: 'build'
00:00:00	Building database for 'ViralProj14034'
00:00:00	Reading configuration file 'snpEff.config'. Genome: 'ViralProj14034'
00:00:00	Reading config file: /home/wzk/anaconda3/envs/evolution/bin/snpEff/snpEff.config
00:00:00	done
Reading GFF3 data file  : '/home/wzk/anaconda3/envs/evolution/bin/snpEff/./data/ViralProj14034/genes.gff'
.
	Total: 185 markers added.

	Create exons from CDS (if needed): ...........................................................................................................................................................................................
	Exons created for 185 transcripts.

	Deleting redundant exons (if needed): 
		Total transcripts with deleted exons: 0

	Collapsing zero length introns (if needed): 
		Total collapsed transcripts: 0
	Reading sequences   :
	Reading FASTA file: '/home/wzk/anaconda3/envs/evolution/bin/snpEff/./data/genomes/ViralProj14034.fa'
		Reading sequence 'NC_001884.1', length: 134416
		Adding genomic sequences to exons: 	Done (187 sequences added, 0 ignored).
	Total: 187 sequences added, 0 sequences ignored.

	Adjusting transcripts: 
	Adjusting genes: 
	Adjusting chromosomes lengths: 
	Ranking exons: 
	Create UTRs from CDS (if needed): 
	Correcting exons based on frame information.
	
	Remove empty chromosomes: 

	Marking as 'coding' from CDS information: 
	Done: 0 transcripts marked
#-----------------------------------------------
# Genome name                : 'ViralProj14034'
# Genome version             : 'ViralProj14034'
# Genome ID                  : 'ViralProj14034[0]'
# Has protein coding info    : true
# Has Tr. Support Level info : true
# Genes                      : 185
# Protein coding genes       : 185
#-----------------------------------------------
# Transcripts                : 185
# Avg. transcripts per gene  : 1.00
# TSL transcripts            : 0
#-----------------------------------------------
# Checked transcripts        : 
#               AA sequences :      0 ( 0.00% )
#              DNA sequences :      0 ( 0.00% )
#-----------------------------------------------
# Protein coding transcripts : 185
#              Length errors :      0 ( 0.00% )
#  STOP codons in CDS errors :      0 ( 0.00% )
#         START codon errors :     18 ( 9.73% )
#        STOP codon warnings :      0 ( 0.00% )
#              UTR sequences :      0 ( 0.00% )
#               Total Errors :     18 ( 9.73% )
# WARNING                    : No protein coding transcript has UTR
#-----------------------------------------------
# Cds                        : 187
# Exons                      : 187
# Exons with sequence        : 187
# Exons without sequence     : 0
# Avg. exons per transcript  : 1.01
#-----------------------------------------------
# Number of chromosomes      : 1
# Chromosomes                : Format 'chromo_name size codon_table'
#		'NC_001884.1'	134416	Standard
#-----------------------------------------------

00:00:01	Caracterizing exons by splicing (stage 1) : 
	
00:00:01	Caracterizing exons by splicing (stage 2) : 
	00:00:01	done.
00:00:01	[Optional] Rare amino acid annotations
00:00:01	Warning: Cannot read optional protein sequence file '/home/wzk/anaconda3/envs/evolution/bin/snpEff/./data/ViralProj14034/protein.fa', nothing done.
00:00:01	Saving database
00:00:01	[Optional] Reading regulation elements: GFF
00:00:01	Warning: Cannot read optional regulation file '/home/wzk/anaconda3/envs/evolution/bin/snpEff/./data/ViralProj14034/regulation.gff', nothing done.
00:00:01	[Optional] Reading regulation elements: BED 
00:00:01	Cannot find optional regulation dir '/home/wzk/anaconda3/envs/evolution/bin/snpEff/./data/ViralProj14034/regulation.bed/', nothing done.
00:00:01	[Optional] Reading motifs: GFF
00:00:01	Warning: Cannot open PWMs file /home/wzk/anaconda3/envs/evolution/bin/snpEff/./data/ViralProj14034/pwms.bin. Nothing done
00:00:01	Done
00:00:01	Logging
00:00:03	Checking for updates...
00:00:04	Done.
```

From the warnings, for complete annotation, it need other annotation files, such as **protein.fa** (amino acid), **regulation.gff** (regulation elements) or **pwms.bin** (motifs).

### Run annotation

```
$ java  -Xmx20g  -jar /home/wzk/anaconda3/envs/evolution/bin/snpEff/snpEff.jar ann ViralProj14034 samtools_VCF/T01.vcf > samtools_VCF/T01_eff.vcf
```

**ViralProj14034** is a indexed annotation database, The input file is a **.vcf** file.


### Annotation result

```
$ cut -f 7 T01_annotation.xls | cut -d '|' -f 8 | less


$ cut -f 7 T01_annotation.xls | cut -d '|' -f 2 | sort | uniq | less
3_prime_UTR_variant
5_prime_UTR_premature_start_codon_gain_variant
5_prime_UTR_variant
Annotation
conservative_inframe_deletion
conservative_inframe_insertion
conservative_inframe_insertion&splice_region_variant
disruptive_inframe_deletion
disruptive_inframe_insertion
disruptive_inframe_insertion&splice_region_variant
downstream_gene_variant
frameshift_variant
frameshift_variant&splice_acceptor_variant&splice_donor_variant&splice_region_variant&intron_variant
frameshift_variant&splice_acceptor_variant&splice_region_variant&intron_variant
frameshift_variant&splice_donor_variant&splice_region_variant&intron_variant
frameshift_variant&splice_region_variant
frameshift_variant&start_lost
frameshift_variant&stop_gained
frameshift_variant&stop_lost
frameshift_variant&stop_lost&splice_region_variant
initiator_codon_variant
initiator_codon_variant&splice_region_variant
intergenic_region
intron_variant
missense_variant
missense_variant&splice_region_variant
splice_acceptor_variant&intron_variant
splice_acceptor_variant&splice_donor_variant&intron_variant
splice_donor_variant&intron_variant
splice_donor_variant&splice_region_variant&intron_variant
splice_region_variant
splice_region_variant&intron_variant
splice_region_variant&stop_retained_variant
splice_region_variant&synonymous_variant
start_lost
start_lost&conservative_inframe_insertion
stop_gained
stop_gained&conservative_inframe_insertion
stop_gained&disruptive_inframe_deletion
stop_gained&disruptive_inframe_insertion
stop_gained&splice_region_variant
stop_lost
stop_lost&conservative_inframe_deletion
stop_lost&splice_region_variant
stop_retained_variant
synonymous_variant
upstream_gene_variant


$ cut -f 7 T01_annotation.xls | cut -d '|' -f 3 | sort | uniq | less
HIGH
LOW
MODERATE
MODIFIER
Putative_impact


$ cut -f 7 T01_annotation.xls | cut -d '|' -f 4 | sort | uniq | less
TraesCS1A01G000100
TraesCS1A01G000100-TraesCS1A01G000200


$ cut -f 7 T01_annotation.xls | cut -d '|' -f 6 | sort | uniq | less
intergenic_region
transcript

$ cut -f 7 T01_annotation.xls | cut -d '|' -f 8 | sort | uniq | less
protein_coding
Transcript_biotype

$ cut -f 7 T01_annotation.xls | cut -d '|' -f 9 | sort | uniq | less
10/10
10/11
10/12

```
