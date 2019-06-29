

## [Deepmod](https://github.com/WGLab/DeepMod)

### [Demo and Examples](https://github.com/WGLab/DeepMod/blob/master/docs/Reproducibility.md)

### [install DeepMod](https://github.com/WGLab/DeepMod/blob/master/docs/Install.md)

#### tools
```
$ tree bin/
bin/
├── DeepMod.py
└── scripts
    ├── __init__.py
    ├── myCom.py
    ├── myDetect.py
    ├── myGetFeatureBasedPos.py
    ├── myMultiBiRNN.py
    └── __pycache__
        ├── __init__.cpython-37.pyc
        └── myCom.cpython-37.pyc

```




```
$ tree tools/
tools/
├── cal_EcoliDetPerf_batch.py
├── cal_EcoliDetPerf.py
├── generate_motif_pos.py
├── hm_cluster_predict.py
└── sum_chr_mod.py

```


#### trained file
```
$ tree train_mod/
train_mod/
├── na12878_cluster_train_mod-keep_prob0.7-nb25-chr1
│   ├── Cg.cov5.nb25.data-00000-of-00001
│   ├── Cg.cov5.nb25.index
│   ├── Cg.cov5.nb25.meta
│   └── checkpoint
├── rnn_conmodA_E1m2wd21_f7ne1u0_4
│   ├── checkpoint
│   ├── mod_train_conmodA_E1m2wd21_f3ne1u0.data-00000-of-00001
│   ├── mod_train_conmodA_E1m2wd21_f3ne1u0.index
│   └── mod_train_conmodA_E1m2wd21_f3ne1u0.meta
├── rnn_conmodA_P100wd21_f7ne1u0_4
│   ├── checkpoint
│   ├── mod_train_conmodA_P100wd21_f3ne1u0.data-00000-of-00001
│   ├── mod_train_conmodA_P100wd21_f3ne1u0.index
│   └── mod_train_conmodA_P100wd21_f3ne1u0.meta
├── rnn_conmodC_P100wd21_f7ne1u0_4
│   ├── checkpoint
│   ├── mod_train_conmodC_P100wd21_f3ne1u0.data-00000-of-00001
│   ├── mod_train_conmodC_P100wd21_f3ne1u0.index
│   └── mod_train_conmodC_P100wd21_f3ne1u0.meta
├── rnn_f7_wd21_chr1to10_4
│   ├── checkpoint
│   ├── mod_train_f7_wd21_chr1to10.data-00000-of-00001
│   ├── mod_train_f7_wd21_chr1to10.index
│   └── mod_train_f7_wd21_chr1to10.meta
└── rnn_sinmodC_P100wd21_f7ne1u0_4
    ├── checkpoint
    ├── mod_train_sinmodC_P100wd21_f3ne1u0.data-00000-of-00001
    ├── mod_train_sinmodC_P100wd21_f3ne1u0.index
    └── mod_train_sinmodC_P100wd21_f3ne1u0.meta

```


### parameters
```
$ python bin/DeepMod.py --help
usage: DeepMod.py [-h] {detect,train,getfeatures} ...

Detect nucleotide modification from nanopore signals data.

positional arguments:
  {detect,train,getfeatures}
    detect              Detect modifications at a genomic scale
    train               Training a modification classifier
    getfeatures         Get features for all fast5 files

optional arguments:
  -h, --help            show this help message and exit

For example, 
 	python DeepMod.py train: Training a modification classifier.
 	python DeepMod.py detect: Detect modification by integrating all long reads. 
 	python DeepMod.py getfeatures: Get features for training a model. 
```


