## anvio

### install anvio
```
$ conda install -c bioconda anvio
```

### anvio tools
```bash
$ ls ~/anaconda3/envs/qiime/bin/ | grep 'anvi'
anvi-cluster-with-concoct
anvi-compute-completeness
anvi-delete-collection
anvi-display-pan
anvi-experimental-organization
anvi-export-collection
anvi-export-contigs
anvi-export-functions
anvi-export-gene-calls
anvi-export-splits-and-coverages
anvi-export-splits-taxonomy
anvi-export-state
anvi-export-table
anvi-gen-contigs-database
anvi-gen-genomes-storage
anvi-gen-network
anvi-gen-samples-info-database
anvi-gen-variability-matrix
anvi-gen-variability-network
anvi-gen-variability-profile
anvi-get-aa-counts
anvi-get-aa-frequencies
anvi-get-aa-sequences-for-gene-calls
anvi-get-dna-sequences-for-gene-calls
anvi-get-sequences-for-hmm-hits
anvi-get-short-reads-from-bam
anvi-get-short-reads-mapping-to-a-gene
anvi-import-collection
anvi-import-functions
anvi-import-state
anvi-import-taxonomy
anvi-init-bam
anvi-interactive
anvi-matrix-to-newick
anvi-merge
anvi-oligotype-linkmers
anvi-pan-genome
anvi-profile
anvi-push
anvi-refine
anvi-rename-bins
anvi-report-linkmers
anvi-run-hmms
anvi-run-ncbi-cogs
anvi-script-convert-annotation-db-to-contigs-db
anvi-script-FASTA-to-contigs-db
anvi-script-gen-CPR-classifier
anvi-script-gen-distribution-of-genes-in-a-bin
anvi-script-gen-environmental-core-summary
anvi-script-generate-auxiliary-data-from-summary-cp
anvi-script-gen-short-reads
anvi-script-gen_stats_for_single_copy_genes.py
anvi-script-gen_stats_for_single_copy_genes.R
anvi-script-gen_stats_for_single_copy_genes.README
anvi-script-gen_stats_for_single_copy_genes.sh
anvi-script-get-collection-info
anvi-script-get-collections-as-tab-delimited-matrix.py
anvi-script-get-prot-sequences.py
anvi-script-itep-to-data-txt
anvi-script-merge-collections
anvi-script-PCs-to-gene-calls
anvi-script-predict-CPR-genomes
anvi-script-reformat-fasta
anvi-script-run-eggnog-mapper
anvi-script-snvs-to-interactive
anvi-script-update-runinfo-variable
anvi-script-upgrade-contigs-db-v5-to-v6
anvi-script-upgrade-contigs-db-v6-to-v7
anvi-script-upgrade-contigs-db-v7-to-v8
anvi-script-upgrade-profile-db-v13-to-v14
anvi-script-upgrade-profile-db-v14-to-v15
anvi-script-upgrade-profile-db-v15-to-v16
anvi-script-upgrade-profile-db-v16-to-v17
anvi-script-upgrade-profile-db-v4-to-v5
anvi-script-upgrade-profile-db-v5-to-v6
anvi-search-functions-in-splits
anvi-self-test
anvi-server
anvi-setup-ncbi-cogs
anvi-show-collections-and-bins
anvi-summarize

```

## [WORKSHOPS INSTALLATION TUTORIALS HELP Anvi'o User Tutorial for Metagenomic  workflow](ttp://merenlab.org/2016/06/22/anvio-tutorial-v2/#anvi-run-hmms)
#### [Importing functions into contigs database](http://merenlab.org/2016/06/18/importing-functions/)

#### Filter contig with length > 1000 and simple name
```bash
$ anvi-script-reformat-fasta HMP_GUT_SRS052697.25M.contigs.fa -o HMP_GUT_SRS052697.25M.contigs_filted.fa -l 1000 --simplify-names

Input ........................................: HMP_GUT_SRS052697.25M.contigs.fa
Output .......................................: HMP_GUT_SRS052697.25M.contigs_filted.fa
Minimum length ...............................: 1,000
Total num contigs ............................: 140,756
Total num nucleotides ........................: 213,146,787
Contigs removed ..............................: 105079 (74.65% of all)
Nucleotides removed ..........................: 52709581 (24.73% of all)
Deflines simplified ..........................: True

```

