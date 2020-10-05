## Annovar annotation

### [ANNOVAR进行突变注释](https://anjingwd.github.io/AnJingwd.github.io/2018/01/20/ANNOVAR进行突变注释/)
### [ANNOVAR的使用](https://www.jianshu.com/p/95331e7a98cd)

### download Annovar
```
wget http://www.openbioinformatics.org/annovar/download/0wgxR2rIVP/annovar.latest.tar.gz
```

you should register using your email and then get the link of software

### download database

#### gene-based annotation
```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  refGene humandb_19/

NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_refGene.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_refGeneMrna.fa.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_refGeneVersion.txt.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory

```


```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  knownGene   humandb_19/

NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_knownGene.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_kgXref.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_knownGeneMrna.fa.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory

```

```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  ensGene  humandb_19/

NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_ensGene.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_ensGeneMrna.fa.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory
```



#### [filter-based annotation](http://annovar.openbioinformatics.org/en/latest/user-guide/download/#-for-filter-based-annotation)

```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  snp138   humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_snp138.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_snp138.txt.idx.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory
```



```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  avdblist  humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_avdblist.txt.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory
```


```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  cosmic70   humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_cosmic70.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_cosmic70.txt.idx.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory
```

```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  clinvar_20180603    humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_clinvar_20180603.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_clinvar_20180603.txt.idx.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory
```


```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  1000g2015aug    humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_1000g2015aug.zip ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory

```




```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  esp6500siv2_all   humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_esp6500siv2_all.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_esp6500siv2_all.txt.idx.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory
```


```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  exac03  humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_exac03.txt.gz ... OK
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_exac03.txt.idx.gz ... OK
NOTICE: Uncompressing downloaded files
NOTICE: Finished downloading annotation files for hg19 build version, with files saved at the 'humandb_19' directory


```


```
$ perl annotate_variation.pl -downdb -webfrom annovar --buildver hg19  avsnp150  humandb_19/
NOTICE: Web-based checking to see whether ANNOVAR new version is available ... Done
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_avsnp150.txt.gz ... Failed
NOTICE: Downloading annotation database http://www.openbioinformatics.org/annovar/download/hg19_avsnp150.txt.idx.gz ... Failed
WARNING: Some files cannot be downloaded, including http://www.openbioinformatics.org/annovar/download/hg19_avsnp150.txt.idx.gz, http://www.openbioinformatics.org/annovar/download/hg19_avsnp150.txt.gz
```

```
annovar_protocol: refGene,cytoBand,GeneName,1000g2015aug_all,avsnp147,clinvar_20170130,cosmic80
operation: g,r,r,f,f,f,f

```

