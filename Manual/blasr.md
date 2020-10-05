## [BLASR](https://github.com/PacificBiosciences/blasr)


```
$ blasr -h
   Options for blasr 
   Basic usage: 'blasr reads.{bam|fasta|bax.h5|fofn} genome.fasta [-options] 
 option Description (default_value).

 Input Files.
   reads.bam   is a PacBio BAM file of reads.
               This is the preferred input to blasr because rich quality
               value (insertion,deletion, and substitution quality values) information is 
               maintained.  The extra quality information improves variant detection and mapping
               speed.
   reads.fasta is a multi-fasta file of reads.  While any fasta file is valid input, 
   reads.bax.h5|reads.plx.h5 is the old DEPRECATED output format of SMRT reads.
   input.fofn  File of file names accepted.

   --sa suffixArrayFile
               Use the suffix array 'sa' for detecting matches
               between the reads and the reference.  The suffix
               array has been prepared by the sawriter program.

   --ctab tab 
               A table of tuple counts used to estimate match significance.  This is 
               by the program 'printTupleCountTable'.  While it is quick to generate on 
               the fly, if there are many invocations of blasr, it is useful to
               precompute the ctab.

   --regionTable table (DEPRECATED)
               Read in a read-region table in HDF format for masking portions of reads.
               This may be a single table if there is just one input file, 
               or a fofn.  When a region table is specified, any region table inside 
               the reads.plx.h5 or reads.bax.h5 files are ignored.

 Options for modifying reads.
   --noSplitSubreads
               Do not split subreads at adapters. This is typically only 
               useful when the genome in an unrolled version of a known template, and 
               contains template-adapter-reverse_template sequence.
               For BAM input it reconstitutes full ZMW reads.

 Option for modifying BAM reads with --noSplitSubreads.
   --polymerase
               Instead of reconstituting ZMW reads,
               this option reconstitutes polymerase reads, omitting LQ regions.
               Polymerase reads are aligned, if at least one subread is present.

(DEPRECATED) Options for modifying HDF reads.
               There is ancilliary information about substrings of reads 
               that is stored in a 'region table' for each read file.  Because 
               HDF is used, the region table may be part of the .bax.h5 or .plx.h5 file,
               or a separate file.  A contiguously read substring from the template 
               is a subread, and any read may contain multiple subreads. The boundaries 
               of the subreads may be inferred from the region table either directly or 
               by definition of adapter boundaries.  Typically region tables also
               contain information for the location of the high and low quality regions of
               reads.  Reads produced by spurrious reads from empty ZMWs have a high
               quality start coordinate equal to high quality end, making no usable read.
   --useccs   
               Align the circular consensus sequence (ccs), then report alignments
               of the ccs subreads to the window that the ccs was mapped to.  Only 
               alignments of the subreads are reported.
   --useccsall
               Similar to -useccs, except all subreads are aligned, rather than just
               the subreads used to call the ccs.  This will include reads that only
               cover part of the template.
   --useccsdenovo
               Align the circular consensus, and report only the alignment of the ccs
               sequence.
   --ignoreRegions(false)
               Ignore any information in the region table.
   --ignoreHQRegions (false)Ignore any hq regions in the region table.

 Alignments To Report.
   --bestn n (10)
               Report the top 'n' alignments.
   --hitPolicy
               (all) Specify a policy to treat multiple hits from [all, allbest, random, randombest, leftmost]
                 all       : report all alignments.
                 allbest   : report all equally top scoring alignments.
                 random    : report a random alignment.
                 randombest: report a random alignment from multiple equally top scoring alignments.
                 leftmost  : report an alignment which has the best alignmentscore and has the smallest mapping coordinate in any reference.
   --placeRepeatsRandomly (false)
               DEPRECATED! If true, equivalent to --hitPolicy randombest.
   --placeGapConsistently (false)
               Place gaps consistently in alignments of a read as alignments 
               of its reverse complementary sequence.
   --randomSeed (0)
               Seed for random number generator. By default (0), use current time as seed. 
   --noSortRefinedAlignments (false) 
               Once candidate alignments are generated and scored via sparse dynamic 
               programming, they are rescored using local alignment that accounts 
               for different error profiles.
               Resorting based on the local alignment may change the order the hits are returned.
   --allowAdjacentIndels 
               When specified, adjacent insertion or deletions are allowed. Otherwise, adjacent 
               insertion and deletions are merged into one operation.  Using quality values 
               to guide pairwise alignments may dictate that the higher probability alignment 
               contains adjacent insertions or deletions.  Current tools such as GATK do not permit
               this and so they are not reported by default.

 Output Formats and Files
   --out out (terminal)  
               Write output to 'out'.
   --bam       Write output in PacBio BAM format. This is the preferred output format.
               Input query reads must be in PacBio BAM format.
   --sam       Write output in SAM format. Starting from version 5.2 is no longer supported
               Use --bam, then translate from .bam to .sam
   -m t           
               If not printing SAM, modify the output of the alignment.
                t=0 Print blast like output with |'s connecting matched nucleotides.
                  1 Print only a summary: score and pos.
                  2 Print in Compare.xml format.
                  3 Print in vulgar format (DEPRECATED).
                  4 Print a longer tabular version of the alignment.
                  5 Print in a machine-parsable format that is read by compareSequences.py.
   --header
               Print a header as the first line of the output file describing the contents of each column.
   --titleTable tab (NULL) 
               Construct a table of reference sequence titles.  The reference sequences are 
               enumerated by row, 0,1,...  The reference index is printed in alignment results
               rather than the full reference name.  This makes output concise, particularly when
               very verbose titles exist in reference names.
   --unaligned file
               Output reads that are not aligned to 'file'
   --noPrintUnalignedSeqs
               Must be used together with -unaligned, print unaligned read names only.
   --clipping [none|hard|subread|soft] (none)
               Use no/hard/subread/soft clipping, ONLY for SAM/BAM output.
   --printSAMQV (false)
               Print quality values to SAM output.
 Options for anchoring alignment regions. This will have the greatest effect on speed and sensitivity.
   --minMatch m (12) 
               Minimum seed length.  Higher minMatch will speed up alignment, 
               but decrease sensitivity.
   --maxMatch l (inf)
               Stop mapping a read to the genome when the lcp length reaches l.  
               This is useful when the query is part of the reference, for example when 
               constructing pairwise alignments for de novo assembly.
   --maxLCPLength l (inf)
               The same as -maxMatch.
   --maxAnchorsPerPosition m (10000) 
               Do not add anchors from a position if it matches to more than 'm' locations in the target.
   --advanceExactMatches E (0)
               Another trick for speeding up alignments with match - E fewer anchors.  Rather than
               finding anchors between the read and the genome at every position in the read, 
               when an anchor is found at position i in a read of length L, the next position 
               in a read to find an anchor is at i+L-E.
               Use this when alignining already assembled contigs.
   --nCandidates n (10)
               Keep up to 'n' candidates for the best alignment.  A large value of n will slow mapping
               because the slower dynamic programming steps are applied to more clusters of anchors
               which can be a rate limiting step when reads are very long.
   --concordant(false)
               Map all subreads of a zmw (hole) to where the longest full pass subread of the zmw 
               aligned to. This requires to use the region table and hq regions.
               This option only works when reads are in base or pulse h5 format.
   --fastMaxInterval(false)
               Fast search maximum increasing intervals as alignment candidates. The search 
               is not as exhaustive as the default, but is much faster.
   --aggressiveIntervalCut(false)
               Agreesively filter out non-promising alignment candidates, if there 
               exists at least one promising candidate. If this option is turned on, 
               Blasr is likely to ignore short alignments of ALU elements.
   --fastSDP(false)
               Use a fast heuristic algorithm to speed up sparse dynamic programming.

  Options for Refining Hits.
   --refineConcordantAlignments(false)
               Refine concordant alignments. It slightly increases alignment accuracy at cost of time.
   --sdpTupleSize K (11)
               Use matches of length K to speed dynamic programming alignments.  This controls
               accuracy of assigning gaps in pairwise alignments once a mapping has been found,
               rather than mapping sensitivity itself.
   --scoreMatrix "score matrix string" 
               Specify an alternative score matrix for scoring fasta reads.  The matrix is 
               in the format 
                  ACGTN
                A abcde
                C fghij
                G klmno
                T pqrst
                N uvwxy . The values a...y should be input as a quoted space separated 
               string: "a b c ... y". Lower scores are better, so matches should be less 
               than mismatches e.g. a,g,m,s = -5 (match), mismatch = 6. 
   --affineOpen value (10) 
               Set the penalty for opening an affine alignment.
   --affineExtend a (0)
               Change affine (extension) gap penalty. Lower value allows more gaps.

 Options for overlap/dynamic programming alignments and pairwise overlap for de novo assembly. 
   --useQuality (false)
               Use substitution/insertion/deletion/merge quality values to score gap and 
               mismatch penalties in pairwise alignments.  Because the insertion and deletion
               rates are much higher than substitution, this will make many alignments 
               favor an insertion/deletion over a substitution.  Naive consensus calling methods 
               will then often miss substitution polymorphisms. This option should be 
               used when calling consensus using the Quiver method.  Furthermore, when 
               not using quality values to score alignments, there will be a lower consensus 
               accuracy in homolymer regions.
   --affineAlign (false)
               Refine alignment using affine guided align.

 Options for filtering reads and alignments
   --minReadLength l(50)
               Skip reads that have a full length less than l. Subreads may be shorter.
   --minSubreadLength l(0)
               Do not align subreads of length less than l.
   --minRawSubreadScore m(0)
               Do not align subreads whose quality score in region table is less than m (quality scores should be in range [0, 1000]).
   --maxScore m(-200)
               Maximum score to output (high is bad, negative good).
   --minAlnLength
               (0) Report alignments only if their lengths are greater than minAlnLength.
   --minPctSimilarity
               (0) Report alignments only if their percentage similarity is greater than minPctSimilarity.
   --minPctAccuracy
               (0) Report alignments only if their percentage accuracy is greater than minAccuracy.

 Options for parallel alignment.
   --nproc N (1)
               Align using N processes.  All large data structures such as the suffix array and 
               tuple count table are shared.
   --start S (0)
               Index of the first read to begin aligning. This is useful when multiple instances 
               are running on the same data, for example when on a multi-rack cluster.
   --stride S (1)
               Align one read every 'S' reads.

 Options for subsampling reads.
   --subsample (0)
               Proportion of reads to randomly subsample (expressed as a decimal) and align.
   --holeNumbers LIST 
               When specified, only align reads whose ZMW hole numbers are in LIST.
               LIST is a comma-delimited string of ranges, such as '1,2,3,10-13'.
               This option only works when reads are in bam, bax.h5 or plx.h5 format.

 -h            Print this help file.

In release v5.1 of BLASR, command-line options will use the 
single dash/double dash convention: 
Character options are preceded by a single dash. (Example: -v) 
Word options are preceded by a double dash. (Example: --verbose) 
Please modify your scripts accordingly when BLASR v5.1 is released. 

To cite BLASR, please use: Chaisson M.J., and Tesler G., Mapping 
single molecule sequencing reads using Basic Local Alignment with 
Successive Refinement (BLASR): Theory and Application, BMC 
Bioinformatics 2012, 13:238.
Please report any bugs to 'https://github.com/PacificBiosciences/blasr/issues'.

```



