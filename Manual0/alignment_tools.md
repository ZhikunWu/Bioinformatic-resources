

## bwa
### bwa men
```
$ bwa mem -t 5 /home/wzk/database/SILVA/greengene/SILVA_Greengene_16SrRNA_dereplication_taxas_species.fasta LGS3-LW-1_test_Consensus.R1.fasta LGS3-LW-1_test_Consensus_cut.R2.fasta > LGS3-LW-1.sam
```

### output all rerults using bwa
```
$ bwa mem  -t 5 -a /home/wzk/database/SILVA/greengene/SILVA_Greengene_16SrRNA_dereplication_taxas_species.fasta LGS3-LW-1_test_Consensus.R1.fasta LGS3-LW-1_test_Consensus_cut.R2.fasta > LGS3-LW-1_all5.sam
```

### get targets

```
$ cut -f 3 LGS3-LW-1_all5_test.sam | sort | uniq -c | sort -k 1nr | grep ' 2' | awk -F " " '{print $NF}' > description.txt

$ cat description.txt 
AF053887.1.1504
AF053896.1.1504
AF053900.1.1504
AY362927.1.1362
AY425283.1.1346
AY425284.1.1401
```


get the taxonomy based on the query gene 
```
$ cat description.txt  | while read marker; do sed -n '/^'"$marker"'\t.*/p' /home/wzk/database/SILVA/greengene/SILVA_Greengene_16SrRNA_dereplication_taxas_species_description.txt; done > description_species.txt

$ cat description_species.txt
AF053887.1.1504 k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Pasteurellales; f__Pasteurellaceae; g__Mannheimia; s__UT26
AF053896.1.1504 k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Pasteurellales; f__Pasteurellaceae; g__Mannheimia; s__ruminalis
AF053900.1.1504 k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Pasteurellales; f__Pasteurellaceae; g__Mannheimia; s__ruminalis
```



### bwa with split reads
```
$ bwa mem -t 8 -a  /home/wzk/database/SILVA/greengene/SILVA_Greengene_16SrRNA_dereplication_taxas_species.fasta  LGS3-LW-1_test_Consensus.R1.fasta  > LGS3-LW-1_test.sam
```


### stats for mapping
```
$ samtools flagstat  J1-08.sam
63479928 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
254110 + 0 supplementary
0 + 0 duplicates
29626440 + 0 mapped (46.67% : N/A)
63225818 + 0 paired in sequencing
31612909 + 0 read1
31612909 + 0 read2
27559856 + 0 properly paired (43.59% : N/A)
28470444 + 0 with itself and mate mapped
901886 + 0 singletons (1.43% : N/A)
903312 + 0 with mate mapped to a different chr
684309 + 0 with mate mapped to a different chr (mapQ>=5)
```



## bowtie2

### bowtie2 build index
```
$ bowtie2-build viral_7955.fasta viral_7955

-rw-r--r-- 1  89M Sep 24 22:06 viral_7955.1.bt2
-rw-r--r-- 1  64M Sep 24 22:06 viral_7955.2.bt2
-rw-r--r-- 1 126K Sep 24 22:04 viral_7955.3.bt2
-rw-r--r-- 1  64M Sep 24 22:04 viral_7955.4.bt2
-rw-r--r-- 1  89M Sep 24 22:09 viral_7955.rev.1.bt2
-rw-r--r-- 1  64M Sep 24 22:09 viral_7955.rev.2.bt2
```

### run bowtie2
```
bowtie2 -x /home/wzk/database/Bacterial_genome/combine/viral_7955  -1 /home/wzk/Project/C128/clean/J1-08.clean.paired.R1.fq.gz -2 /home/wzk/Project/C128/clean/J1-08.clean.paired.R2.fq.gz --threads 30 -S /home/wzk/Project/C128/bowtie_mapping/J1-08_bowtie.sam 
```

output stats:
```
$ samtools flagstat J1-08_bowtie.sam
[W::sam_read1] parse error at line 2069200
[bam_flagstat_core] Truncated file? Continue anyway.
2061242 + 0 in total (QC-passed reads + QC-failed reads)
0 + 0 secondary
0 + 0 supplementary
0 + 0 duplicates
383 + 0 mapped (0.02% : N/A)
2061242 + 0 paired in sequencing
1030621 + 0 read1
1030621 + 0 read2
224 + 0 properly paired (0.01% : N/A)
228 + 0 with itself and mate mapped
155 + 0 singletons (0.01% : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)
```



## soap

### build index
```
2bwt-builder <sequence file>
```

### soap parameters
```
$ soap

Program: SOAPaligner/soap2
Compile Date: 2017-05-11T21:11:08+0000
Author:  BGI shenzhen
Version: 2.20
Contact: soap@genomics.org.cn

Usage:  soap [options]
    -a  <str>   query a file, *.fq, *.fa
    -b  <str>   query b file
    -D  <str>   reference sequences indexing table, *.index format
    -o  <str>   output alignment file(txt)
    -M  <int>   match mode for each read or the seed part of read, which shouldn't contain more than 2 mismaches, [4]
                0: exact match only
                1: 1 mismatch match only
                2: 2 mismatch match only
                4: find the best hits
    -u  <str>   output unmapped reads file
    -t          output reads id instead reads name, [none]
    -l  <int>   align the initial n bps as a seed [256] means whole length of read
    -n  <int>   filter low-quality reads containing >n Ns before alignment, [5]
    -r  [0,1,2] how to report repeat hits, 0=none; 1=random one; 2=all, [1]
    -m  <int>   minimal insert size allowed, [400]
    -x  <int>   maximal insert size allowed, [600]
    -2  <str>   output file of unpaired alignment hits
    -v  <int>   maximum number of mismatches allowed on a read. [5] bp
    -s  <int>   minimal alignment length (for soft clip) [255] bp
    -g  <int>   one continuous gap size allowed on a read. [0] bp
    -R          for long insert size of pair end reads RF. [none](means FR pair)
    -e  <int>   will not allow gap exist inside n-bp edge of a read, default=5
    -p  <int>   number of processors to use, [1]

    -h          this help
```

