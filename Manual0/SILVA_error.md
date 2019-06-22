
### There are something wrong with SILVA database

#### get species name

```
$ grep '^>' SILVA_132_SSUParc_tax_silva.fasta  | cut  -d";"  -f 7 | cut -d" " -f 1 | sort | uniq -c | sort -k 1nr > species
```


```
$ less species

3794714 uncultured
 921647 
  87712 Bacillus
  64576 Arthropoda
  56554 Glomeromycetes
  48410 Pseudomonas
  43257 Pezizomycotina
  40618 metagenome
  37966 bacterium
  33718 Staphylococcus
  32405 Streptococcus
  30959 Streptomyces
  23099 Nematoda
  22711 Lactobacillus
  22131 Embryophyta
  21760 unidentified
  19499 Escherichia

```


```
Firmicutes 硬壁菌门
Bacilli 杆状菌；芽孢杆菌 名词bacillus的复数形式.
Bacillaceae 芽胞杆菌科
Bacillus  杆状菌；细菌

Proteobacteria 变形杆菌
```

#### Bacillus
```
$ grep Bacillus SILVA_132_SSUParc_tax_silva.fasta | cut  -d ";" -f 2 | sort | uniq -c | sort -k 1nr > Bacillus
```

```
$ cat Bacillus
 127706 Firmicutes
    464 Proteobacteria
    102 Actinobacteria
     16 Opisthokonta
     14 Bacteroidetes
      9 Acidobacteria
      9 Planctomycetes
      8 Gemmatimonadetes
      7 Cyanobacteria
      3 Tenericutes
      2 Patescibacteria
      2 Spirochaetes
      1 Aquificae
      1 Archaeplastida
      1 Caldiserica
      1 Chloroflexi
      1 Dependentiae
      1 Epsilonbacteraeota
      1 Fusobacteria
      1 Omnitrophicaeota
      1 Synergistetes
      1 Verrucomicrobia

```

#### uncultured
```
$ grep uncultured SILVA_132_SSUParc_tax_silva.fasta | cut  -d ";" -f 2 | sort | uniq -c | sort -k 1nr > uncultured

$ less uncultured

$ cat uncultured
1569363 Proteobacteria
 900843 Firmicutes
 606608 Bacteroidetes
 416633 Actinobacteria
 165858 Acidobacteria
 140309 Opisthokonta
 131272 Euryarchaeota
 116986 Chloroflexi
 103121 Cyanobacteria
  83974 Planctomycetes
  83307 SAR
  49608 Spirochaetes
  48907 Thaumarchaeota
  45338 Patescibacteria
  41659 Verrucomicrobia
  31778 Crenarchaeota
  25628 Nitrospirae
  25529 Epsilonbacteraeota
  22921 Cloacimonetes
  21936 Fusobacteria

```


#### metagenome
```
$ grep metagenome SILVA_132_SSUParc_tax_silva.fasta | cut  -d ";" -f 2 | sort | uniq -c | sort -k 1nr > metagenome

$ less metagenome
  26894 Proteobacteria
   5909 Actinobacteria
   5151 Bacteroidetes
   5118 Firmicutes
   3507 Opisthokonta
   2898 SAR
   2432 Acidobacteria
   1921 Euryarchaeota
   1572 Verrucomicrobia
   1231 Chloroflexi
   1046 Planctomycetes
    743 Amoebozoa
    728 Cyanobacteria
    462 Patescibacteria
    458 Gemmatimonadetes
```

#### bacterium

```
$ grep bacterium SILVA_132_SSUParc_tax_silva.fasta | cut  -d ";" -f 2 | sort | uniq -c | sort -k 1nr > bacterium
```

```
$ less bacterium
1369923 Proteobacteria
 804919 Firmicutes
 552623 Bacteroidetes
 441204 Actinobacteria
 158494 Acidobacteria
  93668 Chloroflexi
  78466 Cyanobacteria
  60479 Planctomycetes
  39425 Patescibacteria

```



```
>AJWY01005931.408.716 Bacteria;Firmicutes;Clostridia;Clostridiales;Ruminococcaceae;Faecalibacterium;human gut metagenome
>AJXC01109023.1.884 Bacteria;Chloroflexi;Dehalococcoidia;SAR202 clade;marine metagenome
>CXTH01000052.1.935 Bacteria;Actinobacteria;Actinobacteria;Bifidobacteriales;Bifidobacteriaceae;Bifidobacterium;human gut metagenome
```


