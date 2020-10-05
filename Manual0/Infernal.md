# [Infernal](http://eddylab.org/infernal/) Manual

In this tutorial, we doanload all bacterial genomes from NCBI. 
And then extract the sequence of 16S rRNA gene based on the sequence model 
with STOCKHOLM format using infernal.


## Download bacterial genome from NCBI

First, we download the summary file for bacterial genomes from NCBI.
And then we extract the url of the genome form the summary file.
```
$ curl 'ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt' > assembly_summary.txt

$ head -n 4  assembly_summary_20180715.txt
#   See ftp://ftp.ncbi.nlm.nih.gov/genomes/README_assembly_summary.txt for a description of the columns in this file.
# assembly_accession  bioproject  biosample wgs_master  refseq_category taxid species_taxid organism_name infraspecific_namisolate  version_status  assembly_level  release_type  genome_rep  seq_rel_date  asm_name  submitter gbrs_paired_asm paired_asm_comp ftp_path  excluded_from_refseq  relation_to_type_material
GCF_000010525.1 PRJNA224116 SAMD00060925    representative genome 438753  7 Azorhizobium caulinodans ORS 571  strain=ORS 571    latest  Complete Genome Major Full  2007/10/16  ASM1052v1 University of Tokyo GCA_000010525.1 identical ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/010/525/GCF_000010525.1_ASM1052v1    assembly from type material
GCF_000007365.1 PRJNA224116 SAMN02604269    representative genome 198804  9 Buchnera aphidicola str. Sg (Schizaphis graminum)strain=Sg    latest  Complete Genome Major Full  2002/07/02  ASM736v1  Uppsala Univ. GCA_000007365.1 identical ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1


$ cat assembly_summary_20180715.txt |  awk '{FS="\t"} !/^#/ {print $20} ' | sed -r 's|(ftp://ftp.ncbi.nlm.nih.gov/genomes/all/.+/)(GCF_.+)|\1\2/\2_genomic.fna.gz|'  > genomic_file_20180715.txt


$ head -n 2  genomic_file_20180715.txt
ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/010/525/GCF_000010525.1_ASM1052v1/GCF_000010525.1_ASM1052v1_genomic.fna.gz
ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_genomic.fna.gz

$ wget --input genomic_file_20180715.txt
```


## Install infernal

Install infernal through bioconda

```
$ conda install -c bioconda infernal 
```

## Function of indernal

* **cmbuild**: Build a covariance model from an input multiple alignment.
* **cmcalibrate**: Calibrate E-value parameters for a covariance model.
* **cmsearch**: Search a covariance model against a sequence database.
* **cmscan**: Search a sequence against a covariance model database.
* **cmalign**: Make a multiple alignment of many sequences to a common covariance model.
* **cmconvert**: Convert CM formats to/from Infernal v1.1 format.
* **cmemit**: Generate (sample) sequences from a covariance model.
* **cmfetch**: Get a covariance model by name or accession from a CM database.
* **cmpress**: Format a CM database into a binary format for cmscan.
* **cmstat**: Show summary statistics for each model in a CM database.

## Covariance model (CM) for bacterial 16S rRNA gene from [Rfam](http://rfam.xfam.org)

The seed file was downloded from Rfam.
A multiple alignment of bacterial 16S rRNA gene sequences. A simple example of
Stockholm format that Infernal uses for structurally-annotated alignments.

### rRNA of Rfam
```
http://rfam.xfam.org/search/keyword?queryType=unp&query=rRNA&submit=Submit

RF00177 SSU rRNA bacteria   Bacterial small subunit ribosomal RNA               
RF01959 SSU rRNA archaea    Archaeal small subunit ribosomal RNA                            
RF02540 LSU rRNA archaea    Archaeal large subunit ribosomal RNA                
RF02541 LSU rRNA bacteria   Bacterial large subunit ribosomal RNA

http://rfam.xfam.org/family/RF00177/alignment/stockholm?gzip=1&download=1
http://rfam.xfam.org/family/RF01959/alignment/stockholm?gzip=1&download=1
http://rfam.xfam.org/family/RF02540/alignment/stockholm?gzip=1&download=1
http://rfam.xfam.org/family/RF02541/alignment/stockholm?gzip=1&download=1
```




