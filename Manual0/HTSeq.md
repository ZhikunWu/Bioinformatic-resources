## HTSeq manual

### install htseq
```
$ conda install -c bioconda htseq 
```


### count each contigs using samtools
```
$ samtools index HMP_GUT_SRS052697.25M.mapped.sorted.bam
$ samtools idxstats HMP_GUT_SRS052697.25M.mapped.sorted.bam >  HMP_GUT_SRS052697.25M.idxstats.txt

$ samtools index HMP_MOCK_SRR2726667_8.25M.mapped.sorted.bam
$ samtools idxstats HMP_MOCK_SRR2726667_8.25M.mapped.sorted.bam > HMP_MOCK_SRR2726667_8.25M.idxstats.txt
```

### download some scripts to process this file
```
$ git clone https://github.com/metajinomics/mapping_tools.git

$ python /home/wzk/anaconda3/envs/qiime/bin/mapping_tools/get_count_table.py *.idxstats.txt > contig_counts.tsv
```

out files:
```
$ less contig_counts.tsv

contig  length  HMP_GUT_SRS052697.25M.idxstats.txt      HMP_MOCK_SRR2726667_8.25M.idxstats.txt
k141_1  302     0       0
k141_2  329     0       0
k141_3  309     0       0
k141_4  345     0       0
k141_5  362     0       0
k141_6  335     0       0
```


### count each genes


#### make gtf
```bash
$ python /home/wzk/anaconda3/envs/qiime/bin/mapping_tools/350_to_gtf.py ../annotate/MetaContig.faa > MetaContig.gtf
```

#### count using HTSeq
```bash
$ htseq-count  -f bam  HMP_GUT_SRS052697.25M.mapped.sorted.bam  MetaContig.gtf > HMP_GUT_SRS052697.25M_htseq_count
Error occured when processing GFF file (line 1 of file MetaContig.gtf):
  invalid literal for int() with base 10: 'motif=None;rbs'
  [Exception type: ValueError, raised in __init__.py:210]

 ```

HTSeq的作者Simon Anders建议使用ENSEMBL的gtf文件。  但是如果用了ensembl的，那么之前tophat就应该用ensembl的gtf作为参考来比对

#### merge the counts
```bash
python htseq_count_table.py *_count > final.table
```

