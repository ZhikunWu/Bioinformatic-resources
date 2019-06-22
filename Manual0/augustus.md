
## [augustus](http://bioinf.uni-greifswald.de/augustus/)

### [Predicting Genes with AUGUSTUS](http://bioinf.uni-greifswald.de/augustus/binaries/tutorial/prediction.html#predh)

### [AUGUSTUS tutorials](http://bioinf.uni-greifswald.de/bioinf/wiki/pmwiki.php?n=Augustus.Augustus)
### [Using Scipio to create a (training) set of gene structures](http://bioinf.uni-greifswald.de/augustus/binaries/tutorial/scipio.html)
### [Lab Session on Gene Prediction with AUGUSTUS](http://bioinf.uni-greifswald.de/augustus/binaries/tutorial/index.html)
### [Augustus使用技巧](http://www.chenlianfu.com/?p=1248)
### [Augustus Training and Prediction](http://www.chenlianfu.com/?p=2307)



### install augustus

```
$ conda install -c bioconda augustus
```


### augustus parameters

```
$ augustus
AUGUSTUS (3.2.2) is a gene prediction tool
written by M. Stanke, O. Keller, S. König, L. Gerischer and L. Romoth.

usage:
augustus [parameters] --species=SPECIES queryfilename

'queryfilename' is the filename (including relative path) to the file containing the query sequence(s)
in fasta format.

SPECIES is an identifier for the species. Use --species=help to see a list.

parameters:
--strand=both, --strand=forward or --strand=backward
--genemodel=partial, --genemodel=intronless, --genemodel=complete, --genemodel=atleastone or --genemodel=exactlyone
  partial      : allow prediction of incomplete genes at the sequence boundaries (default)
  intronless   : only predict single-exon genes like in prokaryotes and some eukaryotes
  complete     : only predict complete genes
  atleastone   : predict at least one complete gene
  exactlyone   : predict exactly one complete gene
--singlestrand=true
  predict genes independently on each strand, allow overlapping genes on opposite strands
  This option is turned off by default.
--hintsfile=hintsfilename
  When this option is used the prediction considering hints (extrinsic information) is turned on.
  hintsfilename contains the hints in gff format.
--AUGUSTUS_CONFIG_PATH=path
  path to config directory (if not specified as environment variable)
--alternatives-from-evidence=true/false
  report alternative transcripts when they are suggested by hints
--alternatives-from-sampling=true/false
  report alternative transcripts generated through probabilistic sampling
--sample=n
--minexonintronprob=p
--minmeanexonintronprob=p
--maxtracks=n
  For a description of these parameters see section 4 of README.TXT.
--proteinprofile=filename
  When this option is used the prediction will consider the protein profile provided as parameter.
  The protein profile extension is described in section 7 of README.TXT.
--progress=true
  show a progressmeter
--gff3=on/off
  output in gff3 format
--predictionStart=A, --predictionEnd=B
  A and B define the range of the sequence for which predictions should be found.
--UTR=on/off
  predict the untranslated regions in addition to the coding sequence. This currently works only for a subset of species.
--noInFrameStop=true/false
  Do not report transcripts with in-frame stop codons. Otherwise, intron-spanning stop codons could occur. Default: false
--noprediction=true/false
  If true and input is in genbank format, no prediction is made. Useful for getting the annotated protein sequences.
--uniqueGeneId=true/false
  If true, output gene identifyers like this: seqname.gN

For a complete list of parameters, type "augustus --paramlist".
An exhaustive description can be found in the file README.TXT.

```

### config bin

```
$ export PATH=/home/wzk/anaconda3/pkgs/augustus-3.2.2-0/bin:$PATH
```

### config PATH
```
$ export AUGUSTUS_CONFIG_PATH=/home/wzk/anaconda3/pkgs/augustus-3.2.2-0/config
```

config dirrctory
```
(evolution) wzk@ubuntu 08:08:08 ^_^ /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/config 
$ l
total 20K
drwxr-xr-x  2 4.0K Apr 24  2018 cgp
drwxr-xr-x  2 4.0K Apr 24  2018 extrinsic
drwxr-xr-x  2 4.0K Apr 24  2018 model
drwxr-xr-x  2 4.0K Apr 24  2018 profile
drwxr-xr-x 99 4.0K Apr 24  2018 species

```


