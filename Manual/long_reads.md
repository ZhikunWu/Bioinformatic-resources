
## Alignment tools for long reads

* ngmlr
* blasr
* bwa-mem
* graphmap
* LAMSA
* lordFast
* minialign
* minimap2
* rHAT
* MashMap
* LAST


##### [ngmlr](https://github.com/philres/ngmlr):  a long-read mapper designed to align PacBio or Oxford Nanopore (standard and ultra-long) to a reference genome with a focus on reads that span structural variations
```
conda install -c bioconda ngmlr
```


##### [blasr](https://github.com/PacificBiosciences/blasr): The PacBio® long read aligner

```
blasr query.fa ./target.fasta -sa ./target.fasta.sa -bestn 40 -maxScore -500 -m 4 -nproc 24 -out target.m4 -maxLCPLength 15
```


##### [bwa mem](https://github.com/lh3/bwa)
```
conda install -c bioconda bwa
```

manual
```
bwa mem ref.fasta input.fastq | samtools view -b - | samtools sort - > output.bam
```

##### [graphmap](https://github.com/isovic/graphmap): A highly sensitive and accurate mapper for long, error-prone reads (2016,04)
```
conda install -c bioconda graphmap
```

##### [LAMSA](https://github.com/yangao07/LAMSA): Long Approximate Matches-based Split Aligner

```
git clone https://github.com/hitbc/LAMSA.git
cd LAMSA; make
./lamsa index ref.fa
./lamsa aln ref.fa read.fq > aln.sam
```


##### [lordFast](https://github.com/vpc-ccg/lordfast): Sensitive and Fast Alignment Search Tool for Long Read sequencing Data
```
conda install -c bioconda lordfast 
```

or

```
git clone https://github.com/vpc-ccg/lordfast.git
cd lordfast && make
```



##### [minialign](https://github.com/ocxtal/minialign): fast and accurate alignment tool for PacBio and Nanopore long reads
```
conda install -c bioconda minialign
```


#### [minimap2](https://github.com/lh3/minimap2): A versatile pairwise aligner for genomic and spliced nucleotide sequences
```
conda install -c bioconda minimap2
```


##### [rHAT](https://github.com/dfguan/rHAT): fast alignment of noisy long reads with regional hashing
```
git clone https://github.com/dfguan/rHAT.git
cd src && make
cd ../.. && ln -s /home/wuzhikun/anaconda3/envs/NanoSV/bin/rHAT/src/rHAT-aligner rHAT-aligner && ln -s /home/wuzhikun/anaconda3/envs/NanoSV/bin/rHAT/src/rHAT-indexer rHAT-indexer
```

manual:
```
Genome indexing:

rHAT-indexer Genome_Index_Dir Genome_File

Read alignment:

rHAT-aligner Genome_Index_Dir Fastq_File Genome_File > Sam_File
```



##### [MashMap](https://github.com/marbl/MashMap): A fast approximate aligner for long DNA sequences
```
conda install -c bioconda mashmap
```

##### LAST
```
conda install -c bioconda last
```

tools for LAST:
```
lastal
lastal8
lastdb
lastdb8
last-dotplot
last-map-probs
last-merge-batches
last-pair-probs
last-postmask
last-split
last-split8
last-train
```



## Callers for structural variants 

#### [SVIM](https://github.com/eldariont/svim): Structural Variant Identification Method using Long Reads

```
conda install -c bioconda svim
```

#### [Sniffles](https://github.com/fritzsedlazeck/Sniffles): Structural variation caller using third generation sequencing
```
conda install -c bioconda sniffles
```


#### [Picky](https://github.com/TheJacksonLaboratory/Picky): Structural Variants Pipeline for Long Reads

```
$ perl picky.pl
Please specify the command.

picky.pl <command> -h

<command> [hashFq, selectRep, callSV]
hashFq    : hash read uuids to friendly ids
lastParam : Last parameters for alignment
selectRep : select representative alignments for read
callSV    : call structural variants
xls2vcf   : convert Picky sv xls file to vcf
preparepbs: chunk last fastq file and write pbs script for cluster submission
script    : write a bash-script for single fastq processing


      License = JACKSON LABORATORY NON-COMMERCIAL LICENSE AGREEMENT
                https://github.com/TheJacksonLaboratory/Picky/blob/master/LICENSE.md
Documentation = https://github.com/TheJacksonLaboratory/Picky/wiki
   Repository = https://github.com/TheJacksonLaboratory/Picky/

```

```
$ locate picky.pl

/home/wuzhikun/anaconda3/envs/NanoSV/bin/Picky-0.2.a/src/picky.pl
```


##### [pbsv](https://github.com/PacificBiosciences/pbsv) (special for Pacbio read)

```
pbsv fasta [movie].subreads.bam | \
minimap2 -t 8 -x map-pb -a --eqx -L -O 5,56 -E 4,1 -B 5 \
--secondary=no -z 400,50 -r 2k -Y [reference].fa - | \
samtools sort > [sample]_[movie]_[reference].bam
```