### SSU_rRNA_bacteria (RF00177.seed)

```
# STOCKHOLM 1.0

#=GF AC   RF00177
#=GF ID   SSU_rRNA_bacteria
#=GF PI   SSU_rRNA_5
#=GF DE   Bacterial small subunit ribosomal RNA
#=GF AU   Gutell RR, Nawrocki E
#=GF SE   Published; PMID:11869452
#=GF SS   Published; PMID:11869452
#=GF GA   50.00
#=GF TC   50.00
#=GF NC   49.90
#=GF TP   Gene; rRNA;
#=GF BM   cmbuild -F CM SEED
#=GF CB   cmcalibrate --mpi CM
#=GF SM   cmsearch --cpu 4 --verbose --nohmmonly -T 17.38 -Z 549862.597050 --mxsize
#=GF SM   128 CM SEQDB
#=GF CL   CL00111
#=GF DR   URL; http://www.rna.ccbb.utexas.edu/;
#=GF DR   URL; http://oberon.fvms.ugent.be:8080/rRNA/ssu/index.html;
#=GF DR   URL; http://rdp.cme.msu.edu/html/;
#=GF DR   SO; 0001263; ncRNA_gene;
#=GF DR   GO; 0003735; structural constituent of ribosome;
#=GF DR   GO; 0005840; ribosome;
#=GF RN   [1]
#=GF RM   11283358
#=GF RT   Crystal structure of the ribosome at 5.5 A resolution.
#=GF RA   Yusupov MM, Yusupova GZ, Baucom A, Lieberman K, Earnest TN, Cate JH,
#=GF RA   Noller HF
#=GF RL   Science 2001;292:883-896.
#=GF RN   [2]
#=GF RM   11869452
#=GF RT   The comparative RNA web (CRW) site: an online database of comparative
#=GF RT   sequence and structure information for ribosomal, intron, and other RNAs.
#=GF RA   Cannone JJ, Subramanian S, Schnare MN, Collett JR, D'Souza LM, Du Y, Feng
#=GF RA   B, Lin N, Madabusi LV, Muller KM, Pande N, Shang Z, Yu N, Gutell RR
#=GF RL   BMC Bioinformatics. 2002;3:2.
#=GF WK   Ribosomal_RNA
#=GF SQ   99



AY138309.1/1-1552                      UUAUUGGAGAGUU-UGAU-CCUGGCUCAGGAUGAACGCU-GG-CGG--CGUG-CCUAAUACAUGCAAGUCGAGCG-AAUG---------GAUUAAGAGCU-----UG
AEZG01000028.1/4341-5872               UGUUUGGAGAGUU-UGAU-CCUGGCUCAGGACGAACGCU-GG-CGG--CGUG-CUUAACACAUGCAAGUCGAACG-GAA------------AGGUCUCUU-----CG
ABKZ01000640.1/5030-3495               GAACUGAAGAGUU-UGAU-CAUGGCUCAGAUUGAACGCU-GG-CGG--CAGG-CCUAACACAUGCAAGUCGAGCG-GAU-----------GAAGGGAGCU-----UG
AAFJ01000008.1/10852-9340              ACUAUGGAGAGUU-UGAU-CCUGGCUCAGAGUGAACGCU-GG-CGG--CGUG-CCUAAUACAUGCAAGUCGAACG-AUGA---------AGCUUCUAGCU-----UG
GU260705.1/11747-13300                 UAACAUGAGAGUU-UGAU-CCUGGCUCAGAAUCAACGCU-GG-CGG--CGUG-CCUAACACAUGCAAGUCGAACG-CGA------------GGGUCCCGC-----AA
CP001205.1/442210-440675               AUAACGAAGAGUU-UGAU-CCUGGCUUAGAACUAACGCU-GG-CAG--UGCG-UCUUAAGCAUGCAAGUCAAACG----------------GGAUGUAGC-----AA
AC149043.3/15235-16757                 ACAAUGGAGAGUU-UGAU-CCUGGCUCAGGAUGAACGCU-AG-CGG--CAGG-CCUAAUACAUGCAAGUCGAACG-GGC-----------UUUGGGACUU-----CG
EU123923.1/77-1583                     AAACUUGAGAGUU-UGAU-CCUGGCUCAGAACGAACGCU-GG-CGG--CAAG-CCUAACACAUGCAAGUCGAACG-GACAAU-----UAUUUAUAGCCUC-----U-
CP001634.1/1770527-1772065             UGGAUGGAGGGUU-UGAU-CCUGGCUCAGGGUGAACGCU-GG-CGG--CGUG-CCUGACACAUGCAAGUCGUACG-GGC------------GGACCCCCU-----UC
ADVG01000004.1/1323946-1322469         UGAAUGGCGAGUU-UGAU-CCUGGCUCAGGAUAAACGCU-GG-CGG--CGUG-CCUAACACAUGCAAGUCGAACG----------------CCCUCUCGC-----AA
AFPX01000069.1/35-1566                 ACAAUGGAGAGUU-UGAU-CCUGGCUCAGGAUGAACGCU-GG-CUA--CAGG-CUUAACACAUGCAAGUCGUGGG-GAAACG------GCAUUAUGUGCU-----UG
AF211138.2/108-1652                    UUUCUUAUGAGUU-UGAU-CAUAGCUCAGAUUGAACGCU-AG-CGA--CAAG-CCUAACACAUGCAAGUUGUGCG-AAU------------UAUUUUAUU----AAA
ACIN02000006.1/16266-14733             UUAUAUGAGAGUU-UGAU-CCUGGCUCAGGAUGAACGCU-GG-CGG--CGUG-CCUAACACAUGCAAGUCGAACG-GAGA---------UUACGGACGGA-----AG
AJ965256.1/805037-803541               AGCUUGGAGAGUU-UGAU-CCUGGCUCAGGAUGAACGCU-AG-CGG--CGUG-CCUUAUGCAUGCAAGUCGAACG----------------GUCUUAAGC-----AA
CP002458.1/700517-699005               UUUUUCGAGAGUU-UGAU-CCUGGCUCAGGAUGAACGCU-GG-CUG--UGUG-CCUAAUACAUGCAUGUCGAGCG-----------------AAGGUAGC-----AA
CP001100.1/908786-907295               ACAACGGAGAGUU-UGAU-CCUGGCUCAGGACGAACGCU-GG-CGG--CGUG-CCUAACACAUGCAAGCCAAAGG-AA-----------------AGCUU-----CG
FQ859183.1/1179117-1180628             ACGAUGAAGAGUU-UGAU-CCUGGCUCAGGAUGAACGCU-AG-CGG--CAGG-CUUAACACAUGCAAGUCGAGGG---G------------UAUAGUAGC-----AA
AAYP01000003.1/232298-233810           AUUUUAAAGAGUU-UGAU-CCUGGCUCAGGAUUAACGCU-GG-CGG--CAUG-CCUAAUACAUGCAAAUCGAACG-----------------AAGCCUUU-----U-
```



