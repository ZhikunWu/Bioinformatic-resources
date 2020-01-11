

## RepeatModeler: De Novo Repeat Identification

### [RepeatModeler manual](http://www.repeatmasker.org/RepeatModeler/)

### RepeatModeler Statistics

```

Genome  Genome DB Size (bp) Runtime (hh:mm)*    Models Built
D. melanogaster 164 Mbp 12:56   734
D. rerio    1.4 Gbp 40:36   3851
O. sativa   375 Mbp 37:23   2648
```


### BuildDatabase parameters
```
$ BuildDatabase --help
No query sequence file indicated

NAME
    BuildDatabase - Format FASTA files for use with RepeatModeler

SYNOPSIS
      BuildDatabase [-options] -name "mydb" <seqfile(s) in fasta format>
     or 
      BuildDatabase [-options] -name "mydb" 
                                  -dir <dir containing fasta files *.fa, *.fasta,
                                         *.fast, *.FA, *.FASTA, *.FAST, *.dna,
                                         and  *.DNA > 
     or
      BuildDatabase [-options] -name "mydb" 
                                  -batch <file containing a list of fasta files>

DESCRIPTION
      This is basically a wrapper around AB-Blast's and NCBI Blast's
      DB formating programs.  It assists in aggregating files for processing 
      into a single database.  Source files can be specified by:

          - Placing the names of the FASTA files on the command
            line.
          - Providing the name of a directory containing FASTA files 
            with the file suffixes *.fa or *.fasta.
          - Providing the name of a manifest file which contains the 
            names of FASTA files ( fully qualified ) one per line.

      NOTE: Sequence identifiers are not preserved in this database. Each
            sequence is assigned a new GI ( starting from 1 ).  The 
            translation back to the original sequence is preserved in the
            *.translation file.

    The options are:

    -h(elp)
        Detailed help

    -name <database name>
        The name of the database to create.

    -engine <engine name>
        The name of the search engine we are using. I.e abblast/wublast or
        ncbi (rmblast version).

    -dir <directory>
        The name of a directory containing fasta files to be processed. The
        files are recognized by their suffix. Only *.fa and *.fasta files
        are processed.

    -batch <file>
        The name of a file which contains the names of fasta files to
        process. The files names are listed one per line and should be fully
        qualified.

SEE ALSO
        RepeatModeler, ABBlast, NCBIBlast

COPYRIGHT
    Copyright 2004-2017 Institute for Systems Biology

AUTHOR
    Robert Hubley <rhubley@systemsbiology.org>


```


```
$ BuildDatabase -name Pancontigs -engine ncbi Samples_contigs_cdhit_filt.fa
Building database Pancontigs:
  Adding Samples_contigs_cdhit_filt.fa to database
Number of sequences (bp) added to database: 8293 ( 4792534 bp )

```

out files :
```
-rw-rw-r-- 1 300K Dec 28 20:00 Pancontigs.nhr
-rw-rw-r-- 1  98K Dec 28 20:00 Pancontigs.nin
-rw-rw-r-- 1  65K Dec 28 20:00 Pancontigs.nnd
-rw-rw-r-- 1  308 Dec 28 20:00 Pancontigs.nni
-rw-rw-r-- 1  33K Dec 28 20:00 Pancontigs.nog
-rw-rw-r-- 1 1.2M Dec 28 20:00 Pancontigs.nsq
-rw-rw-r-- 1 154K Dec 28 20:00 Pancontigs.translation

```


### RepeatModeler parameter
```
$ RepeatModeler --help
No database indicated

NAME
    RepeatModeler - Model repetitive DNA

SYNOPSIS
      RepeatModeler [-options] -database <XDF Database>

DESCRIPTION
    The options are:

    -h(elp)
        Detailed help

    -database
        The prefix name of a XDF formatted sequence database containing the
        genomic sequence to use when building repeat models. The database
        may be created with the WUBlast "xdformat" utility or with the
        RepeatModeler wrapper script "BuildXDFDatabase".

    -engine <abblast|wublast|ncbi>
        The name of the search engine we are using. I.e abblast/wublast or
        ncbi (rmblast version).

    -pa #
        Specify the number of shared-memory processors available to this
        program. RepeatModeler will use the processors to run BLAST searches
        in parallel. i.e on a machine with 10 cores one might use 1 core for
        the script and 9 cores for the BLAST searches by running with "-pa
        9".

    -recoverDir <Previous Output Directory>
        If a run fails in the middle of processing, it may be possible
        recover some results and continue where the previous run left off.
        Simply supply the output directory where the results of the failed
        run were saved and the program will attempt to recover and continue
        the run.

    -srand #
        Optionally set the seed of the random number generator to a known
        value before the batches are randomly selected ( using Fisher Yates
        Shuffling ). This is only useful if you need to reproduce the sample
        choice between runs. This should be an integer number.

SEE ALSO
        RepeatMasker, WUBlast

COPYRIGHT
     Copyright 2005-2017 Institute for Systems Biology

AUTHOR
     Robert Hubley <rhubley@systemsbiology.org>
     Arian Smit <asmit@systemsbiology.org>

```


### run RepeatModeler
```
$ RepeatModeler -pa 8 -engine ncbi -database Pancontigs  2>&1 | tee repeatmodeler.log
RepeatModeler Version DEV
================================
Search Engine = ncbi
Random Number Seed: 1577534491
Database = Pancontigs .
  - Sequences = 8293
  - Bases = 4792534
Using output directory = /home/wuzhikun/PublicData/common_bean/Contigs/cdhit/RM_78626.SatDec282001322019


RepeatModeler Round # 1
========================
Searching for Repeats
 -- Sampling from the database...
   - Gathering up to 40000000 bp

```


