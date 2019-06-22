## [japsa](https://github.com/mdcao/japsa)

### [japsa document](https://japsa.readthedocs.io/en/latest/index.html)

### install japsa
```
$ cd ~/anaconda3/envs/evolution/bin

$ wget https://github.com/mdcao/japsa/archive/v1.7-10a.tar.gz
$ mv v1.7-10a.tar.gz japsa_v1.7-10a.tar.gz
$ cd japsa-1.7-10a/
$ make install INSTALL_DIR=~/anaconda3/envs/evolution MXMEM=70000m SERVER=true JLP=~/anaconda3/envs/evolution/bin
```

### tools for japsa
```
jsa
jsa.amra.assppro
jsa.amra.genome2res
jsa.amra.mlst
jsa.amra.plasmidfinder
jsa.amra.rescard
jsadebugd
jsa.hts.aareads
jsa.hts.alignOpt
jsa.hts.breakbam
jsa.hts.countReads
jsa.hts.errorAnalysis
jsa.hts.fixsam
jsa.hts.fqtrim
jsa.hts.mgst
jsa.hts.n50
jsa.hts.selectIntesect
jsa.hts.selectSpan
jsa.misc.dnaGraph
jsa.np.barcode
jsa.np.fastnpreader
jsa.np.filter
jsa.np.npreader
jsa.np.npscarf
jsa.np.rtMLST
jsa.np.rtResistGenes
jsa.np.rtSpeciesTyping
jsa.np.rtStrainTyping
jsa.np.timeEmulate
jsa.phylo.normalise
jsa.phylo.xmas
jsa.phylo.xmdist
jsa.seq.addanno
jsa.seq.annotate
jsa.seq.annovcf
jsa.seq.bed2jsa
jsa.seq.emalign
jsa.seq.extract
jsa.seq.format
jsa.seq.geneDBBuild
jsa.seq.gff2fasta
jsa.seq.join
jsa.seq.refseq2genesDb
jsa.seq.rev
jsa.seq.sort
jsa.seq.split
jsa.seq.stats
jsa.sim.capsim
jsa.sim.genome
jsa.sim.htsSim
jsa.sim.testpfsm
jsa.tr.longreads
jsa.tr.longreadsv2
jsa.tr.trdepth
jsa.trv.fragment2var
jsa.trv.jsa2tr
jsa.trv.parseTRF
jsa.trv.sam2fragment
jsa.trv.sortFragment
jsa.trv.trv2bed
jsa.trv.trv2vcf
jsa.trv.vcf2trv
jsa.util.streamClient
jsa.util.streamServer
jsa.xm.compress

```


### tool example