#### train
```
$ python bin/DeepMod.py train
Train
             Current directory: /home/wuzhikun/anaconda3/envs/NanoSV/bin/DeepMod
                      outLevel: 2
                       wrkBase: None
                        FileID: mod
                     outFolder: ./mod_output/
                     recursive: 1
              files_per_thread: 1000
                       threads: 4
                    windowsize: 21
                      alignStr: minimap2
                          fnum: 7
                        hidden: 100
                   outputlayer: 
                    unbalanced: 0
                       modfile: None
                          test: ['N', '100']
Please provide correct parameters
  The input folder is None.
usage: DeepMod.py [-h] {detect,train,getfeatures} ...

Detect nucleotide modification from nanopore signals data.

positional arguments:
  {detect,train,getfeatures}
    detect              Detect modifications at a genomic scale
    train               Training a modification classifier
    getfeatures         Get features for all fast5 files

optional arguments:
  -h, --help            show this help message and exit

For example, 
  python DeepMod.py train: Training a modification classifier.
  python DeepMod.py detect: Detect modification by integrating all long reads. 
  python DeepMod.py getfeatures: Get features for training a model.  
 
usage: DeepMod.py train [-h] [--outLevel {0,1,2,3}] [--wrkBase WRKBASE]
                        [--FileID FILEID] [--outFolder OUTFOLDER]
                        [--recursive {0,1}] [--threads THREADS]
                        [--files_per_thread FILES_PER_THREAD]
                        [--windowsize WINDOWSIZE] [--alignStr {bwa,minimap2}]
                        [--wrkBase2 WRKBASE2] [--fnum FNUM] [--hidden HIDDEN]
                        [--modfile MODFILE] [--test TEST]
                        [--outputlayer {,sigmoid}] [--unbalanced {1,0,None}]

Training a modification classifier

optional arguments:
  -h, --help            show this help message and exit
  --wrkBase2 WRKBASE2   The base folder for long reads without any modifications.
  --fnum FNUM           The number of features. Default: 7
  --hidden HIDDEN       The number of hidden node. Default: 100
  --modfile MODFILE     The path to load training model. Default: 'mod_output/'
  --test TEST           The number of E Coli genomic position for testing. Default: 'E,1,2'
  --outputlayer {,sigmoid}
                        how to put activation function for output layer
  --unbalanced {1,0,None}
                        Whether data is unbalanced

Common options.:
  --outLevel {0,1,2,3}  The level for output: 0 for DEBUG, 1 for INFO, 2 for WARNING, 3 for ERROR. Default: 2
  --wrkBase WRKBASE     The base folder for FAST5 files.
  --FileID FILEID       The unique string for intermediate files and final output files. Default: 'mod'
  --outFolder OUTFOLDER
                        The default folder for outputing the results. Default: ./mod_output
  --recursive {0,1}     Recurise to find fast5 files. Default:1
  --threads THREADS     The number of threads used (not for train). Default:4
  --files_per_thread FILES_PER_THREAD
                        The number of fast5 files for each thread (not for train). Default:500
  --windowsize WINDOWSIZE
                        The window size to extract features. Default: 51
  --alignStr {bwa,minimap2}
                        Alignment tools (bwa or minimap2 is supported). Default: minimap2

For example, 
 python DeepMod.py train --wrkBase umr --wrkBase2 sss --FileID mod_train --outFolder ./mod_output/train1 

```


