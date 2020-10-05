## GATK BaseRecalibrator

### GATK4 parameters

```
$ ./gatk  --list
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar --help
USAGE:  <program name> [-h]

Available Programs:
--------------------------------------------------------------------------------------
Base Calling:                                    Tools that process sequencing machine data, e.g. Illumina base calls, and detect sequencing level attributes, e.g. adapters
    CheckIlluminaDirectory (Picard)              Asserts the validity for specified Illumina basecalling data.  
    CollectIlluminaBasecallingMetrics (Picard)   Collects Illumina Basecalling metrics for a sequencing run.  
    CollectIlluminaLaneMetrics (Picard)          Collects Illumina lane metrics for the given BaseCalling analysis directory.  
    ExtractIlluminaBarcodes (Picard)             Tool determines the barcode for each read in an Illumina lane.  
    IlluminaBasecallsToFastq (Picard)            Generate FASTQ file(s) from Illumina basecall read data.  
    IlluminaBasecallsToSam (Picard)              Transforms raw Illumina sequencing data into an unmapped SAM or BAM file.
    MarkIlluminaAdapters (Picard)                Reads a SAM or BAM file and rewrites it with new adapter-trimming tags.  

--------------------------------------------------------------------------------------
Copy Number Variant Discovery:                   Tools that analyze read coverage to detect copy number variants.
    AnnotateIntervals                            Annotates intervals with GC content, mappability, and segmental-duplication content
    CallCopyRatioSegments                        Calls copy-ratio segments as amplified, deleted, or copy-number neutral
    CollectAllelicCountsSpark                    Collects ref/alt counts at sites.
    CombineSegmentBreakpoints                    (EXPERIMENTAL Tool) Combine the breakpoints of two segment files and annotate the resulting intervals with chosen columns from each file.
    CreateReadCountPanelOfNormals                Creates a panel of normals for read-count denoising
    DenoiseReadCounts                            Denoises read counts to produce denoised copy ratios
    DetermineGermlineContigPloidy                Determines the baseline contig ploidy for germline samples given counts data
    FilterIntervals                              Filters intervals based on annotations and/or count statistics
    GermlineCNVCaller                            Calls copy-number variants in germline samples given their counts and the output of DetermineGermlineContigPloidy
    MergeAnnotatedRegions                        (EXPERIMENTAL Tool) (EXPERIMENTAL) Merge annotated genomic regions based entirely on touching/overlapping intervals.
    MergeAnnotatedRegionsByAnnotation            (EXPERIMENTAL Tool) (EXPERIMENTAL) Merge annotated genomic regions within specified distance if annotation value(s) are exactly the same.
    ModelSegments                                Models segmented copy ratios from denoised read counts and segmented minor-allele fractions from allelic counts
    PlotDenoisedCopyRatios                       Creates plots of denoised copy ratios
    PlotModeledSegments                          Creates plots of denoised and segmented copy-ratio and minor-allele-fraction estimates
    PostprocessGermlineCNVCalls                  Postprocesses the output of GermlineCNVCaller and generates VCF files.
    TagGermlineEvents                            (EXPERIMENTAL Tool) (EXPERIMENTAL) Do a simplistic tagging of germline events in a tumor segment file.

--------------------------------------------------------------------------------------
Coverage Analysis:                               Tools that count coverage, e.g. depth per allele
    ASEReadCounter                               Generates table of filtered base counts at het sites for allele specific expression
    CollectAllelicCounts                         Collects reference and alternate allele counts at specified sites
    CollectF1R2Counts                            Collect F1R2 read counts for the Mutect2 orientation bias mixture model filter
    CollectReadCounts                            Collects read counts at specified intervals
    CountBases                                   Count bases in a SAM/BAM/CRAM file
    CountBasesSpark                              (BETA Tool) Counts bases in the input SAM/BAM
    CountReads                                   Count reads in a SAM/BAM/CRAM file
    CountReadsSpark                              (BETA Tool) Counts reads in the input SAM/BAM
    GetPileupSummaries                           (BETA Tool) Tabulates pileup metrics for inferring contamination
    Pileup                                       Prints read alignments in samtools pileup format
    PileupSpark                                  (BETA Tool) Prints read alignments in samtools pileup format

--------------------------------------------------------------------------------------
Diagnostics and Quality Control:                 Tools that collect sequencing quality related and comparative metrics
    AccumulateVariantCallingMetrics (Picard)     Combines multiple Variant Calling Metrics files into a single file
    AnalyzeCovariates                            Evaluate and compare base quality score recalibration (BQSR) tables
    BamIndexStats (Picard)                       Generate index statistics from a BAM file
    CalcMetadataSpark                            (BETA Tool) (Internal) Collects read metrics relevant to structural variant discovery
    CalculateContamination                       Calculate the fraction of reads coming from cross-sample contamination
    CalculateReadGroupChecksum (Picard)          Creates a hash code based on the read groups (RG).  
    CheckFingerprint (Picard)                    Computes a fingerprint from the supplied input (SAM/BAM or VCF) file and compares it to the provided genotypes
    CheckPileup                                  Compare GATK's internal pileup to a reference Samtools mpileup
    CheckTerminatorBlock (Picard)                Asserts the provided gzip file's (e.g., BAM) last block is well-formed; RC 100 otherwise
    ClusterCrosscheckMetrics (Picard)            Clusters the results of a CrosscheckFingerprints run by LOD score
    CollectAlignmentSummaryMetrics (Picard)      <b>Produces a summary of alignment metrics from a SAM or BAM file.</b>  
    CollectBaseDistributionByCycle (Picard)      Chart the nucleotide distribution per cycle in a SAM or BAM file
    CollectBaseDistributionByCycleSpark          (BETA Tool) Collects base distribution per cycle in SAM/BAM/CRAM file(s).
    CollectGcBiasMetrics (Picard)                Collect metrics regarding GC bias. 
    CollectHiSeqXPfFailMetrics (Picard)          Classify PF-Failing reads in a HiSeqX Illumina Basecalling directory into various categories.
    CollectHsMetrics (Picard)                    Collects hybrid-selection (HS) metrics for a SAM or BAM file.  
    CollectIndependentReplicateMetrics (Picard)  (EXPERIMENTAL Tool) Estimates the rate of independent replication of reads within a bam.
    CollectInsertSizeMetrics (Picard)            Collect metrics about the insert size distribution of a paired-end library.
    CollectInsertSizeMetricsSpark                (BETA Tool) Collects insert size distribution information on alignment data
    CollectJumpingLibraryMetrics (Picard)        Collect jumping library metrics. 
    CollectMultipleMetrics (Picard)              Collect multiple classes of metrics.  
    CollectMultipleMetricsSpark                  (BETA Tool) Runs multiple metrics collection modules for a given alignment file
    CollectOxoGMetrics (Picard)                  Collect metrics to assess oxidative artifacts.
    CollectQualityYieldMetrics (Picard)          Collect metrics about reads that pass quality thresholds and Illumina-specific filters.  
    CollectQualityYieldMetricsSpark              (BETA Tool) Collects quality yield metrics from SAM/BAM/CRAM file(s).
    CollectRawWgsMetrics (Picard)                Collect whole genome sequencing-related metrics.  
    CollectRnaSeqMetrics (Picard)                Produces RNA alignment metrics for a SAM or BAM file.  
    CollectRrbsMetrics (Picard)                  <b>Collects metrics from reduced representation bisulfite sequencing (Rrbs) data.</b>  
    CollectSamErrorMetrics (Picard)              Program to collect error metrics on bases stratified in various ways.
    CollectSequencingArtifactMetrics (Picard)    Collect metrics to quantify single-base sequencing artifacts.  
    CollectTargetedPcrMetrics (Picard)           Calculate PCR-related metrics from targeted sequencing data. 
    CollectVariantCallingMetrics (Picard)        Collects per-sample and aggregate (spanning all samples) metrics from the provided VCF file
    CollectWgsMetrics (Picard)                   Collect metrics about coverage and performance of whole genome sequencing (WGS) experiments.
    CollectWgsMetricsWithNonZeroCoverage (Picard)(EXPERIMENTAL Tool) Collect metrics about coverage and performance of whole genome sequencing (WGS) experiments.  
    CompareBaseQualities                         Compares the base qualities of two SAM/BAM/CRAM files
    CompareDuplicatesSpark                       (BETA Tool) Determine if two potentially identical BAMs have the same duplicate reads
    CompareMetrics (Picard)                      Compare two metrics files.
    CompareSAMs (Picard)                         Compare two input ".sam" or ".bam" files.  
    ConvertSequencingArtifactToOxoG (Picard)     Extract OxoG metrics from generalized artifacts metrics.  
    CrosscheckFingerprints (Picard)              Checks that all data in the input files appear to have come from the same individual
    CrosscheckReadGroupFingerprints (Picard)     DEPRECATED: USE CrosscheckFingerprints. Checks if all read groups appear to come from the same individual.
    EstimateLibraryComplexity (Picard)           Estimates the numbers of unique molecules in a sequencing library.  
    FlagStat                                     Accumulate flag statistics given a BAM file
    FlagStatSpark                                (BETA Tool) Spark tool to accumulate flag statistics
    GetSampleName                                (BETA Tool) Emit a single sample name
    IdentifyContaminant (Picard)                 Computes a fingerprint from the supplied SAM/BAM file, given a contamination estimate.
    MeanQualityByCycle (Picard)                  Collect mean quality by cycle.
    MeanQualityByCycleSpark                      (BETA Tool) MeanQualityByCycle on Spark
    QualityScoreDistribution (Picard)            Chart the distribution of quality scores.  
    QualityScoreDistributionSpark                (BETA Tool) QualityScoreDistribution on Spark
    ValidateSamFile (Picard)                     Validates a SAM or BAM file.
    ViewSam (Picard)                             Prints a SAM or BAM file to the screen

--------------------------------------------------------------------------------------
Intervals Manipulation:                          Tools that process genomic intervals in various formats
    BedToIntervalList (Picard)                   Converts a BED file to a Picard Interval List.  
    CompareIntervalLists                         Compare two interval lists for equality
    IntervalListToBed (Picard)                   Converts an Picard IntervalList file to a BED file.
    IntervalListTools (Picard)                   A tool for performing various IntervalList manipulations
    LiftOverIntervalList (Picard)                Lifts over an interval list from one reference build to another. 
    PreprocessIntervals                          Prepares bins for coverage collection
    SplitIntervals                               Split intervals into sub-interval files.

--------------------------------------------------------------------------------------
Metagenomics:                                    Tools that perform metagenomic analysis, e.g. microbial community composition and pathogen detection
    PathSeqBuildKmers                            Builds set of host reference k-mers
    PathSeqBuildReferenceTaxonomy                Builds a taxonomy datafile of the microbe reference
    PathSeqBwaSpark                              Step 2: Aligns reads to the microbe reference
    PathSeqFilterSpark                           Step 1: Filters low quality, low complexity, duplicate, and host reads
    PathSeqPipelineSpark                         Combined tool that performs all steps: read filtering, microbe reference alignment, and abundance scoring
    PathSeqScoreSpark                            Step 3: Classifies pathogen-aligned reads and generates abundance scores

--------------------------------------------------------------------------------------
Other:                                           Miscellaneous tools, e.g. those that aid in data streaming
    CreateHadoopBamSplittingIndex                (BETA Tool) Create a Hadoop BAM splitting index
    FifoBuffer (Picard)                          Provides a large, FIFO buffer that can be used to buffer input and output streams between programs.
    GatherBQSRReports                            Gathers scattered BQSR recalibration reports into a single file
    GatherTranches                               (BETA Tool) Gathers scattered VQSLOD tranches into a single file
    IndexFeatureFile                             Creates an index for a feature file, e.g. VCF or BED file.
    ParallelCopyGCSDirectoryIntoHDFSSpark        (BETA Tool) Parallel copy a file or directory from Google Cloud Storage into the HDFS file system used by Spark
    PrintBGZFBlockInformation                    (EXPERIMENTAL Tool) Print information about the compressed blocks in a BGZF format file

--------------------------------------------------------------------------------------
Read Data Manipulation:                          Tools that manipulate read data in SAM, BAM or CRAM format
    AddCommentsToBam (Picard)                    Adds comments to the header of a BAM file.
    AddOATag (Picard)                            Record current alignment information to OA tag.
    AddOrReplaceReadGroups (Picard)              Assigns all the reads in a file to a single new read-group.
    AddOriginalAlignmentTags                     (EXPERIMENTAL Tool) Adds Original Alignment tag and original mate contig tag
    ApplyBQSR                                    Apply base quality score recalibration
    ApplyBQSRSpark                               (BETA Tool) Apply base quality score recalibration on Spark
    BQSRPipelineSpark                            (BETA Tool) Both steps of BQSR (BaseRecalibrator and ApplyBQSR) on Spark
    BamToBfq (Picard)                            Converts a BAM file into a BFQ (binary fastq formatted) file
    BaseRecalibrator                             Generates recalibration table for Base Quality Score Recalibration (BQSR)
    BaseRecalibratorSpark                        (BETA Tool) Generate recalibration table for Base Quality Score Recalibration (BQSR) on Spark
    BuildBamIndex (Picard)                       Generates a BAM index ".bai" file.  
    BwaAndMarkDuplicatesPipelineSpark            (BETA Tool) Takes name-sorted file and runs BWA and MarkDuplicates.
    BwaSpark                                     (BETA Tool) Align reads to a given reference using BWA on Spark
    CleanSam (Picard)                            Cleans the provided SAM/BAM, soft-clipping beyond-end-of-reference alignments and setting MAPQ to 0 for unmapped reads
    ClipReads                                    Clip reads in a SAM/BAM/CRAM file
    ConvertHeaderlessHadoopBamShardToBam         (BETA Tool) Convert a headerless BAM shard into a readable BAM
    DownsampleSam (Picard)                       Downsample a SAM or BAM file.
    ExtractOriginalAlignmentRecordsByNameSpark   (BETA Tool) Subsets reads by name
    FastqToSam (Picard)                          Converts a FASTQ file to an unaligned BAM or SAM file
    FilterSamReads (Picard)                      Subsets reads from a SAM or BAM file by applying one of several filters.
    FixMateInformation (Picard)                  Verify mate-pair information between mates and fix if needed.
    FixMisencodedBaseQualityReads                Fix Illumina base quality scores in a SAM/BAM/CRAM file
    GatherBamFiles (Picard)                      Concatenate efficiently BAM files that resulted from a scattered parallel analysis
    LeftAlignIndels                              Left-aligns indels from reads in a SAM/BAM/CRAM file
    MarkDuplicates (Picard)                      Identifies duplicate reads.  
    MarkDuplicatesSpark                          MarkDuplicates on Spark
    MarkDuplicatesWithMateCigar (Picard)         Identifies duplicate reads, accounting for mate CIGAR.  
    MergeBamAlignment (Picard)                   Merge alignment data from a SAM or BAM with data in an unmapped BAM file.  
    MergeSamFiles (Picard)                       Merges multiple SAM and/or BAM files into a single file.  
    PositionBasedDownsampleSam (Picard)          Downsample a SAM or BAM file to retain a subset of the reads based on the reads location in each tile in the flowcell.
    PrintReads                                   Print reads in the SAM/BAM/CRAM file
    PrintReadsSpark                              (BETA Tool) PrintReads on Spark
    ReorderSam (Picard)                          Reorders reads in a SAM or BAM file to match ordering in a second reference file.
    ReplaceSamHeader (Picard)                    Replaces the SAMFileHeader in a SAM or BAM file.  
    RevertBaseQualityScores                      Revert Quality Scores in a SAM/BAM/CRAM file
    RevertOriginalBaseQualitiesAndAddMateCigar (Picard)Reverts the original base qualities and adds the mate cigar tag to read-group BAMs
    RevertSam (Picard)                           Reverts SAM or BAM files to a previous state.  
    RevertSamSpark                               (BETA Tool) Reverts SAM or BAM files to a previous state.
    SamFormatConverter (Picard)                  Convert a BAM file to a SAM file, or a SAM to a BAM
    SamToFastq (Picard)                          Converts a SAM or BAM file to FASTQ.
    SamToFastqWithTags (Picard)                  Converts a SAM or BAM file to FASTQ alongside FASTQs created from tags.
    SetNmAndUqTags (Picard)                      DEPRECATED: Use SetNmMdAndUqTags instead.
    SetNmMdAndUqTags (Picard)                    Fixes the NM, MD, and UQ tags in a SAM file 
    SimpleMarkDuplicatesWithMateCigar (Picard)   (EXPERIMENTAL Tool) Examines aligned records in the supplied SAM or BAM file to locate duplicate molecules.
    SortSam (Picard)                             Sorts a SAM or BAM file
    SortSamSpark                                 (BETA Tool) SortSam on Spark (works on SAM/BAM/CRAM)
    SplitNCigarReads                             Split Reads with N in Cigar
    SplitReads                                   Outputs reads from a SAM/BAM/CRAM by read group, sample and library name
    SplitSamByLibrary (Picard)                   Splits a SAM or BAM file into individual files by library
    SplitSamByNumberOfReads (Picard)             Splits a SAM or BAM file to multiple BAMs.
    UmiAwareMarkDuplicatesWithMateCigar (Picard) (EXPERIMENTAL Tool) Identifies duplicate reads using information from read positions and UMIs. 
    UnmarkDuplicates                             Clears the 0x400 duplicate SAM flag

--------------------------------------------------------------------------------------
Reference:                                       Tools that analyze and manipulate FASTA format references
    BaitDesigner (Picard)                        Designs oligonucleotide baits for hybrid selection reactions.
    BwaMemIndexImageCreator                      Create a BWA-MEM index image file for use with GATK BWA tools
    CountBasesInReference                        Count the numbers of each base in a reference file
    CreateSequenceDictionary (Picard)            Creates a sequence dictionary for a reference sequence.  
    ExtractSequences (Picard)                    Subsets intervals from a reference sequence to a new FASTA file.
    FastaAlternateReferenceMaker                 Create an alternative reference by combining a fasta with a vcf.
    FastaReferenceMaker                          Create snippets of a fasta file
    FindBadGenomicKmersSpark                     (BETA Tool) Identifies sequences that occur at high frequency in a reference
    NonNFastaSize (Picard)                       Counts the number of non-N bases in a fasta file.
    NormalizeFasta (Picard)                      Normalizes lines of sequence in a FASTA file to be of the same length.
    ScatterIntervalsByNs (Picard)                Writes an interval list created by splitting a reference at Ns.

--------------------------------------------------------------------------------------
Short Variant Discovery:                         Tools that perform variant calling and genotyping for short variants (SNPs, SNVs and Indels)
    CombineGVCFs                                 Merges one or more HaplotypeCaller GVCF files into a single GVCF with appropriate annotations
    GenomicsDBImport                             Import VCFs to GenomicsDB
    GenotypeGVCFs                                Perform joint genotyping on one or more samples pre-called with HaplotypeCaller
    HaplotypeCaller                              Call germline SNPs and indels via local re-assembly of haplotypes
    HaplotypeCallerSpark                         (BETA Tool) HaplotypeCaller on Spark
    LearnReadOrientationModel                    Get the maximum likelihood estimates of artifact prior probabilities in the orientation bias mixture model filter
    Mutect2                                      Call somatic SNVs and indels via local assembly of haplotypes
    ReadsPipelineSpark                           (BETA Tool) Takes unaligned or aligned reads and runs BWA (if specified), MarkDuplicates, BQSR, and HaplotypeCaller to generate a VCF file of variants

--------------------------------------------------------------------------------------
Structural Variant Discovery:                    Tools that detect structural variants        
    CpxVariantReInterpreterSpark                 (BETA Tool) (Internal) Tries to extract simple variants from a provided GATK-SV CPX.vcf
    DiscoverVariantsFromContigAlignmentsSAMSpark (BETA Tool) (Internal) Examines aligned contigs from local assemblies and calls structural variants
    ExtractSVEvidenceSpark                       (BETA Tool) (Internal) Extracts evidence of structural variations from reads
    FindBreakpointEvidenceSpark                  (BETA Tool) (Internal) Produces local assemblies of genomic regions that may harbor structural variants
    StructuralVariationDiscoveryPipelineSpark    (BETA Tool) Runs the structural variation discovery workflow on a single sample
    SvDiscoverFromLocalAssemblyContigAlignmentsSpark    (BETA Tool) (Internal) Examines aligned contigs from local assemblies and calls structural variants or their breakpoints

--------------------------------------------------------------------------------------
Variant Evaluation and Refinement:               Tools that evaluate and refine variant calls, e.g. with annotations not offered by the engine
    AnnotatePairOrientation                      (BETA Tool) (EXPERIMENTAL) Annotate a non-M2 VCF (using the associated tumor bam) with pair orientation fields (e.g. F1R2 ).
    AnnotateVcfWithBamDepth                      (Internal) Annotate a vcf with a bam's read depth at each variant locus
    AnnotateVcfWithExpectedAlleleFraction        (Internal) Annotate a vcf with expected allele fractions in pooled sequencing
    CalculateGenotypePosteriors                  Calculate genotype posterior probabilities given family and/or known population genotypes
    CalculateMixingFractions                     (Internal) Calculate proportions of different samples in a pooled bam
    Concordance                                  (BETA Tool) Evaluate concordance of an input VCF against a validated truth VCF
    CountFalsePositives                          (BETA Tool) Count PASS variants
    CountVariants                                Counts variant records in a VCF file, regardless of filter status.
    CountVariantsSpark                           (BETA Tool) CountVariants on Spark
    EvaluateInfoFieldConcordance                 (BETA Tool) Evaluate concordance of info fields in an input VCF against a validated truth VCF
    FilterFuncotations                           (EXPERIMENTAL Tool) Filter variants based on clinically-significant Funcotations.
    FindMendelianViolations (Picard)             Finds mendelian violations of all types within a VCF
    Funcotator                                   Functional Annotator
    FuncotatorDataSourceDownloader               Data source downloader for Funcotator.
    GenotypeConcordance (Picard)                 Calculates the concordance between genotype data of one samples in each of two VCFs - one  being considered the truth (or reference) the other being the call.  The concordance is broken into separate results sections for SNPs and indels.  Statistics are reported in three different files.
    MergeMutect2CallsWithMC3                     (EXPERIMENTAL Tool) UNSUPPORTED.  FOR EVALUATION ONLY. Merge M2 calls with MC
    ValidateBasicSomaticShortMutations           (EXPERIMENTAL Tool) Check the variants in a VCF against a tumor-normal pair of bams representing the same samples, though not the ones from the actual calls.
    ValidateVariants                             Validate VCF
    VariantEval                                  (BETA Tool) General-purpose tool for variant evaluation (% in dbSNP, genotype concordance, Ti/Tv ratios, and a lot more)
    VariantsToTable                              Extract fields from a VCF file to a tab-delimited table

--------------------------------------------------------------------------------------
Variant Filtering:                               Tools that filter variants by annotating the FILTER column
    ApplyVQSR                                     Apply a score cutoff to filter variants based on a recalibration table
    CNNScoreVariants                             Apply a Convolutional Neural Net to filter annotated variants
    CNNVariantTrain                              (EXPERIMENTAL Tool) Train a CNN model for filtering variants
    CNNVariantWriteTensors                       (EXPERIMENTAL Tool) Write variant tensors for training a CNN to filter variants
    CreateSomaticPanelOfNormals                  (BETA Tool) Make a panel of normals for use with Mutect2
    FilterAlignmentArtifacts                     (EXPERIMENTAL Tool) Filter alignment artifacts from a vcf callset.
    FilterByOrientationBias                      (EXPERIMENTAL Tool) Filter Mutect2 somatic variant calls using orientation bias
    FilterMutectCalls                            Filter somatic SNVs and indels called by Mutect2
    FilterVariantTranches                        (EXPERIMENTAL Tool) Apply tranche filtering
    FilterVcf (Picard)                           Hard filters a VCF.
    VariantFiltration                            Filter variant calls based on INFO and/or FORMAT annotations
    VariantRecalibrator                          Build a recalibration model to score variant quality for filtering purposes

--------------------------------------------------------------------------------------
Variant Manipulation:                            Tools that manipulate variant call format (VCF) data
    FixVcfHeader (Picard)                        Replaces or fixes a VCF header.
    GatherVcfs (Picard)                          Gathers multiple VCF files from a scatter operation into a single VCF file
    GatherVcfsCloud                              (BETA Tool) Gathers multiple VCF files from a scatter operation into a single VCF file
    LeftAlignAndTrimVariants                     Left align and trim vairants
    LiftoverVcf (Picard)                         Lifts over a VCF file from one reference build to another.  
    MakeSitesOnlyVcf (Picard)                    Creates a VCF that contains all the site-level information for all records in the input VCF but no genotype information.
    MakeVcfSampleNameMap (Picard)                Creates a TSV from sample name to VCF/GVCF path, with one line per input.
    MergeVcfs (Picard)                           Combines multiple variant files into a single variant file
    PrintVariantsSpark                           (BETA Tool) Prints out variants from the input VCF.
    RemoveNearbyIndels                           (Internal) Remove indels from the VCF file that are close to each other.
    RenameSampleInVcf (Picard)                   Renames a sample within a VCF or BCF.
    SelectVariants                               Select a subset of variants from a VCF file
    SortVcf (Picard)                             Sorts one or more VCF files.  
    SplitVcfs (Picard)                           Splits SNPs and INDELs into separate files.  
    UpdateVCFSequenceDictionary                  Updates the sequence dictionary in a variant file.
    UpdateVcfSequenceDictionary (Picard)         Takes a VCF and a second file that contains a sequence dictionary and updates the VCF with the new sequence dictionary.
    VariantAnnotator                             (BETA Tool) Tool for adding annotations to VCF files
    VcfFormatConverter (Picard)                  Converts VCF to BCF or BCF to VCF.  
    VcfToIntervalList (Picard)                   Converts a VCF or BCF file to a Picard Interval List

--------------------------------------------------------------------------------------
```




