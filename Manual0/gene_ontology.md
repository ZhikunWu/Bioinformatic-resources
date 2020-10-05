

## [geneontology](http://archive.geneontology.org/latest-full/)

```
files:
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
```

### download database
```
wget http://archive.geneontology.org/latest-full/README
wget http://archive.geneontology.org/latest-full/go_monthly-assocdb-data.gz
wget http://archive.geneontology.org/latest-full/go_monthly-assocdb-summary.txt.gz
wget http://archive.geneontology.org/latest-full/go_monthly-assocdb-tables.tar.gz
wget http://archive.geneontology.org/latest-full/go_monthly-termdb-data.gz
wget http://archive.geneontology.org/latest-full/go_monthly-termdb-summary.txt.gz
wget http://archive.geneontology.org/latest-full/go_monthly-termdb-tables.tar.gz
wget http://archive.geneontology.org/latest-full/go_monthly-termdb.obo-xml.gz
wget http://archive.geneontology.org/latest-full/go_monthly-termdb.owl.gz
wget http://archive.geneontology.org/latest-full/go_monthly-termdb.rdf-xml.gz
```




### go_monthly-assocdb-data
```
$ grep -n 'Table structure'  go_monthly-assocdb-data
19:-- Table structure for table `assoc_rel`
47:-- Table structure for table `association`
11550:-- Table structure for table `association_isoform`
11574:-- Table structure for table `association_property`
11602:-- Table structure for table `association_qualifier`
11633:-- Table structure for table `association_species_qualifier`
11660:-- Table structure for table `db`
11695:-- Table structure for table `dbxref`
13598:-- Table structure for table `evidence`
28678:-- Table structure for table `evidence_dbxref`
34750:-- Table structure for table `gene_product`
37998:-- Table structure for table `gene_product_ancestor`
38026:-- Table structure for table `gene_product_count`
40788:-- Table structure for table `gene_product_dbxref`
40813:-- Table structure for table `gene_product_homology`
40839:-- Table structure for table `gene_product_homolset`
40866:-- Table structure for table `gene_product_phylotree`
40892:-- Table structure for table `gene_product_property`
40919:-- Table structure for table `gene_product_seq`
40945:-- Table structure for table `gene_product_subset`
40970:-- Table structure for table `gene_product_synonym`
43386:-- Table structure for table `graph_path`
43457:-- Table structure for table `graph_path2term`
43482:-- Table structure for table `homolset`
43515:-- Table structure for table `instance_data`
43541:-- Table structure for table `intersection_of`
43569:-- Table structure for table `phylotree`
43594:-- Table structure for table `phylotree_property`
43620:-- Table structure for table `relation_composition`
43651:-- Table structure for table `relation_properties`
43681:-- Table structure for table `seq`
43714:-- Table structure for table `seq_dbxref`
43740:-- Table structure for table `seq_property`
43769:-- Table structure for table `source_audit`
43798:-- Table structure for table `species`
43972:-- Table structure for table `term`
44014:-- Table structure for table `term2term`
44048:-- Table structure for table `term2term_metadata`
44077:-- Table structure for table `term_audit`
44101:-- Table structure for table `term_dbxref`
44132:-- Table structure for table `term_definition`
44169:-- Table structure for table `term_property`
44193:-- Table structure for table `term_subset`
44219:-- Table structure for table `term_synonym`

```




## [gene ontology](http://www.geneontology.org/page/download-go-annotations)
### Danio rerio(斑马鱼):
wget http://geneontology.org/gene-associations/gene_association.zfin.gz
### Caenorhabditis elegans (秀丽隐杆线虫)
wget http://geneontology.org/gene-associations/gene_association.wb.gz
### Arabidopsis thaliana (拟南芥)
wget http://geneontology.org/gene-associations/gene_association.tair.gz
### Solanaceae (茄科)
wget http://geneontology.org/gene-associations/gene_association.sgn.gz
### Saccharomyces cerevisiae (酿酒酵母)
wget http://geneontology.org/gene-associations/gene_association.sgd.gz
### Rattus norvegicus (褐鼠)
wget http://geneontology.org/gene-associations/gene_association.rgd.gz
### Pseudomonas aeruginosa (绿脓假单胞菌；绿脓杆菌)
wget http://geneontology.org/gene-associations/gene_association.pseudocap.gz
### Schizosaccharomyces pombe (粟酒裂殖酵母)
wget http://geneontology.org/gene-associations/gene_association.pombase.gz
### Mus musculus (小鼠)
wget http://geneontology.org/gene-associations/gene_association.mgi.gz
### Comprehensive Microbial ()
wget http://geneontology.org/gene-associations/gene_association.jcvi.gz
### Oryza sativa (水稻)
wget http://geneontology.org/gene-associations/gene_association.gramene_oryza.gz
### UniProt
wget ftp://ftp.ebi.ac.uk/pub/databases/GO/goa/UNIPROT/goa_uniprot_all.gaf.gz
### UniProt, no IEA annotations
wget http://geneontology.org/gene-associations/goa_uniprot_all_noiea.gaf.gz
### Sus scrofa (野猪)
wget http://geneontology.org/gene-associations/goa_pig.gaf.gz
### Homo sapiens (智人)
wget http://geneontology.org/gene-associations/goa_human.gaf.gz
### Canis lupus familiaris (狼)
wget http://geneontology.org/gene-associations/goa_dog.gaf.gz
### Bos taurus (牛)
wget http://geneontology.org/gene-associations/goa_cow.gaf.gz
### Gallus gallus (原鸡)
wget http://geneontology.org/gene-associations/goa_chicken.gaf.gz
### Drosophila melanogaster (果蝇)
wget http://geneontology.org/gene-associations/gene_association.fb.gz
### Escherichia coli (大肠杆菌)
wget http://geneontology.org/gene-associations/gene_association.ecocyc.gz
### Dictyostelium discoideum (盘基网柄菌)
wget http://geneontology.org/gene-associations/gene_association.dictyBase.gz
### Candida albicans (白色念珠菌； 白假丝酵母)
wget http://geneontology.org/gene-associations/gene_association.cgd.gz
### Aspergillus nidulans (构巢曲霉)
wget http://geneontology.org/gene-associations/gene_association.aspgd.gz
### Oomycetes (卵菌类)
wget http://geneontology.org/gene-associations/gene_association.PAMGO_Oomycetes.gz
### Magnaporthe grisea (稻瘟病菌)
wget http://geneontology.org/gene-associations/gene_association.PAMGO_Mgrisea.gz
### Dickeya dadantii ()
wget http://geneontology.org/gene-associations/gene_association.PAMGO_Ddadantii.gz
### Trypanosoma brucei (布氏锥虫)
wget http://geneontology.org/gene-associations/gene_association.GeneDB_Tbrucei.gz
### Plasmodium falciparum (镰状疟原虫； 恶性疟原虫)
wget http://geneontology.org/gene-associations/gene_association.GeneDB_Pfalciparum.gz
### Leishmania major (硕大利什曼原虫)
wget http://geneontology.org/gene-associations/gene_association.GeneDB_Lmajor.gz

wget ftp://ftp.ensemblgenomes.org/pub/release-38/metazoa/fasta/drosophila_melanogaster/pep/Drosophila_melanogaster.BDGP6.pep.all.fa.gz