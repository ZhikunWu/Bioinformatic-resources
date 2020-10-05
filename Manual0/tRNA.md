## [rRNAmmer](http://www.cbs.dtu.dk/services/RNAmmer/): predicts 5s/8s, 16s/18s, and 23s/28s ribosomal RNA in full genome sequences
## [RNAmmer的安装和使用](http://www.chenlianfu.com/?p=1979)
## [Manual page for rnammer](https://www.cbs.dtu.dk/cgi-bin/nph-runsafe?man=rnammer)
## [barrnap](https://github.com/tseemann/barrnap):  Bacterial ribosomal RNA predictor



## [ARAGORN]
```
$ conda install -c bioconda aragorn
```

```
$ aragorn -h
----------------------------
ARAGORN v1.2.38 Dean Laslett
----------------------------

Please reference the following papers if you use this
program as part of any published research.

Laslett, D. and Canback, B. (2004) ARAGORN, a
program for the detection of transfer RNA and transfer-messenger
RNA genes in nucleotide sequences
Nucleic Acids Research, 32;11-16

Laslett, D. and Canback, B. (2008) ARWEN: a
program to detect tRNA genes in metazoan mitochondrial
nucleotide sequences
Bioinformatics, 24(2); 172-175.


ARAGORN detects tRNA, mtRNA, and tmRNA genes.

Usage:
aragorn -v -e -s -d -c -l -j -a -q -rn -w -ifro<min>,<max> -t -mt -m
        -rp -ps -gc -tv -seq -br -fasta -fo -o <outfile> <filename>

<filename> is assumed to contain one or more sequences
in FASTA or GENBANK format. Results of the search are printed
to STDOUT. All switches are optional and case-insensitive.
Unless -i is specified, tRNA genes containing introns
are not detected.

    -m            Search for tmRNA genes.
    -t            Search for tRNA genes.
                  By default, all are detected. If one of
                  -m or -t is specified, then the other
                  is not detected unless specified as well.
    -mt           Search for Metazoan mitochondrial tRNA genes.
                  tRNA genes with introns not detected. -i,-sr switchs
                  ignored. Composite Metazoan mitochondrial
                  genetic code used.
    -mtmam        Search for Mammalian mitochondrial tRNA
                  genes. -i switch ignored. -tv switch set.
                  Mammalian mitochondrial genetic code used.
    -mtx          Same as -mt but low scoring tRNA genes are
                  not reported.
    -mtd          Overlapping metazoan mitochondrial tRNA genes
                  on opposite strands are reported.
    -gc<num>      Use the GenBank transl_table = <num> genetic code.
    -gcstd        Use standard genetic code.
    -gcmet        Use composite Metazoan mitochondrial genetic code.
    -gcvert       Use Vertebrate mitochondrial genetic code.
    -gcinvert     Use Invertebrate mitochondrial genetic code.
    -gcyeast      Use Yeast mitochondrial genetic code.
    -gcprot       Use Mold/Protozoan/Coelenterate mitochondrial genetic code.
    -gcciliate    Use Ciliate genetic code.
    -gcflatworm   Use Echinoderm/Flatworm mitochondrial genetic code
    -gceuplot     Use Euplotid genetic code.
    -gcbact       Use Bacterial/Plant chloroplast genetic code.
    -gcaltyeast   Use alternative Yeast genetic code.
    -gcascid      Use Ascidian mitochondrial genetic code.
    -gcaltflat    Use alternative Flatworm mitochondrial genetic code.
    -gcblep       Use Blepharisma genetic code.
    -gcchloroph   Use Chlorophycean mitochondrial genetic code.
    -gctrem       Use Trematode mitochondrial genetic code.
    -gcscen       Use Scenedesmus obliquus mitochondrial genetic code.
    -gcthraust    Use Thraustochytrium mitochondrial genetic code.
    -gcptero      Use Pterobranchia mitochondrial genetic code.
    -gcgrac       Use Gracilibacteria genetic code.
                  Individual modifications can be appended using
    ,BBB=<aa>     B = A,C,G, or T. <aa> is the three letter
                  code for an amino-acid. More than one modification
                  can be specified. eg -gcvert,aga=Trp,agg=Trp uses
                  the Vertebrate Mitochondrial code and the codons
                  AGA and AGG changed to Tryptophan.
    -c            Assume that each sequence has a circular
                  topology. Search wraps around each end.
                  Default setting.
    -l            Assume that each sequence has a linear
                  topology. Search does not wrap.
    -d            Double. Search both strands of each
                  sequence. Default setting.
    -s  or -s+    Single. Do not search the complementary
                  (antisense) strand of each sequence.
    -sc or -s-    Single complementary. Do not search the sense
                  strand of each sequence.
    -i            Search for tRNA genes with introns in
                  anticodon loop with maximum length 3000
                  bases. Minimum intron length is 0 bases.
                  Ignored if -m is specified.
    -i<max>       Search for tRNA genes with introns in
                  anticodon loop with maximum length <max>
                  bases. Minimum intron length is 0 bases.
                  Ignored if -m is specified.
    -i<min>,<max> Search for tRNA genes with introns in
                  anticodon loop with maximum length <max>
                  bases, and minimum length <min> bases.
                  Ignored if -m is specified.
    -io           Same as -i, but allow tRNA genes with long
                  introns to overlap shorter tRNA genes.
    -if           Same as -i, but fix intron between positions
                  37 and 38 on C-loop (one base after anticodon).
    -ifo          Same as -if and -io combined.
    -ir           Same as -i, but report tRNA genes with minimum
                  length <min> bases rather than search for
                  tRNA genes with minimum length <min> bases.
                  With this switch, <min> acts as an output filter,
                  minimum intron length for searching is still 0 bases.
    -tv           Do not search for mitochondrial TV replacement
                  loop tRNA genes. Only relevant if -mt used.
    -c7           Search for tRNA genes with 7 base C-loops only.
    -ss           Use the stricter canonical 1-2 bp spacer1 and
                  1 bp spacer2. Ignored if -mt set. Default is to
                  allow 3 bp spacer1 and 0-2 bp spacer2, which may
                  degrade selectivity.
    -j            Display 4-base sequence on 3' end of astem
                  regardless of predicted amino-acyl acceptor length.
    -jr           Allow some divergence of 3' amino-acyl acceptor
                  sequence from NCCA.
    -jr4          Allow some divergence of 3' amino-acyl acceptor
                  sequence from NCCA, and display 4 bases.
    -e            Print out score for each reported gene.
    -ps           Lower scoring thresholds to 95% of default levels.
    -ps<num>      Change scoring thresholds to <num> percent of default levels.
    -rp           Flag possible pseudogenes (score < 100 or tRNA anticodon
                  loop <> 7 bases long). Note that genes with score < 100
                  will not be detected or flagged if scoring thresholds are not
                  also changed to below 100% (see -ps switch).
    -rp<num>      Flag possible pseudogenes and change score threshold to <num>
                  percent of default levels.
    -seq          Print out primary sequence.
    -br           Show secondary structure of tRNA gene primary sequence
                  using round brackets.
    -fasta        Print out primary sequence in fasta format.
    -fo           Print out primary sequence in fasta format only
                  (no secondary structure).
    -fon          Same as -fo, with sequence and gene numbering in header.
    -fos          Same as -fo, with no spaces in header.
    -fons         Same as -fo, with sequence and gene numbering, but no spaces.
                  as (<species>|<species>) instead of ???
    -v            Verbose. Prints out information during
                  search to STDERR.
    -a            Print out tRNA domain for tmRNA genes.
    -a7           Restrict tRNA astem length to a maximum of 7 bases
    -aa           Display message if predicted iso-acceptor species
                  does not match species in sequence name (if present).
    -amt<num>     Change annotated tRNA length mismatch reporting threshold to
                  <num> bases when searching GENBANK files. Default is 10 bases.
    -amm<num>     Change annotated tmRNA length mismatch reporting threshold to
                  <num> bases when searching GENBANK files. Default is 30 bases.
    -q            Dont print configuration line (which switches
                  and files were used).
    -rn           Repeat sequence name before summary information.
    -o <outfile>  Print output to <outfile>. If <outfile>
                  already exists, it is overwritten. By default
                  all output goes to stdout.
    -w            Print out in batch mode.
    -wa           Same as -w, but for 6 or 8 base anticodon
                  loops, print possible iso-acceptor species
                  For tRNA genes, batch mode output is in the form:

                  Sequence name
                  N genes found
                  1 tRNA-<species> [locus 1] <Apos> (nnn)
                  i(<intron position>,<intron length>)
                            .          
                            .          
                  N tRNA-<species> [Locus N] <Apos> (nnn)
                  i(<intron position>,<intron length>)

                  N is the number of genes found
                  <species> is the tRNA iso-acceptor species
                  <Apos> is the tRNA anticodon relative position
                  (nnn) is the tRNA anticodon base triplet
                  i means the tRNA gene has a C-loop intron

                  For tmRNA genes, output is in the form:

                  n tmRNA(p) [Locus n] <tag offset>,<tag end offset>
                  <tag peptide>

                  p means the tmRNA gene is permuted
    -wunix        Get around problem with some windows gcc compilers
                  (found so far in Strawberry Perl and Active Perl)
                  when reading Unix files.
                  Execution speed may be slower for large files.
                  Execution speed will be a lot slower for files
                  with many small sequences.
```
