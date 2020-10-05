
###   [MetaQUAST](http://bioinf.spbau.ru/metaquast)

evaluates and compares metagenome assemblies based on alignments to close references. It is based on QUAST genome quality assessment tool, but addresses features specific for metagenome datasets

```
$ metaquast.py --output-dir quality --threads 10 HMP_GUT_SRS052697.25M.contigs.fa

Version 3.0, build 07.07.2015 05:57

System information:
  OS: Linux-4.4.0-62-generic-x86_64-with-debian-stretch-sid (linux_64)
  Python version: 2.7.13
  CPUs number: 40

Started: 2017-11-02 07:18:00

Logging to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/metaquast.log

Contigs:

No references are provided, starting to search for reference genomes in SILVA rRNA database and to download them from NCBI...

2017-11-02 07:18:00

Downloading SILVA ribosomal RNA gene database...

ERROR! Failed downloading SILVA rRNA gene database (http://www.arb-silva.de/fileadmin/silva_databases/release_119/Exports/SILVA_119_SSURef_Nr99_tax_silva.fasta.gz)! The search for reference genomes cannot be performed. Try to download it manually in /home/wzk/anaconda3/envs/qiime/bin/quast-3.0/libs/blast/16S_RNA_blastdb and restart MetaQUAST.


NOTICE: No references are provided, starting quast.py with MetaGeneMark gene finder
  /home/wzk/anaconda3/envs/qiime/bin/quast-3.0/quast.pyc --threads 10 --meta  --combined-ref  -o /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output --labels HMP_GUT_SRS052697.25M.contigs HMP_GUT_SRS052697.25M.contigs.fa
  
  Started: 2017-11-02 07:18:01
  
  Logging to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/quast.log
  
  Contigs:
    HMP_GUT_SRS052697.25M.contigs.fa ==> HMP_GUT_SRS052697.25M.contigs
 2017-11-02 07:18:29
  Running Basic statistics processor...
    Contig files: 
      HMP_GUT_SRS052697.25M.contigs
    Calculating N50 and L50...
      HMP_GUT_SRS052697.25M.contigs, N50 = 6259, L50 = 4711, Total length = 188966823, GC % = 46.06, # N's per 100 kbp =  0.00
    Drawing cumulative plot...
      saved to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/basic_stats/cumulative_plot.pdf
    Drawing GC content plot...
      saved to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/basic_stats/GC_content_plot.pdf
    Drawing Nx plot...
      saved to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/basic_stats/Nx_plot.pdf
  Done.
  
  NOTICE: Genes are not predicted by default. Use --gene-finding option to enable it.
  
  2017-11-02 07:18:43
  Drawing large plots...
  This may take a while: press Ctrl-C to skip this step..
    1 of 1: Creating PDF with all tables and plots...
  Done
  
  2017-11-02 07:18:44
  RESULTS:
    Text versions of total report are saved to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/report.txt, report.tsv, and report.tex
    Text versions of transposed total report are saved to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/transposed_report.txt, transposed_report.tsv, and transposed_report.tex
    HTML version (interactive tables and plots) saved to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/report.html
    PDF version (tables and plots) saved to /home/wzk/metagenome_data/assembly/HMP_GUT_SRS052697.25M/quality/quast_output/report.pdf

```





### statistics for assembly genome by running metaquast

download database
```bash
$ wget https://www.arb-silva.de/fileadmin/silva_databases/release_119/Exports/SILVA_119_SSURef_Nr99_tax_silva.fasta.gz
```



```
$ python /home/wzk/anaconda3/envs/qiime/bin/quast-3.0/metaquast.py Meta.contigs.fa -o metaquast_report --threads 20 
```
output files
```
$ tree metaquast_report -L 1
metaquast_report
├── metaquast.log
├── quast_corrected_input
├── quast_downloaded_references
└── quast_output

$ tree metaquast_report/quast_output -L 1
metaquast_report/quast_output
├── basic_stats
├── quast.log
├── report.html
├── report_html_aux
├── report.pdf
├── report.tex
├── report.tsv
├── report.txt
├── transposed_report.tex
├── transposed_report.tsv
└── transposed_report.txt
```
