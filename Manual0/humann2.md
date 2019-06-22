## [HUMAnN2: The HMP Unified Metabolic Analysis Network 2](http://huttenhower.sph.harvard.edu/humann2)

### [humann2 manual](https://bitbucket.org/biobakery/humann2/wiki/Home#markdown-header-download-a-translated-search-database)

### install humann2
```
$ conda install -c bioconda humann2 
```



### humann2 parameters
```
$ humann2 -h
usage: humann2 [-h] [--version] [-v] [-r] [--bypass-prescreen]
               [--bypass-nucleotide-index] [--bypass-translated-search]
               [--bypass-nucleotide-search] -i <input.fastq> -o <output>
               [--nucleotide-database <nucleotide_database>]
               [--annotation-gene-index <8>]
               [--protein-database <protein_database>] [--evalue <1.0>]
               [--search-mode {uniref50,uniref90}] [--metaphlan <metaphlan>]
               [--metaphlan-options <metaphlan_options>]
               [--o-log <sample.log>]
               [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
               [--remove-temp-output] [--threads <1>]
               [--prescreen-threshold <0.01>] [--identity-threshold <50.0>]
               [--translated-subject-coverage-threshold <50.0>]
               [--translated-query-coverage-threshold <90.0>]
               [--bowtie2 <bowtie2>] [--usearch <usearch>]
               [--rapsearch <rapsearch>] [--diamond <diamond>]
               [--taxonomic-profile <taxonomic_profile.tsv>]
               [--id-mapping <id_mapping.tsv>]
               [--translated-alignment {usearch,rapsearch,diamond}]
               [--xipe {on,off}] [--minpath {on,off}] [--pick-frames {on,off}]
               [--gap-fill {on,off}] [--output-format {tsv,biom}]
               [--output-max-decimals <10>] [--output-basename <sample_name>]
               [--remove-stratified-output]
               [--remove-column-description-output]
               [--input-format {fastq,fastq.gz,fasta,fasta.gz,sam,bam,blastm8,genetable,biom}]
               [--pathways-database <pathways_database.tsv>]
               [--pathways {metacyc,unipathway}]
               [--memory-use {minimum,maximum}]

HUMAnN2 : HMP Unified Metabolic Analysis Network 2

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         additional output is printed
  -r, --resume          bypass commands if the output files exist
  --bypass-prescreen    bypass the prescreen step and run on the full ChocoPhlAn database
  --bypass-nucleotide-index
                        bypass the nucleotide index step and run on the indexed ChocoPhlAn database
  --bypass-translated-search
                        bypass the translated search step
  --bypass-nucleotide-search
                        bypass the nucleotide search steps
  -i <input.fastq>, --input <input.fastq>
                        input file of type {fastq,fastq.gz,fasta,fasta.gz,sam,bam,blastm8,genetable,biom} 
                        [REQUIRED]
  -o <output>, --output <output>
                        directory to write output files
                        [REQUIRED]
  --nucleotide-database <nucleotide_database>
                        directory containing the nucleotide database
                        [DEFAULT: /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/data/chocophlan_DEMO]
  --annotation-gene-index <8>
                        the index of the gene in the sequence annotation
                        [DEFAULT: 8]
  --protein-database <protein_database>
                        directory containing the protein database
                        [DEFAULT: /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/data/uniref_DEMO]
  --evalue <1.0>        the evalue threshold to use with the translated search
                        [DEFAULT: 1.0]
  --search-mode {uniref50,uniref90}
                        search for uniref50 or uniref90 gene families
                        [DEFAULT: based on translated database selected]
  --metaphlan <metaphlan>
                        directory containing the MetaPhlAn software
                        [DEFAULT: $PATH]
  --metaphlan-options <metaphlan_options>
                        options to be provided to the MetaPhlAn software
                        [DEFAULT: "-t rel_ab"]
  --o-log <sample.log>  log file
                        [DEFAULT: temp/sample.log]
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        level of messages to display in log
                        [DEFAULT: DEBUG]
  --remove-temp-output  remove temp output files
                        [DEFAULT: temp files are not removed]
  --threads <1>         number of threads/processes
                        [DEFAULT: 1]
  --prescreen-threshold <0.01>
                        minimum percentage of reads matching a species
                        [DEFAULT: 0.01]
  --identity-threshold <50.0>
                        identity threshold for alignments
                        [DEFAULT: 50.0]
  --translated-subject-coverage-threshold <50.0>
                        subject coverage threshold for translated alignments
                        [DEFAULT: 50.0]
  --translated-query-coverage-threshold <90.0>
                        query coverage threshold for translated alignments
                        [DEFAULT: 90.0]
  --bowtie2 <bowtie2>   directory containing the bowtie2 executable
                        [DEFAULT: $PATH]
  --usearch <usearch>   directory containing the usearch executable
                        [DEFAULT: $PATH]
  --rapsearch <rapsearch>
                        directory containing the rapsearch executable
                        [DEFAULT: $PATH]
  --diamond <diamond>   directory containing the diamond executable
                        [DEFAULT: $PATH]
  --taxonomic-profile <taxonomic_profile.tsv>
                        a taxonomic profile (the output file created by metaphlan)
                        [DEFAULT: file will be created]
  --id-mapping <id_mapping.tsv>
                        id mapping file for alignments
                        [DEFAULT: alignment reference used]
  --translated-alignment {usearch,rapsearch,diamond}
                        software to use for translated alignment
                        [DEFAULT: diamond]
  --xipe {on,off}       turn on/off the xipe computation
                        [DEFAULT: off]
  --minpath {on,off}    turn on/off the minpath computation
                        [DEFAULT: on]
  --pick-frames {on,off}
                        turn on/off the pick_frames computation
                        [DEFAULT: off]
  --gap-fill {on,off}   turn on/off the gap fill computation
                        [DEFAULT: on]
  --output-format {tsv,biom}
                        the format of the output files
                        [DEFAULT: tsv]
  --output-max-decimals <10>
                        the number of decimals to output
                        [DEFAULT: 10]
  --output-basename <sample_name>
                        the basename for the output files
                        [DEFAULT: input file basename]
  --remove-stratified-output
                        remove stratification from output
                        [DEFAULT: output is stratified]
  --remove-column-description-output
                        remove the description in the output column
                        [DEFAULT: output column includes description]
  --input-format {fastq,fastq.gz,fasta,fasta.gz,sam,bam,blastm8,genetable,biom}
                        the format of the input file
                        [DEFAULT: format identified by software]
  --pathways-database <pathways_database.tsv>
                        mapping file (or files, at most two in a comma-delimited list) to use for pathway computations
                        [DEFAULT: metacyc database ]
  --pathways {metacyc,unipathway}
                        the database to use for pathway computations
                        [DEFAULT: metacyc]
  --memory-use {minimum,maximum}
                        the amount of memory to use
                        [DEFAULT: minimum]

```


