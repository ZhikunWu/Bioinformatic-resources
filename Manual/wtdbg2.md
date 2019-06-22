## [wtdbg2](https://github.com/ruanjue/wtdbg2)

### install wtdbg2

```
git clone https://github.com/ruanjue/wtdbg2
cd wtdbg2 && make
```

### parameters
```
$ wtdbg2
WTDBG: De novo assembler for long noisy sequences
Author: Jue Ruan <ruanjue@gmail.com>
Version: 2.4 (20190312)
Usage: wtdbg2 [options] -i <reads.fa> -o <prefix> [reads.fa ...]
Options:
 -i <string> Long reads sequences file (REQUIRED; can be multiple), []
 -o <string> Prefix of output files (REQUIRED), []
 -t <int>    Number of threads, 0 for all cores, [4]
 -f          Force to overwrite output files
 -x <string> Presets, comma delimited, []
            rsII/rs: -p 21 -S 4 -s 0.05 -L 5000
          sequel/sq
       nanopore/ont:
            (genome size < 1G)  -p 0 -k 15 -AS 2 -s 0.05 -L 5000
            (genome size >= 1G) -p 19 -AS 2 -s 0.05 -L 5000
      corrected/ccs: -p 21 -k 0 -AS 4 -K 0.05 -s 0.5
             Example: '-e 3 -x ont -S 1' in parsing order, -e will be 3, -S will be 1
 -g <number> Approximate genome size (k/m/g suffix allowed) [0]
 -X <float>  Choose the best <float> depth from input reads(effective with -g) [50]
 -L <int>    Choose the longest subread and drop reads shorter than <int> (5000 recommended for PacBio) [0]
             Negative integer indicate tidying read names too, e.g. -5000.
 -k <int>    Kmer fsize, 0 <= k <= 25, [0]
 -p <int>    Kmer psize, 0 <= p <= 25, [21]
             k + p <= 25, seed is <k-mer>+<p-homopolymer-compressed>
 -K <float>  Filter high frequency kmers, maybe repetitive, [1000.05]
             >= 1000 and indexing >= (1 - 0.05) * total_kmers_count
 -E <int>    Min kmer frequency, [2]
 -S <float>  Subsampling kmers, 1/(<-S>) kmers are indexed, [4.00]
             -S is very useful in saving memeory and speeding up
             please note that subsampling kmers will have less matched length
 -l <float>  Min length of alignment, [2048]
 -m <float>  Min matched length by kmer matching, [200]
 -R          Enable realignment mode
 -A          Keep contained reads during alignment
 -s <float>  Min similarity, calculated by kmer matched length / aligned length, [0.05]
 -e <int>    Min read depth of a valid edge, [3]
 -q          Quiet
 -v          Verbose (can be multiple)
 -V          Print version information and then exit
 --help      Show more options
```


### assemble long reads

