## [BUSCO](https://busco.ezlab.org)

Assessing genome assembly and annotation completeness with
Benchmarking Universal Single-Copy Orthologs

### [BUSCO v3 source code](https://gitlab.com/ezlab/busco)

### install BUSCO
```
$ conda install -c bioconda busco
$ conda install -c bioconda/label/broken busco
```

### run busco
```
$ run_busco -i ERR2173372.fasta --out ERR2173372_busco -l /home/wzk/database/BUSCO/embryophyta_odb9  -m geno -c 30 
INFO    ****************** Start a BUSCO 3.0.2 analysis, current time: 03/22/2018 07:53:10 ******************
INFO    Configuration loaded from /home/wzk/anaconda3/envs/evolution/bin/../config/config.ini
INFO    Init tools...
INFO    Check dependencies...
INFO    Check input file...
INFO    To reproduce this run: python /home/wzk/anaconda3/envs/evolution/bin/run_busco -i ERR2173372.fasta -o ERR2173372_busco -l /home/wzk/database/BUSCO/embryophyta_odb9/ -m genome -c 30 -sp arabidopsis
INFO    Mode is: genome
INFO    The lineage dataset is: embryophyta_odb9 (eukaryota)
INFO    Temp directory is ./tmp/
INFO    ****** Phase 1 of 2, initial predictions ******
INFO    ****** Step 1/3, current time: 03/22/2018 07:53:11 ******
INFO    Create blast database...
INFO    [makeblastdb]   Building a new DB, current time: 03/22/2018 07:53:11
INFO    [makeblastdb]   New DB name:   /home/wzk/Project/AtGenome/pilon/ERR2173373/tmp/ERR2173372_busco_1288262795
INFO    [makeblastdb]   New DB title:  ERR2173372.fasta
INFO    [makeblastdb]   Sequence type: Nucleotide
INFO    [makeblastdb]   Keep Linkouts: T
INFO    [makeblastdb]   Keep MBits: T
INFO    [makeblastdb]   Maximum file size: 1000000000B
INFO    [makeblastdb]   Adding sequences from FASTA; added 62 sequences in 0.983689 seconds.
INFO    [makeblastdb]   1 of 1 task(s) completed at 03/22/2018 07:53:12
INFO    Running tblastn, writing output to /home/wzk/Project/AtGenome/pilon/ERR2173373/run_ERR2173372_busco/blast_output/tblastn_ERR2173372_busco.tsv..
INFO    [tblastn]   1 of 1 task(s) completed at 03/22/2018 07:58:01
INFO    ****** Step 2/3, current time: 03/22/2018 07:58:02 ******
INFO    Maximum number of candidate contig per BUSCO limited to: 3
INFO    Getting coordinates for candidate regions...
INFO    Pre-Augustus scaffold extraction...
INFO    Running Augustus prediction using arabidopsis as species:
INFO    [augustus]  Please find all logs related to Augustus errors here: /home/wzk/Project/AtGenome/pilon/ERR2173373/run_ERR2173372_busco/augustus_output/augustus.log
INFO    [augustus]  224 of 2232 task(s) completed at 03/22/2018 08:00:27
INFO    [augustus]  447 of 2232 task(s) completed at 03/22/2018 08:02:29
INFO    [augustus]  670 of 2232 task(s) completed at 03/22/2018 08:04:19
INFO    [augustus]  893 of 2232 task(s) completed at 03/22/2018 08:05:55
INFO    [augustus]  1116 of 2232 task(s) completed at 03/22/2018 08:07:20
INFO    [augustus]  1340 of 2232 task(s) completed at 03/22/2018 08:08:19
INFO    [augustus]  1563 of 2232 task(s) completed at 03/22/2018 08:09:06
INFO    [augustus]  1786 of 2232 task(s) completed at 03/22/2018 08:09:45
INFO    [augustus]  2009 of 2232 task(s) completed at 03/22/2018 08:10:20
INFO    [augustus]  2232 of 2232 task(s) completed at 03/22/2018 08:10:44
INFO    Extracting predicted proteins...
INFO    ****** Step 3/3, current time: 03/22/2018 08:10:53 ******
INFO    Running HMMER to confirm orthology of predicted proteins:
INFO    [hmmsearch] 888 of 2218 task(s) completed at 03/22/2018 08:10:56
INFO    [hmmsearch] 1331 of 2218 task(s) completed at 03/22/2018 08:10:57
INFO    [hmmsearch] 1553 of 2218 task(s) completed at 03/22/2018 08:10:58
INFO    [hmmsearch] 1997 of 2218 task(s) completed at 03/22/2018 08:10:59
INFO    [hmmsearch] 2218 of 2218 task(s) completed at 03/22/2018 08:10:59
INFO    Results:
INFO    C:96.9%[S:95.9%,D:1.0%],F:0.8%,M:2.3%,n:1440
INFO    1396 Complete BUSCOs (C)
INFO    1381 Complete and single-copy BUSCOs (S)
INFO    15 Complete and duplicated BUSCOs (D)
INFO    12 Fragmented BUSCOs (F)
INFO    32 Missing BUSCOs (M)
INFO    1440 Total BUSCO groups searched
INFO    ****** Phase 2 of 2, predictions using species specific training ******
INFO    ****** Step 1/3, current time: 03/22/2018 08:11:00 ******
INFO    Extracting missing and fragmented buscos from the ancestral_variants file...
INFO    Running tblastn, writing output to /home/wzk/Project/AtGenome/pilon/ERR2173373/run_ERR2173372_busco/blast_output/tblastn_ERR2173372_busco_missing_and_frag_rerun.tsv...
INFO    [tblastn]   1 of 1 task(s) completed at 03/22/2018 08:13:44
INFO    Maximum number of candidate contig per BUSCO limited to: 3
INFO    Getting coordinates for candidate regions...
INFO    ****** Step 2/3, current time: 03/22/2018 08:13:45 ******
INFO    Training Augustus using Single-Copy Complete BUSCOs:
INFO    Converting predicted genes to short genbank files at 03/22/2018 08:13:45...
INFO    All files converted to short genbank files, now running the training scripts at 03/22/2018 08:14:23...
INFO    Pre-Augustus scaffold extraction...
INFO    Re-running Augustus with the new metaparameters, number of target BUSCOs: 44
INFO    [augustus]  10 of 97 task(s) completed at 03/22/2018 08:14:31
INFO    [augustus]  20 of 97 task(s) completed at 03/22/2018 08:14:33
INFO    [augustus]  30 of 97 task(s) completed at 03/22/2018 08:14:35
INFO    [augustus]  39 of 97 task(s) completed at 03/22/2018 08:14:38
INFO    [augustus]  49 of 97 task(s) completed at 03/22/2018 08:14:42
INFO    [augustus]  59 of 97 task(s) completed at 03/22/2018 08:14:45
INFO    [augustus]  68 of 97 task(s) completed at 03/22/2018 08:14:48
INFO    [augustus]  78 of 97 task(s) completed at 03/22/2018 08:14:49
INFO    [augustus]  88 of 97 task(s) completed at 03/22/2018 08:14:52
INFO    [augustus]  97 of 97 task(s) completed at 03/22/2018 08:15:20
INFO    Extracting predicted proteins...
INFO    ****** Step 3/3, current time: 03/22/2018 08:15:20 ******
INFO    Running HMMER to confirm orthology of predicted proteins:
INFO    [hmmsearch] 20 of 97 task(s) completed at 03/22/2018 08:15:20
INFO    [hmmsearch] 30 of 97 task(s) completed at 03/22/2018 08:15:20
INFO    [hmmsearch] 39 of 97 task(s) completed at 03/22/2018 08:15:20
INFO    [hmmsearch] 78 of 97 task(s) completed at 03/22/2018 08:15:20
INFO    [hmmsearch] 97 of 97 task(s) completed at 03/22/2018 08:15:21
INFO    Results:
INFO    C:97.5%[S:96.5%,D:1.0%],F:0.8%,M:1.7%,n:1440
INFO    1404 Complete BUSCOs (C)
INFO    1389 Complete and single-copy BUSCOs (S)
INFO    15 Complete and duplicated BUSCOs (D)
INFO    12 Fragmented BUSCOs (F)
INFO    24 Missing BUSCOs (M)
INFO    1440 Total BUSCO groups searched
INFO    BUSCO analysis done. Total running time: 1331.500517129898 seconds
INFO    Results written in /home/wzk/Project/AtGenome/pilon/ERR2173373/run_ERR2173372_busco/


```