### database

#### available database

```
$ humann2_databases --available
HUMANnN2 Databases ( database : build = location )
utility_mapping : full = http://huttenhower.sph.harvard.edu/humann2_data/full_mapping_1_1.tar.gz
chocophlan : DEMO = http://huttenhower.sph.harvard.edu/humann2_data/chocophlan/DEMO_chocophlan.v0.1.1.tar.gz
chocophlan : full = http://huttenhower.sph.harvard.edu/humann2_data/chocophlan/full_chocophlan_plus_viral.v0.1.1.tar.gz
uniref : DEMO_diamond = http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_annotated/uniref90_DEMO_diamond.tar.gz
uniref : uniref90_diamond = http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_annotated/uniref90_annotated_1_1.tar.gz
uniref : uniref50_ec_filtered_diamond = http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_ec_filtered/uniref50_ec_filtered_1_1.tar.gz
uniref : uniref50_GO_filtered_rapsearch2 = http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref50_GO_filtered/uniref50_GO_filtered_rapsearch2.tar.gz
uniref : uniref50_diamond = http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_annotated/uniref50_annotated_1_1.tar.gz
uniref : uniref90_ec_filtered_diamond = http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_ec_filtered/uniref90_ec_filtered_1_1.tar.gz

```

#### ChocoPhlAn database

