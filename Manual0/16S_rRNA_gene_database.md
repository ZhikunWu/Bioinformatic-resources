# 16S rRNA gene databases

* Bacterial
* Archaeal
* Fungal

There are three mainly used databases: Greengene, SILVA and RDP

## [greengenes](http://greengenes.secondgenome.com/)

### [The Greengenes Database Downloads](http://greengenes.secondgenome.com/downloads/database/13_5)

Three main files:

* gg_13_5.fasta: id and sequence 
* gg_13_5_taxonomy.txt: id and taxonomy
* gg_13_5_accessions.txt: id and genebank id

```
$ head -n 2 gg_13_5.fasta
>1111886
AACGAACGCTGGCGGCATGCCTAACACATGCAAGTCGAACGAGACCTTCGGGTCTAGTGGCGCACGGGTGCGTAACGCGTGGGAATCTGCCCTTGGGTACGGAATAACAGTTAGAAATGACTGCTAATACCGTATAATGACTTCGGTCCAAAGATTTATCGCCCAGGGATGAGCCCGCGTAGGATTAGCTTGTTGGTGAGGTAAAGGCTCACCAAGGCGACGATCCTTAGCTGGTCTGAGAGGATGATCAGCCACACTGGGACTGAGACATGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGGACAATGGGCGAAAGCCTGATCCAGCAATGCCGCGTGAGTGATGAAGGCCTTAGGGTTGTAAAGCTCTTTTACCCGGGATGATAATGACAGTACCGGGAGAATAAGCCCCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGGGCTAGCGTTGTTCGGAATTACTGGGCGTAAAGCGCACGTAGGCGGCTTTGTAAGTTAGAGGTGAAAGCCCGGGGCTCAACTCCGGAATTGCCTTTAAGACTGCATCGCTAGAATTGTGGAGAGGTGAGTGGAATTCCGAGTGTAGAGGTGAAATTCGTAGATATTCGGAAGAACACCAGTGGCGAAGGCGACTCACTGGACACATATTGACGCTGAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGATGACTAGCTGTCGGGGCGCTTAGCGTTTCGGTGGCGCAGCTAACGCGTTAAGTCATCCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAAGAAATTGACGGGGGCCTGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCAACGCGCAGAACCTTACCAGCGTTTGACATGGTAGGACGGTTTCCAGAGATGGATTCCTACCCTTACGGGACCTACACACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTCTTTGGTTGCTACCATTTAGTTGAGCACTCTAAAAAAACTGCCGGTGATAAGCCGGAGGAAGGTGGGGATGACGTCAAGTCCTCATAGCCCTTACGCGCTGGGCTACACACGTGCTACAATGGCGGTGACAGAGGGCAGCAAACCCGCGAGGGTGAGCTAATCTCCAAAAGCCGTCTCAGTTCGGATTGTTCTCTGCAACTCGAGAGCATGAAGGCGGAATCGCTAGTAATCGCGGATCAGCACGCCGCGGTGAATACGTTCCCAGGCCTTGTACACACCGCCCGTCACATCACGAAAGTCGGTTGCACTAGAAGTCGGTGGGCTAACCCGCAAGGGAGGCAGCCGCCTAAAGTGTGATCGGTAATTGGGGTG

```


```
$ grep '1111886' gg_13_5_taxonomy.txt

1111886 k__Bacteria; p__Proteobacteria; c__Alphaproteobacteria; o__Sphingomonadales; f__Sphingomonadaceae; g__Kaistobacter; s__
```


```
$ grep 1111886 gg_13_5_accessions.txt
1111886 Genbank JF319221.1
```

### The records of greengene database
```
$ wc -l gg_13_5_accessions.txt
1262987 gg_13_5_accessions.txt

$ cut -f 1  gg_13_5_accessions.txt | sort | uniq | wc -l
1262987

$ cut -f 3 gg_13_5_accessions.txt | sort | uniq | wc -l
1262978

$ cut -f 3 gg_13_5_accessions.txt | sort | uniq -c | sort -k 1nr | less
      2 CP002440.1
      2 NC_011386.1
      2 NC_013454.1
      2 NC_014618.1
      2 NC_014722.1
      2 NC_014724.1
      2 NC_014804.1
      2 NC_015183.1
      2 NZ_ABKJ02000039.1
      1 1FJG_A
      1 1FKA_A

```

We check that two sequences of id "CP002440.1" are identical



