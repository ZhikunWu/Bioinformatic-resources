
## [uniprot](http://www.uniprot.org/downloads)

## [idmapping](ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/)
### [readme file](ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/README)
```
This file has three columns, delimited by tab:
1. UniProtKB-AC 
2. ID_type 
3. ID
```

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



### idmapping database
```sql
$ sqlite3 idmapping.db 
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .header on
sqlite> .table
Ensembl       EnsemblTrans  GeneORFName   RefSeq      
EnsemblGene   GeneID        KEGG          UniProtKB   
EnsemblPro    GeneName      KO            eggNOG 
```

```sql
sqlite> select * from Ensembl  limit 2;
uniprotAc|Ensembl_id
Q5ZLQ6|ENSGALG00000004143
P31946|ENSG00000166913

sqlite> select * from EnsemblGene  limit 2;
uniprotAc|EnsemblGene_id
Q4U9M9|TA08425
P15711|TP04_0437

sqlite> select * from EnsemblPro  limit 2;
uniprotAc|EnsemblPro_id
Q4U9M9|CAI76474
P15711|EAN31789

sqlite> select * from EnsemblTrans  limit 2;
uniprotAc|EnsemblTrans_id
Q4U9M9|CAI76474
P15711|EAN31789

sqlite> select * from GeneID  limit 2;
uniprotAc|Gene_id
Q6GZX4|2947773
Q6GZX3|2947774

sqlite> select * from GeneName  limit 2;
uniprotAc|GeneName
P0C9F0|Ken-018
P0C9F1|Mal-015

sqlite> select * from GeneORFName  limit 2;
uniprotAc|ORFName_id
Q6GZX4|FV3-001R
Q6GZX3|FV3-002L

sqlite> select * from KEGG  limit 2;
uniprotAc|kegg_id
Q6GZX4|vg:2947773
Q6GZX3|vg:2947774

sqlite> select * from KO  limit 2;
uniprotAc|KO_id
Q6GZS4|K12408
Q92AT0|K21298

sqlite> select * from RefSeq  limit 2;
uniprotAc|Refseq_id
Q6GZX4|YP_031579.1
Q6GZX3|YP_031580.1

sqlite> select * from UniProtKB  limit 2;
uniprotAc|uniprotKB_id
Q6GZX4|001R_FRG3G
Q6GZX3|002L_FRG3G

sqlite> select * from eggNOG  limit 2;
uniprotAc|eggNOG_id
Q43495|ENOG410J6YU
Q43495|ENOG410Z2QH
```


选择KO，eggNOG, GO



### KO database 
```sql
sqlite> select * from KoPathways limit 2;
koid|pid
K00123|ko00630
K04632|ko04270

sqlite> select * from Pathways limit 2;
pid|name
ko04062|Chemokine signaling pathway
ko04060|Cytokine-cytokine receptor interaction


sqlite> .schema KoPathways
CREATE TABLE KoPathways
(
    koid TEXT,
    pid TEXT,
    PRIMARY KEY (koid, pid)
);
sqlite> .schema Pathways
CREATE TABLE Pathways
(
    pid TEXT PRIMARY KEY,
    name TEXT
);
```

建立索引
```sql
sqlite> CREATE INDEX gene_koid on KoPathways (koid);
sqlite> CREATE INDEX pid_name  on Pathways (pid);
```


### interpro
```sql
$ sqlite3 protein2ipr.dat.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .header on
sqlite> .table
interproDesc     uniprotInterpro  uniprotPfam 
```

tabels in protein2ipr.dat.db
```sql
sqlite> select * from uniprotInterpro limit 2;
uniprot_ac|interpro_id
A0A000|IPR010961
A0A000|IPR015421


sqlite> select * from interproDesc limit 2;
interpro_id|interpro_desc
IPR004839|Aminotransferase, class I/classII
IPR010961|Tetrapyrrole biosynthesis, 5-aminolevulinic acid synthase

sqlite> select * from uniprotPfam limit 2;
uniprot_ac|pfam_id
A0A000|TIGR01821
A0A000|G3DSA:3.40.640.10
```


create table and index
```sql
sqlite> .schema  interproDesc
CREATE TABLE interproDesc
        (interpro_id text,
        interpro_desc text);
CREATE INDEX interpro2desc
        on interproDesc (interpro_id);
sqlite> .schema
CREATE TABLE uniprotInterpro
        (uniprot_ac text,
        interpro_id text);
CREATE TABLE interproDesc
        (interpro_id text,
        interpro_desc text);
CREATE TABLE uniprotPfam
        (uniprot_ac text,
        pfam_id text);
CREATE INDEX unipro2interpro
        on uniprotInterpro (uniprot_ac);
CREATE INDEX interpro2desc
        on interproDesc (interpro_id);
CREATE INDEX uniprot2pfam
        on uniprotPfam (uniprot_ac) 
    ;
```