### RF00177.seed calibrated using cmcalibrate

An example CM file. Built with **cmbuild** from **RF00177.seed** and calibrated using
**cmcalibrate** (from infernal). 
```
INFERNAL1/a [1.1.1 | July 2014]
NAME     SSU_rRNA_bacteria
ACC      RF00177
DESC     Bacterial small subunit ribosomal RNA
STATES   4758
NODES    1197
CLEN     1533
W        1614
ALPH     RNA
RF       no
CONS     yes
MAP      yes
DATE     Mon Jan 29 03:19:39 2018
COM      [1] /usr/lib/infernal/cmbuild RF00177.seed.sto RF00177.seed
COM      [2] /usr/lib/infernal/cmcalibrate --cpu 20 RF00177.seed.cm
PBEGIN   0.05
PEND     0.05
WBETA    1e-07
QDBBETA1 1e-07
QDBBETA2 1e-15
N2OMEGA  1.52588e-05
N3OMEGA  1.52588e-05
ELSELF   -0.08926734
NSEQ     99
EFFN     1.211517
CKSUM    2093381478
NULL     0.000  0.000  0.000  0.000 
GA       50.00
TC       50.00
NC       49.90
EFP7GF   -64.8752 0.69565
ECMLC    0.73722    -8.18519    -0.75556     1600000      287021  0.004181
ECMGC    0.06157  -327.82681  -314.36942     1600000         916  0.436681
ECMLI    0.74522    -7.73085    -0.46568     1600000      269471  0.004453
ECMGI    0.06634  -224.15868  -211.57094     1600000         922  0.433839
                                             [ ROOT    0 ]      -      - - - - -
     S     0    -1 0     1     4     0     1  1614  1738  -6.619  -6.826  -0.114  -4.139                 
    IL     1     1 2     1     4  1270  1366  1616  1740  -1.686  -2.369  -1.117  -4.855                  0.000  0.000  0.000  0.000 
    IR     2     2 3     2     3  1270  1366  1616  1740  -1.442  -0.798  -4.142                          0.000  0.000  0.000  0.000 

```



