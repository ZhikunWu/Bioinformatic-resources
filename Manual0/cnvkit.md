# Copy Number Variation using [CNVkit](https://cnvkit.readthedocs.io/en/stable/index.html)

## Install cnvkit
Install cnvkit through bioconda
```
$ conda install -c bioconda cnvkit
```




## Manual for arabidopsis

### Get access region for genome

```
$ cnvkit.py access  -o arabidop.bed Arabidopsis_thaliana.TAIR10.dna.toplevel.fa  -s 10000
```

output file

```
1       0       14511721
1       14538721        14545721
1       14581719        14610668
1       14656720        14750970
1       14803970        30427671
2       1000    19698289
3       100     23459830
4       1000    18585056
5       0       26975502
```

### Get the converage for target regions

```
$ cnvkit.py coverage mapping/Ler/Ler_realigned.bam /home/wzk/database/GENOME/arabidopsis/arabidop.bed -o Ler_coverage.cnn -p 20


Processing reads in Ler_realigned.bam
Time: 326.649 seconds (92270 reads/sec, 0 bins/sec)
Summary: #bins=9, #reads=30139867, mean=3348874.2068, min=160.059602649, max=6603200.82781 
Percent reads in regions: 61.471 (of 49031342 mapped)
Wrote Ler_coverage.cnn with 9 regions

```

### Get reference based on control sample
```
$ cnvkit.py reference Ler_coverage.cnn --fasta /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa -o Ler_reference.cnn


Number of target and antitarget files: 1, 0
No X found in sample; is the input truncated?
Loading Ler_coverage.cnn
Calculating GC and RepeatMasker content in /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa ...
Extracting sequences from chromosome 1
Extracting sequences from chromosome 2
Extracting sequences from chromosome 3
Extracting sequences from chromosome 4
Extracting sequences from chromosome 5
Extracting sequences from chromosome Mt
Extracting sequences from chromosome Pt
Correcting for GC bias...
Correcting for density bias...
Calculating average bin coverages
Calculating bin spreads
Targets: 5362 (16.3311%) bins failed filters (log2 < -5.0, log2 > 5.0, spread > 1.0)
Wrote Ler_reference.cnn with 32833 regions

```
output:
```
chromosome      start   end     gene    depth   log2
1       0       266     -       44.4211 5.47317
1       266     533     -       44.7004 5.48222
1       533     799     -       37.5977 5.23257
1       799     1066    -       29.8801 4.90112
1       1066    1333    -       26.191  4.711
1       1333    1599    -       34.6654 5.11543
1       1599    1866    -       45.9663 5.5225

```


### Fix the treated samples based on reference
First we should create empty file of **MT_anti.cnn** if it has no anti target region.
```
$ cnvkit.py fix MT_coverage.cnn MT_anti.cnn Ler_reference.cnn -o MT.cnr
```
output:
```
$ head MT.cnr
chromosome      start   end     gene    depth   log2    weight
1       0       266     -       54.2444 0.138234        0.875131
1       266     533     -       52.9963 0.0496327       0.873867
1       533     799     -       60.782  0.163466        0.971436
1       799     1066    -       49.3446 0.461645        0.975697
1       1066    1333    -       24.4082 -0.651446       0.911511
1       1333    1599    -       45.2218 0.0504109       0.978193
1       1599    1866    -       44.2022 -0.290924       0.865223
1       1866    2133    -       20.2697 -0.622256       0.956193
1       2133    2399    -       17.1955 -0.912394       0.987237
```


### Get CNS for samples

```
$ cnvkit.py segment MT.cnr -o  MT.cns
```

output:
```
chromosome      start   end     gene    log2    depth   probes  weight
1       0       7065327 -       -0.0311254      49.9115 26142   24629.9
1       7065593 7075193 -       0.804518        127.599 36      24.5463
1       7075193 8786392 -       -0.045626       47.6727 6169    5780.29
1       8786392 8798659 -       0.591066        86.7761 33      25.6681
1       8798659 11660523        -       -0.0449118      47.0076 10121   9441.49
1       11660523        11885589        -       0.0136426       45.3385 811     755.979
1       11885589        11902656        -       0.408484        62.8147 58      48.5845
1       11902656        12769055        -       0.0090103       47.7473 3007    2764.7
1       12775722        12804522        -       -1.14107        11.5604 10      6.16859
1       12804522        13258922        -       0.0490368       47.1151 1444    1305.16
1       13258922        13704255        -       0.15143 53.7465 1507    1343.12

```





### Plotting
```
$ cnvkit.py scatter MT.ncr -s  MT.cns  -o MT-scatter.pdf
```


```
$ cnvkit.py diagram MT.ncr -s  MT.cns  -o MT-diagram.pdf
```


## Run with batch in one command

