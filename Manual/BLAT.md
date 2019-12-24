## BLAT

### [BLAT manual](https://genome.ucsc.edu/goldenPath/help/blatSpec.html)

### BLAT tools

* pslSort – combines and sorts the output of multiple blat runs. The blat default output format is psl.
* pslReps – selects the best alignments for a particular query sequence, using a "near best in genome" approach.
* pslPretty – converts alignments from psl format, which is a tab-delimited format that does not include the bases themselves, to a more readable alignment format.
* faToTwoBit – converts fasta format sequence files to the dense, randomly accessible .2bit format that gfClient can use.
* twoBitToFa – converts from .2bit format back to fasta format.
* faToNib – converts from fasta to the somewhat less dense, randomly accessible .nib format that predated .2bit format. Note that each .nib file can contain only a single sequence.
* nibFrag – converts portions of a .nib file back to fasta format.


### install fatotwobit and blat 
```
conda install -c bioconda blat

conda install -c bioconda ucsc-fatotwobit

conda install -c bioconda ucsc-pslsort
```

### parameters
```
$ faToTwoBit
faToTwoBit - Convert DNA from fasta to 2bit format
usage:
   faToTwoBit in.fa [in2.fa in3.fa ...] out.2bit
options:
   -long          use 64-bit offsets for index.   Allow for twoBit to contain more than 4Gb of sequence. 
                  NOT COMPATIBLE WITH OLDER CODE.
   -noMask        Ignore lower-case masking in fa file.
   -stripVersion  Strip off version number after '.' for GenBank accessions.
   -ignoreDups    Convert first sequence only if there are duplicate sequence
                  names.  Use 'twoBitDup' to find duplicate sequences.

```


1. Prepare the sequence for your twoBit file in a FASTA-formatted file (i.e. genome.fa).
Run the faToTwoBit program on your FASTA file:
```
faToTwoBit genome.fa genome.2bit
```

2. Use twoBitInfo to verify the sequences in this assembly and create a chrom.sizes file, which is useful to construct the big* files in later processing steps:
```
twoBitInfo genome.2bit stdout | sort -k2rn > genome.chrom.sizes
```

3. The twoBit commands can function with the .2bit file as a URL:
```
twoBitInfo -udcDir=. http://your-website.edu/~user/genome.2bit | sort -k2nr > genome.chrom.sizes
```

4. Sequence can be extracted from the .2bit file with the twoBitToFa command, for example:
```
twoBitToFa -seq=chr1 -udcDir=. http://your-website.edu/~user/genome.2bit stdout > genome.chr1.fa
```



```
faToTwoBit Homo_sapiens.GRCh38.dna.primary_assembly.fa Homo_sapiens.GRCh38.dna.primary_assembly.2bit
```