file before and after filtering
```bash
$ head -n 2 HMP_GUT_SRS052697.25M.contigs.fa
>k119_2 flag=1 multi=4.0000 len=311
CCGCTACGCCGGTACGGAACGATTTCCGGCCATCCTCTCCCCAGAGCAGCTACAGGAAGCTGCCCAGCGCCGGTCAGAGCGTAAGCCTGCGGTGCAGATAACCGAAGCACAAAAGGCACTGCGCCGCCTGTGCAACGGCAGACCCAGTGCAGCGGTGGAGTCACAGGTGCTGTCCCTGCTGAATTGTCTTGCGGCAGCGCCGGAACAGATCAAGCCACAGCCGCAGACAGTCAACCGTGGTGAGCTGGCCGAAATGGAGCGGCGATTCTCAGCAGCACTTACCACCAGTCCGGTGGATGAGGGCAGTGCTA

$ head -n 2 HMP_GUT_SRS052697.25M.contigs_filted.fa
>c_000000000030
ATTGTTTTTGCAGTTGAGTATAATTGTCTTTCTGAATCTAGGATCAGAGATCCAAGTTGTTCCTTTGTCATTTAAACACCACCTTTTTTTTTGCCAGCCAGCATTTTCTTAGACGTGCAGAAATCAAAAATATCCCTAATAATTTATTCTTTTTCTTATAAATGGACAAGTTCGTGGTTTTGCACAAAAAAATGTCTACTTTCGATAGTATTCCATAATGAAAGCAATAAAACAAGCATTTGCAAAGGGACATTGTTATAATTAAATTTGTTCATGGGTGTTATTTGTGATTACTTTCATGCTAATATGCTAATGTGCATTATCATATTAGCATGAAAAAAGTTAGGAAAATCTTAATAATTTCGCATGCAATCCATTGTGAATTTAGATGCTGTATTTGTTATACTTAATCGAGTACAAGCAAAAAGGAGAGTTGAAAATATGTCTGAAAAGATACTGATTATAGATGACGAGCAAGATATAGCGGATCTGTTGGAGGTCTACTTGAAAAACGAAAATTACGTCGTTTATAAATTTTACTGCGCAACGGATGCCATGTCGTGTATTGAAAGCGGCGACATTGATCTTGCCATTCTGGATATTATGCTCCCGGATATGAACGGCTTTTCACTTTGCCAGCTTATCCGAAAGAAATACACTTATCCAATCATAATGCTAACGGCTAAAATTGAGGAAACGGATAAAATAACGGGGCTGACATTGGGAGCGGACGATTATGTGACAAAACCTTTTCGCCCACTTGAAGTAGTTGCCAGAGTGAAAGCGCAGTTAAGACGTTACAAGAAATATTCGCCCGGTATCATCACAGAGAAAGTTCCATCGGAACTTTCCTATAACAAATTGTGCCTGAATGTGCAGACCCATGAATGTCTGTTAGACGGTGAGACTGTTTCTCTGACACCGACAGAGTTTTCTATCCTTCAGGTTCTTTTGGAAAGCACTGGGAATGTTGTAAGTATTGAGGAACTGTTTCATGCGGTTTGGAAAGATGAATACTACTCTAAAAACAGCAGCACAATTACTGTGAATATCCGGCATCTGCGTGAGAAACTGAAAGATACTTCCGATACTCCGCAGTATATTAAAACGATTTGGGGTGTTGGTTACAAAATTTAAGCGAAAGGAGTACGCTATGAAAAGAAAATCTAATTGCTTCGTAACCATTTTATTTTTAATTTATCTGGCACTCTTGGTTTGGATCATACTGTTCAAACTACAATTTTCAATCAGTGA



$ grep -c '^>'  HMP_GUT_SRS052697.25M.contigs.fa
140756
$ grep -c '^>'  HMP_GUT_SRS052697.25M.contigs_filted.fa
35677


$ grep  '^>'  HMP_GUT_SRS052697.25M.contigs_filted.fa | tail -n 5
>c_000000140733
>c_000000140738
>c_000000140740
>c_000000140750
>c_000000140752
```
```python
>>> 35677/140756
0.25346699252607346
```

 If you use the flag `--report-file`, it will also create a TAB-delimited file for you to keep track of which defline in the new file corresponds to which defline in the original file.