output files:

```
$ tree -L 1 run_ERR2173372_busco/
run_ERR2173372_busco/
├── augustus_output/
├── blast_output/
├── full_table_ERR2173372_busco.tsv
├── hmmer_output/
├── missing_busco_list_ERR2173372_busco.tsv
├── short_summary_ERR2173372_busco.txt
└── single_copy_busco_sequences/
```

summary files:
```
$ head full_table_ERR2173372_busco.tsv
# BUSCO version is: 3.0.2 
# The lineage dataset is: embryophyta_odb9 (Creation date: 2016-02-13, number of species: 30, number of BUSCOs: 1440)
# To reproduce this run: python /home/wzk/anaconda3/envs/evolution/bin/run_busco -i ERR2173372.fasta -o ERR2173372_busco -l /home/wzk/database/BUSCO/embryophyta_odb9/ -m genome -c 30 -sp arabidopsis
#
# Busco id  Status  Contig  Start   End Score   Length
EOG09360002 Complete    1.000000_pilon  11842543    11860272    6909.6  3893
EOG0936000A Complete    1.000000_pilon  7797278 7814659 7112.5  4133
EOG0936001N Complete    1.000000_pilon  4260986 4271147 3937.1  2274
EOG0936001W Complete    1.000000_pilon  2923289 2931281 2684.5  1669
EOG09360025 Complete    1.000000_pilon  3266184 3278193 2989.4  1661


$ head missing_busco_list_ERR2173372_busco.tsv
# BUSCO version is: 3.0.2 
# The lineage dataset is: embryophyta_odb9 (Creation date: 2016-02-13, number of species: 30, number of BUSCOs: 1440)
# To reproduce this run: python /home/wzk/anaconda3/envs/evolution/bin/run_busco -i ERR2173372.fasta -o ERR2173372_busco -l /home/wzk/database/BUSCO/embryophyta_odb9/ -m genome -c 30 -sp arabidopsis
#
EOG093600UX
EOG093601AL
EOG093602OJ
EOG09360353
EOG093603UO
EOG093603VZ


$ cat  short_summary_ERR2173372_busco.txt
# BUSCO version is: 3.0.2 
# The lineage dataset is: embryophyta_odb9 (Creation date: 2016-02-13, number of species: 30, number of BUSCOs: 1440)
# To reproduce this run: python /home/wzk/anaconda3/envs/evolution/bin/run_busco -i ERR2173372.fasta -o ERR2173372_busco -l /home/wzk/database/BUSCO/embryophyta_odb9/ -m genome -c 30 -sp arabidopsis
#
# Summarized benchmarking in BUSCO notation for file ERR2173372.fasta
# BUSCO was run in mode: genome

    C:97.5%[S:96.5%,D:1.0%],F:0.8%,M:1.7%,n:1440

    1404    Complete BUSCOs (C)
    1389    Complete and single-copy BUSCOs (S)
    15  Complete and duplicated BUSCOs (D)
    12  Fragmented BUSCOs (F)
    24  Missing BUSCOs (M)
    1440    Total BUSCO groups searched

```