### scripts 

```
$ tree bin
bin
├── augustus
├── bam2hints
├── etraining
├── fastBlockSearch
├── filterBam
├── homGeneMapping
├── joingenes
└── prepareAlign

```


```
$ tree scripts
scripts
├── augustus2browser.pl
├── augustus2gbrowse.pl
├── autoAug.pl
├── autoAugPred.pl
├── autoAugTrain.pl
├── autoRun.pathInfo
├── bedgraph2wig.pl
├── blat2gbrowse.pl
├── blat2hints.pl
├── block2prfl.pl
├── cegma2gff.pl
├── checkParamArchive.pl
├── checkUTR
├── cleanDOSfasta.pl
├── clusterAndSplitGenes.pl
├── createAugustusJoblist.pl
├── del_from_prfl.pl
├── evalCGP.pl
├── exonerate2hints.pl
├── exoniphyDb2hints.pl
├── extractTranscriptEnds.pl
├── filterGenesIn_mRNAname.pl
├── filterGenesOut_mRNAname.pl
├── filterGenes.pl
├── filterInFrameStopCodons.pl
├── filterMaf.pl
├── filter-ppx.pl
├── filterPSL.pl
├── filterShrimp.pl
├── filterSpliceHints.pl
├── gbrowse.conf
├── gbrowseold2gff3.pl
├── gbSmallDNA2gff.pl
├── getAnnoFasta.pl
├── gff2gbSmallDNA.pl
├── gff2ps_mycustom
├── gffGetmRNA.pl
├── gp2othergp.pl
├── gtf2gff.pl
├── hal2maf_split.pl
├── helpMod.pm
├── intron2exex.pl
├── join_aug_pred.pl
├── join_mult_hints.pl
├── joinPeptides.pl
├── maf2conswig.pl
├── makeMatchLists.pl
├── makeUtrTrainingSet.pl
├── maskNregions.pl
├── moveParameters.pl
├── msa2prfl.pl
├── new_species.pl
├── optimize_augustus.pl
├── opt_init_and_term_probs.pl
├── parseSim4Output.pl
├── partition_gtf2gb.pl
├── pasapolyA2hints.pl
├── peptides2alternatives.pl
├── peptides2hints.pl
├── phastconsDB2hints.pl
├── polyA2hints.pl
├── prints2prfl.pl
├── pslMap.pl
├── randomSplit.pl
├── ratewig.pl
├── README.autoAug
├── retroDB2hints.pl
├── rmRedundantHints.pl
├── runAllSim4.pl
├── samMap.pl
├── scipiogff2gff.pl
├── selectLongestORFs.pl
├── simpleFastaHeaders.pl
├── simplifyFastaHeaders.pl
├── SplicedAlignment.pm
├── splitMfasta.pl
├── split_wiggle.pl
├── summarizeACGTcontent.pl
├── transMap2hints.pl
├── uniquePeptides.pl
├── utrgff2gbrowse.pl
├── webserver-results.body
├── webserver-results.head
├── webserver-results.tail
├── weedMaf.pl
├── wig2hints.pl
├── wigchoose.pl
├── writeResultsPage.pl
└── yaml2gff.1.4.pl

```


### train the data

```
$ /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/scripts/autoAugTrain.pl  --genome=/home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa --trainingset=/home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.35.gff3 -species=arabidopsis --useexisting

1 - WARNING: Detected whitespace in fasta header of file /home/wzk/database/GENOME/arabidopsis/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa. This may later on cause problems! If the pipeline turns out to crash, please clean up the fasta headers, e.g. by using simplifyFastaHeaders.pl. This message will be suppressed from now on!
Have mRNA and UTR for gene transcript:AT1G05460.2 in sequence 1. Ignoring UTR annotation and using mRNA annotation only.
Suppressing this error message from now on.
Sequence 2 dna:chromosome chromosome:TAIR10:2:1:19698289:1 REF has no annotation but 2 has. Assuming that spacencates name.

Warning: Had redundant UTR exon information for 44605 genes.
Warning: I assumed 7 times that sequence names end at first space.
failed to execute: 

```