#### There are just six levels 
SILVA 
```
>JQ769119.1.1447        Bacteria;Cyanobacteria;Oxyphotobacteria;Nostocales;Phormidiaceae;Tychonema CCAP
AAACTCCTTTTCTCTGGGAAGAACAAAATGACGGTACCAGAGGAATCAGCATCGGCTAACTCCGTGCCAGCAGCCGCGGTAAGACGGAGGATGCAAGCGTTATCCGGAATGATTGGGCGTAAAGCGT
```

NCBI 
```
GenBank: JQ769119.1

FASTA Graphics PopSet
 LOCUS       JQ769119                1447 bp    DNA     linear   BCT 04-JUN-2012
DEFINITION  Phormidium autumnale sv26 16S ribosomal RNA gene and 16S-23S
            ribosomal RNA intergenic spacer, partial sequence.
ACCESSION   JQ769119
VERSION     JQ769119.1
KEYWORDS    .
SOURCE      Phormidium autumnale sv26
  ORGANISM  Phormidium autumnale sv26
            Bacteria; Cyanobacteria; Oscillatoriophycideae; Oscillatoriales;
            Oscillatoriaceae; Phormidium.
```


```
>JQ769113.1.1445        Bacteria;Cyanobacteria;Oxyphotobacteria;Nostocales;Phormidiaceae;Tychonema CCAP


GenBank: JQ769113.1

FASTA Graphics PopSet
 LOCUS       JQ769113                1445 bp    DNA     linear   BCT 04-JUN-2012
DEFINITION  Phormidium autumnale sv17 16S ribosomal RNA gene and 16S-23S
            ribosomal RNA intergenic spacer, partial sequence.
ACCESSION   JQ769113
VERSION     JQ769113.1
KEYWORDS    .
SOURCE      Phormidium autumnale sv17
  ORGANISM  Phormidium autumnale sv17
            Bacteria; Cyanobacteria; Oscillatoriophycideae; Oscillatoriales;
            Oscillatoriaceae; Phormidium.
```


#### Genus and start of species are not identical

>JQ765415.1.1444 Bacteria;Proteobacteria;Gammaproteobacteria;Enterobacteriales;Enterobacteriaceae;Kosakonia;Enterobacter sp. MLB05

LOCUS       JQ765415                1444 bp    DNA     linear   BCT 09-JUN-2012
DEFINITION  Enterobacter sp. MLB05 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ765415
VERSION     JQ765415.1
KEYWORDS    .
SOURCE      Enterobacter sp. MLB05
  ORGANISM  Enterobacter sp. MLB05
            Bacteria; Proteobacteria; Gammaproteobacteria; Enterobacterales;
            Enterobacteriaceae; Enterobacter.
            

#### Species starts with "bacterium"         
            
>JQ765442.1.829 Bacteria;Firmicutes;Bacilli;Bacillales;Bacillaceae;Bacillus;bacterium FA_183B

LOCUS       JQ765442                 829 bp    DNA     linear   BCT 24-MAY-2012
DEFINITION  Bacterium FA_183B 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ765442
VERSION     JQ765442.1
KEYWORDS    .
SOURCE      bacterium FA_183B
  ORGANISM  bacterium FA_183B
            Bacteria.


#### difference for this txonomy and NCBI
```
>JQ772017.1.1246        Bacteria;Tenericutes;Mollicutes;Mollicutes Incertae Sedis;Unknown Family;Candidatus Phytoplasma
GAAACGACTGCTAAGACTGGATAGGAGACAAGAAGGCATCTTCTTGTTTTTAAAAGACCTAGCAATAGGTATGCTTAGGGAGGAGCTTGCGTCACATTAGTTAGTTGGTGGGGTAAAGGCCTACCA
```


```
'Tilia platyphyllos' phytoplasma strain LindenLL (1) 16S ribosomal RNA gene, partial sequence
GenBank: JQ772017.1

FASTA Graphics
 LOCUS       JQ772017                1246 bp    DNA     linear   BCT 12-DEC-2012
DEFINITION  'Tilia platyphyllos' phytoplasma strain LindenLL (1) 16S ribosomal
            RNA gene, partial sequence.
ACCESSION   JQ772017
VERSION     JQ772017.1
KEYWORDS    .
SOURCE      'Tilia platyphyllos' phytoplasma
  ORGANISM  'Tilia platyphyllos' phytoplasma
            Bacteria; Tenericutes; Mollicutes; Acholeplasmatales;
            Acholeplasmataceae; Candidatus Phytoplasma; Candidatus Phytoplasma
            asteris.
```




