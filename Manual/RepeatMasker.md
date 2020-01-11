

## repeatmask

```
$ trf


Please use: trf File Match Mismatch Delta PM PI Minscore MaxPeriod [options]

Where: (all weights, penalties, and scores are positive)
  File = sequences input file
  Match  = matching weight
  Mismatch  = mismatching penalty
  Delta = indel penalty
  PM = match probability (whole number)
  PI = indel probability (whole number)
  Minscore = minimum alignment score to report
  MaxPeriod = maximum period size to report
  [options] = one or more of the following:
        -m        masked sequence file
        -f        flanking sequence
        -d        data file
        -h        suppress html output
        -r        no redundancy elimination
        -l <n>    maximum TR length expected (in millions) (eg, -l 3 or -l=3 for 3 million)
                  Human genome HG38 would need -l 6
        -ngs      more compact .dat output on multisequence files, returns 0 on success.
                  Output is printed to the screen, not a file. You may pipe input in with
                  this option using - for file name. Short 50 flanks are appended to .dat
                  output.

See more information on the TRF Unix Help web page: https://tandem.bu.edu/trf/trf.unix.help.html

Note the sequence file should be in FASTA format:

>Name of sequence
aggaaacctgccatggcctcctggtgagctgtcctcatccactgctcgctgcctctccag
atactctgacccatggatcccctgggtgcagccaagccacaatggccatggcgccgctgt
actcccacccgccccaccctcctgatcctgctatggacatggcctttccacatccctgtg

```





### repeatmask
```
$ RepeatMasker
RepeatMasker version open-4.0.9
No query sequence file indicated

NAME
    RepeatMasker - Mask repetitive DNA

SYNOPSIS
      RepeatMasker [-options] <seqfiles(s) in fasta format>

DESCRIPTION
    The options are:

    -h(elp)
        Detailed help

    Default settings are for masking all type of repeats in a primate
    sequence.

    -e(ngine) [crossmatch|wublast|abblast|ncbi|rmblast|hmmer]
        Use an alternate search engine to the default. Note: 'ncbi' and
        'rmblast' are both aliases for the rmblastn search engine engine.
        The generic NCBI blastn program is not sensitive enough for use with
        RepeatMasker at this time.

    -pa(rallel) [number]
        The number of processors to use in parallel (only works for batch
        files or sequences over 50 kb)

    -s  Slow search; 0-5% more sensitive, 2-3 times slower than default

    -q  Quick search; 5-10% less sensitive, 2-5 times faster than default

    -qq Rush job; about 10% less sensitive, 4->10 times faster than default
        (quick searches are fine under most circumstances) repeat options

    -nolow
        Does not mask low_complexity DNA or simple repeats

    -noint
        Only masks low complex/simple repeats (no interspersed repeats)

    -norna
        Does not mask small RNA (pseudo) genes

    -alu
        Only masks Alus (and 7SLRNA, SVA and LTR5)(only for primate DNA)

    -div [number]
        Masks only those repeats < x percent diverged from consensus seq

    -lib [filename]
        Allows use of a custom library (e.g. from another species)

    -cutoff [number]
        Sets cutoff score for masking repeats when using -lib (default 225)

    -species <query species>
        Specify the species or clade of the input sequence. The species name
        must be a valid NCBI Taxonomy Database species name and be contained
        in the RepeatMasker repeat database. Some examples are:

          -species human
          -species mouse
          -species rattus
          -species "ciona savignyi"
          -species arabidopsis

        Other commonly used species:

        mammal, carnivore, rodentia, rat, cow, pig, cat, dog, chicken, fugu,
        danio, "ciona intestinalis" drosophila, anopheles, worm, diatoaea,
        artiodactyl, arabidopsis, rice, wheat, and maize

    Contamination options

    -is_only
        Only clips E coli insertion elements out of fasta and .qual files

    -is_clip
        Clips IS elements before analysis (default: IS only reported)

    -no_is
        Skips bacterial insertion element check

    Running options

    -gc [number]
        Use matrices calculated for 'number' percentage background GC level

    -gccalc
        RepeatMasker calculates the GC content even for batch files/small
        seqs

    -frag [number]
        Maximum sequence length masked without fragmenting (default 60000)

    -nocut
        Skips the steps in which repeats are excised

    -noisy
        Prints search engine progress report to screen (defaults to .stderr
        file)

    -nopost
        Do not postprocess the results of the run ( i.e. call ProcessRepeats
        ). NOTE: This options should only be used when ProcessRepeats will
        be run manually on the results.

    output options

    -dir [directory name]
        Writes output to this directory (default is query file directory,
        "-dir ." will write to current directory).

    -a(lignments)
        Writes alignments in .align output file

    -inv
        Alignments are presented in the orientation of the repeat (with
        option -a)

    -lcambig
        Outputs ambiguous DNA transposon fragments using a lower case name.
        All other repeats are listed in upper case. Ambiguous fragments
        match multiple repeat elements and can only be called based on
        flanking repeat information.

    -small
        Returns complete .masked sequence in lower case

    -xsmall
        Returns repetitive regions in lowercase (rest capitals) rather than
        masked

    -x  Returns repetitive regions masked with Xs rather than Ns

    -poly
        Reports simple repeats that may be polymorphic (in file.poly)

    -source
        Includes for each annotation the HSP "evidence". Currently this
        option is only available with the "-html" output format listed
        below.

    -html
        Creates an additional output file in xhtml format.

    -ace
        Creates an additional output file in ACeDB format

    -gff
        Creates an additional Gene Feature Finding format output

    -u  Creates an additional annotation file not processed by
        ProcessRepeats

    -xm Creates an additional output file in cross_match format (for
        parsing)

    -no_id
        Leaves out final column with unique ID for each element (was
        default)

    -e(xcln)
        Calculates repeat densities (in .tbl) excluding runs of >=20 N/Xs in
        the query

SEE ALSO
        Crossmatch, ProcessRepeats

COPYRIGHT
    Copyright 2007-2014 Arian Smit, Institute for Systems Biology

AUTHORS
    Arian Smit <asmit@systemsbiology.org>

    Robert Hubley <rhubley@systemsbiology.org>

```



