## Assembly genome using nanopore reads


### install tools

```
$ conda install -c bioconda minimap2

$ conda install -c bioconda miniasm

$ conda install -c bioconda canu

$ conda install -c bioconda racon

$ conda install -c bioconda pilon 

$ conda install -c bioconda quast
```


### download data
```
$ source activate evolution
$ parallel-fastq-dump --sra-id SRR1219899 --threads 4 --outdir out/ --split-files --gzip
```


### dump the reads
 PACBIO_SMRT (Sequel)
```
$ fastq-dump --split-files ERR2173371.sra  -I

miniasmRead 613080 spots for ERR2173371.sra
Written 613080 spots for ERR2173371.sra
```

OXFORD_NANOPORE (MinION)
```
$ fastq-dump --split-files -I ERR2173373.sra 
Read 300071 spots for ERR2173373.sra
Written 300071 spots for ERR2173373.sra
```

 ILLUMINA (Illumina MiSeq)
```
$ fastq-dump --split-files -I ERR2173372.sra
Read 16841951 spots for ERR2173372.sra
Written 16841951 spots for ERR2173372.sra
```


### Overlaps were generated using [minimap](https://github.com/lh3/minimap)
```
$ minimap -Sw5 -L100 -m0 -t 20 ERR2173373_1.fastq ERR2173373_1.fastq | gzip -1 > ERR2173373.paf.gz
```

outfile:
```
[M::mm_idx_gen::75.212*1.83] collected minimizers
[M::mm_idx_gen::93.158*2.80] sorted minimizers
[M::main::93.158*2.80] loaded/built the index for 300071 target sequence(s)
[M::main] max occurrences of a minimizer to consider: 181
ERR2173373.1.1  3478    84      1892    +       ERR2173373.222906.1     22037   7679    9531    617     1852    255     cm:i:87
ERR2173373.1.1  3478    67      1803    +       ERR2173373.197127.1     30418   15639   17411   561     1772    255     cm:i:82
ERR2173373.1.1  3478    80      1837    +       ERR2173373.182651.1     19304   7881    9657    565     1776    255     cm:i:78

```