ouput file:
```
$ less consensi.fa

>rnd-1_family-2 ( RepeatScout Family Size = 101, Final Multiple Alignment Size = 100, Localized to 2006 out of 8293 contigs )
CATCGGCCCGGGCCCGAACGACTCGACATCGGCCCGGGCCCGNNCGACTCGACATCGGCCCGGGCCCGNNCGACTCGACATCGGCCCGGGCCGCTCGACTCGACATCGGCCCGGGCCCGNACGACTCGACATCGGCCCGGGCCCGNNCGACTCGACATCGGCCCGGGCCCGGACGACTCGACATCGGCCCGGGC

>rnd-1_family-1 ( RepeatScout Family Size = 103, Final Multiple Alignment Size = 100, Localized to 2006 out of 8293 contigs )
CTCGACGTGAGAGAGTGTGTTGGAGATCCCACATCGACTAGAGATAAGGACATTTCATAGTATATAAGTGGGTGCAAACCTCACCTTATAAGCCGGTTTTATGAGGTTGAGTTAGGCTTAAAGTCCACTTCTTAATAGTTACAAATAACGTTGTCAAGTCAGTGTCATTAACTAAACCA

```


```
$ less consensi.fa.masked

>rnd-1_family-2 ( RepeatScout Family Size = 101, Final Multiple Alignment Size = 100, Localized to 2006 out of 8293 contigs )
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
>rnd-1_family-1 ( RepeatScout Family Size = 103, Final Multiple Alignment Size = 100, Localized to 2006 out of 8293 contigs )
CTCGACGTGAGAGAGTGTGTTGGAGATCCCACATCGACTAGAGATAAGGA
CATTTCATAGTATATAAGTGGGTGCAAACCTCACCTTATAAGCCGGTTTT
ATGAGGTTGAGTTAGGCTTAAAGTCCACTTCTTAATAGTTACAAATAACG
TTGTCAAGTCAGTGTCATTAACTAAACCA

```


```
$less families.stk

# STOCKHOLM 1.0
#=GF ID    rnd-1_family-2
#=GF DE    RepeatModeler Generated - rnd-1_family-2, RepeatScout: [ Index = R=152, RS Size = 101, Refiner Input Size = 100, Final Multiple Alignment Size = 100 ]
#=GF SQ    101
#=GC RF    xxxxxxxxxxxxxxxxxx.x..xxxxxxxx.....xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.x......x..xxxx.........x......xxxxxxxxxxx..xxxxxxx.x.x.x....x..xxxx........x.x...x.x..x....x......xxxxx.....xxxxxx.....xxxxxx.........xxx...x.xxxxxxxxxxxxxxxxxxxxx..xxxxxx....xxxxxxxxxxxxxxx......x..xxx.......xxxxxxxx..........xx...x.xxxxxxxxxxx..xxxxxxxxx
115_contig1822:165-333    .............................C.....ATTGGCTCAGGCCCGAACGACTCGACAACG.A......C..TCGG.........G......CATGAACGACT..CGTCATC.G.A.C....C..AAGG........C..........T....CAAGT..GACTT.....GATATC.....AGCCCG.........AGT...C.CAGAAGACTCAAAATTGGCAT..GGCCCT....GAACGACTCGAAATC......A..ACC.......CGAGATTG..........GA...C.GACTCGACATC..GGGCCAGAC
115_contig1822:676-840    ......................................GGCCCGGGCCCGAACGACTCGACAACA.A......C..TCGG.........G......CATGAACGACT..CGTCATC.G.A.C....C..AGGG........C..........T....CAAGT..GACTT.....GATATC.....AGCCTG.........AGC...C.CAGAAGACTCAAAATTGGCAT..GGCCCT....GAACGACTCGAAATC......A..ACC.......TGAGATTG..........GA...C.GACTCGACATC..GACCCAGAC

```




### run repeatmask
```
 RepeatMasker -lib consensi.fa -html -gff -dir repeat ../Samples_contigs_cdhit_filt.fa
RepeatMasker version open-4.0.9
Search Engine: NCBI/RMBLAST [ 2.6.0+ ]
Master RepeatMasker Database: /home/wuzhikun/anaconda3/envs/Assembly/share/RepeatMasker/Libraries/RepeatMaskerLib.embl ( Complete Database: CONS-Dfam_3.0 )
Custom Repeat Library: consensi.fa

```


output mask contig
```
$ head  Samples_contigs_cdhit_filt.fa.masked
>119_contig1773
CTAAAATTAGTTTTTGTTTAATAATTTTTTTATAGTGNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
CTCTATGATCAAATTGATATTAAGATACAAAGTTCACATGTTAGTTTGTC
ATTAAGTGATGCACCAAGTAATTATCTATGTAAATAAGTTATGCTTAAAA
ACATAAGTACGTATAAGATTTAAGGGGGAGTGTTGACATAAAGGGAAACA
ATGAAACAAAGAAGAAATGAGTAACTAAGTTAAAAACATTTTGATATGCT
TTTATGTCATTTGTGCTCTTACTAGGAAGGATGCAAAAGGTGCATATCTG
GATCCGAATTGCAGTAACCATTTCGAAAGTGTCTATGGAATGCTCTCATT

```