### run RepeatMasker
```
$ RepeatMasker -parallel 30 -species arabidopsis -html -gff -dir repeat TAIR10_chr_all.fas
RepeatMasker version open-4.0.9
Search Engine: NCBI/RMBLAST [ 2.6.0+ ]
Rebuilding RepeatMaskerLib.embl master library
  - Read in 9 sequences from /home/wuzhikun/anaconda3/envs/Assembly/share/RepeatMasker/Libraries/Artefacts.embl
  - Read in 6235 sequences from /home/wuzhikun/anaconda3/envs/Assembly/share/RepeatMasker/Libraries/Dfam.embl
RepeatMaskerLib.embl: 6244 total sequences.
Building FASTA version...Master RepeatMasker Database: /home/wuzhikun/anaconda3/envs/Assembly/share/RepeatMasker/Libraries/RepeatMaskerLib.embl ( Complete Database: CONS-Dfam_3.0 )

```



libraries:
```
wuzhikun@mu01 15:24:42 ^_^ /home/wuzhikun/anaconda3/envs/Assembly/share/RepeatMasker/Libraries 
$ l
total 1.9G
-rwxrwxr-x 3  25K Dec  9 22:45 Artefacts.embl
drwxrwxr-x 1 4.0K Dec 30 15:24 CONS-Dfam_3.0
-rw-rw-r-- 3  21M Dec  9 22:45 Dfam.embl
-rw-rw-r-- 3 1.6G Dec  9 22:45 Dfam.hmm
-rw-rw-r-- 3  214 Dec  9 22:45 README.meta
-rwxrwxr-x 3  22M Dec  9 22:45 RepeatAnnotationData.pm
-rw-rw-r-- 1 9.9M Dec 30 15:24 RepeatMasker.lib
-rw-rw-r-- 1  20M Dec 30 15:24 RepeatMaskerLib.embl
-rw-rw-r-- 3  18M Dec  9 22:45 RepeatPeps.lib
-rw-rw-r-- 3 2.8M Dec  9 22:45 RepeatPeps.lib.phr
-rw-rw-r-- 3 142K Dec  9 22:45 RepeatPeps.lib.pin
-rw-rw-r-- 3  16M Dec  9 22:45 RepeatPeps.lib.psq
-rw-rw-r-- 3 5.5K Dec  9 22:45 RepeatPeps.readme
-rw-rw-r-- 3  18M Dec  9 22:44 RMRBMeta.embl
-rw-rw-r-- 3 109M Dec  9 22:44 taxonomy.dat

```