```
>JQ796723.1.1397        Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhizobiales Incertae Sedis;Phreatobacter


LOCUS       JQ796723                1397 bp    DNA     linear   BCT 16-MAY-2012
DEFINITION  Rhizobiales bacterium NHI-8 16S ribosomal RNA gene, partial
            sequence.
ACCESSION   JQ796723
VERSION     JQ796723.1
KEYWORDS    .
SOURCE      Rhizobiales bacterium NHI-8
  ORGANISM  Rhizobiales bacterium NHI-8
            Bacteria; Proteobacteria; Alphaproteobacteria; Rhizobiales.

```


```
>JQ806741.1.1303        Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhizobiales Incertae Sedis;Anderseniella


GenBank: JQ806741.1

FASTA Graphics
 LOCUS       JQ806741                1303 bp    DNA     linear   BCT 01-JAN-2014
DEFINITION  Rhodobium sp. MGS3-3 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ806741
VERSION     JQ806741.1
KEYWORDS    .
SOURCE      Rhodobium sp. MGS3-3
  ORGANISM  Rhodobium sp. MGS3-3
            Bacteria; Proteobacteria; Alphaproteobacteria; Rhizobiales;
            Rhodobiaceae; Rhodobium.


https://www.ncbi.nlm.nih.gov/nuccore/JQ806741.1
```


```

>JQ899057.1.1257 Bacteria;Cyanobacteria;Oxyphotobacteria;Nostocales;Phormidiaceae;Trichodesmium IMS101;Okeania sp. PAC-18-Feb-10-2

GenBank: JQ899057.1

FASTA Graphics
 LOCUS       JQ899057                1257 bp    DNA     linear   BCT 12-FEB-2014
DEFINITION  Okeania sp. PAC-18-Feb-10-2 16S ribosomal RNA gene, partial
            sequence.
ACCESSION   JQ899057
VERSION     JQ899057.1
KEYWORDS    .
SOURCE      Okeania sp. PAC-18-Feb-10-2
  ORGANISM  Okeania sp. PAC-18-Feb-10-2
            Bacteria; Cyanobacteria; Oscillatoriophycideae; Oscillatoriales;
            Oscillatoriaceae; Okeania.
```

```
>JQ765887.1.642 Bacteria;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;bacterium Co.J13
UCCUANCAUGCAAGUCGAACGCGCAGCGAGAGGUGCUUGCACCUUUCAAGCGAGUGGCGAACGGGUGAGUAACACGUGGA
UAACCUGCCUCAAGGCUGGGGAUAACAUUUGGAAACAGAUGCUAAUACCGAAUAAAACUUAGUAUCGCAUGAUAUCAAGU
UAAAAGGCGCUACGGCGUCACCUAGAGAUGGAUCCGCGGUGCAUUAGUUAGUUGGUGGGGUAAAGGCUUACCAAGACGAU
GAUGCAUAGCCGAGUUGAGAGACUGAUCGGCCACAUUGGGACUGAGACACGGCCCAAACUCCUACGGGAGGCUGCAGUAG
GGAAUCUUCCACAAUGGGCGCAAGCCUGAUGGAGCAACGCCGCGUGUGUGAUGAAGGCUUUCGGGUCGUAAAGCACUGUU
GUAUGGGAAGAAAUGCUAAAAUAGGGAAUGAUUUUAGUUUGACGGUACCAUACCAGAAAGGGACGGCUAAAUACGUGCCA
GCAGCCGCGGUAAUACGUAUGUCCCGAGCGUUAUCCGGAUUUAUUGGGCGUAAAGCGAGCGCAGACGGUUGAUUAAGUCU
GAUGUGAAAGCCCGGAGCUCAACUCCGGAAUGGCAUUGGAAACUGGUUAACUUGAGUGUUGUAGAGGUAAGUGGAACUCC
AU


GenBank: JQ765887.1

FASTA Graphics PopSet
Go to:
LOCUS       JQ765887                 642 bp    DNA     linear   BCT 13-JUN-2012
DEFINITION  Bacterium Co.J13 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ765887
VERSION     JQ765887.1
KEYWORDS    .
SOURCE      bacterium Co.J13
  ORGANISM  bacterium Co.J13
            Bacteria.
```