out files

```
$ tree autoAugTrain
autoAugTrain
├── gbrowse
├── predictions
│   ├── abinitio.1
│   ├── hints.E
│   └── hints.UTR.E
└── training
    ├── test
    ├── train.err
    ├── training.gb
    ├── training.gb.onlytrain
    ├── training.gb.test
    ├── training.gb.train
    ├── training.gb.train.test
    ├── training.gff
    ├── train.out
    └── utr

```

### gene prediction
```
$ /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/bin/augustus --strand=both  --genemodel=complete --uniqueGeneId=true --noInFrameStop=true --gff3=on --AUGUSTUS_CONFIG_PATH=/home/wzk/anaconda3/pkgs/augustus-3.2.2-0/config  --species=arabidopsis  ../Arabidopsis_thaliana.TAIR10.dna.toplevel.fa > protein_out.txt

Warning: The gff3 standard requires that the stop codon is included in the CDS. Unless this is your intention, set stopCodonExcludedFromCDS to false in your species' configuration file or on the command line.

```

out file
```
##gff-version 3
# This output was generated with AUGUSTUS (version 3.2.2).
# AUGUSTUS is a gene prediction tool written by M. Stanke (mario.stanke@uni-greifswald.
# O. Keller, S. König, L. Gerischer and L. Romoth.
# Please cite: Mario Stanke, Mark Diekhans, Robert Baertsch, David Haussler (2008),
# Using native and syntenically mapped cDNA alignments to improve de novo gene finding
# Bioinformatics 24: 637-644, doi 10.1093/bioinformatics/btn013
# No extrinsic information on sequences given.
# arabidopsis version. Using default transition matrix.
# We have hints for 0 sequences and for 0 of the sequences in the input set.
#
# ----- prediction on sequence number 1 (length = 30427671, name = 1) -----
#
# Predicted genes for sequence number 1 on both strands
# start gene 1.g1
1       AUGUSTUS        gene    3636    5916    0.1     +       .       ID=1.g1
1       AUGUSTUS        transcript      3636    5916    0.1     +       .       ID=1.g1
1       AUGUSTUS        transcription_start_site        3636    3636    .       +
1       AUGUSTUS        exon    3636    3913    .       +       .       Parent=1.g1.t1
1       AUGUSTUS        start_codon     3760    3762    .       +       0       Parent=
1       AUGUSTUS        intron  3914    3995    1       +       .       Parent=1.g1.t1
1       AUGUSTUS        intron  4277    4485    1       +       .       Parent=1.g1.t1
1       AUGUSTUS        intron  4606    4705    1       +       .       Parent=1.g1.t1
1       AUGUSTUS        intron  5096    5173    1       +       .       Parent=1.g1.t1
1       AUGUSTUS        intron  5327    5438    1       +       .       Parent=1.g1.t1
1       AUGUSTUS        CDS     3760    3913    1       +       0       ID=1.g1.t1.cds;
1       AUGUSTUS        CDS     3996    4276    1       +       2       ID=1.g1.t1.cds;
1       AUGUSTUS        exon    3996    4276    .       +       .       Parent=1.g1.t1
1       AUGUSTUS        CDS     4486    4605    1       +       0       ID=1.g1.t1.cds;
1       AUGUSTUS        exon    4486    4605    .       +       .       Parent=1.g1.t1
1       AUGUSTUS        CDS     4706    5095    1       +       0       ID=1.g1.t1.cds;
1       AUGUSTUS        exon    4706    5095    .       +       .       Parent=1.g1.t1
1       AUGUSTUS        CDS     5174    5326    1       +       0       ID=1.g1.t1.cds;
1       AUGUSTUS        exon    5174    5326    .       +       .       Parent=1.g1.t1
1       AUGUSTUS        CDS     5439    5627    1       +       0       ID=1.g1.t1.cds;
1       AUGUSTUS        exon    5439    5916    .       +       .       Parent=1.g1.t1
1       AUGUSTUS        stop_codon      5628    5630    .       +       0       Parent=
1       AUGUSTUS        transcription_end_site  5916    5916    .       +       .
# protein sequence = [MEDQVGFGFRPNDEELVGHYLRNKIEGNTSRDVEVAISEVNICSYDPWNLRFQSKYKSRDAMWYF
# RTTVSGKWKLTGESVEVKDQWGFCSEGFRGKIGHKRVLVFLDGRYPDKTKSDWVIHEFHYDLLPEHQRTYVICRLEYKGDDADIL
# NMTSSAGSVVNQSRQRNSGSYNTYSEYDSANHGQQFNENSNIMQQQPLQGSFNPLLEYDFANHGGQWLSDYIDLQQQVPYLAPYE
# NFEFLVDERTSMQQHYSDHRPKKPVSGVLPDDSSDTETGSMIFEDTSSSTDSVGSSDEPGHTRIDDIPSLNIIEPLHNYKAQEQP
# SECEWKMAEDSIKIPPSTNTVKQSWIVLENAQWNYLKNMIIGVLLFISVISWIILVG]
# end gene 1.g1
###

```



