## delly

### install delly

```
$ conda install -c bioconda delly
```

### run delly

python function:
```
 def dellySV_del(self):
        order = 'order finalbam_%s before dellySV_del_%s' % (self.sampleID,self.sampleID)
        dellyoutDir = os.path.join(self.svDIr,'delly')
        bam = os.path.join(self.bamDir,self.sampleID+'.final.bam')
        step = '  \\\n\t'.join(['%s/DELLY' %self.dellyDir,'-g %s' %self.refData, '-t DEL','-q 20','-n','-i 50','-u 20','-o %s' %os.path.join(dellyoutDir,self.sampleID+'.delly.del.vcf'),'%s' %bam])
        return 'echo "Delly del calling begin: " `date` && \\\n' + 'export OMP_NUM_THREADS=1 && \\\n' + step + ' && \\\necho "Delly del calling end: " `date`\n', order
```

shell command:
```
$ export OMP_NUM_THREADS=10 && delly call --genome /home/wzk/database/GENOME/rice/O_sativa_v7/all.con.fasta --outfile SRR5739119_SRR5739120_delly.bcl mapping/SRR5739119_realigned.bam mapping/SRR5739120_realigned.bam

Warning: The index file is older than the data file: mapping/SRR5739120_realigned.bai
[2018-Jan-18 20:10:21] delly call --genome /home/wzk/database/GENOME/rice/O_sativa_v7/all.con.fasta --outfile SRR5739119_SRR5739120_delly.bcl mapping/SRR5739119_realigned.bam mapping/SRR5739120_realigned.bam 
Warning: The index file is older than the data file: mapping/SRR5739120_realigned.bai
Warning: The index file is older than the data file: mapping/SRR5739120_realigned.bai
[2018-Jan-18 20:10:24] Paired-end clustering

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
Warning: The index file is older than the data file: mapping/SRR5739120_realigned.bai
[2018-Jan-18 20:33:05] Split-read alignment

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
Warning: The index file is older than the data file: mapping/SRR5739120_realigned.bai
[2018-Jan-18 20:40:04] Junction read annotation

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
Warning: The index file is older than the data file: mapping/SRR5739120_realigned.bai
[2018-Jan-18 20:42:48] Breakpoint spanning coverage annotation

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
Warning: The index file is older than the data file: mapping/SRR5739120_realigned.bai
[2018-Jan-18 20:43:50] Read-depth annotation

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
[2018-Jan-18 20:48:38] Genotyping

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
[2018-Jan-18 20:48:39] Library statistics
Sample: SRR5739119
RG: ID=1,ReadSize=125,AvgDist=10,EstCov=12.5,MappedAsPair=0.955528,Median=313,MAD=16,Layout=2,MaxSize=457,MinSize=169,UniqueDiscordantPairs=93891
Sample: SRR5739120
RG: ID=1,ReadSize=125,AvgDist=9,EstCov=13.8889,MappedAsPair=0.947587,Median=317,MAD=16,Layout=2,MaxSize=461,MinSize=173,UniqueDiscordantPairs=118452
[2018-Jan-18 20:48:39] Done.
```


#### result

##### output file header
```
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=GL,Number=G,Type=Float,Description="Log10-scaled genotype likelihoods for RR,RA,AA genotypes">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=FT,Number=1,Type=String,Description="Per-sample genotype filter">
##FORMAT=<ID=RC,Number=1,Type=Integer,Description="Raw high-quality read counts for the SV">
##FORMAT=<ID=RCL,Number=1,Type=Integer,Description="Raw high-quality read counts for the left control region">
##FORMAT=<ID=RCR,Number=1,Type=Integer,Description="Raw high-quality read counts for the right control region">
##FORMAT=<ID=CN,Number=1,Type=Integer,Description="Read-depth based copy-number estimate for autosomal sites">
##FORMAT=<ID=DR,Number=1,Type=Integer,Description="# high-quality reference pairs">
##FORMAT=<ID=DV,Number=1,Type=Integer,Description="# high-quality variant pairs">
##FORMAT=<ID=RR,Number=1,Type=Integer,Description="# high-quality reference junction reads">
##FORMAT=<ID=RV,Number=1,Type=Integer,Description="# high-quality variant junction reads">

```