```
$ /home/wzk/anaconda3/envs/evolution/bin/jsa --help
Japsa: A Java Package for Statistical Sequence Analysis
Version 1.7-05b, Built on Wed Oct 24 21:10:12 EDT 2018 with javac 1.8.0_121

 List of tools:

Sequence manipulation tools:
  jsa.seq.stats            Show statistical composition of sequences)
  jsa.seq.sort             Sort sequences based on their lengths
  jsa.seq.extract          Extract subsequences
  jsa.seq.rev              Reverse complement sequences (must be DNA)
  jsa.seq.bed2jsa          Convert gene annotation from bed format to Japsa format
  jsa.seq.split            Break a multiple sequence files to each sequence per file
  jsa.seq.join             Join multiple sequences into one
  jsa.seq.format           Convert sequence(s) from a format to another
  jsa.seq.addanno          Add annotations to a Japsa file
  jsa.seq.annotate         Annotate a list of regions using some annotation such as RefSeq
  jsa.seq.annovcf          Annotate variation in a vcf file using annotation from gff file
  jsa.seq.gff2fasta        Extract sequences from a gff annotation
  jsa.seq.geneDBBuild      Group genes based on their identity and build a database of gene family and their alleles
  jsa.seq.refseq2genesDb   Extract gene sequences from refseq anotation and group them
  jsa.seq.emalign          Get the best alignment of 2 sequences using Expectation-Maximisation on Finite State Machine

HTS analysis tools:
  jsa.hts.fqtrim           Trim reads from a fastq file and break the file to smaller ones
  jsa.hts.breakbam         Break a sam/bam file to smaller ones
  jsa.hts.selectIntesect   Filter reads that intersect with some regions from a sorted b/sam file
  jsa.hts.selectSpan       Filter reads that span some regions from a sorted b/sam file
  jsa.hts.countReads       Count the number of reads in some regions from a sorted, indexed bam file
  jsa.hts.alignOpt         Parameter estimation for alignment of erronenous read data
  jsa.hts.errorAnalysis    Error analysis of sequencing data
  jsa.hts.aareads          Filter reads supporting alternative alleles
  jsa.hts.n50              Compute N50 of an assembly
  jsa.hts.mgst             Metagenomics species typing from HTS sequencing
  jsa.hts.fixsam           Add read sequences to secondary alignment, applied only for
sam files by bwa without sorting.
Note it does not support paired-end at this version

Bacterial AMR  analysis:
  jsa.amra.mlst            Multi-locus strain typing
  jsa.amra.plasmidfinder   Multi-locus strain typing
  jsa.amra.genome2res      Finding resistance genes/classes in a genome
  jsa.amra.assppro         Extract subsequences
  jsa.amra.rescard         Finding resistance genes/classes in a genome using card database

Oxford Nanopore sequencing analysis tools:
  jsa.np.npreader          Extract and stream Oxford Nanopore sequencing data in real-time. Demultiplexe included.
  jsa.np.fastnpreader      Fast Extraction of Oxford Nanopore sequencing data in real-time
  jsa.np.filter            Filter nanopore reads data from fastq file
  jsa.np.rtSpeciesTyping   Realtime species typing using Nanopore Sequencing data
  jsa.np.rtMLST            Realtime Multi-Locus Strain Typing using Nanopore Sequencing data
  jsa.np.rtStrainTyping    Realtime strain typing using Nanopore sequencing data
  jsa.np.rtResistGenes     Realtime identification of antibiotic resistance genes from Nanopore sequencing
  jsa.np.timeEmulate       Regulate time
  jsa.np.npscarf           Experimental Scaffold and finish assemblies using Oxford Nanopore sequencing reads
  jsa.np.barcode           Clustering nanopore sequences based on barcode

Tandem repeat variation analysis tools:
  jsa.trv.parseTRF         Parse trf output to jsa, bed or tr format
  jsa.trv.sam2fragment     Convert a sam file to list of fragment sizes
  jsa.trv.sortFragment     Sort fragment file
  jsa.trv.fragment2var     Analyse tandem repeat variation from fragment sizes
  jsa.trv.trv2vcf          Convert tandem repeat variation in trv format to vcf
  jsa.trv.vcf2trv          Convert variation from cvf format to trv format
  jsa.trv.jsa2tr           Convert tandem repeat annotation in JAPSA format to TR format
  jsa.trv.trv2bed          Convert tandem repeat variation in trv format to bed format
  jsa.tr.trdepth           Compute read depth in repeats and flanking regions
  jsa.tr.longreads         VNTR typing using long reads

Utilities:
  jsa.util.streamServer    Listen for input from a stream and forward the streamed data to the standard output
  jsa.util.streamClient    Forward data from a stream input or a file over the network to a jsa.util.streamServer

Phylogenetics analysis tools:
  jsa.phylo.xmas           Generate a distance matrix from aligned sequences
  jsa.phylo.xmdist         Generate a distance matrix from genomes (potentially not alignable
  jsa.phylo.normalise      Scale branches of a phylogeny so that the sum of branch lengths is equal to a value

Alignment with Finite State Machines
  jsa.sim.testpfsm         Testing estimation of parameters using a three state finite machine
  jsa.sim.htsSim           Simulation of HTS sequencing with a probabistic finite (3) state machine
  jsa.sim.genome           Simulate genomes with variation from an existing genome
  jsa.sim.capsim           Simulate capture sequencing

Export Model compression
  jsa.xm.compress          Compression of DNA/protein sequences
  jsa.misc.dnaGraph        Visualisation

==========Testing===============
  jsa.tr.longreadsv2       VNTR typing using long reads

```