### annotation
```
$ /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/bin/augustus --species=fly --predictionStart=7000001 --predictionEnd=7500000 chr2R.fa > augustus.abinitio.gff
```

### get the protein sequence

```
$ perl /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/scripts/getAnnoFasta.pl protein_out.txt > protein_sequence.fa
```

out file:
```
# This output was generated with AUGUSTUS (version 3.2.2).
# AUGUSTUS is a gene prediction tool written by M. Stanke (mario.stanke@uni-greifswald.
de),
# O. Keller, S. König, L. Gerischer and L. Romoth.
# Please cite: Mario Stanke, Mark Diekhans, Robert Baertsch, David Haussler (2008),
# Using native and syntenically mapped cDNA alignments to improve de novo gene finding
# Bioinformatics 24: 637-644, doi 10.1093/bioinformatics/btn013
# No extrinsic information on sequences given.
# Initialising the parameters using config directory /home/wzk/anaconda3/pkgs/augustus-
3.2.2-0/config/ ...
# fly version. Using default transition matrix.
# Looks like chr2R.fa is in fasta format.
# We have hints for 0 sequences and for 0 of the sequences in the input set.
#
# ----- prediction on sequence number 1 (length = 500000, name = chr2R) -----
#
# Constraints/Hints:
# (none)
# Predicted genes for sequence number 1 on both strands
# start gene g1
chr2R   AUGUSTUS        gene    7007533 7010935 0.06    -       .       g1
chr2R   AUGUSTUS        transcript      7007533 7010935 0.06    -       .       g1.t1
chr2R   AUGUSTUS        tts     7007533 7007533 .       -       .       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        exon    7007533 7008630 .       -       .       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        stop_codon      7007610 7007612 .       -       0       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        intron  7008631 7008694 1       -       .       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        intron  7008812 7008865 0.87    -       .       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        intron  7009192 7009251 0.95    -       .       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        CDS     7007610 7008630 1       -       1       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        CDS     7008695 7008811 0.87    -       1       transcript_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        exon    7008695 7008811 .       -       .       transcript_id "
g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        CDS     7008866 7009191 1       -       0       transcript_id "
g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        exon    7008866 7009191 .       -       .       transcript_id "
g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        CDS     7009252 7009353 0.94    -       0       transcript_id "
g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        exon    7009252 7009429 .       -       .       transcript_id "
g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        start_codon     7009351 7009353 .       -       0       transcr
ipt_id "g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        exon    7010820 7010935 .       -       .       transcript_id "
g1.t1"; gene_id "g1";
chr2R   AUGUSTUS        tss     7010935 7010935 .       -       .       transcript_id "
g1.t1"; gene_id "g1";
# protein sequence = [MNTLSSARSVAIYVGPVRSSRSASVLAHEQAKSSITEEHKTYDEIPRPNKFKFMRAFMPGGEFQN
ASITEYTSAMRKR
# YGDIYVMPGMFGRKDWVTTFNTKDIEMVFRNEGIWPRRDGLDSIVYFREHVRPDVYGEVQGLVASQNEAWGKLRSAINPIFMQPR
GLRMYYEPLSNIN
# NEFIERIKEIRDPKTLEVPEDFTDEISRLVFESLGLVAFDRQMGLIRKNRDNSDALTLFQTSRDIFRLTFKLDIQPSMWKIISTP
TYRKMKRTLNDSL
# NVAQKMLKENQDALEKRRQAGEKINSNSMLERLMEIDPKVAVIMSLDILFAGVDATATLLSAVLLCLSKHPDKQAKLREELLSIM
PTKDSLLNEENMK
# DMPYLRAVIKETLRYYPNGLGTMRTCQNDVILSGYRVPKGTTVLLGSNVLMKEATYYPRPDEFLPERWLRDPETGKKMQVSPFTF
LPFGFGPRMCIGK
# RVVDLEMETTVAKLIRNFHVEFNRDASRPFKTMFVMEPAITFPFKFTDIEQ]
# end gene g1
###

```