```
$ cd /home/wzk/database/ChocoPhlAn/chocophlan && $ ls *gz | wc -l
4187

$ less g__Zymoseptoria.s__Zymoseptoria_tritici.centroids.ffn.m8.gz

>gi|398395178|ref|XM_003851000.1||1047171|g__Zymoseptoria.s__Zymoseptoria_tritici|UniRef90_unknown|UniRef50_M2R0U3
TTCATTCGGCAGGTGAGTTGTTACACACTCCTTAGCGGATTCCGACTTCCATGGCCACCGTCCTGCTGTCTAGATGAACT
AACACCTTTTGTGGTGTCTGATGAGCGTACATTCCGGCACCTTAACCTCGCGTTCGGTTCATCCCGCATCGCCAGTTCTG
CTTACCAAAAATGGCCCACTAGTAACGATACATTCAAATGTCCACGACTTCTTACATATTTAAAGTTTGAGAATAGGTTA
AGGTTGTTTCAACCCCAAGGCCTCTAA
>gi|398395184|ref|XM_003851003.1||1047171|g__Zymoseptoria.s__Zymoseptoria_tritici|UniRef90_F9XGI9|UniRef50_E1Z6Z7
CGCTTCCCTTTCAACAATTTCACGTGCTTTTTAACTCTCTTTCCAAAGTGCTTTTCATCTTTCGATCACTCTACTTGTGC
GCTATCGGTCTCTGGCCGGTATTTAGCTTTAGAAGAAATTTACCTCCCATTTAGAGCTGCATTCCCAAACAACTCGACTC
GTCGAAGGAGCTACGTGGAGGGCGCGGGCCGGTCGCATACGGGATTCTCACCCTCTATGACGTCCTGTTCCAAGGAACTT

```

#### translated search database

```
$ humann2_databases --download uniref uniref90_diamond /home/wzk/database/humann2/uniref90

Creating subdirectory to install database: /home/wzk/database/humann2/uniref
Download URL: http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_annotated/uniref90_annotated_1_1.tar.gz
Downloading file of size: 5.87 GB
```

```
$ humann2_databases --download uniref uniref90_ec_filtered_diamond /home/wzk/database/humann2/uniref90
```


pathway

```
(evolution) wzk@ubuntu 21:34:13 ^_^ /home/wzk/Project/C100 
$ cp /home/wzk/anaconda3/pkgs/humann2-0.11.1-py27_3/lib/python2.7/site-packages/humann2/data/pathways/metacyc_reactions_level4ec_only.uniref.bz2 /home/wzk/database/HUMAnN2/metacyc_uniref
(evolution) wzk@ubuntu 21:35:11 ^_^ /home/wzk/Project/C100 
$ cp /home/wzk/anaconda3/pkgs/humann2-0.11.1-py27_3/lib/python2.7/site-packages/humann2/data/pathways/metacyc_pathways_structured /home/wzk/database/HUMAnN2/metacyc_uniref
```



#### download database through harvard

database directory
```
http://huttenhower.sph.harvard.edu/humann2_data/chocophlan/
http://huttenhower.sph.harvard.edu/humann2_data/uniprot/
http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_ec_filtered/
```


```
$ humann2_databases --download chocophlan full /home/wzk/database/HUMAnN2

Creating subdirectory to install database: /home/wzk/database/HUMAnN2/chocophlan
Download URL: http://huttenhower.sph.harvard.edu/humann2_data/chocophlan/full_chocophlan_plus_viral.v0.1.1.tar.gz

$ humann2_databases --download uniref uniref90_ec_filtered_diamond /home/wzk/database/HUMAnN2

$ humann2_databases --download uniref uniref90_diamond /home/wzk/database/HUMAnN2

$ humann2_databases --download utility_mapping full /home/wzk/database/HUMAnN2
```

or 
```
wget http://huttenhower.sph.harvard.edu/humann2_data/chocophlan/full_chocophlan_plus_viral.v0.1.1.tar.gz

wget http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_ec_filtered/uniref90_ec_filtered_1_1.tar.gz

wget http://huttenhower.sph.harvard.edu/humann2_data/uniprot/uniref_annotated/uniref90_annotated_1_1.tar.gz

wget http://huttenhower.sph.harvard.edu/humann2_data/uniprot/idmapping/map_uniprot_UniRef90.dat.gz
```


