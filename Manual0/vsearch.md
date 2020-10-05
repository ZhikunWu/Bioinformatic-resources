# [Vsearch pipeline](https://github.com/torognes/vsearch/wiki/VSEARCH-pipeline)

## Pipeline of 16S rDNA data analysis

* Quality control
* Merge paired-end reads
* Trip primers (and barcodes) 
* Dereplication
* Cluster
* Check chimeras
* Filter OTU
* Construct OTU table (abudance)
* Taxonomy assign

### Vsearch function

* Chimera detection
* Clustering
* Dereplication and rereplication
* FASTQ format conversion
* FASTQ format detection and quality analysis
* FASTQ quality statistics
* Filtering
* Masking
* Paired-end reads merging
* Pairwise alignment
* Reverse complementation
* Searching
* Shuffling and sorting
* Subsampling
* UDB files


### Merge paired-end sequence



```
$ vsearch --fastq_mergepairs V4test1.clean.paired.R1.fq \
        --reverse V4test1.clean.paired.R2.fq  \
        --fastqout V4test1.merge.fq  \
        --threads 20  \
        --fastq_minovlen 5 

vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Merging reads 100%  
   1110488  Pairs
    886174  Merged (79.8%)
    224314  Not merged (20.2%)

Pairs that failed merging due to various reasons:
     39715  too few kmers found on same diagonal
       255  potential tandem repeat
        54  too many differences
    183923  alignment score too low, or score drop to high
       367  staggered read pairs

Statistics of merged reads:
    292.21  Mean fragment length
      7.04  Standard deviation of fragment length
      0.13  Mean expected error in forward sequences
      0.26  Mean expected error in reverse sequences
      0.33  Mean expected error in merged sequences
      0.00  Mean observed errors in merged region of forward sequences
      0.00  Mean observed errors in merged region of reverse sequences
      0.00  Mean observed errors in merged region

```





#### Merge using join_paired_ends.py and MSA

```
$ join_paired_ends.py -f clean.R1.fq -r clean.R2.fq -m fastq-join -o fastq-join.fastq

$ grep -c '^@' fastqjoin.join.fastq
1025552

$ grep -c '^@' fastqjoin.un1.fastq
84936
```

merged ratio 92.4%
merged length: 290-293

