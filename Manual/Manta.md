## [manta](https://github.com/Illumina/manta/tree/master/docs/userGuide)

### install manta
need python 2.7
```
  - manta -> python[version='2.7.*|>=2.7,<2.8.0a0']

```


```
(Assembly) wuzhikun@mu01 13:52:23 ^_^ /home/wuzhikun/anaconda3/envs 
$ conda install -c bioconda manta

```

### parameters

```
$ configManta.py
Usage: configManta.py [options]

Version: 1.6.0

This script configures the Manta SV analysis pipeline.
You must specify a BAM or CRAM file for at least one sample.

Configuration will produce a workflow run script which
can execute the workflow on a single node or through
sge and resume any interrupted execution.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --config=FILE         provide a configuration file to override defaults in
                        global config file (/home/wuzhikun/anaconda3/envs/Asse
                        mbly/share/manta-1.6.0-0/bin/configManta.py.ini)
  --allHelp             show all extended/hidden options

  Workflow options:
    --bam=FILE, --normalBam=FILE
                        Normal sample BAM or CRAM file. May be specified more
                        than once, multiple inputs will be treated as each BAM
                        file representing a different sample. [optional] (no
                        default)
    --tumorBam=FILE, --tumourBam=FILE
                        Tumor sample BAM or CRAM file. Only up to one tumor
                        bam file accepted. [optional] (no default)
    --exome             Set options for WES input: turn off depth filters
    --rna               Set options for RNA-Seq input. Must specify exactly
                        one bam input file
    --unstrandedRNA     Set if RNA-Seq input is unstranded: Allows splice-
                        junctions on either strand
    --referenceFasta=FILE
                        samtools-indexed reference fasta file [required]
    --runDir=DIR        Name of directory to be created where all workflow
                        scripts and output will be written. Each analysis
                        requires a separate directory. (default:
                        MantaWorkflow)
    --callRegions=FILE  Optionally provide a bgzip-compressed/tabix-indexed
                        BED file containing the set of regions to call. No VCF
                        output will be provided outside of these regions. The
                        full genome will still be used to estimate statistics
                        from the input (such as expected fragment size
                        distribution). Only one BED file may be specified.
                        (default: call the entire genome)

  Extended options (hidden):

```

#### config file

```
$ cat  /home/wuzhikun/anaconda3/envs/Assembly/share/manta-1.6.0-0/bin/configManta.py.ini

#
# This section contains all configuration settings for the top-level manta workflow,
#
[manta]

referenceFasta = /illumina/development/Isis/Genomes/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta/genome.fa

# Run discovery and candidate reporting for all SVs/indels at or above this size
# Separate option (to provide different default) used for runs in RNA-mode
minCandidateVariantSize = 8
rnaMinCandidateVariantSize = 1000

# Remove all edges from the graph unless they're supported by this many 'observations'.
# Note that one supporting read pair or split read usually equals one observation, but evidence is sometimes downweighted.
minEdgeObservations = 3

# If both nodes of an edge have an edge count higher than this, then skip evaluation of the edge.
# Set to 0 to turn this filtration off
graphNodeMaxEdgeCount = 10

# Run discovery and candidate reporting for all SVs/indels with at least this
# many spanning support observations
minCandidateSpanningCount = 3

# After candidate identification, only score and report SVs/indels at or above this size:
minScoredVariantSize = 50

# minimum VCF "QUAL" score for a variant to be included in the diploid vcf:
minDiploidVariantScore = 10

# VCF "QUAL" score below which a variant is marked as filtered in the diploid vcf:
minPassDiploidVariantScore = 20

# minimum genotype quality score below which single samples are filtered for a variant in the diploid vcf:
minPassDiploidGTScore = 15

# somatic quality scores below this level are not included in the somatic vcf:
minSomaticScore = 10

# somatic quality scores below this level are filtered in the somatic vcf:
minPassSomaticScore = 30

# Remote read retrieval is used ot improve the assembly of putative insertions by retrieving any mate reads in remote
# locations with poor mapping quality, which pair to confidently mapping reads near the insertion locus. These reads
# can help to fully assemble longer insertions, under certain circumstances this feature can add a very large runtime
# burden. For instance, given the very high chimeric pair rates found in degraded FFPE samples, the runtime of the read
# retrieval process can be unpredicable. For this reason the feature is disabled by default for somatic variant calling.
# This feature can be enabled/disabled separately for germline and cancer calling below.
#
# Here "CancerCallingModes" includes tumor-normal subtraction and tumor-only calling. "GermlineCallingModes" includes
# all other calling modes.
enableRemoteReadRetrievalForInsertionsInGermlineCallingModes = 1
enableRemoteReadRetrievalForInsertionsInCancerCallingModes = 0

# Set if an overlapping read pair will be considered as evidence
# Set to 0 to skip overlapping read pairs
useOverlapPairEvidence = 0

# Set the filter on candidates of insignificant evidence signal
# This is forced to 0 for runs in RNA-mode
enableEvidenceSignalFilter = 1

```


