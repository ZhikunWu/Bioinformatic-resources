## minimap2

### install minimap2
```
$ conda install -c bioconda minimap2
```

### minimap2 parameters
```
$ minimap2
Usage: minimap2 [options] <target.fa>|<target.idx> [query.fa] [...]
Options:
  Indexing:
    -H           use homopolymer-compressed k-mer
    -k INT       k-mer size (no larger than 28) [15]
    -w INT       minizer window size [10]
    -I NUM       split index for every ~NUM input bases [4G]
    -d FILE      dump index to FILE []
  Mapping:
    -f FLOAT     filter out top FLOAT fraction of repetitive minimizers [0.0002]
    -g NUM       stop chain enlongation if there are no minimizers in INT-bp [5000]
    -G NUM       max intron length (effective with -xsplice; changing -r) [200k]
    -F NUM       max fragment length (effective with -xsr or in the fragment mode) [800]
    -r NUM       bandwidth used in chaining and DP-based alignment [500]
    -n INT       minimal number of minimizers on a chain [3]
    -m INT       minimal chaining score (matching bases minus log gap penalty) [40]
    -X           skip self and dual mappings (for the all-vs-all mode)
    -p FLOAT     min secondary-to-primary score ratio [0.8]
    -N INT       retain at most INT secondary alignments [5]
  Alignment:
    -A INT       matching score [2]
    -B INT       mismatch penalty [4]
    -O INT[,INT] gap open penalty [4,24]
    -E INT[,INT] gap extension penalty; a k-long gap costs min{O1+k*E1,O2+k*E2} [2,1]
    -z INT[,INT] Z-drop score and inversion Z-drop score [400,200]
    -s INT       minimal peak DP alignment score [80]
    -u CHAR      how to find GT-AG. f:transcript strand, b:both strands, n:don't match GT-AG [n]
  Input/Output:
    -a           output in the SAM format (PAF by default)
    -Q           don't output base quality in SAM
    -L           write CIGAR with >65535 ops at the CG tag
    -R STR       SAM read group line in a format like '@RG\tID:foo\tSM:bar' []
    -c           output CIGAR in PAF
    --cs[=STR]   output the cs tag; STR is 'short' (if absent) or 'long' [none]
    -Y           use soft clipping for supplementary alignments
    -t INT       number of threads [3]
    -K NUM       minibatch size for mapping [500M]
    --version    show version number
  Preset:
    -x STR       preset (always applied before other options) []
                 map-pb: -Hk19 (PacBio vs reference mapping)
                 map-ont: -k15 (Oxford Nanopore vs reference mapping)
                 asm5: -k19 -w19 -A1 -B19 -O39,81 -E3,1 -s200 -z200 (asm to ref mapping; break at 5% div.)
                 asm10: -k19 -w19 -A1 -B9 -O16,41 -E2,1 -s200 -z200 (asm to ref mapping; break at 10% div.)
                 ava-pb: -Hk19 -Xw5 -m100 -g10000 --max-chain-skip 25 (PacBio read overlap)
                 ava-ont: -k15 -Xw5 -m100 -g10000 --max-chain-skip 25 (ONT read overlap)
                 splice: long-read spliced alignment (see minimap2.1 for details)
                 sr: short single-end reads without splicing (see minimap2.1 for details)

See `man ./minimap2.1' for detailed description of command-line options.

```


### minimap2 alignment

```
$ minimap2 -MD -a -t 10 /home/wzk/database/GENOME/human/Homo_sapiens.GRCh38.fa /disk1/Project/KC2018-C128/PRJEB26791/raw/*fastq.gz > mapping/ERR2631603.sam
[M::mm_idx_gen::79.766*1.64] collected minimizers
[M::mm_idx_gen::86.712*2.26] sorted minimizers
[M::main::86.712*2.26] loaded/built the index for 194 target sequence(s)
[M::mm_mapopt_update::89.938*2.22] mid_occ = 705
[M::mm_idx_stat] kmer size: 15; skip: 10; is_hpc: 0; #seq: 194
[M::mm_idx_stat::91.231*2.20] distinct minimizers: 100159079 (38.79% are singletons); average occurrences: 5.540; average spacing: 5.586
[M::worker_pipeline::93.309*2.32] mapped 1000 sequences
[M::worker_pipeline::95.681*2.45] mapped 1000 sequences
[M::main] Version: 2.9-r720
[M::main] CMD: minimap2 -MD -a -t 10 /home/wzk/database/GENOME/human/Homo_sapiens.GRCh38.fa /disk1/Project/KC2018-C128/PRJEB26791/raw/ERR2631603-1.fastq.gz /disk1/Project/KC2018-C128/PRJEB26791/raw/ERR2631603-2.fastq.gz
[M::main] Real time: 95.830 sec; CPU: 234.652 sec

```