### Genome assembly graphs (GFA) were generated using [miniasm](https://github.com/lh3/miniasm)
```
$ pigz -dc -p 20 ERR2173373.paf.gz > ERR2173373.paf
$ miniasm -f ERR2173373_1.fastq ERR2173373.paf > ERR2173373.gfa

[M::main] ===> Step 1: reading read mappings <===
[M::ma_hit_read::61.250*1.00] read 39064189 hits; stored 70128835 hits and 219878 sequences (3181461046 bp)
[M::main] ===> Step 2: 1-pass (crude) read selection <===
[M::ma_hit_sub::68.420*1.00] 184789 query sequences remain after sub
[M::ma_hit_cut::69.334*1.00] 40191250 hits remain after cut
[M::ma_hit_flt::69.935*1.00] 30792089 hits remain after filtering; crude coverage after filtering: 95.15
[M::main] ===> Step 3: 2-pass (fine) read selection <===
[M::ma_hit_sub::70.462*1.00] 181701 query sequences remain after sub
[M::ma_hit_cut::70.966*1.00] 23483797 hits remain after cut
[M::ma_hit_contained::71.424*1.00] 13315 sequences and 104973 hits remain after containment removal
[M::main] ===> Step 4: graph cleaning <===
[M::ma_sg_gen] read 99588 arcs
[M::main] ===> Step 4.1: transitive reduction <===
[M::asg_arc_del_trans] transitively reduced 67688 arcs
[M::asg_arc_del_multi] removed 613 multi-arcs
[M::asg_arc_del_asymm] removed 1617 asymmetric arcs
[M::main] ===> Step 4.2: initial tip cutting and bubble popping <===
[M::asg_cut_tip] cut 247 tips
[M::asg_pop_bubble] popped 484 bubbles and trimmed 3 tips
[M::main] ===> Step 4.3: cutting short overlaps (3 rounds in total) <===
[M::asg_arc_del_multi] removed 0 multi-arcs
[M::asg_arc_del_asymm] removed 211 asymmetric arcs
[M::asg_arc_del_short] removed 1207 short overlaps
[M::asg_cut_tip] cut 85 tips
[M::asg_pop_bubble] popped 87 bubbles and trimmed 2 tips
[M::asg_arc_del_multi] removed 0 multi-arcs
[M::asg_arc_del_asymm] removed 29 asymmetric arcs
[M::asg_arc_del_short] removed 35 short overlaps
[M::asg_cut_tip] cut 10 tips
[M::asg_pop_bubble] popped 4 bubbles and trimmed 1 tips
[M::asg_arc_del_multi] removed 0 multi-arcs
[M::asg_arc_del_asymm] removed 21 asymmetric arcs
[M::asg_arc_del_short] removed 27 short overlaps
[M::asg_cut_tip] cut 11 tips
[M::asg_pop_bubble] popped 3 bubbles and trimmed 1 tips
[M::main] ===> Step 4.4: removing short internal sequences and bi-loops <===
[M::asg_cut_internal] cut 13 internal sequences
[M::asg_cut_biloop] cut 36 small bi-loops
[M::asg_cut_tip] cut 2 tips
[M::asg_pop_bubble] popped 0 bubbles and trimmed 0 tips
[M::main] ===> Step 4.5: aggressively cutting short overlaps <===
[M::asg_arc_del_multi] removed 0 multi-arcs
[M::asg_arc_del_asymm] removed 21 asymmetric arcs
[M::asg_arc_del_short] removed 23 short overlaps
[M::asg_cut_tip] cut 11 tips
[M::asg_pop_bubble] popped 2 bubbles and trimmed 1 tips
[M::main] ===> Step 5: generating unitigs <===
[M::main] Version: 0.2-r128
[M::main] CMD: miniasm -f ERR2173373_1.fastq ERR2173373.paf.gz
[M::main] Real time: 77.200 sec; CPU: 77.192 sec

```

output file:
```
S       utg000001l      GAACCACTTGTGTTTGAACATGATCGCACTTGGCACGGATAGATCTACTTGATCGGCATTTCCTTGATGCATAAATCTATCACTTTGATACGCTTTCTAATTTCGAACTATATGTGTCAGCCAGA
a       utg000001l      0       ERR2173373.20921.1:65-42608     +       13495
a       utg000001l      13495   ERR2173373.3199.1:33-31230      -       4731
a       utg000001l      18226   ERR2173373.27281.1:86-38787     -       11935
a       utg000001l      30161   ERR2173373.151774.1:34-38124    +       13046
a       utg000001l      43207   ERR2173373.35647.1:125-30588    -       5713
```




### Three rounds of consensus correction was performed using [racon](https://github.com/isovic/racon)

```

$ python gfa2fasta.py ERR2173373.gfa ERR2173373.gfa.fasta
$ minimap -t 20 ERR2173373.gfa.fasta ERR2173373_1.fastq  > ERR2173373_realigned.paf
$ racon ERR2173373_1.fastq ERR2173373_realigned.paf  ERR2173373.gfa.fasta > ERR2173373.racon.fasta
$ minimap -t 20 ERR2173373.racon.fasta ERR2173373_1.fastq  > ERR2173373_realigned2.paf
$ racon -t 20 ERR2173373_1.fastq ERR2173373_realigned2.paf  ERR2173373.racon.fasta > ERR2173373.racon2.fasta
$ minimap -t 20 ERR2173373.racon2.fasta ERR2173373_1.fastq  > ERR2173373_realigned3.paf
$ racon -t 20 ERR2173373_1.fastq ERR2173373_realigned3.paf  ERR2173373.racon2.fasta > ERR2173373.racon3.fasta

```


