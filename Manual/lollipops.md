## [lollipops](https://github.com/joiningdata/lollipops)


### lollipops parameter

 ```
$ ./lollipops 
ERROR: Unable to find Arial.ttf - Which is required for accurate font sizing.
       Please use -f=/path/to/arial.ttf or the TrueType (.ttf) font of your choice.
Usage: ./lollipops [options] {-Q UNIPROT_DB IDENTIFER | -U UNIPROT_ID | GENE_SYMBOL} [PROTEIN CHANGES ...]

Protein ID input:
  GENE_SYMBOL is the official human HGNC gene symbol. This will use the
  UniprotKB API to lookup the UNIPROT_ID.

  You can provide a UniProt ID directly with -U (e.g. "-U P04637" for TP53)

  For more advanced usage, query UniprotKB's database mappings directly using
  a supported identifier with -Q DBNAME. Available DBNAMEs can be found here:
     http://www.uniprot.org/help/programmatic_access#id_mapping_examples

     RefSeq ID        e.g. -Q P_REFSEQ_AC NP_001265252.1
     Entrez GeneID    e.g. -Q P_ENTREZGENEID 4336
     Ensembl ID       e.g. -Q ENSEMBL_ID ENSG00000168314

Protein changes:
  Currently only point mutations are supported, and may be specified as:

    <AMINO><CODON><AMINO><#COLOR><@COUNT>

  Only CODON is required, and AMINO tags are not parsed.

  Synonymous mutations are denoted if the first AMINO tag matches the second
  AMINO tag, or if the second tag is not present. Otherwise the non-synonymous
  mutation color is used. The COLOR tag will override using the #RRGGBB style
  provided. The COUNT tag can be used to scale the lollipop marker size so that
  the area is exponentially proportional to the count indicated. Examples:

    R273C            -- non-synonymous mutation at codon 273
    T125@5           -- synonymous mutation at codon 125 with "5x" marker sizing
    R248Q#00ff00     -- green lollipop at codon 248
    R248Q#00ff00@131 -- green lollipop at codon 248 with "131x" marker sizing

  (N.B. color must come before count in tags)

Diagram generation options:
  -legend                 draw a legend for colored regions
  -syn-color="#0000ff"    color to use for synonymous mutation markers
  -mut-color="#ff0000"    color to use for non-synonymous mutation markers
  -hide-axis              do not draw the amino position x-axis
  -show-disordered        draw disordered regions on the backbone
  -show-motifs            draw simple motif regions
  -labels                 draw label text above lollipop markers
  -no-patterns            use solid fill instead of patterns (SVG only)
  -domain-labels=fit      hot to apply domain labels (default="truncated")
                            "fit" = only if fits in space available
                            "off" = do not draw text in the domains

Output options:
  -o=filename.png         set output filename (.png or .svg supported)
  -w=700                  set diagram pixel width (default = automatic fit)
  -dpi=300                set DPI (PNG output only)

Alternative input sources:
  -uniprot                use UniprotKB as an alternative to Pfam for
                          fetching domain/motif information
  -l=filename.json        use local file instead of Pfam API for graphic data
                            see: http://pfam.xfam.org/help#tabview=tab9

 ```

### run lollipops
 ```
$ ./lollipops -legend -labels TP53 R248Q#7f3333@131 R273C R175H T125@5
ERROR: Unable to find Arial.ttf - Which is required for accurate font sizing.
       Please use -f=/path/to/arial.ttf or the TrueType (.ttf) font of your choice.
HGNC Symbol:  TP53
Uniprot/SwissProt Accession:  P04637
Drawing diagram to TP53.svg

 ```



 ```
$ ./lollipops -legend  -U P06400    -labels   L491P  S758P R467X@2 R661W H483fs Q637X R552X R579X R320X R621S R698fs
ERROR: Unable to find Arial.ttf - Which is required for accurate font sizing.
       Please use -f=/path/to/arial.ttf or the TrueType (.ttf) font of your choice.
Gene Symbol:  RB_HUMAN
Drawing diagram to RB_HUMAN.svg
 ```


