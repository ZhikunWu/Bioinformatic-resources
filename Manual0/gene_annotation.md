# 基因注释数据库构建 (2018.05.18)

## [idmapping file](ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/)

### [idmapping readme file](ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/README)

one record per line
```
This file has three columns, delimited by tab:
1. UniProtKB-AC 
2. ID_type 
3. ID
```

The ID_type list:
```
1. UniProtKB-AC
2. UniProtKB-ID
3. GeneID (EntrezGene)
4. RefSeq
5. GI
6. PDB
7. GO
8. UniRef100
9. UniRef90
10. UniRef50
11. UniParc
12. PIR
13. NCBI-taxon
14. MIM
15. UniGene
16. PubMed
17. EMBL
18. EMBL-CDS
19. Ensembl
20. Ensembl_TRS
21. Ensembl_PRO
22. Additional PubMed
```


## The gene id from gff3 file in Ensembl  is identical to different labels in **idmapping** database

* The genes in animal may be identical to **Ensembl**, genes in plant to **EnsemblGenome**,
and genes in bacterial to **Gene_ORFName** or **EnsemblGenome**

#### 人类中基因对应Ensembl

```
$ grep ENSG00000187961 idmapping.dat
Q6TDP4  Ensembl ENSG00000187961
Q6TDP4  EuPathDB    HostDB:ENSG00000187961.13
Q0VGE6  Ensembl ENSG00000187961
Q0VGE6  EuPathDB    HostDB:ENSG00000187961.13
J3QLT4  Ensembl ENSG00000187961
J3QLT4  EuPathDB    HostDB:ENSG00000187961.13
```

#### 小鼠中基因对应Ensembl
```
$ grep ENSMUSG00000041809 idmapping.dat
B2CKC6  Ensembl ENSMUSG00000041809
```

#### 大鼠中基因对应Ensembl
```
$ grep ENSRNOG00000061316 idmapping.dat
A0A0G2K5L0  Ensembl ENSRNOG00000061316

$ grep ENSRNOG00000050129 idmapping.dat
M0RCY4  Ensembl ENSRNOG00000050129

```

#### 斑马鱼基因对应Ensembl
```
$ grep ENSDARG00000103783 idmapping.dat
Q6NYG4  Ensembl ENSDARG00000103783
```

#### 鸡基因对应Ensembl
```
$ grep ENSGALG00000045540 idmapping.dat
A0A1L1RTX2  Ensembl ENSGALG00000045540
```


#### 拟南芥基因对应EnsemblGenome
```
$ grep AT1G01010 idmapping.dat
Q0WV96  STRING  3702.AT1G01010.1
Q0WV96  EnsemblGenome   AT1G01010
Q0WV96  EnsemblGenome_TRS   AT1G01010.1
Q0WV96  EnsemblGenome_PRO   AT1G01010.1
Q0WV96  KEGG    ath:AT1G01010
Q0WV96  Araport AT1G01010
A0A178WAE4  EnsemblGenome   AT1G01010
A0A178WAE4  KEGG    ath:AT1G01010
```

#### 黄瓜基因对应EnsemblGenome
```
$ grep Csa_1G000010 idmapping.dat
A0A0A0LTV1  Gene_ORFName    Csa_1G000010
A0A0A0LTV1  EnsemblGenome   Csa_1G000010
```

#### 二穗短柄草基因对应EnsemblGenome
```
$ grep BRADI1G00200 idmapping.dat
I1GKD6  STRING  15368.BRADI1G00200.1
I1GKD6  EnsemblGenome   BRADI1G00200
```

#### 番茄基因对应EnsemblGenome
```
$ grep Solyc01g005000.2 idmapping.dat
B1Q3F2  STRING  4081.Solyc01g005000.2.1
B1Q3F2  EnsemblGenome   Solyc01g005000.2
```

#### 玉米基因对应EnsemblGenome
```
$ grep Zm00001d027230 idmapping.dat
A0A1D6JJ64  Gene_ORFName    ZEAMMB73_Zm00001d027230
A0A1D6JJ64  EnsemblGenome   Zm00001d027230
A0A1D6JJ64  EnsemblGenome_TRS   Zm00001d027230_T001
A0A1D6JJ64  EnsemblGenome_PRO   Zm00001d027230_P001

```