gfa2fasta.py
```python
def gfa2fa(gfa_file, fa_file):
    in_h = open(gfa_file, 'r')
    out_h = open(fa_file, 'w')
    for line in in_h:
        lines = line.strip().split('\t')
        sym = lines[0]
        if sym == 'S':
            desc = lines[1]
            seq = lines[2]
            out_h.write('>%s\n%s\n' % (desc, seq))
    in_h.close()
    out_h.close()
    
gfa2fa('/home/wzk/Project/AtGenome/ERR2173373.gfa','/home/wzk/Project/AtGenome/ERR2173373.gfa.fasta')
```


### trim low quality reads for Illumina reads
```
$ grep -c GATCGGAAGAGCACACGTCTGAACTCCAGTCAC ERR2173372_1.fastq
771929

$ grep -c AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT ERR2173372_2.fastq
445316

$ wc -l ERR2173372_1.fastq
67367804 ERR2173372_1.fastq

$ cat /home/Adapters/DNA.fa
>mRNA-p5
AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT
>mRNA-p5-as
AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT
>mRNA-p7
GATCGGAAGAGCACACGTCTGAACTCCAGTCAC
>mRNA-PCR
ATCTCGTATGCCGTCTTCTGCTTG
>mRNA-p7as
GTGACTGGAGTTCAGACGTGTGCTCTTCCGATC
>miRNA-PCR-as
CAAGCAGAAGACGGCATACGAGAT

$ java -jar ~/anaconda3/envs/evolution/bin/trimmomatic-0.36.jar  PE -threads 20  -phred33  ERR2173372_1.fastq ERR2173372_2.fastq ERR2173372_clean_pair_1.fastq ERR2173372_clean_unpair_1.fastq ERR2173372_clean_pair_2.fastq ERR2173372_clean_unpair_2.fastq ILLUMINACLIP:/home/Adapters/DNA.fa:2:30:12 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:10  MINLEN:50

```