### get protein sequence
```
$ perl /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/scripts/getAnnoFasta.pl augustus.abinitio.gff
```

output file **augustus.abinitio.aa**
```
$ head augustus.abinitio.aa

>g1.t1
MNTLSSARSVAIYVGPVRSSRSASVLAHEQAKSSITEEHKTYDEIPRPNKFKFMRAFMPGGEFQNASITEYTSAMRKRYGDIYVMPGMFGRKDWVTTFNT
KDIEMVFRNEGIWPRRDGLDSIVYFREHVRPDVYGEVQGLVASQNEAWGKLRSAINPIFMQPRGLRMYYEPLSNINNEFIERIKEIRDPKTLEVPEDFTD
EISRLVFESLGLVAFDRQMGLIRKNRDNSDALTLFQTSRDIFRLTFKLDIQPSMWKIISTPTYRKMKRTLNDSLNVAQKMLKENQDALEKRRQAGEKINS
NSMLERLMEIDPKVAVIMSLDILFAGVDATATLLSAVLLCLSKHPDKQAKLREELLSIMPTKDSLLNEENMKDMPYLRAVIKETLRYYPNGLGTMRTCQN
DVILSGYRVPKGTTVLLGSNVLMKEATYYPRPDEFLPERWLRDPETGKKMQVSPFTFLPFGFGPRMCIGKRVVDLEMETTVAKLIRNFHVEFNRDASRPF
KTMFVMEPAITFPFKFTDIEQ
>g2.t1
MNTLSSARSVAIYVGPVRSSRSASVLAHEQAKSSITEEHKTYDEIPRPNKFKFMRAFMPGGEFQNASITEYTSAMRKRYGDIYVMPGMFGRKDWVTTFNT
KDIEMVFRNEGIWPRRDGLDSIVYFREHVRPDVYGEVQGLVASQNEAWGKLRSAINPIFMQPRGLRMYYEPLSNINNEFIERIKEIRDPKTLEVPEDFTD

```


### browser tract
In order to visually inspect our results and to compare with the FlyBase annotation we will now make a custom track of the gene structures in augustus.abinitio.gff. We need to create a few header lines in the custom track file which we can either do manually with an editor or like below on the command line (cut and paste).
```
$ echo -e "browser position chr2R:7000000-7050000\nbrowser hide multiz15way bdtnpChipper\ntrack name=abinitio description=\"Augustus ab initio predictions\" db=dm3 visibility=3" > abinitio.browser

$ grep -P "AUGUSTUS\tCDS" augustus.abinitio.gff >> abinitio.browser

```

### prepare hints

Sources of Hints
ESTs or mRNAs   transcriptome reads, long enough to span several exons (454, Sanger)
RNA-Seq high coverage short read transcriptome sequences (Illumina, SOLiD)
genomic conservation    
MSMS

#### from ESTs

