## [StrainPhlAn](http://segatalab.cibio.unitn.it/tools/strainphlan/)
A metagenomic strain-level population genomics tool

### install strainPhlAn
```bash
$ conda install -c bioconda pysam
$ conda install -c bioconda biopython
$ conda install -c conda-forge numpy
$ conda install -c conda-forge msgpack-python
#conda install -c dan_blanchard msgpack 
$ pip install -i https://pypi.anaconda.org/pypi/simple dendropy #dendropy=3.12.0
#conda install -c judowill dendropy

$ conda install -c bioconda muscle
$ conda install -c bioconda bcftools
$ conda install -c bioconda raxml

```

#### it quire [samtools 0.1.19](https://sourceforge.net/projects/samtools/files/samtools/0.1.19/)
```bash
$ tar -jxf samtools-0.1.19.tar.bz2
$ cd samtools-0.1.19/
$ ./configure --prefix=/home/wzk/anaconda3/envs/qiime
$ make
```