### BUSCO specific configuration
```
# BUSCO specific configuration
# It overrides default values in code and dataset cfg, and is overridden by arguments in command line
# Uncomment lines when appropriate
[busco]
# Input file
;in = ./sample_data/target.fa
# Run name, used in output files and folder
;out = SAMPLE
# Where to store the output directory
;out_path = ./sample_data
# Path to the BUSCO dataset
;lineage_path = ./sample_data/example
# Which mode to run (genome / protein / transcriptome)
;mode = genome
# How many threads to use for multithreaded steps
;cpu = 1
# Domain for augustus retraining, eukaryota or prokaryota
# Do not change this unless you know exactly why !!!
;domain = eukaryota
# Force rewrite if files already exist (True/False)
;force = False
# Restart mode (True/False)
;restart = False
# Blast e-value
;evalue = 1e-3
# Species to use with augustus, for old datasets only
;species = fly
# Augustus extra parameters
# Use single quotes, like this: '--param1=1 --param2=2'
;augustus_parameters = ''
# Tmp folder
;tmp_path = ./tmp/
# How many candidate regions (contigs, scaffolds) to consider for each BUSCO
;limit = 3
# Augustus long mode for retraining (True/False)
;long = False
# Quiet mode (True/False)
;quiet = False
# Debug logs (True/False), it needs Quiet to be False
;debug = True
# tar gzip output files (True/False)
;gzip = False
# Force single core for the tblastn step
;blast_single_core = True


[tblastn]
# path to tblastn
path = /home/wzk/anaconda3/envs/evolution/bin/

[makeblastdb]
# path to makeblastdb
path = /home/wzk/anaconda3/envs/evolution/bin/

[augustus]
# path to augustus
path = /home/wzk/anaconda3/envs/evolution/bin/

[etraining]
# path to augustus etraining
path = /home/wzk/anaconda3/envs/evolution/bin/

# path to augustus perl scripts, redeclare it for each new script
[gff2gbSmallDNA.pl]
path = /home/wzk/anaconda3/envs/evolution/bin/
[new_species.pl]
path = /home/wzk/anaconda3/envs/evolution/bin/
[optimize_augustus.pl]
path = /home/wzk/anaconda3/envs/evolution/bin/

[hmmsearch]
# path to HMMsearch executable
path = /home/wzk/anaconda3/envs/evolution/bin/

[Rscript]
# path to Rscript, if you wish to use the plot tool
path = /home/wzk/anaconda3/envs/evolution/bin/

```

