## 原核生物COG注释流程


### cognames2003-2014.tab
COG-id functional-class COG-annotation
```
$ head  cognames2003-2014.tab
# COG	func	name
COG0001	H	Glutamate-1-semialdehyde aminotransferase
COG0002	E	N-acetyl-gamma-glutamylphosphate reductase
COG0003	P	Anion-transporting ATPase, ArsA/GET3 family
COG0004	P	Ammonia channel protein AmtB
COG0005	F	Purine nucleoside phosphorylase
COG0006	E	Xaa-Pro aminopeptidase
COG0007	H	Uroporphyrinogen-III methylase (siroheme synthase)
COG0008	J	Glutamyl- or glutaminyl-tRNA synthetase
COG0009	J	tRNA A37 threonylcarbamoyladenosine synthetase subunit TsaC/SUA5/YrdC
```

### fun2003-2014.tab
class-id description
```
$ head fun2003-2014.tab
# Code	Name
J	Translation, ribosomal structure and biogenesis
A	RNA processing and modification
K	Transcription
L	Replication, recombination and repair
B	Chromatin structure and dynamics
D	Cell cycle control, cell division, chromosome partitioning
Y	Nuclear structure
V	Defense mechanisms
T	Signal transduction mechanisms
```

### cog2003-2014.csv
domain-id, genome-name, protein-id,protein-length,
domain-start, domain-end, COG-id, membership-class,
```
$ head cog2003-2014.csv
158333741,Acaryochloris_marina_MBIC11017_uid58167,158333741,432,1,432,COG0001,0,
158339504,Acaryochloris_marina_MBIC11017_uid58167,158339504,491,1,491,COG0001,0,
379012832,Acetobacterium_woodii_DSM_1030_uid88073,379012832,430,1,430,COG0001,0,
302391336,Acetohalobium_arabaticum_DSM_5501_uid51423,302391336,441,1,441,COG0001,0,
311103820,Achromobacter_xylosoxidans_A8_uid59899,311103820,425,1,425,COG0001,0,
332795879,Acidianus_hospitalis_W1_uid66875,332795879,369,1,369,COG0001,0,
332796307,Acidianus_hospitalis_W1_uid66875,332796307,416,1,416,COG0001,0,
302349002,Acidilobus_saccharovorans_345_15_uid51395,302349002,422,1,422,COG0001,0,
470179987,Acidimicrobidae_bacterium_YM16_304_uid193703,470179987,446,1,446,COG0001,0,
470180372,Acidimicrobidae_bacterium_YM16_304_uid193703,470180372,428,1,428,COG0001,0,
```

### one gi id may have mutiple cog id
```
$ cut -d ',' -f 1  cog2003-2014.csv | sort | uniq| wc -l 
1785722
(qiime) wzk@ubuntu 00:54:28 ^_^ /home/wzk/database/COG2014 
$ cut -d ',' -f 3  cog2003-2014.csv | sort | uniq| wc -l 
1785722

$ cut -d ',' -f 1  cog2003-2014.csv | wc -l 
1962317


$ awk -F ','  '{if($1==$3){print $0}}' cog2003-2014.csv | wc -l 
1962317
(qiime) wzk@ubuntu 01:20:27 ^_^ /home/wzk/database/COG2014 
$ wc -l cog2003-2014.csv
1962317 cog2003-2014.csv


$ cut -d ',' -f 1  cog2003-2014.csv | sort | uniq -c | sort -nk 1r | head 
      9 91785193
      9 83645367
      9 76801970
      9 71908619
      9 529077625
      9 521466756
      9 521462260
      9 521462259
      9 521459493
      9 470166686

$ grep '71908619' cog2003-2014.csv
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,1,129,COG0517,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,130,264,COG0517,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,889,1215,COG0642,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,1216,1349,COG0784,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,1350,1560,COG2198,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,265,419,COG2202,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,571,700,COG2202,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,701,888,COG2202,1,
71908619,Dechloromonas_aromatica_RCB_uid58025,71908619,1560,420,570,COG2203,1,
```

### genomes2003-2014.tab

genome-code ncbi-taxid ncbi-ftp-name
```
$ head genomes2003-2014.tab
# code	taxid	FTP-name
Acihos	933801	Acidianus_hospitalis_W1_uid66875
Acisac	666510	Acidilobus_saccharovorans_345_15_uid51395
Aerper	272557	Aeropyrum_pernix_K1_uid57757
Callag	1056495	Caldisphaera_lagunensis_DSM_15908_uid183486
Calmaq	397948	Caldivirga_maquilingensis_IC_167_uid58711
Deskam	490899	Desulfurococcus_kamchatkensis_1221n_uid59133
Ferfon	1163730	Fervidicoccus_fontis_Kam940_uid162201
Hypbut	415426	Hyperthermus_butylicus_DSM_5456_uid57755
Ignagg	583356	Ignisphaera_aggregans_DSM_17230_uid51875
```

### prot2003-2014.gi2gbk.tab
protein-id refseq-acc genbank-acc
```
$ head prot2003-2014.gi2gbk.tab
103485499	YP_615060	ABF51727
103485500	YP_615061	ABF51728
103485501	YP_615062	ABF51729
103485502	YP_615063	ABF51730
103485503	YP_615064	ABF51731
103485504	YP_615065	ABF51732
103485505	YP_615066	ABF51733
103485506	YP_615067	ABF51734
103485507	YP_615068	ABF51735
103485509	YP_615070	ABF51737
```


### fasta
gi|protein-id
```
>gi|118430838|ref|NP_146899.2| putative mercury ion binding protein
[Aeropyrum pernix K1]
MIIFKRHSQAILFSHNKQEKALLGIEGMHCEGCAIAIETALKNVKGIIDTKVNYSRGSAI
VTFDDTLVSINDILEHYIFKVPSNYRAKLVSFIS
```

### blast output using diamond
```
$ less -S /home/wzk/metagenome_data/result20171123/ORFCluster/representive.faa.diamond

EAOPGHJF_00004  gi|352681342|ref|YP_004891866.1|        78.6    126     26      1       1       126     472
EAOPGHJF_00008  gi|17229784|ref|NP_486332.1|    99.4    155     1       0       1       155     238     392
EAOPGHJF_00011  gi|219847796|ref|YP_002462229.1|        80.4    56      11      0       3       58      244
EAOPGHJF_00012  gi|159898670|ref|YP_001544917.1|        98.9    88      1       0       1       88      635
EAOPGHJF_00013  gi|414561717|ref|NP_715645.2|   93.7    191     12      0       1       191     263     453
```


### COG注释流程
* 首先将已知的蛋白质序列用`diamond`比对到COG数据库中的蛋白质序列，得到类似blast格式的文件
* 然后根据结果获取quest比对结果对应的gi号
* 在文件`cog2003-2014.csv`中根据gi号得到COG号
* 根据文件`cognames2003-2014.tab`由COG号得到对应的功能编号和名字
* 根据文件`fun2003-2014.tab`由功能编号得到相应的功能描述

### 注意事项
* 文件`cog2003-2014.csv`中一个gi号可能对应多个COG号
* 文件`cognames2003-2014.tab`中一个COG号可能有多个功能编号