```
JQ765577.1.1452 Bacteria;Firmicu      AACTACGTGCCAGCAGCCGCGGTAATACGTAGGTGGCAAGCGTTGTCCGGAATTATTGGG
V4test1_2;barcodelabel=V4test1        -------TGCCAGCAGCCGCGGTAATACGTAGGGGGCGAGCGTTATCCGGATTTATTGGG
V4test1_3;barcodelabel=V4test1        -------TGCCAGCAGCCGCGGTAATACGTAGGTGGCAAGCGTTGTCCGGAATTACTGGG
V4test1_1;barcodelabel=V4test1        -------TGCCAGCAGCCGCGGTAATACGTATGGTGCAAGCGTTATCCGGATTTACTGGG
                                             ************************ *  ** ****** ****** *** ****

JQ765577.1.1452 Bacteria;Firmicu      CGTAAAGGGCTCGCAGGCGGTTTCTTAAGTCTGATGTGAAAGCCCCCGGCTCAACCGGGG
V4test1_2;barcodelabel=V4test1        CGTAAAGCGTGTGTAGGCGATTTATTAAGTCTAAGATCAAAGCCCGAGGCTCTACCTCGG
V4test1_3;barcodelabel=V4test1        TGTAAAGGGAGCGCAGGCGGGACTGCAAGTTGGATGTGAAATACCGCAGCTTAACTGCGG
V4test1_1;barcodelabel=V4test1        TGTAAAGGGAGCGCAGGCGGTTTAGCAAGTCTGATGTGAAAGCCCGGGGCTCAACCCCGG
                                       ****** *   * *****       ****   *  * ***  **   ***  **   **

JQ765577.1.1452 Bacteria;Firmicu      AGGGTCATTGGAAACTGGGGAACTTGAGTGCAGAAGAGGAGAGTGGAATTCCACGTGTAG
V4test1_2;barcodelabel=V4test1        TTCGTC-TTAGAAACTGGTATACTTGAGTGTGGTAGAGGCAAGTGGAATTTCTAGTGTAG
V4test1_3;barcodelabel=V4test1        AGCTGCATCCAAAACTGTAGTTCTTGAGTGGAGTAGAGGTAGGCGGAATTCCGAGTGTAG
V4test1_1;barcodelabel=V4test1        TACTGCATTGGAAACTGTTGGACTAGAGTGTCGGAGGGGTAAGTGGAATACCTAGTGTAG
                                           * *   ******     ** *****  * ** **   * *****  *  ******

JQ765577.1.1452 Bacteria;Firmicu      CGGTGAAATGCGTAGAGATGTGGAGGAACACCCAGTGGCGAAGGCGACTCTCTGGTCTGT
V4test1_2;barcodelabel=V4test1        CGGTTAAATGCGTAGATATTAGAAGGAAAA-CCAGTGGCGAAGGCGGCTTGCTGGGCCAT
V4test1_3;barcodelabel=V4test1        CGGTGAAATGCGTAGATATTCGGAGGAACA-CCAGTGGCGAAGGCGGCCTACTGGGCTCT
V4test1_1;barcodelabel=V4test1        CGGTGAAATGCGTAGATATTAGGAGGAACA-CCAGTGGCGAAGGCGGCTTACTGGACGAT
                                      **** *********** **  * ***** * *************** *   **** *  *

JQ765577.1.1452 Bacteria;Firmicu      AACTGACGCTGAGGAGCGAAAGCGTGGGGAGCGAACAGGATTAGATACCCTGGTAGTCCA
V4test1_2;barcodelabel=V4test1        TACTGACGCTGAGACACGAAAGCGTGGGGAGCAAATAGGATTAGATACCCTAGTAGTCC-
V4test1_3;barcodelabel=V4test1        TACTGACGCTGAGGCTCGAAAGTGTGGGGAGCAAACAGGATTAGATACCCTAGTAGTCC-
V4test1_1;barcodelabel=V4test1        TACTGACGCTGAGGCTCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTAGTAGTCC-
                                       ************   ****** ********* ** *************** ******* 



```

### Strip primers and barcodes

```
$ vsearch --fastx_filter   V4test1.merge.fq  \
    --fastq_stripleft  15 \
    --fastq_stripright 20 \
    --fastqout V4test1.merge_strip.fq  \
    --threads 20

Reading input file 100%  
886174 sequences kept (of which 886174 truncated), 0 sequences discarded.
```



### Dereplication the merged sequence

```
$ vsearch --threads 20 \
    --derep_fulllength fastqjoin.join.fasta \
    --output fastqjoin.join_dereplication.fasta \
    --minuniquesize 2 \
    --threads 20  \
    --sizeout


vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file fastqjoin.join.fasta 100%  
299789462 nt in 1025552 seqs, min 36, max 296, avg 292
Dereplicating 100%  
Sorting 100%
191515 unique sequences, avg cluster 5.4, median 1, max 26877
Writing output file 100%  
28864 uniques written, 162651 clusters discarded (84.9%)
```


output file:
```
$ head fastqjoin.join_dereplication.fasta
>V4test1_31;barcodelabel=V4test1;size=26877;
GTGCCAGCAGCCGCGGTAATACGGAGGATGCGAGCGTTATCCGGATTTATTGGGTTTAAAGGGTGCGCAGGCGGCACGTT
AAGTCAGCGGTGAAATGTCGGGGCTCAACCCCGTCACTGCCGTTGAAACTGGCGAGCTCGAGTACGGATGAAGTGGGCGG
AATGTGATGTGTAGCGGTGAAATGCTTAGATATGTCACAGAACACCGATTGCGAAGGCAGCTCACTAATCCGCAACTGAC
GCTCATGCACGAAAGCGTGGGGATCGAACAGGATTAGATACCCTAGTAGTCCA
>V4test1_164;barcodelabel=V4test1;size=22065;
GTGCCAGCAGCCGCGGTAATACGTAGGTTGCAAGCGTTGTCCGGATTTACTGGGTGTAAAGGGCGTGTAGGCGGAGATGC
AAGTTGGGAGTGAAATCCCGGGGCTCAACCCCGGAACTGCTTTCAAAACTGCATCCCTTGAGTATCGGAGAGGCAAGCGG
AATTCCTAGTGTAGCGGTGAAATGCGTAGATATTAGGAGGAACACCAGTGGCGAAGGCGGCTTGCTGGACGACAACTGAC
GCTGAGGCGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTAGTAGTCCA
```