```
$ blasr --help
NAME
         blasr - Map SMRT Sequences to a reference genome.

SYNOPSIS
         blasr reads.bam genome.fasta --bam --out out.bam

         blasr reads.fasta genome.fasta 

         blasr reads.fasta genome.fasta --sa genome.fasta.sa

         blasr reads.bax.h5 genome.fasta [--sa genome.fasta.sa] 

         blasr reads.bax.h5 genome.fasta --sa genome.fasta.sa --maxScore 100 --minMatch 15 ... 

         blasr reads.bax.h5 genome.fasta --sa genome.fasta.sa --nproc 24 --out alignment.out ... 

DESCRIPTION 
  blasr is a read mapping program that maps reads to positions 
  in a genome by clustering short exact matches between the read and
  the genome, and scoring clusters using alignment. The matches are
  generated by searching all suffixes of a read against the genome
  using a suffix array. Global chaining methods are used to score 
  clusters of matches.

  The only required inputs to blasr are a file of reads and a
  reference genome.  It is exremely useful to have read filtering
  information, and mapping runtime may decrease substantially when a
  precomputed suffix array index on the reference sequence is
  specified.
  
  Although reads may be input in FASTA format, the recommended input is
  PacBio BAM files because these contain quality value
  information that is used in the alignment and produces higher quality
  variant detection.
  Although alignments can be output in various formats, the recommended 
  output format is PacBio BAM.
  Support to bax.h5 and plx.h5 files will be DEPRECATED.
  Support to region tables for h5 files will be DEPRECATED.
  
  When suffix array index of a genome is not specified, the suffix array is
  built before producing alignment.   This may be prohibitively slow
  when the genome is large (e.g. Human).  It is best to precompute the
  suffix array of a genome using the program sawriter, and then specify
  the suffix array on the command line using -sa genome.fa.sa.
  
  The optional parameters are roughly divided into three categories:
  control over anchoring, alignment scoring, and output. 
  
  The default anchoring parameters are optimal for small genomes and
  samples with up to 5% divergence from the reference genome.  The main
  parameter governing speed and sensitivity is the -minMatch parameter.
  For human genome alignments, a value of 11 or higher is recommended.  
  Several methods may be used to speed up alignments, at the expense of
  possibly decreasing sensitivity.  
  
  Regions that are too repetitive may be ignored during mapping by
  limiting the number of positions a read maps to with the
  -maxAnchorsPerPosition option.  Values between 500 and 1000 are effective
  in the human genome.
  
  For small genomes such as bacterial genomes or BACs, the default parameters 
  are sufficient for maximal sensitivity and good speed.
```


