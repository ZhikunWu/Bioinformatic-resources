## eggnog-mapper

### [Discover EggNOG 4.5.1](http://eggnogdb.embl.de/#/app/home)

### [manual of eggnog-mapper](https://github.com/jhcepas/eggnog-mapper/wiki/Installation)

### install diamond eggnog-mapper
```
$ conda install -c bioconda diamond 
$ conda install -c bioconda eggnog-mapper
```
or
```
$ git clone https://github.com/jhcepas/eggnog-mapper.git
```


### [/download/eggnog_4.5/eggnog-mapper-data/](http://eggnogdb.embl.de/download/eggnog_4.5/eggnog-mapper-data/)

### simulation of downloading data
```
$ ~/anaconda3/envs/qiime/bin/eggnog-mapper/download_eggnog_data.py -s bact arch viruses
Downloading "og2level.tsv.gz" at /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data
cd /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data && wget -O og2level.tsv.gz http://eggnogdb.embl.de/download/emapperdb-4.5.1/og2level.tsv.gz
Download main annotation database? [y,n] y
Downloading "eggnog.db" at /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data...
cd /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data && wget -nH --user-agent=Mozilla/5.0 --relative --no-parent --reject "index.html*" --cut-dirs=4 -e robots=off -O eggnog.db.gz http://eggnogdb.embl.de/download/emapperdb-4.5.1/eggnog.db.gz && echo Decompressing... && gunzip eggnog.db.gz 
Download OG fasta files for annotation refinement (~20GB after decompression)? [y,n] y
Downloading fasta files " at /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/OG_fasta...
cd /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data && wget -nH --user-agent=Mozilla/5.0 --relative --no-parent --reject "index.html*" --cut-dirs=4 -e robots=off -O OG_fasta.tar.gz  http://eggnogdb.embl.de/download/emapperdb-4.5.1/OG_fasta.tar.gz && echo Decompressing... && tar -zxf OG_fasta.tar.gz && rm OG_fasta.tar.gz
Download diamond database (~4GB after decompression)? [y,n] y
Downloading fasta files " at /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/eggnog_proteins.dmnd...
cd /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data && wget -nH --user-agent=Mozilla/5.0 --relative --no-parent --reject "index.html*" --cut-dirs=4 -e robots=off -O eggnog_proteins.dmnd.gz  http://eggnogdb.embl.de/download/emapperdb-4.5.1/eggnog_proteins.dmnd.gz && echo Decompressing... && gunzip eggnog_proteins.dmnd.gz 
Download 3 HMM database(s): bact,arch,viruses? [y,n] y
Downloading bact HMM database " at /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/bact\_hmm ...
mkdir -p /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/bact_50; cd /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/bact_50; wget -N -nH --user-agent=Mozilla/5.0 --relative -r --no-parent --reject "index.html*" --cut-dirs=4 -e robots=off http://eggnogdb.embl.de/download/emapperdb-4.5.1/hmmdb_levels/bact_50/
Downloading arch HMM database " at /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/arch\_hmm ...
mkdir -p /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/arch_1; cd /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/arch_1; wget -N -nH --user-agent=Mozilla/5.0 --relative -r --no-parent --reject "index.html*" --cut-dirs=4 -e robots=off http://eggnogdb.embl.de/download/emapperdb-4.5.1/hmmdb_levels/arch_1/
Downloading viruses HMM database " at /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/viruses\_hmm ...
mkdir -p /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/viruses_hmm; cd /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/data/hmmdb_levels/viruses_hmm; wget -N -nH --user-agent=Mozilla/5.0 --relative -r --no-parent --reject "index.html*" --cut-dirs=4 -e robots=off http://eggnogdb.embl.de/download/emapperdb-4.5.1/hmmdb_levels/viruses_hmm/

```


### download data
```
$ ~/anaconda3/envs/qiime/bin/eggnog-mapper/download_eggnog_data.py -h
usage: download_eggnog_data.py [-h] [-D] [-y] [-f] [-s] [-q] [--data_dir]
                               dbs [dbs ...]

positional arguments:
  dbs          list of eggNOG HMM databases to download. Choose "none" if only
               diamond will be used

optional arguments:
  -h, --help   show this help message and exit
  -D           Do not install the diamond database
  -y           assume "yes" to all questions
  -f           forces download even if the files exist
  -s           simulate and print commands. Nothing is downloaded
  -q           quiet_mode
  --data_dir   Directory to use for DATA_PATH.
(qiime) wzk@ubuntu 03:56:39 ^_^ /home/wzk/metagenome_data 
$ nohup ~/anaconda3/envs/qiime/bin/eggnog-mapper/download_eggnog_data.py -q -f -y  bact arch viruses --data_dir /home/wzk/database/eggnog-mapper-data &
[1] 45795
(qiime) wzk@ubuntu 03:58:06 ^_^ /home/wzk/metagenome_data 
$ nohup: ignoring input and appending output to 'nohup.out'
```