#### detect modification
```
$ python DeepMod.py detect
No mod file is provided. The default one is used

Nanopore sequencing data analysis is resourece-intensive and time consuming. 
Some potential strong recommendations are below:
	If your reference genome is large as human genome and your Nanopore data is huge,
	It would be faster to run this program parallelly to speed up.
	You might run different input folders of your fast5 files and 
	give different output names (--FileID) or folders (--outFolder)
	A good way for this is to run different chromosome individually.

             Current directory: /home/wuzhikun/anaconda3/envs/NanoSV/bin/DeepMod/bin
                      outLevel: 2
                       wrkBase: None
                        FileID: mod
                     outFolder: ./mod_output/
                     recursive: 1
              files_per_thread: 1000
                       threads: 4
                    windowsize: 21
                      alignStr: minimap2
                   basecall_1d: Basecall_1D_000
              basecall_2strand: BaseCalled_template
                        ConUnk: True
                   outputlayer: 
                          Base: C
                   mod_cluster: 0
                       predDet: 1
                           Ref: None
                          fnum: 7
                        hidden: 100
                       modfile: train_mod/rnn_P90wd21_f53/mod_train_P90wd21_f53
                        region: [[None, None, None]]
Please provide correct parameters
	The input folder is None.
	 reference file does not exist (None)
	The meta file (train_mod/rnn_P90wd21_f53/mod_train_P90wd21_f53.meta) does not exist
usage: DeepMod.py [-h] {detect,train,getfeatures} ...

Detect nucleotide modification from nanopore signals data.

positional arguments:
  {detect,train,getfeatures}
    detect              Detect modifications at a genomic scale
    train               Training a modification classifier
    getfeatures         Get features for all fast5 files

optional arguments:
  -h, --help            show this help message and exit

For example, 
 	python DeepMod.py train: Training a modification classifier.
 	python DeepMod.py detect: Detect modification by integrating all long reads. 
 	python DeepMod.py getfeatures: Get features for training a model.  
 
usage: DeepMod.py detect [-h] [--outLevel {0,1,2,3}] [--wrkBase WRKBASE]
                         [--FileID FILEID] [--outFolder OUTFOLDER]
                         [--recursive {0,1}] [--threads THREADS]
                         [--files_per_thread FILES_PER_THREAD]
                         [--windowsize WINDOWSIZE] [--alignStr {bwa,minimap2}]
                         [--Ref REF] [--predDet {0,1}] [--predpath PREDPATH]
                         [--modfile MODFILE] [--fnum FNUM] [--hidden HIDDEN]
                         [--basecall_1d BASECALL_1D]
                         [--basecall_2strand BASECALL_2STRAND]
                         [--region REGION] [--ConUnk {False,True}]
                         [--outputlayer {,sigmoid}] [--Base {A,C,G,T}]
                         [--mod_cluster {0,1}]

Detect modifications by integrating all long reads for a genome

optional arguments:
  -h, --help            show this help message and exit
  --Ref REF             The reference sequence
  --predDet {0,1}       pred first and then detect (1) or only detect (0). Default: 1
  --predpath PREDPATH   The file path of predictions for each fast5 file. The file pattern is *_*.detail. Default: './mod_output/pred2/'
  --modfile MODFILE     The path to load training model. Default: 'mod_output/'
  --fnum FNUM           The number of features. Default: 7
  --hidden HIDDEN       The number of hidden node. Default: 100
  --basecall_1d BASECALL_1D
                        Path for basecall_1d. Default: Basecall_1D_000
  --basecall_2strand BASECALL_2STRAND
                        Path for basecall_2strand. Default: BaseCalled_template
  --region REGION       The region of interest: for example, chr:1:100000;chr2:10000
  --ConUnk {False,True}
                        Whether contain unknown chromosome
  --outputlayer {,sigmoid}
                        how to put activation function for output layer
  --Base {A,C,G,T}      Interest of bases
  --mod_cluster {0,1}   1: CpG cluster effect; 0: not

Common options.:
  --outLevel {0,1,2,3}  The level for output: 0 for DEBUG, 1 for INFO, 2 for WARNING, 3 for ERROR. Default: 2
  --wrkBase WRKBASE     The base folder for FAST5 files.
  --FileID FILEID       The unique string for intermediate files and final output files. Default: 'mod'
  --outFolder OUTFOLDER
                        The default folder for outputing the results. Default: ./mod_output
  --recursive {0,1}     Recurise to find fast5 files. Default:1
  --threads THREADS     The number of threads used (not for train). Default:4
  --files_per_thread FILES_PER_THREAD
                        The number of fast5 files for each thread (not for train). Default:500
  --windowsize WINDOWSIZE
                        The window size to extract features. Default: 51
  --alignStr {bwa,minimap2}
                        Alignment tools (bwa or minimap2 is supported). Default: minimap2

For example, 
 python DeepMod.py detect --wrkBase ctrl_oligo_SpeI_cut --FileID mod_det --outFolder ./mod_output/detect3 
```


