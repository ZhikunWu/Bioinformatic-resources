
## [ngmlr](https://github.com/philres/ngmlr)

### install ngmlr
```
$ conda install -c bioconda ngmlr
```

### ngmlr parameters
```
$ ngmlr --help
ngmlr 0.2.7 (build: Jul  2 2018 10:32:15, start: 2019-01-30.07:57:36)
Contact: philipp.rescheneder@univie.ac.at

Usage: ngmlr [options] -r <reference> -q <reads> [-o <output>]

Input/Output:
    -r <file>,  --reference <file>
        (required)  Path to the reference genome (FASTA/Q, can be gzipped)
    -q <file>,  --query <file>
        Path to the read file (FASTA/Q) [/dev/stdin]
    -o <string>,  --output <string>
        Adds RG:Z:<string> to all alignments in SAM/BAM [none]
    --skip-write
        Don't write reference index to disk [false]
    --bam-fix
        Report reads with > 64k CIGAR operations as unmapped. Required to be compatibel to BAM format [false]
    --rg-id <string>
        Adds RG:Z:<string> to all alignments in SAM/BAM [none]
    --rg-sm <string>
        RG header: Sample [none]
    --rg-lb <string>
        RG header: Library [none]
    --rg-pl <string>
        RG header: Platform [none]
    --rg-ds <string>
        RG header: Description [none]
    --rg-dt <string>
        RG header: Date (format: YYYY-MM-DD) [none]
    --rg-pu <string>
        RG header: Platform unit [none]
    --rg-pi <string>
        RG header: Median insert size [none]
    --rg-pg <string>
        RG header: Programs [none]
    --rg-cn <string>
        RG header: sequencing center [none]
    --rg-fo <string>
        RG header: Flow order [none]
    --rg-ks <string>
        RG header: Key sequence [none]

General:
    -t <int>,  --threads <int>
        Number of threads [1]
    -x <pacbio, ont>,  --presets <pacbio, ont>
        Parameter presets for different sequencing technologies [pacbio]
    -i <0-1>,  --min-identity <0-1>
        Alignments with an identity lower than this threshold will be discarded [0.65]
    -R <int/float>,  --min-residues <int/float>
        Alignments containing less than <int> or (<float> * read length) residues will be discarded [0.25]
    --no-smallinv
        Don't detect small inversions [false]
    --no-lowqualitysplit
        Split alignments with poor quality [false]
    --verbose
        Debug output [false]
    --no-progress
        Don't print progress info while mapping [false]

Advanced:
    --match <float>
        Match score [2]
    --mismatch <float>
        Mismatch score [-5]
    --gap-open <float>
        Gap open score [-5]
    --gap-extend-max <float>
        Gap open extend max [-5]
    --gap-extend-min <float>
        Gap open extend min [-1]
    --gap-decay <float>
        Gap extend decay [0.15]
    -k <10-15>,  --kmer-length <10-15>
        K-mer length in bases [13]
    --kmer-skip <int>
        Number of k-mers to skip when building the lookup table from the reference [2]
    --bin-size <int>
        Sets the size of the grid used during candidate search [4]
    --max-segments <int>
        Max number of segments allowed for a read per kb [1]
    --subread-length <int>
        Length of fragments reads are split into [256]
    --subread-corridor <int>
        Length of corridor sub-reads are aligned with [40]

```

### run ngmlr

```
$ ngmlr --presets ont -t 6 -r /home/wzk/database/GENOME/human/Homo_sapiens.GRCh38.fa -q /disk1/Project/KC2018-C128/PRJEB26791/raw/ERR2631603-1.fastq.gz -o  mapping/ngmlr/ERR2631603-1.sam
ngmlr 0.2.7 (build: Jul  2 2018 10:32:15, start: 2019-01-14.04:34:10)
Contact: philipp.rescheneder@univie.ac.at
Opening for output (SAM): mapping/ngmlr/ERR2631603-1.sam
Encoding reference sequence.
Size of reference genome 3099 Mbp (max. 68719 Mbp)
0 reference sequences were skipped (length < 10).
Writing encoded reference to /home/wzk/database/GENOME/human/Homo_sapiens.GRCh38.fa-enc.2.ngm
Writing to disk took 1.39s
Building reference index #0 (kmer length: 13, reference skip: 2)
66205 prefixes were ignored due to the frequency cutoff (1000)
Overall time for creating RefTable: 551.00s
Writing reference index to /home/wzk/database/GENOME/human/Homo_sapiens.GRCh38.fa-ht-13-2.2.ngm
Writing to disk took 3.57s
Opening query file /disk1/Project/KC2018-C128/PRJEB26791/raw/ERR2631603-1.fastq.gz
Mapping reads...
Processed: 1000 (0.83), R/S: 6.94, RL: 7405, Time: 4.65 1.50 17.51, Align: 1.00, 375, 0.93
Done (831 reads mapped (83.10%), 169 reads not mapped, 1099 lines written)(elapsed: 12m, 1 r/s)

```

