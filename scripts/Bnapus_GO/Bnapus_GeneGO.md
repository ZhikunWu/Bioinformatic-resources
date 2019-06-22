# GO annotation of Brassica napus

## The input files for creating database

### Brassica_napus_GO
``` 
$ head -n 5 Brassica_napus_GO

BnaC09g12820D GO:0046983
BnaC09g12810D GO:0003922
BnaC09g12810D GO:0004066
BnaC09g12810D GO:0005524
BnaC09g12810D GO:0006164
```

### Brassica_napus.annotation_v5.gff3
```
$ awk '{if($3=="mRNA"){print $0}}' Brassica_napus.annotation_v5.gff3 | head -n 3

chrC09  GazeA2  mRNA    9318184 9322857 214.6819        -       .       ID=BnaC09g12820D;Name=BnaC09g12820D;Alias=GSBRNA2T00000001001
chrC09  GazeA2  mRNA    9310901 9313544 288.8598        +       .       ID=BnaC09g12810D;Name=BnaC09g12810D;Alias=GSBRNA2T00000003001
chrC09  GazeA2  mRNA    9299578 9303058 118.4062        +       .       ID=BnaC09g12800D;Name=BnaC09g12800D;Alias=GSBRNA2T00000005001
```

### GO term.txt
```
$ le term.txt

30      mitochondrion inheritance       biological_process      GO:0000001      0       0
31      exact   synonym_scope   exact   0       0       0
32      mitochondrial genome maintenance        biological_process      GO:0000002      0
33      reproduction    biological_process      GO:0000003      0       0       0
```


## create annotation database
```
python createBnapusGOdb.py --GO Brassica_napus_GO  --gff Brassica_napus.annotation_v5.gff3 --term term.txt --database BnapusGeneGO.db
```

## The output annotation database
```sql
$ sqlite3 BnapusGeneGO.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .tables
GOInfor   GeneAnno  GeneGO    GeneName

sqlite> .schema GeneAnno
CREATE TABLE GeneAnno
        (gene_id text,
        chr_id text,
        start_pos integer,
        end_pos integer,
        strand text,
        symbol text,
        alias text);
sqlite> select * from GeneAnno limit 5;
BnaC09g12820D|chrC09|9318184|9322857|-|BnaC09g12820D|GSBRNA2T00000001001
BnaC09g12810D|chrC09|9310901|9313544|+|BnaC09g12810D|GSBRNA2T00000003001
BnaC09g12800D|chrC09|9299578|9303058|+|BnaC09g12800D|GSBRNA2T00000005001
BnaC09g12790D|chrC09|9281711|9282146|-|BnaC09g12790D|GSBRNA2T00000007001
BnaC09g12780D|chrC09|9271294|9275153|-|BnaC09g12780D|GSBRNA2T00000008001

sqlite> .schema GeneGO
CREATE TABLE GeneGO
        (gene_name text,
        GO_id text);
sqlite> select * from GeneGO limit 5;
BnaC09g12820D|GO:0046983
BnaC09g12810D|GO:0003922
BnaC09g12810D|GO:0004066
BnaC09g12810D|GO:0005524
BnaC09g12810D|GO:0006164

sqlite> .schema GeneName
CREATE TABLE GeneName
        (gene_alias text,
        gene_name text);
sqlite> select * from GeneName  limit 5;
GSBRNA2T00121640001|BnaA01g00010D
GSBRNA2T00121639001|BnaA01g00020D
GSBRNA2T00121638001|BnaA01g00030D
GSBRNA2T00121637001|BnaA01g00040D
GSBRNA2T00121635001|BnaA01g00050D


sqlite> .schema GOInfor
CREATE TABLE GOInfor
        (GO_id text,
        GO_category text,
        GO_term text);
sqlite> select * from GOInfor limit 5;
GO:0000001|biological_process|mitochondrion inheritance
GO:0000002|biological_process|mitochondrial genome maintenance
GO:0000003|biological_process|reproduction
GO:0000005|molecular_function|obsolete ribosomal chaperone activity
GO:0042254|biological_process|ribosome biogenesis
```