```bash
$ anvi-script-reformat-fasta HMP_GUT_SRS052697.25M.contigs.fa -o HMP_GUT_SRS052697.25M.contigs_filted.fa -l 1000  --report-file HMP_GUT_SRS052697.25M.contigs_report
Input ........................................: HMP_GUT_SRS052697.25M.contigs.fa
Output .......................................: HMP_GUT_SRS052697.25M.contigs_filted.fa
Minimum length ...............................: 1,000
Total num contigs ............................: 140,756
Total num nucleotides ........................: 213,146,787
Contigs removed ..............................: 105079 (74.65% of all)
Nucleotides removed ..........................: 52709581 (24.73% of all)
Deflines simplified ..........................: False

```

#### Filter contig with length > 1000 with original name 
```bash
$ anvi-script-reformat-fasta HMP_GUT_SRS052697.25M.contigs.fa -o HMP_GUT_SRS052697.25M.contigs_filted.fa -l 1000
```


#### Creating an anvi’o contigs database
An anvi’o contigs database will keep all the information related to your contigs: positions of open reading frames, k-mer frequencies for each contigs, where splits start and end, functional and taxonomic annotation of genes, etc. The contigs database is an essential component of everything related to anvi’o metagenomic workflow.
```bash
$ anvi-gen-contigs-database -f HMP_GUT_SRS052697.25M.contigs_filted.fa --split-length -1 --skip-gene-calling 
                                                                                                            

Config Error: At least one of the deflines in your FASTA File does not comply with the 'simple
              deflines' requirement of anvi'o. You can either use the script `anvi-script-    
              reformat-fasta` to take care of this issue, or read this section in the tutorial
              to understand the reason behind this requirement (anvi'o is very upset for      
              making you do this): http://merenlab.org/2016/06/22/anvio-tutorial-v2/#take-a   
              -look-at-your-fasta-file
```
it need 'simple deflines' name 
```bash
$ anvi-script-reformat-fasta HMP_GUT_SRS052697.25M.contigs.fa -o HMP_GUT_SRS052697.25M.contigs_filted.fa -l 1000  --simplify-names

$ anvi-gen-contigs-database -f HMP_GUT_SRS052697.25M.contigs_filted.fa --split-length -1 --skip-gene-calling 

Contigs database .............................: A new database, CONTIGS.db, has been created.               
Number of contigs ............................: 35,677
Number of splits .............................: 35,677
Total number of nucleotides ..................: 160,437,206
Gene calling step skipped ....................: True
Splits broke genes (non-mindful mode) ........: True
Desired split length (what the user wanted) ..: 9,223,372,036,854,775,807
Average split length (wnat anvi'o gave back) .: (Anvi'o did not create any splits)

```




* Compute k-mer frequencies for each contig (the default is 4, but you can change it using `--kmer-size` parameter if you feel adventurous).

* Soft-split contigs longer than 20,000 bp into smaller ones (you can change the split size using the `--split-length`). When gene calling step is not skipped, the process splitting contigs will consider where genes are and avoid cutting genes in the middle. For very very large assemblies this process can take a while, and you can skip it with `--skip-mindful-splitting` flag.

* Identify open reading frames using *Prodigal*, the bacterial and archaeal gene finding program developed at Oak Ridge National Laboratory and the University of Tennessee. If you don’t want gene calling to be done, you can use the flag `--skip-gene-calling` to skip it. If you have your own gene calls, you can provide them to be used to identify where genes are in your contigs. All you need to do is to use the parameter `--external-gene-calls` (see down below for the format).

output files (two binary files):
```
-rw-r--r-- 1 201M Nov  1 07:28 CONTIGS.db
-rw-r--r-- 1 6.1K Nov  1 07:28 CONTIGS.h5

```


