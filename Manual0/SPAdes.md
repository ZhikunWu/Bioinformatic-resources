## [SPAdes](https://github.com/ablab/spades): Genome Assembler

### [SPAdes manual](http://spades.bioinf.spbau.ru/release3.11.1/manual.html)

### Install SPAdes
```
$ conda install -c bioconda spades
```
or

```
$ wget http://cab.spbu.ru/files/release3.11.1/SPAdes-3.11.1-Linux.tar.gz
$ tar -zxf SPAdes-3.11.1-Linux.tar.gz
$ cd SPAdes-3.11.1-Linux/
```


### Assemble the Illumina data with SPAdes
```
$ spades.py --careful --pe1-1 Kp2146_paired_1.fastq.gz --pe1-2 Kp2146_paired_2.fastq.gz -o spades -t 16

 * Corrected reads are in /home/wzk/Project/npScarf/spades/corrected/
 * Assembled contigs are in /home/wzk/Project/npScarf/spades/contigs.fasta
 * Assembled scaffolds are in /home/wzk/Project/npScarf/spades/scaffolds.fasta
 * Assembly graph is in /home/wzk/Project/npScarf/spades/assembly_graph.fastg
 * Assembly graph in GFA format is in /home/wzk/Project/npScarf/spades/assembly_graph_with_scaffolds.gfa
 * Paths in the assembly graph corresponding to the contigs are in /home/wzk/Project/npScarf/spades/contigs.paths
 * Paths in the assembly graph corresponding to the scaffolds are in /home/wzk/Project/npScarf/spades/scaffolds.paths

======= SPAdes pipeline finished.
```

output files:
```
-rw-r--r-- 1  12M Oct 24 21:49 assembly_graph.fastg
-rw-r--r-- 1 5.6M Oct 24 21:49 assembly_graph_with_scaffolds.gfa
-rw-r--r-- 1 5.6M Oct 24 21:49 before_rr.fasta
-rw-r--r-- 1 5.6M Oct 24 21:52 contigs.fasta
-rw-r--r-- 1  22K Oct 24 21:49 contigs.paths
drwxr-xr-x 3 4.0K Oct 24 21:30 corrected
-rw-r--r-- 1   64 Oct 24 21:30 dataset.info
-rw-r--r-- 1  192 Oct 24 21:14 input_dataset.yaml
drwxr-xr-x 5 4.0K Oct 24 21:49 K127
drwxr-xr-x 3 4.0K Oct 24 21:33 K21
drwxr-xr-x 3 4.0K Oct 24 21:35 K33
drwxr-xr-x 3 4.0K Oct 24 21:38 K55
drwxr-xr-x 3 4.0K Oct 24 21:41 K77
drwxr-xr-x 3 4.0K Oct 24 21:45 K99
drwxr-xr-x 2 4.0K Oct 24 21:55 misc
drwxr-xr-x 4 4.0K Oct 24 21:52 mismatch_corrector
-rw-r--r-- 1 1.4K Oct 24 21:14 params.txt
-rw-r--r-- 1 5.6M Oct 24 21:55 scaffolds.fasta
-rw-r--r-- 1  21K Oct 24 21:49 scaffolds.paths
-rw-r--r-- 1 216K Oct 24 21:55 spades.log
drwxr-xr-x 2 4.0K Oct 24 21:55 tmp

```

```
$ tree corrected
corrected
├── configs
│   └── config.info
├── corrected.yaml
├── Kp2146_paired_1.fastq.00.0_0.cor.fastq.gz
├── Kp2146_paired_2.fastq.00.0_0.cor.fastq.gz
└── Kp2146_paired__unpaired.00.0_0.cor.fastq.gz
```


### Getting Stats For the Assemblies

To get some basic stats for the assemblies, run:
```bash
python /usr/local/share/khmer/sandbox/assemstats3.py  1000 assembly/scaffolds.fasta
```
This will yield something like:
```
N       sum     max     filename
38      671957  83467   dn.21/contigs.fa
32      668918  83568   dn.23/contigs.fa
35      668509  83401   dn.25/contigs.fa
31      671843  83817   dn.27/contigs.fa
```