### gtf to genephred
```
$ gtfToGenePred Arabidopsis_thaliana.TAIR10.35.gtf Arabidopsis_thaliana.TAIR10.35.refseq.txt
```


### batch
```
$ cnvkit.py batch mapping/MT/MT_realigned.bam --normal mapping/Ler/Ler_realigned.bam   --targets /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.bed  --fasta /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa  --access /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.bed  --output-reference my_reference.cnn --output-dir cnvkit --method wgs -p 10 --diagram --scatter  

CNVkit 0.9.4.dev0
Detected file format: bed
Splitting large targets
Wrote cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.target.bed with 446183 regions
Detected file format: bed
Wrote cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.antitarget.bed with 0 regions
Building a copy number reference from normal samples...
Processing reads in Ler_realigned.bam
Time: 4832.188 seconds (6237 reads/sec, 92 bins/sec)
Summary: #bins=446183, #reads=30140603, mean=67.5521, min=0.0, max=92717.4370861 
Percent reads in regions: 61.472 (of 49031342 mapped)
Wrote cnvkit/Ler_realigned.targetcoverage.cnn with 446183 regions
Skip processing Ler_realigned.bam with empty regions file cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.antitarget.bed
Wrote cnvkit/Ler_realigned.antitargetcoverage.cnn with 0 regions
No X found in sample; is the input truncated?
Loading cnvkit/Ler_realigned.targetcoverage.cnn
Calculating GC and RepeatMasker content in /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa ...
Extracting sequences from chromosome 1
Extracting sequences from chromosome 2
Extracting sequences from chromosome 3
Extracting sequences from chromosome 4
Extracting sequences from chromosome 5
Correcting for GC bias...
Correcting for density bias...
Calculating average bin coverages
Calculating bin spreads
Loading cnvkit/Ler_realigned.antitargetcoverage.cnn
Targets: 36483 (8.1767%) bins failed filters (log2 < -5.0, log2 > 5.0, spread > 1.0)
Wrote my_reference.cnn with 446183 regions
Running 1 samples in serial
Running the CNVkit pipeline on mapping/MT/MT_realigned.bam ...
Processing reads in MT_realigned.bam
Time: 7374.829 seconds (6047 reads/sec, 61 bins/sec)
Summary: #bins=446183, #reads=44592510, mean=99.9422, min=0.0, max=111225.562914 
Percent reads in regions: 59.060 (of 75503293 mapped)
Wrote cnvkit/MT_realigned.targetcoverage.cnn with 446183 regions
Skip processing MT_realigned.bam with empty regions file cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.antitarget.bed
Wrote cnvkit/MT_realigned.antitargetcoverage.cnn with 0 regions
Processing target: MT_realigned
Keeping 409700 of 446183 bins
Correcting for GC bias...
Correcting for density bias...
No X found in sample; is the input truncated?
Processing antitarget: MT_realigned
Wrote cnvkit/MT_realigned.cnr with 409700 regions
Segmenting cnvkit/MT_realigned.cnr ...
Segmenting with method 'cbs', significance threshold 0.0001, in 1 processes
Wrote cnvkit/MT_realigned.cns with 156 regions
Wrote cnvkit/MT_realigned-scatter.pdf
No X found in sample; is the input truncated?
No X found in sample; is the input truncated?
No X found in sample; is the input truncated?
Wrote cnvkit/MT_realigned-diagram.pdf

```


cnvkit.py 为运行的脚本

batch是脚本内的一个整合了很多命令的方法，当然也可以使用cnvkit.py提供的access、coverrage、fix等方法一起来完成和batch同样功能的分析，但是作为懒人还是建议使用batch。

Tumor.bam 和Normal.bam都是相应样本的bam文件，建议用bwa通过ucsc的hg38参考基因组做mapping，并用samtool排序转换成bam格式。这里可以输入多个tumor.bam和normal.bam

--targets 想要分析的区域信息

--annotate refFlat格式的基因注释信息，可以从UCSC上下载

--fasta 参考基因组

--access 需要跟bed文件，可用过cnvkit.py access mm10.fasta -s 10000 -o access-10kb.mm10.bed 生成

--output-reference 输出的reference.cnn可以作为下一批tumor数据分析的输入文件，reference.cnn和输入的normal.bam有关

--output-dir 输出目录名

--diagram –scatter 两个都是顺带绘图的参数

--processes 处理的线程数




### analysis for multiple samples
假如我们还需要对其他样本进行分析，而对照样本与上述一样，则可以基于得到的**my_reference.cnn**文件，简化分析步骤：
```
$ cnvkit.py batch  sample2.bam --reference my_flat_reference.cnn -d sample2 -p 10  --scatter  --diagram
```



## Others

