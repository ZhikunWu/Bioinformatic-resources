
## [stringtie2](https://github.com/mpertea/stringtie2)

Transcript assembly and quantification for RNA-Seq

### install stringtie2

The python scripts based on python2

```
git clone https://github.com/mpertea/stringtie2  && cd stringtie2/ && make release
```


```
cd SuperReads_RNA/ && ./install.sh
...
make[3]: Leaving directory `/home/wuzhikun/anaconda3/envs/Assembly/bin/stringtie2/SuperReads_RNA/global-1/SuperReadsR'
make[2]: Leaving directory `/home/wuzhikun/anaconda3/envs/Assembly/bin/stringtie2/SuperReads_RNA/global-1/SuperReadsR'
make[1]: Leaving directory `/home/wuzhikun/anaconda3/envs/Assembly/bin/stringtie2/SuperReads_RNA/global-1/SuperReadsR'
creating sr_config_example.txt with correct PATHs
You can now copy the script create_rna_sr.py in any directory of PATH for convenience
or run the script with its full path: /home/wuzhikun/anaconda3/envs/Assembly/bin/stringtie2/SuperReads_RNA/create_rna_sr.py

```


```
ln -s /home/wuzhikun/anaconda3/envs/Assembly/bin/stringtie2/SuperReads_RNA/create_rna_sr.py /home/wuzhikun/anaconda3/envs/Assembly/bin/create_rna_sr.py
```


### parameters

```
$ stringtie --help
StringTie v2.0 usage:
 stringtie <input.bam ..> [-G <guide_gff>] [-l <label>] [-o <out_gtf>] [-p <cpus>]
  [-v] [-a <min_anchor_len>] [-m <min_tlen>] [-j <min_anchor_cov>] [-f <min_iso>]
  [-C <coverage_file_name>] [-c <min_bundle_cov>] [-g <bdist>] [-u] [-L]
  [-e] [-x <seqid,..>] [-A <gene_abund.out>] [-h] {-B | -b <dir_path>} 
Assemble RNA-Seq alignments into potential transcripts.
 Options:
 --version : print just the version at stdout and exit
 --conservative : conservative transcriptome assembly, same as -t -c 1.5 -f 0.05
 --rf assume stranded library fr-firststrand
 --fr assume stranded library fr-secondstrand
 -G reference annotation to use for guiding the assembly process (GTF/GFF3)
 -o output path/file name for the assembled transcripts GTF (default: stdout)
 -l name prefix for output transcripts (default: STRG)
 -f minimum isoform fraction (default: 0.01)
 -L use long reads settings (default:false)
 -m minimum assembled transcript length (default: 200)
 -a minimum anchor length for junctions (default: 10)
 -j minimum junction coverage (default: 1)
 -t disable trimming of predicted transcripts based on coverage
    (default: coverage trimming is enabled)
 -c minimum reads per bp coverage to consider for multi-exon transcript
    (default: 1)
 -s minimum reads per bp coverage to consider for single-exon transcript
    (default: 4.75)
 -v verbose (log bundle processing details)
 -g maximum gap allowed between read mappings (default: 50)
 -M fraction of bundle allowed to be covered by multi-hit reads (default:1)
 -p number of threads (CPUs) to use (default: 1)
 -A gene abundance estimation output file
 -B enable output of Ballgown table files which will be created in the
    same directory as the output GTF (requires -G, -o recommended)
 -b enable output of Ballgown table files but these files will be 
    created under the directory path given as <dir_path>
 -e only estimate the abundance of given reference transcripts (requires -G)
 -x do not assemble any transcripts on the given reference sequence(s)
 -u no multi-mapping correction (default: correction enabled)
 -h print this usage message and exit

Transcript merge usage mode: 
  stringtie --merge [Options] { gtf_list | strg1.gtf ...}
With this option StringTie will assemble transcripts from multiple
input files generating a unified non-redundant set of isoforms. In this mode
the following options are available:
  -G <guide_gff>   reference annotation to include in the merging (GTF/GFF3)
  -o <out_gtf>     output file name for the merged transcripts GTF
                    (default: stdout)
  -m <min_len>     minimum input transcript length to include in the merge
                    (default: 50)
  -c <min_cov>     minimum input transcript coverage to include in the merge
                    (default: 0)
  -F <min_fpkm>    minimum input transcript FPKM to include in the merge
                    (default: 1.0)
  -T <min_tpm>     minimum input transcript TPM to include in the merge
                    (default: 1.0)
  -f <min_iso>     minimum isoform fraction (default: 0.01)
  -g <gap_len>     gap between transcripts to merge together (default: 250)
  -i               keep merged transcripts with retained introns; by default
                   these are not kept unless there is strong evidence for them
  -l <label>       name prefix for output transcripts (default: MSTRG)

```


Any SAM spliced read alignment (a read alignment across at least one junction) needs to contain the XS tag to indicate the strand from which the RNA that produced this read originated. TopHat alignments already include this tag, but if you use a different read mapper you should check that this tag is also included for spliced alignment records. For example HISAT2 should be run with the --dta option in order to tag spliced alignments this way. As explained above, the alignments in SAM format should be sorted and preferrably converted to BAM.




```
$ /home/wuzhikun/anaconda3/envs/Assembly/bin/stringtie2/SuperReads_RNA/create_rna_sr.py --help
usage: create_rna_sr.py [-h] [-1 SHORT_PAIR1] [-2 SHORT_PAIR2]
                        [-U SHORT_UNPAIRED] [-w WORK_DIR] -H HISAT_INDEX -G
                        GMAP_INDEX [-g GMAP_DIRECTORY] [-p NUM_THREADS]
                        [-o OUT_DIR] [--frag-len FRAG_LEN]
                        [--frag-std FRAG_STD] [--gmap-cmd GMAP_CMD]
                        [--hisat2-cmd HISAT2_CMD]

Quantifies Super-Reads

optional arguments:
  -h, --help            show this help message and exit
  -1 SHORT_PAIR1, --short-pair1 SHORT_PAIR1
                        Paired short read FASTQ. Must also specify '--short-
                        pair2' and NOT '--short-unpaired'
  -2 SHORT_PAIR2, --short-pair2 SHORT_PAIR2
                        Paired short read FASTQ. Must also specify '--short-
                        pair1' and NOT '--short-unpaired'
  -U SHORT_UNPAIRED, --short-unpaired SHORT_UNPAIRED
                        Unpaired short read FASTQ. Must not include '--short-
                        pair1' or '--short-pair2'
  -w WORK_DIR, --work-dir WORK_DIR
                        MaSuRCA super-read assembly 'work1' directory. Will
                        perform super-read assembly if not included.
  -H HISAT_INDEX, --hisat-index HISAT_INDEX
                        HISAT2 index prefix for aligning short reads
  -G GMAP_INDEX, --gmap-index GMAP_INDEX
                        Gmap index for aligning super-reads
  -g GMAP_DIRECTORY, --gmap-directory GMAP_DIRECTORY
                        Gmap directory to find gmap index
  -p NUM_THREADS, --num-threads NUM_THREADS
                        Number of threads each tool can use
  -o OUT_DIR, --out-dir OUT_DIR
                        Output directory
  --frag-len FRAG_LEN   Paired fragment length for MaSuRCA to use. Will only
                        be used if '--work-dir' not specify
  --frag-std FRAG_STD   Paired fragment standard deviation for MaSuRCA to use.
                        Will only be used if '--work-dir' not specify
  --gmap-cmd GMAP_CMD   Gmap executable
  --hisat2-cmd HISAT2_CMD
                        HISAT2 executable

```