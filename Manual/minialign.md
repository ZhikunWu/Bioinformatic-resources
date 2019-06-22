
### minialign
```
$ minialign

  minialign - fast aligner for PacBio and Nanopore long reads

minialign is a fast long-read (nucleotide sequence) alignment tool built on
the top of minimap long-read overlapper adopting libgaba SIMD-parallelized
Smith-Waterman extension algorithm.

Usage:
  first trial:
    $ minialign -t4 -xont <ref.fa> <ont2d.{fa,fq,bam}> > mapping.sam

  mapping on a prebuilt index (saves ~1min for human genome per run):
    $ minialign [indexing options] -d <index.mai> <ref.fa>
    $ minialign -l <index.mai> <reads.{fa,fq,bam}> > mapping.sam

  all-versus-all alignment in a read set:
    $ minialign -X -xava <reads.fa> [<reads.fa> ...] > allvsall.paf

Options:
  Global:
    -x STR       load preset params {pacbio,ont,ava} [ont]
    -t INT       number of threads [1]
    -X           switch to all-versus-all alignment mode
    -v           show version number [0.5.2-unknown]
  Indexing:
    -k INT       k-mer size [15]
    -w INT       minimizer window size [{-k}*2/3]
    -d FILE      dump index to FILE []
    -l FILE      load index from FILE [] (overriding -k and -w)
  Mapping:
    -a INT       match award [1]
    -b INT       mismatch penalty [1]
    -p INT       gap open penalty [1]
    -q INT       gap extension penalty [1]
    -s INT       minimum alignment score [50]
    -m INT       minimum alignment score ratio [0.30]
  Output:
    -O STR       output format {sam,maf,blast6,blasr1,blasr4,paf,mhap,falcon} [sam]
    -Q           include quality string
    -R STR       read group header line, like "@RG\tID:1" []
    -T STR,...   list of optional tags: {RG,AS,XS,NM,NH,IH,SA,MD} []
                   RG is also inferred from -R
                   supp. records are omitted when SA tag is enabled

  Pass -hVV to show all the options.
```


```
$ minialign -t 20 -x ont -O sam -R '@RG\tID:FAB45321' -T MD /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa  FAB45321_sub.fastq > FAB45321_sub_minialign.sam
```



#### [miniAlign SM tag](https://github.com/ocxtal/minialign/issues/6)
```
Thank you for your bug report. I've briefly tested picard (master on github) and confirmed that it requires the RG line with the SM option accompanied (and also quality string present in each record). So I added a quality string sustaining option '-Q' and a RG line injection option '-R' (the same as the bwa-mem's -R option) in the 0.4.3 release. Just giving -Q to minialign (or -Q -R"@RG\tID:1\tSM:foo" or something, if you need RG tags) works[ed] well with the CollectAlignmentSummaryMetrics subcommand.
```