## Infernal manuals





### Get CM file from msafile using cmbuild


#### Run cmbuild

take the example of tRNAs
```
$ cmbuild test/tRNA5.cm  test/tRNA5.sto 
# cmbuild :: covariance model construction from multiple sequence alignments
# INFERNAL 1.1.2 (July 2016)
# Copyright (C) 2016 Howard Hughes Medical Institute.
# Freely distributed under a BSD open source license.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CM file:                                            test/tRNA5.cm
# alignment file:                                     test/tRNA5.sto
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                                                                      rel entropy
#                                                                      -----------
# idx    name                     nseq eff_nseq   alen  clen  bps bifs    CM   HMM description
# ------ -------------------- -------- -------- ------ ----- ---- ---- ----- ----- -----------
       1 tRNA5                       5     3.73     74    72   21    2 0.783 0.489 
#
# CPU time: 0.45u 0.00s 00:00:00.45 Elapsed: 00:00:00.52
```

### cmcalibrate

#### Parameters for cmcalibrate
```
$ cmcalibrate --help
Failed to parse command line: No such option "--help".
Usage: cmcalibrate [-options] <cmfile>

where basic options are:
  -h     : show brief help on version and usage
  -L <x> : set random seq length to search in Mb to <x>  [1.6]  (0.01<=x<=160.)

To see more help on available options, do cmcalibrate -h
```

#### Run cmcalibrate
```
$ cmcalibrate --forecast test/tRNA5.cm
# cmcalibrate :: fit exponential tails for CM E-values
# INFERNAL 1.1.2 (July 2016)
# Copyright (C) 2016 Howard Hughes Medical Institute.
# Freely distributed under a BSD open source license.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CM file:                                     test/tRNA5.cm
# forecast mode (no calibration):              on
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Forecasting running time for CM calibration(s) on 40 cpus:
#
#                          predicted
#                       running time
# model name            (hr:min:sec)
# --------------------  ------------
  tRNA5                     00:00:46
#
# CPU time: 0.20u 0.00s 00:00:00.20 Elapsed: 00:00:00.22
[ok]
```


### Run cmsearch to search target sequence in genome

```
$ cmsearch /home/wzk/database/Bacterial_genome/infernal_test/RF00177.seed.cm  /home/wzk/database/Bacterial_genome/species/GCF_900241005.1_PRJEB22714_genomic.fna > test_result
```


