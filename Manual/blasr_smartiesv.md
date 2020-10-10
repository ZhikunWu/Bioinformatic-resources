
## [smartie-sv](https://github.com/zeeev/smartie-sv)

### install smartie-sv
```
git clone --recursive https://github.com/zeeev/smartie-sv.git

cd smartie-sv && make
```

### insatll library
```
conda install -c bioconda blasr

conda install -c bioconda htslib
```



### example files
```
(pangenome) wuzhikun@mu03 08:45:50 ^_^ /home/wuzhikun/anaconda3/envs/pangenome/share/smartie-sv/example 
$ l
total 795K
-rw-rw-r--. 1 398K Sep  2 08:40 000943F_quiver_patched.fa_0.5_0.9.fa
-rw-rw-r--. 1 398K Sep  2 08:40 hg38-chr19_39.4_39.8.fa

```



### blasr

```
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

### run blasr


```
$ blasr --clipping  hard --sam  --nproc 6 --minPctIdentity 50 --unaligned smartie-sv/M671-2_unaligned.fasta --out smartie-sv/M671-2_aligned.sam  /home/wuzhikun/Project/Population/Assembly/pangenome/M671-2_assembly_polish.fasta  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa
[INFO] 2020-09-02T16:26:30 [blasr] started.

```

output files:
```
-rw-rw-r-- 1 13K Sep  3 09:07 M671-2_contig3100_aligned.sam.tmp
-rw-rw-r-- 1   0 Sep  3 09:07 M671-2_contig3100_unaligned.fasta

```


### [Can blasr produce SAM/BAM output when input is a FASTA file?](https://github.com/PacificBiosciences/blasr/wiki/BLASR-Frequently-Asked-Questions)





This error message is usually reported by BLASR v5.1+ when input reads are in FASTA or FASTQ, while output file is SAM or BAM. For BLASR v5.1+ to produce SAM/BAM output given a FASTA or FASTQ input, input read names must conform to PacBio convention, which is

```
{movie}/{zmw}/{start}_{end}
```


```
>ctg3088 len=5593
ATTGATTCCATTTATTGATTTCAGAATTCGATGATTCCATTCAATTCCATTCAATATGATCCCTTCGAGTCCATTCAATGATTCCATTCAGTCCATTCG
```

convert to
```
>ctg3088/0/0_5592
CATTGATTCCATTTATTGATTTCAGAATTCGATGATTCCATTCAATTCCATTCAATATGATCCCTTCGAGTCCATTCAATGATTCCATTCAGTCCATTCG
```


```
$ time blasr --clipping  hard --sam  --nproc 20 --minPctIdentity 50  --out test/M671-2_contig3100_aligned.sam  /home/wuzhikun/Project/Population/Assembly/pangenome/M671-2_assembly_contig3100.fasta  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa
[INFO] 2020-09-03T10:28:18 [blasr] started.
[INFO] 2020-09-03T10:52:26 [blasr] ended.

real    24m8.236s
user    23m49.078s
sys 0m7.972s

```



```
$ grep -v '^@' M671-2_contig3100_aligned.sam | less

ctg3088/0/0_5593        16      1       143212349       254     20=1X7=1D5=1X5=1X9=1D3=1D1=2D7=1D1=2D22=2D1=3D1=1D2=1D3=1D5=4D1=2D3=3D9=2D2=1D4=1D1=2D1=2D2=2D6=1D12=1D3=1D1=1D6=1D7=1D5=1D1=1D2=2D4=2D1=1D8=1D6=1D5=1D9=2D6=1D9=1D4=1D2=1D4=1D5=2D2=1D6=1D10=1D1=1X5=1D16=2D9=1D30=3D21=1D22=1D14=1D4=1D2=2D3=1D1=1D6=2D2=1D2=1X1D4=1X41=1D3=2D20=1D6=1D3=1D9=1D4=1D6=1D7=1D4=1D9=2D2=1D4=1D3=1X4=1X4=1D23=1I8=1D13=1I14=1D4=1D11=1X19=1D1=1I6=1D12=1D1=1D25=1D35=1D2=1D1=1D10=1D10=2D1=1I19=1I12=2I14=1D24=1I2=1D23=1D7=2D18=1I1=1D12=2D2=1D4=2D2=3D1=1D2=3D1=8D6=1D1=1D1=2D1=428D1=2D3=1D1=3D1=1D5=11D1=7D30=1D9=1I8=1D2=1D5=1D6=1D13=1D2=1D3=1D5=1D12=1I2=1X1I1=1I1=1D1=1I2=1D2=1D37=1I9=1D3=4D20=1X20=1X6=1X16=1X5=1X15=1X3=1X21=1X17=2X2=2D2=1X8=1I23=1I12=1X1D3=1X12=1X17=2I8=1X28=1X36=1X17=1D15=1D1=1I14=1X2=1X14=1D14=1D16=1I11=1D34=1       *       0       0       TGGACTCGAATGGAATAATCATTGAACGAATCGAATGGAATCATCATCGATGATGAATGGAATCATCGAATGGAATCGAATAGTGAAGAATCCAGAATCGAATGGACCAAGGAACCCCCGGAAGTAATGGAATCAAATCATGAATCAATGGAACACCACAAGAAAATGGAATTACATGAATTGAATGGATGGACATCATCAATGGATTCAATGAACATCAATAATTATTGAATCATCATCAATGGAATCAATGGTATCATTGAATAATCGAATGAATCATCATCAGATGGAAATGAATGGAATCATAGAATGGAATCGAATGGATCATTGAATGGAATCAGATGGAACATCGAATGGACTGAATGAAATTATGGACTAAGGATCATGATTGAATGGAATTGAATGGAATCATCGAATGGTCTCGATTGAATTTATCAAATGGAATCGAATGAATCACGAAAGAATCGAAGGAAAATCATGAATGGATCAATGGAATTATTCAATGAATGGAATCGAATATCGAATGCAATCGAATGGAATTCATCGAATGAATCGAATAGAATTCATCGAATGGACTCAAT
```



```

