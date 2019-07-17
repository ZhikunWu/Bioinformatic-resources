### BUSCO

environment NanoSV

```
$ python scripts/run_BUSCO.py -h
usage: python BUSCO.py -i [SEQUENCE_FILE] -l [LINEAGE] -o [OUTPUT_NAME] -m [MODE] [OTHER OPTIONS]

Welcome to BUSCO 3.1.0: the Benchmarking Universal Single-Copy Ortholog assessment tool.
For more detailed usage information, please review the README file provided with this distribution and the BUSCO user guide.

optional arguments:
  -i FASTA FILE, --in FASTA FILE
                        Input sequence file in FASTA format. Can be an assembled genome or transcriptome (DNA), or protein sequences from an annotated gene set.
  -c N, --cpu N         Specify the number (N=integer) of threads/cores to use.
  -o OUTPUT, --out OUTPUT
                        Give your analysis run a recognisable short name. Output folders and files will be labelled with this name. WARNING: do not provide a path
  -e N, --evalue N      E-value cutoff for BLAST searches. Allowed formats, 0.001 or 1e-03 (Default: 1e-03)
  -m MODE, --mode MODE  Specify which BUSCO analysis mode to run.
                        There are three valid modes:
                        - geno or genome, for genome assemblies (DNA)
                        - tran or transcriptome, for transcriptome assemblies (DNA)
                        - prot or proteins, for annotated gene sets (protein)
  -l LINEAGE, --lineage_path LINEAGE
                        Specify location of the BUSCO lineage data to be used.
                        Visit http://busco.ezlab.org for available lineages.
  -f, --force           Force rewriting of existing files. Must be used when output files with the provided name already exist.
  -r, --restart         Restart an uncompleted run. Not available for the protein mode
  -sp SPECIES, --species SPECIES
                        Name of existing Augustus species gene finding parameters. See Augustus documentation for available options.
  --augustus_parameters AUGUSTUS_PARAMETERS
                        Additional parameters for the fine-tuning of Augustus run. For the species, do not use this option.
                        Use single quotes as follow: '--param1=1 --param2=2', see Augustus documentation for available options.
  -t PATH, --tmp_path PATH
                        Where to store temporary files (Default: ./tmp/)
  --limit REGION_LIMIT  How many candidate regions (contig or transcript) to consider per BUSCO (default: 3)
  --long                Optimization mode Augustus self-training (Default: Off) adds considerably to the run time, but can improve results for some non-model organisms
  -q, --quiet           Disable the info logs, displays only errors
  -z, --tarzip          Tarzip the output folders likely to contain thousands of files
  --blast_single_core   Force tblastn to run on a single core and ignore the --cpu argument for this step only. Useful if inconsistencies when using multiple threads are noticed
  -v, --version         Show this version and exit
  -h, --help            Show this help message and exit

```


### config file

```
$ cat /home/wuzhikun/anaconda3/envs/NanoSV/bin/busco-master/config/config.ini

# BUSCO specific configuration
# It overrides default values in code and dataset cfg, and is overridden by arguments in command line
# Uncomment lines when appropriate
[busco]
# Input file
;in = ./sample_data/target.fa
# Run name, used in output files and folder
;out = SAMPLE
# Where to store the output directory
;out_path = /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2
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
;blast_single_core = False

[tblastn]
# path to tblastn
path = /opt/software/blast-2.9.0/bin/

[makeblastdb]
# path to makeblastdb
path = /opt/software/blast-2.9.0/bin/

[augustus]
# path to augustus
path = ~/anaconda3/envs/NanoSV/bin/

[etraining]
# path to augustus etraining
path = ~/anaconda3/envs/NanoSV/bin/

# path to augustus perl scripts, redeclare it for each new script
[gff2gbSmallDNA.pl]
path = /home/wuzhikun/anaconda3/envs/NanoSV/bin/augustus-3.3.2/scripts/
[new_species.pl]
path = /home/wuzhikun/anaconda3/envs/NanoSV/bin/augustus-3.3.2/scripts
[optimize_augustus.pl]
path = /home/wuzhikun/anaconda3/envs/NanoSV/bin/augustus-3.3.2/scripts

[hmmsearch]
# path to HMMsearch executable
path = ~/anaconda3/envs/NanoSV/bin/

[Rscript]
# path to Rscript, if you wish to use the plot tool
path = ~/anaconda3/envs/NanoSV/bin/

```