### The result contigs file of interest is spades/contigs.fasta. The contig list is then sorted with
```
$ jsa.seq.sort -r -n --input spades/contigs.fasta --output Kp2146_spades.fasta 
```



#### The contig list is then sorted with jsa.seq.sort
```
$ jsa.seq.sort -r -n --input spades/contigs.fasta --output Kp2146_spades.fasta 
```



#### alignment with bwa
```
$ bwa mem -t 10 -k11 -W20 -r10 -A1 -B1 -O1 -E1 -L0 -a -Y Kp2146_spades.fasta ERR868296_1.fastq.gz > ERR868296.sam

```

#### jsa.np.npscarf
```
$ jsa.np.npscarf -input ERR868296.sam  -format sam -seq Kp2146_spades.fasta -prefix Kp2146-batch

[main] WARN japsa.tools.bio.np.NPScarfCmd - Not found any legal SPAdes output folder, assembly graph thus not included!
#Sort list of bridges
========================== START =============================
  contig   0  ======>     0  839487 1-NODE_1_length_839487_cov_89.415705 
Size = 1 sequence
============================ END ===========================
========================== START =============================
  contig   1  ======>     0  808622 2-NODE_2_length_808622_cov_83.447634 gaps =  -121
  contig  61  ======>808501  810060 62-NODE_62_length_1559_cov_388.005587 gaps =  -36
  contig  34  ======>810024  823263 35-NODE_35_length_13239_cov_94.795226 gaps =  -134
  contig  54  ======<823129  825408 55-NODE_55_length_2279_cov_254.593401 gaps =  -241
  contig  12  ======<825167  943590 13-NODE_13_length_118423_cov_80.342023 
```

output files:
```
-rw-r--r--  1 5.6M Oct 24 22:52 Kp2146-batch.fin.fasta
-rw-r--r--  1 7.5M Oct 24 22:52 Kp2146-batch.fin.japsa


$ head Kp2146-batch.fin.fasta
>Scaffold0
TTGCCTGGCGGCACTAGCGCGGTGGTCCCACCTGACCCCATGCCGAACTCAGAAGTGAAA
CGCCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCATGTGAGAGTAGGGAACTGCCAGGCA
TCAAATTTAGCGTGCTGATATGGCTCAGTTGGTAGAGCGCACCCTTGGTAAGGGTGAGGT
CCCCAGTTCGACTCTGGGTATCAGCACCACTTTTTAGGTTAAAGTTCGGCACGTTGTAAA
GAATTTGCCTGGCGACAATAGCGCGGCGGTCCCACCTGACCCCATGCCGAACTCAGAAGT
GAAACGTCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCATGTGAGAGTAGGGAATCGCCA
GGCATCAAATAAAGCAGAAGGCCCAGTCGAAAGACTGGGCCTTCTGCTTTTGTGTTATCT
GTTATCTGTTGATAAACAGTCCTGCCACCAGGGGGAAACCCGTCAAAGTCGATTTGCTCG
TAATGCAGCAAGGGACAGAGAGTTTATTTGCCCGGTTGTCATGTGGATGATGCGCAGAAG



$ head  Kp2146-batch.fin.japsa
#JSA:Scaffold0:839487:DNA16
>A:Linear


>>CONTIG:1:839487:1-NODE_1_length_839487_cov_89.415705:+::0.0
>1-NODE_1_length_839487_cov_89.415705+[0,839487)

         1   TTGCCTGGCG GCACTAGCGC GGTGGTCCCA CCTGACCCCA TGCCGAACTC
        51   AGAAGTGAAA CGCCGTAGCG CCGATGGTAG TGTGGGGTCT CCCCATGTGA
       101   GAGTAGGGAA CTGCCAGGCA TCAAATTTAG CGTGCTGATA TGGCTCAGTT


```


