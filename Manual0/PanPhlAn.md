## [PanPhlAn](http://segatalab.cibio.unitn.it/tools/panphlan/)

### [PanPhlAn tutorial](https://bitbucket.org/CibioCM/panphlan/wiki/Tutorial)

### install panphlan
```bash
$ hg clone https://bitbucket.org/CibioCM/panphlan
```
or
```bash
$ wget https://bitbucket.org/cibiocm/panphlan/get/default.zip
$ unzip default.zip
$ mkdir panphlan
$ mv CibioCM-panphlan-*/panphlan_* panphlan/
```

Add the paths of your installed tools to your `.bashrc` file
```bash
export PATH=/your/path/to/samtools/:$PATH
export PATH=/your/path/to/bowtie2/bowtie2-2.1.0/:$PATH
export BT2_HOME=/your/path/to/bowtie2/bowtie2-2.1.0/
export BOWTIE2_INDEXES=/your/path/to/PanPhlAn_DB/and/bowtie2_indexes/
```


