## [mummer](Ultra-fast alignment of large-scale DNA and protein sequences)

### [最新最详细的MUMmer中文使用说明](https://www.plob.org/article/11355.html)
### [mummer manual](http://mummer.sourceforge.net/manual/)
### [mummer example](http://mummer.sourceforge.net/examples/)

### install mummer

```
$ conda install -c bioconda mummer
```

### run mummer 

#### mummer parameters
```
$ mummer -h
Usage: mummer [options] <reference-file> <query-files>

Find and output (to stdout) the positions and length of all
sufficiently long maximal matches of a substring in
<query-file> and <reference-file>

Options:
-mum           compute maximal matches that are unique in both sequences
-mumcand       same as -mumreference
-mumreference  compute maximal matches that are unique in the reference-
               sequence but not necessarily in the query-sequence (default)
-maxmatch      compute all maximal matches regardless of their uniqueness
-n             match only the characters a, c, g, or t
               they can be in upper or in lower case
-l             set the minimum length of a match
               if not set, the default value is 20
-b             compute forward and reverse complement matches
-r             only compute reverse complement matches
-s             show the matching substrings
-c             report the query-position of a reverse complement match
               relative to the original query sequence
-F             force 4 column output format regardless of the number of
               reference sequence inputs
-L             show the length of the query sequences on the header line
-h             show possible options
-help          show possible options

```


#### run mummer
```
$ mummer -mum -l 30 GCF_900198195.1_Tjejuense_V1_genomic.fna GCF_900215725.1_PRJEB22476_genomic.fna > genome_compare.txt
# reading input file "GCF_900198195.1_Tjejuense_V1_genomic.fna" of length 4614879
# construct suffix tree for sequence of length 4614879
# (maximum reference length is 536870908)
# (maximum query length is 4294967295)
# process 46148 characters per dot
#....................................................................................................
# CONSTRUCTIONTIME mummer GCF_900198195.1_Tjejuense_V1_genomic.fna 1.74
# reading input file "GCF_900215725.1_PRJEB22476_genomic.fna" of length 1673084
# matching query-file "GCF_900215725.1_PRJEB22476_genomic.fna"
# against subject-file "GCF_900198195.1_Tjejuense_V1_genomic.fna"
# COMPLETETIME mummer GCF_900198195.1_Tjejuense_V1_genomic.fna 2.44
# SPACE mummer GCF_900198195.1_Tjejuense_V1_genomic.fna 6.07

```

output file:
```
> NZ_LT962469.1
> NZ_LT962470.1
 3805277    204244        42
 3805320    204287        34
 3805932    204911        55
 3806020    204999        30
 3807279    206349        30
 3808604    207640        30
 3808978    208031        41
> NZ_LT962471.1
> NZ_LT962472.1
> NZ_LT962473.1

```

#### change the reference and query genome
```
$ mummer -mum -l 30 GCF_900215725.1_PRJEB22476_genomic.fna GCF_900198195.1_Tjejuense_V1_genomic.fna >  genome_compare-1.txt
# reading input file "GCF_900215725.1_PRJEB22476_genomic.fna" of length 1673084
# construct suffix tree for sequence of length 1673084
# (maximum reference length is 536870908)
# (maximum query length is 4294967295)
# process 16730 characters per dot
#....................................................................................................
# CONSTRUCTIONTIME mummer GCF_900215725.1_PRJEB22476_genomic.fna 0.36
# reading input file "GCF_900198195.1_Tjejuense_V1_genomic.fna" of length 4614879
# matching query-file "GCF_900198195.1_Tjejuense_V1_genomic.fna"
# against subject-file "GCF_900215725.1_PRJEB22476_genomic.fna"
# COMPLETETIME mummer GCF_900215725.1_PRJEB22476_genomic.fna 1.39
# SPACE mummer GCF_900215725.1_PRJEB22476_genomic.fna 6.07

```

output file
```
$ cat genome_compare-1.txt
> NZ_LT899436.1
  NZ_LT962470.1    204244   3805277        42
  NZ_LT962470.1    204287   3805320        34
  NZ_LT962470.1    204911   3805932        55
  NZ_LT962470.1    204999   3806020        30
  NZ_LT962470.1    206349   3807279        30
  NZ_LT962470.1    207640   3808604        30
  NZ_LT962470.1    208031   3808978        41
```


### nucmer
```
$ nucmer -maxmatch -mincluste  90 -minmatch  20 --prefix GCA_002201585_to_GCA_002864125 GCA_002864125.1_ASM286412v1_genomic.fna GCA_002201585.1_ASM220158v1_genomic.fna
1: PREPARING DATA

```

### delta_filter