```
$ blat
blat - Standalone BLAT v. 36 fast sequence search command line tool
usage:
   blat database query [-ooc=11.ooc] output.psl
where:
   database and query are each either a .fa, .nib or .2bit file,
      or a list of these files with one file name per line.
   -ooc=11.ooc tells the program to load over-occurring 11-mers from
      an external file.  This will increase the speed
      by a factor of 40 in many cases, but is not required.
   output.psl is the name of the output file.
   Subranges of .nib and .2bit files may be specified using the syntax:
      /path/file.nib:seqid:start-end
   or
      /path/file.2bit:seqid:start-end
   or
      /path/file.nib:start-end
   With the second form, a sequence id of file:start-end will be used.
options:
   -t=type        Database type.  Type is one of:
                    dna - DNA sequence
                    prot - protein sequence
                    dnax - DNA sequence translated in six frames to protein
                  The default is dna.
   -q=type        Query type.  Type is one of:
                    dna - DNA sequence
                    rna - RNA sequence
                    prot - protein sequence
                    dnax - DNA sequence translated in six frames to protein
                    rnax - DNA sequence translated in three frames to protein
                  The default is dna.
   -prot          Synonymous with -t=prot -q=prot.
   -ooc=N.ooc     Use overused tile file N.ooc.  N should correspond to 
                  the tileSize.
   -tileSize=N    Sets the size of match that triggers an alignment.  
                  Usually between 8 and 12.
                  Default is 11 for DNA and 5 for protein.
   -stepSize=N    Spacing between tiles. Default is tileSize.
   -oneOff=N      If set to 1, this allows one mismatch in tile and still
                  triggers an alignment.  Default is 0.
   -minMatch=N    Sets the number of tile matches.  Usually set from 2 to 4.
                  Default is 2 for nucleotide, 1 for protein.
   -minScore=N    Sets minimum score.  This is the matches minus the 
                  mismatches minus some sort of gap penalty.  Default is 30.
   -minIdentity=N Sets minimum sequence identity (in percent).  Default is
                  90 for nucleotide searches, 25 for protein or translated
                  protein searches.
   -maxGap=N      Sets the size of maximum gap between tiles in a clump.  Usually
                  set from 0 to 3.  Default is 2. Only relevent for minMatch > 1.
   -noHead        Suppresses .psl header (so it's just a tab-separated file).
   -makeOoc=N.ooc Make overused tile file. Target needs to be complete genome.
   -repMatch=N    Sets the number of repetitions of a tile allowed before
                  it is marked as overused.  Typically this is 256 for tileSize
                  12, 1024 for tile size 11, 4096 for tile size 10.
                  Default is 1024.  Typically comes into play only with makeOoc.
                  Also affected by stepSize: when stepSize is halved, repMatch is
                  doubled to compensate.
   -mask=type     Mask out repeats.  Alignments won't be started in masked region
                  but may extend through it in nucleotide searches.  Masked areas
                  are ignored entirely in protein or translated searches. Types are:
                    lower - mask out lower-cased sequence
                    upper - mask out upper-cased sequence
                    out   - mask according to database.out RepeatMasker .out file
                    file.out - mask database according to RepeatMasker file.out
   -qMask=type    Mask out repeats in query sequence.  Similar to -mask above, but
                  for query rather than target sequence.
   -repeats=type  Type is same as mask types above.  Repeat bases will not be
                  masked in any way, but matches in repeat areas will be reported
                  separately from matches in other areas in the psl output.
   -minRepDivergence=NN   Minimum percent divergence of repeats to allow 
                  them to be unmasked.  Default is 15.  Only relevant for 
                  masking using RepeatMasker .out files.
   -dots=N        Output dot every N sequences to show program's progress.
   -trimT         Trim leading poly-T.
   -noTrimA       Don't trim trailing poly-A.
   -trimHardA     Remove poly-A tail from qSize as well as alignments in 
                  psl output.
   -fastMap       Run for fast DNA/DNA remapping - not allowing introns, 
                  requiring high %ID. Query sizes must not exceed 5000.
   -out=type      Controls output file format.  Type is one of:
                    psl - Default.  Tab-separated format, no sequence
                    pslx - Tab-separated format with sequence
                    axt - blastz-associated axt format
                    maf - multiz-associated maf format
                    sim4 - similar to sim4 format
                    wublast - similar to wublast format
                    blast - similar to NCBI blast format
                    blast8- NCBI blast tabular format
                    blast9 - NCBI blast tabular format with comments
   -fine          For high-quality mRNAs, look harder for small initial and
                  terminal exons.  Not recommended for ESTs.
   -maxIntron=N  Sets maximum intron size. Default is 750000.
   -extendThroughN  Allows extension of alignment through large blocks of Ns.

```

### run blat
            

### output with 
```
$ blat /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa 9_127322405_127322597_DEL.fasta 9_127322405_1273
22597_DEL_align.txt  -t=dna -q=dna  -out=blast8 Loaded 3099750718 letters in 194 sequences
Searched 67885 bases in 3 sequences
```