### HMMER based searches of eggnog-mapper
Disk based searches on the optimized bacterial database
```
$ python emapper.py -i test/polb.fa --output polb_bact -d bact
```

Disk based searches on the optimized database of viral models
```
$ python emapper.py -i test/polb.fa --output polb_viruses  -d viruses
```

Disk based searches on the mammal specific database
```
$ python emapper.py -i test/p53.fa --output p53_maNOG -d maNOG
```

Memory based searches on the mammal specific database
```
$ python emapper.py -i test/p53.fa --output p53_maNOG -d maNOG --usemem
```

Using DIAMOND as search method.
Note that no target database is required when using DIAMOND.
```
$ python emapper.py -i test/p53.fa --output p53_maNOG  -m diamond
```

### run eggnog-mapper
```
$ python /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/emapper.py -i /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/test/polb.fa  --output /home/wzk/metagenome_data/eggnog-mapper --database bact --data_dir /home/wzk/database/eggnog-mapper-data   --cpu 10 --override 


#  emapper-1.0.2
# ./emapper.py  -i /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/test/polb.fa --output /home/wzk/metagenome_data/eggnog-mapper --database bact --data_dir /home/wzk/database/eggnog-mapper-data --cpu 10 --override
/home/wzk/database/eggnog-mapper-data/hmmdb_levels/bact_50/bact_50.hmm
Sequence mapping starts now!
 Processed queries:1 total_time:16.6726629734 rate:0.06 q/s
Hit refinement starts now
 Processed queries:1 total_time:6.99160194397 rate:0.14 q/s
Reading HMM matches
Functional annotation of refined hits starts now
 Processed queries:1 total_time:21.1304039955 rate:0.05 q/s
Done
   /home/wzk/metagenome_data/eggnog-mapper.emapper.hmm_hits
   /home/wzk/metagenome_data/eggnog-mapper.emapper.seed_orthologs
   /home/wzk/metagenome_data/eggnog-mapper.emapper.annotations
Total time: 44.9859 secs

================================================================================
CITATION:
If you use this software, please cite:

[1] Fast genome-wide functional annotation through orthology assignment by
      eggNOG-mapper. Jaime Huerta-Cepas, Kristoffer Forslund, Luis Pedro Coelho,
      Damian Szklarczyk, Lars Juhl Jensen, Christian von Mering and Peer Bork.
      Mol Biol Evol (2017). doi: https://doi.org/10.1093/molbev/msx148

[2] eggNOG 4.5: a hierarchical orthology framework with improved functional
      annotations for eukaryotic, prokaryotic and viral sequences. Jaime
      Huerta-Cepas, Damian Szklarczyk, Kristoffer Forslund, Helen Cook, Davide
      Heller, Mathias C. Walter, Thomas Rattei, Daniel R. Mende, Shinichi
      Sunagawa, Michael Kuhn, Lars Juhl Jensen, Christian von Mering, and Peer
      Bork. Nucl. Acids Res. (04 January 2016) 44 (D1): D286-D293. doi:
      https://doi.org/10.1093/nar/gkv1248

[3] Accelerated Profile HMM Searches. PLoS Comput. Biol. 7:e1002195. Eddy SR.
       2011.


(e.g. Functional annotation was performed using emapper-1.0.2 [1]
 based on eggNOG orthology data [2]. Sequence searches were performed
 using [3].)

```

