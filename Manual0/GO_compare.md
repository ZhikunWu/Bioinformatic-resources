## 分析结果
分析结果：

* 根据idmapping整理的数据库和KOBAS中的数据库基因中GO数据有一定的差别，具体表现为我们的数据库中GO数量相对均衡，KOBAS中在模式生物（小鼠）中很多，非模式生物较少；而且这些数据库和DAVID也有一定的差异（DAVID更新慢）。

* 我们可以基于自己构建的数据库进行富集分析，主要利用fisher's exact test，计算结果基本和KOBAS类似，但仍存在较小的差异，需要深入KOBAS源码进一步分析，也可能存在总基因数目计算的差异，因为KOBAS中存在基因漏算的问题，其准确度也可能有问题。



## GO enrichment test

该测试均是利用KOBAS数据库中数据

#### 自己的脚本进行GO富集（利用fisher exact test）
get mouse gene and GO term

```
python ~/github/kcgo/pipeline/db2GeneGO.py mmu.db mmu_gene_GO_list
```


fisher exact test uring in home script
```
$ python ~/github/kcgo/script/GOFisherExactTest.py --GO mmu_gene_GO_list  --gene ../../gene_list --number  24042 --termdb /home/wzk/database/geneontology/term.db --method GO --out mouse_genes_fisher_test.txt
```

output:
```
GO:0044464  cellular_component  cell part   417 12696   4.48987063566   4.67652850001e-46   1.6685853688e-42
```


#### KOBAS中的富集分析
KOBAS website GO enrichment
```
cell part   Gene Ontology   GO:0044464  415 12696   2.09433007158e-45   6.75316731581e-42
cell    Gene Ontology   GO:0005623  415 12696   2.09433007158e-45   6.75316731581e-42
binding Gene Ontology   GO:0005488  368 10562   7.27592486956e-41   1.56408131613e-37
intracellular   Gene Ontology   GO:0005622  373 11177   3.72489906532e-37   6.00546851807e-34
intracellular part  Gene Ontology   GO:0044424  367 11083   5.18476279196e-35   6.68730704907e-32
membrane-bounded organelle  Gene Ontology   GO:0043227  342 9845    6.33098492238e-35   6.8047536274e-32
organelle   Gene Ontology   GO:0043226  356 10598   2.70986874227e-34   2.49656335985e-31
cellular process    Gene Ontology   GO:0009987  377 11700   4.31530565436e-34   3.47867577062e-31
single-organism process Gene Ontology   GO:0044699  339 10288   2.79521102288e-29   2.0029239874e-26
intracellular membrane-bounded organelle    Gene Ontology   GO:0043231  302 8811    8.06862913008e-27   5.20345892599e-24
```


compare two result to find different genes

```
$ python ~/github/kcgo/pipeline/CompreGOEnrichment.py --kobas mouse_KOBAS_enrichment.txt  --inhome mouse_genes_fisher_test.txt  --out mouse_GO_kobas_inhome_compare.xls
```

output 
```
$ grep 'GO:0044464' mouse_GO_kobas_inhome_compare.xls
GO_id   KOBAS   Self_script
GO:0044464   -   ENSMUSG00000000486|ENSMUSG00000002250
```
我们自己计算的结果发现该GO中有的两个基因在KOBAS的算法中没有

#### 结果发现自己的分析结果和KOBAS中分析结果有一点差异


there are two gene in our enrichment but not in KOBAS

```sql

sqlite> select * from GeneEnsemblGeneIds where GeneEnsemblGeneIds.ensembl_gene_id = 'ENSMUSG00000000486';
gid|ensembl_gene_id
mmu:100043580|ENSMUSG00000000486
mmu:54204|ENSMUSG00000000486

sqlite> select * from GeneGos where gid = 'mmu:100043580' and  goid = 'GO:0044464';

sqlite> select * from GeneGos where gid = 'mmu:54204' and  goid = 'GO:0044464';
gid|goid
mmu:54204|GO:0044464




sqlite> select * from GeneEnsemblGeneIds where GeneEnsemblGeneIds.ensembl_gene_id = 'ENSMUSG00000002250';
gid|ensembl_gene_id
mmu:19015|ENSMUSG00000002250
mmu:69050|ENSMUSG00000002250

sqlite> select * from GeneGos where gid = 'mmu:19015' and  goid = 'GO:0044464';
gid|goid
mmu:19015|GO:0044464

sqlite> select * from GeneGos where gid = 'mmu:69050' and  goid = 'GO:0044464';
```

以上ENSMUSG00000002250在数据库中一个ensembl_gene_id对应两个gid


