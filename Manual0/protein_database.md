# Protein database

## In-silico characterization of proteins
BLAST: In bioinformatics, Basic Local Alignment Search Tool, or BLAST, is an algorithm for comparing primary biological sequence information, such as the amino-acid sequences of different proteins or the nucleotides of DNA sequences. A BLAST search enables a researcher to compare a query sequence with a library or database of sequences, and identify library sequences that resemble the query sequence above a certain threshold. Different types of BLASTs are available according to the query sequences. For example, following the discovery of a previously unknown gene in the mouse, a scientist will typically perform a BLAST search of the human genome to see if humans carry a similar gene; BLAST will identify sequences in the human genome that resemble the mouse gene based on similarity of sequence. The BLAST program was designed by Eugene Myers, Stephen Altschul, Warren Gish, David J. Lipman, and Webb Miller at the NIH and was published in the Journal of Molecular Biology in 1990

CDD search: Conserved Domain Database (CDD) is a protein annotation resource that consists of a collection of well-annotated multiple sequence alignment models for ancient domains and full-length proteins. These are available as position-specific score matrices (PSSMs) for fast identification of conserved domains in protein sequences via RPS-BLAST. CDD content includes NCBI-curated domains, which use 3D-structure information to explicitly to define domain boundaries and provide insights into sequence/structure/function relationships, as well as domain models imported from a number of external source databases (Pfam, SMART, COG, PRK, TIGRFAM).

PFAM: The Pfam database is a large collection of protein families, each represented by multiple sequence alignments and hidden Markov models (HMMs). Proteins are generally composed of one or more functional regions, commonly termed domains. Different combinations of domains give rise to the diverse range of proteins found in nature. The identification of domains that occur within proteins can therefore provide insights into their function. There are two components to Pfam: Pfam-A and Pfam-B. Pfam-A entries are high quality, manually curated families. Although these Pfam-A entries cover a large proportion of the sequences in the underlying sequence database, in order to give a more comprehensive coverage of known proteins we also generate a supplement using the ADDA database. These automatically generated entries are called Pfam-B. Although of lower quality, Pfam-B families can be useful for identifying functionally conserved regions when no Pfam-A entries are found. Pfam also generates higher-level groupings of related families, known as clans. A clan is a collection of Pfam-A entries which are related by similarity of sequence, structure or profile-HMM.

TMHMM: A variety of tools are available to predict the topology of transmembrane proteins. To date no independent evaluation of the performance of these tools has been published. A better understanding of the strengths and weaknesses of the different tools would guide both the biologist and the bioinformatician to make better predictions of membrane protein topology.

SignalP: SignalP 4.0 server predicts the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms: Gram-positive prokaryotes, Gram-negative prokaryotes, and eukaryotes. The method incorporates a prediction of cleavage sites and a signal peptide/non-signal peptide prediction based on a combination of several artificial neural networks.

STRING: STRING is a database of known and predicted protein interactions. The interactions include direct (physical) and indirect (functional) associations; they are derived from four sources i.e. Genomic context, high throughput experiments, coexpression, previous knowledge. STRING quantitatively integrates interaction data from these sources for a large number of organisms, and transfers information between these organisms where applicable. The database currently covers 5’214’234 proteins from 1133 organisms.

PROTPARAM: ProtParam (References / Documentation) is a tool which allows the computation of various physical and chemical parameters for a given protein stored in Swiss-Prot or TrEMBL or for a user entered sequence. The computed parameters include the molecular weight, theoretical pI, amino acid composition, atomic composition, extinction coefficient, estimated half-life, instability index, aliphatic index and grand average of hydropathicity (GRAVY)

PROSITE: Search your query sequence for protein motifs, rapidly compare your query protein sequence against all patterns stored in the PROSITE pattern database and determine what the function of an uncharacterised protein is. This tool requires a protein sequence as input, but DNA/RNA may be translated into a protein sequence using transeq and then queried.

InterPro: InterPro is an integrated database of predictive protein “signatures” used for the classification and automatic annotation of proteins and genomes. InterPro classifies sequences at superfamily, family and subfamily levels, predicting the occurrence of functional domains, repeats and important sites. InterPro adds in-depth annotation, including GO terms, to the protein signatures.