### [Humann2 config](https://groups.google.com/forum/#!topic/humann-users/MF--EoXQRnU)

Run config settings:
```
 

DATABASE SETTINGS 
nucleotide database folder = /data/home/bioinfo/nsher/programs/humann2_v0.2.1/db/chocophlan 
protein database folder = /data/home/bioinfo/nsher/programs/humann2_v0.2.1/db/uniref 
pathways database file 1 = /data/home/bioinfo/nsher/.local/lib/python2.7/site-packages/humann2-0.2.1-py2.7.egg/humann2/data/pathways/metacyc_reactions.uniref 
pathways database file 2 = /data/home/bioinfo/nsher/.local/lib/python2.7/site-packages/humann2-0.2.1-py2.7.egg/humann2/data/pathways/metacyc_pathways_structured_filtered 

RUN MODES 
resume = False 
verbose = False 
bypass prescreen = False 
bypass nucleotide index = False 
bypass nucleotide search = False 
bypass translated search = False 
translated search = diamond 
pick frames = off 
threads = 20 

ALIGNMENT SETTINGS 
evalue threshold = 1.0 
average read length = 1 
prescreen threshold = 0.01 
identity threshold = 40.0 

PATHWAYS SETTINGS 
minpath = on 
xipe = off 

INPUT AND OUTPUT FORMATS 
input file format = fastq 
output file format = tsv 
output max decimals = 10 
remove stratified output = False 
log level = DEBUG 
```


### configuration

```
$ humann2_config --print
HUMAnN2 Configuration ( Section : Name = Value )
output_format : remove_stratified_output = False
output_format : output_max_decimals = 10
output_format : remove_column_description_output = False
alignment_settings : prescreen_threshold = 0.01
alignment_settings : translated_query_coverage_threshold = 90.0
alignment_settings : evalue_threshold = 1.0
alignment_settings : translated_subject_coverage_threshold = 50.0
database_folders : utility_mapping = /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/data/misc
database_folders : protein = /home/wzk/database/humann2/uniref
database_folders : nucleotide = /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/data/chocophlan_DEMO
run_modes : bypass_nucleotide_search = False
run_modes : verbose = False
run_modes : bypass_nucleotide_index = False
run_modes : bypass_translated_search = False
run_modes : resume = False
run_modes : threads = 1
run_modes : bypass_prescreen = False

```


#### change a value in the configuration file
```
$ humann2_config --update run_modes threads 5
HUMAnN2 configuration file updated: run_modes : threads = 5
```


### run humann2

