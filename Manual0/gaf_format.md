
### [gaf_format.md format ](http://www.geneontology.org/page/go-annotation-file-format-20)
```

Column  Content Required?   Cardinality Example
1   DB  required    1   UniProtKB
2   DB Object ID    required    1   P12345
3   DB Object Symbol    required    1   PHO3
4   Qualifier   optional    0 or greater    NOT
5   GO ID   required    1   GO:0003993
6   DB:Reference (|DB:Reference)    required    1 or greater    SGD_REF:S000047763|PMID:2676709
7   Evidence Code   required    1   IMP
8   With (or) From  optional    0 or greater    GO:0000346
9   Aspect  required    1   F
10  DB Object Name  optional    0 or 1  Toll-like receptor 4
11  DB Object Synonym (|Synonym)    optional    0 or greater    hToll|Tollbooth
12  DB Object Type  required    1   protein
13  Taxon(|taxon)   required    1 or 2  taxon:9606
14  Date    required    1   20090118
15  Assigned By required    1   SGD
16  Annotation Extension    optional    0 or greater    part_of(CL:0000576)
17  Gene Product Form ID    optional    0 or 1  UniProtKB:P12345-2
```

gaf文件中第五列为GO id



### gaf 文件
goa_human.gaf文件来源于UniProtKB
```
$ grep 'IGLV5-48' goa_human.gaf

UniProtKB       A0A075B6I7      IGLV5-48                GO:0002377      GO_REF:0000033  IBA     PANTHER:PTN000587099    P       Immunoglobulin lambda variable 5-48 (non-functional)    A0A075B6I7_HUMAN|IGLV5-48
       protein taxon:9606      20150528        GO_Central              
UniProtKB       A0A075B6I7      IGLV5-48                GO:0005615      GO_REF:0000033  IBA     PANTHER:PTN000587099    C       Immunoglobulin lambda variable 5-48 (non-functional)    A0A075B6I7_HUMAN|IGLV5-48
       protein taxon:9606      20150528        GO_Central              
UniProtKB       A0A075B6I7      IGLV5-48                GO:0006955      GO_REF:0000033  IBA     PANTHER:PTN000587099    P       Immunoglobulin lambda variable 5-48 (non-functional)    A0A075B6I7_HUMAN|IGLV5-48
       protein taxon:9606      20150528        GO_Central              
```



```
$ grep 'IGLV5-48' uniprot_trembl.fasta
>tr|A0A075B6I7|A0A075B6I7_HUMAN Immunoglobulin lambda variable 5-48 (non-functional) OS=Homo sapiens GN=IGLV5-48 PE=1 SV=2
>tr|A0A1D5QW74|A0A1D5QW74_MACMU Immunoglobulin lambda variable 5-48 (non-functional) OS=Macaca mulatta GN=IGLV5-48 PE=4 SV=1
>tr|A0A0D9RMU8|A0A0D9RMU8_CHLSB Immunoglobulin lambda variable 5-48 (non-functional) OS=Chlorocebus sabaeus GN=IGLV5-48 PE=4 SV=1
```

goa_cow.gaf.gz



```
$ grep -c 'GN=' uniprot_trembl.fasta
96093055
```

```
$ grep -c '^>' uniprot_trembl.fasta
102248261
```
uniprot_trembl数据库中94.0%含有GN，即是第三列基因编号

gaf文件中
```
UniProtKB   A0A0M4KIE1  gcdH        GO:0016491  GO_REF:0000038  IEA UniProtKB-KW:KW-0560    F   Glutaryl-CoA dehydrogenase  A0A0M4KIE1_9BURK|gcdH|CR3_0571  protein taxon:1267562   20180224    UniProt
```

```
$ grep 'A0A0M4KIE1_9BURK' uniprot_trembl.fasta
>tr|A0A0M4KIE1|A0A0M4KIE1_9BURK Glutaryl-CoA dehydrogenase OS=Cupriavidus gilardii CR3 GN=gcdH PE=3 SV=1
```



* Align the query protein sequence to uniprot database file **uniprot_trembl.fasta**
* Extract the gene name for uniprot database
* Get the ralationship with the query gene name to the gene name of uniprot
* Get the GO term of gene name of uniprot based on the GO database **goa_uniprot_all.gaf**
* Get the GO term for query gene name
 