### BaseRecalibrator parameter
```

$ gatk BaseRecalibrator
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar BaseRecalibrator
USAGE: BaseRecalibrator [arguments]

First pass of the Base Quality Score Recalibration (BQSR) -- Generates recalibration table based on various
user-specified covariates (such as read group, reported quality score, machine cycle, and nucleotide context).
Version:4.1.0.0


Required Arguments:

--input,-I:String             BAM/SAM/CRAM file containing reads  This argument must be specified at least once.
                              Required. 

--known-sites:FeatureInput    One or more databases of known polymorphic sites used to exclude regions around known
                              polymorphisms from analysis.  This argument must be specified at least once. Required. 

--output,-O:File              The output recalibration table file to create  Required. 

--reference,-R:String         Reference sequence file  Required. 


Optional Arguments:

--add-output-sam-program-record,-add-output-sam-program-record:Boolean
                              If true, adds a PG tag to created SAM/BAM/CRAM files.  Default value: true. Possible
                              values: {true, false} 

--add-output-vcf-command-line,-add-output-vcf-command-line:Boolean
                              If true, adds a command line header line to created VCF files.  Default value: true.
                              Possible values: {true, false} 

--arguments_file:File         read one or more arguments files and add them to the command line  This argument may be
                              specified 0 or more times. Default value: null. 

--binary-tag-name:String      the binary tag covariate name if using it  Default value: null. 

--bqsr-baq-gap-open-penalty:Double
                              BQSR BAQ gap open penalty (Phred Scaled).  Default value is 40.  30 is perhaps better for
                              whole genome call sets  Default value: 40.0. 

--cloud-index-prefetch-buffer,-CIPB:Integer
                              Size of the cloud-only prefetch buffer (in MB; 0 to disable). Defaults to
                              cloudPrefetchBuffer if unset.  Default value: -1. 

--cloud-prefetch-buffer,-CPB:Integer
                              Size of the cloud-only prefetch buffer (in MB; 0 to disable).  Default value: 40. 

--create-output-bam-index,-OBI:Boolean
                              If true, create a BAM/CRAM index when writing a coordinate-sorted BAM/CRAM file.  Default
                              value: true. Possible values: {true, false} 

--create-output-bam-md5,-OBM:Boolean
                              If true, create a MD5 digest for any BAM/SAM/CRAM file created  Default value: false.
                              Possible values: {true, false} 

--create-output-variant-index,-OVI:Boolean
                              If true, create a VCF index when writing a coordinate-sorted VCF file.  Default value:
                              true. Possible values: {true, false} 

--create-output-variant-md5,-OVM:Boolean
                              If true, create a a MD5 digest any VCF file created.  Default value: false. Possible
                              values: {true, false} 

--default-base-qualities:Byte Assign a default base quality  Default value: -1. 

--deletions-default-quality:Byte
                              default quality for the base deletions covariate  Default value: 45. 

--disable-bam-index-caching,-DBIC:Boolean
                              If true, don't cache bam indexes, this will reduce memory requirements but may harm
                              performance if many intervals are specified.  Caching is automatically disabled if there
                              are no intervals specified.  Default value: false. Possible values: {true, false} 

--disable-read-filter,-DF:String
                              Read filters to be disabled before analysis  This argument may be specified 0 or more
                              times. Default value: null. Possible Values: {MappedReadFilter,
                              MappingQualityAvailableReadFilter, MappingQualityNotZeroReadFilter,
                              NotDuplicateReadFilter, NotSecondaryAlignmentReadFilter,
                              PassesVendorQualityCheckReadFilter, WellformedReadFilter}

--disable-sequence-dictionary-validation,-disable-sequence-dictionary-validation:Boolean
                              If specified, do not check the sequence dictionaries from our inputs for compatibility.
                              Use at your own risk!  Default value: false. Possible values: {true, false} 

--exclude-intervals,-XL:StringOne or more genomic intervals to exclude from processing  This argument may be specified 0
                              or more times. Default value: null. 

--gatk-config-file:String     A configuration file to use with the GATK.  Default value: null. 

--gcs-max-retries,-gcs-retries:Integer
                              If the GCS bucket channel errors out, how many times it will attempt to re-initiate the
                              connection  Default value: 20. 

--gcs-project-for-requester-pays:String
                              Project to bill when accessing "requester pays" buckets. If unset, these buckets cannot be
                              accessed.  Default value: . 

--help,-h:Boolean             display the help message  Default value: false. Possible values: {true, false} 

--indels-context-size,-ics:Integer
                              Size of the k-mer context to be used for base insertions and deletions  Default value: 3. 

--insertions-default-quality:Byte
                              default quality for the base insertions covariate  Default value: 45. 

--interval-exclusion-padding,-ixp:Integer
                              Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. 

--interval-merging-rule,-imr:IntervalMergingRule
                              Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL,
                              OVERLAPPING_ONLY} 

--interval-padding,-ip:IntegerAmount of padding (in bp) to add to each interval you are including.  Default value: 0. 

--interval-set-rule,-isr:IntervalSetRule
                              Set merging approach to use for combining interval inputs  Default value: UNION. Possible
                              values: {UNION, INTERSECTION} 

--intervals,-L:String         One or more genomic intervals over which to operate  This argument may be specified 0 or
                              more times. Default value: null. 

--lenient,-LE:Boolean         Lenient processing of VCF files  Default value: false. Possible values: {true, false} 

--low-quality-tail:Byte       minimum quality for the bases in the tail of the reads to be considered  Default value: 2.

--maximum-cycle-value,-max-cycle:Integer
                              The maximum cycle value permitted for the Cycle covariate  Default value: 500. 

--mismatches-context-size,-mcs:Integer
                              Size of the k-mer context to be used for base mismatches  Default value: 2. 

--mismatches-default-quality:Byte
                              default quality for the base mismatches covariate  Default value: -1. 

--preserve-qscores-less-than:Integer
                              Don't recalibrate bases with quality scores less than this threshold (with -bqsr)  Default
                              value: 6. 

--quantizing-levels:Integer   number of distinct quality scores in the quantized output  Default value: 16. 

--QUIET:Boolean               Whether to suppress job-summary info on System.err.  Default value: false. Possible
                              values: {true, false} 

--read-filter,-RF:String      Read filters to be applied before analysis  This argument may be specified 0 or more
                              times. Default value: null. Possible Values: {AlignmentAgreesWithHeaderReadFilter,
                              AllowAllReadsReadFilter, AmbiguousBaseReadFilter, CigarContainsNoNOperator,
                              FirstOfPairReadFilter, FragmentLengthReadFilter, GoodCigarReadFilter,
                              HasReadGroupReadFilter, LibraryReadFilter, MappedReadFilter,
                              MappingQualityAvailableReadFilter, MappingQualityNotZeroReadFilter,
                              MappingQualityReadFilter, MatchingBasesAndQualsReadFilter, MateDifferentStrandReadFilter,
                              MateOnSameContigOrNoMappedMateReadFilter, MetricsReadFilter,
                              NonChimericOriginalAlignmentReadFilter, NonZeroFragmentLengthReadFilter,
                              NonZeroReferenceLengthAlignmentReadFilter, NotDuplicateReadFilter,
                              NotOpticalDuplicateReadFilter, NotSecondaryAlignmentReadFilter,
                              NotSupplementaryAlignmentReadFilter, OverclippedReadFilter, PairedReadFilter,
                              PassesVendorQualityCheckReadFilter, PlatformReadFilter, PlatformUnitReadFilter,
                              PrimaryLineReadFilter, ProperlyPairedReadFilter, ReadGroupBlackListReadFilter,
                              ReadGroupReadFilter, ReadLengthEqualsCigarLengthReadFilter, ReadLengthReadFilter,
                              ReadNameReadFilter, ReadStrandFilter, SampleReadFilter, SecondOfPairReadFilter,
                              SeqIsStoredReadFilter, ValidAlignmentEndReadFilter, ValidAlignmentStartReadFilter,
                              WellformedReadFilter}

--read-index,-read-index:String
                              Indices to use for the read inputs. If specified, an index must be provided for every read
                              input and in the same order as the read inputs. If this argument is not specified, the
                              path to the index for each input will be inferred automatically.  This argument may be
                              specified 0 or more times. Default value: null. 

--read-validation-stringency,-VS:ValidationStringency
                              Validation stringency for all SAM/BAM/CRAM/SRA files read by this program.  The default
                              stringency value SILENT can improve performance when processing a BAM file in which
                              variable-length data (read, qualities, tags) do not otherwise need to be decoded.  Default
                              value: SILENT. Possible values: {STRICT, LENIENT, SILENT} 

--seconds-between-progress-updates,-seconds-between-progress-updates:Double
                              Output traversal statistics every time this many seconds elapse  Default value: 10.0. 

--sequence-dictionary,-sequence-dictionary:String
                              Use the given sequence dictionary as the master/canonical sequence dictionary.  Must be a
                              .dict file.  Default value: null. 

--sites-only-vcf-output:Boolean
                              If true, don't emit genotype fields when writing vcf file output.  Default value: false.
                              Possible values: {true, false} 

--tmp-dir:String              Temp directory to use.  Default value: null. 

--use-jdk-deflater,-jdk-deflater:Boolean
                              Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false.
                              Possible values: {true, false} 

--use-jdk-inflater,-jdk-inflater:Boolean
                              Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false.
                              Possible values: {true, false} 

--use-original-qualities,-OQ:Boolean
                              Use the base quality scores from the OQ tag  Default value: false. Possible values: {true,
                              false} 

--verbosity,-verbosity:LogLevel
                              Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING,
                              INFO, DEBUG} 

--version:Boolean             display the version number for this tool  Default value: false. Possible values: {true,
                              false} 


Advanced Arguments:

--disable-tool-default-read-filters,-disable-tool-default-read-filters:Boolean
                              Disable all tool default read filters (WARNING: many tools will not function correctly
                              without their default read filters on)  Default value: false. Possible values: {true,
                              false} 

--showHidden,-showHidden:Boolean
                              display hidden arguments  Default value: false. Possible values: {true, false} 


***********************************************************************

A USER ERROR has occurred: Argument known-sites was missing: Argument 'known-sites' is required.

***********************************************************************
Set the system property GATK_STACKTRACE_ON_USER_EXCEPTION (--java-options '-DGATK_STACKTRACE_ON_USER_EXCEPTION=true') to print the stack trace.

```



