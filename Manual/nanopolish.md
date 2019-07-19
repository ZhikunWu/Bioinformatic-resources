

### nanopolish
```
nanopolish extract: extract reads in FASTA or FASTQ format from a directory of FAST5 files
nanopolish call-methylation: predict genomic bases that may be methylated
nanopolish variants: detect SNPs and indels with respect to a reference genome
nanopolish variants --consensus: calculate an improved consensus sequence for a draft genome assembly
nanopolish eventalign: align signal-level events to k-mers of a reference genome
```


### Indexing fastq from 1D Basecalling

In order to prepare our 1D fastq file for nanopolish (so that the tool can find the original raw files), we need to index the fastq files from the 1D basecalling again with nanopolish:

```
nanopolish index -d ~/workdir/Data/Nanopore/ ~/workdir/Results/1D_basecall.fastq
```


```
running install_scripts
running build_scripts
creating build/scripts-3.6
copying scripts/medaka_consensus -> build/scripts-3.6
copying scripts/medaka_variant -> build/scripts-3.6
error: file '/home/wuzhikun/anaconda3/envs/NanoSV/share/medaka/scripts/mini_align' does not exist



  - medaka
  - h5py==2.7.1
  - medaka
  - intervaltree[version='>=3.0.0']
  - medaka
  - keras==2.2.4
  - medaka
  - numpy==1.16.1
  - medaka
  - tensorflow==1.12.0
  - medaka
  - pyyaml==5.1
  - medaka
  - whatshap==0.18
  - libstdcxx-ng[version='>=7.3.0']
  - medaka
  - whatshap==0.18
  - xopen[version='>=0.5.0']
  - bz2file
```