##### [SMRT-SV](https://github.com/EichlerLab/pacbio_variant_caller): Structural variant and indel caller for PacBio reads


##### [nanosv](https://github.com/mroosmalen/nanosv): SV caller for nanopore data





## Tools for genonme Assembly 

### Assembly only for long reads


#### [MECAT](https://github.com/xiaochuanle/MECAT): an ultra-fast mapping, error correction and de novo assembly tool for single-molecule sequencing reads
```
git clone https://github.com/xiaochuanle/MECAT.git
make
```

tools
```
$ tree /home/wuzhikun/anaconda3/envs/Assembly/bin/MECAT/Linux-amd64/bin 
/home/wuzhikun/anaconda3/envs/Assembly/bin/MECAT/Linux-amd64/bin
├── bogart
├── buildGraph
├── correctOverlaps
├── es_fasta2fastq
├── es_fastq2ca
├── es_gatekeeper
├── extract_sequences
├── fastaconvert
├── filter_reads
├── findErrors
├── gatekeeperCreate
├── gatekeeperDumpFASTQ
├── gatekeeperDumpMetaData
├── gatekeeperPartition
├── lib
│   └── canu
│       ├── Configure.pm
│       ├── Consensus.pm
│       ├── Defaults.pm
│       ├── Execution.pm
│       ├── Gatekeeper.pm
│       ├── Grid_LSF.pm
│       ├── Grid_PBSTorque.pm
│       ├── Grid.pm
│       ├── Grid_SGE.pm
│       ├── Grid_Slurm.pm
│       ├── HTML.pm
│       ├── lib
│       │   └── perl5
│       │       └── x86_64-linux-thread-multi
│       │           ├── auto
│       │           │   └── Filesys
│       │           │       └── Df
│       │           │           ├── Df.bs
│       │           │           └── Df.so
│       │           ├── Filesys
│       │           │   └── Df.pm
│       │           └── perllocal.pod
│       ├── man
│       │   └── man3
│       │       └── Filesys::Df.3pm
│       ├── Output.pm
│       ├── OverlapBasedTrimming.pm
│       ├── OverlapErrorAdjustment.pm
│       ├── Overlapmecat2asmpw.pm
│       ├── OverlapStore.pm
│       └── Unitig.pm
├── libcanu.a
├── libes.a
├── libmecat.a
├── mecat2asmpw
├── mecat2asmpw50
├── mecat2asmpwConvert
├── mecat2canu
├── mecat2canu.defaults
├── mecat2cns
├── mecat2pw
├── mecat2ref
├── mecat2trimpw
├── mecat2trimpw50
├── ovStoreBucketizer
├── ovStoreBuild
├── ovStoreDump
├── ovStoreStats
├── partition_reads
├── splitReads
├── tgStoreCoverageStat
├── tgStoreDump
├── tgStoreLoad
├── trimReads
└── utgcns

```


#### [wtdbg2](https://github.com/ruanjue/wtdbg2): A fuzzy Bruijn graph approach to long noisy reads assembly
```
git clone https://github.com/ruanjue/wtdbg2.git
cd wtdbg2/ && make

ln -s /home/wuzhikun/anaconda3/envs/Assembly/share/wtdbg2/wtdbg2 /home/wuzhikun/anaconda3/envs/Assembly/bin/wtdbg2
ln -s /home/wuzhikun/anaconda3/envs/Assembly/share/wtdbg2/wtdbg-cns /home/wuzhikun/anaconda3/envs/Assembly/bin/wtdbg-cns
ln -s /home/wuzhikun/anaconda3/envs/Assembly/share/wtdbg2/wtpoa-cns /home/wuzhikun/anaconda3/envs/Assembly/bin/wtpoa-cns
ln -s /home/wuzhikun/anaconda3/envs/Assembly/share/wtdbg2/kbm2 /home/wuzhikun/anaconda3/envs/Assembly/bin/kbm2
ln -s /home/wuzhikun/anaconda3/envs/Assembly/share/wtdbg2/pgzf /home/wuzhikun/anaconda3/envs/Assembly/bin/pgzf

```

#### [canu](https://github.com/marbl/canu): A single molecule sequence assembler for genomes large and small
```
conda install -c bioconda canu
```



#### [miniasm](https://github.com/lh3/miniasm): Ultrafast de novo assembly for long noisy reads (though having no consensus step)

```
conda install -c bioconda miniasm
```


#### FALCON

pb-falcon: pypeflow/FALCON/FALCON_unzip
```
conda install -c bioconda pb-falcon
```

### Assembly for short reads

#### [SparseAssembler](https://github.com/yechengxi/SparseAssembler): A sparse k-mer graph based, memory-efficient genome assembler
```
conda install -c bioconda sparseassembler 
```


### Hybrid assembly for long and short reads

#### [DBG2OLC](https://github.com/yechengxi/DBG2OLC): Efficient Assembly of Large Genomes Using Long Erroneous Reads of the Third Generation Sequencing Technologies
```
conda install -c bioconda dbg2olc
```


### Gap Filling

##### [PBJelly 2](https://sourceforge.net/projects/pb-jelly/)