### run manta
```
(Assembly) wuzhikun@fat01 14:27:15 ^_^ /home/wuzhikun/Project/Illumina_Trio/mapping/delly 
$ configManta.py --config /home/wuzhikun/anaconda3/envs/Assembly/share/manta-1.6.0-0/bin/configManta.py.ini --referenceFasta /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --bam  M446-0.bqsr_chr16.bam  --runDir M446-0

Successfully created workflow run script.
To execute the workflow, run the following script and set appropriate options:

/home/wuzhikun/Project/Illumina_Trio/mapping/delly/M446-0/runWorkflow.py

```

#### output file 

```
/home/wuzhikun/Project/Illumina_Trio/mapping/delly/M446-0/results/variants

-rw-rw-r-- 1  85K Dec 24 14:33 candidateSmallIndels.vcf.gz
-rw-rw-r-- 1  18K Dec 24 14:33 candidateSmallIndels.vcf.gz.tbi
-rw-rw-r-- 1 101K Dec 24 14:33 candidateSV.vcf.gz
-rw-rw-r-- 1  15K Dec 24 14:33 candidateSV.vcf.gz.tbi
-rw-rw-r-- 1  16K Dec 24 14:33 diploidSV.vcf.gz
-rw-rw-r-- 1 1.7K Dec 24 14:33 diploidSV.vcf.gz.tbi

```

```
(Assembly) wuzhikun@fat01 14:50:00 ^_^ /home/wuzhikun/Project/Illumina_Trio/mapping/delly/M446-0/results/stats 
$ l
total 13K
-rw-rw-r-- 1  437 Dec 24 14:30 alignmentStatsSummary.txt
-rw-rw-r-- 1 5.5K Dec 24 14:33 svCandidateGenerationStats.tsv
-rw-rw-r-- 1 4.7K Dec 24 14:33 svCandidateGenerationStats.xml
-rw-rw-r-- 1 1.5K Dec 24 14:33 svLocusGraphStats.tsv

```

```
$ less alignmentStatsSummary.txt

group:  /home/wuzhikun/Project/Illumina_Trio/mapping/delly/M446-0.bqsr_chr16.bam
fragment length observations:   799600
fragment length quantiles:
0.01    109
0.05    148
0.1     172
0.25    224
0.5     295
0.75    376
0.9     452
0.95    498
0.99    582
Total sampled reads:    2022550
Total sampled paired reads:     2022550
Total sampled unpaired reads:   0
Total sampled paired reads with low MAPQ:       24673
Total sampled high-confidence read pairs passing all filters:   800115

```


### execution example

Joint Diploid Sample Analysis -- Example Configuration:
```
${MANTA_INSTALL_PATH}/bin/configManta.py \
--bam NA12878_S1.cram \
--bam NA12891_S1.cram \
--bam NA12892_S1.cram \
--referenceFasta hg19.fa \
--runDir ${MANTA_ANALYSIS_PATH}
```

Tumor Normal Analysis -- Example Configuration:
```
${MANTA_INSTALL_PATH}/bin/configManta.py \
--normalBam HCC1187BL.cram \
--tumorBam HCC1187C.cram \
--referenceFasta hg19.fa \
--runDir ${MANTA_ANALYSIS_PATH}

```