```
>GY194061.5315.6843 Bacteria;Firmicutes;Bacilli;Lactobacillales;Streptococcaceae;Streptococcus;unidentified

GenBank: GY194061.1

FASTA Graphics
Go to:
LOCUS       GY194061                8172 bp    DNA     linear   PAT 23-MAY-2011
DEFINITION  Sequence 12019 from patent US 7939087.
ACCESSION   GY194061
VERSION     GY194061.1
KEYWORDS    .
SOURCE      Unknown.
  ORGANISM  Unknown.
            Unclassified.
REFERENCE   1  (bases 1 to 8172)
  AUTHORS   Telford,J., Masignani,V., Scarselli,M., Grandi,G., Tettelin,H. and
            Fraser,C.
  TITLE     Nucleic acids and proteins from Streptococcus groups A & B
  JOURNAL   Patent: US 7939087-B2 12019 10-MAY-2011;
            Novartis Vaccines and Diagnostics, Inc.; Emeryville, CA
```



### different taxonomy
```
    >AY584513.1.2387 Bacteria;Cyanobacteria;Oxyphotobacteria;Nostocales;Nostocaceae;Nodularia PCC-9350;Nodularia harveyana CCAP 1452/1

GenBank: AY584513.1

FASTA Graphics PopSet
 LOCUS       AY584513                2387 bp    DNA     linear   BCT 25-JUL-2007
DEFINITION  Nodularia harveyana CCAP 1452/1 23S ribosomal RNA gene, partial
            sequence.
ACCESSION   AY584513
VERSION     AY584513.1
KEYWORDS    .
SOURCE      Nodularia harveyana CCAP 1452/1
  ORGANISM  Nodularia harveyana CCAP 1452/1
            Bacteria; Cyanobacteria; Nostocales; Aphanizomenonaceae; Nodularia.


```


```
>JQ765423.1.1445 Bacteria;Proteobacteria;Gammaproteobacteria;Enterobacteriales;Enterobacteriaceae;Kosakonia;Enterobacter sp. MLB27

GenBank: JQ765423.1

FASTA Graphics
Go to:
LOCUS       JQ765423                1445 bp    DNA     linear   BCT 09-JUN-2012
DEFINITION  Enterobacter sp. MLB27 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ765423
VERSION     JQ765423.1
KEYWORDS    .
SOURCE      Enterobacter sp. MLB27
  ORGANISM  Enterobacter sp. MLB27
            Bacteria; Proteobacteria; Gammaproteobacteria; Enterobacterales;
            Enterobacteriaceae; Enterobacter.
```


```
>JQ765430.1.1439 Bacteria;Proteobacteria;Gammaproteobacteria;Betaproteobacteriales;Burkholderiaceae;Burkholderia-Caballeronia-Paraburkholderia;Paraburkholderia fungorum


GenBank: JQ765430.1

FASTA Graphics PopSet
Go to:
LOCUS       JQ765430                1439 bp    DNA     linear   BCT 09-JUN-2012
DEFINITION  Burkholderia fungorum strain BH113 16S ribosomal RNA gene, partial
            sequence.
ACCESSION   JQ765430
VERSION     JQ765430.1
KEYWORDS    .
SOURCE      Paraburkholderia fungorum
  ORGANISM  Paraburkholderia fungorum
            Bacteria; Proteobacteria; Betaproteobacteria; Burkholderiales;
            Burkholderiaceae; Paraburkholderia.
REFERENCE   1  (bases 1 to 1439)
```



```
>JQ765861.1.899 Bacteria;Firmicutes;Bacilli;Lactobacillales;Streptococcaceae;Lactococcus;Lactococcus lactis subsp. lactis


GenBank: JQ765861.1

FASTA Graphics
 LOCUS       JQ765861                 899 bp    DNA     linear   BCT 02-NOV-2012
DEFINITION  Lactococcus lactis subsp. lactis strain STG45 16S ribosomal RNA
            gene, partial sequence.
ACCESSION   JQ765861
VERSION     JQ765861.1
KEYWORDS    .
SOURCE      Lactococcus lactis subsp. lactis
  ORGANISM  Lactococcus lactis subsp. lactis
            Bacteria; Firmicutes; Bacilli; Lactobacillales; Streptococcaceae;
            Lactococcus.
REFERENCE   1  (bases 1 to 899)
```