output file:
```
# cmsearch :: search CM(s) against a sequence database
# INFERNAL 1.1.1 (July 2014)
# Copyright (C) 2014 Howard Hughes Medical Institute.
# Freely distributed under the GNU General Public License (GPLv3).
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# query CM file:                         /home/wzk/database/Bacterial_genome/seeds/RF00177.seed.cm
# target sequence database:              /home/wzk/database/Bacterial_genome/Bacteria_16S/species_temp/GCF_900251075.1_M3095_genomic.fna
# number of worker threads:              40
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Query:       SSU_rRNA_bacteria  [CLEN=1533]
Accession:   RF00177
Description: Bacterial small subunit ribosomal RNA
Hit scores:
 rank     E-value  score  bias  sequence           start    end   mdl trunc   gc  description
 ----   --------- ------ -----  ----------------- ------ ------   --- ----- ----  -----------
  (1) !         0 1632.1   1.8  NZ_OGBY01000003.1     49   1600 +  cm    no 0.51  Staphylococcus aureus strain M3095 isolate M3095, whole geno
  (2) !   9.2e-17   60.3   0.0  NZ_OGBY01000041.1    284    223 -  cm    5' 0.53  Staphylococcus aureus strain M3095 isolate M3095, whole geno
  (3) !   9.8e-11   41.6   0.0  NZ_OGBY01000027.1     50      1 -  cm    3' 0.54  Staphylococcus aureus strain M3095 isolate M3095, whole geno
  (4) !   1.3e-05   25.8   0.0  NZ_OGBY01000006.1 179423 179457 +  cm    3' 0.46  Staphylococcus aureus strain M3095 isolate M3095, whole geno

Hit alignments:
>> NZ_OGBY01000003.1  Staphylococcus aureus strain M3095 isolate M3095, whole genome shotgun sequence
 rank     E-value  score  bias mdl mdl from   mdl to       seq from      seq to       acc trunc   gc
 ----   --------- ------ ----- --- -------- --------    ----------- -----------      ---- ----- ----
  (1) !         0 1632.1   1.8  cm        1     1533 []          49        1600 + .. 0.99    no 0.51

                                                                                              v    v                NC
                         ::::::::<<<<<_______>>>>>,{{{{-{{{{{{,{{{{{{{{{----{{{-{{{,,<<<--<<<<<-...<<<<<<<____>>>>> CS
  SSU_rRNA_bacteria    1 uuuauggAGaGuuUGAUCcUggCuCAGggcGaaCGCuGGCGGcgcGcuUaAcaCAuGCAAGuCGagcccca...cggggccuuaaggccc 87  
                         UUUAUGGAGAGUUUGAUCCUGGCUCAGG::GAACGCUGGCGGCG:GC+UAA:ACAUGCAAGUCGAGC::      G:G::: U++:::C:
  NZ_OGBY01000003.1   49 UUUAUGGAGAGUUUGAUCCUGGCUCAGGAUGAACGCUGGCGGCGUGCCUAAUACAUGCAAGUCGAGCGAACggaCGAGAAGCUUGCUUCU 138 
                         ********************************************************************8866888999999999999999 PP

                          v    v                       v                              v                v            NC
                         >>...->>->>>>>>,,,,,,[[[,,,,,,((((((((--((---(((((((,<<<<----<<<<<<<____>>>>>>>----->>>>,, CS
  SSU_rRNA_bacteria   88 cg...agggggcGgCGaAcGGGuGAGUAAcgCGcgggcAAccUacCcccgggugcgGgAUAccccccgGAAAcggggggUAAUACcgcAU 174 
                         C      :+:GCGGCG ACGGGUGAGUAAC CG:GG::AACCUACC:::::G+::GGGAUA C: C:GGAAAC:G :G UAAUACC::AU
  NZ_OGBY01000003.1  139 CUgau-GUUAGCGGCGGACGGGUGAGUAACACGUGGAUAACCUACCUAUAAGACUGGGAUAACUUCGGGAAACCGGAGCUAAUACCGGAU 227 
                         98774.555********************************************************************************* PP

                                                                                           v                        NC
                         ,,,<<<<<<<<<<____>>>>>>>>>.>,,,,<<<...._____>>>,)))))))--))))))))))<<<--<-<<<--<<<<<<<<___ CS
  SSU_rRNA_bacteria  175 aaugccccggcccguaugggccgggg.cuAAAGgc....auuuagcCGcccgggGAugggcccgCGccccAUcAGcuAGuuGGuggGGUA 259 
                         AAU:::::G::CCG+AUGG::C:::: : AAAG:C    +U ++G:C C:::::GAUGG::CC:CG ::CAU:AGCUAGUUGGU::GGUA
  NZ_OGBY01000003.1  228 AAUAUUUUGAACCGCAUGGUUCAAAAgUGAAAGACggucUUGCUGUCACUUAUAGAUGGAUCCGCGCUGCAUUAGCUAGUUGGUAAGGUA 317 
                         **********************9765389*******97555555********************************************** PP
```

