## canu 

### install canu
```
$ conda install -c bioconda canu
```

## canu parameters
```
$ canu --help

usage: canu [-correct | -trim | -assemble | -trim-assemble] \
            [-s <assembly-specifications-file>] \
             -p <assembly-prefix> \
             -d <assembly-directory> \
             genomeSize=<number>[g|m|k] \
             errorRate=0.X \
            [other-options] \
            [-pacbio-raw | -pacbio-corrected | -nanopore-raw | -nanopore-corrected] *fastq

  By default, all three stages (correct, trim, assemble) are computed.
  To compute only a single stage, use:
    -correct       - generate corrected reads
    -trim          - generate trimmed reads
    -assemble      - generate an assembly
    -trim-assemble - generate trimmed reads and then assemble them

  The assembly is computed in the (created) -d <assembly-directory>, with most
  files named using the -p <assembly-prefix>.

  The genome size is your best guess of the genome size of what is being assembled.
  It is used mostly to compute coverage in reads.  Fractional values are allowed: '4.7m'
  is the same as '4700k' and '4700000'

  The errorRate is not used correctly (we're working on it).  Don't set it
  If you want to change the defaults, use the various utg*ErrorRate options.

  A full list of options can be printed with '-options'.  All options
  can be supplied in an optional sepc file.

  Reads can be either FASTA or FASTQ format, uncompressed, or compressed
  with gz, bz2 or xz.  Reads are specified by the technology they were
  generated with:
    -pacbio-raw         <files>
    -pacbio-corrected   <files>
    -nanopore-raw       <files>
    -nanopore-corrected <files>

Complete documentation at http://canu.readthedocs.org/en/latest/

ERROR:  Invalid command line option '--help'.  Did you forget quotes around options with spaces?
ERROR:  Assembly name prefix not supplied with -p.
ERROR:  Directory not supplied with -d.
ERROR:  Invalid 'corErrorRate' specified; must be set
ERROR:  Required parameter 'genomeSize' is not set

```


