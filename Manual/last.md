## last

```
$ lastdb --help
Usage: lastdb [options] output-name fasta-sequence-file(s)
Prepare sequences for subsequent alignment with lastal.

Main Options:
-h, --help: show all options and their default settings, and exit
-p: interpret the sequences as proteins
-R: repeat-marking options (default=10)
-c: soft-mask lowercase letters (in reference *and* query sequences)
-u: seeding scheme (default: YASS for DNA, else exact-match seeds)

Advanced Options (default settings):
-w: use initial matches starting at every w-th position in each sequence (1)
-W: use "minimum" positions in sliding windows of W consecutive positions (1)
-S: strand: 0=reverse, 1=forward, 2=both (1)
-s: volume size (unlimited)
-Q: input format: 0=fasta or fastq-ignore,
                  1=fastq-sanger, 2=fastq-solexa, 3=fastq-illumina (fasta)
-P: number of parallel threads (1)
-m: seed pattern
-a: user-defined alphabet
-i: minimum limit on initial matches per query position (0)
-b: bucket depth
-C: child table type: 0=none, 1=byte-size, 2=short-size, 3=full (0)
-x: just count sequences and letters
-v: be verbose: write messages about what lastdb is doing
-V, --version: show version information, and exit

Report bugs to: last-align (ATmark) googlegroups (dot) com
LAST home page: http://last.cbrc.jp/

```

```
$ last-train --help
Usage: last-train [options] lastdb-name sequence-file(s)

Try to find suitable score parameters for aligning the given sequences.

Options:
  -h, --help           show this help message and exit
  -v, --verbose        show more details of intermediate steps

  Training options:
    --revsym           force reverse-complement symmetry
    --matsym           force symmetric substitution matrix
    --gapsym           force insertion/deletion symmetry
    --pid=PID          skip alignments with > PID% identity (default: 100)
    --postmask=NUMBER  skip mostly-lowercase alignments (default=1)
    --sample-number=N  number of random sequence samples (default: 500)
    --sample-length=L  length of each sample (default: 2000)

  Initial parameter options:
    -r SCORE           match score (default: 6 if Q>0, else 5)
    -q COST            mismatch cost (default: 18 if Q>0, else 5)
    -p NAME            match/mismatch score matrix
    -a COST            gap existence cost (default: 21 if Q>0, else 15)
    -b COST            gap extension cost (default: 9 if Q>0, else 3)
    -A COST            insertion existence cost
    -B COST            insertion extension cost

  Alignment options:
    -D LENGTH          query letters per random alignment (default: 1e6)
    -E EG2             maximum expected alignments per square giga
    -s STRAND          0=reverse, 1=forward, 2=both (default: 2 if DNA, else
                       1)
    -S NUMBER          score matrix applies to forward strand of: 0=reference,
                       1=query (default: 1)
    -C COUNT           omit gapless alignments in COUNT others with > score-
                       per-length
    -T NUMBER          type of alignment: 0=local, 1=overlap (default: 0)
    -m COUNT           maximum initial matches per query position (default:
                       10)
    -k STEP            use initial matches starting at every STEP-th position
                       in each query (default: 1)
    -P THREADS         number of parallel threads
    -Q NUMBER          input format: 0=fasta or fastq-ignore, 1=fastq-sanger
                       (default=fasta)

```