#### 高粱（sorghum_bicolor）基因对应Gene_ORFName和EnsemblGenome
```
$ grep SORBI_3001G000200  idmapping.dat
C5WR13  Gene_ORFName    SORBI_3001G000200
C5WR13  EnsemblGenome   SORBI_3001G000200

$ grep SORBI_3001G000300  idmapping.dat
A0A1B6QGK8  Gene_ORFName    SORBI_3001G000300
A0A1B6QGK8  EnsemblGenome   SORBI_3001G000300
```


#### 马铃薯（solanum tuberosum）基因对应EnsemblGenome
```
$ grep PGSC0003DMG400015133  idmapping.dat
M1B7U5  EnsemblGenome   PGSC0003DMG400015133
```



#### 禾谷镰刀菌基因（fusarium graminearum）对应Gene_ORFName
```
$ grep FGRAMPH1_01T00001  idmapping.dat
A0A1C3YHY7  Gene_ORFName    FGRAMPH1_01T00001

$ grep FGRAMPH1_01T00011  idmapping.dat
I1S429  Gene_ORFName    FGRAMPH1_01T00011

```

#### 小麦条锈菌基因（Puccinia striiformis) 对应Gene_ORFName和EnsemblGenome

```
$ grep PSTG_40005  idmapping.dat
A0A0L0W5Z1  Gene_ORFName    PSTG_40005
A0A0L0W5Z1  EnsemblGenome   PSTG_40005

$ grep PSTG_40010  idmapping.dat
A0A0L0W5V4  Gene_ORFName    PSTG_40010
A0A0L0W5V4  EnsemblGenome   PSTG_40010
```

#### Acinetobacter_baumannii（鲍曼不动杆菌）基因对应Gene_ORFName和EnsemblGenome
```
$ grep IX87_00055  idmapping.dat
A0A0E1FGF8  Gene_ORFName    IX87_00055
A0A0E1FGF8  EnsemblGenome   IX87_00055
A0A0E1FGF8  KEGG    abau:IX87_00055
```

#### Suillus luteus（褐环粘盖牛肝菌）基因对应Gene_ORFName和EnsemblGenome
```
$ grep CY34DRAFT_7286  idmapping.dat
A0A0D0C3J9  Gene_ORFName    CY34DRAFT_7286
A0A0D0C3J9  EnsemblGenome   CY34DRAFT_7286
```



## gff3获得的数据库
```sql
$ sqlite3 Zea_mays.AGPv4.37_gff3.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .tables
GeneAnno   GeneTrans
sqlite> select * from GeneAnno limit 5;
Zm00001d027230|1|44289|49837|+|NULL|protein_coding|Mitochondrial transcription termination factor family protein
Zm00001d027231|1|50877|55716|-|NULL|protein_coding|OSJNBa0093O08.6 protein%3B  protein
Zm00001d027232|1|92299|95134|-|NULL|protein_coding|NULL
Zm00001d027233|1|111655|118312|-|NULL|protein_coding|NULL
Zm00001d027234|1|118683|119739|-|NULL|protein_coding|NULL
```


## KO in KOBAS
```sql
$ sqlite3 ko.db 
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .table
GeneKOmap           KoGenes             KoUniprotkbAcs    
KoEnsemblGeneIds    KoPathways          Kos               
KoEntrezGeneIds     KoRefSeqProteinIds  Pathways

sqlite> select * from KoPathways limit 2;
koid|pid
K00123|ko00630
K04632|ko04270 

sqlite> select * from Pathways limit 2;
pid|name
ko04062|Chemokine signaling pathway
ko04060|Cytokine-cytokine receptor interaction
```

## uniprot gaf database have the record with UniprotKB to GO term
```
$ grep -c '^UniProtKB' goa_uniprot_all.gaf 
494827336


$ wc -l goa_uniprot_all.gaf
494843807 goa_uniprot_all.gaf

```
most the records have the UniprotKB id


### get GO term database
```
python Term2db.py --term term.txt --database term.db
```
output term.db
```
sqlite> .schema
CREATE TABLE GODescription
        (go_id text,
        go_level text,
        go_description text);
CREATE INDEX go_term
        on GODescription (go_id);

sqlite> select * from GODescription limit 5;
go_id|go_level|go_description
GO:0071138|cellular_component|alpha5-beta5-fibronectin-SFRP2 complex
GO:1900561|biological_process|dehydroaustinol metabolic process
GO:2001305|biological_process|xanthone-containing compound metabolic process
GO:0043087|biological_process|regulation of GTPase activity
GO:0036313|molecular_function|phosphatidylinositol 3-kinase catalytic subunit binding
```

