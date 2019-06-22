
## [jcvi](https://github.com/tanghaibao/jcvi): Python version of MCscan

### [其实MCScan画图也可以很好看](https://www.jianshu.com/p/39448b970287)

### install jcvi
It is based on python 2
```
$ conda install -c bioconda jcvi
```


### download test data

```
$ python -m jcvi.apps.fetch phytozome Vvinifera,Ppersica
```

files:
```
-rw-r--r-- 1  11M Dec  4 03:43 Ppersica_139_cds.fa.gz
-rw-r--r-- 1 3.3M Dec  4 03:43 Ppersica_139_gene.gff3.gz
-rw-r--r-- 1 8.4M Dec  4 03:41 Vvinifera_145_cds.fa.gz
-rw-r--r-- 1 3.4M Dec  4 03:23 Vvinifera_145_gene.gff3.gz

```

### Convert the GFF to BED file and rename them

```
$ python -m jcvi.formats.gff --help
[error] --help not a valid ACTION

Did you mean one of these?
    

Usage:
    python -m jcvi.formats.gff ACTION


Available ACTIONs:
        addparent | Merge sister features and infer their parent
              bed | Parse gff and produce bed file for particular feature type
            bed12 | Produce bed12 file for coding features
            chain | Fill in parent features by chaining children
         children | Find all children that belongs to the same parent
          cluster | Cluster transcripts based on shared splicing structure
          extract | Extract contig or features from gff file
           filter | Filter the gff file based on Identity and Coverage
    fixboundaries | Fix boundaries of parent features by range chaining child features
      fixpartials | Fix 5/3 prime partial transcripts, locate nearest in-frame start/stop
           format | Format the gff file, change seqid, etc.
          frombed | Convert from bed format to gff3
          fromgtf | Convert gtf to gff3 format
         fromsoap | Convert from soap format to gff3
         gapsplit | Split alignment GFF3 at gaps based on CIGAR string
               gb | Convert gff3 to genbank format
              gtf | Convert gff3 to gtf format
         liftover | Adjust gff coordinates based on tile number
             load | Extract the feature (e.g. CDS) sequences and concatenate
            merge | Merge several gff files into one
             note | Extract certain attribute field for each feature
           orient | Orient the coding features based on translation
          parents | Find the parents given a list of IDs
           rename | Change the IDs within the gff3
            sizes | Calculate sizes of features in gff file
             sort | Sort the gff file
        splicecov | Tag gff introns with coverage info from junctions.bed
            split | Split the gff into one contig per file
          summary | Print summary stats for features of different types
             uniq | Remove the redundant gene models

JCVI utility libraries v0.8.4 [Copyright (c) 2010-2017, Haibao Tang]

```


```
$ python -m jcvi.formats.gff bed
Usage: 
    gff.py bed gff_file [--options]

    Parses the start, stop locations of the selected features out of GFF and
    generate a bed file
    

Options:
  -h, --help            Show this help message and exit
  --type=TYPE           Feature type to extract, use comma for multiple
                        [default: gene]
  --key=KEY             Key in the attributes to extract [default: ID]
  --source=SOURCE       Source to extract from, use comma for multiple
                        [default: none]
  --span                Use feature span in the score column [default: False]
  --score_attrib=SCORE_ATTRIB
                        Attribute whose value is to be used as score in
                        `bedline` [default: False]
  --append_source       Append GFF source name to extracted key value
                        [default: False]
  --append_ftype        Append GFF feature type to extracted key value
                        [default: False]
  --nosort              Do not sort the output bed file [default: False]
  --strip_names         Strip alternative splicing (e.g. At5g06540.1 ->
                        At5g06540) [default: False]
  -o OUTFILE, --outfile=OUTFILE
                        Outfile name [default: stdout]

JCVI utility libraries v0.8.4 [Copyright (c) 2010-2017, Haibao Tang]
```

```
$ python -m jcvi.formats.gff bed --type=mRNA --key=Name Vvinifera_145_gene.gff3.gz -o grape.bed03:48:39 [base] Load file `Vvinifera_145_gene.gff3.gz`
03:48:53 [gff] Extracted 26346 features (type=mRNA id=Name)

$ python -m jcvi.formats.gff bed --type=mRNA --key=Name Ppersica_139_gene.gff3.gz -o peach.bed
03:48:59 [base] Load file `Ppersica_139_gene.gff3.gz`
03:49:12 [gff] Extracted 28701 features (type=mRNA id=Name)

```

#### clean headers to remove description fields from Phytozome FASTA files
```
$ python -m jcvi.formats.fasta format --sep="|" Vvinifera_145_cds.fa.gz grape.cds

$ python -m jcvi.formats.fasta format --sep="|" Ppersica_139_cds.fa.gz peach.cds

```


### Pairwise synteny search

```
$ python -m jcvi.compara.catalog ortholog grape peach
03:53:01 [base] lastdb peach peach.cds
/bin/bash: lastdb: command not found
03:53:01 [base] lastal -u 0 -P 40 -i3G -f BlastTab peach grape.cds >grape.peach.last
/bin/bash: lastal: command not found

```

#### solution
install **last**
```
$ conda install -c bioconda last
```

##### [last tutorial](http://last.cbrc.jp/doc/last-tutorial.html)
from scipy.spatial import cKDTree



#### run jcvi.compara.catalog

```
$ python -m jcvi.compara.catalog ortholog grape peach

  File "/home/wzk/anaconda3/envs/py27/lib/python2.7/site-packages/matplotlib/dviread.py", line 1045, in find_tex_file
    stderr=subprocess.PIPE)
  File "/home/wzk/anaconda3/envs/py27/lib/python2.7/site-packages/subprocess32.py", line 825, in __init__
    restore_signals, start_new_session)
  File "/home/wzk/anaconda3/envs/py27/lib/python2.7/site-packages/subprocess32.py", line 1574, in _execute_child
    raise child_exception_type(errno_num, err_msg)
OSError: [Errno 2] No such file or directory: 'kpsewhich'

```

#### [PyLaTeX](https://github.com/JelteF/PyLaTeX): A Python library for creating LaTeX files
```
$ conda install -c auto pylatex
```


```
$ python -m jcvi.compara.catalog ortholog grape peach

  File "/home/wzk/anaconda3/envs/py27/lib/python2.7/site-packages/scipy/linalg/lapack.py", line 356, in <module>
    from scipy.linalg import _flapack
ImportError: /home/wzk/anaconda3/envs/py27/lib/python2.7/site-packages/scipy/linalg/_flapack.so: undefined symbol: _gfortran_copy_string
```