### idx error
```
$ gatk BaseRecalibrator --reference  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --input /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_realigned.bam --known-sites  /home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf --known-sites  /home/wuzhikun/database/GATK/hg38/Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf --output  /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recal_data.txt
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar BaseRecalibrator --reference /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --input /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_realigned.bam --known-sites /home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf --known-sites /home/wuzhikun/database/GATK/hg38/Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf --output /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recal_data.txt
15:37:36.548 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar!/com/intel/gkl/native/libgkl_compression.so
15:37:38.947 INFO  BaseRecalibrator - ------------------------------------------------------------
15:37:38.948 INFO  BaseRecalibrator - The Genome Analysis Toolkit (GATK) v4.1.0.0
15:37:38.948 INFO  BaseRecalibrator - For support and documentation go to https://software.broadinstitute.org/gatk/
15:37:38.948 INFO  BaseRecalibrator - Executing as wuzhikun@cu27 on Linux v3.10.0-327.el7.x86_64 amd64
15:37:38.949 INFO  BaseRecalibrator - Java runtime: OpenJDK 64-Bit Server VM v1.8.0_192-b01
15:37:38.949 INFO  BaseRecalibrator - Start Date/Time: March 23, 2019 3:37:36 PM CST
15:37:38.949 INFO  BaseRecalibrator - ------------------------------------------------------------
15:37:38.949 INFO  BaseRecalibrator - ------------------------------------------------------------
15:37:38.951 INFO  BaseRecalibrator - HTSJDK Version: 2.18.2
15:37:38.951 INFO  BaseRecalibrator - Picard Version: 2.18.25
15:37:38.951 INFO  BaseRecalibrator - HTSJDK Defaults.COMPRESSION_LEVEL : 2
15:37:38.951 INFO  BaseRecalibrator - HTSJDK Defaults.USE_ASYNC_IO_READ_FOR_SAMTOOLS : false
15:37:38.951 INFO  BaseRecalibrator - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_SAMTOOLS : true
15:37:38.951 INFO  BaseRecalibrator - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_TRIBBLE : false
15:37:38.952 INFO  BaseRecalibrator - Deflater: IntelDeflater
15:37:38.952 INFO  BaseRecalibrator - Inflater: IntelInflater
15:37:38.952 INFO  BaseRecalibrator - GCS max retries/reopens: 20
15:37:38.952 INFO  BaseRecalibrator - Requester pays: disabled
15:37:38.952 INFO  BaseRecalibrator - Initializing engine
15:37:39.575 INFO  FeatureManager - Using codec VCFCodec to read file file:///home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf
15:37:39.895 INFO  BaseRecalibrator - Shutting down engine
[March 23, 2019 3:37:39 PM CST] org.broadinstitute.hellbender.tools.walkers.bqsr.BaseRecalibrator done. Elapsed time: 0.06 minutes.
Runtime.totalMemory()=2165309440
htsjdk.tribble.TribbleException$CorruptedIndexFile: Index file is corrupted, for input source: /home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf.idx
    at htsjdk.tribble.index.IndexFactory.loadIndex(IndexFactory.java:200)
    at htsjdk.tribble.index.IndexFactory.loadIndex(IndexFactory.java:178)

```

