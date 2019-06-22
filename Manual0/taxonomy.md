## taxonomy tree

### download the database
```
wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz.md5
wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump_readme.txt
```

### genus name of taxonomy
```
$grep Nitrospira  /home/wzk/database/taxonomy/names.dmp

1946986 |   Nitrospira sp. UBA2082  |       |   scientific name |
1946987 |   Nitrospira sp. UBA2083  |       |   scientific name |
1946988 |   Nitrospira sp. UBA4129  |       |   scientific name |
1946989 |   Nitrospira sp. UBA5698  |       |   scientific name |
1946990 |   Nitrospira sp. UBA5699  |       |   scientific name |
1946991 |   Nitrospira sp. UBA5702  |       |   scientific name |
1946992 |   Nitrospira sp. UBA6488  |       |   scientific name |
1946993 |   Nitrospira sp. UBA6493  |       |   scientific name |
1946994 |   Nitrospira sp. UBA667   |       |   scientific name |
1946995 |   Nitrospira sp. UBA6909  |       |   scientific name |
1946996 |   Nitrospira sp. UBA7240  |       |   scientific name |
1946997 |   Nitrospira sp. UBA7655  |       |   scientific name |

```

#### levels
```
$ cut -f 5 /home/wzk/database/taxonomy/nodes.dmp | uniq | sort | uniq
class
cohort
family
forma
genus
infraclass
infraorder
kingdom
no rank
order
parvorder
phylum
species
species group
species subgroup
subclass
subfamily
subgenus
subkingdom
suborder
subphylum
subspecies
subtribe
superclass
superfamily
superkingdom
superorder
superphylum
tribe
varietas
```

taxa id is unique
```
$ grep 'scientific name'  /home/wzk/database/taxonomy/names.dmp | cut -f 1 | sort | uniq -c | sort -k 1nr | head
      1 1
      1 10
      1 100
      1 100000
      1 1000000
      1 1000001
      1 1000002
      1 1000003
      1 1000004
      1 1000005
```

### parents
```
$ grep 1946986 nodes.dmp
1946986 |   1234    |   species |   NS  |   0   |   1   |   11  |   1   |   0      
```

```
$ grep '^1234'  nodes.dmp

1234    |       189779  |       genus   |               |       0       |       1       |       11      |       1       |       0 
```

```
$ grep '^189779'  nodes.dmp
189779  |   189778  |   family  |       |   0   |   1   |   11  |   1   |   0      |
```


```
$ grep '^189778'  nodes.dmp
189778  |   203693  |   order   |       |   0   |   1   |   11  |   1   |   0      |
```

```
$ grep '^203693'  nodes.dmp
203693  |   40117   |   class   |       |   0   |   1   |   11  |   1   |   0      |
```

```
$ grep '^40117'  nodes.dmp
40117   |   2   |   phylum  |       |   0   |   1   |   11  |   1   |   0      |
```

```
$ grep '^40117'  nodes.dmp | less

2   |   131567  |   superkingdom    |       |   0   |   0   |   11  |   0   |      |
```

```
$ grep '^131567' nodes.dmp

131567  |   1   |   no rank |       |   8   |   1   |   1   |   1   |   0      |
```


### names

```
$ grep -c  'scientific name' names.dmp
1660013
```

```
2       |       Bacteria        |       Bacteria <prokaryotes>  |       scientific name |

```

```
40117   |       'Nitrospirae'   |               |       synonym |
40117   |       Nitrospira group        |               |       synonym |
40117   |       Nitrospirae     |               |       scientific name |
40117   |       Nitrospiraeota  |               |       synonym |
40117   |       Nitrospiraeota Oren et al. 2015 |               |       authority       |
40117   |       Thermodesulfovibrio group       |               |       synonym |
```

```
203693  |       Nitrospira      |       Nitrospira <class>      |       scientific name |
203693  |       Nitrospiria     |               |       synonym |
203693  |       Nitrospiria Oren et al. 2015    |               |       authority       |
```

```
189778  |       'Nitrospirales' |               |       synonym |
189778  |       Nitrospirales   |               |       scientific name |
```

```
189779  |       'Nitrospiraceae'        |               |       synonym |
189779  |       Nitrospiraceae  |               |       scientific name |
```