output file:
```
$ less eggnog-mapper.emapper.annotations

# emapper version: emapper-1.0.2 emapper DB: 4.5.1
# command: ./emapper.py  -i /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/test/polb.fa --output /home/wzk/metagenome_data/eggnog-mapper --database bact --data_dir /home/wzk/database/eggnog-mapper-data --cpu 10 --override
# time: Sun Nov 12 22:12:56 2017
#query_name     seed_eggNOG_ortholog    seed_ortholog_evalue    seed_ortholog_score     predicted_gene_name     GO_terms
        KEGG_KOs        BiGG_reactions  Annotation_tax_scope    OGs     bestOG|evalue|score     COG cat eggNOG annot
362663.ECP_0061 362663.ECP_0061 0.0     1848.0  POLB    GO:0003674,GO:0003824,GO:0003887,GO:0004518,GO:0004527,GO:0004529,GO:0004536,GO:0005575,GO:0005622,GO:0005623,GO:0005694,GO:0006139,GO:0006259,GO:0006260,GO:0006261,GO:0006281,GO:0006289,GO:0006297,GO:0006301,GO:0006725,GO:0006807,GO:0006950,GO:0006974,GO:0007154,GO:0008150,GO:0008152,GO:0008296,GO:0008408,GO:0009058,GO:0009059,GO:0009432,GO:0009605,GO:0009987,GO:0009991,GO:0016740,GO:0016772,GO:0016779,GO:0016787,GO:0016788,GO:0016796,GO:0016895,GO:0018130,GO:0019438,GO:0019985,GO:0031668,GO:0033554,GO:0034061,GO:0034641,GO:0034645,GO:0034654,GO:0043170,GO:0043226,GO:0043228,GO:0043229,GO:0043232,GO:0044237,GO:0044238,GO:0044249,GO:0044260,GO:0044271,GO:0044424,GO:0044464,GO:0044699,GO:0044763,GO:0045004,GO:0045005,GO:0046483,GO:0050896,GO:0051716,GO:0071496,GO:0071704,GO:0071897,GO:0090304,GO:0090305,GO:1901360,GO:1901362,GO:1901576  K02336          bactNOG[38]     05CQ2@bactNOG,0QJ17@gproNOG,16PSF@proNOG,COG0417@NOG    05CQ2|0.0|1100.4        L       DNA polymerase
# 1 queries scanned
# Total time (seconds): 21.1304039955
# Rate: 0.05 q/s



$ less eggnog-mapper.emapper.hmm_hits

# Tue Nov 14 02:36:35 2017
# emapper-1.0.2
# /home/wzk/anaconda3/envs/qiime/bin/eggnog-mapper/emapper.py -i /home/wzk/metagenome_data/annotate/MetaContig-1.faa --output /home/wzk/metagenome_data/eggnog-mapper --database bact --data_dir /home/wzk/database/eggnog-mapper-data --cpu 10
#
# #query_name   hit     evalue  sum_score       query_length    hmmfrom hmmto   seqfrom seqto   query_coverage
EFHFDALL_00002  bactNOG.ENOG4105CQ9.meta_raw    1.2e-14 57.3    67      235     297     2       65      0.940298507463
EFHFDALL_00003  -       -       -       -       -       -       -       -       -
EFHFDALL_00004  bactNOG.ENOG4105INJ.meta_raw    3.2e-23 85.6    162     66      211     1       153     0.938271604938
EFHFDALL_00005  bactNOG.ENOG4105SHN.meta_raw    3.8e-30 107.6   97      59      152     1       93      0.948453608247
EFHFDALL_00007  bactNOG.ENOG4105GNA.meta_raw    1.2e-58 200.9   142     37      166     1       130     0.908450704225
EFHFDALL_00008  -       -       -       -       -       -       -       -       -
EFHFDALL_00009  bactNOG.ENOG4105N6H.meta_raw    8.6e-50 172.6   121     93      203     2       118     0.95867768595
EFHFDALL_00010  bactNOG.ENOG4108WER.meta_raw    2.6e-119        399.5   206     3       207     1       206     0.995145631068
EFHFDALL_00011  bacNOG.ENOG4105016.meta_raw     3e-63   217.1   242     260     462     1       242     0.995867768595
EFHFDALL_00012  -       -       -       -       -       -       -       -       -
EFHFDALL_00013  -       -       -       -       -       -       -       -       -
EFHFDALL_00014  -       -       -       -       -       -       -       -       -
EFHFDALL_00017  bactNOG.ENOG4106B19.meta_raw    2.2e-30 107.2   74      8       78      1       71      0.945945945946
EFHFDALL_00018  -       -       -       -       -       -       -       -       -
EFHFDALL_00020  bactNOG.ENOG4105DBI.meta_raw    3.3e-92 313.1   209     291     492     1       201     0.956937799043
EFHFDALL_00021  bactNOG.ENOG4105C0Y.meta_raw    3e-39   138.4   144     496     621     2       124     0.847222222222
EFHFDALL_00022  bactNOG.ENOG4106QIF.meta_raw    5.1e-20 75.2    75      180     250     1       71      0.933333333333
EFHFDALL_00023  -       -       -       -       -       -       -       -       -
EFHFDALL_00024  bactNOG.ENOG4105W7M.meta_raw    2.4e-33 118.6   122     47      164     7       120     0.926229508197
EFHFDALL_00025  -       -       -       -       -       -       -       -       -
EFHFDALL_00026  -       -       -       -       -       -       -       -       -
EFHFDALL_00027  bactNOG.ENOG4106MGB.meta_raw    3e-31   111.9   106     203     305     2       105     0.971698113208
EFHFDALL_00028  bactNOG.ENOG4105MGU.meta_raw    1.7e-50 174.9   180     58      231     1       178     0.983333333333
# 23 queries scanned
# Total time (seconds): 98.9936361313
# Rate: 0.23 q/s
```