```
$ rm dbsnp_146.hg38_dechr-1.vcf.idx Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf.idx
```


```
$ gatk BaseRecalibrator --reference  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --input /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_realigned.bam --known-sites  /home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf --known-sites  /home/wuzhikun/database/GATK/hg38/Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf --output  /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recal_data.txt
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar BaseRecalibrator --reference /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --input /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_realigned.bam --known-sites /home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf --known-sites /home/wuzhikun/database/GATK/hg38/Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf --output /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recal_data.txt
15:46:48.916 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.0.0-0/gatk-package-4.1.0.0-local.jar!/com/intel/gkl/native/libgkl_compression.so
15:46:50.607 INFO  BaseRecalibrator - ------------------------------------------------------------
15:46:50.608 INFO  BaseRecalibrator - The Genome Analysis Toolkit (GATK) v4.1.0.0
15:46:50.608 INFO  BaseRecalibrator - For support and documentation go to https://software.broadinstitute.org/gatk/
15:46:50.608 INFO  BaseRecalibrator - Executing as wuzhikun@cu27 on Linux v3.10.0-327.el7.x86_64 amd64
15:46:50.608 INFO  BaseRecalibrator - Java runtime: OpenJDK 64-Bit Server VM v1.8.0_192-b01
15:46:50.609 INFO  BaseRecalibrator - Start Date/Time: March 23, 2019 3:46:48 PM CST
15:46:50.609 INFO  BaseRecalibrator - ------------------------------------------------------------
15:46:50.609 INFO  BaseRecalibrator - ------------------------------------------------------------
15:46:50.610 INFO  BaseRecalibrator - HTSJDK Version: 2.18.2
15:46:50.610 INFO  BaseRecalibrator - Picard Version: 2.18.25
15:46:50.610 INFO  BaseRecalibrator - HTSJDK Defaults.COMPRESSION_LEVEL : 2
15:46:50.610 INFO  BaseRecalibrator - HTSJDK Defaults.USE_ASYNC_IO_READ_FOR_SAMTOOLS : false
15:46:50.610 INFO  BaseRecalibrator - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_SAMTOOLS : true
15:46:50.611 INFO  BaseRecalibrator - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_TRIBBLE : false
15:46:50.611 INFO  BaseRecalibrator - Deflater: IntelDeflater
15:46:50.611 INFO  BaseRecalibrator - Inflater: IntelInflater
15:46:50.611 INFO  BaseRecalibrator - GCS max retries/reopens: 20
15:46:50.611 INFO  BaseRecalibrator - Requester pays: disabled
15:46:50.611 INFO  BaseRecalibrator - Initializing engine
15:46:51.070 INFO  FeatureManager - Using codec VCFCodec to read file file:///home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf
15:46:51.088 INFO  FeatureManager - Using codec VCFCodec to read file file:///home/wuzhikun/database/GATK/hg38/Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf
15:46:51.150 INFO  BaseRecalibrator - Done initializing engine
15:46:51.262 INFO  BaseRecalibrationEngine - The covariates being used here: 
15:46:51.262 INFO  BaseRecalibrationEngine -    ReadGroupCovariate
15:46:51.262 INFO  BaseRecalibrationEngine -    QualityScoreCovariate
15:46:51.262 INFO  BaseRecalibrationEngine -    ContextCovariate
15:46:51.262 INFO  BaseRecalibrationEngine -    CycleCovariate
15:46:51.278 INFO  ProgressMeter - Starting traversal
15:46:51.279 INFO  ProgressMeter -        Current Locus  Elapsed Minutes       Reads Processed     Reads/Minute
15:46:51.334 INFO  BaseRecalibrator - Shutting down engine
[March 23, 2019 3:46:51 PM CST] org.broadinstitute.hellbender.tools.walkers.bqsr.BaseRecalibrator done. Elapsed time: 0.04 minutes.
Runtime.totalMemory()=2196242432
***********************************************************************

A USER ERROR has occurred: Input /home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf must support random access to enable queries by interval. If it's a file, please index it using the bundled tool IndexFeatureFile

***********************************************************************
Set the system property GATK_STACKTRACE_ON_USER_EXCEPTION (--java-options '-DGATK_STACKTRACE_ON_USER_EXCEPTION=true') to print the stack trace.
```