The TAB-delimited file for `--external-gene-calls` should follow this format:
```
gene_callers_id contig  start   stop    direction   partial source  version
1   contig_01   1113    1677    f   0   program v1.0
2   contig_01   1698    2142    f   0   program v1.0
3   contig_01   2229    3447    f   0   program v1.0
4   contig_01   3439    6820    r   0   program v1.0
7   contig_01   8496    10350   r   1   program v1.0
8   contig_02   306 1650    f   0   program v1.0
9   contig_02   1971    3132    f   0   program v1.0
10  contig_02   3230    4007    f   0   program v1.0
11  contig_02   4080    5202    f   0   program v1.0
12  contig_02   5194    5926    f   0   program v1.0
13  contig_03   606 2514    f   0   program v1.0
14  contig_03   2751    3207    f   0   program v1.0
15  contig_03   3219    5616    f   0   program v1.0
16  contig_03   5720    6233    f   0   program v1.0
```

NOTES:
```
Please note: For a complete gene call where the value of partial is 0, the number of nucleotides, i.e. the value of stop - start, must be divided by three without any remainder. Any other gene call is not a complete gene call, and must be identified as such by setting the value of partial to 1 so anvi’o does not try to translate their sequence. Otherwise anvi’o will be upset, and then frustrate you.

Please note: anvi’o follows the convention of string indexing and splicing that is identical the way one does it in Python or C.
```


The statement above means that the index of the first nucleotide in any contig should be 0. In other words, we start counting from 0, not from 1. The start and stop positions in the input file should comply with this. Here is an example gene in a contig:

```
                 1         2         3
nt pos: 12345678901234567890123456789012 (...)
contig: NNNATGNNNNNNNNNNNNNNNNNTAGAAAAAA (...)
           |______ gene X _______|

```
The start and stop positions in the input file for this gene should be 3 and 26, respectively. If you think we should change this behavior, please let us know (here is a relevant issue). Thanks for your patience!



#### anvi-run-hmms
Although this is absolutely optional, you shouldn’t skip this step. Anvi’o can do a lot with hidden Markov models (HMMs provide statistical means to model complex data in probabilistic terms that can be used to search for patterns, which works beautifully in bioinformatics where we create models from known sequences, and then search for those patterns rapidly in a pool of unknown sequences to recover hits). To decorate your contigs database with hits from HMM models that ship with the platform (which, at this point, constitute multiple published bacterial single-copy gene collections), run this command:

```bash
$ anvi-run-hmms -c CONTIGS.db


Config Error: It seems the contigs database 'CONTIGS.db' was created with '--skip-gene-
              calling' flag. Nothing to do here :/                                     
```
it need the reult not using flag `--skip-gene-calling` in step of `anvi-gen-contigs-database`
```
$ anvi-gen-contigs-database -f HMP_GUT_SRS052697.25M.contigs_filted.fa --split-length -1


Config Error: Anvi'o will not overwrite an existing contigs database. Please choose a
              different name or remove the existing database ('CONTIGS.db') first. 
```
it need delete the original database
```
$ rm CONTIGS.db CONTIGS.h5

$ anvi-gen-contigs-database -f HMP_GUT_SRS052697.25M.contigs_filted.fa --split-length -1
                                                                                                            
Finding ORFs in contigs
===============================================
Genes ........................................: /tmp/tmpvEgprz/contigs.genes
Proteins .....................................: /tmp/tmpvEgprz/contigs.proteins
Log file .....................................: /tmp/tmpvEgprz/00_log.txt
Result .......................................: Prodigal (v2.6.3) has identified 165650 genes.              

Contigs with at least one gene call ..........: 35668 of 35677 (100.0%)                                     
Contigs database .............................: A new database, CONTIGS.db, has been created.
Number of contigs ............................: 35,677
Number of splits .............................: 35,677
Total number of nucleotides ..................: 160,437,206
Gene calling step skipped ....................: False
Splits broke genes (non-mindful mode) ........: False
Desired split length (what the user wanted) ..: 9,223,372,036,854,775,807
Average split length (wnat anvi'o gave back) .: (Anvi'o did not create any splits)
```
the predicted gene were added to file `CONTIGS.db` and `CONTIGS.h5`