### Cluster using dereplicated sequences

```
$ vsearch --cluster_fast fastqjoin.join_dereplication.fasta \
    --id 0.97  \
    --centroids fastqjoin.join_dereplication_out.txt  \
    --relabel OTU_   \
    --threads 20  \
    --msaout fastqjoin.join_dereplication_msaout.txt


vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file fastqjoin.join_dereplication.fasta 100%  
8429062 nt in 28864 seqs, min 81, max 295, avg 292
Masking 100%  
Sorting by length 100%
Counting k-mers 100%  
Clustering 100%  
Sorting clusters 100%
Writing clusters 100%  
Clusters: 2141 Size min 1, max 1045, avg 13.5
Singletons: 862, 3.0% of seqs, 40.3% of clusters
Multiple alignments 100% 
```


output files

clusters
```
$ head fastqjoin.join_dereplication_out.txt
>OTU_1
GTGCCAGCAGCCGCGGTCATACGTAGGATCCGAGCATTATCCGGAGTGACTGGGCGTAAAGAGTTGCGTAGGTGGATGTT
TAAGTAGATGGTGAAATCTGGTGGCTCAACCATTCAGACTGTTATCTAAACTGGACATCTCGAGAGCGTCAGGGGTGACT
GGAATTTCTAGTGTAGGAGTGAAATCCGTAGATATTAGAAGGAACACCGATAGCGTAGGCAGGTCACTAGGGCGTTTCTG
ACACTAAGGCACGAAAGCGTAGGGAGCAAACGGGATTAGATACCCTAGTAGTCCA
>OTU_2
GTGCCAGCAGCCGCGGTCATACGTAGGACCCAAGTGTTATCCGGAGTGACTGGGCGTAAAGAGTTGCGTAGGCGGTTATG
CAAGTGAATAGTGAAACCTGGTGGCTCAACCACTCAGACTATTATTCAAACTGCATAACTCGAGAATAGTAGAGGTAACT
GGAATTTCTTGTGTAGGAGTGAAATCCGTAGATATAAGAAGGAACACCAATGGCGTAGGCAGGTTACTGGGCTATTTCTG
ACGCTAAGGCACGAAAGCGTGGGGAGCGAACCGGATTAGATACCCTAGTAGTCCA
```

consensus sequences and corresponding sequences
```
$ grep -c '>consensus' fastqjoin.join_dereplication_msaout.txt
2141

$ head -n 11 fastqjoin.join_dereplication_msaout.txt

>*V4test1_137959;barcodelabel=V4test1;size=2;
GTGCCAGCAGCCGCGGTCATACGTAGGATCCGAGCATTATCCGGAGTGACTGGGCGTAAAGAGTTGCGTAGGTGGATGTT
TAAGTAGATGGTGAAATCTGGTGGCTCAACCATTCAGACTGTTATCTAAACTGGACATCTCGAGAGCGTCAGGGGTGACT
GGAATTTCTAGTGTAGGAGTGAAATCCGTAGATATTAGAAGGAACACCGATAGCGTAGGCAGGTCACTAGGGCGTTTCTG
ACACTAAGGCACGAAAGCGTAGGGAGCAAACGGGATTAGATACCCTAGTAGTCCA
>consensus
GTGCCAGCAGCCGCGGTCATACGTAGGATCCGAGCATTATCCGGAGTGACTGGGCGTAAAGAGTTGCGTAGGTGGATGTT
TAAGTAGATGGTGAAATCTGGTGGCTCAACCATTCAGACTGTTATCTAAACTGGACATCTCGAGAGCGTCAGGGGTGACT
GGAATTTCTAGTGTAGGAGTGAAATCCGTAGATATTAGAAGGAACACCGATAGCGTAGGCAGGTCACTAGGGCGTTTCTG
ACACTAAGGCACGAAAGCGTAGGGAGCAAACGGGATTAGATACCCTAGTAGTCCA
```