### Error resolution
```
$ gatk IndexFeatureFile -F dbsnp_146.hg38_dechr-1.vcf
$ gatk IndexFeatureFile  -F Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf

```


```
$ gatk BaseRecalibrator --reference  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --input /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_realigned.bam --known-sites  /home/wuzhikun/database/GATK/hg38/dbsnp_146.hg38_dechr-1.vcf --known-sites  /home/wuzhikun/database/GATK/hg38/Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf --output  /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recal_data.txt

16:07:33.042 INFO  ProgressMeter -      GL000216.2:1965              1.8                158795          87558.7
16:07:33.042 INFO  ProgressMeter - Traversal complete. Processed 158795 total reads in 1.8 minutes.
16:07:33.130 INFO  BaseRecalibrator - Calculating quantized quality scores...
16:07:33.144 INFO  BaseRecalibrator - Writing recalibration report...
16:07:35.216 INFO  BaseRecalibrator - ...done!
16:07:35.217 INFO  BaseRecalibrator - Shutting down engine
[March 23, 2019 4:07:35 PM CST] org.broadinstitute.hellbender.tools.walkers.bqsr.BaseRecalibrator done. Elapsed time: 1.92 minutes.
Runtime.totalMemory()=5274337280
Tool returned:
158795

```



#### AnalyzeCovariates