out file with blast table format
```
1a8ce359-6d5a-4ee7-ba46-dfd19cdccd40    9       92.82   348     6       14      12283   12614   127317407       127317063       1.1e-139        493.0
1a8ce359-6d5a-4ee7-ba46-dfd19cdccd40    9       95.29   276     5       4       8886    9153    127320951       127320676       4.7e-131        464.0
```


out file with psl format
```
blat /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa 9_127322405_127322597_DEL.fasta 9_127322405_127322597_DEL_align.psl  -t=dna -q=dn
a  -out=psl
```

```
psLayout version 3

match   mis-    rep.    N's     Q gap   Q gap   T gap   T gap   strand  Q               Q       Q       Q       T               T       T       T       block   blockSizes
      qStarts  tStarts        match   match           count   bases   count   bases           name            size    start   end     name            size    start   end     count
---------------------------------------------------------------------------------------------------------------------------------------------------------------
84      7       0       0       1       1       3       137     +       1a8ce359-6d5a-4ee7-ba46-dfd19cdccd40    19199   12014   12106   X       156040895       3609215 36
09443 5       22,23,23,5,18,  12014,12036,12060,12083,12088,  3609215,3609238,3609261,3609322,3609425,80      1       0       0       2       31      5       38      +       1a8ce359-6d5a-4ee7-ba46-dfd19cdccd40    19199   10340   10452   X       156040895       46717444
        46717563        6       15,14,15,11,22,4,       10340,10355,10369,10385,10426,10448,    46717444,46717460,46717475,46717492,46717536,46717559,
82      0       0       0       4       69      3       28      +       1a8ce359-6d5a-4ee7-ba46-dfd19cdccd40    19199   3908    4059    X       156040895       16399087
        16399197        5       14,27,15,11,15, 3908,3977,4010,4032,4044,       16399087,16399115,16399147,16399171,16399182,


```


blast output
```
Searching.done
                                                                 Score    E
Sequences producing significant alignments:                      (bits) Value

7                                                                     593   e-170
7                                                                     480   e-136
7                                                                     460   e-129
7                                                                     454   e-128

```



blast8 output
```
426dd044-5c31-4f11-811a-3b90b199713a    7       93.22   398     13      13      3808    4195    99435225        99435618        6.
8e-170        593.0426dd044-5c31-4f11-811a-3b90b199713a    7       93.07   332     5       13      4336    4653    99435757        99436084        9.
3e-136        480.0426dd044-5c31-4f11-811a-3b90b199713a    7       94.67   300     5       10      9351    9642    98695394        98695690        1.
1e-129        460.0426dd044-5c31-4f11-811a-3b90b199713a    7       93.01   286     7       6       2681    2960    99434080        99434358        4.
8e-128        454.0
```


blast9 output
```
# BLAT 36 [2009/02/26]
# Query: 426dd044-5c31-4f11-811a-3b90b199713a
# Database: /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.2bit
# Fields: Query id, Subject id, % identity, alignment length, mismatches, gap openings, q. start, q. end, s. start, s. end, e-valu
426dd044-5c31-4f11-811a-3b90b199713a    7       93.22   398     13      13      3808    4195    99435225        99435618        6.
8e-170        593.0426dd044-5c31-4f11-811a-3b90b199713a    7       93.07   332     5       13      4336    4653    99435757        99436084        9.
3e-136        480.0426dd044-5c31-4f11-811a-3b90b199713a    7       94.67   300     5       10      9351    9642    98695394        98695690        1.
1e-129        460.0426dd044-5c31-4f11-811a-3b90b199713a    7       93.01   286     7       6       2681    2960    99434080        99434358        4.
8e-128        454.0
```


