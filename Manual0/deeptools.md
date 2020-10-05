## [deeptools](https://github.com/fidelram/deepTools): http://deeptools.readthedocs.io/en/latest/

### install deeptools
```
$ conda install -c bioconda deeptools
```

### calculate the genebody converage

* bam files should be sorted and indexed
```
samtools index Aligned.sortedByCoord.out.bam
```

* run bamcoverage
```
bamCoverage -b Aligned.sortedByCoord.out.bam  -o coverage.bw
```

* the paramaters for bamcoverage
```
minFragmentLength: 0
verbose: False
out_file_for_raw_data: None
numberOfSamples: None
bedFile: None
bamFilesList: ['Aligned.sortedByCoord.out.bam']
ignoreDuplicates: False
numberOfProcessors: 20
samFlag_exclude: None
save_data: False
stepSize: 50
smoothLength: None
center_read: False
defaultFragmentLength: read length
chrsToSkip: []
region: None
maxPairedFragmentLength: 1000
samFlag_include: None
binLength: 50
blackListFileName: None
maxFragmentLength: 0
minMappingQuality: None
zerosToNans: False

```

* calculate the matrix based on the *.bed* and *.bam* file
```
computeMatrix scale-regions -S coverage.bw  -R /home/genome/human/wqj.bed --beforeRegionStartLength 3000 --regionBodyLength 5000 --afterRegionStartLength 3000 --skipZeros -o matrix.mat.gz
```

* plot the *.pdf* 
```
plotProfile -m matrix.mat.gz --perGroup -out matrix.mat.pdf
```