```
>JQ766030.1.600 Bacteria;Proteobacteria;Gammaproteobacteria;Enterobacteriales;Enterobacteriaceae;Kosakonia;bacterium Co.S1

GenBank: JQ766030.1

FASTA Graphics PopSet
Go to:
LOCUS       JQ766030                 600 bp    DNA     linear   BCT 13-JUN-2012
DEFINITION  Bacterium Co.S1 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ766030
VERSION     JQ766030.1
KEYWORDS    .
SOURCE      bacterium Co.S1
  ORGANISM  bacterium Co.S1
            Bacteria.
REFERENCE   1  (bases 1 to 600)
```


```
>AC200763.88363.89885 Bacteria;Proteobacteria;Gammaproteobacteria;Enterobacteriales;Enterobacteriaceae;Candidatus Regiella;Candidatus Regiella insecticola



GenBank: AC200763.1

FASTA Graphics
 LOCUS       AC200763               96078 bp    DNA     linear   HTG 14-APR-2007
DEFINITION  Candidatus Regiella insecticola clone CUGI_APP_BA-001J20, WORKING
            DRAFT SEQUENCE.
ACCESSION   AC200763
VERSION     AC200763.1
KEYWORDS    HTG; HTGS_PHASE2; HTGS_DRAFT; HTGS_FULLTOP.
SOURCE      Candidatus Regiella insecticola (Candidatus Adiaceo aphidicola)
  ORGANISM  Candidatus Regiella insecticola
            Bacteria; Proteobacteria; Gammaproteobacteria; Enterobacterales;
            Enterobacteriaceae; aphid secondary symbionts; Candidatus Regiella.
```



```
>JQ765632.1.1331 Bacteria;Spirochaetes;Leptospirae;Leptospirales;Leptospiraceae;Leptospira;Leptospira interrogans serovar Hardjo-prajitno


GenBank: JQ765632.1

FASTA Graphics PopSet
 LOCUS       JQ765632                1331 bp    DNA     linear   BCT 05-JUN-2012
DEFINITION  Leptospira interrogans serovar Hardjo-prajitno strain Lagoa 16S
            ribosomal RNA gene, partial sequence.
ACCESSION   JQ765632
VERSION     JQ765632.1
KEYWORDS    .
SOURCE      Leptospira interrogans serovar Hardjo-prajitno
  ORGANISM  Leptospira interrogans serovar Hardjo-prajitno
            Bacteria; Spirochaetes; Leptospirales; Leptospiraceae; Leptospira.
REFERENCE   1  (bases 1 to 1331)


Lineage( full )
cellular organisms; Bacteria; Spirochaetes; Spirochaetia; Leptospirales; Leptospiraceae; Leptospira; Leptospira interrogans; Leptospira interrogans serovar Hardjo
```


```
>JQ765935.1.710 Bacteria;Firmicutes;Bacilli;Bacillales;Family XII;Exiguobacterium;bacterium Pu.J18


GenBank: JQ765935.1

FASTA Graphics PopSet
Go to:
LOCUS       JQ765935                 710 bp    DNA     linear   BCT 13-JUN-2012
DEFINITION  Bacterium Pu.J18 16S ribosomal RNA gene, partial sequence.
ACCESSION   JQ765935
VERSION     JQ765935.1
KEYWORDS    .
SOURCE      bacterium Pu.J18
  ORGANISM  bacterium Pu.J18
            Bacteria.
REFERENCE   1  (bases 1 to 710)
```


```
>JQ766310.1.1245 Bacteria;Tenericutes;Mollicutes;Mollicutes Incertae Sedis;Unknown Family;Candidatus Phytoplasma;Begonia shoot proliferation phytoplasma


LOCUS       JQ766310                1245 bp    DNA     linear   BCT 09-JUN-2012
DEFINITION  Begonia shoot proliferation phytoplasma clone BeSP-Br01 16S
            ribosomal RNA gene, partial sequence.
ACCESSION   JQ766310
VERSION     JQ766310.1
KEYWORDS    .
SOURCE      Begonia shoot proliferation phytoplasma
  ORGANISM  Begonia shoot proliferation phytoplasma
            Bacteria; Tenericutes; Mollicutes; Acholeplasmatales;
            Acholeplasmataceae; Candidatus Phytoplasma; 16SrIII (X-disease
            group).
REFERENCE   1  (bases 1 to 1245)
```