```

java -jar /home/wuzhikun/anaconda3/envs/WGS/bin/GenomeAnalysisTK.jar -T AnalyzeCovariates -L 1 -R /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -before /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recal_data.txt -after /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recal_post_data.txt -U ALLOW_SEQ_DICT_INCOMPATIBILITY -plots /home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recalibration_plots.pdf >/home/wuzhikun/Project/Illumina_Trio/log/R19001827.AnalyzeCovariates.log


INFO  17:32:57,126 AnalyzeCovariates - Generating plots file '/home/wuzhikun/Project/Illumina_Trio/mapping/R19001827/R19001827_recalibration_plots.pdf' 
##### ERROR --
##### ERROR stack trace 
org.broadinstitute.gatk.utils.R.RScriptExecutorException: RScript exited with 1. Run with -l DEBUG for more info.
        at org.broadinstitute.gatk.utils.R.RScriptExecutor.exec(RScriptExecutor.java:176)
        at org.broadinstitute.gatk.engine.recalibration.RecalUtils.generatePlots(RecalUtils.java:555)
        at org.broadinstitute.gatk.tools.walkers.bqsr.AnalyzeCovariates.generatePlots(AnalyzeCovariates.java:373)
        at org.broadinstitute.gatk.tools.walkers.bqsr.AnalyzeCovariates.initialize(AnalyzeCovariates.java:387)
        at org.broadinstitute.gatk.engine.executive.LinearMicroScheduler.execute(LinearMicroScheduler.java:83)
        at org.broadinstitute.gatk.engine.GenomeAnalysisEngine.execute(GenomeAnalysisEngine.java:323)
        at org.broadinstitute.gatk.engine.CommandLineExecutable.execute(CommandLineExecutable.java:123)
        at org.broadinstitute.gatk.utils.commandline.CommandLineProgram.start(CommandLineProgram.java:256)
        at org.broadinstitute.gatk.utils.commandline.CommandLineProgram.start(CommandLineProgram.java:158)
        at org.broadinstitute.gatk.engine.CommandLineGATK.main(CommandLineGATK.java:108)
##### ERROR ------------------------------------------------------------------------------------------
##### ERROR A GATK RUNTIME ERROR has occurred (version 3.8-1-0-gf15c1c3ef):
##### ERROR
##### ERROR This might be a bug. Please check the documentation guide to see if this is a known problem.
##### ERROR If not, please post the error message, with stack trace, to the GATK forum.
##### ERROR Visit our website and forum for extensive documentation and answers to 
##### ERROR commonly asked questions https://software.broadinstitute.org/gatk
##### ERROR
##### ERROR MESSAGE: RScript exited with 1. Run with -l DEBUG for more info.
##### ERROR ------------------------------------------------------------------------------------------

```

According to the GATK website the required R dependencies are:
```
gplots
ggplot2
gsalib
reshape
```

```
conda install -c conda-forge r-gplots
conda install -c r r-ggplot2
conda install -c bioconda r-gsalib
conda install -c r r-reshape
```


### BaseRecalibrator
```
# Analyze patterns of covariation in the sequence dataset
java -Xmx16g -jar $gatk -T BaseRecalibrator -R $reference \ 
       -I $file  -knownSites $dbsnp -o ${file%%.*}_recal_data.table
# Do a second pass to analyze covariation remaining after recalibration
java -Xmx16g -jar $gatk -T BaseRecalibrator -R $reference  \
    -I $file  -knownSites $dbsnp -BQSR ${file%%.*}_recal_data.table \
   -o ${file%%.*}_post_recal_data.table    
#  Generate before/after plots, need configure your R environment
java -Xmx16g -jar $gatk -T AnalyzeCovariates \
    -R $reference  -before ${file%%.*}_recal_data.table \
    -after ${file%%.*}_post_recal_data.table \
    -plots ${file%%.*}_recalibration_plots.pdf
# Apply the recalibration to your sequence data
java -Xmx16g -jar $gatk -T PrintReads \
    -R $reference -I $file \
    -BQSR ${file%%.*}_recal_data.table \
    -o ${file%%.*}_recal_reads.bam
```