maf output
```
##maf version=1 scoring=blastz
a score=455.000000
s 1                                    15498085 5 + 248956422 ttttt
s 426dd044-5c31-4f11-811a-3b90b199713a      325 5 -     14162 ttttt

a score=3511.000000
s 1                                    15498092 51 + 248956422 ttttgttttttgagaga--gtctcattctgtcacccaggctggagtgcagtgg
s 426dd044-5c31-4f11-811a-3b90b199713a      331 52 -     14162 tttt-ttttttgagacagggtctcattctgtcactcaggctggagtgcagtgg

a score=1155.000000
s 1                                    15498600 12 + 248956422 ctcaggctgtca
s 426dd044-5c31-4f11-811a-3b90b199713a      417 12 -     14162 ctcaggctgtca


```

wublast output
```
Sequences producing High-scoring Segment Pairs:              Score  P(N)      N

7                                                             1523  6.6e-262 2515
3                                                              868  1.3e-145 2017
11                                                             846  1.2e-141 2113
9                                                              799  2.6e-133 2152
15                                                             716  1.9e-118 1988
14                                                             702  4.5e-116 1849
1                                                              700  1.3e-115 2536
4                                                              697  3.5e-115 1696


```


### select best alignment

install

```
conda install -c bioconda ucsc-pslreps
```



```
$ pslReps
pslReps - Analyze repeats and generate genome-wide best alignments from a
sorted set of local alignments
usage:
    pslReps in.psl out.psl out.psr
where:
    in.psl is an alignment file generated by psLayout and sorted by pslSort
    out.psl is the best alignment output
    out.psr contains repeat info
options:
    -nohead            Don't add PSL header.
    -ignoreSize        Will not weigh as much in favor of larger alignments.
    -noIntrons         Will not penalize for not having introns when calculating
                       size factor.
    -singleHit         Takes single best hit, not splitting into parts.
    -minCover=0.N      Minimum coverage to output.  Default is 0.
    -ignoreNs          Ignore Ns when calculating minCover.
    -minAli=0.N        Minimum alignment ratio.  Default is 0.93.
    -nearTop=0.N       How much can deviate from top and be taken.
                       Default is 0.01.
    -minNearTopSize=N  Minimum size of alignment that is near top
                       for alignment to be kept.  Default 30.
    -coverQSizes=file  Tab-separate file with effective query sizes.
                       When used with -minCover, this allows polyAs
                       to be excluded from the coverage calculation.

```

run pslReps
```
pslReps  M517_7_98694448_dup_test.psl M517_7_98694448_dup_test-1.psl M517_7_98694448_dup_test.psr
```

output file:
```
psLayout version 3

match   mis-    rep.    N's     Q gap   Q gap   T gap   T gap   strand  Q               Q       Q       Q       T               T       T       T       block   blockSizes      qStar
        match   match           count   bases   count   bases           name            size    start   end     name            size    start   end     count
---------------------------------------------------------------------------------------------------------------------------------------------------------------
6216    160     0       0       162     5326    212     2705837 +       426dd044-5c31-4f11-811a-3b90b199713a    14162   2449    14151   7       159345973       95988105        98700
8490    241     0       0       197     5259    298     1703737 +       426dd044-5c31-4f11-811a-3b90b199713a    14162   29      14019   7       159345973       99431285        1011
```


### pslPretty

install
```
conda install -c bioconda ucsc-pslpretty
```

parameters
```
$ pslPretty
pslPretty - Convert PSL to human-readable output
usage:
   pslPretty in.psl target.lst query.lst pretty.out
options:
   -axt             Save in format like Scott Schwartz's axt format.
                    Note gaps in both sequences are still allowed in the
                    output, which not all axt readers will expect.
   -dot=N           Output a dot every N records.
   -long            Don't abbreviate long inserts.
   -check=fileName  Output alignment checks to filename.
It's recommended that the psl file be sorted by target if it contains
multiple targets; otherwise, this will be extremely slow. The target and query
lists can be fasta, 2bit or nib files, or a list of these files, one per line.

```