### Align the sequence derived from cmsearch

If we had the CM file **tRNA5.c.cm**, and we also got the seqeunce file **mrum-tRNAs10.fa**
form based on this CM file using **cmsearch**. Now we can align the sequence using **cmalign** basd on this CM file.

input fasta file 

```
$ head mrum-tRNAs10.fa
>mrum-tRNA.1
GGAGCUAUAGCUCAAUGGCAGAGCGUUUGGCUGACAUCCAAAAGGUUAUGGGUUCGAUUC
CCUUUAGCCCCA
>mrum-tRNA.2
GGGCCCGUAGCUCAGUUGGGAGAGCGCUGCCCUUGCAAGGCAGAGGCCCCGGGUUCAAAU
CCCGGUGGGUCCA
>mrum-tRNA.3
GGGCCCAUAGCUUAGCCAGGUAGAGCGCUCGGCUCAUAACCGGGAUGUCAUGGGUUCGAA
UCCCAUUGGGCCCA
```

```
$ cmalign tRNA5.c.cm mrum-tRNAs10.fa > mrum-tRNAs10.out

$ head mrum-tRNAs10.out
# STOCKHOLM 1.0
#=GF AU Infernal 1.1.2

mrum-tRNA.1          GGAGCUAUAGCUCAAU..GGC..AGAGCGUUUGGCUGACAU........................................CCAAAAGGUUAUGGGUUCGAUUCCCUUUAGCCCCA
#=GR mrum-tRNA.1  PP ****************..***..******************........................................***********************************
mrum-tRNA.2          GGGCCCGUAGCUCAGU.uGGG..AGAGCGCUGCCCUUGCAA........................................GGCAGAGGCCCCGGGUUCAAAUCCCGGUGGGUCCA
#=GR mrum-tRNA.2  PP ****************.****..******************........................................***********************************
mrum-tRNA.3          GGGCCCAUAGCUUAGCcaGGU..AGAGCGCUCGGCUCAUAA........................................CCGGGAUGUCAUGGGUUCGAAUCCCAUUGGGCCCA
#=GR mrum-tRNA.3  PP *********************..******************........................................***********************************
mrum-tRNA.4          AGGCUAGUGGCACAGCcuGGU.cAGCGCGCACGGCUGAUAA........................................CCGUGAGGUCCUGGGUUCGAAUCCCAGCUAGCCUA
```


#### Now we can re-build CM file based on the file **mrum-tRNAs10.out**