##### variation
```
Chr12	4217039	DEL00006038	AGTTGGTTTCTACGTTTTAGCACAAGCAGAATATCAATCTAAAATGTTTCAGTTGGGTTCTATGTTTTTTTTCAGGTT	A	.	PASS	PRECISE;SVTYPE=DEL;SVMETHOD=EMBL.DELLYv0.7.7;CHR2=Chr12;END=4217117;PE=0;MAPQ=39;CT=3to5;CIPOS=-11,11;CIEND=-11,11;INSLEN=0;HOMLEN=10;SR=3;SRQ=0.985714;CONSENSUS=ATCTAAAATGTTTCAGTTGGGTTCTATGTTTTCAATGTTCAAAGAGAGAACCTTCATACCAGTCACGACGATTGACCCAGCTGCATGATCCCAGATCTTCTCTCTGTAACCTTTGTGTGGAAAACGCAAGTAAATGGCAC;CE=1.97702	GT:GL:GQ:FT:RCL:RC:RCR:CN:DR:DV:RR:RV	1/1:-47.8925,-1.21099,0:12:LowQual:784:515:751:1:0:0:1:17	0/0:0,-9.32501,-107.593:93:PASS:1614:3358:1438:2:0:0:31:0

$ grep '4217039' HY___F2.DEL.vcf
Chr12	4217039	DEL00003414	AGTTGGTTTCTACGTTTTAGCACAAGCAGAATATCAATCTAAAATGTTTCAGTTGGGTTCTATGTTTTTTTTCAGGTT	A	.	PASS	PRECISE;SVTYPE=DEL;SVMETHOD=EMBL.DELLYv0.7.7;CHR2=Chr12;END=4217117;PE=0;MAPQ=60;CT=3to5;CIPOS=-11,11;CIEND=-11,11;INSLEN=0;HOMLEN=10;SR=10;SRQ=0.986842;CONSENSUS=AGAATATCAATCTAAAATGTTTCAGTTGGGTTCTATGTTTTCAATGTTCAAAGAGAGAACCTTCATACCAGTCACGACGATTGACCCAGCTGCATGATCCCAGATCTTCTCTCTGTAACCTTTGTGTGGAAAACGCAAGTAAATGGCACCGT;CE=1.97416	GT:GL:GQ:FT:RCL:RC:RCR:CN:DR:DV:RR:RV	1/1:-47.8925,-1.21099,0:12:LowQual:784:515:751:1:0:0:1:17	1/1:-43.2988,-3.31008,0:33:PASS:257:174:611:0:0:0:0:11
```

### Structure variation type

DEL, INS, DUP, INV, BND
```
##ALT=<ID=DEL,Description="Deletion">
##ALT=<ID=DUP,Description="Duplication">
##ALT=<ID=INV,Description="Inversion">
##ALT=<ID=BND,Description="Translocation">
##ALT=<ID=INS,Description="Insertion">
```


#### FORMAT
```
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=GL,Number=G,Type=Float,Description="Log10-scaled genotype likelihoods for RR,RA,AA genotypes">
##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
##FORMAT=<ID=FT,Number=1,Type=String,Description="Per-sample genotype filter">
##FORMAT=<ID=RC,Number=1,Type=Integer,Description="Raw high-quality read counts for the SV">
##FORMAT=<ID=RCL,Number=1,Type=Integer,Description="Raw high-quality read counts for the left control region">
##FORMAT=<ID=RCR,Number=1,Type=Integer,Description="Raw high-quality read counts for the right control region">
##FORMAT=<ID=CN,Number=1,Type=Integer,Description="Read-depth based copy-number estimate for autosomal sites">
##FORMAT=<ID=DR,Number=1,Type=Integer,Description="# high-quality reference pairs">
##FORMAT=<ID=DV,Number=1,Type=Integer,Description="# high-quality variant pairs">
##FORMAT=<ID=RR,Number=1,Type=Integer,Description="# high-quality reference junction reads">
##FORMAT=<ID=RV,Number=1,Type=Integer,Description="# high-quality variant junction reads">
```


GT：基因型。
GL: 三种基因型的质量值。
GQ：基因型质量数。
FT：是否通过基因型过滤，PASS表示通过。
RC：支持结构变异高质量序列数。
RCL：左边控制区域高质量序列数。
RCR：右边控制区域高质量序列数。
CN：常染色体基于序列深度的拷贝数估计。
DR：高质量参照对数。
DV：高质量变异对数。
RR：高质量与参考一致的跨越序列数。
RV：高质量与变异一致的跨越序列数。


#### DEL
```
GT:GL:GQ:FT:RCL:RC:RCR:CN:DR:DV:RR:RV
0/1:-45.7787,0,-25.679:10000:PASS:3845:5936:3254:2:2:0:8:13
0/0:0,-3.00986,-40.0996:30:PASS:2040:7867:2559:3:1:0:10:0
1/1:-101.195,-8.7252,0:87:PASS:5460:99:4889:0:0:24:0:29
```

#### INS
```
GT:GL:GQ:FT:RCL:RC:RCR:CN:DR:DV:RR:RV
0/1:-93.8653,0,-22.1662:10000:PASS:0:0:0:-1:0:0:8:26
0/0:0,-4.21329,-54.8989:42:PASS:0:0:0:-1:0:0:14:0
1/1:-157.688,-13.8349,0:138:PASS:0:0:0:-1:0:0:0:46
```

#### BND
```
GT:GL:GQ:FT:RCL:RC:RCR:CN:DR:DV:RR:RV
0/0:0,-1.20412,-24:12:LowQual:0:0:0:-1:4:0:0:0
1/1:-6.27102,-1.2772,0:13:LowQual:0:0:0:-1:0:6:0:0
0/1:-122.452,0,-512.463:10000:PASS:0:0:0:-1:94:50:0:0

0/0:0,-2.63875,-172.926:26:PASS:0:0:0:-1:40:12:0:0 ?
```

#### INV
```
GT:GL:GQ:FT:RCL:RC:RCR:CN:DR:DV:RR:RV
0/0:0,-19.868,-396:10000:PASS:0:9365007:0:-1:66:0:0:0
0/1:-3.0633,0,-136.851:31:PASS:2030318:4077631:2024832:2:26:10:0:0
1/1:-304.072,-21.9617,0:10000:PASS:918190:1936836:913509:2:1:0:1:86
```

#### DUP
```
GT:GL:GQ:FT:RCL:RC:RCR:CN:DR:DV:RR:RV
1/1:-18,-0.903089,0:10:LowQual:20:35:16:2:0:3:0:0
0/0:0,-14.4494,-287.7:144:PASS:44:135:76:2:48:0:0:0
```