```
>JQ829387.1.517 Bacteria;Proteobacteria;Gammaproteobacteria;Enterobacteriales;Enterobacteriaceae;Enterobacter;Klebsiella aerogenes


Go to:
LOCUS       JQ829387                 517 bp    DNA     linear   BCT 04-JUN-2012
DEFINITION  Enterobacter aerogenes strain p62_D05 16S ribosomal RNA gene,
            partial sequence.
ACCESSION   JQ829387
VERSION     JQ829387.1
KEYWORDS    .
SOURCE      Klebsiella aerogenes
  ORGANISM  Klebsiella aerogenes
            Bacteria; Proteobacteria; Gammaproteobacteria; Enterobacterales;
            Enterobacteriaceae; Klebsiella.
REFERENCE   1  (bases 1 to 517)
```


```
>JQ791566.1.700 Bacteria;Proteobacteria;Gammaproteobacteria;Betaproteobacteriales;Burkholderiaceae;Undibacterium;Undibacterium sp. BF-GEL-BP9


GenBank: JQ791566.1

FASTA Graphics PopSet
 LOCUS       JQ791566                 700 bp    DNA     linear   BCT 04-APR-2014
DEFINITION  Undibacterium sp. BF-GEL-BP9 16S ribosomal RNA gene, partial
            sequence.
ACCESSION   JQ791566
VERSION     JQ791566.1
KEYWORDS    .
SOURCE      Undibacterium sp. BF-GEL-BP9
  ORGANISM  Undibacterium sp. BF-GEL-BP9
            Bacteria; Proteobacteria; Betaproteobacteria; Burkholderiales;
            Oxalobacteraceae; Undibacterium.
```


### species without high level taxonomy
```
$ grep 'GCF_000427465.1' assembly_summary.txt
GCF_000427465.1 PRJNA224116 SAMN02440592    ATYB00000000.1  na  935557  76745   Sinorhizobium arboris LMG 14919 strain=LMG 14919     latest Scaffold    Major   Full    2013/07/15  ASM42746v1  JGI GCA_000427465.1 identical   ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/427/465/GCF_000427465.1_ASM42746v1       assembly from type material
```

eight levels
```
$ grep 'Sinorhizobium arboris' SILVA_132_SSUParc_tax_silva_DNA.fasta
>ATYB01000014.3370398.3371862 Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhizobiaceae;Ensifer;Sinorhizobium arboris LMG 14919
>ATYB01000014.2915529.2916993 Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhizobiaceae;Ensifer;Sinorhizobium arboris LMG 14919
>ATYB01000014.2468447.2469911 Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhizobiaceae;Ensifer;Sinorhizobium arboris LMG 14919

```


```
>KX955231.1.902 Bacteria;Cyanobacteria;Oxyphotobacteria;Nostocales;Nostocaceae;Cylindrospermopsis CRJ1;Cylindrospermopsis raciborskii TZ-1
>KX955233.1.901 Bacteria;Cyanobacteria;Oxyphotobacteria;Nostocales;Nostocaceae;Cylindrospermopsis CRJ1;Cylindrospermopsis raciborskii UP
```


```
$ grep 'Prevotella bryantii' SILVA_132_SSUParc_tax_silva_DNA.fasta
>AY189149.1.920 Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella 1;Prevotella bryantii
>AF396925.1.1518 Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella 1;Prevotella bryantii
>AJ006457.1.1486 Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella 1;Prevotella bryantii
```

```
$ grep 'GCF_000144625.1' assembly_summary.txt
GCF_000144625.1 PRJNA224116 SAMN00017134        representative genome   610130  84030   [Clostridium] saccharolyticum WM1   strain=WM1      latest  Complete Genome Major   Full    2010/08/05  ASM14462v1  US DOE Joint Genome Institute   GCA_000144625.1 identical   ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/144/625/GCF_000144625.1_ASM14462v1       assembly from type material


>KJ194894.1.1072 Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae;Lachnoclostridium 5;[Clostridium] saccharolyticum
>LF133655.1.1511 Bacteria;Firmicutes;Clostridia;Clostridiales;Lachnospiraceae;Lachnoclostridium 5;[Clostridium] saccharolyticum
>KM972403.1.903 Bacteria;Firmicutes;Clostridia;Thermoanaerobacterales;Family III;Thermoanaerobacterium;Thermoanaerobacterium thermosaccharolyticum
```