### gff to bed
```
$ convert2bed --input gff --output bed < /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35.gff3 > /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35.bed
```

### gtf to bed
```
$ convert2bed --input gtf --output bed < /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35-1.gtf  > /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35.bed
Error: Potentially missing gene or transcript ID from GTF attributes (malformed GTF at line [1]?)
```

```
$ awk '{ if ($0 ~ "transcript_id") print $0; else print $0" transcript_id \"\";"; }' /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35-1.gtf | gtf2bed  >  /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35.bed
```

```
ValueError: Duplicated genomic coordinates in sample set:
Pandas(chromosome='1', start=9473379, end=9473379)
Pandas(chromosome='1', start=10489781, end=10489781)

$ grep 9473379 MT_coverage.cnn
1	9473379	9473379	AT1G06063	0	-20
1	9473379	9473379	AT1G06067	0	-20

$ awk '{if($2!=$3){print $0}}' MT_coverage.cnn > MT_coverage-1.cnn
$ awk '{if($2!=$3){print $0}}' Ler_reference.cnn > Ler_reference-1.cnn
```




### cnr and cns files
```
$ cnvkit.py fix MT_coverage-1.cnn MT_anti.cnn Ler_reference-1.cnn -o MT.ncr
Blank tab file?: MT_anti.cnn
Processing target: MT_coverage-1
Keeping 27471 of 28436 bins
Correcting for GC bias...
Correcting for density bias...
No X found in sample; is the input truncated?
Processing antitarget: MT_anti
Wrote MT.ncr with 27471 regions

```

```
$ cnvkit.py segment MT.ncr -o  MT.cns
```

```
$ cnvkit.py scatter MT.ncr -s  MT.cns  -o MT-scatter.pdf
```

```
$ cnvkit.py diagram MT.ncr -s  MT.cns  -o MT-diagram.pdf
```





```
$ cnvkit.py batch mapping/MT/MT_realigned.bam --normal mapping/Ler/Ler_realigned.bam   --targets /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.bed  --fasta /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa  --access /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.bed --annotate /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35.gff3   --output-reference my_reference.cnn --output-dir cnvkit --method wgs -p 20 --diagram --scatter

Estimated read length 151.0
WGS average depth 49.51 --> using bin size 1010
Detected file format: bed
Splitting large targets
Applying annotations as target names
Detected file format: gff
Wrote cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.target.bed with 117803 regions
Wrote cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.antitarget.bed with 0 regions
Building a copy number reference from normal samples...
Processing reads in Ler_realigned.bam
Skip processing Ler_realigned.bam with empty regions file cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.antitarget.bed
Wrote cnvkit/Ler_realigned.antitargetcoverage.cnn with 0 regions
Time: 225.481 seconds (133669 reads/sec, 522 bins/sec)
Summary: #bins=117803, #reads=30139867, mean=255.8497, min=0.0, max=182677.582781 
Percent reads in regions: 61.471 (of 49031342 mapped)
Wrote cnvkit/Ler_realigned.targetcoverage.cnn with 117803 regions
No X found in sample; is the input truncated?
Loading cnvkit/Ler_realigned.targetcoverage.cnn
Calculating GC and RepeatMasker content in /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa ...
Extracting sequences from chromosome 1
Extracting sequences from chromosome 2
Extracting sequences from chromosome 3
Extracting sequences from chromosome 4
Extracting sequences from chromosome 5
Correcting for GC bias...
Calculating average bin coverages
Calculating bin spreads
Loading cnvkit/Ler_realigned.antitargetcoverage.cnn
Targets: 8145 (6.9141%) bins failed filters (log2 < -5.0, log2 > 5.0, spread > 1.0)
Moved existing file my_reference.cnn -> my_reference.cnn.1
Wrote my_reference.cnn with 117803 regions
Running 1 samples in 20 processes (that's 20 processes per bam)
Running the CNVkit pipeline on mapping/MT/MT_realigned.bam ...
Processing reads in MT_realigned.bam
Time: 381.225 seconds (116984 reads/sec, 309 bins/sec)
Summary: #bins=117803, #reads=44597154, mean=378.5740, min=0.0, max=253159.298013 
Percent reads in regions: 59.067 (of 75503293 mapped)
Wrote cnvkit/MT_realigned.targetcoverage.cnn with 117803 regions
Skip processing MT_realigned.bam with empty regions file cnvkit/Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.antitarget.bed
Wrote cnvkit/MT_realigned.antitargetcoverage.cnn with 0 regions
Processing target: MT_realigned
Keeping 109658 of 117803 bins
Correcting for GC bias...
No X found in sample; is the input truncated?
Processing antitarget: MT_realigned
Wrote cnvkit/MT_realigned.cnr with 109658 regions
Segmenting cnvkit/MT_realigned.cnr ...
Segmenting with method 'cbs', significance threshold 1e-06, in 20 processes
Wrote cnvkit/MT_realigned.cns with 65 regions
Wrote cnvkit/MT_realigned-scatter.pdf
No X found in sample; is the input truncated?
No X found in sample; is the input truncated?
No X found in sample; is the input truncated?
Wrote cnvkit/MT_realigned-diagram.pdf

```


