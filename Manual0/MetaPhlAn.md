## [MetaPhlAn2](https://bitbucket.org/biobakery/metaphlan2)

Estimates the relative abundance of microbial cells by mapping reads against a reduced set of clade-specific marker sequences. MetaPhlAn accurately profiles microbial communities and requires only minutes to process millions of metagenomic reads. This classifier compares each metagenomic read from a sample to this marker catalog to identify high-confidence matches. It finally compares metagenomic reads against this precomputed marker catalog using nucleotide BLAST searches in order to provide clade abundances for one or more sequenced metagenomes.


### [MetaPhlAn_Pipelines_Tutorial](https://bitbucket.org/nsegata/metaphlan/wiki/MetaPhlAn_Pipelines_Tutorial)
### [MetaPhlAn 2: Metagenomic Phylogenetic Analysis](https://bitbucket.org/biobakery/metaphlan2)


### MetaPhlAn database

[Blast database of the MetaPhlAn markers](https://bitbucket.org/nsegata/metaphlan/src/f353151d84e3/blastdb): (3 files, 95MBs)

[BowTie2 database of the MetaPhlAn markers](https://bitbucket.org/nsegata/metaphlan/src/f353151d84e3/bowtie2db): (6 files, 500MBs)

[MetaPhlAn2/db_v20/](https://bitbucket.org/biobakery/metaphlan2/src/f78b79798fbca839d5f185bf32159b9ffa91d537/db_v20/?at=default)


```
https://bitbucket.org/biobakery/metaphlan2/downloads/

wget https://bitbucket.org/biobakery/metaphlan2/downloads/mpa_v20_m200.tar
wget https://bitbucket.org/biobakery/metaphlan2/downloads/mpa_v20_m200_marker_info.txt.bz2
```

all download data:
```
-rw-r--r-- 1  168 Jul 30 02:59 download.sh
-rw-r--r-- 1 291M Jul 30 03:36 mpa_v20_m200.1.bt2
-rw-r--r-- 1 170M Jul 30 03:36 mpa_v20_m200.2.bt2
-rw-r--r-- 1 9.0M Jul 30 03:30 mpa_v20_m200.3.bt2
-rw-r--r-- 1 170M Jul 30 03:30 mpa_v20_m200.4.bt2
-rw-r--r-- 1 736M Nov  2  2017 mpa_v20_m200.fna
-rw-r--r-- 1 282M Jul 30 02:37 mpa_v20_m200_marker_info.txt
-rw-r--r-- 1  32M Jul 30 02:37 mpa_v20_m200_marker_info.txt.bz2
-rw-r--r-- 1   51 Jul 30 04:40 mpa_v20_m200.md5
-rw-r--r-- 1  39M Nov  2  2017 mpa_v20_m200.pkl
-rw-r--r-- 1 291M Jul 30 03:42 mpa_v20_m200.rev.1.bt2
-rw-r--r-- 1 170M Jul 30 03:42 mpa_v20_m200.rev.2.bt2
-rw-r--r-- 1 242M Jul 30 03:09 mpa_v20_m200.tar

```






### [Instructions on download and install metaphlan2 database, if not automatically installed](https://groups.google.com/forum/#!topic/metaphlan-users/7TfY_h-SELQ)
```
1. Download the metaphlan2 database tar file to a folder (e.g. db_v20 under metaphlan2 install directory so that humann2 would automatically recoganize)
The location is (you can download the md5 file to check the download):
https://bitbucket.org/biobakery/metaphlan2/downloads/
Direct link is:
https://bitbucket.org/biobakery/metaphlan2/downloads/mpa_v20_m200.tar

2. Un-tar the above file
`tar -xzvf mpa_v20_m200.tar`

3. Un-bzip the extracted bzip2 file
`bzip -dk mpa_v20_m200.fna.bz2`

NOTE: Above Step 1-3 can be executed anywhere (in case bzip2 or gzip or tar aren't available in the system you use humann2). Just copy the resulting mpa_v20_m200.fna to the step 1 folder.

4. build bowtie2 index
`bowtie2-build --threads 4 mpa_v20_m200.fna mpa_v20_m200`
```

### bowtie2 build index
```
$ bowtie2-build --threads 20 mpa_v20_m200.fna mpa_v20_m200
```

### run bowtie2
```
$ bowtie2 -x /home/wzk/database/MetaPhlAn/mpa_v20_m200 -1 clean/TD4.clean.paired.R1.fq.gz clean/TD4.clean.paired.R2.fq.gz -S TD4.sam --threads 8

$ bowtie2 --sam-no-hd --sam-no-sq --no-unal --very-sensitive -S HMP_GUT_SRS052697.25M.sam -x /home/wzk/anaconda3/envs/qiime/bin/metaphlan2/db_v20/mpa_v20_m200 -1 TARA_OCEAN.25M-1.1.fastq -2 TARA_OCEAN.25M-1.2.fastq --threads 30
```

### run metaphlan2 using the result of bowtie2
```

$ metaphlan2.py --input_type sam --mpa_pkl /home/wzk/database/MetaPhlAn/mpa_v20_m200.pkl  --nproc 10 --tax_lev a --ignore_eukaryotes   TD4.sam  TD4.txt


$ metaphlan2.py --input_type sam  --mpa_pkl /home/wzk/database/MetaPhlAn/mpa_v20_m200.pkl  --nproc 8 --tax_lev a --ignore_eukaryotes /home/wzk/Project/metagenome/MetaPhlAn/mapping/SP1.sam /home/wzk/Project/metagenome/metaphlan/SP1.txt
```




### example of bowtie2 and metaphlan2

example:
```
$ metaphlan2.py -t marker_ab_table metagenome_outfmt.bz2 --input_type bowtie2out > marker_abundance_table.txt
```

   The obtained RPK can be optionally normalized by the total number of reads in the metagenome 
   to guarantee fair comparisons of abundances across samples. The number of reads in the metagenome
   needs to be passed with the '--nreads' argument


*  The list of markers present in the sample can be obtained with '-t marker_pres_table'
```
$ metaphlan2.py -t marker_pres_table metagenome_outfmt.bz2 --input_type bowtie2out > marker_abundance_table.txt
```
   The --pres_th argument (default 1.0) set the minimum RPK value to consider a marker present


*  The list '-t clade_profiles' analysis type reports the same information of '-t marker_ab_table'
   but the markers are reported on a clade-by-clade basis.
```
$ metaphlan2.py -t clade_profiles metagenome_outfmt.bz2 --input_type bowtie2out > marker_abundance_table.txt
```

*  Finally, to obtain all markers present for a specific clade and all its subclades, the 
   '-t clade_specific_strain_tracker' should be used. For example, the following command
   is reporting the presence/absence of the markers for the B. fragulis species and its strains

```  
$ metaphlan2.py -t clade_specific_strain_tracker --clade s__Bacteroides_fragilis metagenome_outfmt.bz2 databases/mpa_v20_m200.pkl --input_type bowtie2out > marker_abundance_table.txt
```

   the optional argument --min_ab specifies the minimum clade abundance for reporting the markers



### merge and plot heatmap
```
$ merge_metaphlan_tables.py profiled_SRS015646.txt profiled_SRS022145.txt > merged_abundance_table.txt
$ metaphlan_hclust_heatmap.py -c bbcry --top 25 --minv 0.1 -s log --in merged_abundance_table.txt  --out merged_abundance_table_heatmap.pdf
```




### Metaphlan to krona 
```
$ /home/wzk/anaconda3/envs/qiime/bin/metaphlan2/utils/metaphlan2krona.py --help
Usage: metaphlan2krona.py [options]

Options:
  -h, --help            show this help message and exit
  -p PROFILE, --profile=PROFILE
                        The input file is the MetaPhlAn standard result file
  -k KRONA, --krona=KRONA
                        the Krons output file name
```

```
$ /home/wzk/anaconda3/envs/qiime/bin/metaphlan2/utils/metaphlan2krona.py -p  merged_abundance_table.txt -k  merged_abundance_krona.txt
```

input
```
$ head merged_abundance_table.txt 
ID  profiled_SRS015646  profiled_SRS022145
#SampleID   Metaphlan2_Analysis Metaphlan2_Analysis
k__Bacteria 89.13087    98.28249
k__Bacteria|p__Actinobacteria   1.44344 4.87151
k__Bacteria|p__Actinobacteria|c__Actinobacteria 1.44344 4.87151
k__Bacteria|p__Actinobacteria|c__Actinobacteria|o__Actinomycetales  1.4299  4.87151
k__Bacteria|p__Actinobacteria|c__Actinobacteria|o__Actinomycetales|f__Actinomycetaceae  0.05839 0.32727
k__Bacteria|p__Actinobacteria|c__Actinobacteria|o__Actinomycetales|f__Actinomycetaceae|g__Actinomyces   0.05839 0.32727
k__Bacteria|p__Actinobacteria|c__Actinobacteria|o__Actinomycetales|f__Actinomycetaceae|g__Actinomyces|s__Actinomyces_graevenitzii   0.03632 0.04988
k__Bacteria|p__Actinobacteria|c__Actinobacteria|o__Actinomycetales|f__Actinomycetaceae|g__Actinomyces|s__Actinomyces_graevenitzii|t__Actinomyces_graevenitzii_unclassified     0.03632  0.04988
```

```
$ grep 'k__Viruses|p__Viruses_noname' profiled_SRS015646.txt
k__Viruses|p__Viruses_noname    10.86913
k__Viruses|p__Viruses_noname|c__Viruses_noname  10.86913
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales  10.86913
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Myoviridae    7.8142
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Siphoviridae  3.05492
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Myoviridae|g__Myoviridae_noname   7.8142
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Siphoviridae|g__Siphoviridae_noname   3.05492
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Myoviridae|g__Myoviridae_noname|s__Streptococcus_phage_EJ_1   7.8142
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Siphoviridae|g__Siphoviridae_noname|s__Streptococcus_phage_SM1    3.05492
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Myoviridae|g__Myoviridae_noname|s__Streptococcus_phage_EJ_1|t__PRJNA14604 7.8142
k__Viruses|p__Viruses_noname|c__Viruses_noname|o__Caudovirales|f__Siphoviridae|g__Siphoviridae_noname|s__Streptococcus_phage_SM1|t__PRJNA14295  3.05492
```


output:
```
$ head merged_abundance_krona.txt
0.04988     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_graevenitzii    0.03632
0.04988     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_graevenitzii    Actinomyces_graevenitzii_unclassified   0.03632
0.01226     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_naeslundii  0.0
0.01226     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_naeslundii  GCF_000285995   0.0
0.06876     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_odontolyticus   0.01915
0.06876     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_odontolyticus   Actinomyces_odontolyticus_unclassified  0.01915
0.06747     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_oris    0.0
0.06747     Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_oris    GCF_000180155   0.0
0.1289      Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_viscosus    0.00291
0.1289      Bacteria    Actinobacteria  Actinobacteria  Actinomycetales Actinomycetaceae    Actinomyces Actinomyces_viscosus    GCF_000175315   0.00291
```



### outpu html
```
$ ktImportText -o merged_abundance_krona.out.html merged_abundance_krona.txt
```
