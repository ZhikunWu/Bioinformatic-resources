## [rmats](http://rnaseq-mats.sourceforge.net)

Multivariate Analysis of Transcript Splicing (MATS)

### [rmats manual](http://rnaseq-mats.sourceforge.net/rmats4.0.1/user_guide.htm)

### install rmats
```
$ conda install -c bioconda rmats 
```


### run rmats

b1.txt file example
```
$ cat b1.txt
PC3Ebam/PC3E-1.bam,PC3Ebam/PC3E-2.bam,PC3Ebam/PC3E-3.bam
```


rmats v2:
```
python rmats.py --b1 b1.txt --b2 b2.txt --gtf Homo_sapiens.GRCh37.75.gtf --od output_b2 -t paired --nthread 6 --readLength 101 --anchorLength 1 --tstat 6
```


run rmats v4:
```
$ python /home/wzk/anaconda3/envs/kcmRNA/bin/rMATS.4.0.1/rMATS-turbo-Linux-UCS4/rmats.py --b1 b1.txt --b2 b2.txt --gtf  /home/wzk/database/mouse/Mus_musculus.GRCm38.87.gtf --od outdir -t paired --nthread 20  --readLength 150  --tstat 20 --cstat  0.1
There are 49671 distinct gene ID in the gtf file
There are 123063 distinct transcript ID in the gtf file
There are 31477 one-transcript genes in the gtf file
There are 745096 exons in the gtf file
There are 22970 one-exon transcripts in the gtf file
There are 19002 one-transcript genes with only one exon in the transcript
Average number of transcripts per gene is 2.477562
Average number of exons per transcript is 6.054590
Average number of exons per transcript excluding one-exon tx is 7.214550
Average number of gene per geneGroup is 7.014025

==========
Done processing each gene from dictionary to compile AS events
Found 38442 exon skipping events
Found 4921 exon MX events
Found 7468 alt SS events
There are 4649 alt 3 SS events and 2819 alt 5 SS events.
Found 3441 RI events
==========

Running the statistical part.
The statistical part is done.
Done.
```

it just need 10 m


splicing events summary:
```
======================================================================
EventType   NumEvents.JC.only   SigEvents.JC.only   NumEvents.JC+readsOnTarget  SigEvents.JC+readsOnTarget
======================================================================
SE  56281   9 (2:7) 56424   10 (1:9)
MXE 11492   12 (6:6)    11545   11 (5:6)
A5SS    21043   13 (5:8)    21056   13 (5:8)
A3SS    34187   12 (7:5)    34199   12 (7:5)
RI  6125    2 (1:1) 6170    1 (0:1)
```

### rmats plot
```
$ rmats2sashimiplot --b1 /home/wzk/rmats_test/mapping/C007_620_1/Aligned.sortedByCoord.out.bam  --b2 /home/wzk/rmats_test/mapping/C007_620_ON_1/Aligned.sortedByCoord.out.bam -c 10:-:75233969:75236029:/home/wzk/rmats_test/Homo_sapiens.GRCh38_with_GENE_anno.gff --l1 control --l2 treat --exon_s 1 --intron_s 1 -o /home/wzk/rmats_test/coordinate_output
```