### Other projects based on Japsa
##### [eXpert Model](https://github.com/mdcao/xm): The expert model compression model
##### [XMas](https://github.com/mdcao/XMas): Phylogenetic distance method using information theory
##### [capsim](https://github.com/mdcao/capsim): Simulation of capture sequencing
##### [npScarf](https://github.com/mdcao/npScarf): Scaffold and Complete assemblies in real-time fashion
##### [npAnalysis](https://github.com/mdcao/npAnalysis): Realtime identification of bacterial sample
##### [npReader](https://github.com/mdcao/npReader): Real-time extraction and analysis Oxford Nanopore sequencing data
##### [npBarcode](https://github.com/hsnguyen/npBarcode): Demultiplex barcoded Oxford Nanopore sequencing
##### [PhageXpress](https://github.com/mdcao/phagexpress)

### Japsa manual

#### The contig list is then sorted with jsa.seq.sort
```
$ jsa.seq.sort -r -n --input spades/contigs.fasta --output Kp2146_spades.fasta 
```



#### alignment with bwa
```
$ bwa mem -t 10 -k11 -W20 -r10 -A1 -B1 -O1 -E1 -L0 -a -Y Kp2146_spades.fasta ERR868296_1.fastq.gz > ERR868296.sam

```

### Experimental Scaffold and finish assemblies using Oxford Nanopore sequencing reads
```
$ jsa.np.npscarf -input ERR868296.sam  -format sam -seq Kp2146_spades.fasta -prefix Kp2146-batch

[main] WARN japsa.tools.bio.np.NPScarfCmd - Not found any legal SPAdes output folder, assembly graph thus not included!
#Sort list of bridges
========================== START =============================
  contig   0  ======>     0  839487 1-NODE_1_length_839487_cov_89.415705 
Size = 1 sequence
============================ END ===========================
========================== START =============================
  contig   1  ======>     0  808622 2-NODE_2_length_808622_cov_83.447634 gaps =  -121
  contig  61  ======>808501  810060 62-NODE_62_length_1559_cov_388.005587 gaps =  -36
  contig  34  ======>810024  823263 35-NODE_35_length_13239_cov_94.795226 gaps =  -134
  contig  54  ======<823129  825408 55-NODE_55_length_2279_cov_254.593401 gaps =  -241
  contig  12  ======<825167  943590 13-NODE_13_length_118423_cov_80.342023 
```

output files:
```
-rw-r--r--  1 5.6M Oct 24 22:52 Kp2146-batch.fin.fasta
-rw-r--r--  1 7.5M Oct 24 22:52 Kp2146-batch.fin.japsa


$ head Kp2146-batch.fin.fasta
>Scaffold0
TTGCCTGGCGGCACTAGCGCGGTGGTCCCACCTGACCCCATGCCGAACTCAGAAGTGAAA
CGCCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCATGTGAGAGTAGGGAACTGCCAGGCA
TCAAATTTAGCGTGCTGATATGGCTCAGTTGGTAGAGCGCACCCTTGGTAAGGGTGAGGT
CCCCAGTTCGACTCTGGGTATCAGCACCACTTTTTAGGTTAAAGTTCGGCACGTTGTAAA
GAATTTGCCTGGCGACAATAGCGCGGCGGTCCCACCTGACCCCATGCCGAACTCAGAAGT
GAAACGTCGTAGCGCCGATGGTAGTGTGGGGTCTCCCCATGTGAGAGTAGGGAATCGCCA
GGCATCAAATAAAGCAGAAGGCCCAGTCGAAAGACTGGGCCTTCTGCTTTTGTGTTATCT
GTTATCTGTTGATAAACAGTCCTGCCACCAGGGGGAAACCCGTCAAAGTCGATTTGCTCG
TAATGCAGCAAGGGACAGAGAGTTTATTTGCCCGGTTGTCATGTGGATGATGCGCAGAAG



$ head  Kp2146-batch.fin.japsa
#JSA:Scaffold0:839487:DNA16
>A:Linear


>>CONTIG:1:839487:1-NODE_1_length_839487_cov_89.415705:+::0.0
>1-NODE_1_length_839487_cov_89.415705+[0,839487)

         1   TTGCCTGGCG GCACTAGCGC GGTGGTCCCA CCTGACCCCA TGCCGAACTC
        51   AGAAGTGAAA CGCCGTAGCG CCGATGGTAG TGTGGGGTCT CCCCATGTGA
       101   GAGTAGGGAA CTGCCAGGCA TCAAATTTAG CGTGCTGATA TGGCTCAGTT


```