NCBI中确实是对应两个基因：
```
Name/Gene ID    Description Location    Aliases
Select item 19015Ppard
ID: 19015
peroxisome proliferator activator receptor delta [Mus musculus (house mouse)]   Chromosome 17, NC_000083.6 (28232754..28301469) NUC-1, NUC1, Nr1c2, PPAR-beta, PPAR-delta, PPAR[b], PPARdelta, Pparb, Pparb/d
Select item 690501810013A23Rik
ID: 69050
RIKEN cDNA 1810013A23 gene [Mus musculus (house mouse)] Chromosome 17, NC_000083.6 (28271708..28273163) 
```

但是KOBAS没有考虑这些基因对应的GO，因此计算是有一定问题的





### fisher test
进一步确定我们的fisher test是否有问题，我们在自用自己脚本和KOBAS在线计算比较

fisher test in python
```python
import scipy.stats as stats
#gene_numbre: 24042
obs = [[368, 132], [10562, 13480]]
oddsratio, pvalue= stats.fisher_exact(obs)
print(oddsratio, pvalue)

3.55809563157 2.41127716957e-40
```

R for fisher test
```R
> a = matrix(c(368, 132, 10562, 13480), nrow=2)
> b <- fisher.test(a)
> b$p.value
[1] 2.411277e-40


> a = matrix(c(368, 132, 10562, 13480), nrow=2)
> b <- fisher.test(a, alternative="great")
> b$p.value
[1] 1.792346e-40
```

利用python和R计算结果是一致的


KOBAS计算结果
```shell
term database ID input_number Background_number p_value corrected_Pvalue

binding Gene Ontology   GO:0005488  368 10562   7.27592486956e-41   1.56408131613e-37
```

KOBAS 中富集公式fisher test: (discover.py)
```python
def fisher_test(m1, n1, m2, n2, **kargs):
    alternative = kargs.get('alternative', 'greater')
    cmd = 'fisher.test(matrix(c(%d, %d, %d, %d), nc = 2), alternative = "%s")' \
          % (m1, n1 - m1, m2, n2 - m2, alternative)
    return robjects.r(cmd)[0][0]

def chisq_test(m1, n1, m2, n2, **kargs):
    ##m1         m2
    ##n1 - m1    n2 - m2
    cmd = 'chisq.test(matrix(c(%d, %d, %d, %d), nc = 2))' \
          % (m1, n1 - m1, m2, n2 - m2)
    res = robjects.r(cmd)
    if res[7][0] > 0:
        return res[2][0] / 2
    else:
        return 1 - res[2][0] / 2

```
计算结果间存在一定的差异，需要进一步在源码中查找相关计算公式


KOBAS中fisher test 公式
```
def fisher_test(m1, n1, m2, n2, **kargs):
    alternative = kargs.get('alternative', 'greater')
    cmd = 'fisher.test(matrix(c(%d, %d, %d, %d), nc = 2), alternative = "%s")' \
          % (m1, n1 - m1, m2, n2 - m2, alternative)
    return robjects.r(cmd)[0][0]
```

当基因组所有基因为24125是Pvalue正好为7.27592486956e-41
```
a = matrix(c(368, 132, 10562, 13563), nrow=2)
b <- fisher.test(a, alternative="great")
b$p.value
[1] 7.275925e-41
```


```
n = a + b + c + d
p_value = factorial(a+b) * factorial(c+d) * factorial(a+c) * factorial(b+d) / ( factorial(a) * factorial(b) * factorial(c) * factorial(d) * factorial(n) )
```


## idmapping表格和整理后数据库结果相符


该基因在idmapping中的uniprot编号
```
$ grep ENSMUSG00000000028 idmapping.dat
Q9Z1X9  Ensembl ENSMUSG00000000028
F8WJ72  Ensembl ENSMUSG00000000028
D3Z0L5  Ensembl ENSMUSG00000000028
```

uniprotGO数据库结果
```
sqlite> select * from UniprotGO where uniprot_id = "Q9Z1X9" order by go_id;
uniprot_id|go_id
Q9Z1X9|GO:0000727
Q9Z1X9|GO:0003682
Q9Z1X9|GO:0003688
Q9Z1X9|GO:0003697
Q9Z1X9|GO:0005634
Q9Z1X9|GO:0005656
Q9Z1X9|GO:0005813
Q9Z1X9|GO:0006260
Q9Z1X9|GO:0006267
Q9Z1X9|GO:0006270
Q9Z1X9|GO:0007049
Q9Z1X9|GO:0031261
Q9Z1X9|GO:0031298
Q9Z1X9|GO:0031938
Q9Z1X9|GO:0032508
Q9Z1X9|GO:0043138
Q9Z1X9|GO:1900087
Q9Z1X9|GO:1902977

sqlite> select * from UniprotGO where uniprot_id = "F8WJ72" order by go_id;
uniprot_id|go_id
F8WJ72|GO:0006270

sqlite> select * from UniprotGO where uniprot_id = "D3Z0L5" order by go_id;
uniprot_id|go_id
D3Z0L5|GO:0006270

```