```
$ head Arabidopsis_thaliana.TAIR10.dna.toplevel_10kb.target.bed
1	0	1010	-
1	1010	2020	-
1	2020	3030	-
1	3030	4040	-,AT1G01010.1.exon1,NAC001,AT1G01010.1.exon2
1	4040	5050	-,NAC001,AT1G01010.1.exon2,AT1G01010.1.exon3,AT1G01010.1.exon4
1	5050	6060	-,NAC001,AT1G01010.1.exon4,AT1G01010.1.exon5,AT1G01010.1.exon6
1	6060	7070	-,AT1G01020.2.exon8,AT1G01020.1.exon9,ARV1
1	7070	8080	-,ARV1,AT1G01020.1.exon8,AT1G01020.2.exon7,AT1G01020.1.exon7,AT1G01020.1.exon6,AT1G01020.1.exon5,AT1G01020.1.exon4
1	8080	9090	-,ARV1,AT1G01020.1.exon3,AT1G01020.4.exon2,AT1G01020.5.exon2,AT1G01020.1.exon2,AT1G01020.2.exon1,AT1G01020.3.exon1,AT1G01020.1.exon1,AT1G01020.6.exon1,AT1G01020.4.exon1
1	9090	10100	-,ARV1,AT1G01020.3.exon1,AT1G01020.1.exon1,AT1G01020.4.exon1
```

```
$ head Ler_realigned.targetcoverage.cnn
chromosome	start	end	gene	depth	log2
1	0	1010	-	39.9743	5.321
1	1010	2020	-	35.0604	5.13177
1	2020	3030	-	36.4653	5.18845
1	3030	4040	-,AT1G01010.1.exon1,NAC001,AT1G01010.1.exon2	35.5762	5.15284
1	4040	5050	-,NAC001,AT1G01010.1.exon2,AT1G01010.1.exon3,AT1G01010.1.exon4	37.3584	5.22336
1	5050	6060	-,NAC001,AT1G01010.1.exon4,AT1G01010.1.exon5,AT1G01010.1.exon6	38.6059	5.27075
1	6060	7070	-,AT1G01020.2.exon8,AT1G01020.1.exon9,ARV1	43.0535	5.42806
1	7070	8080	-,ARV1,AT1G01020.1.exon8,AT1G01020.2.exon7,AT1G01020.1.exon7,AT1G01020.1.exon6,AT1G01020.1.exon5,AT1G01020.1.exon4	35.1941	5.13726
1	8080	9090	-,ARV1,AT1G01020.1.exon3,AT1G01020.4.exon2,AT1G01020.5.exon2,AT1G01020.1.exon2,AT1G01020.2.exon1,AT1G01020.3.exon1,AT1G01020.1.exon1,AT1G01020.6.exon1,AT1G01020.4.exon1	39.5832	5.30682
```

```
$ head MT_realigned.cnr
chromosome	start	end	gene	depth	log2	weight
1	0	1010	-	55.0416	0.230483	0.922875
1	1010	2020	-	36.6762	-0.201555	0.970781
1	2020	3030	-	36.7356	-0.277797	0.960563
1	3030	4040	-,AT1G01010.1.exon1,NAC001,AT1G01010.1.exon2	40.1297	-0.211368	0.976721
1	4040	5050	-,NAC001,AT1G01010.1.exon2,AT1G01010.1.exon3,AT1G01010.1.exon4	55.1059	-0.0407982	0.992816
1	5050	6060	-,NAC001,AT1G01010.1.exon4,AT1G01010.1.exon5,AT1G01010.1.exon6	45.4723	-0.207783	0.96637
1	6060	7070	-,AT1G01020.2.exon8,AT1G01020.1.exon9,ARV1	64.3277	0.110805	0.937412
1	7070	8080	-,ARV1,AT1G01020.1.exon8,AT1G01020.2.exon7,AT1G01020.1.exon7,AT1G01020.1.exon6,AT1G01020.1.exon5,AT1G01020.1.exon4	47.2842	0.057713	0.97741
1	8080	9090	-,ARV1,AT1G01020.1.exon3,AT1G01020.4.exon2,AT1G01020.5.exon2,AT1G01020.1.exon2,AT1G01020.2.exon1,AT1G01020.3.exon1,AT1G01020.1.exon1,AT1G01020.6.exon1,AT1G01020.4.exon1	43.8931	-0.191407	0.941506
```