$ cat M671-2_contig3100_aligned.sam | printgaps /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa M671-2_contig3100
INFO: fasta: /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa

```


output files:
```
-rw-rw-r-- 1 254 Sep  3 10:59 M671-2_contig3100.aln.coords.bed
-rw-rw-r-- 1 40K Sep  3 10:59 M671-2_contig3100.indel.bed
-rw-rw-r-- 1 15K Sep  3 10:59 M671-2_contig3100.snp.bed
-rw-rw-r-- 1 704 Sep  3 10:59 M671-2_contig3100.svs.bed

```

```
$ cat M671-2_contig3100.svs.bed
#target_name    target_start_0  target_end_0    sv_type sv_len  query_strand    query_name  query_start_0   query_end_0 query_length    matching_bases_count    consumed_bases_count    percent_identity    sequence
1   143213358   143213786   deletion    428 -   ctg3088/0/0_5593    4713    4713    5593    5220    6509    0.801967    ATCATTGAAGAGAATTGAATGGAATCGTCATCGAATGAATTGAATGCAATCATCAAATGGTCTCGAATGGAATCATCATCTAATAGAAAGGAATGGAATCATCGCATAGAATCGAATGGAATTATCATCGAATGGAATCGAATGGTATCAACACCAAACGAAAAAAAACGGAATTTTCGAATGGAATCGAAGAGAATCTTCGAACGGACCCGAATGGAATCATCTAATGGAATGGAATGGAATAATCCATGGACTGGAAGGCAATCATCATCGAATGGAATCGAATGGAATCATCGAATGGACTCGAATGGAATAATCATTGAACGGAATCCAATGGAATCATCATCGGATGGAAACGAATGGAATCATCATCGAATGGAAATGAAAGGAGTCAACATCTAATGGAATTGCATGGAATCATCATAAAA

```






## blasrmc


### index for reference
```
$ /home/litong/software/blasr/alignment/bin/sawritermc Homo_sapiens.GRCh38.dna.primary_assembly.fa
```

```
/home/litong/software/blasr/alignment/bin/blasrmc -clipping  hard -sam -alignContigs -minMapQV 30 -nproc 60 -minPctIdentity 50 -unaligned /home/wuzhikun/Project/PanGenome/CallSV/Smartie/CN353/CN353_blasr.unalign -out /home/wuzhikun/Project/PanGenome/CallSV/Smartie/CN353/CN353_blasr.sam -sa /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa.sa /home/wuzhikun/Project/PanGenome/Assembly/CN353_assembly_polish_temp.fasta /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa > /home/wuzhikun/Project/PanGenome/log/blasr_CN353.log 2>&1
```



### 
```
cat /home/wuzhikun/Project/PanGenome/CallSV/Smartie/CN353/CN353_blasr.sam | printgaps /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/PanGenome/CallSV/Smartie/CN353/CN353
```

output file:
```
-rw-rw-r-- 1  345 Sep  8 09:46 CN353.aln.coords.bed
-rw-rw-r-- 1    0 Sep  8 09:44 CN353_blasr.unalign
-rw-rw-r-- 1  20M Sep  8 09:46 CN353.indel.bed
-rw-rw-r-- 1 2.7M Sep  8 09:46 CN353.snp.bed
-rw-rw-r-- 1  47K Sep  8 09:46 CN353.svs.bed

```


```
$ head CN353.svs.bed

#target_name    target_start_0  target_end_0    sv_type sv_len  query_strand    query_name  query_start_0   query_end_0 query_length    matching_bases_count    consumed_bases_count    percent_identity    sequence
18  47684880    47684880    insertion   165 +   ctg1/0/0_15024684   21266   21431   15024685    14750225 15056534   0.979656    TTATATATATTATATATTTTATATATATTATATATATTATATATATTTATATATATTATATATTTTATATATATTATATATATTATATATATTTATATATAATATATATATATTTTATATATAATATATATATATTTTATATATAATATATATTTTATATATAAT
18  47850356    47850356    insertion   50  +   ctg1/0/0_15024684   184354  184404  15024685    14750225 15056534   0.979656    TTATTATAATATATATTATTATATATATATTATAATATATATATATGTAT

```



```
$ head CN353.aln.coords.bed

#target_name    target_start_0  target_end_0    query_name  query_start_0   query_end_0 query_strand    query_length    matching_bases_count    consumed_bases_count    percent_identity
18  47666569    62691269    ctg1/0/0_15024684   3243    14812938    +   15024685    14750225    15056534 0.979656
18  62735612    62906279    ctg1/0/0_15024684   14856589    15024655    +   15024685    167664  170848  0.981364
```