#### mapping Illumina reads to assembly genome
```
$ mkdir bwa_index
$ cp ERR2173373.racon3.fasta bwa_index
$ cd bwa_index/ &&  bwa index ERR2173373.racon3.fasta
$ bwa mem -t 30 bwa_index/ERR2173373.racon3.fasta ERR2173372_clean_pair_1.fastq  ERR2173372_clean_pair_2.fastq > mapping/ERR2173372.sam

[mem_sam_pe] paired reads have different names: "ERR2173372.1.1", "ERR2173372.1.2"

$ head ERR2173372_clean_pair_1.fastq
@ERR2173372.1.1 MISEQ:13:000000000-AE4FK:1:1101:15829:1331 length=250
AACCAAGATCTAGAGTCTTAATATTGTTCATCGGGTTTTGCTTTTTGCAATTTTAGCCGGCCCCAACTATGAATCAATAAGCAGCAAAATTAAGTGCAACAAAAAAAACAAATTTCCAAAATAAAAAAAATTT
+ERR2173372.1.1 MISEQ:13:000000000-AE4FK:1:1101:15829:1331 length=250
AA@AA?1FFBF3B31B1FD3E3333AAF3D33100AAEA0111AA1/1212122201A////A/A//0B2FE221@1@2111100B0F011111@21B110?0G//>//F<B1B1222B</11111F//<@1F
@ERR2173372.2.1 MISEQ:13:000000000-AE4FK:1:1101:15542:1332 length=250
TGTGTCTTCTAACAAGGAAACACTACTTTGGCTTATAAGATGCGGTTGCGGTTTAAGTTCTTATACTCAATCATACACATGAGATCAAGTCATATTCGACTCCAAAACAGTAACCAACCTTCTTCTTACTTCTCAAAGCTTTCATGGTGTAGCGAAAGTCCATATGAGTCTTTGGCTTTCTGTCTTTTAACAAGGATACAATTCTTAGGCCTTTCAATCCAGGTCGGGGTTTAAGTCGTATACTCAATCA
+ERR2173372.2.1 MISEQ:13:000000000-AE4FK:1:1101:15542:1332 length=250
CCCBCFFFFFFFGGGGGGGGGGHHHHHHHHHHHHHHHHHGHHHGGGGGHGGFGGHHHHHHHHGHHHHHHHHHHGHHHHHHHHHHHHHHGHHHHHHGHHHGGGHHHHHHHCGHHHHHHGGHHHHHHHH4BGHHHHHHHHHHHHHHHHH?FGHHH@GGGGHHHHGHHHFHGHHHHHHHHHHBHHHHHH1GHH1FGHHGBD1G0=0=GGHBGH0C0D0=000;0:/=0----AC.C00;9.;F/B0000:00;
@ERR2173372.3.1 MISEQ:13:000000000-AE4FK:1:1101:15643:1333 length=250
GTTTATACATATAGAATCAAGTGTACATTAGGGATCAAAAGGTATCGTTTTTAGAGTTATAGTTGTAATTAAGTTTTAAACCGAGTGAAATAACTCTGCCGACACAACGACAAGATAAAATGTAATAAACTCTTCTTCACTTTCCCATCAAGATTATTACATTAGCTTTCAAGTGCTAGTTTCATTATATTATATGTATATACACACATGCGCACACATACACGTTGATGGGCTATGATCAACAATGAGA
(evolution) wzk@ubuntu 20:49:09 ^_^ /home/wzk/Project/AtGenome 
$ head ERR2173372_clean_pair_2.fastq
@ERR2173372.1.2 MISEQ:13:000000000-AE4FK:1:1101:15829:1331 length=250
CTTGCATAAAAACTGACACAGTTCTAATTGTACCACTGAAGTTGTTTGCATTACACGTAGTAAAAGATTATTTATTGGAATACAAATACTCCTGAAAATTGGAGAGACAAACCGGACAAAATCCAGTCATTTATATCTGTCGATGGAAACAAAATCCATTTCATAAAAATACGAAACTGTAATTGTAAAAAAAAAAATTAAAATTAAAAT
+ERR2173372.1.2 MISEQ:13:000000000-AE4FK:1:1101:15829:1331 length=250
>>A?AF3DDDDGEEG1GGGFGGGFGBF3GFDEGHGCH1AFGEAEDEGB1FA2F111BAAA/2FFFFFGFFDHHFH2FGFFFFHGFFHGHHGFGB1F1FHF1FEB1ECGFGHHGGECEEFHHFHHHFF>BGHFGFHGHEHGBFHGBEGFHFF/CHBCGFDD>GFHFHEFHHHDG/?ECHGHHFHFFGGBFHFGC-CC@.:00000/:;0CC
@ERR2173372.2.2 MISEQ:13:000000000-AE4FK:1:1101:15542:1332 length=250
GAACTTAAACTACTACTCGATGTTATAAGCCTAAGTAATATTTCCTTCTTAGAAGACACAAAGCCAAAGACTCATATGGACTTTGGCTACACCATGAAAGCTTTGAGAAGCAAGAAGAAGGTTGGTTAGTGTTTTGGAGTCGAATATGACTTGATCTCATGTGTATGATTGAGTATAAGAACTTAAACCGCAACAGGATCTTATAAGCGAAAGTAGTGTTTCCTTGTTAGCAGCCACAA
+ERR2173372.2.2 MISEQ:13:000000000-AE4FK:1:1101:15542:1332 length=250
>AABCFFFFFFGGGGGGGGGGHHHHHHHHGGHHHHFHHHHHHHHHHHHHHHHHHHHHHHHGHEHHHHHHHHGHHHHHHHHHHHH3FHGHGHFHHHHHHHGHHHHGFGHGHHHHHGHHHEHFBDGEEGHCHE4FGFHGHHFGEFEHGGHHHHHGEGHGHHHHHHGFDHHHHGBHGHHHGHGGFEHHGBG0>/@CC0>.0FGFFHFF0<0-.<@D0:00/C0/<0CFHHBGB0<0/.9:F?
@ERR2173372.3.2 MISEQ:13:000000000-AE4FK:1:1101:15643:1333 length=250
CTTAATGGTGCATTCTTCACCTATTCTGGTGCTGGACCAGCTAAATCATCAAGCTATTCAAAAGCTTCGAGTCTAGCCGCGAGACCGTCCTCTCATGTTGGTGAGATAACTATAGCCTCGGGTGCACTCAGCTGCAAAAGGGGTTCTCATTGTTGATCATAGCCCATCAACGTGTATGTGTGCGCATGTGTGTATATACATATAATATAATGAAACTAGCACTTGAAAGCTAATGTAATAATCTTGATG


```