整理后的数据库和原始的idmapping结果一致：
```
ENSMUSG00000000028      GO:0000727
ENSMUSG00000000028      GO:0003682
ENSMUSG00000000028      GO:0003688
ENSMUSG00000000028      GO:0003697
ENSMUSG00000000028      GO:0005634
ENSMUSG00000000028      GO:0005656
ENSMUSG00000000028      GO:0005813
ENSMUSG00000000028      GO:0006260
ENSMUSG00000000028      GO:0006267
ENSMUSG00000000028      GO:0006270
ENSMUSG00000000028      GO:0007049
ENSMUSG00000000028      GO:0031261
ENSMUSG00000000028      GO:0031298
ENSMUSG00000000028      GO:0031938
ENSMUSG00000000028      GO:0032508
ENSMUSG00000000028      GO:0043138
ENSMUSG00000000028      GO:1900087
ENSMUSG00000000028      GO:1902977
```





## 自己构建的数据库和KOBAS中GO差别大
以基因ENSMUSG00000001366为例：


#### 流程结果（uniprot GO database）
```
$ grep ENSMUSG00000001366 idmapping.dat
Q8BK06  Ensembl ENSMUSG00000001366
E0CYX8  Ensembl ENSMUSG00000001366

GO:0004842, GO:0005737, GO:0016567, GO:0019005, GO:0031146, GO:0032006, GO:0045087, GO:0045444
```

#### KOBAS 中结果
```sql
sqlite> select * from GeneEnsemblGeneIds where ensembl_gene_id = "ENSMUSG00000001366";
gid|ensembl_gene_id
mmu:71538|ENSMUSG00000001366

sqlite> select count(*) from GeneGos  where gid = "mmu:71538";

71
```


两个数据库中基因相差甚大，而且他们和DAVID中的GO数量也不一致


## KOBSA中部分物种含有GO，部分无GO信息

### KOBAS中小鼠注释信息丰富
#### 小鼠基因数
```
$ awk '{if($3=="gene"){print $0}}'  Mus_musculus.GRCm38.91.chr.gff3 | cut -d ";" -f 1 | cut -d ":" -f 2 | sort | uniq  > all_gene

$ wc -l all_gene 
25759 all_gene
```

#### KOBAS中小鼠信息
```
sqlite> select count(distinct gid) from GeneEntrezGeneIds;
count(distinct gid)
38668

sqlite> select count(distinct entrez_gene_id) from GeneEntrezGeneIds;
count(distinct entrez_gene_id)
38668


sqlite> select count(distinct uniprotkb_ac) from GeneUniprotkbAcs;
count(distinct uniprotkb_ac)
26976

sqlite> select count(distinct ensembl_gene_id) from GeneEnsemblGeneIds;
count(distinct ensembl_gene_id)
24042

sqlite> select count(distinct gid) from GeneGos;
count(distinct gid)
14875
```


### KOBAS中human基因的GO与本数据库中有差异

```
sqlite> select * from GeneEnsemblGeneIds  limit 5;
gid|ensembl_gene_id
hsa:9117|ENSG00000093183
hsa:25949|ENSG00000117614
hsa:81706|ENSG00000198729
hsa:26150|ENSG00000128408
hsa:60314|ENSG00000139637
```

hsa:81706|ENSG00000198729


idmapping
```
$ grep ENSG00000198729  idmapping.dat
Q8TAE6  Ensembl ENSG00000198729
Q8TAE6  EuPathDB    HostDB:ENSG00000198729.4
```

