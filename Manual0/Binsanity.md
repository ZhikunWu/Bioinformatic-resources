
## [BinSanity usage](https://github.com/edgraham/BinSanity/wiki/Usage)
## [Binsanity google group](https://groups.google.com/forum/#!forum/binsanity)

## install Binsanity

```
$ conda install -c bioconda binsanity
```

tools
```
Binsanity
Binsanity-lc
Binsanity-profile
Binsanity-refine
Binsanity-wf

get-ids
simplify-fasta
```

### get-ids
```
get-ids -f /home/wzk/Project/BinSanity/assembly/binsanity/ -l binsanity.contigs.fa  -o contig -x 1000
```

contig:
```
$ head contig
k119_29
k119_30
k119_34
k119_36
k119_37
k119_38
k119_41
k119_42
k119_54
k119_58
```

## Once the coverage profile is generated for your fasta file you can run either Binsanity-wf, Binsanity, Binsanity-refine, or Binsanity-lc. 

### Binsanity
```

$ Binsanity -f assembly/binsanity/  -l binsanity.contigs_simplyId.fa -p -3 -c assembly/binsanity/binsanity_coverage.cov.x100.lognorm -o /home/wzk/Project/BinSanity/assembly/binsanity/binning

        ******************************************************
        **********************BinSanity***********************
        |____________________________________________________|
        |                                                    |
        |             Computing Coverage Array               |
        |____________________________________________________|
        
          Preference: -3.0
          Maximum Iterations: 4000
          Convergence Iterations: 400
          Contig Cut-Off: 1000
          Damping Factor: 0.95
          Coverage File: assembly/binsanity/binsanity_coverage.cov.x100.lognorm
          Fasta File: binsanity.contigs_simplyId.fa
          Output directory: /home/wzk/Project/BinSanity/assembly/binsanity/binning
          logfile: binsanity-logfile.txt
          (894, 3)

         ______________________________________________________
        |                                                      |
        |                 Clustering Contigs                   |
        |______________________________________________________|

        
          Cluster 0: 173
          Cluster 1: 8
          Cluster 2: 187
          Cluster 3: 307
          Cluster 4: 57
          Cluster 5: 47
          Cluster 6: 53
          Cluster 7: 62
          Total Number of Bins: 8


         _____________________________________________________

                       Putative Bins Computed
                       in 4.26113510132 seconds
         _____________________________________________________

```


### Binsanity-refine
```
$ Binsanity-refine -f assembly/binsanity/  -l binsanity.contigs_simplyId.fa -p -3 -c assembly/binsanity/binsanity_coverage.cov.x100.lognorm -o /home/wzk/Project/BinSanity/assembly/binsanity/binning2

        ******************************************************
        **********************BinSanity***********************
        |____________________________________________________|
        |               Binsanity refinement                 |
        |                                                    |
        |              Calculating GC content                |
        |____________________________________________________|
        
          GC content calculated in 0.165695905685 seconds

         ______________________________________________________

                     Calculating 4mer frequencies
         ______________________________________________________
           4mer frequency calculated in 15.4862518311 seconds

        ______________________________________________________

                   Creating Combined Profile
        ______________________________________________________
            Combined profile created in 9.53674316406e-07 seconds

        ______________________________________________________

         Clustering Using 4mers, GC percentage, and Coverage
        ______________________________________________________
          Preference: -3.0
          Maximum Iterations: 4000
          Convergence Iterations: 400
          Contig Cut-Off: 1000
          Damping Factor: 0.95
          Coverage File: assembly/binsanity/binsanity_coverage.cov.x100.lognorm
          Fasta File: binsanity.contigs_simplyId.fa
          (894, 260)
          Cluster 0: 1
          Cluster 1: 1
          Cluster 2: 3
          Cluster 3: 3
          Cluster 4: 40
          Cluster 5: 24
          Cluster 6: 46
          Cluster 7: 9
          Cluster 8: 1
          Cluster 9: 7
          Cluster 10: 5
          Cluster 11: 71
          Cluster 12: 9
          Cluster 13: 91
          Cluster 14: 110
          Cluster 15: 114
          Cluster 16: 1
          Cluster 17: 31
          Cluster 18: 1
          Cluster 19: 171
          Cluster 20: 65
          Cluster 21: 1
          Cluster 22: 47
          Cluster 23: 7
          Cluster 24: 35
          Total Number of Bins: 17

        ______________________________________________________
                   Bins Computed in 
                   21.0622739792 seconds
        ______________________________________________________

```


### Binsanity-lc