### Check chimeras

#### Detect chimeras based on reference
```
$ vsearch --uchime_ref fastqjoin.join_dereplication_out.txt  \
    -db /home/wzk/Project/KC2017-B123/rdp_gold.fa  \
    --nonchimeras  fastqjoin.join_dereplication_nochimeras.txt \
    --threads 20  


vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file /home/wzk/Project/KC2017-B123/rdp_gold.fa 100%  
29007378 nt in 20098 seqs, min 320, max 2210, avg 1443
Masking 100%  
Counting k-mers 100%  
Creating k-mer index 100%  
Detecting chimeras 100%  
Found 22 (1.0%) chimeras, 2118 (98.9%) non-chimeras,
and 1 (0.0%) borderline sequences in 2141 unique sequences.
Taking abundance information into account, this corresponds to
22 (1.0%) chimeras, 2118 (98.9%) non-chimeras,
and 1 (0.0%) borderline sequences in 2141 total sequences.
```

```
$ vsearch --uchime_ref fastqjoin.join_dereplication_out.txt \
      -db /home/wzk/database/SILVA/SILVA_132_SSUParc_tax_silva_genus.fasta  \
      --nonchimeras  fastqjoin.join_dereplication_nochimeras.txt \
      --threads 20  


vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file /home/wzk/database/SILVA/SILVA_132_SSUParc_tax_silva_genus.fasta 100%  
2296961572 nt in 1627728 seqs, min 1200, max 4000, avg 1411
Masking 100%  
Counting k-mers 100%  
Creating k-mer index 100%  
Detecting chimeras 100%  
Found 182 (8.5%) chimeras, 1929 (90.1%) non-chimeras,
and 30 (1.4%) borderline sequences in 2141 unique sequences.
Taking abundance information into account, this corresponds to
182 (8.5%) chimeras, 1929 (90.1%) non-chimeras,
and 30 (1.4%) borderline sequences in 2141 total sequences.
```


the database records:
```
$ grep -c '^>' /home/wzk/Project/KC2017-B123/rdp_gold.fa
20098

$ grep -c '^>' /home/wzk/database/SILVA/SILVA_132_SSUParc_tax_silva_genus.fasta
1627728
```

These databases are enough, bacause the ratios of chemiras are similiar even the records of databased have great difference.



#### De novo detect chimeras

```
$ vsearch --uchime_denovo B120.fa  \
    --nonchimeras B120_nochimeras.fa  \
    --threads 20

vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file B120.fa 100%  
1422191 nt in 5723 seqs, min 37, max 296, avg 249
Masking 100%  
Sorting by abundance 100%
Counting k-mers 100%  
Detecting chimeras 100%  
Found 0 (0.0%) chimeras, 5723 (100.0%) non-chimeras,
and 0 (0.0%) borderline sequences in 5723 unique sequences.
Taking abundance information into account, this corresponds to
0 (0.0%) chimeras, 5723 (100.0%) non-chimeras,
and 0 (0.0%) borderline sequences in 5723 total sequences.
```


### Construct OTU table

```
$ vsearch --usearch_global fastqjoin.join.fasta    \
    -db fastqjoin.join_dereplication_nochimeras.txt     \
    --id 0.97 \
    --otutabout otu_table.txt   \
    --threads 20 

vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file fastqjoin.join_dereplication_nochimeras.txt 100%  
546713 nt in 1929 seqs, min 81, max 295, avg 283
Masking 100%  
Counting k-mers 100%  
Creating k-mer index 100%  
Searching 100%  
Matching query sequences: 934567 of 1025552 (91.13%)
Writing OTU table (classic) 100% 
```

output files:
```
$ wc -l  out_table.txt
1930 otu_table.txt

$ head otu_table.txt 
#OTU ID V4test1
OTU_1   2
OTU_10  245
OTU_100 37
OTU_1000    25
OTU_1001    12
OTU_1002    11
OTU_1003    13
OTU_1004    12
OTU_1005    24
```

### Assign taxonomy for OTU

database:

```
$ less rdp_16s_v16.fa

>AJ000684_S000004347;tax=d:Bacteria,p:"Actinobacteria",c:Actinobacteria,o:Actinomycetales,f:Mycobacteriaceae,g:Mycobacterium;
GAACGCTGGCGGCGTGCTTAACACATGCAAGTCGAACGGAAAGGTCTCTTCGGAGATACTCGAGTGGCGAACGGGTGAGT
AACACGTGGGTAATCTGCCCTGCACATCGGGATAAGCCTGGGAAACTGGGTCTAATACCGAATAGGACCTCGAGGCGCAT
GCCTTGTGGTGGAAAGCTTTTGCGGTGTGGGATGGGCCCGCGGCCTATCAGCTTGTTGGTGGGGTGACGGCCTACCAAGG
CGACGACGGGTAGCCGGCCTGAGAGGGTGTCCGGCCACACTGGGACTGAGATACGGCCCAGACTCCTACGGGAGGCAGCA
GTGGGGAATATTGCACAATGGGCGCAAGCCTGATGCAGCGACGCCGCGTGGGGGATGACGGNCTTCGGGTTGTAAACCTC
TTTCAGCAGGGACGAAGCGCAAGTGACGGTACCTGCAGAAGAAGCACCGGCCAACTACGTGCCAGCAGCCGCGGTAATAC
GTAGGGTGCGAGCGTTGTCCGGAATTACTGGGCGTAAAGAGCTCGTAGGTGGTTTGTCGCGTTGTTCGTGAAAACCGGGG
GCTTAACCCTCGGCGTGCGGGCGATACGGGCAGACTGGAGTACTGCAGGGGAGACTGGAATTCCTGGTGTAGCGGTGGAA
TGCGCAGATATCAGGAGGAACACCGGTGGCGAAGGCGGGTCTCTGGGCAGTAACTGACGCTGAGGAGCGAAAGCGTGGGG
```

#### Alignment format
```
$ vsearch --usearch_global  fastqjoin.join_dereplication_nochimeras.txt   \
    -db /home/wzk/database/SILVA/rdp_16s_v16.fa \
    --alnout otu_table_tax.aln \
    --id 0.97 \
    --threads 20


vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file /home/wzk/database/SILVA/rdp_16s_v16.fa 100%  
19098167 nt in 13212 seqs, min 320, max 2210, avg 1446
Masking 100%  
Counting k-mers 100%  
Creating k-mer index 100%  
Searching 100%  
Matching query sequences: 99 of 1929 (5.13%)
```

output file
```
$ less otu_table_tax.aln


Query >OTU_16
 %Id   TLen  Target
 98%   1266  AY615201_S000548389;tax=d:Archaea,p:"Euryarchaeota",c:Methanobacteria,o:Methanobacteriales,f:Methanobac

 Query  294nt >OTU_16
Target 1266nt >AY615201_S000548389;tax=d:Archaea,p:"Euryarchaeota",c:Methanobacteria,o:Methanobacteriales,f:Methanob

Qry    1 + GTGCCAGCAGCCGCGGTAACACCGGCAGCTCTAGTGGTAGCTGTTTTTATTGGGCCTAAAGCGT 64
           |||||||| |||||||||||||||||||||||||||||||||||||||||||||||||||||||
Tgt  373 + GTGCCAGCCGCCGCGGTAACACCGGCAGCTCTAGTGGTAGCTGTTTTTATTGGGCCTAAAGCGT 436

Qry   65 + TCGTAGCCGGTTTGATAAGTCACTGGTGAAATCCTGTAGCTTAACTGTGGGAATTGCTGGTGAT 128
           |||||||||||||| ||||||||||||||||||||||||||||||| |||||||||||||||||
Tgt  437 + TCGTAGCCGGTTTGGTAAGTCACTGGTGAAATCCTGTAGCTTAACTATGGGAATTGCTGGTGAT 500

Qry  129 + ACTGTTGAACTTGAGGTCGGGAGAGGTTAGCGGTACTCCCAGGGTAGAGGTGAAATTCTGTAAT 192
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Tgt  501 + ACTGTTGAACTTGAGGTCGGGAGAGGTTAGCGGTACTCCCAGGGTAGAGGTGAAATTCTGTAAT 564

Qry  193 + CCTGGGAGGACCACCTGTGGCGAAGGCGGCTAACTGGAACGAACCTGACGGTGAGGGACGAAAG 256
           ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Tgt  565 + CCTGGGAGGACCACCTGTGGCGAAGGCGGCTAACTGGAACGAACCTGACGGTGAGGGACGAAAG 628

Qry  257 + CTAGGGGCGCGAACCGGATTAGATACCCTAGTAGTCCA 294
           ||||||||||||||||||||||||||||  ||||||| 
Tgt  629 + CTAGGGGCGCGAACCGGATTAGATACCCGGGTAGTCCT 666

294 cols, 288 ids (98.0%), 0 gaps (0.0%)

```