```
$ cmbuild mrum-tRNAs10.cm mrum-tRNAs10.out

# cmbuild :: covariance model construction from multiple sequence alignments
# INFERNAL 1.1.2 (July 2016)
# Copyright (C) 2016 Howard Hughes Medical Institute.
# Freely distributed under a BSD open source license.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CM file:                                            mrum-tRNAs10.cm
# alignment file:                                     mrum-tRNAs10.out_201807
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                                                                      rel entropy
#                                                                      -----------
# idx    name                     nseq eff_nseq   alen  clen  bps bifs    CM   HMM description
# ------ -------------------- -------- -------- ------ ----- ---- ---- ----- ----- -----------
       1 mrum-tRNAs10               10     3.15    116    74   21    2 0.762 0.486 
#
# CPU time: 0.47u 0.00s 00:00:00.47 Elapsed: 00:00:00.50
```




## Search genome based on Rfam CM files

### Download all Rfam seeds
```
$ wget ftp://ftp.ebi.ac.uk/pub/databases/Rfam/14.0/Rfam.cm.gz
$ gunzip Rfam.cm.gz
```

### Stats for all CM files

```
$ cmstat Rfam.cm | head -n 15
# cmstat :: display summary statistics for CMs
# INFERNAL 1.1.1 (July 2014)
# Copyright (C) 2014 Howard Hughes Medical Institute.
# Freely distributed under the GNU General Public License (GPLv3).
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                                                                                              rel entropy
#                                                                                             ------------
# idx   name                  accession      nseq  eff_nseq   clen      W   bps  bifs  model     cm    hmm
# ----  --------------------  ---------  --------  --------  -----  -----  ----  ----  -----  -----  -----
     1  5S_rRNA               RF00001         712      7.35    119    194    34     1     cm  0.590  0.370
     2  5_8S_rRNA             RF00002          61      3.62    154    203    25     3     cm  0.590  0.471
     3  U1                    RF00003         100      4.43    166    197    40     3     cm  0.590  0.390
     4  U2                    RF00004         208      5.46    193    229    45     4     cm  0.590  0.398
     5  tRNA                  RF00005         954     67.04     71    259    21     2     cm  0.793  0.453
     6  Vault                 RF00006          73      4.46    101    302    19     0     cm  0.590  0.469

```

### Fetch one certain CM file 
Based on all CM files, we can fetch one CM file based on the accession number from all CM files.

```
$ cmfetch Rfam.cm RF00001 | head -n 20
INFERNAL1/a [1.1.1 | July 2014]
NAME     5S_rRNA
ACC      RF00001
STATES   366
NODES    91
CLEN     119
W        194
ALPH     RNA
RF       no
CONS     yes
MAP      yes
DATE     Thu Apr 10 16:29:08 2014
COM      [1] /nfs/production/xfam/rfam/software/bin/cmbuild -F CM SEED
COM      [2] /nfs/production/xfam/rfam/software/bin/cmcalibrate --mpi CM
PBEGIN   0.05
PEND     0.05
WBETA    1e-07
QDBBETA1 1e-07
QDBBETA2 1e-15
N2OMEGA  1.52588e-05
```

### Get sequence from CM file

```
$ cmemit RF00001.cm | head -n 10
>5S_rRNA-sample1
AAUACACCAUGCGGCGUAAAUGCACUAGACCUCAUUAUGGCCUUUACGGCUAAGCAUGCC
UGUCUCAGCGGACUAGUGAGAUGGGUGGUCACAGGGGGUCG
>5S_rRNA-sample2
GAUGAUGGCUAGAGAGCCACUUAAGCUCCUAAACACAUGACGUACUUAGUAGCUAACACU
GGCACCGAUAUGGGAGUACCACGAUUGUCUUCAGACUGGGAACAUAUAUAGCUAUUUGGC
A
>5S_rRNA-sample3
UCUUGUAGCCAUGCCGGUUAGGAAGCACCCGAUCUCGUUUGAAAUCGGUAGUUAAGUAAU
CUUGGAUGCCUGGUAUGUCGCUCCGUGAUGCUCAGCGAACUGGCCAAUGCUACAGUAC
```


