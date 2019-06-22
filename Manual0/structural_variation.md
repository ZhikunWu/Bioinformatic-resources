## Structural variation

### align with bwa
```
$ bwa mem -aM -R "@RG\tID:DR1\tSM:DR1\tPL:ILLUMINA\tCN:Seqhealth\tLB:DR1" /home/genome/Bacillus_virus/GCF_000837685.1_ViralProj14034_genomic.fa  /home/Project/KC2018-C073/20180712analysis/clean/DR1.clean.paired.R1.fq.gz   /home/Project/KC2018-C073/20180712analysis/clean/DR1.clean.paired.R2.fq.gz | samtools view -bSh -o  DR1.bam

$ bwa mem -aM -R "@RG\tID:DR2\tSM:DR2\tPL:ILLUMINA\tCN:Seqhealth\tLB:DR2" /home/genome/Bacillus_virus/GCF_000837685.1_ViralProj14034_genomic.fa /home/Project/KC2018-C073/20180712analysis/clean/DR2.clean.paired.R1.fq.gz /home/Project/KC2018-C073/20180712analysis/clean/DR2.clean.paired.R2.fq.gz | samtools view -bSh -o DR2.bam
```

### sam to bam
```
$ samtools sort  -@ 10 -m 2G DR1.bam -o DR1.sort.bam

$ samtools sort  -@ 10 -m 2G DR2.bam -o DR2.sort.bam
```

### markduplicate  and sort
```
$ java -Xmx20g -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar MarkDuplicates INPUT=DR1.sort.bam OUTPUT=DR1.sort.markdup.bam METRICS_FILE=marked_dup_metrics.txt REMOVE_DUPLICATES=false ASSUME_SORTED=true

$ java -Xmx20g -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar MarkDuplicates INPUT=DR2.sort.bam OUTPUT=DR2.sort.markdup.bam METRICS_FILE=marked_dup_metrics.txt REMOVE_DUPLICATES=false ASSUME_SORTED=true
```

### index bam
```
$ samtools index  DR1.sort.markdup.bam
```

## Call SV

### call SV using delly

```
$ export OMP_NUM_THREADS=1 && delly call --type DEL --genome /home/genome/Bacillus_virus/GCF_000837685.1_ViralProj14034_genomic.fa --outfile DR1.DEL.vcf DR1.sort.markdup.bam
```



### call SV using  breakdancer

```
$ bam2cfg.pl -v 3 -q 20 -c 4 -g -h DR2.sort.markdup.bam   > DR2.bamcfg
[Fri Jul 20 03:24:10 2018 /home/wzk/anaconda3/envs/evolution/bin/bam2cfg.pl] Processing bam: DR2.sort.markdup.bam
[Fri Jul 20 03:24:11 2018 /home/wzk/anaconda3/envs/evolution/bin/bam2cfg.pl] selected_libs is : 1
[Fri Jul 20 03:24:11 2018 /home/wzk/anaconda3/envs/evolution/bin/bam2cfg.pl] Closing BAM file
[Fri Jul 20 03:24:11 2018 /home/wzk/anaconda3/envs/evolution/bin/bam2cfg.pl] Send TERM signal for 70943
[Fri Jul 20 03:24:13 2018 /home/wzk/anaconda3/envs/evolution/bin/bam2cfg.pl] samtools pid process 70943 is still there...
[Fri Jul 20 03:24:13 2018 /home/wzk/anaconda3/envs/evolution/bin/bam2cfg.pl] invoking kill -9 on 70943 ...
[Fri Jul 20 03:24:13 2018 /home/wzk/anaconda3/envs/evolution/bin/bam2cfg.pl] Closing samtools process : 70943

```

```
$  breakdancer-max  -q 20 -d /home/wzk/SV_CNV/DR2/DR2 DR2.bamcfg > DR1.raw.ctx
```


### call SV using cnvnator

```
/home/zyb/soft/CNVnator-0.3.3/cnvnator -root /home/wzk/SV_CNV/DR1/DR1  -genome /home/genome/Bacillus_virus/GCF_000837685.1_ViralProj14034_genomic.fa  -tree ../DR1.sort.markdup.bam  

/home/zyb/soft/CNVnator-0.3.3/cnvnator -root /home/wzk/SV_CNV/DR1/DR1  -genome /home/genome/Bacillus_virus/GCF_000837685.1_ViralProj14034_genomic.fa  -his 100 -d /home/wzk/SV_CNV/DR1

/home/zyb/soft/CNVnator-0.3.3/cnvnator -root /home/wzk/SV_CNV/DR1/DR1  -stat 100

/home/zyb/soft/CNVnator-0.3.3/cnvnator -root /home/wzk/SV_CNV/DR1/DR1   -partition 100

/home/zyb/soft/CNVnator-0.3.3/cnvnator -root /home/wzk/SV_CNV/DR1/DR1  -call 100 > DR1.raw


perl /home/zyb/soft/CNVnator-0.3.3/cnvnator2VCF.pl DR1.raw > DR1.vcf
```