#### Alignment using SILVA database

SILVA database


```
>GY193009.2153721.2155249   Bacteria;Firmicutes;Bacilli;Lactobacillales;Streptococcaceae;Streptococcus
AGAGTTTGATCCTGGCTCAGGACGAACGCTGGCGGCGTGCCTAATACATGCAAGTAGAACGCTGAGGTTTGGTGTTTACACTAGACTGATGAGTTGCGAACGGGTGAGTAACGCGTAGGTAACCTGCCTCATAGCGGGGGATAACTATTGGAAACGATAGCTAATACCGCATAAGAGTAATTAACACATGTTAGTTATTTAAAAGGAGCAATTGCTTCACTGTGAGATGGACCTGCGTTGTATTAGCTAGTTGGTGAGGTAAAGGCTCACCAAGGCGACGATACATAGCCGACCTGAGAGGGTGATCGGCCACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTAGGGAATCTTCGGCAATGGACGGAAGTCTGACCGAGCAACGCCGCGTGAGTGAAGAAGGTTTTCGGATCGTAAAGCTCTGTTGTTAGAGAAGAACGTTGGTAGGAGTGGAAAATCTACCAAGTGACGGTAACTAACCAGAAAGGGACGGCTAACTACGTGCCAGCAGCCGCGGTAATACGTAGGTCCCGAGCGTTGTCCGGATTTATTGGGCGTAAAGCGAGCGCAGGCGGTTCTTTAAGTCTGAAGTTAAAGGCAGTGGCTTAACCATTGTACGCTTTGGAAACTGGAGGACTTGAGTGCAGAAGGGGAGAGTGGAATTCCATGTGTAGCGGTGAAATGCGTAGATATATGGAGGAACACCGGTGGCGAAAGCGGCTCTCTGGTCTGTAACTGACGCTGAGGCTCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGAGTGCTAGGTGTTAGGCCCTTTCCGGGGCTTAGTGCCGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCAACGCGAAGAACCTTACCAGGTCTTGACATCCTTCTGACCGGCCTAGAGATAGGCTTTCTCTTCGGAGCAGAAGTGACAGGTGGTGCATGGTTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCCTATTGTTAGTTGCCATCATTAAGTTGGGCACTCTAGCGAGACTGCCGGTAATAAACCGGAGGAAGGTGGGGATGACGTCAAATCATCATGCCCCTTATGACCTGGGCTACACACGTGCTACAATGGTTGGTACAACGAGTCGCAAGCCGGTGACGGCAAGCTAATCTCTTAAAGCCAATCTCAGTTCGGATTGTAGGCTGCAACTCGCCTACATGAAGTCGGAATCGCTAGTAATCGCGGATCAGCACGCCGCGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCACGAGAGTTTGTAACACCCGAAGTCGGTGAGGTAACCTTTTAGGAGCCAGCCGCCTAAGGTGGGATAGATGATTGGGGTGAAGTCGTAACAAGGTAGCCGTATCGGAAGGTGCGGCTG
```


```
$ vsearch --usearch_global  fastqjoin.join_dereplication_nochimeras.txt    \
       -db /home/wzk/database/SILVA/SILVA_132_SSUParc_tax_silva_genus.fasta  \
       --alnout otu_table_tax.aln     \
       --id 0.97     \
       --threads 20


vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file /home/wzk/database/SILVA/SILVA_132_SSUParc_tax_silva_genus.fasta 100%  
2296961572 nt in 1627728 seqs, min 1200, max 4000, avg 1411
Masking 100%  
Counting k-mers 100%  
Creating k-mer index 100%  
Searching 100%  
Matching query sequences: 694 of 1929 (35.98%)
```