est sequence file
```
$ head est.chr2R.7M-8M.fa
>gi|1703783
CCGAACCGGTCCGGTACTCAGTTTTTGTTGTAGAAGTAGGCGTTCGACGGCCTAGTTGAACTTGAATTAT
TCACCGATATCGCTTCAAGTGAACCCAAATAATGATGTGGCGCCTTGCTGGAGTGCTCCTACTAGGCTTC
ATCGCCATCTCGTCCGGAGCGGAGCAGGATGTCCTGGAACTGGGGGACGACGACTTTGCCACCACCCTAA
AACAACACGAGACGACGCTGGTCATGTTCTACGCCCCCTGGTGCGGCCACTGCAAGCGATTGAAGCCCGA
GTACGCCAAGGCGGCGGAGATNGTGAAAGACGATAATCCGCCAATCAAACTGGCCAAGGTTGACTGTACG
GAAGCTGGAAAGGAAACGTGTAGCAAGTACTCCGTCAGCGGGTACCCAACTCTGAAGATCTTCCGTCAGG
ATGAGGTGTCGCANGACTACAATGGAC
>gi|1703784
TAGAACTCAATCAGCGTGTCTTTGCCATTGTTGATAACCAGATCGTCGAAGTTCTTGGCGACGGCCACCT
```


align est sequence to genome
```
$ blat -noHead chr2R.fa est.chr2R.7M-8M.fa est.psl

Loaded 21146708 letters in 1 sequences
Searched 3387685 bases in 8458 sequences
```

create the out file with **PSL** format

```
$ head est.psl
440 5   0   2   0   0   1   1281    -   gi|1703783  447 0   447 chr2R   21146708    7776697 7778425 2     197,250,  0,197,  7776697,7778175,
494 3   0   1   0   0   2   65  +   gi|1703784  498 0   498 chr2R   21146708    7775550 7776113 3     452,12,34,    0,452,464,  7775550,7776003,7776079,
346 0   0   0   0   0   0   0   -   gi|1704556  354 8   354 chr2R   21146708    7775076 7775422 1     346,  0,  7775076,
295 8   0   9   0   0   2   66  -   gi|1704738  313 1   313 chr2R   21146708    7925978 7926356 3     10,127,175,   0,10,137,   7925978,7925989,7926181,
333 1   0   9   0   0   1   426 -   gi|1705114  594 251 594 chr2R   21146708    12419393    12420162    2   14,329, 0,14,   12419393,12419833,
242 0   0   1   0   0   0   0   -   gi|1705114  594 8   251 chr2R   21146708    7583430 7583673 1     243,  343,    7583430,
508 5   0   0   0   0   0   0   +   gi|1705221  513 0   513 chr2R   21146708    7302454 7302967 1     513,  0,  7302454,
350 1   0   0   1   2   2   90  -   gi|1705271  527 0   353 chr2R   21146708    7036958 7037399 4     58,239,38,16, 174,232,473,511,    7036958,7037105,7037344,7037383,
52  0   0   0   0   0   0   0   -   gi|1705271  527 348 400 chr2R   21146708    15166038    15166090    1   52, 127,    15166038,
265 0   0   0   0   0   1   1370    +   gi|1796896  265 0   265 chr2R   21146708    7779646 7781281 2     43,222,   0,43,   7779646,7781059,

```


However, typically some ESTs align well to very many places in the genome. BLAT also includes short local alignments starting from 30bp. For this reason, we further filter the alignments

##### filt the alignment 
```
$ cat est.psl | /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/scripts/filterPSL.pl --best --minCover=80 > est.f.psl
processed line 1
        filtered:
----------------:
percent identity: 653
coverage        : 947
best            : 281
command line: --best --minCover=80
```


We can have a look at those EST alignments by creating another custom browser track:

```
$ echo -e "browser position chr2R:7000000-7050000\ntrack name=ESTs description=\"EST alignments\" db=dm3 visibility=4" > ests.browser

$ cat est.f.psl >> ests.browser
```


##### generate hints from the EST alignments

```
$ /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/scripts/blat2hints.pl --nomult --in=est.f.psl --out=hints.est.gff
```