```
$ delta-filter -h 

USAGE: delta-filter  [options]  <deltafile>

-1            1-to-1 alignment allowing for rearrangements
              (intersection of -r and -q alignments)
-g            1-to-1 global alignment not allowing rearrangements
-h            Display help information
-i float      Set the minimum alignment identity [0, 100], default 0
-l int        Set the minimum alignment length, default 0
-m            Many-to-many alignment allowing for rearrangements
              (union of -r and -q alignments)
-q            Maps each position of each query to its best hit in
              the reference, allowing for reference overlaps
-r            Maps each position of each reference to its best hit
              in the query, allowing for query overlaps
-u float      Set the minimum alignment uniqueness, i.e. percent of
              the alignment matching to unique reference AND query
              sequence [0, 100], default 0
-o float      Set the maximum alignment overlap for -r and -q options
              as a percent of the alignment length [0, 100], default 100

  Reads a delta alignment file from either nucmer or promer and
filters the alignments based on the command-line switches, leaving
only the desired alignments which are output to stdout in the same
delta format as the input. For multiple switches, order of operations
is as follows: -i -l -u -q -r -g -m -1. If an alignment is excluded
by a preceding operation, it will be ignored by the succeeding
operations.
  An important distinction between the -g option and the -1 and -m
options is that -g requires the alignments to be mutually consistent
in their order, while the -1 and -m options are not required to be
mutually consistent and therefore tolerate translocations,
inversions, etc. In general cases, the -m option is the best choice,
however -1 can be handy for applications such as SNP finding which
require a 1-to-1 mapping. Finally, for mapping query contigs, or
sequencing reads, to a reference genome, use -q.

```


### dnadiff
```
$ dnadiff

  USAGE: dnadiff  [options]  <reference>  <query>
    or   dnadiff  [options]  -d <delta file>
    
Try '/home/wzk/anaconda3/envs/evolution/bin/dnadiff -h' for more information.
(evolution) wzk@ubuntu 20:24:51 O_O /home/wzk/Project/mummer_test 
$ dnadiff -h

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

### mapview
```
$ mapview -h 

  USAGE: mapview  [options]  <coords file>  [UTR coords]  [CDS coords]

  DESCRIPTION:
    mapview is a utility program for displaying sequence alignments as
    provided by MUMmer, NUCmer, PROmer or Mgaps. mapview takes the output of
    show-coords and converts it to a FIG, PDF or PS file for visual analysis.
    It can also break the output into multiple files for easier viewing and
    printing.

  MANDATORY:
    coords file    The output of 'show-coords -rl[k]' or 'mgaps'

  OPTIONS:
    UTR coords      UTR coordinate file in GFF format
    CDS coords      CDS coordinate file in GFF format

    -d|maxdist      Set the maximum base-pair distance between linked matches
                    (default 50000)
    -f|format       Set the output format to 'pdf', 'ps' or 'fig'
                    (default 'fig')
    -h
    --help          Display help information and exit
    -m|mag          Set the magnification at which the figure is rendered,
                    this is an option for fig2dev which is used to generate
                    the PDF and PS files (default 1.0)
    -n|num          Set the number of output files used to partition the
                    output, this is to avoid generating files that are too
                    large to display (default 10)
    -p|prefix       Set the output file prefix
                    (default "PROMER_graph or NUCMER_graph")
    -v
    --verbose       Verbose logging of the processed files
    -V
    --version       Display the version information and exit
    -x1 coord       Set the lower coordinate bound of the display
    -x2 coord       Set the upper coordinate bound of the display
    -g|ref          If the input file is provided by 'mgaps', set the
                    reference sequence ID (as it appears in the first column
                    of the UTR/CDS coords file)
    -I              Display the name of query sequences
    -Ir             Display the name of reference genes

```


### show-coords

```
$ show-coords -h

USAGE: show-coords  [options]  <deltafile>

-b          Merges overlapping alignments regardless of match dir
            or frame and does not display any idenitity information.
-B          Switch output to btab format
-c          Include percent coverage information in the output
-d          Display the alignment direction in the additional
            FRM columns (default for promer)
-g          Deprecated option. Please use 'delta-filter' instead
-h          Display help information
-H          Do not print the output header
-I float    Set minimum percent identity to display
-k          Knockout (do not display) alignments that overlap
            another alignment in a different frame by more than 50%
            of their length, AND have a smaller percent similarity
            or are less than 75% of the size of the other alignment
            (promer only)
-l          Include the sequence length information in the output
-L long     Set minimum alignment length to display
-o          Annotate maximal alignments between two sequences, i.e.
            overlaps between reference and query sequences
-q          Sort output lines by query IDs and coordinates
-r          Sort output lines by reference IDs and coordinates
-T          Switch output to tab-delimited format

  Input is the .delta output of either the "nucmer" or the
"promer" program passed on the command line.
  Output is to stdout, and consists of a list of coordinates,
percent identity, and other useful information regarding the
alignment data contained in the .delta file used as input.
  NOTE: No sorting is done by default, therefore the alignments
will be ordered as found in the <deltafile> input.

```

### show-aligns

```
$ show-aligns -h

USAGE: show-aligns  [options]  <deltafile>  <ref ID>  <qry ID>

-h            Display help information
-q            Sort alignments by the query start coordinate
-r            Sort alignments by the reference start coordinate
-w int        Set the screen width - default is 60
-x int        Set the matrix type - default is 2 (BLOSUM 62),
              other options include 1 (BLOSUM 45) and 3 (BLOSUM 80)
              note: only has effect on amino acid alignments

  Input is the .delta output of either the "nucmer" or the
"promer" program passed on the command line.
  Output is to stdout, and consists of all the alignments between the
query and reference sequences identified on the command line.
  NOTE: No sorting is done by default, therefore the alignments
will be ordered as found in the <deltafile> input.

```

### mummerplot
```
$ mummerplot -h

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