[JF319221.1](https://www.ncbi.nlm.nih.gov/nuccore/JF319221.1)

```
Uncultured Sphingomonadaceae bacterium clone LJ-J29 16S ribosomal RNA gene, partial sequence
GenBank: JF319221.1

FASTA Graphics PopSet
Go to:
LOCUS       JF319221                1409 bp    DNA     linear   ENV 12-JUL-2011
DEFINITION  Uncultured Sphingomonadaceae bacterium clone LJ-J29 16S ribosomal
            RNA gene, partial sequence.
ACCESSION   JF319221
VERSION     JF319221.1
KEYWORDS    ENV.
SOURCE      uncultured Sphingomonadaceae bacterium
  ORGANISM  uncultured Sphingomonadaceae bacterium
            Bacteria; Proteobacteria; Alphaproteobacteria; Sphingomonadales;
            Sphingomonadaceae; environmental samples.
REFERENCE   1  (bases 1 to 1409)
  AUTHORS   Zhao,B., Yan,J. and Liu,Q.
  TITLE     Bacterial community diversity in rhizosphere soil of chili in
            Dalian
  JOURNAL   Unpublished
REFERENCE   2  (bases 1 to 1409)
  AUTHORS   Zhao,B., Yan,J. and Liu,Q.
  TITLE     Direct Submission
  JOURNAL   Submitted (10-FEB-2011) Lifescience College, Dalian Nationalities
            University, No. 18, Dalian, Liaoning 116600, China
```


## [RDP](https://rdp.cme.msu.edu)

For the RDP. 1. Go to the website and click on "Browser": 2. Change the options if you want to include shorter sequences or low quality ones and click on "browse" 3. Click on "+" left to Bacteria if you want all the bacterial sequences, do the same for other groups if you are interested 4. Click on download and then check the options for formatting and then click your option under "Choose an alignment model for download" if you click on "Remove all gaps" the sequences will be unaligned

### [RDP sequence](https://rdp.cme.msu.edu/misc/resources.jsp)

download sequence
```
$ wget https://rdp.cme.msu.edu/download/current_Bacteria_unaligned.fa.gz --no-check-certificate
$ wget https://rdp.cme.msu.edu/download/current_Archaea_unaligned.fa.gz  --no-check-certificate
```

```
$ grep -c '^>' current_Bacteria_unaligned.fa
3196041

$ grep -c 'uncultured' current_Bacteria_unaligned.fa
2660781

$ grep  -c  'genus' current_Bacteria_unaligned.fa
2284003

$ grep  -c  'species' current_Bacteria_unaligned.fa
23

$ head current_Bacteria_unaligned.fa
>S000494589 uncultured bacterium; YRM60L1D06060904  Lineage=Root;rootrank;Bacteria;domain;"Actinobacteria";phylum;Actinobacteria;class;Acidimicrobidae;subclass;Acidimicrobiales;order;"Acidimicrobineae";suborder;Acidimicrobiaceae;family;Acidimicrobium;genus
gcggcgtgctacacatgcagtcgtacgcggtggcacaccgagtggcgaacgggtgcgtaacacgtgaggaacctaccccg
aagtgggggataacaccgggaaaccggtgctaataccgcatacgctccccggaccgcatggtccagggagcaaagcctcc
gggcgcttcgggacggcctcgcggcctatcagcttgttggtggggtaacggcccaccaaggcgacgacgggtagctggtc
tgagaggacgatcagccacactgggactgagacacggcccagactcctacgggaggcagcagtggggaatattgcgcaat
gggcgaaagcctgacgcagcaacgccgcgtggaggacgaaggccttcgggttgtaaactcctttcagcagggacgaaact
gacggtacctgcagaagaagccccggctaactacgtgccagcagccgcggtaag
>S000632122 uncultured Acidimicrobium sp.; SK297    Lineage=Root;rootrank;Bacteria;domain;"Actinobacteria";phylum;Actinobacteria;class;Acidimicrobidae;subclass;Acidimicrobiales;order;"Acidimicrobineae";suborder;Acidimicrobiaceae;family;Acidimicrobium;genus
gacgaacgctggcggcgtgcctaacacatgcaagtcgtacgcggtggcaacaccgagtggcgaacgggtgcgtaacacgt
gaggaacctaccccgaagtgggggataacaccgggaaaccggtgctaataccgcatacgctccccggaccgcatggtcca
```

* 71.5% of the seqeunce are assigned to genus, very few records were assigned to species level
* The taxonomy is not easily readable, because it is not seven levels or can not have the prefix, such as p (phylum), o (order), c (class), f (family), g (genus) and s (species).


## [SILVA](http://www.arb-silva.de)

### [SILVA_132_SSUParc](https://www.arb-silva.de/fileadmin/silva_databases/release_132/Exports/SILVA_132_SSUParc_tax_silva.fasta.gz)

The record number of SILVA database
```
$ grep -c '^>' SILVA_132_SSUParc_tax_silva.fasta
6073181
```


The record number of this database is most and the taxonomy is standard seven levels.

#### There are so many wrong assignment of taxonomy.


##### example 1:

the record in SILVA database:
```
>JQ766109.1.1426 Bacteria;Proteobacteria;Alphaproteobacteria;Rhodobacterales;Rhodobacteraceae;uncultured;Seohicola sp. JL2247
```

The record in [NCBI](https://www.ncbi.nlm.nih.gov)

```
https://www.ncbi.nlm.nih.gov/nuccore/JQ766109.1/


LOCUS       JQ766109                1426 bp    DNA     linear   BCT 09-JUN-2014
DEFINITION  Seohicola sp. JL2247 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ766109
VERSION     JQ766109.1
KEYWORDS    .
SOURCE      Seohicola sp. JL2247
  ORGANISM  Seohicola sp. JL2247
            Bacteria; Proteobacteria; Alphaproteobacteria; Rhodobacterales;
            Rhodobacteraceae; Seohaeicola.

```


##### example 2:

the record in SILVA database:
```
>JQ765935.1.710 Bacteria;Firmicutes;Bacilli;Bacillales;Family XII;Exiguobacterium;bacterium Pu.J18
```

The record in NCBI
```
https://www.ncbi.nlm.nih.gov/nuccore/JQ765935

LOCUS       JQ765935                 710 bp    DNA     linear   BCT 13-JUN-2012
DEFINITION  Bacterium Pu.J18 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ765935
VERSION     JQ765935.1
KEYWORDS    .
SOURCE      bacterium Pu.J18
  ORGANISM  bacterium Pu.J18
            Bacteria.
```



These database had a lot of brawbacks, so we should combine these database and filt the records with low quality.