## select the record base on the genome position
```sql
sqlite> select * from GeneAnno where chr_id = 'chrC09' and start_pos <  9299588 and end_pos > 9299588;
BnaC09g12800D|chrC09|9299578|9303058|+|BnaC09g12800D|GSBRNA2T00000005001


select * from GeneAnno left join GeneGO on GeneGO.gene_name = GeneAnno.gene_id  where GeneAnno.chr_id = 'chrC09' and GeneAnno.start_pos <  9299588 and GeneAnno.end_pos > 9299588;


sqlite> select * from GeneAnno left join GeneGO on GeneGO.gene_name = GeneAnno.gene_id left join GOInfor on GeneGO.GO_id  = GOInfor.GO_id limit 5;

BnaC09g12820D|chrC09|9318184|9322857|-|BnaC09g12820D|GSBRNA2T00000001001|BnaC09g12820D|GO:0046983|GO:0046983|molecular_function|protein dimerization activity
BnaC09g12810D|chrC09|9310901|9313544|+|BnaC09g12810D|GSBRNA2T00000003001|BnaC09g12810D|GO:0003922|GO:0003922|molecular_function|GMP synthase (glutamine-hydrolyzing) activity
BnaC09g12810D|chrC09|9310901|9313544|+|BnaC09g12810D|GSBRNA2T00000003001|BnaC09g12810D|GO:0004066|GO:0004066|molecular_function|asparagine synthase (glutamine-hydrolyzing) activity
BnaC09g12810D|chrC09|9310901|9313544|+|BnaC09g12810D|GSBRNA2T00000003001|BnaC09g12810D|GO:0005524|GO:0005524|molecular_function|ATP binding
BnaC09g12810D|chrC09|9310901|9313544|+|BnaC09g12810D|GSBRNA2T00000003001|BnaC09g12810D|GO:0006164|GO:0006164|biological_process|purine nucleotide biosynthetic process



sqlite> select GeneAnno.gene_id, GeneAnno.chr_id,  GeneAnno.start_pos, GeneAnno.end_pos, GeneAnno.strand, GeneAnno.alias, GOInfor.GO_id, GOInfor.GO_category, GOInfor.GO_term  from GeneAnno left join GeneGO on GeneGO.gene_name = GeneAnno.gene_id left join GOInfor on GeneGO.GO_id  = GOInfor.GO_id limit 5 ;
BnaC09g12820D|chrC09|9318184|9322857|-|GSBRNA2T00000001001|GO:0046983|molecular_function|protein dimerization activity
BnaC09g12810D|chrC09|9310901|9313544|+|GSBRNA2T00000003001|GO:0003922|molecular_function|GMP synthase (glutamine-hydrolyzing) activity
BnaC09g12810D|chrC09|9310901|9313544|+|GSBRNA2T00000003001|GO:0004066|molecular_function|asparagine synthase (glutamine-hydrolyzing) activity
BnaC09g12810D|chrC09|9310901|9313544|+|GSBRNA2T00000003001|GO:0005524|molecular_function|ATP binding
BnaC09g12810D|chrC09|9310901|9313544|+|GSBRNA2T00000003001|GO:0006164|biological_process|purine nucleotide biosynthetic process


sqlite> select GeneAnno.gene_id, GeneAnno.chr_id,  GeneAnno.start_pos, GeneAnno.end_pos, GeneAnno.strand, GeneAnno.alias, GOInfor.GO_id, GOInfor.GO_category, GOInfor.GO_term  from GeneAnno left join GeneGO on GeneGO.gene_name = GeneAnno.gene_id left join GOInfor on GeneGO.GO_id  = GOInfor.GO_id  where GeneAnno.chr_id = 'chrA05' and   GeneAnno.start_pos <= 9318184 and GeneAnno.end_pos >= 9318184;
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0003676|molecular_function|nucleic acid binding
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0003684|molecular_function|damaged DNA binding
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0003906|molecular_function|DNA-(apurinic or apyrimidinic site) endonuclease activity
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0006281|biological_process|DNA repair
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0006284|biological_process|base-excision repair
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0006289|biological_process|nucleotide-excision repair
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0008270|molecular_function|zinc ion binding
BnaA05g14830D|chrA05|9318081|9320425|-|GSBRNA2T00094066001|GO:0008534|molecular_function|oxidized purine nucleobase lesion DNA N-glycosylase activity
```