### allign illumina read to contig
```

$ sed 's/\.1 / /g' ERR2173372_clean_pair_1.fastq > ERR2173372_clean_paired_1.fastq
$ sed 's/\.2 / /g' ERR2173372_clean_pair_2.fastq > ERR2173372_clean_paired_2.fastq
$ bwa mem -t 30 bwa_index/ERR2173373.racon3.fasta ERR2173372_clean_paired_1.fastq ERR2173372_clean_paired_2.fastq  > mapping/ERR2173372.sam
$ samtools view -h -b -S mapping/ERR2173372.sam > mapping/ERR2173372.bam

```


```
$ sed -n '1263779, 1263785p' ERR2173372-1.sam
ERR2173372.630998   163 utg000009l_C:1.000000_C:1.000000_C:1.000000 2012699 60  205M1I18M   =   2012698 223 TCAATACATAAAATCTCATCAGATAAATTGCTTTTAAGTTTTTAACATATGAACACTTTGACTATAACCAAACAAGAACATGATAAAGAGAGAAAGTGTCTCTAAATATGATCCTAATCAAATTCCAAGGTGATGTTTTGAAGTCTTTTCCAAAGACTGGTCGTCTTATCCAACACTAGCACATGCTCTTATTTCCCTACCATTTCTTTTAAATTCAAAAGCTA    CCCDDFFFFFFFGGGGGGGGGGHHHHHHHHHHHHHHHHGHHHGHHHHHHHHHHHHHHHHHHIIHHHHHHHHHHHHHHHHHHHHHHHHHHHHGGHHHHHHHGHHHHHHHHHHHHHHHHHHHHHHHFHHGHGDGFHFGBHHHGHHHHHHHHHHHHHHHHHGHHGGGGHGHHHHHGHGGHGHHHHHHHHHGHHGHHHHFHHHGHHHHHHHHGGGGHHHHGGHFCHHG    NM:i:1  MD:Z:223    AS:i:216    XS:i:19
ERR2173372.630999   83  utg000[M::process] read 1254902 sequences (300000238 bp)...
[M::mem_pestat] # candidate unique pairs for (FF, FR, RF, RR): (104, 401405, 44, 4)
[M::mem_pestat] analyzing insert size distribution for orientation FF...
[M::mem_pestat] (25, 50, 75) percentile: (141, 310, 445)
[M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 1053)
[M::mem_pestat] mean and std.dev: (297.50, 168.04)
```


### correct the header for illumina reads
```
$ fastq-dump --defline-qual '+' --defline-seq '@$ac-$si/$ri length=$rl ' --split-3 ERR2173372.sra
```

run downstream pipeline
```
$ java -jar ~/anaconda3/envs/evolution/bin/trimmomatic-0.36.jar  PE -threads 20  -phred33  ERR2173372_1.fastq ERR2173372_2.fastq ERR2173372_clean_pair_1.fastq ERR2173372_clean_unpair_1.fastq ERR2173372_clean_pair_2.fastq ERR2173372_clean_unpair_2.fastq ILLUMINACLIP:/home/Adapters/DNA.fa:2:30:12 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:10  MINLEN:50
$ bwa mem -t 30 bwa_index/ERR2173373.racon3.fasta ERR2173372_clean_pair_1.fastq ERR2173372_clean_pair_2.fastq  > mapping/ERR2173372.sam
$ samtools view -h -b -S mapping/ERR2173372.sam > mapping/ERR2173372.bam
$ samtools sort mapping/ERR2173372.bam > mapping/ERR2173372_sorted.bam
$ samtools index mapping/ERR2173372_sorted.bam

```