There are 47141 records in the GO term database
```
$ cut -f 4 term.txt  | uniq |sort | uniq | grep 'GO' | wc -l
47141

sqlite> select count(distinct go_id) from GODescription limit 5 ;
count(distinct go_id)
47141
```



## get the annotation database through merging these database

```sql
$ sqlite3 /home/wzk/database/GENOME/maize/Zea_mays.AGPv4.37_GeneAnno_Anno.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .tables
Ensembl        EnsemblTrans   GeneID         GeneUniProtKB  KO           
EnsemblGene    GeneAnno       GeneName       GeneUniprotAc  RefSeq       
EnsemblPro     GeneGO         GeneORFName    KEGG           eggNOG 

sqlite> select * from Ensembl  limit 2;

sqlite> select * from EnsemblTrans  limit 2;
gene_id|EnsemblTrans_id
Zm00001d027230|Zm00001d027230_T001
Zm00001d027231|Zm00001d027231_T001

sqlite> select * from GeneID  limit 2;
gene_id|Geneid
Zm00001d027231|100382519
Zm00001d027267|100193420

sqlite> select * from GeneUniProtKB  limit 2;
gene_id|uniprotKB_id
Zm00001d027230|A0A1D6JJ64_MAIZE
Zm00001d027231|A0A1D6JJ65_MAIZE

sqlite> select * from KO  limit 2;
gene_id|KO_id
Zm00001d027276|K00344
Zm00001d027285|K14638


sqlite> select * from EnsemblGene  limit 2;
gene_id|EnsemblGene_id
Zm00001d027230|Zm00001d027230
Zm00001d027231|Zm00001d027231

sqlite> select * from GeneAnno  limit 2;
gene_id|chr_id|start_pos|end_pos|strand|symbol|biotype|description
Zm00001d027230|1|44289|49837|+|NULL|protein_coding|Mitochondrial transcription termination factor family protein
Zm00001d027231|1|50877|55716|-|NULL|protein_coding|OSJNBa0093O08.6 protein%3B  protein

sqlite> select * from GeneName  limit 2;


sqlite> select * from GeneUniprotAc  limit 2;
gene_id|uniprotAc
Zm00001d027230|A0A1D6JJ64
Zm00001d027231|A0A1D6JJ65

sqlite> select * from RefSeq  limit 2;
gene_id|Refseq_id
Zm00001d027231|NP_001168727.1
Zm00001d027231|XP_008644051.1

gene_id|EnsemblPro_id
Zm00001d027230|Zm00001d027230_P001
Zm00001d027231|Zm00001d027231_P001

sqlite> select * from GeneGO  limit 2;
gene_id|go_id
Zm00001d027230|GO:0003690
Zm00001d027230|GO:0006355

sqlite> select * from GeneORFName  limit 2;
gene_id|ORFName_id
Zm00001d027230|ZEAMMB73_Zm00001d027230
Zm00001d027231|ZEAMMB73_Zm00001d027231

sqlite> select * from KEGG  limit 2;
gene_id|kegg_id
Zm00001d027231|zma:100382519
Zm00001d027268|zma:100283177

sqlite> select * from eggNOG  limit 2;
gene_id|eggNOG_id
Zm00001d027231|KOG1724
Zm00001d027231|COG5201
```


### some genes with no uniprot_Ac id were not in annotation database
```sql
sqlite> select count(distinct gene_id) from GeneUniprotAc;
count(distinct gene_id)
39468

sqlite> select count(distinct gene_id) from GeneUniProtKB;
count(distinct gene_id)
39468

sqlite> select count(distinct gene_id) from EnsemblGene;
count(distinct gene_id)
39468
```

genes have the same number of ids for UniprotAc, UniProtKB and EnsemblGene

there are 30 genes do not have the ids of uniprotAc
```sql
sqlite> select gene_id  from GeneAnno where gene_id not in (select gene_id from GeneUniprotAc) limit 5;
Zm00001d030401
Zm00001d024227
Zm00001d025403
Zm00001d040572
Zm00001d013852

sqlite> select count(gene_id)  from GeneAnno where gene_id not in (select gene_id from GeneUniprotAc);
30
```




