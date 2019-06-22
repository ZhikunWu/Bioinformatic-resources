## [RSeQC](https://github.com/dnanexus/rseqc): RNA-Seq Quality Control

### install RSeQC
```
pip2 install qc bitsets RSeQC

pip2 install --upgrade cython bx-python pysam RSeQC numpy
```

#### install using conda
It need the environment of python 2.7
```
$ conda install -c bioconda rseqc
```

####  install using code source
```
sudo apt-get install libpython2.7-dev
wget 'http://downloads.sourceforge.net/project/rseqc/RSeQC-2.6.4.tar.gz'
tar zxvf RSeQC-2.6.4.tar.gz
RSeQC-2.6.4
python ./setup.py build
sudo python ./setup.py install
```


#### error
```
processing /home/zhouy/seqhealth/database/Sesamum_indicum/Sesamum_indicum_v1.0.gene_exon.bed ...Traceback (most recent call last):
  File "/home/zhouy/anaconda3/envs/kcmRNA/bin/RSeQC-2.6/scripts/read_distribution.py", line 303, in <module>
    main()
  File "/home/zhouy/anaconda3/envs/kcmRNA/bin/RSeQC-2.6/scripts/read_distribution.py", line 192, in main
    intergenic_down1kb_base,intergenic_down5kb_base,intergenic_down10kb_base) = process_gene_model(options.ref_gene_model)
  File "/home/zhouy/anaconda3/envs/kcmRNA/bin/RSeQC-2.6/scripts/read_distribution.py", line 81, in process_gene_model
    intron = BED.unionBed3(intron)
  File "/home/zhouy/anaconda3/envs/kcmRNA/lib/python2.7/site-packages/RSeQC-2.6-py2.7-linux-x86_64.egg/qcmodule/BED.py", line 2389, in unionBed3
    bitsets = binned_bitsets_from_list(lst)
  File "/home/zhouy/anaconda3/envs/kcmRNA/lib/python2.7/site-packages/RSeQC-2.6-py2.7-linux-x86_64.egg/bx/bitset_builders.py", line 143, in binned_bitsets_from_list
    last_bitset.set_range( start, end - start )
  File "bitset.pyx", line 212, in bx.bitset.BinnedBitSet.set_range (lib/bx/bitset.c:3155)
  File "bitset.pyx", line 183, in bx.bitset.bb_check_range_count (lib/bx/bitset.c:2613)
IndexError: Count (-10575) must be non-negative.

```

#### answer
Python路径+/site-packages/rpy2/rinterface/__init__.py

add two lines in line 92
```
import readline
import rpy2.robjects
```


### run RSeQC
```
$ python /home/wzk/anaconda3/envs/kcmRNA/bin/RSeQC-2.6/scripts/bam_stat.py -i Aligned.sortedByCoord.out.bam

Load BAM file ...  Done

#==================================================
#All numbers are READ count
#==================================================

Total records:                          89170257

QC failed:                              0
Optical/PCR duplicate:                  0
Non primary hits                        8567025
Unmapped reads:                         8488450
mapq < mapq_cut (non-unique):           5288154

mapq >= mapq_cut (unique):              66826628
Read-1:                                 33423323
Read-2:                                 33403305
Reads map to '+':                       33351183
Reads map to '-':                       33475445
Non-splice reads:                       45959324
Splice reads:                           20867304
Reads mapped in proper pairs:           60901684
Proper-paired reads map to different chrom:0

```