```
$ humann2 --input synthetic_dna_human_gut.1.fq.gz --nucleotide-database   /home/wzk/database/ChocoPhlAn/chocophlan  --protein-database  /home/wzk/database/humann2/uniref   --output humann2_result --threads 10  --o-log run.log 
Output files will be written to: /home/wzk/Project/humann2_test/humann2_result
Decompressing gzipped file ...


Running metaphlan2.py ........

Found g__Alistipes.s__Alistipes_onderdonkii : 29.81% of mapped reads
Found g__Alistipes.s__Alistipes_putredinis : 19.60% of mapped reads
Found g__Alistipes.s__Alistipes_shahii : 14.89% of mapped reads
Found g__Bacteroides.s__Bacteroides_caccae : 10.70% of mapped reads
Found g__Bacteroides.s__Bacteroides_cellulosilyticus : 7.53% of mapped reads
Found g__Bacteroides.s__Bacteroides_dorei : 5.13% of mapped reads
Found g__Bacteroides.s__Bacteroides_massiliensis : 3.71% of mapped reads
Found g__Bacteroides.s__Bacteroides_ovatus : 2.53% of mapped reads
Found g__Bacteroides.s__Bacteroides_stercoris : 1.91% of mapped reads
Found g__Bacteroides.s__Bacteroides_thetaiotaomicron : 1.31% of mapped reads
Found g__Bacteroides.s__Bacteroides_uniformis : 0.90% of mapped reads
Found g__Bacteroides.s__Bacteroides_vulgatus : 0.68% of mapped reads
Found g__Barnesiella.s__Barnesiella_intestinihominis : 0.48% of mapped reads
Found g__Dialister.s__Dialister_invisus : 0.31% of mapped reads
Found g__Eubacterium.s__Eubacterium_rectale : 0.22% of mapped reads
Found g__Faecalibacterium.s__Faecalibacterium_prausnitzii : 0.07% of mapped reads
Found g__Parabacteroides.s__Parabacteroides_distasonis : 0.07% of mapped reads
Found g__Parabacteroides.s__Parabacteroides_merdae : 0.07% of mapped reads
Found g__Prevotella.s__Prevotella_copri : 0.05% of mapped reads
Found g__Ruminococcus.s__Ruminococcus_bromii : 0.04% of mapped reads

Total species selected from prescreen: 20

Selected species explain 100.00% of predicted community composition


Creating custom ChocoPhlAn database ........


Running bowtie2-build ........


Running bowtie2 ........

Traceback (most recent call last):
  File "/home/wzk/anaconda3/envs/qiime/bin/humann2", line 11, in <module>
    sys.exit(main())
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/humann2.py", line 927, in main
    nucleotide_alignment_file, alignments, unaligned_reads_store, keep_sam=True)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/search/nucleotide.py", line 257, in unaligned_reads
    if int(info[config.sam_flag_index]) & config.sam_unmapped_flag != 0:
IndexError: list index out of range

```

### run humann2 using sam files


```
$ humann2 --input SP1.sam  --nucleotide-database /home/wzk/database/ChocoPhlAn/chocophlan  --protein-database  /home/wzk/database/HUMAnN2/ --output temp
Creating output directory: /home/wzk/Project/metagenome/MetaPhlAn/mapping/temp
Output files will be written to: /home/wzk/Project/metagenome/MetaPhlAn/mapping/temp

Process the sam mapping results ...

Computing gene families ...

Computing pathways abundance and coverage ...

Output files created: 
/home/wzk/Project/metagenome/MetaPhlAn/mapping/temp/SP1_genefamilies.tsv
/home/wzk/Project/metagenome/MetaPhlAn/mapping/temp/SP1_pathabundance.tsv
/home/wzk/Project/metagenome/MetaPhlAn/mapping/temp/SP1_pathcoverage.tsv

```


or

```
$ humann2 --input-format sam --input SP1.sam  --nucleotide-database /home/wzk/database/ChocoPhlAn/chocophlan  --protein-database  /home/wzk/database/HUMAnN2/uniref90  --output temp_temp  --search-mode uniref90 --pathways-database /home/wzk/database/HUMAnN2/uniref90_ec/uniref90.ec_filtered.1.1.dmnd
```


output files
```
$ head /home/wzk/Project/metagenome/MetaPhlAn/mapping/temp/SP1_genefamilies.tsv
# Gene Family   SP1_Abundance-RPKs
UNMAPPED    1935440.0000000000
gi|421568039|ref|NZ_ALYA01000017.1|:37498-38388 726.1567106948
gi|421568039|ref|NZ_ALYA01000017.1|:37498-38388|unclassified    726.1567106948
gi|433516503|ref|NZ_ANRW01000019.1|:572-1684    626.9224494163
gi|433516503|ref|NZ_ANRW01000019.1|:572-1684|unclassified   626.9224494163
gi|161869018|ref|NC_010120.1|:c1549712-1548879  562.0617103147
gi|161869018|ref|NC_010120.1|:c1549712-1548879|unclassified 562.0617103147
gi|320117067|ref|NZ_GL636062.1|:c2831888-2827800    375.3510905524
gi|320117067|ref|NZ_GL636062.1|:c2831888-2827800|unclassified   375.3510905524


$ head /home/wzk/Project/metagenome/MetaPhlAn/mapping/temp/SP1_pathabundance.tsv
# Pathway   SP1_Abundance
UNMAPPED    0.0000000000
UNINTEGRATED    0.0000000000


$ head /home/wzk/Project/metagenome/MetaPhlAn/mapping/temp/SP1_pathcoverage.tsv
# Pathway   SP1_Coverage
UNMAPPED    1.0000000000
UNINTEGRATED    1.0000000000
```