```
1234    |       Nitrospira      |       Nitrospira <genus>      |       scientific name |
1234    |       Nitrospira Watson et al. 1986   |               |       authority       |
```

```
1946986 |       Nitrospira sp. UBA2082  |               |       scientific name |
```




### Select 
```
sqlite> select taxa_id  from TaxaNameLevel where taxa_name = 'Zavarzinella';
taxa_id
600332

sqlite> select parent_id from  TaxaParent where taxa_id = 600332;
parent_id
1914233

sqlite> select parent_id from  TaxaParent where taxa_id = 1914233;
parent_id
112

sqlite> select parent_id from  TaxaParent where taxa_id = 112;
parent_id
203683

sqlite> select parent_id from  TaxaParent where taxa_id = 203683;
parent_id
203682

sqlite> select parent_id from  TaxaParent where taxa_id = 203682;
parent_id
1783257

sqlite> select parent_id from  TaxaParent where taxa_id = 1783257;
parent_id
2

sqlite> select parent_id from  TaxaParent where taxa_id = 2;
parent_id
131567

sqlite> select parent_id from  TaxaParent where taxa_id = 131567;
parent_id
1

sqlite> select parent_id from  TaxaParent where taxa_id = 1;
parent_id
1

```


```
sqlite> select taxa_name, taxa_level from TaxaNameLevel where taxa_id = 1914233;
taxa_name|taxa_level
Gemmataceae|family


sqlite> select taxa_name, taxa_level from TaxaNameLevel where taxa_id =  112;
taxa_name|taxa_level
Planctomycetales|order

sqlite> select taxa_name, taxa_level from TaxaNameLevel where taxa_id = 203683;
taxa_name|taxa_level
Planctomycetia|class

sqlite> select taxa_name, taxa_level from TaxaNameLevel where taxa_id = 203682;
taxa_name|taxa_level
Planctomycetes|phylum

sqlite> select taxa_name, taxa_level from TaxaNameLevel where taxa_id = 1783257;
taxa_name|taxa_level
PVC group|no rank


sqlite> select taxa_name, taxa_level from TaxaNameLevel where taxa_id = 2;
taxa_name|taxa_level
Bacteria|superkingdom
```

### superkingdom 
```
$ grep superkingdom nodes.dmp

2   |   131567  |   superkingdom    |       |   0   |   0   |   11  |   0   ||
2157    |   131567  |   superkingdom    |       |   0   |   0   |   11  |   0   ||
2759    |   131567  |   superkingdom    |       |   1   |   0   |   1   |   0   ||
10239   |   1   |   superkingdom    |       |   9   |   0   |   1   |   0   ||
12884   |   1   |   superkingdom    |       |   9   |   0   |   1   |   0   |

4751    |   33154   |   kingdom |       |   4   |   0   |   1   |   1   |   4
33090   |   2759    |   kingdom |       |   4   |   0   |   1   |   1   |   1|
33208   |   33154   |   kingdom |       |   1   |   0   |   1   |   1   |   1

451864  |   4751    |   subkingdom  |       |   4   |   1   |   1   |   1   |
```


```
2       |       Bacteria        |       Bacteria <prokaryotes>  |       scientific name |
2157    |       Archaea |               |       scientific name |
2759    |       Eukaryota       |               |       scientific name |
10239   |       Viruses |               |       scientific name |
12884   |       Viroids |               |       scientific name |

4751    |       Fungi   |               |       scientific name |
33090   |       Viridiplantae   |               |       scientific name |
33208   |       Metazoa |               |       scientific name |

451864  |       Dikarya |               |       scientific name |

```


### create taxanomy.db database
```
$ sqlite3 taxanomy.db
SQLite version 3.25.3 2018-11-05 20:37:38
Enter ".help" for usage hints.
sqlite> .header on
sqlite> .table
TaxaNameLevel  TaxaParent   

sqlite> select * from TaxaNameLevel limit 5;
taxa_id|taxa_name|taxa_level
1|root|no rank
2|Bacteria|superkingdom
6|Azorhizobium|genus
7|Azorhizobium caulinodans|species
9|Buchnera aphidicola|species

sqlite> select * from TaxaParent limit 5;
taxa_id|parent_id
1|1
2|131567
6|335928
7|6
9|32199
```