## [NCBI database](ftp://ftp.ncbi.nlm.nih.gov/)


## NCBI
就是在blastp, 或者psi-blast中的那个NR 数据库.NCBI 的说明是:
All non-redundant GenBank CDS translations + RefSeq Proteins + PDB + SwissProt + PIR + PRF


## [nr（protein）和nt（nucletide）数据库](ftp://ftp.ncbi.nih.gov/blast/db/FASTA/)
2017/11/14 下午5:54:00
```
ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nr.gz
ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nr.gz.md5
ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nt.gz
ftp://ftp.ncbi.nih.gov/blast/db/FASTA/nt.gz.md5
ftp://ftp.ncbi.nih.gov/blast/db/FASTA/swissprot.gz
ftp://ftp.ncbi.nih.gov/blast/db/FASTA/swissprot.gz.md5
```

## [/pub/db/refgene/](ftp://ftp.genome.jp/pub/db/refgene/)
```
ftp://ftp.genome.jp/pub/db/refgene/README
ftp://ftp.genome.jp/pub/db/refgene/RG001
ftp://ftp.genome.jp/pub/db/refgene/RG001.nuc
ftp://ftp.genome.jp/pub/db/refgene/RG001.pep
ftp://ftp.genome.jp/pub/db/refgene/RG002
ftp://ftp.genome.jp/pub/db/refgene/RG002.nuc
ftp://ftp.genome.jp/pub/db/refgene/RG002.pep
```
名称  大小  修改日期
README  1.5 kB  2017/3/10 上午8:00:00
RG001   50.7 GB 2017/1/23 上午8:00:00
RG001.nuc   26.9 GB 2017/1/18 上午8:00:00
RG001.pep   11.1 GB 2017/1/18 上午8:00:00
RG002   13.9 GB 2017/1/23 上午8:00:00
RG002.nuc   7.4 GB  2017/1/18 上午8:00:00
RG002.pep   2.7 GB  2017/1/18 上午8:00:00

