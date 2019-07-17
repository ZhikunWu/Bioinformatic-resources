## [MUMmer4](https://github.com/mummer4/mummer)

### [MUMmer4 manual](https://github.com/mummer4/mummer/blob/master/MANUAL.md)

### nucmer

```
$ nucmer --help
Usage: nucmer [options] ref:path qry:path+

nucmer generates nucleotide alignments between two mutli-FASTA input
files. The out.delta output file lists the distance between insertions
and deletions that produce maximal scoring alignments between each
sequence. The show-* utilities know how to read this format.

By default, nucmer uses anchor matches that are unique in in the
reference but not necessarily unique in the query. See --mum and
--maxmatch for different bevahiors.

Options (default value in (), *required):
     --mum                                Use anchor matches that are unique in both the reference and query (false)
     --maxmatch                           Use all anchor matches regardless of their uniqueness (false)
 -b, --breaklen=uint32                    Set the distance an alignment extension will attempt to extend poor scoring regions before giving up (200)
 -c, --mincluster=uint32                  Sets the minimum length of a cluster of matches (65)
 -D, --diagdiff=uint32                    Set the maximum diagonal difference between two adjacent anchors in a cluster (5)
 -d, --diagfactor=double                  Set the maximum diagonal difference between two adjacent anchors in a cluster as a differential fraction of the gap length (0.12)
     --noextend                           Do not perform cluster extension step (false)
 -f, --forward                            Use only the forward strand of the Query sequences (false)
 -g, --maxgap=uint32                      Set the maximum gap between two adjacent matches in a cluster (90)
 -l, --minmatch=uint32                    Set the minimum length of a single exact match (20)
 -L, --minalign=uint32                    Minimum length of an alignment, after clustering and extension (0)
     --nooptimize                         No alignment score optimization, i.e. if an alignment extension reaches the end of a sequence, it will not backtrack to optimize the alignment score and instead terminate the alignment at the end of the sequence (false)
 -r, --reverse                            Use only the reverse complement of the Query sequences (false)
     --nosimplify                         Don't simplify alignments by removing shadowed clusters. Use this option when aligning a sequence to itself to look for repeats (false)
 -p, --prefix=PREFIX                      Write output to PREFIX.delta (out)
     --delta=PATH                         Output delta file to PATH (instead of PREFIX.delta)
     --sam-short=PATH                     Output SAM file to PATH, short format
     --sam-long=PATH                      Output SAM file to PATH, long format
     --save=PREFIX                        Save suffix array to files starting with PREFIX
     --load=PREFIX                        Load suffix array from file starting with PREFIX
     --batch=BASES                        Proceed by batch of chunks of BASES from the reference
 -t, --threads=NUM                        Use NUM threads (# of cores)
 -U, --usage                              Usage
 -h, --help                               This message
     --full-help                          Detailed help
 -V, --version                            Version

```


```
$ nucmer --threads 40 -l 50  -c 500  --maxmatch --delta test.delta --save human  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa M628-0.contig_test.fa
```

save the database
```
-rw-rw-r-- 1    49 Jul 11 18:04 human.aux
-rw-rw-r-- 1   18G Jul 11 18:06 human.isa
-rw-rw-r-- 1  8.1M Jul 11 18:06 human.kmer
-rw-rw-r-- 1  2.9G Jul 11 18:05 human.lcp
-rw-rw-r-- 1   18G Jul 11 18:05 human.sa

```

output file:
```
$ head test.delta
/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2/M628-0.contig_test.fa
NUCMER
>1 ctg2679 248956422 6801
13060002 13066915 6801 15 144 144 0
20
2
5
4
2
3
```

### dnadiff

