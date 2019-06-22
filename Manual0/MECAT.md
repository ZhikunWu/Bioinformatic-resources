## manual for [MECAT](https://github.com/xiaochuanle/MECAT)
### install MECAT
```
git clone https://github.com/xiaochuanle/MECAT.git
cd MECAT
make 
cd ..
```
After installation, all the executables are found in MECAT/Linux-amd64/bin. 

### Install [HDF5](https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.15-patch1/src/):
```
wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.15-patch1/src/hdf5-1.8.15-patch1.tar.gz
tar xzvf hdf5-1.8.15-patch1.tar.gz
mkdir hdf5
cd hdf5-1.8.15-patch1
./configure --enable-cxx --prefix=/home/wzk/anaconda3/envs/meta3/bin/hdf5
make
make install
cd ..
```
The header files of HDF5 are in hdf5/include. The library files of HDF5 are in hdf5/lib (in some systems, they are put in hdf5/lib64, check it!).

### Install [dextract](https://github.com/PacificBiosciences/DEXTRACTOR)
```

git clone https://github.com/PacificBiosciences/DEXTRACTOR.git
cp MECAT/dextract_makefile DEXTRACTOR
cd DEXTRACTOR
echo "export HDF5_INCLUDE=/home/wzk/anaconda3/envs/meta3/bin/hdf5/include" >> ~/.bashrc
echo 'export HDF5_LIB=/home/wzk/anaconda3/envs/meta3/bin/hdf5/lib' >> ~/.bashrc
source ~/.bashrc
source activate meta3 (anaconda environment)
```
#### edit 'gdexta.c' to 'dexta.c' in dextract_makefile
```
make -f dextract_makefile
cd ..
```

### Add relative pathes
```
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/wzk/anaconda3/envs/meta3/bin/hdf5/lib' >> ~/.bashrc
export PATH=/home/wzk/anaconda3/envs/meta3/bin/MECAT/Linux-amd64/bin:$PATH
export PATH=/home/wzk/anaconda3/envs/meta3/bin/DEXTRACTOR:$PATH
source ~/.bashrc
source activate meta3
```


## Assemblying Pacbio
### download data
```
mkdir meta3_test %% cd meta3_test
wget http://gembox.cbcb.umd.edu/mhap/raw/ecoli_filtered.fastq.gz
gunzip ecoli_filtered.fastq.gz
```
###  using mecat2pw to detect overlapping candidates
```
mecat2pw -j 0 -d ecoli_filtered.fastq -o ecoli_filtered.fastq.pm.can -w wrk_dir -t 16
```
output files:
```
ecoli_filtered.fastq.pm.can
wrk_dir/
├── fileindex.txt
├── r_0
└── vol0
```
### correct the noisy reads based on their pairwise overlapping candidates.
```
mecat2cns -i 0 -t 8 ecoli_filtered.fastq.pm.can ecoli_filtered.fastq corrected_ecoli_filtered.fasta
```

## Assemblying Nanopore Data
```
mecat2cns -i 0 -t 8 ecoli_filtered.fastq.pm.can ecoli_filtered.fastq corrected_ecoli_filtered.fasta
```
output files:
```
corrected_ecoli_filtered.fasta
ecoli_filtered.fastq.pm.can.part0
ecoli_filtered.fastq.pm.can.partition_files
```
reads number after filting
```
$ grep -c '^@' ecoli_filtered.fastq
47910
(meta3) wzk@Dell-03 10:00:15 ^_^ /home/wzk/meta3_test 
$ grep -c '^>' corrected_ecoli_filtered.fasta
27568
```
###  extract the longest 25X corrected reads
```
extract_sequences corrected_ecoli_filtered.fasta corrected_ecoli_25x.fasta 4800000 25
```
output files:
```
corrected_ecoli_25x.fasta.fasta
corrected_ecoli_25x.fasta.fasta.qual
corrected_ecoli_25x.fasta.fasta.qv
corrected_ecoli_25x.fasta.frg

```


### assemble the longest 25X corrected reads using mecat2cacu
```
mecat2canu -trim-assemble -p ecoli -d ecoli genomeSize=4800000 ErrorRate=0.02 maxMemory=40 maxThreads=8 useGrid=0 Overlapper=mecat2asmpw -pacbio-corrected corrected_ecoli_25x.fasta.fasta
```
output files:
```
$ tree ecoli -L 1
ecoli
├── canu-logs/
├── canu-scripts/
├── ecoli.bubbles.fasta
├── ecoli.contigs.fasta
├── ecoli.gfa
├── ecoli.layout
├── ecoli.layout.readToTig
├── ecoli.layout.tigInfo
├── ecoli.trimmedReads.fastq
├── ecoli.unassembled.fasta
├── trimming/
├── trimming.html
├── unitigging/
└── unitigging.html
```






### download nanopore data 
```
mkdir nanopore
cd nanopore
wget http://nanopore.s3.climb.ac.uk/MAP006-PCR-1_2D_pass.fasta
```
### using mecat2pw to detect overlapping candidates
```
mecat2pw -j 0 -d MAP006-PCR-1_2D_pass.fasta -o candidates.txt -w wrk_dir -t 16 -x 1
```
output files:
```
candidates.txt
wrk_dir/
├── fileindex.txt
├── r_0
└── vol0

```
### correct the noisy reads based on their pairwise overlapping candidates.
```
mecat2pw -j 0 -d MAP006-PCR-1_2D_pass.fasta -o candidates.txt -w wrk_dir -t 16 -x 1
```

### extract the longest 25X corrected reads
```
 mecat2cns -i 0 -t 16 -x 1 candidates.txt MAP006-PCR-1_2D_pass.fasta corrected_ecoli.fasta
```
### extract the longest 25X corrected reads
```
output files:
```
candidates.txt.part0
candidates.txt.partition_files
corrected_ecoli.fasta
```

### extract the longest 25X corrected reads
```
extract_sequences corrected_ecoli.fasta corrected_ecoli_25x.fasta 4800000 25
```

output files:
```
corrected_ecoli_25x.fasta.fasta
corrected_ecoli_25x.fasta.fasta.qual
corrected_ecoli_25x.fasta.fasta.qv
corrected_ecoli_25x.fasta.frg
```


### assemble the longest 25X corrected reads using mecat2cacu
```
mecat2canu -trim-assemble -p ecoli -d ecoli genomeSize=4800000 ErrorRate=0.06 maxMemory=40 maxThreads=16 useGrid=0 Overlapper=mecat2asmpw -nanopore-corrected corrected_ecoli_25x.fasta.fasta
```
output files
```
$ tree ecoli/ -L 1
ecoli/
├── canu-logs
├── canu-scripts
├── ecoli.bubbles.fasta
├── ecoli.contigs.fasta
├── ecoli.gfa
├── ecoli.layout
├── ecoli.layout.readToTig
├── ecoli.layout.tigInfo
├── ecoli.trimmedReads.fastq
├── ecoli.unassembled.fasta
├── trimming
├── trimming.html
├── unitigging
└── unitigging.html

```

 




## Input Format
MECAT is capable of processing FASTA, FASTQ, and H5 format files. However, the H5 files must first be transfered to FASTA format by running DEXTRACTOR/dextract before running MECAT. For example:
```
find pathto/raw_reads -name "*.bax.h5" -exec readlink -f {} \; > reads.fofn
while read line; do   dextract -v $line >> reads.fasta ; done <  reads.fofn
```