#### run test data

#####  get test data
```
$ locate demo.fastq
/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/tests/data/demo.fastq
/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/kneaddata/tests/data/demo.fastq
/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/kneaddata/tests/data/demo.fastq.gz

```


#### run humann2 for test data
```
$ humann2 --input /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/tests/data/demo.fastq --output humann2_result
Creating output directory: /home/wzk/Project/humann2_test/humann2_result
Output files will be written to: /home/wzk/Project/humann2_test/humann2_result

Running metaphlan2.py ........

Found g__Bacteroides.s__Bacteroides_dorei : 59.40% of mapped reads
Found g__Bacteroides.s__Bacteroides_vulgatus : 40.60% of mapped reads

Total species selected from prescreen: 2

Selected species explain 100.00% of predicted community composition


Creating custom ChocoPhlAn database ........


Running bowtie2-build ........


Running bowtie2 ........

Total bugs from nucleotide alignment: 2
g__Bacteroides.s__Bacteroides_vulgatus: 7336 hits
g__Bacteroides.s__Bacteroides_dorei: 8820 hits

Total gene families from nucleotide alignment: 3685

Unaligned reads after nucleotide alignment: 23.0666666667 %


Running diamond ........


Aligning to reference database: uniref90_annotated.1.1.dmnd

CRITICAL ERROR: Error executing: /home/wzk/anaconda3/envs/qiime/bin/diamond blastx --query /home/wzk/Project/humann2_test/humann2_result/demo_humann2_temp/demo_bowtie2_unaligned.fa --evalue 1.0 --threads 1 --max-target-seqs 20 --outfmt 6 --db /home/wzk/database/humann2/uniref/uniref90_annotated.1.1 --out /home/wzk/Project/humann2_test/humann2_result/demo_humann2_temp/tmpoJg3f8/diamond_m8_XlM56o --tmpdir /home/wzk/Project/humann2_test/humann2_result/demo_humann2_temp/tmpoJg3f8

Error message returned from diamond :
diamond v0.9.10.111 | by Benjamin Buchfink <buchfink@gmail.com>
Licensed under the GNU AGPL <https://www.gnu.org/licenses/agpl.txt>
Check http://github.com/bbuchfink/diamond for updates.

#CPU threads: 1
Scoring parameters: (Matrix=BLOSUM62 Lambda=0.267 K=0.041 Penalties=11/1)
#Target sequences to report alignments for: 20
Temporary directory: /home/wzk/Project/humann2_test/humann2_result/demo_humann2_temp/tmpoJg3f8
Opening the database...  [0.054509s]
Error: Database was built with a different version of diamond as is incompatible.
```



#### **humann2 v0.11.2 uses diamond verison 0.8.22**

get **diamond** with version of 0.8.22
```
$ /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/bin/diamond --version
diamond version 0.8.22

```


#### run humann2
```
$ humann2 --input /home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/humann2/tests/data/demo.fastq  --nucleotide-database   /home/wzk/database/ChocoPhlAn/chocophlan  --protein-database  /home/wzk/database/humann2/uniref   --output humann2_result --threads 10  --o-log run.log --diamond /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/bin/
Output files will be written to: /home/wzk/Project/humann2_test/humann2_result

Running metaphlan2.py ........

Found g__Bacteroides.s__Bacteroides_dorei : 59.40% of mapped reads
Found g__Bacteroides.s__Bacteroides_vulgatus : 40.60% of mapped reads

Total species selected from prescreen: 2

Selected species explain 100.00% of predicted community composition


Creating custom ChocoPhlAn database ........


Running bowtie2-build ........


Running bowtie2 ........

Total bugs from nucleotide alignment: 2
g__Bacteroides.s__Bacteroides_vulgatus: 7407 hits
g__Bacteroides.s__Bacteroides_dorei: 8895 hits

Total gene families from nucleotide alignment: 3685

Unaligned reads after nucleotide alignment: 23.0666666667 %


Running diamond ........


Aligning to reference database: uniref90_annotated.1.1.dmnd


Aligning to reference database: uniref90.ec_filtered.1.1.dmnd

Total bugs after translated alignment: 3
g__Bacteroides.s__Bacteroides_vulgatus: 7407 hits
unclassified: 2060 hits
g__Bacteroides.s__Bacteroides_dorei: 8895 hits

Total gene families after translated alignment: 3787

Unaligned reads after translated alignment: 18.2333333333 %


Computing gene families ...

Computing pathways abundance and coverage ...

Output files created: 
/home/wzk/Project/humann2_test/humann2_result/demo_genefamilies.tsv
/home/wzk/Project/humann2_test/humann2_result/demo_pathabundance.tsv
/home/wzk/Project/humann2_test/humann2_result/demo_pathcoverage.tsv


```

