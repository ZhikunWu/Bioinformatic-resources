
## [kneaddata](http://huttenhower.sph.harvard.edu/kneaddata) manual

### [KneadData User Manual](https://bitbucket.org/biobakery/kneaddata/wiki/Home)

### Install kneaddata 
```
$ conda install -c bioconda kneaddata
```


### Download human reference database

#### kneaddata_database parameters
```
$ kneaddata_database --help
usage: kneaddata_database [-h] [--available]
                          [--download <database> <build> <install_location>]

KneadData Databases

optional arguments:
  -h, --help            show this help message and exit
  --available           print the available databases
  --download <database> <build> <install_location>
                        download the selected database to the install location
```

```
$ kneaddata_database  --available
KneadData Databases ( database : build = location )
human_genome : bmtagger = http://huttenhower.sph.harvard.edu/kneadData_databases/Homo_sapiens_BMTagger_v0.1.tar.gz
human_genome : bowtie2 = http://huttenhower.sph.harvard.edu/kneadData_databases/Homo_sapiens_Bowtie2_v0.1.tar.gz
mouse_C57BL : bowtie2 = http://huttenhower.sph.harvard.edu/kneadData_databases/mouse_C57BL_6NJ_Bowtie2_v0.1.tar.gz
human_transcriptome : bowtie2 = http://huttenhower.sph.harvard.edu/kneadData_databases/Homo_sapiens_hg38_transcriptome_Bowtie2_v0.1.tar.gz
ribosomal_RNA : bowtie2 = http://huttenhower.sph.harvard.edu/kneadData_databases/SILVA_128_LSUParc_SSUParc_ribosomal_RNA_v0.1.tar.gz

```

#### download human genome database

```
$ cd /home/wzk/database &&　mkdir kneaddata　

$ kneaddata_database  --download human_genome  bowtie2  /home/wzk/database/kneaddata

Download URL: http://huttenhower.sph.harvard.edu/kneadData_databases/Homo_sapiens_Bowtie2_v0.1.tar.gz
Downloading file of size: 3.44 GB

3.44 GB 100.00 %   9.31 MB/sec  0 min -0 sec         
Extracting: /home/wzk/database/kneaddata/Homo_sapiens_Bowtie2_v0.1.tar.gz
Database installed: /home/wzk/database/kneaddata

```

**bowtie2** tell us the softwawre building the database, which is also the tool aligning the reads 

**/home/wzk/database/kneaddata** is your directory path of the bowtie2 index of human genome


database files:

```
-rw-rw-r-- 1 915M Jun 11  2015 Homo_sapiens.1.bt2
-rw-rw-r-- 1 684M Jun 11  2015 Homo_sapiens.2.bt2
-rw-rw-r-- 1 3.8K Jun 11  2015 Homo_sapiens.3.bt2
-rw-rw-r-- 1 684M Jun 11  2015 Homo_sapiens.4.bt2
-rw-rw-r-- 1 915M Jun 11  2015 Homo_sapiens.rev.1.bt2
-rw-rw-r-- 1 684M Jun 11  2015 Homo_sapiens.rev.2.bt2

```

### Build specific reference database

Because the **kneaddata** using **bowtie2** to align the reads to host genome,

you can build the database by youself.

```
$ bowtie2-build --threads 10  mouse_genome.fa mouse_genome 
```
**--threads**  means the threads used for constructing index of genome


### run kneaddata

#### Single end reads


```
$ kneaddata --input examples/demo.fastq --reference-db examples/demo_db --output kneaddata_demo_output
```

output files:
```
kneaddata_demo_output/demo_kneaddata.fastq
kneaddata_demo_output/demo_kneaddata_demo_db_bowtie2_contam.fastq
kneaddata_demo_output/demo_kneaddata.log
kneaddata_demo_output/demo_kneaddata.trimmed.fastq
```

#### Additional Arguments

If you want to specify additional arguments for Bowtie2 using the **--bowtie2-options** flag, you will need to use the equals sign along with quotes. Add additional flags for each option.


For example:
```
$ kneaddata --input demo.fastq --output kneaddata_output --reference-db database_folder --bowtie2-options="--very-fast" --bowtie2-options="-p 2"
```

A similar approach is used to specify additional arguments for Trimmomatic:
```
$ kneaddata --input demo.fastq --output kneaddata_output --reference-db database_folder --trimmomatic-options="LEADING:3" --trimmomatic-options="TRAILING:3"
```

#### multiple reference

Also more than one database can be provided for each run. The database argument can contain the folder that includes the database or the prefix of the database files.

```
$ kneaddata --input demo.fastq --output kneaddata_output --reference-db database_folder --reference-db database_folder2/demo
```


### Complete Option List