### canu options
```
$ canu -options
batConcurrency                          Unused, only one process supported
batMemory                               Approximate maximum memory usage, in gigabytes, default is the maxMemory limit
batOptions                              Advanced options to bogart
batThreads                              Number of threads to use; default is the maxThreads limit
cnsConcurrency                          If grid not enabled, number of unitig consensus jobs to run at the same time; default is n_proc / n_threads
cnsConsensus                            Which consensus algorithm to use; 'pbdagcon' (fast, reliable); 'utgcns' (multialignment output); 'quick' (single read mosaic); default 'pbdagcon'
cnsErrorRate                            Consensus expects alignments at about this error rate
cnsMaxCoverage                          Limit unitig consensus to at most this coverage; default '0' = unlimited
cnsMemory                               Amount of memory, in gigabytes, to use for unitig consensus jobs
cnsPartitionMin                         Don't make a consensus partition with fewer than N reads
cnsPartitions                           Partition consensus into N jobs
cnsThreads                              Number of threads to use for unitig consensus jobs
contigFilter                            Parameters to filter out 'unassembled' unitigs: minReads; minLength; singleReadSpan; lowCovFraction, lowCovDepth
corConcurrency                          If grid not enabled, number of read correction jobs to run at the same time; default is n_proc / n_threads
corConsensus                            Which consensus algorithm to use; only 'falcon' and 'falconpipe' are supported; default 'falconpipe'
corErrorRate                            Only use raw alignments below this error rate to construct corrected reads
corFilter                               Method to filter short reads from correction; 'quick' or 'expensive'; default 'expensive'
corLegacyFilter                         Expert option: global filter, length * identity (default) or length with  broken by identity (if on)
corMMapBlockSize                        Number of reads per 1GB; memory * blockSize = the size of  block loaded into memory per job
corMMapMerSize                          K-mer size for seeds in minmap
corMaxEvidenceCoverageGlobal            Limit reads used for correction to supporting at most this coverage; default: '1.0x' = 1.0 * estimated coverage
corMaxEvidenceCoverageLocal             Limit reads being corrected to at most this much evidence coverage; default: '2.0x' = 2.0 * estimated coverage
corMaxEvidenceErate                     Limit read correction to only overlaps at or below this fraction error; default: unlimited
corMemory                               Amount of memory, in gigabytes, to use for read correction jobs
corMhapBlockSize                        Number of reads per 1GB; memory * blockSize = the size of  block loaded into memory per job
corMhapFilterThreshold                  Value between 0 and 1. kmers which comprise more than this percentage of the input are downweighted
corMhapFilterUnique                     Expert option: True or false, supress the low-frequency k-mer distribution based on them being likely noise and not true overlaps. Threshold auto-computed based on error rate and coverage.
corMhapMerSize                          K-mer size for seeds in mhap
corMhapNoTf                             Expert option: True or false, do not use tf weighting, only idf of tf-idf.
corMhapOptions                          Expert option: free-form parameters to pass to MHAP.
corMhapOrderedMerSize                   K-mer size for second-stage filter in mhap
corMhapSensitivity                      Coarse sensitivity level: 'low', 'normal' or 'high'.  Usually set automatically based on coverage; 'high' <= 30x < 'normal' < 60x <= 'low'
corMhapVersion                          Version of the MHAP jar file to use
corMinCoverage                          Minimum number of bases supporting each corrected base, if less than this sequences are split; default based on input read coverage: 0 <= 30x < 4 < 60x <= 4
corMinEvidenceLength                    Limit read correction to only overlaps longer than this; default: unlimited
corOutCoverage                          Only correct the longest reads up to this coverage; default 40
corOverlapper                           Which overlap algorithm to use for correction
corOvlErrorRate                         Overlaps above this error rate are not computed
corOvlFilter                            Filter overlaps based on expected kmers vs observed kmers
corOvlFrequentMers                      Do not seed overlaps with these kmers (fasta format)
corOvlHashBits                          Width of the kmer hash.  Width 22=1gb, 23=2gb, 24=4gb, 25=8gb.  Plus 10b per corOvlHashBlockLength
corOvlHashBlockLength                   Amount of sequence (bp) to load into the overlap hash table
corOvlHashLoad                          Maximum hash table load.  If set too high, table lookups are inefficent; if too low, search overhead dominates run time; default 0.75
corOvlMerDistinct                       K-mer frequency threshold; the least frequent fraction of distinct mers can seed overlaps
corOvlMerSize                           K-mer size for seeds in overlaps
corOvlMerThreshold                      K-mer frequency threshold; mers more frequent than this count are ignored; default 'auto'
corOvlMerTotal                          K-mer frequency threshold; the least frequent fraction of all mers can seed overlaps
corOvlRefBlockLength                    Amount of sequence (bp) to search against the hash table per batch
corOvlRefBlockSize                      Number of reads to search against the hash table per batch
corPartitionMin                         Don't make a read correction partition with fewer than N reads
corPartitions                           Partition read correction into N jobs
corReAlign                              Compute actual alignments from overlaps; 'raw' from output, 'final' from overlap store; uses either obtErrorRate or ovlErrorRate, depending on which overlaps are computed
corThreads                              Number of threads to use for read correction jobs
cormhapConcurrency                      If grid not enabled, number of mhap overlaps for correction jobs to run at the same time; default is n_proc / n_threads
cormhapMemory                           Amount of memory, in gigabytes, to use for mhap overlaps for correction jobs
cormhapThreads                          Number of threads to use for mhap overlaps for correction jobs
cormmapConcurrency                      If grid not enabled, number of mmap overlaps for correction jobs to run at the same time; default is n_proc / n_threads
cormmapMemory                           Amount of memory, in gigabytes, to use for mmap overlaps for correction jobs
cormmapThreads                          Number of threads to use for mmap overlaps for correction jobs
corovlConcurrency                       If grid not enabled, number of overlaps for correction jobs to run at the same time; default is n_proc / n_threads
corovlMemory                            Amount of memory, in gigabytes, to use for overlaps for correction jobs
corovlThreads                           Number of threads to use for overlaps for correction jobs
enableOEA                               Do overlap error adjustment - comprises two steps: read error detection (RED) and overlap error adjustment (OEA); default 'true'
errorRate                               The expected error rate in the corrected reads, typically set based on sequencing type. Set to 0 to try to estimate dynamically. (EXPERIMENTAL)
falconSense                             Path to fc_consensus.py or falcon_sense.bin
genomeSize                              An estimate of the size of the genome
gnuplot                                 Path to the gnuplot executable
gnuplotImageFormat                      Image format that gnuplot will generate, used in HTML reports.  Default: based on gnuplot, 'png', 'svg' or 'gif'
gnuplotTested                           If set, skip the initial testing of gnuplot
gridOptions                             Grid engine options applied to all jobs
gridOptionsExecutive                    Grid engine options applied to the canu executive script
gridOptionsJobName                      Grid jobs job-name suffix
gridOptionsbat                          Grid engine options applied to unitig construction jobs
gridOptionscns                          Grid engine options applied to unitig consensus jobs
gridOptionscor                          Grid engine options applied to read correction jobs
gridOptionscormhap                      Grid engine options applied to mhap overlaps for correction jobs
gridOptionscormmap                      Grid engine options applied to mmap overlaps for correction jobs
gridOptionscorovl                       Grid engine options applied to overlaps for correction jobs
gridOptionsmeryl                        Grid engine options applied to mer counting jobs
gridOptionsobtmhap                      Grid engine options applied to mhap overlaps for trimming jobs
gridOptionsobtmmap                      Grid engine options applied to mmap overlaps for trimming jobs
gridOptionsobtovl                       Grid engine options applied to overlaps for trimming jobs
gridOptionsoea                          Grid engine options applied to overlap error adjustment jobs
gridOptionsovb                          Grid engine options applied to overlap store bucketizing jobs
gridOptionsovs                          Grid engine options applied to overlap store sorting jobs
gridOptionsred                          Grid engine options applied to read error detection jobs
gridOptionsutgmhap                      Grid engine options applied to mhap overlaps for unitig construction jobs
gridOptionsutgmmap                      Grid engine options applied to mmap overlaps for unitig construction jobs
gridOptionsutgovl                       Grid engine options applied to overlaps for unitig construction jobs
java                                    Java interpreter to use; at least version 1.8; default 'java'
maxMemory                               Maximum memory to use by any component of the assembler
maxThreads                              Maximum number of compute threads to use by any component of the assembler
merylConcurrency                        Unused, there is only one process
merylMemory                             Amount of memory, in gigabytes, to use for mer counting
merylThreads                            Number of threads to use for mer counting
minMemory                               Minimum amount of memory needed to compute the assembly (do not set unless prompted!)
minOverlapLength                        Overlaps shorter than this length are not computed; default 500
minReadLength                           Reads shorter than this length are not loaded into the assembler; default 1000
minThreads                              Minimum number of compute threads suggested to compute the assembly
obtErrorRate                            Stringency of overlaps to use for trimming
obtMMapBlockSize                        Number of reads per 1GB; memory * blockSize = the size of  block loaded into memory per job
obtMMapMerSize                          K-mer size for seeds in minmap
obtMhapBlockSize                        Number of reads per 1GB; memory * blockSize = the size of  block loaded into memory per job
obtMhapFilterThreshold                  Value between 0 and 1. kmers which comprise more than this percentage of the input are downweighted
obtMhapFilterUnique                     Expert option: True or false, supress the low-frequency k-mer distribution based on them being likely noise and not true overlaps. Threshold auto-computed based on error rate and coverage.
obtMhapMerSize                          K-mer size for seeds in mhap
obtMhapNoTf                             Expert option: True or false, do not use tf weighting, only idf of tf-idf.
obtMhapOptions                          Expert option: free-form parameters to pass to MHAP.
obtMhapOrderedMerSize                   K-mer size for second-stage filter in mhap
obtMhapSensitivity                      Coarse sensitivity level: 'low', 'normal' or 'high'.  Usually set automatically based on coverage; 'high' <= 30x < 'normal' < 60x <= 'low'
obtMhapVersion                          Version of the MHAP jar file to use
obtOverlapper                           Which overlap algorithm to use for overlap based trimming
obtOvlErrorRate                         Overlaps at or below this error rate are used to trim reads
obtOvlFilter                            Filter overlaps based on expected kmers vs observed kmers
obtOvlFrequentMers                      Do not seed overlaps with these kmers (fasta format)
obtOvlHashBits                          Width of the kmer hash.  Width 22=1gb, 23=2gb, 24=4gb, 25=8gb.  Plus 10b per obtOvlHashBlockLength
obtOvlHashBlockLength                   Amount of sequence (bp) to load into the overlap hash table
obtOvlHashLoad                          Maximum hash table load.  If set too high, table lookups are inefficent; if too low, search overhead dominates run time; default 0.75
obtOvlMerDistinct                       K-mer frequency threshold; the least frequent fraction of distinct mers can seed overlaps
obtOvlMerSize                           K-mer size for seeds in overlaps
obtOvlMerThreshold                      K-mer frequency threshold; mers more frequent than this count are ignored; default 'auto'
obtOvlMerTotal                          K-mer frequency threshold; the least frequent fraction of all mers can seed overlaps
obtOvlRefBlockLength                    Amount of sequence (bp) to search against the hash table per batch
obtOvlRefBlockSize                      Number of reads to search against the hash table per batch
obtReAlign                              Compute actual alignments from overlaps; 'raw' from output, 'final' from overlap store; uses either obtErrorRate or ovlErrorRate, depending on which overlaps are computed
obtmhapConcurrency                      If grid not enabled, number of mhap overlaps for trimming jobs to run at the same time; default is n_proc / n_threads
obtmhapMemory                           Amount of memory, in gigabytes, to use for mhap overlaps for trimming jobs
obtmhapThreads                          Number of threads to use for mhap overlaps for trimming jobs
obtmmapConcurrency                      If grid not enabled, number of mmap overlaps for trimming jobs to run at the same time; default is n_proc / n_threads
obtmmapMemory                           Amount of memory, in gigabytes, to use for mmap overlaps for trimming jobs
obtmmapThreads                          Number of threads to use for mmap overlaps for trimming jobs
obtovlConcurrency                       If grid not enabled, number of overlaps for trimming jobs to run at the same time; default is n_proc / n_threads
obtovlMemory                            Amount of memory, in gigabytes, to use for overlaps for trimming jobs
obtovlThreads                           Number of threads to use for overlaps for trimming jobs
oeaBatchLength                          Number of bases per overlap error correction batch
oeaBatchSize                            Number of reads per overlap error correction batch
oeaConcurrency                          If grid not enabled, number of overlap error adjustment jobs to run at the same time; default is n_proc / n_threads
oeaMemory                               Amount of memory, in gigabytes, to use for overlap error adjustment jobs
oeaThreads                              Number of threads to use for overlap error adjustment jobs
onFailure                               Full path to command to run on failure
onSuccess                               Full path to command to run on successful completion
ovbConcurrency                          If grid not enabled, number of overlap store bucketizing jobs to run at the same time; default is n_proc / n_threads
ovbMemory                               Amount of memory, in gigabytes, to use for overlap store bucketizing jobs
ovbThreads                              Number of threads to use for overlap store bucketizing jobs
ovsConcurrency                          If grid not enabled, number of overlap store sorting jobs to run at the same time; default is n_proc / n_threads
ovsMemory                               Amount of memory, in gigabytes, to use for overlap store sorting jobs
ovsMethod                               Use the 'sequential' or 'parallel' algorithm for constructing an overlap store; default 'sequential'
ovsThreads                              Number of threads to use for overlap store sorting jobs
pathMap                                 File with a hostname to binary directory map
redBatchLength                          Number of bases per fragment error detection batch
redBatchSize                            Number of reads per fragment error detection batch
redConcurrency                          If grid not enabled, number of read error detection jobs to run at the same time; default is n_proc / n_threads
redMemory                               Amount of memory, in gigabytes, to use for read error detection jobs
redThreads                              Number of threads to use for read error detection jobs
saveMerCounts                           Save full mer counting results, sometimes useful
saveOverlaps                            Save intermediate overlap files, almost never a good idea
saveReadCorrections                     Save intermediate read correction files, almost never a good idea
shell                                   Command interpreter to use; sh-compatible (e.g., bash), NOT C-shell (csh or tcsh); default '/bin/sh'
showNext                                Don't run any commands, just report what would run
stopAfter                               Tell canu when to halt execution
stopBefore                              Tell canu when to halt execution
stopOnReadQuality                       Stop if a significant portion of the input data is too short or has quality value or base composition errors
trimReadsCoverage                       Minimum depth of evidence to retain bases; default '1'
trimReadsOverlap                        Minimum overlap between evidence to make contiguous trim; default '1'
unitigger                               Which unitig algorithm to use; only 'bogart' supported; default 'bogart'
useGrid                                 If 'true', enable grid-based execution; if 'false', run all jobs on the local machine; if 'remote', create jobs for grid execution but do not submit; default 'true'
useGridBAT                              If 'true', run module BAT under grid control; if 'false' run locally.
useGridCNS                              If 'true', run module CNS under grid control; if 'false' run locally.
useGridCOR                              If 'true', run module COR under grid control; if 'false' run locally.
useGridCORMHAP                          If 'true', run module CORMHAP under grid control; if 'false' run locally.
useGridCORMMAP                          If 'true', run module CORMMAP under grid control; if 'false' run locally.
useGridCOROVL                           If 'true', run module COROVL under grid control; if 'false' run locally.
useGridMERYL                            If 'true', run module MERYL under grid control; if 'false' run locally.
useGridOBTMHAP                          If 'true', run module OBTMHAP under grid control; if 'false' run locally.
useGridOBTOVL                           If 'true', run module OBTOVL under grid control; if 'false' run locally.
useGridOEA                              If 'true', run module OEA under grid control; if 'false' run locally.
useGridOVB                              If 'true', run module OVB under grid control; if 'false' run locally.
useGridOVS                              If 'true', run module OVS under grid control; if 'false' run locally.
useGridRED                              If 'true', run module RED under grid control; if 'false' run locally.
useGridUTGMHAP                          If 'true', run module UTGMHAP under grid control; if 'false' run locally.
useGridUTGMMAP                          If 'true', run module UTGMMAP under grid control; if 'false' run locally.
useGridUTGOVL                           If 'true', run module UTGOVL under grid control; if 'false' run locally.
utgGraphDeviation                       Overlaps this much above median will not be used for initial graph construction (BOGART)
utgMMapBlockSize                        Number of reads per 1GB; memory * blockSize = the size of  block loaded into memory per job
utgMMapMerSize                          K-mer size for seeds in minmap
utgMhapBlockSize                        Number of reads per 1GB; memory * blockSize = the size of  block loaded into memory per job
utgMhapFilterThreshold                  Value between 0 and 1. kmers which comprise more than this percentage of the input are downweighted
utgMhapFilterUnique                     Expert option: True or false, supress the low-frequency k-mer distribution based on them being likely noise and not true overlaps. Threshold auto-computed based on error rate and coverage.
utgMhapMerSize                          K-mer size for seeds in mhap
utgMhapNoTf                             Expert option: True or false, do not use tf weighting, only idf of tf-idf.
utgMhapOptions                          Expert option: free-form parameters to pass to MHAP.
utgMhapOrderedMerSize                   K-mer size for second-stage filter in mhap
utgMhapSensitivity                      Coarse sensitivity level: 'low', 'normal' or 'high'.  Usually set automatically based on coverage; 'high' <= 30x < 'normal' < 60x <= 'low'
utgMhapVersion                          Version of the MHAP jar file to use
utgOverlapper                           Which overlap algorithm to use for unitig construction
utgOvlErrorRate                         Overlaps at or below this error rate are used to trim reads
utgOvlFilter                            Filter overlaps based on expected kmers vs observed kmers
utgOvlFrequentMers                      Do not seed overlaps with these kmers (fasta format)
utgOvlHashBits                          Width of the kmer hash.  Width 22=1gb, 23=2gb, 24=4gb, 25=8gb.  Plus 10b per utgOvlHashBlockLength
utgOvlHashBlockLength                   Amount of sequence (bp) to load into the overlap hash table
utgOvlHashLoad                          Maximum hash table load.  If set too high, table lookups are inefficent; if too low, search overhead dominates run time; default 0.75
utgOvlMerDistinct                       K-mer frequency threshold; the least frequent fraction of distinct mers can seed overlaps
utgOvlMerSize                           K-mer size for seeds in overlaps
utgOvlMerThreshold                      K-mer frequency threshold; mers more frequent than this count are ignored; default 'auto'
utgOvlMerTotal                          K-mer frequency threshold; the least frequent fraction of all mers can seed overlaps
utgOvlRefBlockLength                    Amount of sequence (bp) to search against the hash table per batch
utgOvlRefBlockSize                      Number of reads to search against the hash table per batch
utgReAlign                              Compute actual alignments from overlaps; 'raw' from output, 'final' from overlap store; uses either obtErrorRate or ovlErrorRate, depending on which overlaps are computed
utgRepeatConfusedBP                     Repeats where the next best edge is at least this many bp shorter will not be split (BOGART)
utgRepeatDeviation                      Overlaps this much above mean unitig error rate will not be used for repeat splitting (BOGART)
utgmhapConcurrency                      If grid not enabled, number of mhap overlaps for unitig construction jobs to run at the same time; default is n_proc / n_threads
utgmhapMemory                           Amount of memory, in gigabytes, to use for mhap overlaps for unitig construction jobs
utgmhapThreads                          Number of threads to use for mhap overlaps for unitig construction jobs
utgmmapConcurrency                      If grid not enabled, number of mmap overlaps for unitig construction jobs to run at the same time; default is n_proc / n_threads
utgmmapMemory                           Amount of memory, in gigabytes, to use for mmap overlaps for unitig construction jobs
utgmmapThreads                          Number of threads to use for mmap overlaps for unitig construction jobs
utgovlConcurrency                       If grid not enabled, number of overlaps for unitig construction jobs to run at the same time; default is n_proc / n_threads
utgovlMemory                            Amount of memory, in gigabytes, to use for overlaps for unitig construction jobs
utgovlThreads                           Number of threads to use for overlaps for unitig construction jobs

```