run repeatmask
```
$ tree repeat/
repeat/
├── TAIR10_chr_all.fas.cat.gz
├── TAIR10_chr_all.fas.masked
├── TAIR10_chr_all.fas.out
├── TAIR10_chr_all.fas.out.gff
├── TAIR10_chr_all.fas.out.html
└── TAIR10_chr_all.fas.tbl

```


```
$ head TAIR10_chr_all.fas.out
   SW   perc perc perc  query         position in query              matching       repeat           position in repeat
score   div. del. ins.  sequence      begin    end          (left)   repeat         class/family   begin  end    (left)    ID

   49   13.1  0.0  7.5  1                    1      115 (30427556) + A-rich         Low_complexity      1    107    (0)     1  
   22   10.0  0.0  0.0  1                 1066     1097 (30426574) + (C)n           Simple_repeat       1     32    (0)     2  
   15   17.1  0.0  0.0  1                 1155     1187 (30426484) + (TTTCTT)n      Simple_repeat       1     33    (0)     3  
   28    8.4  0.0  0.0  1                 4291     4328 (30423343) + (AT)n          Simple_repeat       1     38    (0)     4  
   16    9.3  0.0  0.0  1                 5680     5702 (30421969) + (T)n           Simple_repeat       1     23    (0)     5  
   36    0.0  0.0  0.0  1                 8669     8699 (30418972) + (CT)n          Simple_repeat       1     31    (0)     6  
   25   20.7  2.9  2.9  1                 9961    10030 (30417641) + (AT)n          Simple_repeat       1     70    (0)     7  

```


```
$ head TAIR10_chr_all.fas.out.gff
##gff-version 2
##date 2019-12-30
##sequence-region TAIR10_chr_all.fas
1 RepeatMasker  similarity  1 115 13.1  + . Target "Motif:A-rich" 1 107
1 RepeatMasker  similarity  1066  1097  10.0  + . Target "Motif:(C)n" 1 32
1 RepeatMasker  similarity  1155  1187  17.1  + . Target "Motif:(TTTCTT)n" 1 33
1 RepeatMasker  similarity  4291  4328   8.4  + . Target "Motif:(AT)n" 1 38
1 RepeatMasker  similarity  5680  5702   9.3  + . Target "Motif:(T)n" 1 23
1 RepeatMasker  similarity  8669  8699   0.0  + . Target "Motif:(CT)n" 1 31
1 RepeatMasker  similarity  9961  10030 20.7  + . Target "Motif:(AT)n" 1 70

```


```
==================================================
file name: TAIR10_chr_all.fas       
sequences:             7
total length:  119667750 bp  (119482146 bp excl N/X-runs)
GC level:         36.06 %
bases masked:    2211370 bp ( 1.85 %)


==================================================
               number of      length   percentage
               elements*    occupied  of sequence
--------------------------------------------------
Retroelements            0            0 bp    0.00 %



Small RNA:               0            0 bp    0.00 %

Satellites:              0            0 bp    0.00 %
Simple repeats:      40167      1627651 bp    1.36 %
Low complexity:      10698       585594 bp    0.49 %

```