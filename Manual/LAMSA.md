
## [LAMSA](https://github.com/hitbc/LAMSA): Long Approximate Matches-based Split Aligner

### install LAMSA
```
git clone https://github.com/hitbc/LAMSA.git
cd LAMSA; make
```



### lamsa index
```
$ /home/wuzhikun/anaconda3/envs/NanoSV/bin/LAMSA/lamsa index

Usage:   lamsa index <ref.fa>
                     bulid BWT and GEM index for ref.fa
```



```
$ ./lamsa index  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa
[bwt_index] Building bwt-index for genome...
[BWTIncCreate] textLength=497912844, availableWord=47034604
[BWTIncConstructFromPacked] 10 iterations done. 76325452 characters processed.
[BWTIncConstructFromPacked] 20 iterations done. 142216380 characters processed.
[BWTIncConstructFromPacked] 30 iterations done. 200776364 characters processed.
[BWTIncConstructFromPacked] 40 iterations done. 252820604 characters processed.
[BWTIncConstructFromPacked] 50 iterations done. 299073676 characters processed.
[BWTIncConstructFromPacked] 60 iterations done. 340179500 characters processed.
[BWTIncConstructFromPacked] 70 iterations done. 376710428 characters processed.
[BWTIncConstructFromPacked] 80 iterations done. 409175164 characters processed.
[BWTIncConstructFromPacked] 90 iterations done. 438025868 characters processed.
[BWTIncConstructFromPacked] 100 iterations done. 463664428 characters processed.
[BWTIncConstructFromPacked] 110 iterations done. 486447996 characters processed.
[bwt_gen] Finished constructing BWT in 116 iterations.
[bwt_index] Building done!
[lamsa_index] Executing gem-indexer ... done!

```

output files:
```
-rw-rw-r-- 1 2.5K Mar 21 15:54 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.amb
-rw-rw-r-- 1   35 Mar 21 15:54 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.ann
-rw-rw-r-- 1 238M Mar 21 15:54 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.bwt
-rw-rw-r-- 1 660M Mar 21 16:06 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.gem
-rw-rw-r-- 1  60M Mar 21 15:54 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.pac
-rw-rw-r-- 1 119M Mar 21 15:55 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.sa

```



### lamsa aln
```
$ /home/wuzhikun/anaconda3/envs/NanoSV/bin/LAMSA/lamsa aln

Usage:   lamsa aln [options] <ref.fa> <read.fa/fq>

Algorithm options:

    -t --thread    [INT]    Number of threads. [1]
    -l --seed-len  [INT]    Length of seeding fragments. [50]
    -i --seed-inv  [INT]    Distance between neighboring seeding fragments. [100]
    -p --max-loci  [INT]    Maximum allowed number of seeding fragments' hits. [200]
    -V --SV-len    [INT]    Expected maximum length of SV. [10000]
    -v --ovlp-rat  [FLOAT]  Minimum overlapping ratio to cluster two skeletons or alignment records.
                            [0.70]
    -s --max-skel  [INT]    Maximum number of skeletons that are reserved in a cluster. [10]
    -R --max-reg   [INT]    Maximum allowed length of unaligned read part to trigger a bwt-based query.
                            [300]
    -k --bwt-kmer  [INT]    Length of BWT-seed. [19]
    -f --fastest            Use GEM-mapper's fastest mode(--fast-mapping=0). [false]

Scoring options:

    -m --match-sc  [INT]    Match score for SW-alignment. [1]
    -M --mis-pen   [INT]    Mismatch penalty for SW-alignment. [3]
    -O --open-pen  [INT(,INT,INT,INT)]
                            Gap open penalty for SW-alignment(end2end-global: insertion, deletion,
                            one-end-extend: insertion, deletion). [5(,5,5,5)]
    -E --ext-pen   [INT(,INT,INT,INT)]
                            Gap extension penalty for SW-alignment(end2end-global: insertion, deletion,
                            one-end-extend: insertion, deletion). [2(,2,2,2)]
    -w --band-width[INT]    Band width for banded-SW. [10]
    -b --end-bonus [INT]    Penalty for end-clipping. [5]

Read options:

    -e --err-rate  [FLOAT]  Maximum error rate of read. [0.04]
    -d --diff-rate [FLOAT]  Maximum length difference ratio between read and reference. [0.04]
    -x --mis-rate  [FLOAT]  Maximum error rate of mismatch within reads. [0.04]

    -T --read-type [STR]    Specifiy the type of reads and set multiple parameters unless overriden.
                            [null] (Illumina Moleculo)
                            pacbio (PacBio SMRT): -i25 -l50 -m1 -M1 -O1,1,2,2 -E1,1,1,1 -w200 -b0 -e0.30 -d0.30
                            ont2d (Oxford Nanopore): -i25 -l50 -m1 -M1 -O1,1,1,1 -E1,1,1,1 -w100 -b0 -e0.25 -d0.10

Output options:

    -r --max-out   [INT]    Maximum number of output records for a specific split read region. [10]
    -g --gap-split [INT]    Minimum length of gap that causes a split-alignment. [100]
    -S --soft-clip          Use soft clipping for supplementary alignment. [false]
    -C --comment            Append FASTQ comment to SAM output. [false]
    -o --output    [STR]    Output file (SAM format). [stdout]

    -h --help               Print this short usage.
    -H --HELP               Print a detailed usage.

```

\

```
lamsa aln --thread 8 --read-type  ont2d --output out.sam reference.fa input.fastq
```