out file:
```
$ head hints.est.gff
chr2R   b2h ep  7776708 7776894 0   .   .   grp=gi|1703783;pri=4;src=E
chr2R   b2h ep  7778176 7778415 0   .   .   grp=gi|1703783;pri=4;src=E
chr2R   b2h ep  7775561 7776015 0   .   .   grp=gi|1703784;pri=4;src=E
chr2R   b2h ep  7776080 7776103 0   .   .   grp=gi|1703784;pri=4;src=E
chr2R   b2h ep  7775087 7775412 0   .   .   grp=gi|1704556;pri=4;src=E
chr2R   b2h ep  7925989 7926116 0   .   .   grp=gi|1704738;pri=4;src=E
chr2R   b2h ep  7926182 7926346 0   .   .   grp=gi|1704738;pri=4;src=E
chr2R   b2h ep  7302465 7302957 0   .   .   grp=gi|1705221;pri=4;src=E
chr2R   b2h ep  7779657 7779689 0   .   .   grp=gi|1796896;pri=4;src=E
chr2R   b2h ep  7781060 7781271 0   .   .   grp=gi|1796896;pri=4;src=E
```


#### from  RNA-Seq

the input **wig** file which contains a coverage graph
```
$ head -n 8 chr2R.7M-8M.wig
browser position chr2R:7000000-7050000
track name=dm3.rnaseq.coverage type=wiggle_0 visibility=3
variableStep chrom=chr2R
7003586 1
7003587 1
7003588 1
7003589 1
7003590 1

```

Generate hints about exonic regions from the coverage graph

```
$ cat chr2R.7M-8M.wig | /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/scripts/wig2hints.pl --width=10 --margin=10 --minthresh=2 --minscore=4  --src=W --type=ep --radius=4.5 > hints.rnaseq.ep.gff
```


output file:
```
$ head hints.rnaseq.ep.gff
chr2R   w2h ep  7007551 7007560 5.300   .   .   src=W;mult=5;
chr2R   w2h ep  7007561 7007570 7.400   .   .   src=W;mult=7;
chr2R   w2h ep  7007571 7007580 9.700   .   .   src=W;mult=9;
chr2R   w2h ep  7007581 7007590 10.200  .   .   src=W;mult=10;
chr2R   w2h ep  7007591 7007600 9.000   .   .   src=W;mult=9;
chr2R   w2h ep  7007601 7007610 9.700   .   .   src=W;mult=9;
chr2R   w2h ep  7007611 7007620 13.000  .   .   src=W;mult=13;
chr2R   w2h ep  7007621 7007630 15.300  .   .   src=W;mult=15;
chr2R   w2h ep  7007631 7007640 13.400  .   .   src=W;mult=13;
chr2R   w2h ep  7007641 7007650 13.700  .   .   src=W;mult=13;

```


#### intron hints

The file **hints.rnaseq.intron.gff** contains likely intron positions, inferred from gaps in the query of the read alignments. Together with the intron boundaries the multiplicity (mult) is reported, which counts the number of alignments that support the given intron candidate, if there is more than one.

```
$ head hints.rnaseq.intron.gff
chr2R   b2h intron  7007656 7011244 0   .   .   grp=SRR023608.8894141/1;pri=4;src=E
chr2R   b2h intron  7007727 7011335 0   .   .   grp=SRR026433.17457170/2;pri=4;src=E
chr2R   b2h intron  7008528 7012136 0   .   .   grp=SRR023608.2379695/2;pri=4;src=E
chr2R   b2h intron  7008599 7012149 0   .   .   grp=SRR026433.15352763/1;pri=4;src=E
chr2R   b2h intron  7008631 7008694 0   .   .   grp=SRR023546.8642467/1;pri=4;src=E
chr2R   b2h intron  7008783 7012293 0   .   .   grp=SRR026433.19696268/1;pri=4;src=E
chr2R   b2h intron  7008812 7008865 0   .   .   mult=8;pri=4;src=E
chr2R   b2h intron  7008966 7012515 0   .   .   grp=SRR026433.7812602/2;pri=4;src=E
chr2R   b2h intron  7009007 7012632 0   .   .   mult=2;pri=4;src=E
chr2R   b2h intron  7009031 7012656 0   .   .   grp=SRR023546.1146214/2;pri=4;src=E
```