RefGene is a set of non-redundant microbial reference gene catalogs. It consists
of two previously published reference gene catalogs, OM-RGC and IGC. They contain
genes from marine and human gut microorganisms respectively. The taxonomic and
functional annotations were performed at GenomeNet based on amino acid level
sequence similarity searches against KEGG GENES database using GhostKOALA
(http://www.kegg.jp/ghostkoala/). For further information about the catalogs,
see [1] for OM-RGC and [2] for IGC.

This directory contains following files:
RG001: annotated gene entries of OM-RGC.
RG001.nuc: FASTA formatted nucleotide sequences of OM-RGC.
RG001.pep: FASTA formatted amino acid sequences of OM-RGC.
RG002: annotated gene entries of IGC.
RG002.nuc: FASTA formatted nucleotide sequences of IGC.
RG002.pep: FASTA formatted amino acid sequences of IGC.

REFERENCE
==========
[1] Sunagawa, S. et al. (2015) "Structure and function of the global ocean microbiome." Science, 348(6237)
[2] Li, J. et al. (2014) "An integrated catalog of reference genes in the human gut microbiome." 


## [UNIPROT download](http://www.uniprot.org/downloads)
## [UNIPROT](ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete)
```
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/LICENSE
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/README
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/RELEASE.metalink
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/reldate.txt
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot.xsd
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.dat.gz
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot_varsplic.fasta.gz
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.dat.gz
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.xml.gz
```



## eggNOG
```
##../
##hmmdb_levels/                                      29-May-2016 08:05       -
##OG_fasta.tar.gz                                    29-Jun-2016 09:51      6G
##eggnog.db.gz                                       13-Sep-2016 15:00      4G
##eggnog4.clustered_proteins.fa.gz                   13-Jul-2017 09:40      2G
##eggnog_proteins.all_seqs.dmnd.gz                   14-Sep-2016 15:49      2G
##eggnog_proteins.dmnd.gz                            09-Feb-2017 15:50      2G
##emapper_benchmark_data.tar.gz                      01-Apr-2017 11:40     13G
##hmmdb.euk_bact_arch.tar.gz                         21-Aug-2015 10:09     42G
##og2level.tsv.gz                                    02-Nov-2017 17:16      5M


wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/hmmdb_levels/
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/OG_fasta.tar.gz
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/eggnog.db.gz
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/eggnog4.clustered_proteins.fa.gz
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/eggnog_proteins.all_seqs.dmnd.gz
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/eggnog_proteins.dmnd.gz
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/emapper_benchmark_data.tar.gz
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/hmmdb.euk_bact_arch.tar.gz
wget http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/og2level.tsv.gz
```

## [WikiPathways ](https://www.wikipathways.org/index.php/WikiPathways)

## Databases for MOCAT2:
```
## Taxonomic profiling (these are included in the MOCAT2 download already):
### RefMG.v1 database (summarizing into specI & NCBI taxonomic levels)
wget http://vm-lux.embl.de/~kultima/share/mOTU/RefMG.v1.padded.tar.gz
### mOTU.v1 database (summarizing into mOTU-LGs)
wget http://vm-lux.embl.de/~kultima/share/mOTU/mOTU.v1.padded.tar.gz
## Human reference genome (not included in the MOCAT2 download):
### Human Genome 19 database (used for removing human contaminants)
wget http://vm-lux.embl.de/~kultima/share/MOCAT/data/hg19.gz
```

```
## Do you want the public, stable version of MOCAT2 WITHOUT functional annotation capabilities?
### Download MOCAT2 v 2.0 (26 MB) | Manual in PDF format
wget http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/MOCAT2-lite.zip
wget http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/MOCATv2.0.manual.pdf


## wgetsite: http://vm-lux.embl.de/~kultima/MOCAT/download.html
## Pre-compiled reference gene catalogs (RGCs) for funcitonal profiling:
### Downloads include (padded) nucleotide sequences, required coord and length files, and functional annotation file = all you'd ever need ;)
### IGC (human gut): Download (2.6 GB) 
wget http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/IGC.zip
### Colorectal cancer-RGC (human gut): Download (2.2 GB)
wget http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/CRC-RGC.zip
### skin-RGC (human skin): Download (1.1 GB)
wget http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/skin-RGC.zip
### mouse-RGC (mouse gut): Download (0.7 GB) 
wget http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/mouse-RGC.zip
### OM-RGC (ocean): Download (9.3 GB)
wget http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/OM-RGC.zip
```


## [物种分类数据库](ftp://ftp.ncbi.nih.gov/pub/taxonomy)

https://github.com/giffordlabcvr/DIGS-for-EVEs/wiki/NCBI-taxonomy-database
2017/11/15 上午10:20:00
```
ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz
ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz.md5
ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump_readme.txt
```

## [kobas seq_pep](ftp://ftp.cbi.pku.edu.cn/pub/KOBAS_3.0_DOWNLOAD/seq_pep/)

## [Welcome to the Carbohydrate-Active enZYmes Database](http://www.cazy.org/)

Modules that catalyze the breakdown, biosynthesis or modification of carbohydrates and glycoconjugates:

- Glycoside Hydrolases (GHs) : hydrolysis and/or rearrangement of glycosidic bonds (see CAZypedia definition)

- GlycosylTransferases (GTs) : formation of glycosidic bonds (see definition)

- Polysaccharide Lyases (PLs) : non-hydrolytic cleavage of glycosidic bonds

- Carbohydrate Esterases (CEs) : hydrolysis of carbohydrate esters

- Auxiliary Activities (AAs) : redox enzymes that act in conjunction with CAZymes.


## [dbCAN](http://csbl.bmb.uga.edu/dbCAN/index.php)
## [cazy-parser](https://github.com/rodrigovrgs/cazy-parser): A way to extract specific information from CAZy
## [CAZy_utils](https://github.com/nielshanson/CAZy_utils): utilities for working with the CAZy database
## [CAZyinformatics](http://research.ahv.dk/)
## [ARDB - Antibiotic Resistance Genes Database](https://ardb.cbcb.umd.edu/)
## [GO Database](http://geneontology.org/page/go-database)
## [kegg readme](http://www.kegg.jp/kegg/download/Readme/README.genes)

# Protein database



## [CDD数据库](ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd)
```
wget ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/cdd.info
wget ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/cdd.tar.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/cddannot.dat.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/cddid.tbl.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/cddid_all.tbl.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/mmdb/cdd/cddmasters.fa.gz
```

files:
```

cdd.info    334 B   2017/3/28 上午8:00:00
cdd.tar.gz  3.7 GB  2017/3/28 上午8:00:00
cdd.versions    42.1 MB 2017/3/28 上午8:00:00
cddannot.dat.gz 522 kB  2017/3/28 上午8:00:00
cddannot_generic.dat.gz 300 kB  2017/3/28 上午8:00:00
cddid.tbl.gz    5.5 MB  2017/3/28 上午8:00:00
cddid_all.tbl.gz    5.8 MB  2017/3/28 上午8:00:00
cddmasters.fa.gz    12.5 MB 2017/3/28 上午8:00:00
cdtrack.txt 
```


### [TIGRFAMs](http://www.jcvi.org/cgi-bin/tigrfams/Resources.cgi)
### [TIGRFAMs ftp](ftp://ftp.jcvi.org/pub/data/TIGRFAMs/)
```
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/NEW_TIGRFAMs_RELEASE.adapt_release.15
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/CHANGES_15.0
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGRFAMS_GO_LINK
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGRFAMS_ROLE_LINK
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGRFAMs_15.0_HMM.LIB.gz
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGRFAMs_15.0_HMM.tar.gz
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGRFAMs_15.0_INFO.tar.gz
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGRFAMs_15.0_SEED.tar.gz
wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGR_ROLE_NAMES
```

#### TIGRFAMS TERMS
TIGRFAMs: TIGRFAMs are a collection of protein families featuring curated multiple sequence alignments, Hidden Markov Models (HMMs) and associated information designed to support the automated functional identification of proteins by sequence homology. Classification by equivalog family (see below), where achievable, complements classification by orthologs, superfamily, domain or motif. It provides the information best suited for automatic assignment of specific functions to proteins from large scale genome sequencing projects. 

HMM: A Hidden Markov Model, or HMM, is a statistical model for any system that can be represented as a succession of transitions between discrete states. In this case, the discrete states correspond to the successive columns of a protein multiple sequence alignment. In principle, HMMs can be developed from unaligned sequences by successive rounds of optimization, but in practice, protein profile HMMs are simply built from curated multiple sequence alignments. HMM searches resemble later round PSI-BLAST searches (although based on curated alignments), with position-specific scoring for each of the amino acid, insertion, and deletion over the length of the sequence. Scores are reported both in bits of information and as an E-value.

Equivalog: Equivalogs describe members of a set of homologous proteins that are conserved with respect to function since their last common ancestor. Related proteins are grouped into equivalog families where possible, and otherwise into protein families with other hierarchically defined homology types. Equivalogs are constructed to be full-length or as nearly so as is possible, homologous regions of conserved function which are generally substrings of longer proteins are classified as "equivalog domain" (see domain, below). In certain cases a family of proteins may be noted which have the phylogenetic characteristics of an equivalog, but the specific function has not yet been experimentally determined, models of these families are classified as "hypothetical equivalog" (or "hypothetical equivalog domain")

Orthologs: Proteins related to each other by descent from a common ancestral sequence by speciation. Orthologs may differ in function.

Superfamily: The complete set of proteins having sequence homology over essentially their full length.

Subfamily: Where superfamilies are presumed to be complete, subfamilies represent an incomplete set of homologous proteins which yet encompass proteins of diverse function. Since superfamilies, however, are often impractical to construct, subfamilies are far more common in TIGRFAMs. Subfamilies fulfill a number of useful roles in tha annotation process. The construction of equivalogs is a process which results in models which may not identify all homologous sequences of conserved function due to the limits of current experimental characterization - a subfamily may encompass all of the sequences included within one (or more) equivalog(s) as well as related sequences which fall outside of an equivalog's scope. Subfamilies, then, are often a hierarchical level above equivalogs and may provide information through their associated comment fields which may assist in the naming of genes which are not members of any current equivalog. In certain situations equivalogs may not be constructed because of the rapid change of function (substrate variability) within a related group of sequences relative to the slower drift of evolutionary changes to which HMMs are sensitive. In these cases, subfamily models will be the most specific models available, and will provide warnings that assignment of specific fucntion based on pairwise alignments may result in errors of annotation. Like equivalogs and superfamilies, subfamilies are presumed to be full-length models. Models of portions of longer proteins which encompass more than one function are classified as "subfamily domain" (see domain, below).

Domain: A region of sequence homology among sets of proteins that are not all full-length homologs. Homology domains often, but not always, correspond to recognizable protein folding domains.

Motif: Generally, a small region of sequence similarity (not necessarily homology) characterized by distinct patterns of amino acids at specific positions. An example of a motif is the N-glycosylation site motif N{P}[ST] (Asn, anything but Pro, choice of Ser or Thr).

EGAD: A database used to store gene, protein and TIGRFam/HMM information.

Noise Cutoff: The HMM score below which hits to the HMM are considered uninteresting.

Trusted Cutoff: The HMM score above which there should be no false positive hits.

PFAM: A collection of HMM models of protein families complementary to TIGRFAMs. While the names of TIGRFAMs models (particularly equivalogs) strive to provide functionally accurate names which can be applied to the genes which they describe, PFAM models tend to use names which may represent only a subset (or even one) of the functions of the genes which they describe. PFAM models are constrained to be non-overlapping with one another and thus are more likely to describe domains rather than full-length proteins. Some PFAM models have the properties of equivalogs and many of these have been classified as "PFAM equivalog".


### [Pfam](ftp://ftp.ebi.ac.uk/pub/databases/Pfam)
### [dowblod website](ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam31.0/)

### [COG](ftp://ftp.ncbi.nih.gov/pub/COG)


## [OTU table](ftp://ftp.microbio.me/emp/release1/otu_tables)
## [microbio](ftp://ftp.microbio.me/pub/)

### [Megam](http://ab.inf.uni-tuebingen.de/data/software/megan6/download/welcome.html)
```
wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/prot_gi2tax-Aug2016X.bin.zip
wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/nucl_gi2tax-Aug2016.bin.zip
wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/gi2eggnog-June2016X.bin.zip
wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/gi2interpro-June2016X.bin.zip
wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/gi2seed-May2015X.bin.zip
wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/gi2kegg-Aug2016X-ue.bin.zip
```


### [ensembl](ftp://ftp.ensembl.org/pub/release-85/)


### [uniprot](http://www.uniprot.org/downloads)
Reviewed (Swiss-Prot):
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz

Unreviewed (TrEMBL):
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz

### [UniProt](https://en.wikipedia.org/wiki/UniProt#UniProtKB.2FSwiss-Prot)


### [GO.db](https://bioconductor.org/packages/release/data/annotation/html/GO.db.html): A set of annotation maps describing the entire Gene Ontology

### [Mysql-Query On Go-Database Ucsc Server](https://www.biostars.org/p/75411/)

### [Ensembl Plants Home ](http://plants.ensembl.org/info/website/ftp/index.html)




### [gene ontology](http://www.geneontology.org/page/download-go-annotations)
##### Danio rerio(斑马鱼):
wget http://geneontology.org/gene-associations/gene_association.zfin.gz
##### Caenorhabditis elegans (秀丽隐杆线虫)
wget http://geneontology.org/gene-associations/gene_association.wb.gz
##### Arabidopsis thaliana (拟南芥)
wget http://geneontology.org/gene-associations/gene_association.tair.gz
##### Solanaceae (茄科)
wget http://geneontology.org/gene-associations/gene_association.sgn.gz
##### Saccharomyces cerevisiae (酿酒酵母)
wget http://geneontology.org/gene-associations/gene_association.sgd.gz
##### Rattus norvegicus (褐鼠)
wget http://geneontology.org/gene-associations/gene_association.rgd.gz
##### Pseudomonas aeruginosa (绿脓假单胞菌；绿脓杆菌)
wget http://geneontology.org/gene-associations/gene_association.pseudocap.gz
##### Schizosaccharomyces pombe (粟酒裂殖酵母)
wget http://geneontology.org/gene-associations/gene_association.pombase.gz
##### Mus musculus (小鼠)
wget http://geneontology.org/gene-associations/gene_association.mgi.gz
##### Comprehensive Microbial ()
wget http://geneontology.org/gene-associations/gene_association.jcvi.gz
##### Oryza sativa (水稻)
wget http://geneontology.org/gene-associations/gene_association.gramene_oryza.gz
##### UniProt
wget ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/goa_uniprot_all.gaf.gz
##### UniProt, no IEA annotations
wget http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
##### Sus scrofa (野猪)
wget http://geneontology.org/gene-associations/goa_pig.gaf.gz
##### Homo sapiens (智人)
wget http://geneontology.org/gene-associations/goa_human.gaf.gz
##### Canis lupus familiaris (狼)
wget http://geneontology.org/gene-associations/goa_dog.gaf.gz
##### Bos taurus (牛)
wget http://geneontology.org/gene-associations/goa_cow.gaf.gz
##### Gallus gallus (原鸡)
wget http://geneontology.org/gene-associations/goa_chicken.gaf.gz
##### Drosophila melanogaster (果蝇)
wget http://geneontology.org/gene-associations/gene_association.fb.gz
##### Escherichia coli (大肠杆菌)
wget http://geneontology.org/gene-associations/gene_association.ecocyc.gz
##### Dictyostelium discoideum (盘基网柄菌)
wget http://geneontology.org/gene-associations/gene_association.dictyBase.gz
##### Candida albicans (白色念珠菌； 白假丝酵母)
wget http://geneontology.org/gene-associations/gene_association.cgd.gz
##### Aspergillus nidulans (构巢曲霉)
wget http://geneontology.org/gene-associations/gene_association.aspgd.gz
##### Oomycetes (卵菌类)
wget http://geneontology.org/gene-associations/gene_association.PAMGO_Oomycetes.gz
##### Magnaporthe grisea (稻瘟病菌)
wget http://geneontology.org/gene-associations/gene_association.PAMGO_Mgrisea.gz
##### Dickeya dadantii ()
wget http://geneontology.org/gene-associations/gene_association.PAMGO_Ddadantii.gz
##### Trypanosoma brucei (布氏锥虫)
wget http://geneontology.org/gene-associations/gene_association.GeneDB_Tbrucei.gz
##### Plasmodium falciparum (镰状疟原虫； 恶性疟原虫)
wget http://geneontology.org/gene-associations/gene_association.GeneDB_Pfalciparum.gz
##### Leishmania major (硕大利什曼原虫)
wget http://geneontology.org/gene-associations/gene_association.GeneDB_Lmajor.gz




### [GO latest-full](http://archive.geneontology.org/latest-full/)
```
[TXT] README                            10-May-2011 15:00  5.9K  
[   ] go_monthly-assocdb-data.gz        07-Jan-2017 01:51  6.2G  
[   ] go_monthly-assocdb-summary.txt.gz 07-Jan-2017 01:51  1.1K  
[   ] go_monthly-assocdb-tables.tar.gz  07-Jan-2017 01:56  6.1G  
[   ] go_monthly-termdb-data.gz         07-Jan-2017 01:56   12M  
[   ] go_monthly-termdb-summary.txt.gz  07-Jan-2017 01:56  387   
[   ] go_monthly-termdb-tables.tar.gz   07-Jan-2017 01:56   12M  
[   ] go_monthly-termdb.obo-xml.gz      07-Jan-2017 01:56  4.4M  
[   ] go_monthly-termdb.owl.gz          07-Jan-2017 01:56  5.5M  
[   ] go_monthly-termdb.rdf-xml.gz      07-Jan-2017 01:56  4.4M  
GO DATABASE DOWNLOADS
=====================

For full documentation see

  http://www.geneontology.org/GO.database.shtml

FILENAME CONVENTION
===================

releases are named

  go_<YYYYMM>-<DATASET><TYPE>

YYYYMM is the release date (the release export usually follows some
time after the monthly release, due to time taken to build)

the DATASET is one of:
    -------

* termdb - a database containing just the information on the
GO terms and relationships. These are the table that are populated:

term                        GO controlled vocab terms
term2term                   relationships between GO terms
term_definition             definitions of terms
dbxref                      external database identifier entities
term_dbxref                 links from terms to other databases
term_synonym                synonyms for terms
graph_path                  transitive closure (all paths) in graph

* assocdb - a database containing both the GO vocabulary and
associations between GO terms and gene products. This database
subsumes termdb. These are the extra tables that are populated:

gene_product                 gene or protein or entity annotated
association                  link between gene product and GO term
evidence                     evidence type and reference for an assoc
gene_product_count           recursive product counts per GO term

*seqdb - a database containing GO terms, gene products and the
sequences associated with these gene products. This db subsumes the
two above. It populates these additional tables:

seq                          biological sequence
gene_product_seq             link between a product and a sequence
seq_dbxref                   external database links for a sequence

NOTE: there are other unpopulated tables - we may or may not decide to
populate these at some point in the future.

NOTE: The production version of seqdb with the full database has been
suspended until further notice.

*seqdblite - this is the same as seqdb, except all IEA associations
have been removed. The IEA associations provide relatively little
value compared to the curated associations, and they slow querying
down immensely. This is the distribution that AmiGO runs off of. We
are working on optimisations to allow AmiGO to run off of the full
seqdb release.

the TYPE is either
    ----

.rdf-xml - RDF XML export of the database. this comes as one single
file. Note there is no RDF XML export of seqdb, as we do not include
sequences in the xml yet. We do not include IEA evidence associations
in the xml. We may decide to split this xml file into multiple files
at a later date.

.obo-xml - OBO XML Export. Currently ontology only

.owl - OWL Export. Currently ontology only

.tables - this is a directory containing the MySQL dump, see below

.sql - SQL CREATE TABLE and INSERT statements for building a local
instance of the database. equivalent to the .tables TYPE (but slower
to load)


SCHEMA DOCUMENTATION
********************
### This schema file is no longer being provided as of 2011-01-27

In this distribution, uncomporess the file:

go_YYYYMM-schema-mysql.sql.gz

Which contains the (MySQL ported) schema used in this release 

You can also look at the HTML marked up version of the schema, or
schema diagrams here:

Go to 

  http://www.geneontology.org/GO.database.shtml

  click on "Schema Docs" or "Tables" in the sidebar

To guarantee that your schema, code and database release are in sync
you should use the files from the same release.

**********************************
MYSQL USERS

The database export was prepared from a mysql db - you should have no
problem importing it:

tar -zxvf go-YYYYMM-TYPE-tables.gz
cd <releasedir>
echo "create database mygo" | mysql
cat *.sql | mysql mygo
mysqlimport -L mygo *.txt

Note: if you are using Windows, you may see warning messages when
loading some tables; to avoid this, load tables this way:

mysql> load data infile
"c:\\download\\GO\\july-release\\go_200307-assocdb-table
s\\association.txt" into table association lines terminated by '\r\n';

This can be avoided if you disable "TAR file smart CR/LF conversion"
when using Winzip (thanks to Henrik Edgren for the tip

We are unable to support Windows users - please refer to your MySQL
documentation; if you experience other problems, you may wish to try
posting a question to the go-database mail list to see if other
Windows users have any advice.

**********************************
OTHER DBMS USERS

Your database is not supported; but we do have some tips below:

also: the perl api code is mostly DBMS neutral, it should in theory
work on non mysql setups

**********************************
POSTGRES USERS:

TIP: for converting mysql dumps to postgres, try my2pg

http://www.ziet.zhitomir.ua/~fonin/code/

Thanks to Joe Morris of Affymetrix for the tip

************************************
ORACLE USERS:

see the directory sql/oracle/ in the go_YYYYMM-utilities_src software
distribution

This is contributed software, and not supported by the go-dev group.

************************************
PROGRAMMERS:

you can access the data using the perl API - see
http://www.geneontology.org/GO.database.shtml

OR look at the perl API release for the data release:

tar -zxvf go_YYYYMM-utilities_src.tar.gz
cd go_YYYYMM-utilities_src
cd perl-api
perldoc GO/AppHandle.pm

sometimes the perl API must be in sync with the database, eg if the
schema changes in a way to break old code

*************************************
AMIGO:

you can build a local AmiGO installation using the source code and
data included in this distribution. You can load your own data into it
using either the scripts in go-dev/apps/db-loading, or the configure
script and makefile in go-dev/sql

*************************************
QUESTIONS:

Email the go-database mail list; go to

  http://www.geneontology.org/GO.database.shtml

And click on "Mail List" in the sidebar

Be sure to have read the rest of the database documentation before
asking a question
```