Canu v1.4 (+11 commits) r8006 (4a7090bd17c914f5c21bacbebf4add163e492d54)
was used to assemble the initial 20-fold coverage data set:
```
canu -p asm -d asm genomeSize=3.1g gridOptionsJobNa
me=na12878nano "gridOptions=–time 72:00:00–partition
norm" -nanopore-raw rel2*.fastq.gz corMinCoverage=0
corMaxEvidenceErate=0.22 errorRate=0.045
```


These are the suggested low-coverage parameters from the Canu documentation, but with a decreased maximum evidence error rate. This specific
parameter was decreased to reduced memory requirements after it was determined that the MinHash overlapping algorithm was underestimating error
rates owing to systematic error in the reads. Counterintuitively, this systematic
error makes two reads look more similar than they are, because they share
more k-mers than expected under a random model. Manually decreasing the
maximum overlap error rate threshold adjusted for this bias. The assembly
took 40K CPU hours (25K to correct and 15K to assemble). This is about twofold slower than a comparable PacBio data set, mostly because of the higher
noise and errors in the nanopore reads.
The same version of Canu was also used to assemble the 30-fold data set:

```
canu -p asm -d asm genomeSize=3.1g gridOptionsJobNa
me=na12878nano "gridOptions=–time 72:00:00–partition
norm" -nanopore-raw rel3*.fastq.gz corMinCoverage=0
corMaxEvidenceErate=0.22 errorRate=0.045 "corMhapOptions=–threshold 0.8–num-hashes 512–ordered-sketchsize 1000–ordered-kmer-size 14"
```