### GO term
```sql
$ sqlite3 term.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .header on
sqlite> .table
GODescription

sqlite> .schema GODescription
CREATE TABLE GODescription
        (go_id text,
        go_level text,
        go_description text);
CREATE INDEX go_term
        on GODescription (go_id);

```


```sql
sqlite> select * from GODescription limit 2;
go_id|go_level|go_description
GO:0071138|cellular_component|alpha5-beta5-fibronectin-SFRP2 complex
GO:1900561|biological_process|dehydroaustinol metabolic process
```

## pfam
```sql
$ sqlite3 Pfam-A.full.uniprot.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .header on
sqlite> .table
pfamInfor    uniprotPfam

```

```
sqlite> select * from uniprotPfam limit 5;
uniprot_ac|pfam_ac
X8HP43|PF10417
|PF10417
A0A061SW14|PF10417
A0A0M2NS92|PF10417
Q21824|PF10417

sqlite> select * from pfamInfor limit 5;
pfam_ac|pfam_id|pfam_desc
PF10417|1-cysPrx_C|C-terminal domain of 1-Cys peroxiredoxin
PF12574|120_Rick_ant|120 KDa Rickettsia surface antigen
PF09847|12TM_1|Membrane protein of 12 TMs
PF00244|14-3-3|14-3-3 protein
PF16998|17kDa_Anti_2|17 kDa outer membrane surface antigen
```


### merge idmapping and gff database
```sql
$ sqlite3 Mus_musculus.GRCm38.91.chr_GeneAnno_Anno.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .header on
sqlite> .table
Ensembl        EnsemblTrans   GeneID         GeneUniProtKB  KO           
EnsemblGene    GeneAnno       GeneName       GeneUniprotAc  RefSeq       
EnsemblPro     GeneGO         GeneORFName    KEGG           eggNOG     
```

```sql

sqlite> .schema Ensembl
CREATE TABLE Ensembl
        (gene_id text,
        Ensembl_id text);

sqlite> .schema EnsemblGene
CREATE TABLE EnsemblGene
        (gene_id text,
        EnsemblGene_id text);

sqlite> .schema GeneORFName
CREATE TABLE GeneORFName
        (gene_id text,
        ORFName_id text);

sqlite> .schema GeneGO
CREATE TABLE GeneGO
        (gene_id text,
        go_id text);

sqlite> .schema KO
CREATE TABLE KO
        (gene_id text,
        KO_id text);


sqlite> .schema eggNOG
CREATE TABLE eggNOG
        (gene_id text,
        eggNOG_id text);

sqlite> .schema GeneAnno
CREATE TABLE GeneAnno
        (gene_id text,
        chr_id text,
        start_pos integer,
        end_pos integer,
        strand text,
        symbol text,
        biotype text,
        description text);
```

GeneAnno (gene_id) -> GeneUniprotAc (uniprotAc)
GeneGO gene_id -> go_id
KO     gene_id -> KO_id
eggNOG  gene_id -> eggNOG

```sql
sqlite> select * from GeneAnno  limit 2;
gene_id|chr_id|start_pos|end_pos|strand|symbol|biotype|description
ENSMUSG00000102693|1|3073253|3074322|+|4933401J01Rik|TEC|RIKEN cDNA 4933401J01 gene [Source:MGI Symbol;Acc:MGI:1918292]
ENSMUSG00000051951|1|3205901|3671498|-|Xkr4|protein_coding|X-linked Kx blood group related 4 [Source:MGI Symbol;Acc:MGI:3528744]

sqlite> select * from GeneUniprotAc  limit 2;
gene_id|uniprotAc
ENSMUSG00000051951|Q5GH67
ENSMUSG00000025900|P56716

sqlite> select * from GeneGO  limit 2;
gene_id|go_id
ENSMUSG00000051951|GO:0003674
ENSMUSG00000051951|GO:0008150

sqlite> select * from KO  limit 2;
gene_id|KO_id
ENSMUSG00000025900|K19538
ENSMUSG00000025902|K04495

sqlite> select * from eggNOG  limit 2;
gene_id|eggNOG_id
ENSMUSG00000051951|KOG4790
ENSMUSG00000051951|ENOG410YRUD
```


create index
```sql
sqlite> CREATE INDEX gene_uniprotac on GeneUniprotAc (gene_id);
sqlite> CREATE INDEX gene_KO on KO (gene_id);
sqlite> CREATE INDEX gene_GO on GeneGO (gene_id);
sqlite> CREATE INDEX gene_eggNOG on eggNOG (gene_id);
```

