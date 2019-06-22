## [TACO](https://github.com/tacorna/taco): Multi-sample transcriptome assembly from RNA-Seq

### install TACO
```
$ conda install -c bioconda taco
```

### The parameters for TACO
```
$ ./taco_run --help
usage: taco_run [-h] [-o DIR] [-p N] [-v] [--resume] [--assemble BED]
                [--gtf-expr-attr ATTR] [--filter-min-length N]
                [--filter-min-expr X] [--filter-splice-juncs]
                [--add-splice-motif ADD_SPLICE_MOTIF]
                [--ref-genome-fasta REF_GENOME_FASTA_FILE]
                [--isoform-frac FRAC] [--max-isoforms N]
                [--assemble-unstranded] [--no-assemble-unstranded]
                [--change-point] [--no-change-point]
                [--change-point-pvalue <float 0.0-1.0>]
                [--change-point-fold-change <float 0.0-1.0>]
                [--change-point-trim] [--no-change-point-trim]
                [--path-kmax kmax] [--path-frac X] [--max-paths N]
                [sample_file]

TACO: Multi-sample transcriptome assembly from RNA-Seq

positional arguments:
  sample_file

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --output-dir DIR
                        directory where output files will be stored (if
                        already exists then --resume must be specified)
                        [default=output]
  -p N, --num-processes N
                        Run TACO in parallel with N processes [default=1]
  -v, --verbose         Enabled detailed logging (for debugging)
  --resume              Resumes an existing run that may have ended
                        prematurely. Specify the location of the run using the
                        -o/--output-dir option.
  --assemble BED        Assemble transfrags produced by a previous TACO run,
                        bypassing the GTF aggregation step. Accepts a taco-
                        formatted BED file.
  --gtf-expr-attr ATTR  GTF attribute field containing expression
                        [default=FPKM]
  --filter-min-length N
                        Filter input transfrags with length < N prior to
                        assembly [default=200]
  --filter-min-expr X   Filter input transfrags with expression (FPKM/TPM) < X
                        prior to assembly [default=0.5]
  --filter-splice-juncs
                        Filter input transfrags that possess non-canonical
                        splice motifs prior to assembly. Splice motifs are
                        GTAG, GCAG, and ATAC are allowed [default=False].
                        Requires genome sequence to be specified using --ref-
                        genome-fasta.
  --add-splice-motif ADD_SPLICE_MOTIF
                        Add additional splice junction motifs to permit when
                        using the --filter-splice-juncs flag. Use this flag
                        multiple times for each additional junction motif.
                        Motif must be 4 bases.
  --ref-genome-fasta REF_GENOME_FASTA_FILE
                        Reference genome sequence in FASTA format needed to
                        assess splice junction motif sequences. Use in
                        conjunction with --filter-splice-juncs.
  --isoform-frac FRAC   Report transcript isoforms with expression fraction >=
                        FRAC (0.0-1.0) relative to the major isoform within
                        each gene [default=0.05]
  --max-isoforms N      Maximum isoforms to report for each gene [default=0]
  --assemble-unstranded
                        Enable assembly of unstranded transfrags
                        [default=False]
  --no-assemble-unstranded
                        Disable assembly of unstranded transfrags
  --change-point        Enable change point detection [default=True]
  --no-change-point     Disable change point detection

Advanced Options:
  (recommend leaving at their default settings for most purposes)

  --change-point-pvalue <float 0.0-1.0>
                        Mann-Whitney-U p-value threshold for calling change
                        points [default=0.01]
  --change-point-fold-change <float 0.0-1.0>
                        Fold change threshold between the means of two
                        putative segments on either side of a change point. A
                        value of 0.0 is the most strict setting, effectively
                        calling no change points. Conversely, setting the
                        value to 1.0 calls allchange points [default=0.85]
  --change-point-trim   Trim transfrags around change points [default=True]
  --no-change-point-trim
                        Disable trimming around change points
  --path-kmax kmax      Limit optimization for choosing parameter k for path
                        graph (DeBruijn graph) to k <= kmax [default=0]
  --path-frac X         dynamic programming algorithm will stop finding
                        suboptimal paths when path expression drops below a
                        fraction X (0.0-1.0) of the total locus expression
                        [default=0.0]
  --max-paths N         dynamic programming algorithm will stop after finding
                        N paths [default=0]

```

### run TACO
```
/home/wzk/software/taco-v0.7.2.Linux_x86_64/taco_run /home/wzk/test_cufflinks/TACO/gtf_list.txt -o /home/wzk/test_cufflinks/TACO/TACO_result -p 10 --gtf-expr-attr FPKM
```