### BaseRecalibrator

```
java –jar GenomeAnalysisTK.jar –T BaseRecalibrator \
–R human.fasta \
–I realigned.bam \
–knownSites dbsnp137.vcf \
–knownSites gold.standard.indels.vcf \
–o recal.table
```



#### Base Recalibrator
```
java –jar GenomeAnalysisTK.jar –T BaseRecalibrator \
–R human.fasta \
–I realigned.bam \
–knownSites dbsnp137.vcf \
–knownSites gold.standard.indels.vcf \
–BQSR recal.table \
–o aSer_recal.table
```


#### AnalyzeCovariates
```
java –jar GenomeAnalysisTK.jar –T AnalyzeCovariates \
–R human.fasta \
–before recal.table \
–aSer aSer_recal.table \
–plots recal_plots.pdf
```



### View realigned reads and assembled haplotypes

But we’re not satisfied with “probably” here. Let’s take a peek under the hood of HaplotypeCaller. You find that HaplotypeCaller has a parameter called -bamout, which allows you to ask for the realigned version of the bam. That realigned version is what HaplotypeCaller uses to make its variant calls, so you will be able to see if a realignment fixed the messy region in the original bam.

You decide to run the following command:

```
java -jar GenomeAnalysisTK.jar -T HaplotypeCaller \
    -R ref/human_g1k_b37_20.fasta \
    -I bams/exp_design/NA12878_wgs_20.bam \
    -o sandbox/NA12878_wgs_20_HC_calls_debug.vcf \
    -bamout sandbox/NA12878_wgs_20.HC_out.bam \
    -forceActive -disableOptimizations \
    -L 20:10,002,371-10,002,546 -ip 100
```
Since you are only interested in looking at that messy region, you decide to give the tool a narrowed interval with -L 20:10,002,371-10,002,546, with a 100 bp padding on either side using -ip 100. To make sure the tool does perform the reassembly in that region, you add in the -forceActive and -disableOptimizations arguments.




### HaplotypeCaller
Call germline SNPs and indels via local re-assembly of haplotypes


Single-sample GVCF calling on DNAseq (for `-ERC GVCF` cohort analysis workflow)
```
   java -jar GenomeAnalysisTK.jar \
     -R reference.fasta \
     -T HaplotypeCaller \
     -I sample1.bam \
     --emitRefConfidence GVCF \
     [--dbsnp dbSNP.vcf] \
     [-L targets.interval_list] \
     -o output.raw.snps.indels.g.vcf
```


Single-sample GVCF calling on DNAseq with allele-specific annotations (for allele-specific cohort analysis workflow)
```
   java -jar GenomeAnalysisTK.jar \
     -R reference.fasta \
     -T HaplotypeCaller \
     -I sample1.bam \
     --emitRefConfidence GVCF \
     [--dbsnp dbSNP.vcf] \
     [-L targets.interval_list] \
     -G Standard -G AS_Standard \
     -o output.raw.snps.indels.AS.g.vcf
```


Variant-only calling on DNAseq
```
   java -jar GenomeAnalysisTK.jar \
     -R reference.fasta \
     -T HaplotypeCaller \
     -I sample1.bam [-I sample2.bam ...] \
     [--dbsnp dbSNP.vcf] \
     [-stand_call_conf 30] \
     [-L targets.interval_list] \
     -o output.raw.snps.indels.vcf

```


Variant-only calling on RNAseq
```
   java -jar GenomeAnalysisTK.jar \
     -R reference.fasta \
     -T HaplotypeCaller \
     -I sample1.bam \
     [--dbsnp dbSNP.vcf] \
     -stand_call_conf 20 \
     -o output.raw.snps.indels.vcf
```


### GenotypeGVCFs
Perform joint genotyping on gVCF files produced by HaplotypeCaller
```
 java -jar GenomeAnalysisTK.jar \
   -T GenotypeGVCFs \
   -R reference.fasta \
   --variant sample1.g.vcf \
   --variant sample2.g.vcf \
   -o output.vcf
 	
```



on exoms
```
-T GenotypeGVCFs -R /projects/resources/Homo_sapiens_assembly19.fasta --variant /projects/combinedgvcfs/combined_gvcfs.list --dbsnp /projects/resources/gatk_bundle/dbsnp_138.b37.vcf -o /04_15_2016/genotype_gvcfs/04_15_2016_raw.vcf -log /04_15_2016/genotype_gvcfs/04_15_2016_raw.log -L /projects/resources/bed.and.interval.files/b37_refseqplus50_clean.bed -nt 16 --max_alternate_alleles 6

```



### https://gatkforums.broadinstitute.org/gatk/discussion/11455/realignertargetcreator-and-indelrealigner

The indel realignment tools have been retired from the best practices; they are unnecessary if you are using an assembly based caller like Mutect2 or HaplotypeCaller. Someone has proposed a port of those tools but we have not yet fully evaluated it.

PrintReads -BQSR has been replaced by another tool called ApplyBQSR.


es the indel realignment step can simply be skipped.

For BQSR, no, the new tool just replaces PrintReads for that particular use case. The other two tools still exist; BaseRecalibrator is no longer able to do on the fly recalibration, so you have to run it on the recalibrated bam to do the QC cycle, and AnalyzeCovariates is used the same way as before except the argument is now lowercased (-bqsr).