## align B.napus sequence to the uniprot database using **diamond**
```
diamond blastp --no-auto-append  --db uniprot.dmnd   --query Brassica_napus.annotation_v5.pep.fa  --threads 20 --evalue e-5 --max-target-seqs 1 --out Brassica_napus.annotation_v5.pep_uniprot.blast

```

convert the diamond output to the database:
```sql
$ sqlite3 Bnapus_uniprot.db
SQLite version 3.19.3 2017-06-08 14:26:16
Enter ".help" for usage hints.
sqlite> .schema 
CREATE TABLE GeneBlast
        (query text,
        subject text,
        identity real,
        alignLen integer,
        mismatch integer,
        gap integer,
        queryStart integer,
        queryEnd integer,
        subjectStart integer,
        subjectEnd integer,
        evalue real,
        bitScore real);
sqlite> select * from GeneBlast limit 5;
GSBRNA2T00000001001;tr|A0A078F5I3|A0A078F5I3_BRANA;100.0;605;0;0;1;605;1;605;0.0;1148.3
GSBRNA2T00000003001;tr|A0A078F1H1|A0A078F1H1_BRANA;100.0;535;0;0;1;535;1;535;0.0;1088.2
GSBRNA2T00000005001;tr|A0A078F4H7|A0A078F4H7_BRANA;100.0;584;0;0;1;584;1;584;0.0;1137.9
GSBRNA2T00000009001;tr|A0A078F5I6|A0A078F5I6_BRANA;100.0;870;0;0;1;870;1;870;0.0;1723.8
GSBRNA2T00000011001;tr|A0A078F1H6|A0A078F1H6_BRANA;100.0;839;0;0;1;839;1;839;0.0;1696.8
```



# snakemake workflow of napus annotation 
```python
rule IndexGstatGene:
    input:
        Index_Gstats = rules.MergeDeltaindexGstats.output.Index_Gstats,
    output:
        gene = IN_PATH + '/Candidate/{group}_Delta_index_Gstats_gene.xls',
    params:
        CandiLociGene = SRC_DIR + '/CandiLociGene.py',
        GFF = config['GFF'],
        distance = 2000,
    log:
        IN_PATH + "/log/IndexGstatGene/IndexGstatGene_{group}.log",
    run:
        shell('python {params.CandiLociGene} --input {input.Index_Gstats} --gff {params.GFF} --distance {params.distance} --out {output.gene} >{log} 2>&1')     

rule createGOdb:
    input:
        gene_GO = IN_PATH + '/Brassica_napus_GO',
        term = IN_PATH + '/term.txt',
    output:
        GOdb = IN_PATH + '/BnapusGeneGO.db',
    params:
        GFF = config['GFF'],
        createBnapusGOdb = SRC_DIR + '/createBnapusGOdb.py',
    log:
        IN_PATH + "/log/IndexGstatGene/createGOdb_{group}.log",
    run:
        shell('python {params.createBnapusGOdb} --GO {input.gene_GO}  --gff {params.GFF} --term term.txt --database {output.GOdb} >{log} 2>&1')


rule IndexGstatGeneAnno:
    input:
        gene = rules.IndexGstatGene.output.gene,
    output:
        anno = IN_PATH + '/Candidate/{group}_Delta_index_Gstats_gene_anno.xls',
    params:
        LociGeneAnno = SRC_DIR + '/LociGeneAnno.py',
        GO_db = '/home/wzk/Project/bsa-zhan/BnapusGeneGO.db'
    log:
        IN_PATH + "/log/IndexGstatGene/IndexGstatGeneAnno_{group}.log",
    run:
        shell('python {params.LociGeneAnno} --gene {input.gene} --database {params.GO_db} --out {output.anno} >{log} 2>&1') 


```

