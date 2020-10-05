## STAR manual

### build index of STAR
```
$ mkdir /home/wzk/database/hg38/hg38_STAR_reference
$ /home/wzk/anaconda3/bin/tools/STAR --runMode genomeGenerate --runThreadN 20 --genomeFastaFiles /home/wzk/database/hg38/hg38.fa  --genomeDir /home/wzk/database/hg38/hg38_STAR_reference --sjdbGTFfile /home/wzk/database/hg38/hg38_ref.gtf --sjdbOverhang 149

Nov 07 00:44:45 ..... started STAR run
Nov 07 00:44:45 ... starting to generate Genome files
Nov 07 00:45:38 ... starting to sort Suffix Array. This may take a long time...
Nov 07 00:45:53 ... sorting Suffix Array chunks and saving them to disk...
Nov 07 01:10:21 ... loading chunks from disk, packing SA...
Nov 07 01:13:14 ... finished generating suffix array
Nov 07 01:13:14 ... generating Suffix Array index
Nov 07 01:16:17 ... completed Suffix Array index
Nov 07 01:16:17 ..... processing annotations GTF
Nov 07 01:16:22 ..... inserting junctions into the genome indices
Nov 07 01:19:57 ... writing Genome to disk ...
Nov 07 01:19:59 ... writing Suffix Array to disk ...
Nov 07 01:20:16 ... writing SAindex to disk
Nov 07 01:20:18 ..... finished successfully

```

--sjdbGTFfile should be a .gtf file, not .gff


### The result after get index
```
- -rw-r--r-- 1 1.2K May  9 09:29 chrLength.txt
- -rw-r--r-- 1 3.1K May  9 09:29 chrNameLength.txt
- -rw-r--r-- 1 1.9K May  9 09:29 chrName.txt
- -rw-r--r-- 1 2.1K May  9 09:29 chrStart.txt
- -rw-r--r-- 1  14M May  9 09:49 exonGeTrInfo.tab
- -rw-r--r-- 1 5.7M May  9 09:49 exonInfo.tab
- -rw-r--r-- 1 1.2M May  9 09:49 geneInfo.tab
- -rw-r--r-- 1 3.0G May  9 09:51 Genome
- -rw-r--r-- 1  613 May  9 09:29 genomeParameters.txt
- -rw-r--r-- 1  24G May  9 09:51 SA
- -rw-r--r-- 1 1.5G May  9 09:51 SAindex
- -rw-r--r-- 1 6.5M May  9 09:49 sjdbInfo.txt
- -rw-r--r-- 1 5.1M May  9 09:49 sjdbList.fromGTF.out.tab
- -rw-r--r-- 1 5.1M May  9 09:49 sjdbList.out.tab
- -rw-r--r-- 1 5.3M May  9 09:49 transcriptInfo.tab

```

### run STAR
```
~/bin/STAR-2.5.2b --runThreadN 20 --genomeDir /home/wzk/reference/  --readFilesIn MCF-7-2835.R1.fq  MCF-7-2835.R2.fq  --quantMode  TranscriptomeSAM --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /home/wzk/test_STAR/D14E509  --outFilterType BySJout --outFilterMultimapNmax 20 --alignSJoverhangMin 8 --alignSJDBoverhangMin 1 --outFilterMismatchNmax 999 --outFilterMismatchNoverLmax 0.04 --alignIntronMin 20 --alignIntronMax 1000000 --alignMatesGapMax 1000000  --chimSegmentMin 20 

Tue May  9 04:42:17 EDT 2017
May 09 04:42:17 ..... started STAR run
May 09 04:42:17 ..... loading genome
May 09 04:44:18 ..... started mapping
May 09 04:55:09 ..... started sorting BAM
May 09 04:56:45 ..... finished successfully
Tue May  9 04:56:49 EDT 2017
```

or

```
mkdir MCF-7-2835
~/bin/STAR-2.5.2b --runThreadN 25 --genomeDir /home/wzk/reference/  --readFilesIn raw/MCF-7-2835.R1.fq  raw/MCF-7-2835.R2.fq  --quantMode  TranscriptomeSAM --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /home/wzk/test_rMATs/mapping/MCF-7-2835/  --outFilterType BySJout
```

--readFilesIn 输出的原始测序数据

--outSAMtype BAM SortedByCoordinate 输出格式为BAM并排序

--chimSegmentMin20 输出融合转录本，20代表比对的最短的碱基数目

--outFileNamePrefix  输出文件的前缀

--quantMode TranscriptomeSAM  转录本定量





output files:
```
-rw-r--r-- 1 3.0G May  9 04:56 D14E509Aligned.sortedByCoord.out.bam
-rw-r--r-- 1 2.4G May  9 04:55 D14E509Aligned.toTranscriptome.out.bam
-rw-r--r-- 1  46M May  9 04:55 D14E509Chimeric.out.junction
-rw-r--r-- 1 357M May  9 04:55 D14E509Chimeric.out.sam
-rw-r--r-- 1 1.9K May  9 04:56 D14E509Log.final.out
-rw-r--r-- 1  33K May  9 04:56 D14E509Log.out
-rw-r--r-- 1 1.6K May  9 04:56 D14E509Log.progress.out
-rw-r--r-- 1 7.9M May  9 04:56 D14E509SJ.out.tab
lrwxrwxrwx 1   50 May  9 04:40 MCF-7-2835.R1.fq -> /home/Project/KC2017-A05/mRNA/raw/MCF-7-2835.R1.fq
lrwxrwxrwx 1   50 May  9 04:40 MCF-7-2835.R2.fq -> /home/Project/KC2017-A05/mRNA/raw/MCF-7-2835.R2.fq
-rw------- 1  258 May  9 04:56 nohup.out
-rwxr-xr-x 1  499 May  9 04:41 work.sh
```


Chimeric.out.junction  融合转录本

Aligned.sortedByCoord.out.bam  比对输出

Aligned.toTranscriptome.out.bam 转录本比对输出

SJ.out.tab 可变剪切结果输出