### 玉米注释结果
```
$ head  /home/wzk/database/GENOME/maize/Zea_mays.AGPv4.37_GeneAnno_Anno_description.xls

Gene    Chr Start   End Strand  Symbol  Biotype Description uniprotAc   GO(GO_term,class,description)   KEGG(KO,pathway,description)
GRMZM5G801074   Pt  66998   67198   +   rpl33   protein_coding  50S ribosomal protein L33%2C chloroplastic [Source:UniProtKB/Swiss-Prot%3BAcc:P25461]   P25461  GO:0003735,molecular_function,structural constituent of ribosome;GO:0005622,cellular_component,intracellular;GO:0005840,cellular_component,ribosome;GO:0006412,biological_process,translation;GO:0009507,cellular_component,chloroplast;GO:0009536,cellular_component,plastid   K02913,ko03010,Ribosome
GRMZM5G835775   Pt      112473  112778  -       ndhE    protein_coding  NAD(P)H-quinone oxidoreductase subunit 4L%2C chloroplastic [Source:UniProtKB/Swiss-Prot%3BAcc:P11646]   P11646  GO:0009507,cellular_component,chloroplast;GO:0009534,cellular_component,chloroplast thylakoid;GO:0009535,cellular_component,chloroplast thylakoid membrane;GO:0009536,cellular_component,plastid;GO:0009579,cellular_component,thylakoid;GO:0016020,cellular_component,membrane;GO:0016021,cellular_component,integral component of membrane;GO:0016491,molecular_function,oxidoreductase activity;GO:0016651,molecular_function,oxidoreductase activity, acting on NAD(P)H;GO:0042773,biological_process,ATP synthesis coupled electron transport;GO:0048038,molecular_function,quinone binding;GO:0055114,biological_process,oxidation-reduction process      K05576,ko00190,Oxidative phosphorylation
```


### 小鼠
```
ENSMUSG00000000058      6       17281185        17289115        +       Cav2    protein_codingcaveolin 2 [Source:MGI Symbol;Acc:MGI:107571]     Q924U4,D3Z147,Q9WVC3    GO:0000139,cellular_component,Golgi membrane;GO:0001937,biological_process,negative regulation of endothelial cell proliferation;GO:0001938,biological_process,positive regulation of endothelial cell proliferation;GO:0002080,cellular_component,acrosomal membrane;GO:0005622,cellular_component,intracellular;GO:0005634,cellular_component,nucleus;GO:0005737,cellular_component,cytoplasm;GO:0005794,cellular_component,Golgi apparatus;GO:0005886,cellular_component,plasma membrane;GO:0005887,cellular_component,integral component of plasma membrane;GO:0005901,cellular_component,caveola;GO:0005925,cellular_component,focal adhesion;GO:0006897,biological_process,endocytosis;GO:0006906,biological_process,vesicle fusion;GO:0007005,biological_process,mitochondrion organization;GO:0007029,biological_process,endoplasmic reticulum organization;GO:0007088,biological_process,regulation of mitotic nuclear division;GO:0008285,biological_process,negative regulation of cell proliferation;GO:0008286,biological_process,insulin receptor signaling pathway;GO:0016020,cellular_component,membrane;GO:0016021,cellular_component,integral component of membrane;GO:0016050,biological_process,vesicle organization;GO:0019065,biological_process,receptor-mediated endocytosis of virus by host cell;GO:0019901,molecular_function,protein kinase binding;GO:0030133,cellular_component,transport vesicle;GO:0030512,biological_process,negative regulation of transforming growth factor beta receptor signaling pathway;GO:0030674,molecular_function,protein binding, bridging;GO:0031234,cellular_component,extrinsic component of cytoplasmic side of plasma membrane;GO:0031410,cellular_component,cytoplasmic vesicle;GO:0031748,molecular_function,D1 dopamine receptor binding;GO:0032947,molecular_function,protein-containing complex scaffold activity;GO:0032991,cellular_component,protein-containing complex;GO:0042803,molecular_function,protein homodimerization activity;GO:0043410,biological_process,positive regulation of MAPK cascade;GO:0043547,biological_process,positive regulation of GTPase activity;GO:0044791,biological_process,positive regulation by host of viral release from host cell;GO:0044794,biological_process,positive regulation by host of viral process;GO:0045121,cellular_component,membrane raft;GO:0046982,molecular_function,protein heterodimerization activity;GO:0048278,biological_process,vesicle docking;GO:0048471,cellular_component,perinuclear region of cytoplasm;GO:0048741,biological_process,skeletal muscle fiber development;GO:0051259,biological_process,protein complex oligomerization;GO:0060161,biological_process,positive regulation of dopamine receptor signaling pathway;GO:0070836,biological_process,caveola assembly;GO:0097110,molecular_function,scaffold protein binding     K12958,ko04144,Endocytosis;K12958,ko04510,Focal adhesion;K12958,ko05100,Bacterial invasion of epithelial cells;K12958,ko05205,Proteoglycans in cancer
```