```
$ kneaddata --help
usage: kneaddata [-h] [--version] [-v] -i INPUT -o OUTPUT_DIR
                 [-db REFERENCE_DB] [--bypass-trim]
                 [--output-prefix OUTPUT_PREFIX] [-t <1>] [-p <1>]
                 [-q {phred33,phred64}] [--run-bmtagger] [--run-trf]
                 [--run-fastqc-start] [--run-fastqc-end] [--store-temp-output]
                 [--remove-intermediate-output] [--cat-final-output]
                 [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--log LOG]
                 [--trimmomatic TRIMMOMATIC_PATH] [--max-memory MAX_MEMORY]
                 [--trimmomatic-options TRIMMOMATIC_OPTIONS]
                 [--bowtie2 BOWTIE2_PATH] [--bowtie2-options BOWTIE2_OPTIONS]
                 [--no-discordant] [--reorder] [--serial]
                 [--bmtagger BMTAGGER_PATH] [--trf TRF_PATH] [--match MATCH]
                 [--mismatch MISMATCH] [--delta DELTA] [--pm PM] [--pi PI]
                 [--minscore MINSCORE] [--maxperiod MAXPERIOD]
                 [--fastqc FASTQC_PATH]

KneadData

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         additional output is printed

global options:
  --version             show program's version number and exit
  -i INPUT, --input INPUT
                        input FASTQ file (add a second argument instance to run with paired input files)
  -o OUTPUT_DIR, --output OUTPUT_DIR
                        directory to write output files
  -db REFERENCE_DB, --reference-db REFERENCE_DB
                        location of reference database (additional arguments add databases)
  --bypass-trim         bypass the trim step
  --output-prefix OUTPUT_PREFIX
                        prefix for all output files
                        [ DEFAULT : $SAMPLE_kneaddata ]
  -t <1>, --threads <1>
                        number of threads
                        [ Default : 1 ]
  -p <1>, --processes <1>
                        number of processes
                        [ Default : 1 ]
  -q {phred33,phred64}, --quality-scores {phred33,phred64}
                        quality scores
                        [ DEFAULT : phred33 ]
  --run-bmtagger        run BMTagger instead of Bowtie2 to identify contaminant reads
  --run-trf             run TRF to remove tandem repeats
  --run-fastqc-start    run fastqc at the beginning of the workflow
  --run-fastqc-end      run fastqc at the end of the workflow
  --store-temp-output   store temp output files
                        [ DEFAULT : temp output files are removed ]
  --remove-intermediate-output
                        remove intermediate output files
                        [ DEFAULT : intermediate output files are stored ]
  --cat-final-output    concatenate all final output files
                        [ DEFAULT : final output is not concatenated ]
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        level of log messages
                        [ DEFAULT : DEBUG ]
  --log LOG             log file
                        [ DEFAULT : $OUTPUT_DIR/$SAMPLE_kneaddata.log ]

trimmomatic arguments:
  --trimmomatic TRIMMOMATIC_PATH
                        path to trimmomatic
                        [ DEFAULT : $PATH ]
  --max-memory MAX_MEMORY
                        max amount of memory
                        [ DEFAULT : 500m ]
  --trimmomatic-options TRIMMOMATIC_OPTIONS
                        options for trimmomatic
                        [ DEFAULT : ILLUMINACLIP:/TruSeq3-SE.fa:2:30:10 SLIDINGWINDOW:4:20 MINLEN:50 ]
                        MINLEN is set to 50 percent of total input read length

bowtie2 arguments:
  --bowtie2 BOWTIE2_PATH
                        path to bowtie2
                        [ DEFAULT : $PATH ]
  --bowtie2-options BOWTIE2_OPTIONS
                        options for bowtie2
                        [ DEFAULT : --very-sensitive ]
  --no-discordant       do not include discordant alignments for pairs (ie one of the two pairs aligns)
                        [ DEFAULT : Discordant alignments are included ]
  --reorder             order the sequences in the same order as the input
                        [ DEFAULT : With discordant paired alignments sequences are not ordered ]
  --serial              filter the input in serial for multiple databases so a subset of reads are processed in each database search

bmtagger arguments:
  --bmtagger BMTAGGER_PATH
                        path to BMTagger
                        [ DEFAULT : $PATH ]

trf arguments:
  --trf TRF_PATH        path to TRF
                        [ DEFAULT : $PATH ]
  --match MATCH         matching weight
                        [ DEFAULT : 2 ]
  --mismatch MISMATCH   mismatching penalty
                        [ DEFAULT : 7 ]
  --delta DELTA         indel penalty
                        [ DEFAULT : 7 ]
  --pm PM               match probability
                        [ DEFAULT : 80 ]
  --pi PI               indel probability
                        [ DEFAULT : 10 ]
  --minscore MINSCORE   minimum alignment score to report
                        [ DEFAULT : 50 ]
  --maxperiod MAXPERIOD
                        maximum period size to report
                        [ DEFAULT : 500 ]

fastqc arguments:
  --fastqc FASTQC_PATH  path to fastqc
                        [ DEFAULT : $PATH ]

```