#### [Creating Hints for AUGUSTUS from Protein Sequences](http://bioinf.uni-greifswald.de/bioinf/wiki/pmwiki.php?n=Augustus.IncorporateProteins)

#### Concatenate all Hints

Now, join the hints from all sources into one file

```
$ cat hints.est.gff hints.rnaseq.intron.gff hints.rnaseq.ep.gff > hints.gff
```

hints.gff now contains the exon, intron and exonpart hints from ESTs as well as the intron and exonpart hints from RNA-Seq



#### prediction genes using all hits

```
$ /home/wzk/anaconda3/pkgs/augustus-3.2.2-0/bin/augustus --species=fly --predictionStart=7000001 --predictionEnd=7500000 chr2R.fa --extrinsicCfgFile=/home/wzk/anaconda3/pkgs/augustus-3.2.2-0/config/extrinsic/extrinsic.M.RM.E.W.cfg --hintsfile=hints.gff > augustus.hints.gff
```

output file:

```
# start gene g2
chr2R   AUGUSTUS        gene    7011299 7013175 0.24    -       .       g2
chr2R   AUGUSTUS        transcript      7011299 7013175 0.24    -       .       g2.t1
chr2R   AUGUSTUS        tts     7011299 7011299 .       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        exon    7011299 7012396 .       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        stop_codon      7011376 7011378 .       -       0       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        intron  7012397 7012460 1       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        intron  7012578 7012631 1       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        intron  7012958 7013017 1       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        CDS     7011376 7012396 1       -       1       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        CDS     7012461 7012577 1       -       1       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        exon    7012461 7012577 .       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        CDS     7012632 7012957 1       -       0       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        exon    7012632 7012957 .       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        CDS     7013018 7013119 1       -       0       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        exon    7013018 7013175 .       -       .       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        start_codon     7013117 7013119 .       -       0       transcript_id "g2.t1"; gene_id "g2";
chr2R   AUGUSTUS        tss     7013175 7013175 .       -       .       transcript_id "g2.t1"; gene_id "g2";
# protein sequence = [MNTLSSARSVAIYVGPVRSSRSASVLAHEQAKSSITEEHKTYDEIPRPNKFKFMRAFMPGGEFQNASITEYTSAMRKR
# YGDIYVMPGMFGRKDWVTTFNTKDIEMVFRNEGIWPRRDGLDSIVYFREHVRPDVYGEVQGLVASQNEAWGKLRSAINPIFMQPRGLRMYYEPLSNIN
# NEFIERIKEIRDPKTLEVPEDFTDEISRLVFESLGLVAFDRQMGLIRKNRDNSDALTLFQTSRDIFRLTFKLDIQPSMWKIISTPTYRKMKRTLNDSL
# NVSQKMLKENQDALEKRRQAGEKINSNSMLERLMEIDPKVAVIMSLDILFAGVDATATLLSAVLLCLSKHPDKQAKLREELLSIMPTKDSLLNEENMK
# DMPYLRAVIKETLRYYPNGFGTMRTCQNDVILSGYRVPKGTTVLLGSNVLMKEATYYPRPDEFLPERWLRDPETGKKMQVSPFTFLPFGFGPRMCIGK
# RVVDLEMETTVAKLIRNFHVEFNRDASRPFKTMFLMEPAITFPFKFTDIEQ]
# Evidence for and against this transcript:
# % of transcript supported by hints (any source): 88.9
# CDS exons: 4/4
#      W:   4 
# CDS introns: 3/3
#      E:   3 
# 5'UTR exons and introns: 0/1
# 3'UTR exons and introns: 1/1
#      W:   1 
# hint groups fully obeyed: 99
#      E:   3 
#      W:  96 
# incompatible hint groups: 42
#      E:   4 (gi|4203815,gi|2701440,gi|2871896,gi|2700091)
#      W:  38 
# end gene g2



```