#### Alignment using greengene database

```
>Bacteria;Proteobacteria;Alphaproteobacteria;Sphingomonadales;Sphingomonadaceae;Kaistobacter
AACGAACGCTGGCGGCATGCCTAACACATGCAAGTCGAACGAGACCTTCGGGTCTAGTGGCGCACGGGTGCGTAACGCGTGGGAATCTGCCCTTGGGTACGGAATAACAGTTAGAAATGACTGCTAATACCGTATAATGACTTCGGTCCAAAGATTTATCGCCCAGGGATGAGCCCGCGTAGGATTAGCTTGTTGGTGAGGTAAAGGCTCACCAAGGCGACGATCCTTAGCTGGTCTGAGAGGATGATCAGCCACACTGGGACTGAGACATGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGGACAATGGGCGAAAGCCTGATCCAGCAATGCCGCGTGAGTGATGAAGGCCTTAGGGTTGTAAAGCTCTTTTACCCGGGATGATAATGACAGTACCGGGAGAATAAGCCCCGGCTAACTCCGTGCCAGCAGCCGCGGTAATACGGAGGGGGCTAGCGTTGTTCGGAATTACTGGGCGTAAAGCGCACGTAGGCGGCTTTGTAAGTTAGAGGTGAAAGCCCGGGGCTCAACTCCGGAATTGCCTTTAAGACTGCATCGCTAGAATTGTGGAGAGGTGAGTGGAATTCCGAGTGTAGAGGTGAAATTCGTAGATATTCGGAAGAACACCAGTGGCGAAGGCGACTCACTGGACACATATTGACGCTGAGGTGCGAAAGCGTGGGGAGCAAACAGGATTAGATACCCTGGTAGTCCACGCCGTAAACGATGATGACTAGCTGTCGGGGCGCTTAGCGTTTCGGTGGCGCAGCTAACGCGTTAAGTCATCCGCCTGGGGAGTACGGCCGCAAGGTTAAAACTCAAAGAAATTGACGGGGGCCTGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCAACGCGCAGAACCTTACCAGCGTTTGACATGGTAGGACGGTTTCCAGAGATGGATTCCTACCCTTACGGGACCTACACACAGGTGCTGCATGGCTGTCGTCAGCTCGTGTCGTGAGATGTTGGGTTAAGTCCCGCAACGAGCGCAACCCTCGTCTTTGGTTGCTACCATTTAGTTGAGCACTCTAAAAAAACTGCCGGTGATAAGCCGGAGGAAGGTGGGGATGACGTCAAGTCCTCATAGCCCTTACGCGCTGGGCTACACACGTGCTACAATGGCGGTGACAGAGGGCAGCAAACCCGCGAGGGTGAGCTAATCTCCAAAAGCCGTCTCAGTTCGGATTGTTCTCTGCAACTCGAGAGCATGAAGGCGGAATCGCTAGTAATCGCGGATCAGCACGCCGCGGTGAATACGTTCCCAGGCCTTGTACACACCGCCCGTCACATCACGAAAGTCGGTTGCACTAGAAGTCGGTGGGCTAACCCGCAAGGGAGGCAGCCGCCTAAAGTGTGATCGGTAATTGGGGTG
```



#### Biom format for taxonomy
```
$ vsearch --usearch_global  fastqjoin.join_dereplication_nochimeras.txt   \
    -db /home/wzk/database/SILVA/rdp_16s_v16.fa \
    --biomout out_table_tax.biom  \
    --id 0.97  \
    --threads 20 


vsearch v2.6.0_linux_x86_64, 251.7GB RAM, 40 cores
https://github.com/torognes/vsearch

Reading file /home/wzk/database/SILVA/rdp_16s_v16.fa 100%  
19098167 nt in 13212 seqs, min 320, max 2210, avg 1446
Masking 100%  
Counting k-mers 100%  
Creating k-mer index 100%  
Searching 100%  
Matching query sequences: 99 of 1929 (5.13%)
Writing OTU table (biom 1.0) 100%
```






