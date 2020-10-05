## falcon

### [FALCON_unzip](https://github.com/PacificBiosciences/FALCON_unzip/wiki/Binaries)

### install falcon
```
$ wget https://downloads.pacbcloud.com/public/falcon/falcon-2018.08.08-21.41-py2.7-ucs4-beta.tar.gz

$ tar -zxf falcon-2018.08.08-21.41-py2.7-ucs4-beta.tar.gz

```


or

```
$ conda install -c conda-forge falcon 
```



### falcon tools
get two directories **bin** and **lib**

```
$ tree bin
bin
├── arrow
├── avro
├── bam2fasta
├── bam2fastq
├── bam2sam
├── bamSieve
├── bgzip
├── blasr
├── Catrack
├── ccs
├── chardetect
├── conv-template
├── createChemistryHeader.py
├── cygdb
├── cython
├── cythonize
├── daligner
├── daligner_p
├── DAM2fasta
├── datander
├── dataset
├── DB2Falcon
├── DB2fasta
├── DBdump
├── DBdust
├── DBrm
├── DBshow
├── DBsplit
├── DBstats
├── dexta
├── extractUnmappedSubreads.py
├── f2py
├── falcon-task
├── fasta2DAM
├── fasta2DB
├── fc_actg_coordinate
├── fc_calc_cutoff
├── fc_consensus
├── fc_consensus.exe
├── fc_contig_annotate
├── fc_ctg_link_analysis
├── fc_dedup_a_tigs
├── fc_dedup_h_tigs.py
├── fc_fasta2fasta
├── fc_fetch_reads
├── fc_gen_gfa_v1
├── fc_get_read_ctg_map
├── fc_get_read_hctg_map.py
├── fc_graphs_to_h_tigs.py
├── fc_graph_to_contig
├── fc_graph_to_utgs
├── fc_ovlp_filter
├── fc_ovlp_filter_with_phase.py
├── fc_ovlp_stats
├── fc_ovlp_to_graph
├── fc_phased_ovlp_to_graph.py
├── fc_phasing_readmap.py
├── fc_pr_ctg_track
├── fc_quiver.py
├── fc_rr_ctg_track
├── fc_rr_hctg_track2.exe
├── fc_rr_hctg_track2.py
├── fc_rr_hctg_track.exe
├── fc_rr_hctg_track.py
├── fc_run
├── fc_run1
├── fc_run.py
├── fc_select_reads_from_bam.py
├── fc_unzip_gen_gfa_v1.py
├── fc_unzip.py
├── from-template
├── futurize
├── gffToBed
├── gffToVcf
├── heartbeat-wrapper
├── HPC.daligner
├── HPC.REPmask
├── HPC.TANmask
├── htsfile
├── jsonschema
├── LA4Falcon
├── LA4Ice
├── LAcat
├── LAcheck
├── LAdump
├── LAindex
├── LAmerge
├── LAshow
├── LAsort
├── LAsplit
├── loadChemistry.py
├── maskAlignedReads.py
├── minimap
├── pasteurize
├── pbalign
├── pbbamify
├── pb-falcon
├── pbindex
├── pbindexdump
├── pb-ini2xml
├── pbmerge
├── pbvalidate
├── pip
├── pip2
├── pip2.7
├── plurality
├── poa
├── pwatcher-main
├── pwatcher-pypeflow-example
├── quiver
├── rangen
├── REPmask
├── sawriter
├── simulator
├── summarizeConsensus
├── tabix
├── TANmask
├── undexta
└── variantCaller

```