### run deepmod
```
$ python /home/wuzhikun/anaconda3/envs/NanoSV/bin/DeepMod/bin/DeepMod.py detect --wrkBase /home/wuzhikun/data/RNA/Caenorhabditis_elegans/experiments/nanopore_datasets/L1/bio1/tech1/data/fast5/10  --Ref /home/wuzhikun/database/genome/wormbase/WBcel235/c_elegans.PRJNA13758.WS270.genomic.fa --outFolder /home/wuzhikun/data/RNA/Caenorhabditis_elegans/deepmod  --Base C --modfile /home/wuzhikun/anaconda3/envs/NanoSV/bin/DeepMod/train_mod/rnn_f7_wd21_chr1to10_4/mod_train_f7_wd21_chr1to10 --FileID L1_rep1 --threads 20

Nanopore sequencing data analysis is resourece-intensive and time consuming. 
Some potential strong recommendations are below:
	If your reference genome is large as human genome and your Nanopore data is huge,
	It would be faster to run this program parallelly to speed up.
	You might run different input folders of your fast5 files and 
	give different output names (--FileID) or folders (--outFolder)
	A good way for this is to run different chromosome individually.

             Current directory: /home/wuzhikun/data/RNA/Caenorhabditis_elegans
                      outLevel: 2
                       wrkBase: /home/wuzhikun/data/RNA/Caenorhabditis_elegans/experiments/nanopore_datasets/L1/bio1/tech1/data/fast5/10
                        FileID: L1_rep1
                     outFolder: /home/wuzhikun/data/RNA/Caenorhabditis_elegans/deepmod/
                     recursive: 1
              files_per_thread: 1000
                       threads: 20
                    windowsize: 21
                      alignStr: minimap2
                   basecall_1d: Basecall_1D_000
              basecall_2strand: BaseCalled_template
                        ConUnk: True
                   outputlayer: 
                          Base: C
                   mod_cluster: 0
                       predDet: 1
                           Ref: /home/wuzhikun/database/genome/wormbase/WBcel235/c_elegans.PRJNA13758.WS270.genomic.fa
                          fnum: 7
                        hidden: 100
                       modfile: /home/wuzhikun/anaconda3/envs/NanoSV/bin/DeepMod/train_mod/rnn_f7_wd21_chr1to10_4/mod_train_f7_wd21_chr1to10
                        region: [[None, None, None]]



[M::mm_idx_gen::3.326*1.29] collected minimizers
[M::mm_idx_gen::4.050*1.59] sorted minimizers
[M::main::4.050*1.59] loaded/built the index for 7 target sequence(s)
[M::mm_idx_gen::3.349*1.29] collected minimizers
[M::mm_mapopt_update::4.312*1.55] mid_occ = 95
[M::mm_idx_stat] kmer size: 15; skip: 10; is_hpc: 0; #seq: 7
[M::mm_idx_stat::4.462*1.54] distinct minimizers: 12514822 (80.90% are singletons); average occurrences: 1.505; average spacing: 5.325
[M::main] Version: 2.15-r905
[M::main] CMD: minimap2 -ax map-ont /home/wuzhikun/database/genome/wormbase/WBcel235/c_elegans.PRJNA13758.WS270.genomic.fa /tmp/tmp0r3xiyao.fa
[M::main] Real time: 4.525 sec; CPU: 6.912 sec; Peak RSS: 0.826 GB
Cur Prediction consuming time 34 for 0 1
[M::mm_idx_gen::4.086*1.60] sorted minimizers
[M::main::4.087*1.60] loaded/built the index for 7 target sequence(s)
[M::mm_idx_gen::3.288*1.30] collected minimizers
[M::mm_mapopt_update::4.343*1.56] mid_occ = 95
[M::mm_idx_stat] kmer size: 15; skip: 10; is_hpc: 0; #seq: 7
[M::mm_idx_stat::4.491*1.54] distinct minimizers: 12514822 (80.90% are singletons); average occurrences: 1.505; average spacing: 5.325
[M::main] Version: 2.15-r905
[M::main] CMD: minimap2 -ax map-ont /home/wuzhikun/database/genome/wormbase/WBcel235/c_elegans.PRJNA13758.WS270.genomic.fa /tmp/tmph5y243gs.fa
[M::main] Real time: 4.511 sec; CPU: 6.949 sec; Peak RSS: 0.833 GB
[M::mm_idx_gen::3.430*1.30] collected minimizers
Cur Prediction consuming time 34 for 0 3
[M::mm_idx_gen::4.009*1.60] sorted minimizers
[M::main::4.009*1.60] loaded/built the index for 7 target sequence(s)
[M::mm_mapopt_update::4.274*1.56] mid_occ = 95
[M::mm_idx_stat] kmer size: 15; skip: 10; is_hpc: 0; #seq: 7
[M::mm_idx_stat::4.427*1.54] distinct minimizers: 12514822 (80.90% are singletons); average occurrences: 1.505; average spacing: 5.325
[M::mm_idx_gen::4.181*1.60] sorted minimizers
[M::main::4.181*1.60] loaded/built the index for 7 target sequence(s)
[M::main] Version: 2.15-r905
[M::main] CMD: minimap2 -ax map-ont /home/wuzhikun/database/genome/wormbase/WBcel235/c_elegans.PRJNA13758.WS270.genomic.fa /tmp/tmpql4ynsur.fa
[M::main] Real time: 4.494 sec; CPU: 6.901 sec; Peak RSS: 0.837 GB
Cur Prediction consuming time 35 for 0 2
[M::mm_mapopt_update::4.444*1.57] mid_occ = 95
[M::mm_idx_stat] kmer size: 15; skip: 10; is_hpc: 0; #seq: 7
[M::mm_idx_stat::4.595*1.55] distinct minimizers: 12514822 (80.90% are singletons); average occurrences: 1.505; average spacing: 5.325
[M::main] Version: 2.15-r905
[M::main] CMD: minimap2 -ax map-ont /home/wuzhikun/database/genome/wormbase/WBcel235/c_elegans.PRJNA13758.WS270.genomic.fa /tmp/tmpp22xgj7x.fa
[M::main] Real time: 4.615 sec; CPU: 7.133 sec; Peak RSS: 0.837 GB
Cur Prediction consuming time 36 for 0 0
Error information for different fast5 files:
  No Fastq data 1998
  Cannot open fast5 or other errors 3
Per-read Prediction consuming time 52
Find: /home/wuzhikun/data/RNA/Caenorhabditis_elegans/deepmod//L1_rep1 0 rnn.pred.ind
[]
Genomic-position Detection consuming time 0

```