```
$ dnadiff --help

  USAGE: dnadiff  [options]  <reference>  <query>
    or   dnadiff  [options]  -d <delta file>

  DESCRIPTION:
    Run comparative analysis of two sequence sets using nucmer and its
    associated utilities with recommended parameters. See MUMmer
    documentation for a more detailed description of the
    output. Produces the following output files:

    .report  - Summary of alignments, differences and SNPs
    .delta   - Standard nucmer alignment output
    .1delta  - 1-to-1 alignment from delta-filter -1
    .mdelta  - M-to-M alignment from delta-filter -m
    .1coords - 1-to-1 coordinates from show-coords -THrcl .1delta
    .mcoords - M-to-M coordinates from show-coords -THrcl .mdelta
    .snps    - SNPs from show-snps -rlTHC .1delta
    .rdiff   - Classified ref breakpoints from show-diff -rH .mdelta
    .qdiff   - Classified qry breakpoints from show-diff -qH .mdelta
    .unref   - Unaligned reference IDs and lengths (if applicable)
    .unqry   - Unaligned query IDs and lengths (if applicable)

  MANDATORY:
    reference       Set the input reference multi-FASTA filename
    query           Set the input query multi-FASTA filename
      or
    delta file      Unfiltered .delta alignment file from nucmer

  OPTIONS:
    -d|delta        Provide precomputed delta file for analysis
    -h
    --help          Display help information and exit
    -p|prefix       Set the prefix of the output files (default "out")
    -V
    --version       Display the version information and exit

```


```
$ dnadiff -d test.delta
Filtering alignments
Extracting alignment coordinates
Analyzing SNPs
Extracting alignment breakpoints
Generating report file

```

output files:
```
-rw-rw-r-- 1   155 Jul 11 18:38 out.1coords
-rw-rw-r-- 1  1.3K Jul 11 18:38 out.1delta
-rw-rw-r-- 1  1.7K Jul 11 17:41 out.delta
-rw-rw-r-- 1   233 Jul 11 18:38 out.mcoords
-rw-rw-r-- 1  1.7K Jul 11 18:38 out.mdelta
-rw-rw-r-- 1    45 Jul 11 18:39 out.qdiff
-rw-rw-r-- 1   181 Jul 11 18:39 out.rdiff
-rw-rw-r-- 1  4.2K Jul 11 18:40 out.report
-rw-rw-r-- 1   20K Jul 11 18:39 out.snps
-rw-rw-r-- 1   196 Jul 11 18:40 out.unqry
-rw-rw-r-- 1  5.4K Jul 11 18:40 out.unref
```

```
$ head  out.1coords
13159877	13166790	15	6801	6914	6787	97.92	248956422	6801	0.00 99.79	1	ctg2679
12402210	12410447	8039	1	8238	8039	97.32	50818468	8076	0.02 99.54	22	ctg2681

```

```
$ head out.mcoords
13060002	13066915	6801	15	6914	6787	97.92	248956422	6801	0.00 99.79	1	ctg2679
13159877	13166790	15	6801	6914	6787	97.92	248956422	6801	0.00 99.79	1	ctg2679
12402210	12410447	8039	1	8238	8039	97.32	50818468	8076	0.02 99.54	22	ctg2681

```

```
$ head out.qdiff
ctg2679	BRK	1	14	14
ctg2681	BRK	8040	8076	37
```

```
$ head out.rdiff
1	BRK	1	13060001	13060001
1	DUP	13060002	13066915	6914
1	BRK	13066916	13159876	92961
1	BRK	13166791	248956422	235789632
22	BRK	1	12402209	12402209
22	BRK	12410448	50818468	38408021

```

```
$ head out.report
/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/NanoTrio/Assembly/wtdbg2/M628-0.contig_test.fa
NUCMER

                               [REF]                [QRY]
[Sequences]
TotalSeqs                        194                   10
AlignedSeqs                 2(1.03%)            2(20.00%)
UnalignedSeqs            192(98.97%)            8(80.00%)

[Bases]
```