### Compress all CM files
The **cmscan** program has to read a lot of CMs and their filter HMMs in a hurry, and Infernal’s ASCII flatfiles
are bulky. To accelerate this, **cmscan** uses binary compression and indexing of the flatfiles. To use **cmscan**, 
you must first compress and index your CM database with the **cmpress** program:

```
$ cmpress Rfam.cm
Working...    done.
Pressed and indexed 2686 CMs and p7 HMM filters (2686 names and 2686 accessions).
Covariance models and p7 filters pressed into binary file:  Rfam.cm.i1m
SSI index for binary covariance model file:                 Rfam.cm.i1i
Optimized p7 filter profiles (MSV part)  pressed into:      Rfam.cm.i1f
Optimized p7 filter profiles (remainder) pressed into:      Rfam.cm.i1p
```

output four files:
```
Rfam.cm.i1f
Rfam.cm.i1i
Rfam.cm.i1m
Rfam.cm.i1p
```


### Run cmscan
```
$ cmscan -Z 20000 Rfam.cm /home/wzk/database/Bacterial_genome/Bacteria_16S/species_temp/GCF_000350085.1_ASM35008v1_genomic.fna > GCF_000350085.1_ASM35008v1_genomic.cmscan
```

output file:
```
# cmscan :: search sequence(s) against a CM database
# INFERNAL 1.1.1 (July 2014)
# Copyright (C) 2014 Howard Hughes Medical Institute.
# Freely distributed under the GNU General Public License (GPLv3).
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# query sequence file:                   /home/wzk/database/Bacterial_genome/Bacteria_16S/species_temp/GCF_000350085.1_ASM35008v1_genomic.fna
# target CM database:                    Rfam.cm
# database size is set to:               1000.0 Mb
# number of worker threads:              40
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Query:       NZ_CAUM01000191.1  [L=72994]
Description: Mesorhizobium metallidurans STM 2683, whole genome shotgun sequence
Hit scores:
 rank     E-value  score  bias  modelname    start    end   mdl trunc   gc  description
 ----   --------- ------ -----  ----------- ------ ------   --- ----- ----  -----------
  (1) !   5.1e-05   43.4   0.0  Intron_gpII  15628  15530 -  cm    no 0.65  -
 ------ inclusion threshold ------
  (2) ?     0.027   33.7   0.0  ar14         48418  48530 +  cm    no 0.62  -
  (3) ?       1.4   24.7   0.0  HIV_FS2      26111  26148 +  cm    no 0.55  -
  (4) ?       1.9   21.9   0.0  EAV_LTH      24018  23979 -  cm    no 0.65  -
  (5) ?       8.9   22.3   0.0  TB9Cs1H1     31773  31831 +  cm    no 0.66  -


```

All targeted results associated with rRNA
```
$ grep '!' GCF_000350085.1_ASM35008v1_genomic.cmscan | grep rRNA
  (1) !         0 2803.2  32.8  LSU_rRNA_bacteria        3062   5859 +  cm    no 0.53  -
  (2) !         0 1861.1  32.7  LSU_rRNA_archaea         3060   5859 +  cm    no 0.53  -
  (3) !         0 1575.1  14.7  SSU_rRNA_bacteria         765   2249 +  cm    no 0.56  -
  (4) !         0 1231.6  31.7  LSU_rRNA_eukarya         3275   5847 +  cm    no 0.54  -
  (5) !         0 1080.3  15.8  SSU_rRNA_archaea          770   2247 +  cm    no 0.56  -
  (6) !  8.1e-229  758.4  16.3  SSU_rRNA_microsporidia    770   2244 +  cm    no 0.56  -
  (7) !  6.1e-214  719.1  16.3  SSU_rRNA_eukarya          770   2244 +  cm    no 0.56  -
  (8) !     6e-14   77.3   0.0  5S_rRNA                  5956   6070 +  cm    no 0.63  -
 (12) !   7.9e-06   38.1   0.0  5_8S_rRNA                3075   3219 +  cm    no 0.52  -
```