```

$ Binsanity-lc  -f /home/wzk/Project/BinSanity/assembly/binsanity/ -l binsanity.contigs_simplyId.fa -p -3 -c /home/wzk/Project/BinSanity/assembly/binsanity/binsanity_coverage.cov.x100.lognorm -o /home/wzk/Project/BinSanity/assembly/binsanity/binning-lc --threads   10

        ******************************************************
        *******************BinSanity-lc***********************
        |____________________________________________________|
        |                                                    |
        |             Computing Coverage Array               |
        |____________________________________________________|
        
          K-Mean cluster number: 10
          Fasta File: binsanity.contigs_simplyId.fa
          Coverage File: /home/wzk/Project/BinSanity/assembly/binsanity/binsanity_coverage.cov.x100.lognorm
          Fasta File: binsanity.contigs_simplyId.fa
          Output Directory: /home/wzk/Project/BinSanity/assembly/binsanity/binning-lc
          Contig Cut-Off: 1000
          (894, 3)

        ____________________________________________________
       |                                                    |
       |        Initializing clustering via K-means         |
       |____________________________________________________|
        
          Cluster 0: 251
          Cluster 1: 59
          Cluster 2: 39
          Cluster 3: 128
          Cluster 4: 47
          Cluster 5: 165
          Cluster 6: 33
          Cluster 7: 130
          Cluster 8: 8
          Cluster 9: 34
          Total Number of Bins: 10

            ____________________________________________________

             Clustering Bin  BinSanityLC-kmean-bin_1.fna 
             via Affinity Propagation
            ____________________________________________________    
            
           ____________________________________________________
          |                                                    |
          |     Evaluating Initial Genome Bins With CheckM     |
          |____________________________________________________|
        


*******************************************************************************
 [CheckM - tree] Placing bins in reference genome tree.
*******************************************************************************

  Identifying marker genes in 10 bins with 1 threads:
Process Process-2:ssing 0 of 10 (0.00%) bins.
Traceback (most recent call last):
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/multiprocessing/process.py", line 258, in _bootstrap
    self.run()
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/markerGeneFinder.py", line 122, in __processBin
    hmmModelFile = markerSetParser.createHmmModelFile(binId, markerFile)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/markerSets.py", line 330, in createHmmModelFile
    markerFileType = self.markerFileType(markerFile)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/markerSets.py", line 430, in markerFileType
    with open(markerFile, 'r') as f:
IOError: [Errno 2] No such file or directory: '/home/wzk/Project/BinSanity/hmms/phylo.hmm'

  Saving HMM info to file.

  Calculating genome statistics for 10 bins with 1 threads:
    Finished processing 10 of 10 (100.00%) bins.

  Extracting marker genes to align.
  [Error] Models must be parsed before identifying HMM hits.
Traceback (most recent call last):
  File "/home/wzk/anaconda3/envs/qiime/bin/checkm", line 709, in <module>
    checkmParser.parseOptions(args)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/main.py", line 1253, in parseOptions
    self.tree(options)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/main.py", line 156, in tree
    os.path.join(options.out_folder, 'storage', 'tree')
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/hmmerAligner.py", line 104, in makeAlignmentToPhyloMarkers
    resultsParser.parseBinHits(outDir, hmmTableFile, False, bIgnoreThresholds, evalueThreshold, lengthThreshold)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/main.py", line 1213, in parseOptions
    if options.bVerbose:
AttributeError: 'Namespace' object has no attribute 'bVerbose'
Traceback (most recent call last):
  File "/home/wzk/anaconda3/envs/qiime/bin/Binsanity-lc", line 470, in <module>
    checkm_analysis(str(args.prefix)+"-checkm_lineagewf-binsanity.out",".fna",str(out_1),args.prefix)
  File "/home/wzk/anaconda3/envs/qiime/bin/Binsanity-lc", line 282, in checkm_analysis
    if float(list_[12]) >95 and (float(list_[13])<10):
IndexError: list index out of range

```

### Binsanity-wf
```
$ Binsanity-wf   -f /home/wzk/Project/BinSanity/assembly/binsanity/ -l binsanity.contigs_simplyId.fa -p -3 -c /home/wzk/Project/BinSanity/assembly/binsanity/binsanity_coverage.cov.x100.lognorm -o /home/wzk/Project/BinSanity/assembly/binsanity/binning-lc --threads  10


IOError: [Errno 2] No such file or directory: u'/home/wzk/Project/BinSanity/hmms/phylo.hmm'

```


### answer to phylo.hmm

```
$ locate phylo.hmm
/home/wzk/anaconda3/envs/qiime/database/checkm/hmms/phylo.hmm
/home/wzk/anaconda3/envs/qiime/database/checkm/hmms/phylo.hmm.ssi

$ cp /home/wzk/anaconda3/envs/qiime/database/checkm/hmms/phylo.hmm /home/wzk/anaconda3/envs/qiime/database/checkm/hmms/phylo.hmm.ssi /home/wzk/Project/BinSanity/hmms/
```

