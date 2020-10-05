
## Quast

### Install quast

quast need the environment python 2.7
```
$ conda install -c bioconda quast 
```

or download package

```bash
$ curl -L http://sourceforge.net/projects/quast/files/quast-3.0.tar.gz/download > quast-3.0.tar.gz
```


### Run quast
```
$ /home/wzk/anaconda3/envs/py27/lib/python2.7/site-packages/quast-4.6.3-py2.7.egg-info/scripts/quast.py -o /home/wzk/Project/AtGenome/quast -R /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa -G /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35.gff3 -m 500 -t 20 Correction/ERR2173373_racon3.fasta

Version: 4.6.3

System information:
  OS: Linux-4.4.0-62-generic-x86_64-with-debian-stretch-sid (linux_64)
  Python version: 2.7.14
  CPUs number: 40

Started: 2018-05-20 04:27:30

Logging to /home/wzk/Project/AtGenome/quast/quast.log

CWD: /home/wzk/Project/AtGenome
Main parameters: 
  Threads: 20, minimum contig length: 500, ambiguity: one, threshold for extensive misassembly size: 1000

Reference:
  /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa ==> Arabidopsis_thaliana.TAIR10.dna.toplevel

Contigs:
  Pre-processing...
  Correction/ERR2173373_racon3.fasta ==> ERR2173373_racon3

2018-05-20 04:27:41
Running Basic statistics processor...
  Reference genome:
    Arabidopsis_thaliana.TAIR10.dna.toplevel.fa, length = 119667750, num fragments = 7, GC % = 36.06
  Contig files: 
    ERR2173373_racon3
  Calculating N50 and L50...
    ERR2173373_racon3, N50 = 11188487, L50 = 5, Total length = 117536784, GC % = 36.15, # N's per 100 kbp =  0.00
  Drawing Nx plot...
    saved to /home/wzk/Project/AtGenome/quast/basic_stats/Nx_plot.pdf
  Drawing NGx plot...
    saved to /home/wzk/Project/AtGenome/quast/basic_stats/NGx_plot.pdf
  Drawing cumulative plot...
    saved to /home/wzk/Project/AtGenome/quast/basic_stats/cumulative_plot.pdf
  Drawing GC content plot...
    saved to /home/wzk/Project/AtGenome/quast/basic_stats/GC_content_plot.pdf
  Drawing ERR2173373_racon3 GC content plot...
    saved to /home/wzk/Project/AtGenome/quast/basic_stats/ERR2173373_racon3_GC_content_plot.pdf
Done.

2018-05-20 04:27:53
Running Contig analyzer...
  ERR2173373_racon3
  Logging to files /home/wzk/Project/AtGenome/quast/contigs_reports/contigs_report_ERR2173373_racon3.stdout and contigs_report_ERR2173373_racon3.stderr...
  Aligning contigs to the reference
    Aligning to different chromosomes in parallel (6 threads)
WARNING:   Drawing MUMmer plots is disabled in QUAST's Bioconda package.
  Analysis is finished.
  Gzipping /home/wzk/Project/AtGenome/quast/contigs_reports/nucmer_output/ERR2173373_racon3.all_snps to reduce disk space usage...
    saved to /home/wzk/Project/AtGenome/quast/contigs_reports/nucmer_output/ERR2173373_racon3.all_snps.gz
  Creating total report...
    saved to /home/wzk/Project/AtGenome/quast/contigs_reports/misassemblies_report.txt, misassemblies_report.tsv, and misassemblies_report.tex
  Transposed version of total report...
    saved to /home/wzk/Project/AtGenome/quast/contigs_reports/transposed_report_misassemblies.txt, transposed_report_misassemblies.tsv, and transposed_report_misassemblies.tex
  Creating total report...
    saved to /home/wzk/Project/AtGenome/quast/contigs_reports/unaligned_report.txt, unaligned_report.tsv, and unaligned_report.tex
  Drawing misassemblies by types plot...
    saved to /home/wzk/Project/AtGenome/quast/contigs_reports/misassemblies_plot.pdf
  Drawing misassemblies FRCurve plot...
    saved to /home/wzk/Project/AtGenome/quast/contigs_reports/misassemblies_frcurve_plot.pdf
Done.

2018-05-20 04:39:58
Running NA-NGA calculation...
  ERR2173373_racon3, Largest alignment = 1157284, NA50 = 114026, NGA50 = 111325, LA50 = 239, LGA50 = 248
  Drawing cumulative plot...
    saved to /home/wzk/Project/AtGenome/quast/aligned_stats/cumulative_plot.pdf
  Drawing NAx plot...
    saved to /home/wzk/Project/AtGenome/quast/aligned_stats/NAx_plot.pdf
  Drawing NGAx plot...
    saved to /home/wzk/Project/AtGenome/quast/aligned_stats/NGAx_plot.pdf
Done.

2018-05-20 04:40:02
Running Genome analyzer...
  Loaded 31435 genes
  NOTICE: No file with operons provided. Use the -O option if you want to specify it.
  ERR2173373_racon3
  Analysis is finished.
  Drawing genes cumulative plot...
    saved to /home/wzk/Project/AtGenome/quast/genome_stats/genes_cumulative_plot.pdf
  Drawing genes FRCurve plot...
    saved to /home/wzk/Project/AtGenome/quast/genome_stats/genes_frcurve_plot.pdf
  Skipping drawing # complete genes histogram... (less than 2 columns histogram makes no sense)
  Skipping drawing Genome fraction, % histogram... (less than 2 columns histogram makes no sense)
Done.

NOTICE: Genes are not predicted by default. Use --gene-finding option to enable it.

2018-05-20 04:40:52
Creating large visual summaries...
This may take a while: press Ctrl-C to skip this step..
  1 of 2: Creating Icarus viewers...
  2 of 2: Creating PDF with all tables and plots...
Done

2018-05-20 04:40:56
RESULTS:
  Text versions of total report are saved to /home/wzk/Project/AtGenome/quast/report.txt, report.tsv, and report.tex
  Text versions of transposed total report are saved to /home/wzk/Project/AtGenome/quast/transposed_report.txt, transposed_report.tsv, and transposed_report.tex
  HTML version (interactive tables and plots) saved to /home/wzk/Project/AtGenome/quast/report.html
  PDF version (tables and plots) is saved to /home/wzk/Project/AtGenome/quast/report.pdf
  Icarus (contig browser) is saved to /home/wzk/Project/AtGenome/quast/icarus.html
  Log saved to /home/wzk/Project/AtGenome/quast/quast.log

Finished: 2018-05-20 04:40:56
Elapsed time: 0:13:25.725488
NOTICEs: 2; WARNINGs: 1; non-fatal ERRORs: 0

Thank you for using QUAST!

```

output files:
```
drwxr-xr-x 2 4.0K May 20 04:40 aligned_stats
drwxr-xr-x 2 4.0K May 20 04:27 basic_stats
drwxr-xr-x 3 4.0K May 20 04:39 contigs_reports
drwxr-xr-x 2 4.0K May 20 04:40 genome_stats
-rw-r--r-- 1  55K May 20 04:40 icarus.html
drwxr-xr-x 2 4.0K May 20 04:40 icarus_viewers
-rw-r--r-- 1 8.9K May 20 04:40 quast.log
-rw-r--r-- 1 590K May 20 04:40 report.html
-rw-r--r-- 1  58K May 20 04:40 report.pdf
-rw-r--r-- 1 2.1K May 20 04:40 report.tex
-rw-r--r-- 1 1.1K May 20 04:40 report.tsv
-rw-r--r-- 1 2.5K May 20 04:40 report.txt
-rw-r--r-- 1 1.8K May 20 04:40 transposed_report.tex
-rw-r--r-- 1 1.1K May 20 04:40 transposed_report.tsv
-rw-r--r-- 1 1.9K May 20 04:40 transposed_report.txt
```