```
$ wtdbg2 -i DM18A2084-B_unmapped.fq -o DM18A2084-B -t 20 -p 0 -k 15 -AS 2 -s 0.05 -L 5000
--
-- total memory      131579768.0 kB
-- available         112348536.0 kB
-- 24 cores
-- Starting program: wtdbg2 -i DM18A2084-B_unmapped.fq -o DM18A2084-B -t 20 -p 0 -k 15 -AS 2 -s 0.05 -L 5000
-- pid                      4240
-- date         Fri May 17 17:14:36 2019
--
[Fri May 17 17:14:36 2019] loading reads
50426 reads
[Fri May 17 17:14:41 2019] Done, 50426 reads (>=5000 bp), 1076287867 bp, 4179107 bins
** PROC_STAT(0) **: real 5.008 sec, user 4.970 sec, sys 0.790 sec, maxrss 354484.0 kB, maxvsize 504204.0 kB
[Fri May 17 17:14:41 2019] Set --edge-cov to 3
KEY PARAMETERS: -k 15 -p 0 -K 1000.049988 -A -S 2.000000 -s 0.050000 -g 0 -X 50.000000 -e 3 -L 5000
[Fri May 17 17:14:41 2019] generating nodes, 20 threads
[Fri May 17 17:14:41 2019] indexing bins[0,4179107] (1069851392 bp), 20 threads
[Fri May 17 17:14:41 2019] - scanning kmers (K15P0S2.00) from 4179107 bins
4179107 bins
********************** Kmer Frequency **********************
**********************     1 - 201    **********************
Quatiles:
   10%   20%   30%   40%   50%   60%   70%   80%   90%   95%
     2     8    29   106   343  1092  3354  9106 21889 52919
# If the kmer distribution is not good, please kill me and adjust -k, -p, and -K
# Cannot get a good distribution anyway, should adjust -S -s, also -A -e in assembly
** PROC_STAT(0) **: real 18.859 sec, user 158.650 sec, sys 29.410 sec, maxrss 1941872.0 kB, maxvsize 4663240.0 kB
[Fri May 17 17:14:55 2019] - high frequency kmer depth is set to 57832
[Fri May 17 17:14:55 2019] - Total kmers = 60532882
[Fri May 17 17:14:55 2019] - average kmer depth = 17
[Fri May 17 17:14:55 2019] - 35385767 low frequency kmers (<2)
[Fri May 17 17:14:55 2019] - 44 high frequency kmers (>57832)
[Fri May 17 17:14:55 2019] - indexing 25147071 kmers, 433382262 instances (at most)
4179107 bins
[Fri May 17 17:15:14 2019] - indexed  25147071 kmers, 432038645 instances
[Fri May 17 17:15:14 2019] - masked 2593 bins as closed
[Fri May 17 17:15:14 2019] - sorting
** PROC_STAT(0) **: real 39.431 sec, user 417.410 sec, sys 80.530 sec, maxrss 4057840.0 kB, maxvsize 7040020.0 kB
[Fri May 17 17:15:16 2019] Done
4000|341172
50425 reads|total hits 8682406
** PROC_STAT(0) **: real 928.441 sec, user 17207.380 sec, sys 504.080 sec, maxrss 8102124.0 kB, maxvsize 13089412.0 kB
[Fri May 17 17:30:04 2019] sorting rdhits ... Done
[Fri May 17 17:30:05 2019] clipping ... 2.12% bases
[Fri May 17 17:30:05 2019] generating regs ... 140883416
[Fri May 17 17:30:23 2019] sorting regs ...  Done
[Fri May 17 17:30:25 2019] generating intervals ...  1016621 intervals
[Fri May 17 17:30:26 2019] selecting important intervals from 1016621 intervals
[Fri May 17 17:30:35 2019] Intervals: kept 8557, discarded 1008064
** PROC_STAT(0) **: real 958.522 sec, user 17275.790 sec, sys 514.630 sec, maxrss 8102124.0 kB, maxvsize 15126268.0 kB
[Fri May 17 17:30:35 2019] Done, 8557 nodes
[Fri May 17 17:30:35 2019] output "DM18A2084-B.1.nodes". Done.
[Fri May 17 17:30:35 2019] median node depth = 13
[Fri May 17 17:30:35 2019] masked 133 high coverage nodes (>200 or <3)
[Fri May 17 17:30:35 2019] masked 650 repeat-like nodes by local subgraph analysis
[Fri May 17 17:30:35 2019] generating edges
[Fri May 17 17:30:35 2019] Done, 130910 edges
[Fri May 17 17:30:35 2019] output "DM18A2084-B.1.reads". Done.
[Fri May 17 17:30:35 2019] output "DM18A2084-B.1.dot.gz". Done.
[Fri May 17 17:30:35 2019] graph clean
[Fri May 17 17:30:35 2019] rescued 88 low cov edges
[Fri May 17 17:30:35 2019] deleted 988 binary edges
[Fri May 17 17:30:35 2019] deleted 1017 isolated nodes
[Fri May 17 17:30:35 2019] cut 3233 transitive edges
[Fri May 17 17:30:35 2019] output "DM18A2084-B.2.dot.gz". Done.
[Fri May 17 17:30:36 2019] 275 bubbles; 1514 tips; 12 yarns;
[Fri May 17 17:30:36 2019] deleted 412 isolated nodes
[Fri May 17 17:30:36 2019] output "DM18A2084-B.3.dot.gz". Done.
[Fri May 17 17:30:36 2019] cut 226 branching nodes
[Fri May 17 17:30:36 2019] deleted 23 isolated nodes
[Fri May 17 17:30:36 2019] building unitigs
[Fri May 17 17:30:36 2019] TOT 8364544, CNT 407, AVG 20552, MAX 196352, N50 37376, L50 64, N90 9472, L90 226, Min 1280
[Fri May 17 17:30:36 2019] output "DM18A2084-B.frg.nodes". Done.
[Fri May 17 17:30:36 2019] generating links
[Fri May 17 17:30:36 2019] generated 248 links
[Fri May 17 17:30:36 2019] output "DM18A2084-B.frg.dot.gz". Done.
[Fri May 17 17:30:36 2019] rescue 0 weak links
[Fri May 17 17:30:36 2019] deleted 24 binary links
[Fri May 17 17:30:36 2019] cut 27 transitive links
[Fri May 17 17:30:36 2019] remove 22 boomerangs
[Fri May 17 17:30:36 2019] detached 12 repeat-associated paths
[Fri May 17 17:30:36 2019] remove 56 weak branches
[Fri May 17 17:30:36 2019] cut 6 tips
[Fri May 17 17:30:36 2019] pop 1 bubbles
[Fri May 17 17:30:36 2019] cut 0 tips
[Fri May 17 17:30:36 2019] output "DM18A2084-B.ctg.dot.gz". Done.
[Fri May 17 17:30:36 2019] building contigs
[Fri May 17 17:30:36 2019] searched 329 contigs
[Fri May 17 17:30:36 2019] Estimated: TOT 8270080, CNT 220, AVG 37592, MAX 302592, N50 61440, L50 37, N90 16384, L90 135, Min 5120
[Fri May 17 17:30:38 2019] output 220 contigs
[Fri May 17 17:30:38 2019] Program Done
** PROC_STAT(TOTAL) **: real 962.451 sec, user 17307.760 sec, sys 517.460 sec, maxrss 8102124.0 kB, maxvsize 15126268.0 kB
---

```


