## [svviz2](https://github.com/nspies/svviz2)

### install svviz2

```
conda install -c bioconda pysam
conda install -c bioconda numpy
conda install -c r rpy2
conda install -c conda-forge pybind11
pip install -U git+git://github.com/nspies/svviz2.git
```

### run svviz2
```
$ svviz2 --ref /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --variants probands_denovo_common.bcf  /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M625-0.bam
```