```bash
$ anvi-run-hmms -c CONTIGS.db --num-threads 20
HMM profiles .................................: 2 sources have been loaded: Rinke_et_al (162 genes, domain: archaea), Campbell_et_al (139 genes, domain: bacteria)
Target found .................................: AA:GENE
Auxiliary Data ...............................: Found: CONTIGS.h5 (v. 1)                                    
Contigs DB ...................................: Initialized: CONTIGS.db (v. 8)
Sequences ....................................: 165650 sequences reported.                                  
FASTA ........................................: /tmp/tmpm6nMSj/aa_gene_sequences.fa

HMM Profiling for Rinke_et_al
===============================================
Reference ....................................: Rinke et al, http://www.nature.com/nature/journal/v499/n7459/full/nature12352.html
Kind .........................................: singlecopy
Target .......................................: AA:GENE
Domain .......................................: archaea
Pfam model ...................................: /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/anvio/data/hmm/Rinke_et_al/genes.hmm.gz
Number of genes ..............................: 162
Number of CPUs will be used for search .......: 20
Temporary work dir ...........................: /tmp/tmp1KI0jj
HMM scan output ..............................: /tmp/tmp1KI0jj/hmm.output
HMM scan hits ................................: /tmp/tmp1KI0jj/hmm.hits
Log file .....................................: /tmp/tmp1KI0jj/00_log.txt
Number of raw hits ...........................: 4,052                                                       

HMM Profiling for Campbell_et_al
===============================================
Reference ....................................: Campbell et al, http://www.pnas.org/content/110/14/5540.short
Kind .........................................: singlecopy
Target .......................................: AA:GENE
Domain .......................................: bacteria
Pfam model ...................................: /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/anvio/data/hmm/Campbell_et_al/genes.hmm.gz
Number of genes ..............................: 139
Number of CPUs will be used for search .......: 20
Temporary work dir ...........................: /tmp/tmplc6HIa
HMM scan output ..............................: /tmp/tmplc6HIa/hmm.output
HMM scan hits ................................: /tmp/tmplc6HIa/hmm.hits
Log file .....................................: /tmp/tmplc6HIa/00_log.txt
Number of raw hits ...........................: 6,483     
```
output was added to `CONTIGS.db`?


* It will utilize multiple default bacterial single-copy core gene collections and identify hits among your genes to those collections using HMMER. If you have already run this once, and now would like to add an HMM profile of your own, that is easy. You can use `--hmm-profile-dir` parameter to declare where should anvi’o look for it.

* Note that the program will use only one CPU by default, especially if you have multiple of them available to you, you should use the `--num-threads` parameter. It significantly improves the runtime, since *HMMER* is truly an awesome software.

####  take a quick look at the contig
```bash
$ anvi-script-gen_stats_for_single_copy_genes.py CONTIGS.db 
Contigs database .............................: An existing database, CONTIGS.db, has been initiated.
Number of contigs ............................: 35,677
Number of splits .............................: 35,677
Total number of nucleotides ..................: 160,437,206
Split length .................................: 9,223,372,036,854,775,807

```

output files:
```bash
$ head CONTIGS.db.genes
source  gene
Rinke_et_al Ribosomal_L37e
Rinke_et_al NAC
Rinke_et_al Enolase_C
Rinke_et_al Nop10p
Rinke_et_al Ribosomal_S8e
Rinke_et_al EIF_2_alpha
Rinke_et_al TIM
Rinke_et_al Prefoldin
Rinke_et_al Ribosomal_S3_C


$ head CONTIGS.db.hits
source  contig  gene    e_value
Rinke_et_al c_000000125876  Ribosomal_S13   6.5e-38
Rinke_et_al c_000000082663  CTP_synth_N 5.4e-118
Rinke_et_al c_000000043798  Ribosomal_L13   1.1e-54
Rinke_et_al c_000000047140  TIM 9.3e-94
Rinke_et_al c_000000111415  Ribosomal_S3_C  7.8e-40
Rinke_et_al c_000000076825  RNA_pol_Rpb1_3  1.3e-23
Rinke_et_al c_000000064483  Ribosomal_L6    2.3e-37
Rinke_et_al c_000000071179  DUF137  4.6e-10
Rinke_et_al c_000000110512  tRNA-synt_1c    4.2e-78
```