For this larger data set, overlapping was again tweaked by reducing the number
of hashes used and increasing the minimum overlap identity threshold. This
has the effect of lowering sensitivity to further compensate for the bias in the
input reads. This assembly required 62K CPU hours (29K to correct, 33K to
assemble) and a peak of 120 Gbp of memory, which is about fourfold slower
than a comparable PacBio data set. The assembly ran on a cluster comprised
of a mix of 48-thread dual-socket Intel E5-2680 v3 @ 2.50GHz CPUs with 128
Gbp of memory and 8-thread dual-socket Intel CPU E5-2698 v4 @ 2.20GHz
CPUs with 1,024 Gbp of memory.
The combined data set incorporating an additional 5× coverage of
ultra-long reads was assembled with an updated version of Canu v1.4 (+125
commits) r8120:

```
canu -p asm -d asm genomeSize=3.1g gridOptionsJo
bName=na12878nano "gridOptions=–time 72:00:00–partition norm" -nanopore-raw rel3*.fastq.gz -nanopore-raw rel4*.fastq.gz "corMhapOptions=–threshold
0.8–num-hashes 512–ordered-sketch-size 1000–orderedkmer-size 14" batOptions="-dg 3 -db 3 -dr 1 -el 2000
-nofilter suspicious-lopsided"
```
