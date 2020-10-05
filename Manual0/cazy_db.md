
## [dbCAN](http://csbl.bmb.uga.edu/dbCAN/index.php)
## [dbCAN_seq](http://cys.bios.niu.edu/dbCAN_seq/download.php)

## [cazy-parser](https://github.com/rodrigovrgs/cazy-parser)

### Database creation
```
$ create_cazy_db
```
This script will parse the CAZy database website and create a comma separated table containing the following information:
```
domain
protein_name
family
tag (characterized status)
organism_code
EC number (ec stands for enzyme comission number)
GENBANK id
UNIPROT code
subfamily
organism
PDB code
```


### Extract sequences
Based on the previously generated csv table, extract accession codes for a given protein family.
```
$ extract_cazy_ids --db <database> --family <family code>
```
Optional:

```
--subfamilies Create a file for each subfamily, default = False

--characterized Create a file containing only characterized enzymes, default = False
```

### Usage examples
Extract all accession codes from family 9 of Glycosyl Transferases.
```
$ extract_cazy_ids --db CAZy_DB_xx-xx-xxxx.csv --family GT9
```

This will generate the following files:
```
GT9.csv
```
Extract all accession codes from family 43 of Glycoside Hydrolase, including subfamilies
```
$ extract_cazy_ids --db CAZy_DB_xx-xx-xxxx.csv --family GH43 --subfamilies
```


This will generate the following files:
```
GH43.csv
GH43_sub1.csv
GH43_sub2.csv
GH43_sub3.csv
(...)
GH43_sub37.csv
```


Extract all accession codes from family 42 of Polysaccharide Lyases including characterized entries

```
$ extract_cazy_ids --db CAZy_DB_xx-xx-xxxx.csv --family PL42 --characterized
```

This will generate the following files:
```
PL42.fasta
PL42_characterized.fasta
````



### hmm for CAZy
```
$ hmmpress /home/wzk/metagenome_data/CAZy/dbCAN-fam-HMMs.txt
```
output files:
```
-rw-r--r-- 1 15M Dec  6 08:00 dbCAN-fam-HMMs.txt.h3f
-rw-r--r-- 1 29K Dec  6 08:00 dbCAN-fam-HMMs.txt.h3i
-rw-r--r-- 1 34M Dec  6 08:00 dbCAN-fam-HMMs.txt.h3m
-rw-r--r-- 1 40M Dec  6 08:00 dbCAN-fam-HMMs.txt.h3p


```


run hmm
```
$ hmmscan --cpu 10 --tblout /home/wzk/metagenome_data/CAZy/representive.tblout   --domtblout /home/wzk/metagenome_data/CAZy/representive.domtblout --pfamtblout /home/wzk/metagenome_data/CAZy/representive.pfamtblout  -o /home/wzk/metagenome_data/CAZy/representive_hmm_out.txt   /home/wzk/metagenome_data/CAZy/dbCAN-fam-HMMs.txt  /home/wzk/metagenome_data/ORFCluster/representive.faa
```