### mummerplot
```
$ mummerplot --help

  USAGE: mummerplot  [options]  <match file>

  DESCRIPTION:
    mummerplot generates plots of alignment data produced by mummer, nucmer,
    promer or show-tiling by using the GNU gnuplot utility. After generating
    the appropriate scripts and datafiles, mummerplot will attempt to run
    gnuplot to generate the plot. If this attempt fails, a warning will be
    output and the resulting .gp and .[frh]plot files will remain so that the
    user may run gnuplot independently. If the attempt succeeds, either an x11
    window will be spawned or an additional output file will be generated
    (.ps or .png depending on the selected terminal). Feel free to edit the
    resulting gnuplot script (.gp) and rerun gnuplot to change line thinkness,
    labels, colors, plot size etc.

  MANDATORY:
    match file      Set the alignment input to 'match file'
                    Valid inputs are from mummer, nucmer, promer and
                    show-tiling (.out, .cluster, .delta and .tiling)

  OPTIONS:
    -b|breaklen     Highlight alignments with breakpoints further than
                    breaklen nucleotides from the nearest sequence end
    --[no]color     Color plot lines with a percent similarity gradient or
                    turn off all plot color (default color by match dir)
                    If the plot is very sparse, edit the .gp script to plot
                    with 'linespoints' instead of 'lines'
    -c
    --[no]coverage  Generate a reference coverage plot (default for .tiling)
    --depend        Print the dependency information and exit
    -f
    --filter        Only display .delta alignments which represent the "best"
                    hit to any particular spot on either sequence, i.e. a
                    one-to-one mapping of reference and query subsequences
    -h
    --help          Display help information and exit
    -l
    --layout        Layout a .delta multiplot in an intelligible fashion,
                    this option requires the -R -Q options
    --fat           Layout sequences using fattest alignment only
    -p|prefix       Set the prefix of the output files (default 'out')
    -rv             Reverse video for x11 plots
    -r|IdR          Plot a particular reference sequence ID on the X-axis
    -q|IdQ          Plot a particular query sequence ID on the Y-axis
    -R|Rfile        Plot an ordered set of reference sequences from Rfile
    -Q|Qfile        Plot an ordered set of query sequences from Qfile
                    Rfile/Qfile Can either be the original DNA multi-FastA
                    files or lists of sequence IDs, lens and dirs [ /+/-]
    -r|rport        Specify the port to send reference ID and position on
                    mouse double click in X11 plot window
    -q|qport        Specify the port to send query IDs and position on mouse
                    double click in X11 plot window
    -s|size         Set the output size to small, medium or large
                    --small --medium --large (default 'small')
    -S
    --SNP           Highlight SNP locations in each alignment
    -t|terminal     Set the output terminal to x11, postscript or png
                    --x11 --postscript --png (default 'x11')
    -t|title        Specify the gnuplot plot title (default none)
    -x|xrange       Set the xrange for the plot '[min:max]'
    -y|yrange       Set the yrange for the plot '[min:max]'
    -V
    --version       Display the version information and exit
```


```
$ mummerplot test.delta
gnuplot 4.6 patchlevel 2
Reading delta file test.delta
Writing plot files out.fplot, out.rplot
Writing gnuplot script out.gp
Forking mouse listener
Rendering plot to screen
WARNING: Unable to query clipboard with xclip
WARNING: Unable to run 'false -geometry 500x500+0+0 -title mummerplot out.gp', Invalid argument

```


output files:
```
-rw-rw-r-- 1   111 Jul 11 19:44 out.fplot
-rw-rw-r-- 1  6.5K Jul 11 19:44 out.gp

```


```
$ mummerplot M628-0.contig_aln_genome.delta
gnuplot 4.6 patchlevel 0
Reading delta file M628-0.contig_aln_genome.delta
Writing plot files out.fplot, out.rplot
Writing gnuplot script out.gp
Forking mouse listener
Rendering plot to screen
WARNING: Unable to run 'false -geometry 500x500+0+0 -title mummerplot out.gp', Invalid argument
```