#### GATK ERROR
```

##### ERROR   known contigs = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 20, 21, 22, 2, 3, 4, 5, 6, KI270728.1, KI270727.1, KI270442.1, KI270729.1, GL000225.1, KI270743.1, GL000008.2, GL000009.2, KI270747.1, KI270722.1, GL000194.1, KI270742.1, GL000205.2, GL000195.1, KI270736.1, KI270733.1, GL000224.1, GL000219.1, KI270719.1, GL000216.2, KI270712.1, KI270706.1, KI270725.1, KI270744.1, KI270734.1, GL000213.1, GL000220.1, KI270715.1, GL000218.1, KI270749.1, KI270741.1, GL000221.1, KI270716.1, KI270731.1, KI270751.1, KI270750.1, KI270519.1, GL000214.1, KI270708.1, KI270730.1, KI270438.1, KI270737.1, KI270721.1, KI270738.1, KI270748.1, KI270435.1, GL000208.1, KI270538.1, KI270756.1, KI270739.1, KI270757.1, KI270709.1, KI270746.1, KI270753.1, KI270589.1, KI270726.1, KI270735.1, KI270711.1, KI270745.1, KI270714.1, KI270732.1, KI270713.1, KI270754.1, KI270710.1, KI270717.1, KI270724.1, KI270720.1, KI270723.1, KI270718.1, KI270317.1, KI270740.1, KI270755.1, KI270707.1, KI270579.1, KI270752.1, KI270512.1, KI270322.1, GL000226.1, KI270311.1, KI270366.1, KI270511.1, KI270448.1, KI270521.1, KI270581.1, KI270582.1, KI270515.1, KI270588.1, KI270591.1, KI270522.1, KI270507.1, KI270590.1, KI270584.1, KI270320.1, KI270382.1, KI270468.1, KI270467.1, KI270362.1, KI270517.1, KI270593.1, KI270528.1, KI270587.1, KI270364.1, KI270371.1, KI270333.1, KI270374.1, KI270411.1, KI270414.1, KI270510.1, KI270390.1, KI270375.1, KI270420.1, KI270509.1, KI270315.1, KI270302.1, KI270518.1, KI270530.1, KI270304.1, KI270418.1, KI270424.1, KI270417.1, KI270508.1, KI270303.1, KI270381.1, KI270529.1, KI270425.1, KI270396.1, KI270363.1, KI270386.1, KI270465.1, KI270383.1, KI270384.1, KI270330.1, KI270372.1, KI270548.1, KI270580.1, KI270387.1, KI270391.1, KI270305.1, KI270373.1, KI270422.1, KI270316.1, KI270340.1, KI270338.1, KI270583.1, KI270334.1, KI270429.1, KI270393.1, KI270516.1, KI270389.1, KI270466.1, KI270388.1, KI270544.1, KI270310.1, KI270412.1, KI270395.1, KI270376.1, KI270337.1, KI270335.1, KI270378.1, KI270379.1, KI27032
9.1, KI270419.1, KI270336.1, KI270312.1, KI270539.1, KI270385.1, KI270423.1, KI270392.1, KI270394.1, 7, 8, 9, MT, X, Y]
##### ERROR   reference contigs = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 3, 4, 5, 6, 7, 8, 9, MT, X, Y, KI270728.1, KI270727.1, KI270442
.1, KI270729.1, GL000225.1, KI270743.1, GL000008.2, GL000009.2, KI270747.1, KI270722.1, GL000194.1, KI270742.1, GL000205.2, GL000195.1, KI270736.1, KI270733
.1, GL000224.1, GL000219.1, KI270719.1, GL000216.2, KI270712.1, KI270706.1, KI270725.1, KI270744.1, KI270734.1, GL000213.1, GL000220.1, KI270715.1, GL000218
.1, KI270749.1, KI270741.1, GL000221.1, KI270716.1, KI270731.1, KI270751.1, KI270750.1, KI270519.1, GL000214.1, KI270708.1, KI270730.1, KI270438.1, KI270737
.1, KI270721.1, KI270738.1, KI270748.1, KI270435.1, GL000208.1, KI270538.1, KI270756.1, KI270739.1, KI270757.1, KI270709.1, KI270746.1, KI270753.1, KI270589
.1, KI270726.1, KI270735.1, KI270711.1, KI270745.1, KI270714.1, KI270732.1, KI270713.1, KI270754.1, KI270710.1, KI270717.1, KI270724.1, KI270720.1, KI270723
.1, KI270718.1, KI270317.1, KI270740.1, KI270755.1, KI270707.1, KI270579.1, KI270752.1, KI270512.1, KI270322.1, GL000226.1, KI270311.1, KI270366.1, KI270511
.1, KI270448.1, KI270521.1, KI270581.1, KI270582.1, KI270515.1, KI270588.1, KI270591.1, KI270522.1, KI270507.1, KI270590.1, KI270584.1, KI270320.1, KI270382
.1, KI270468.1, KI270467.1, KI270362.1, KI270517.1, KI270593.1, KI270528.1, KI270587.1, KI270364.1, KI270371.1, KI270333.1, KI270374.1, KI270411.1, KI270414
.1, KI270510.1, KI270390.1, KI270375.1, KI270420.1, KI270509.1, KI270315.1, KI270302.1, KI270518.1, KI270530.1, KI270304.1, KI270418.1, KI270424.1, KI270417
.1, KI270508.1, KI270303.1, KI270381.1, KI270529.1, KI270425.1, KI270396.1, KI270363.1, KI270386.1, KI270465.1, KI270383.1, KI270384.1, KI270330.1, KI270372
.1, KI270548.1, KI270580.1, KI270387.1, KI270391.1, KI270305.1, KI270373.1, KI270422.1, KI270316.1, KI270340.1, KI270338.1, KI270583.1, KI270334.1, KI270429
.1, KI270393.1, KI270516.1, KI270389.1, KI270466.1, KI270388.1, KI270544.1, KI270310.1, KI270412.1, KI270395.1, KI270376.1, KI270337.1, KI270335.1, KI270378
.1, KI270379.1, KI270329.1, KI270419.1, KI270336.1, KI270312.1, KI270539.1, KI270385.1, KI270423.1, KI270392.1, KI270394.1]


```


##### reference
```
grep '^>' /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa | cut -f 1 -d ' ' | sed 's/^>//g' | less

1
10
11
12
13
14
15
16
17
18
19
2
20
21
22
3
4
5
6
7
8
9
MT
X
Y
KI270728.1
KI270727.1
KI270442.1
KI270729.1
GL000225.1
KI270743.1
GL000008.2
GL000009.2
KI270747.1

```


### gold standard indels
```
$ cut -f 1  Mills_and_1000G_gold_standard.indels.hg38_dechr.vcf | grep -v '#' |  uniq | less

1
10
11
12
13
14
15
16
17
18
19
2
20
21
22
3
4
5
6
7
8
9
X
Y


```



##### bam files
```
$ samtools view R19001827_sorted.bam |cut -f 3 | uniq | less
1
10
11
12
13
14
15
16
17
18
19
2
20
21
22
3
4
5
6
7
8
9
MT
X
Y
KI270728.1
KI270727.1
KI270442.1
KI270729.1
GL000225.1
KI270743.1
GL000008.2
GL000009.2
KI270747.1
```


#### something wrong with the annotation of vcf file for gold standard indels:

```
##contig=<ID=chr1,length=248956422,assembly=20>
##contig=<ID=chr2,length=242193529,assembly=20>
##contig=<ID=chr3,length=198295559,assembly=20>
##contig=<ID=chr4,length=190214555,assembly=20>
##contig=<ID=chr5,length=181538259,assembly=20>
##contig=<ID=chr6,length=170805979,assembly=20>
##contig=<ID=chr7,length=159345973,assembly=20>
##contig=<ID=chr8,length=145138636,assembly=20>
##contig=<ID=chr9,length=138394717,assembly=20>
##contig=<ID=chr10,length=133797422,assembly=20>
##contig=<ID=chr11,length=135086622,assembly=20>
##contig=<ID=chr12,length=133275309,assembly=20>
##contig=<ID=chr13,length=114364328,assembly=20>
##contig=<ID=chr14,length=107043718,assembly=20>
##contig=<ID=chr15,length=101991189,assembly=20>
##contig=<ID=chr16,length=90338345,assembly=20>
##contig=<ID=chr17,length=83257441,assembly=20>
##contig=<ID=chr18,length=80373285,assembly=20>
##contig=<ID=chr19,length=58617616,assembly=20>
##contig=<ID=chr20,length=64444167,assembly=20>
##contig=<ID=chr21,length=46709983,assembly=20>
##contig=<ID=chr22,length=50818468,assembly=20>
##contig=<ID=chrX,length=156040895,assembly=20>
##contig=<ID=chrY,length=57227415,assembly=20>
##contig=<ID=chrM,length=16569,assembly=20>

```


solution: delete characters 'chr' in 'ID=chr1'
```
grep '^#' Mills_and_1000G_gold_standard.indels.hg38_dechr.vcf > head
sed 's/ID=chr/ID=/g' head > head-1
grep -v '^#' Mills_and_1000G_gold_standard.indels.hg38_dechr.vcf > temp
cat head-1 temp > Mills_and_1000G_gold_standard.indels.hg38_dechr-1.vcf
```

### Merge two separate callsets of VCF
```
 java -jar GenomeAnalysisTK.jar \
   -T CombineVariants \
   -R reference.fasta \
   --variant input1.vcf \
   --variant input2.vcf \
   -o output.vcf \
   -genotypeMergeOptions UNIQUIFY
```


### Get the union of calls made on the same samples
```
 java -jar GenomeAnalysisTK.jar \
   -T CombineVariants \
   -R reference.fasta \
   --variant:foo input1.vcf \
   --variant:bar input2.vcf \
   -o output.vcf \
   -genotypeMergeOptions PRIORITIZE \
   -priority foo,bar
```


#### combine vcf files
```
$ java -jar /home/wuzhikun/anaconda3/envs/WGS/bin/GenomeAnalysisTK.jar -T CombineVariants -R /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --variant M625-0_2.vcf --variant  M625-2_2.vcf -o output.vcf -genotypeMergeOptions UNIQUIFY
```




### Generate an alternative reference sequence over the specified interval 
```
java -Xms1g -jar "/home/GenomeAnalysisTK.jar" \
-T "FastaAlternateReferenceMaker" \
-R "/home/refGen.fa" \
-L "chromosome3" \
-lw "100" \
--variant "/home/chromosome3_raw_snp_filter3.vcf.gz" \
-o "/home/chromosome3.fasta" \
--useIUPAC 
```