output files:

```
$ tree humann2_result

humann2_result
├── demo_genefamilies.tsv
├── demo_humann2_temp
│   ├── demo_bowtie2_aligned.sam
│   ├── demo_bowtie2_aligned.tsv
│   ├── demo_bowtie2_index.1.bt2
│   ├── demo_bowtie2_index.2.bt2
│   ├── demo_bowtie2_index.3.bt2
│   ├── demo_bowtie2_index.4.bt2
│   ├── demo_bowtie2_index.rev.1.bt2
│   ├── demo_bowtie2_index.rev.2.bt2
│   ├── demo_bowtie2_unaligned.fa
│   ├── demo_custom_chocophlan_database.ffn
│   ├── demo_diamond_aligned.tsv
│   ├── demo_diamond_unaligned.fa
│   ├── demo_metaphlan_bowtie2.txt
│   ├── demo_metaphlan_bugs_list.tsv
│   └── tmpk3fMYz
│       ├── bowtie2_stderr_mFbYcP
│       ├── bowtie2_stdout_0wVRYf
│       └── temp_alignmentsTwimky
├── demo_pathabundance.tsv
└── demo_pathcoverage.tsv

```


details of output files:
```
$ head demo_genefamilies.tsv
# Gene Family   demo_Abundance-RPKs
UNMAPPED    3829.0000000000
UniRef90_unknown    1633.3754216411
UniRef90_unknown|g__Bacteroides.s__Bacteroides_dorei    894.7763053061
UniRef90_unknown|g__Bacteroides.s__Bacteroides_vulgatus 738.5991163350
UniRef90_R6HHA8 333.3333333333
UniRef90_R6HHA8|g__Bacteroides.s__Bacteroides_dorei 333.3333333333
UniRef90_R7NYS9 166.6666666667
UniRef90_R7NYS9|g__Bacteroides.s__Bacteroides_vulgatus  166.6666666667
UniRef90_D1K9F5 66.6666666667


$ head demo_pathabundance.tsv
# Pathway   demo_Abundance
UNMAPPED    1300.1656345474
UNINTEGRATED    6520.5868810676
UNINTEGRATED|g__Bacteroides.s__Bacteroides_dorei    3123.1902040899
UNINTEGRATED|g__Bacteroides.s__Bacteroides_vulgatus 2753.6043067990
UNINTEGRATED|unclassified   227.4537285403
PWY-6305: putrescine biosynthesis IV    30.3913024756
PWY-6305: putrescine biosynthesis IV|unclassified   30.3913024756
PWY-5423: oleoresin monoterpene volatiles biosynthesis  23.5421011503
PWY-5423: oleoresin monoterpene volatiles biosynthesis|unclassified 23.5421011503


$ head demo_pathcoverage.tsv
# Pathway   demo_Coverage
UNMAPPED    1.0000000000
UNINTEGRATED    1.0000000000
UNINTEGRATED|g__Bacteroides.s__Bacteroides_dorei    1.0000000000
UNINTEGRATED|g__Bacteroides.s__Bacteroides_vulgatus 1.0000000000
UNINTEGRATED|unclassified   1.0000000000
PWY-6305: putrescine biosynthesis IV    0.9999818077
PWY-6305: putrescine biosynthesis IV|unclassified   0.9401999667
PWY-5423: oleoresin monoterpene volatiles biosynthesis  0.9997477716
PWY-5423: oleoresin monoterpene volatiles biosynthesis|unclassified 0.7679602982

```