goa_human.gaf
```
$ grep Q8TAE6  goa_human.gaf
UniProtKB   Q8TAE6  PPP1R14C        GO:0004865  GO_REF:0000107  IEA UniProtKB:Q8R4R9|ensembl:ENSRNOP00000022046 F   Protein phosphatase 1 regulatory subunit 14C    PP14C_HUMAN|PPP1R14C|KEPI   protein taxon:9606  20180127    Ensembl     
UniProtKB   Q8TAE6  PPP1R14C        GO:0004865  GO_REF:0000107  IEA UniProtKB:Q8R4S0|ensembl:ENSMUSP00000045110 F   Protein phosphatase 1 regulatory subunit 14C    PP14C_HUMAN|PPP1R14C|KEPI   protein taxon:9606  20180127    Ensembl     
UniProtKB   Q8TAE6  PPP1R14C        GO:0005737  GO_REF:0000039  IEA UniProtKB-SubCell:SL-0086   C   Protein phosphatase 1 regulatory subunit 14C    PP14C_HUMAN|PPP1R14C|KEPI   protein taxon:9606  20180127    UniProt     
UniProtKB   Q8TAE6  PPP1R14C        GO:0016020  GO_REF:0000039  IEA UniProtKB-SubCell:SL-0162   C   Protein phosphatase 1 regulatory subunit 14C    PP14C_HUMAN|PPP1R14C|KEPI   protein taxon:9606  20180127    UniProt     
UniProtKB   Q8TAE6  PPP1R14C        GO:0032515  GO_REF:0000108  IEA GO:0004864  P   Protein phosphatase 1 regulatory subunit 14C    PP14C_HUMAN|PPP1R14C|KEPI   protein taxon:9606  20180127    GOC     
UniProtKB   Q8TAE6  PPP1R14C        GO:0032515  GO_REF:0000108  IEA GO:0004865  P   Protein phosphatase 1 regulatory subunit 14C    PP14C_HUMAN|PPP1R14C|KEPI   protein taxon:9606  20180127    GOC     
UniProtKB   Q8TAE6  PPP1R14C        GO:0042325  GO_REF:0000002  IEA InterPro:IPR008025|InterPro:IPR036658   P   Protein phosphatase 1 regulatory subunit 14C    PP14C_HUMAN|PPP1R14C|KEPI   protein taxon:9606  20180127    InterPro        
HGNC    14952   PPP1R14C        GO:0004865  PAINT_REF:16188 IBA PANTHER:PTN000415514    F   Protein phosphatase 1 regulatory subunit 14C    UniProtKB:Q8TAE6|PTN002497185   protein taxon:9606  20170427    GO_Central      
HGNC    14952   PPP1R14C        GO:0035304  PAINT_REF:16188 IBA PANTHER:PTN000415514    P   Protein phosphatase 1 regulatory subunit 14C    UniProtKB:Q8TAE6|PTN002497185   protein taxon:9606  20170427    GO_Central  
```



KOBAS
```
sqlite> select * from GeneGos where gid = 'hsa:81706';
gid|goid
hsa:81706|GO:0004857
hsa:81706|GO:0004864
hsa:81706|GO:0004865
hsa:81706|GO:0005622
hsa:81706|GO:0005623
hsa:81706|GO:0005737
hsa:81706|GO:0006464
hsa:81706|GO:0006470
hsa:81706|GO:0006793
hsa:81706|GO:0006796
hsa:81706|GO:0008152
hsa:81706|GO:0009987
hsa:81706|GO:0016020
hsa:81706|GO:0016310
hsa:81706|GO:0016311
hsa:81706|GO:0019208
hsa:81706|GO:0019212
hsa:81706|GO:0019220
hsa:81706|GO:0019222
hsa:81706|GO:0019538
hsa:81706|GO:0019888
hsa:81706|GO:0030234
hsa:81706|GO:0031323
hsa:81706|GO:0031399
hsa:81706|GO:0032268
hsa:81706|GO:0035303
hsa:81706|GO:0035304
hsa:81706|GO:0036211
hsa:81706|GO:0042325
hsa:81706|GO:0043086
hsa:81706|GO:0043170
hsa:81706|GO:0043412
hsa:81706|GO:0044092
hsa:81706|GO:0044237
hsa:81706|GO:0044238
hsa:81706|GO:0044260
hsa:81706|GO:0044267
hsa:81706|GO:0044424
hsa:81706|GO:0044464
hsa:81706|GO:0050789
hsa:81706|GO:0050790
hsa:81706|GO:0050794
hsa:81706|GO:0051174
hsa:81706|GO:0051246
hsa:81706|GO:0060255
hsa:81706|GO:0065007
hsa:81706|GO:0065009
hsa:81706|GO:0071704
hsa:81706|GO:0080090
hsa:81706|GO:0098772
```

### KOBAS数据库的某些物种(玉米)中无GO
```
sqlite> .table
Diseases              GeneGos               GoSlims             
GeneDiseases          GenePathways          Gos                 
GeneEnsemblGeneIds    GeneRefSeqProteinIds  Orthologs           
GeneEntrezGeneIds     GeneUniprotkbAcs      Pathways            
GeneGoSlims           Genes               
sqlite> select * from GeneGos;

sqlite> select * from Gos  limit 5;
sqlite> select * from GoSlims  limit 5;

sqlite> select * from genes  limit 5;
gid|name
zma:100384857|GRMZM2G381138
zma:103649097|GRMZM2G008313
zma:100216695|GRMZM2G042127
zma:103648308|
zma:100273881|

```