### Some typical use cases

Align subreads in movie.subreads.bam to ecoli_K12 genome, and output in BAM format.
```
blasr movie.subreads.bam ecoli_K12.fasta --bam --out alignments.bam
```


Align subreads in movie.subreadset.xml to ecoli_K12 genome, and output in BAM format.
```
blasr movie.subreadset.xml ecoli_K12.fasta --bam --out alignments.bam
```

Align subreads in movie.subreadset.xml to ecoli_K12 genome ReferenceSet, and output in BAM format.
```
blasr movie.subreadset.xml ecoli_K12.referenceset.xml --bam --out alignments.bam
```

Align CCS reads in movie.consensusreadset.xml to ecoli_K12 genome, and output in BAM format.
```
blasr movie.consensusreadset.xml ecoli_K12.fasta --bam --out alignments.bam
```

Use multiple threads, e.x., 16 threads
```
blasr movie.subreads.bam ecoli_K12.fasta --nproc 16
```

Include a larger minimal match, for faster but less sensitive alignments
```
blasr movie.subreads.bam ecoli_K12.fasta --minMatch 15
```


Produce alignments in a pairwise human readable format
```
blasr movie.subreads.bam ecoli_K12.fasta -m 0
```

Use a precomputed suffix array for faster startup

sawriter ecoli_K12.fasta.sa ecoli_K12.fasta #First precompute the suffix array
```
blasr movie.subreads.bam ecoli_K12.fasta --sa ecoli_K12.fasta.sa
```

Align RSII reads from reads.bas.h5 to ecoli_K12 genome, and output in SAM format.
```
blasr reads.bas.h5  ecoli_K12.fasta --sam --out alignments.sam

```

Same as above, but with soft clipping
```
blasr reads.bas.h5  ecoli_K12.fasta --sam --clipping soft --out alignments.sam
```



### manual
```
$ gzip -dc nano_test.fastq.gz > nano_test.fastq

$ blasr nano_test.fastq  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa --nproc 24 --sam  --out nano_test.sam

[INFO] 2019-03-21T17:43:37 [blasr] started.
ERROR, can not convert non-pacbio reads to pbbam record.
```


#### [ERROR, can not convert non-pacbio reads to pbbam record](https://github.com/PacificBiosciences/blasr/wiki/BLASR-Frequently-Asked-Questions)