### run busco

```
python /home/wuzhikun/anaconda3/envs/NanoSV/bin/busco-master/scripts/run_BUSCO.py --in M628-0.contig.fa --out /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2/contig_busco  --evalue 1e-05 --mode genome --lineage_path /home/wuzhikun/database/BUSCO/mammalia_odb9 --cpu 20
ERROR	No section [busco] found in /home/wuzhikun/anaconda3/envs/NanoSV/bin/busco-master/scripts/../config/config.ini. Please make sure both the file and this section exist, see userguide.
```


```
$ python /home/wuzhikun/anaconda3/envs/NanoSV/bin/busco-master/scripts/run_BUSCO.py --in /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2/M628-0.contig.fa --out contig_busco  --evalue 1e-05 --mode genome --lineage_path /home/wuzhikun/database/BUSCO/mammalia_odb9 --cpu 20
WARNING	You are using a custom e-value cutoff
INFO	****************** Start a BUSCO 3.1.0 analysis, current time: 07/12/2019 15:17:47 ******************
INFO	Configuration loaded from /home/wuzhikun/anaconda3/envs/NanoSV/bin/busco-master/scripts/../config/config.ini
INFO	Init tools...
INFO	Check dependencies...
ERROR	The environment variable AUGUSTUS_CONFIG_PATH is not set
ERROR	BUSCO analysis failed !
ERROR	Check the logs, read the user guide, if you still need technical support, then please contact mailto:support@orthodb.org

```

set path of augustus
```
$ export AUGUSTUS_CONFIG_PATH=/home/wuzhikun/anaconda3/envs/NanoSV/bin/augustus-3.3.2/config/

$ python /home/wuzhikun/anaconda3/envs/NanoSV/bin/busco-master/scripts/run_BUSCO.py --in /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2/M628-0.contig.fa --out contig_busco  --evalue 1e-05 --mode genome --lineage_path /home/wuzhikun/database/BUSCO/mammalia_odb9 --cpu 20
```


### output files

output files in the dir **run_contig_busco**

```
drwxrwxr-x 1 4.0K Jul 12 18:30 augustus_output
drwxrwxr-x 1 4.0K Jul 12 18:33 blast_output
-rw-rw-r-- 1   15 Jul 12 18:33 checkpoint.tmp
-rw-rw-r-- 1 119K Jul 12 18:33 full_table_contig_busco.tsv
drwxrwxr-x 1 4.0K Jul 12 18:33 hmmer_output
-rw-rw-r-- 1  36K Jul 12 18:33 missing_busco_list_contig_busco.tsv
-rw-rw-r-- 1  808 Jul 12 18:33 short_summary_contig_busco.txt

```


```
$ cat short_summary_contig_busco.txt
# BUSCO version is: 3.1.0 
# The lineage dataset is: mammalia_odb9 (Creation date: 2016-02-13, number of species: 50, number of BUSCOs: 4104)
# To reproduce this run: python /home/wuzhikun/anaconda3/envs/NanoSV/bin/busco-master/scripts/run_BUSCO.py -i /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2/M628-0.contig.fa -o contig_busco -l /home/wuzhikun/database/BUSCO/mammalia_odb9/ -m genome -c 20 -e 1e-05 -sp human
#
# Summarized benchmarking in BUSCO notation for file /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2/M628-0.contig.fa
# BUSCO was run in mode: genome

	C:12.6%[S:12.6%,D:0.0%],F:14.8%,M:72.6%,n:4104

	517	Complete BUSCOs (C)
	517	Complete and single-copy BUSCOs (S)
	0	Complete and duplicated BUSCOs (D)
	606	Fragmented BUSCOs (F)
	2981	Missing BUSCOs (M)
	4104	Total BUSCO groups searched

```