### Guides to HUMAnN2 utility scripts

```
humann2_associate
humann2_barplot
humann2_build_custom_database
humann2_config
humann2_databases
humann2_gene_families_genus_level
humann2_humann1_kegg
humann2_infer_taxonomy
humann2_join_tables
humann2_reduce_table
humann2_regroup_table
humann2_rename_table
humann2_renorm_table
humann2_rna_dna_norm
humann2_split_stratified_table
humann2_split_table
humann2_strain_profiler
humann2_test
humann2_unpack_pathways

```

#### humann2_barplot
```
$ humann2_barplot
usage: humann2_barplot [-h] -i <input table> [-f <feature id>] [-t <int>]
                       [-s <sorting methods> [<sorting methods> ...]]
                       [-l <feature>] [-m <feature>] [-c <colormap>]
                       [-k <colormap>] [-x] [-o <file.ext>] [-a <choice>] [-g]
                       [-r] [-z] [-w <int>] [-d <size> <size>]
                       [-y <limit> <limit>] [-e]
humann2_barplot: error: argument -i/--input is required
(qiime) wzk@ubuntu 03:15:36 O_O /home/wzk/database 
$ humann2_barplot -h
usage: humann2_barplot [-h] -i <input table> [-f <feature id>] [-t <int>]
                       [-s <sorting methods> [<sorting methods> ...]]
                       [-l <feature>] [-m <feature>] [-c <colormap>]
                       [-k <colormap>] [-x] [-o <file.ext>] [-a <choice>] [-g]
                       [-r] [-z] [-w <int>] [-d <size> <size>]
                       [-y <limit> <limit>] [-e]

HUMAnN2 plotting tool

optional arguments:
  -h, --help            show this help message and exit
  -i <input table>, --input <input table>
                        HUMAnN2 table with optional metadata
  -f <feature id>, --focal-feature <feature id>
                        Feature ID of interest (give ID not full name)
  -t <int>, --top-strata <int>
                        Number of top stratifications to highlight (top = highest grand means)
  -s <sorting methods> [<sorting methods> ...], --sort <sorting methods> [<sorting methods> ...]
                        Sample sorting methods (can use more than one; will evaluate in order)
                        
                        none        : Default
                        sum         : Sum of stratified values
                        dominant    : Value of the most dominant stratification
                        similarity  : Bray-Curtis agreement of relative stratifications
                        usimilarity : Bray-Curtis agreement of raw stratifications
                        metadata    : Given metadata label
                        
  -l <feature>, --last-metadatum <feature>
                        Indicate end of metadata rows
  -m <feature>, --focal-metadatum <feature>
                        Indicate metadatum to highlight / group by
  -c <colormap>, --colormap <colormap>
                        Color space for stratifications
  -k <colormap>, --meta-colormap <colormap>
                        Color space for metadata levels
  -x, --exclude-unclassified
                        Do not include the 'unclassified' stratum
  -o <file.ext>, --output <file.ext>
                        Where to save the figure
  -a <choice>, --scaling <choice>
                        Scaling options for total bar heights (strata are always proportional to height)
                        
                        none        : Default
                        pseudolog   : Total bar heights log-scaled (strata are NOT log scaled)
                        normalize   : Bars all have height=1 (highlighting relative attribution)
                        
  -g, --as-genera       Collapse species to genera
  -r, --grid            Add y-axis grid
  -z, --remove-zeroes   Do not plot samples with zero sum for this feature
  -w <int>, --width <int>
                        Relative width of the plot vs. legend (default: 5)
  -d <size> <size>, --dimensions <size> <size>
                        Image height and width in inches (default: 8 4)
  -y <limit> <limit>, --ylims <limit> <limit>
                        Fix limits for y-axis
  -e , --legend-stretch 
                        Stretch/compress legend elements

```