### Format of output

The output is in a BED format like below. The first six columns are Chr, Start pos, End pos, Base, Capped coverage, and Strand, and the last three columns are Real coverage, Mehylation percentage and Methylation coverage.

```
chr6 148655 148656 C 10 -  148655 148656 0,0,0 10 10 1
chr6 148657 148658 C 12 +  148657 148658 0,0,0 12 8 1
chr6 148674 148675 C 14 -  148674 148675 0,0,0 14 7 1
chr6 148675 148676 C 15 -  148675 148676 0,0,0 15 6 1
chr6 148676 148677 C 14 -  148676 148677 0,0,0 14 7 1
chr6 148684 148685 C 12 -  148684 148685 0,0,0 12 25 3
chr6 148685 148686 C 16 -  148685 148686 0,0,0 16 6 1
chr6 148689 148690 C 11 +  148689 148690 0,0,0 11 72 8
chr6 148691 148692 C 10 +  148691 148692 0,0,0 10 50 5
chr6 148693 148694 C 8 +  148693 148694 0,0,0 8 100 8
chr6 148694 148695 C 11 -  148694 148695 0,0,0 11 54 6
chr6 148695 148696 C 10 +  148695 148696 0,0,0 10 90 9
chr6 148697 148698 C 12 +  148697 148698 0,0,0 12 50 6
chr6 148699 148700 C 9 +  148699 148700 0,0,0 9 22 2
chr6 148701 148702 C 13 -  148701 148702 0,0,0 13 7 1
chr6 148703 148704 C 13 -  148703 148704 0,0,0 13 15 2
chr6 148706 148707 C 9 -  148706 148707 0,0,0 9 22 2
```