### checkm
```
$ checkm lineage_wf BINSANITY-INITIAL BinSanityWf_binsanity_checkm2

*******************************************************************************
 [CheckM - tree] Placing bins in reference genome tree.
*******************************************************************************

  Identifying marker genes in 8 bins with 1 threads:
    Finished processing 8 of 8 (100.00%) bins.
  Saving HMM info to file.

  Calculating genome statistics for 8 bins with 1 threads:
    Finished processing 8 of 8 (100.00%) bins.

  Extracting marker genes to align.
  Parsing HMM hits to marker genes:
  [Error] Input file does not exists: /home/wzk/Project/BinSanity/pfam/Pfam-A.hmm.dat


  Controlled exit resulting from an unrecoverable error or warning.

```

##### It need the database **Pfam-A.hmm.dat**

```
$ locate Pfam-A.hmm.dat
/home/wzk/anaconda3/envs/qiime/database/checkm/pfam/Pfam-A.hmm.dat
/home/wzk/bin/PfamScan/Pfam_db_zfc/Pfam-A.hmm.dat

$ cp /home/wzk/anaconda3/envs/qiime/database/checkm/pfam/Pfam-A.hmm.dat /home/wzk/Project/BinSanity/pfam/

```

##### re-run checkm
```
$ checkm lineage_wf BINSANITY-INITIAL BinSanityWf_binsanity_checkm2 --threads 10

  Reading marker alignment files.
  Concatenating alignments.
  Placing 8 bins into the genome tree with pplacer (be patient).
Uncaught exception: Sys_error("/home/wzk/Project/BinSanity/genome_tree/genome_tree_full.refpkg: No such file or directory")
Fatal error: exception Sys_error("/home/wzk/Project/BinSanity/genome_tree/genome_tree_full.refpkg: No such file or directory")
Uncaught exception: Sys_error("BinSanityWf_binsanity_checkm2/storage/tree/concatenated.pplacer.json: No such file or directory")
Fatal error: exception Sys_error("BinSanityWf_binsanity_checkm2/storage/tree/concatenated.pplacer.json: No such file or directory")

  { Current stage: 0:00:30.037 || Total: 0:00:30.037 }

*******************************************************************************
 [CheckM - lineage_set] Inferring lineage-specific marker sets.
*******************************************************************************

  Reading HMM info from file.
  Parsing HMM hits to marker genes:
    Finished parsing hits for 8 of 8 (100.00%) bins.

  Determining marker sets for each genome bin.

Unexpected error: <type 'exceptions.IOError'>
Traceback (most recent call last):
  File "/home/wzk/anaconda3/envs/qiime/bin/checkm", line 709, in <module>
    checkmParser.parseOptions(args)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/main.py", line 1254, in parseOptions
    self.lineageSet(options)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/main.py", line 230, in lineageSet
    resultsParser, options.unique, options.multi)
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/treeParser.py", line 479, in getBinMarkerSets
    uniqueIdToLineageStatistics = self.readNodeMetadata()
  File "/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/checkm/treeParser.py", line 558, in readNodeMetadata
    with open(metadataFile) as f:
IOError: [Errno 2] No such file or directory: u'/home/wzk/Project/BinSanity/genome_tree/genome_tree.metadata.tsv'


IOError: [Errno 2] No such file or directory: u'/home/wzk/Project/BinSanity/selected_marker_sets.tsv'

```


##### It need the data **genome_tree.metadata.tsv**

```
$ locate genome_tree.metadata.tsv
/home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree.metadata.tsv

$ locate genome_tree_full.refpkg
/home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree_full.refpkg
/home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree_full.refpkg/CONTENTS.json
/home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree_full.refpkg/genome_tree.fasta
/home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree_full.refpkg/genome_tree.log
/home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree_full.refpkg/genome_tree.tre
/home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree_full.refpkg/phylo_modelEcOyPk.json


$ locate selected_marker_sets.tsv
/home/wzk/anaconda3/envs/qiime/database/checkm/selected_marker_sets.tsv
```

##### copy the data sets to the target directory
```
$ cp /home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree.metadata.tsv /home/wzk/Project/BinSanity/genome_tree/


$ cp -r /home/wzk/anaconda3/envs/qiime/database/checkm/genome_tree/genome_tree_full.refpkg /home/wzk/Project/BinSanity/genome_tree/

cp /home/wzk/anaconda3/envs/qiime/database/checkm/selected_marker_sets.tsv /home/wzk/Project/BinSanity/
```