output files:
```
-rw-rw-r-- 1 wuzhikun wuzhikun 2.0M May 17 17:30 DM18A2084-B.1.dot.gz
-rw-rw-r-- 1 wuzhikun wuzhikun  12M May 17 17:30 DM18A2084-B.1.nodes
-rw-rw-r-- 1 wuzhikun wuzhikun 5.6M May 17 17:30 DM18A2084-B.1.reads
-rw-rw-r-- 1 wuzhikun wuzhikun 230K May 17 17:30 DM18A2084-B.2.dot.gz
-rw-rw-r-- 1 wuzhikun wuzhikun 126K May 17 17:30 DM18A2084-B.3.dot.gz
-rw-rw-r-- 1 wuzhikun wuzhikun 1.6G May 17 17:30 DM18A2084-B.alignments.gz
-rw-rw-r-- 1 wuzhikun wuzhikun  998 May 17 17:15 DM18A2084-B.binkmer
-rw-rw-r-- 1 wuzhikun wuzhikun 129K May 17 17:15 DM18A2084-B.closed_bins
-rw-rw-r-- 1 wuzhikun wuzhikun 2.5M May 17 17:30 DM18A2084-B.clps
-rw-rw-r-- 1 wuzhikun wuzhikun  21K May 17 17:30 DM18A2084-B.ctg.dot.gz
-rw-rw-r-- 1 wuzhikun wuzhikun  34M May 17 17:30 DM18A2084-B.ctg.lay.gz
-rw-rw-r-- 1 wuzhikun wuzhikun  77K May 17 17:30 DM18A2084-B.events
-rw-rw-r-- 1 wuzhikun wuzhikun  22K May 17 17:30 DM18A2084-B.frg.dot.gz
-rw-rw-r-- 1 wuzhikun wuzhikun  51K May 17 17:30 DM18A2084-B.frg.nodes
-rw-rw-r-- 1 wuzhikun wuzhikun 675K May 17 17:14 DM18A2084-B.kmerdep

```


### derive consensus sequence

```
$ wtpoa-cns -t 24 -i DM18A2084-B.ctg.lay.gz -o DM18A2084-B.fa
--
-- total memory      131579768.0 kB
-- available         106567180.0 kB
-- 24 cores
-- Starting program: wtpoa-cns -t 24 -i DM18A2084-B.ctg.lay.gz -o DM18A2084-B.fa
-- pid                      7164
-- date         Fri May 17 17:40:55 2019
--

```


### other manuals
```
# polish consensus, not necessary if you want to polish the assemblies using other tools
minimap2 -t 16 -x map-pb -a prefix.ctg.fa reads.fa.gz | samtools view -Sb - >prefix.ctg.map.bam
samtools sort prefix.ctg.map.bam prefix.ctg.map.srt
samtools view prefix.ctg.map.srt.bam | ./wtpoa-cns -t 16 -d prefix.ctg.fa -i - -fo prefix.ctg.2nd.fa

# polish contigs using short reads
bwa mem -t 16 prefix.ctg.fa sr.1.fa sr.2.fa | samtools view -Sb - >sr.bam
samtools sort sr.bam sr.srt
samtools view sr.srt.bam | ./wtpoa-cns -t 16 -x sam-sr -d prefix.ctg.fa -i - -fo prefix.ctg.3rd.fa
```