#### align illumina read to assembly genome using bowtie2
```
$ bowtie2-build  bwa_index/ERR2173373.racon3.fasta bwa_index/ERR2173373.racon3
$ bowtie2 -x bwa_index/ERR2173373.racon3 -1 ERR2173372_clean_pair_1.fastq -2 ERR2173372_clean_pair_2.fastq -S bowtie2_mapping/ERR2173372.sam --threads 30


$ samtools view -h -b -S bowtie2_mapping/ERR2173372.sam > bowtie2_mapping/ERR2173372.bam && \
samtools sort bowtie2_mapping/ERR2173372.bam > bowtie2_mapping/ERR2173372_sorted.bam && \
samtools index bowtie2_mapping/ERR2173372_sorted.bam && \
pilon --genome ERR2173373.racon3.fasta --frags bowtie2_mapping/ERR2173372_sorted.bam  --output  ERR2173373 --outdir pilon --threads 25 

```





### Polish the assembly genome using [pilon](https://github.com/broadinstitute/pilon/wiki/Requirements-&-Usage)
```
$ pilon --genome ERR2173373.racon3.fasta --frags mapping/ERR2173372_sorted.bam  --output  ERR2173373 --outdir pilon --threads 25 --vcf --tracks --changes --fix indels,local,breaks,novel
Pilon version 1.22 Wed Mar 15 16:38:30 2017 -0400
Warning: experimental fix option breaks
Warning: experimental fix option novel
Genome: ERR2173373.racon3.fasta
Exception in thread "main" java.lang.reflect.InvocationTargetException
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:498)
    at com.simontuffs.onejar.Boot.run(Boot.java:340)
    at com.simontuffs.onejar.Boot.main(Boot.java:166)
Caused by: java.lang.OutOfMemoryError: Java heap space
    at org.broadinstitute.pilon.GenomeRegion.<init>(GenomeRegion.scala:60)
    at org.broadinstitute.pilon.GenomeFile$$anonfun$contigRegions$1.apply(GenomeFile.scala:72)
    at org.broadinstitute.pilon.GenomeFile$$anonfun$contigRegions$1.apply(GenomeFile.scala:72)
    at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
    at scala.collection.TraversableLike$$anonfun$map$1.apply(TraversableLike.scala:234)
    at scala.collection.immutable.Range.foreach(Range.scala:160)
    at scala.collection.TraversableLike$class.map(TraversableLike.scala:234)
    at scala.collection.AbstractTraversable.map(Traversable.scala:104)
    at org.broadinstitute.pilon.GenomeFile.contigRegions(GenomeFile.scala:72)
    at org.broadinstitute.pilon.GenomeFile$$anonfun$2.apply(GenomeFile.scala:52)
    at org.broadinstitute.pilon.GenomeFile$$anonfun$2.apply(GenomeFile.scala:52)
    at scala.collection.immutable.List.map(List.scala:277)
    at org.broadinstitute.pilon.GenomeFile.<init>(GenomeFile.scala:52)
    at org.broadinstitute.pilon.Pilon$.main(Pilon.scala:98)
    at org.broadinstitute.pilon.Pilon.main(Pilon.scala)
    ... 6 more

```



issues:
```
https://github.com/broadinstitute/pilon/issues/12
```


### polish the assembly genome by pilon 
```

$ java -Xmx250g  -jar /home/wzk/anaconda3/envs/evolution/bin/pilon-1.22.jar  --genome ERR2173373.racon3.fasta --frags mapping/ERR2173372_sorted.bam  --output  ERR2173373 --outdir pilon --threads 25
```







