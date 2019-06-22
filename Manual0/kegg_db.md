# [KEGG PATHWAY Database](http://www.genome.jp/kegg/pathway.html)

## the file with kegg information
the input file can be download from the [KEGG web site](http://www.genome.jp/kegg-bin/download_htext?htext=ko00001.keg&format=htext&filedir=)

```
$ le ko00001.keg

A<b>Metabolism</b>
B
B  <b>Carbohydrate metabolism</b>
C    00010 Glycolysis / Gluconeogenesis [PATH:ko00010]
D      K00844  HK; hexokinase [EC:2.7.1.1]
D      K12407  GCK; glucokinase [EC:2.7.1.2]
D      K00845  glk; glucokinase [EC:2.7.1.2]
```

## run script to parse the information and insert the results to the database
```
python keggHtext2db.py --kegg  ko00001.keg --database kegg.db
```


## the result database

#### There are five tables in the database **kegg.db**
```
sqlite> .tables
KODesc        KOEC          PathKO        Pathway       PathwayLevel
```

#### table **PathwayLevel** has three columns: levelA, levelB and pathway
```
sqlite> select * from PathwayLevel limit 2;
levelA|levelB|pathway
Metabolism|Carbohydrate metabolism|ko00010
Metabolism|Carbohydrate metabolism|ko00020
```


#### table **Pathway** has two columns: pathway, pathway_id and pathway_desc
```
sqlite> select * from Pathway limit 5;
pathway|pathway_id|pathway_desc
ko00640|00640|Propanoate metabolism
ko05416|05416|Viral myocarditis
```

#### teble **PathKO** has two columns: pathway and KO_id
```
sqlite> select * from PathKO limit 2;
pathway|KO_id
ko00051|K22252
ko00622|K07104
```


#### table **KODesc** has three columns: KO_id, KO_symbol and KO_desc
```
sqlite> select * from KODesc limit 2;
KO_id|KO_symbol|KO_desc
K18693|PLPP4_5|diacylglycerol diphosphate phosphatase / phosphatidate phosphatase
K11594|DDX3X|ATP-dependent RNA helicase DDX3X
```


#### table **KOEC** has two columns: KO_id and EC_id
```
sqlite> select * from KOEC limit 2;
KO_id|EC_id
K11149|1.1.-.-
K03394|2.1.1.151
```