## COG annotation

### [COG database](https://www.ncbi.nlm.nih.gov/COG/)

### install prodigal
```bash
$ conda install -c bioconda prodigal
```

### gene prediction 
```bash
$ mkdir -p  /home/wzk/metagenome_data/assembly2/annotate
$ cd /home/wzk/metagenome_data/assembly2/annotate
$ perl /home/wzk/anaconda3/envs/qiime/bin/metag-rev-sup/scripts/LengthFilter.pl /home/wzk/metagenome_data/assembly2/HMP_MOCK.contigs_10k.fa 1000 > HMP_MOCK.contigs_10k_gt1000.fa

$ wc -l /home/wzk/metagenome_data/assembly2/HMP_MOCK.contigs_10k.fa
14936 /home/wzk/metagenome_data/assembly2/HMP_MOCK.contigs_10k.fa

$ wc -l HMP_MOCK.contigs_10k_gt1000.fa
13206 HMP_MOCK.contigs_10k_gt1000.fa

$ prodigal -i HMP_MOCK.contigs_10k_gt1000.fa -a  HMP_MOCK.contigs_10k_gt1000.faa -d HMP_MOCK.contigs_10k_gt1000.fna -f gff -p meta -o HMP_MOCK.contigs_10k_gt1000.gff
```
output files
```
HMP_MOCK.contigs_10k_gt1000.faa
HMP_MOCK.contigs_10k_gt1000.fna
HMP_MOCK.contigs_10k_gt1000.gff
```


### install blast+ (required)
```
$ conda install -c bioconda blast
```

## COG analysis
### download COG database
```bash
$ mkdir -p /home/wzk/database/COG_database &&  cd /home/wzk/database/COG_database && wget ftp://ftp.ncbi.nih.gov/pub/mmdb/cdd/little_endian/Kog_LE.tar.gz
$ tar -zxf Cog_LE.tar.gz && mkdir Cog_LE && mv Cog.* Cog_LE
```

### set the pathway of COG database
in ~/.bashrc
```
export COGSDB_DIR=/home/wzk/database/COG_database/Cog_LE
```
then
```bash
$ source ~/.bashrc  && source activate qiime
```

### perform rpsblast
```bash
$ /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/RPSBLAST.sh -f HMP_MOCK.contigs_10k_gt1000.faa -p -c 5  -t 4 -r 1
```
output file 
```
HMP_MOCK.out

$ head HMP_MOCK.out
k141_13_1	gnl|CDD|224311	9.47e-14	21.622	141	1	72	2	75	74	117
k141_25_2	gnl|CDD|223351	1.15e-105	60.930	772	1	214	6	220	215	228
k141_14_1	gnl|CDD|224401	7.73e-72	41.224	555	1	242	3	247	245	254
k141_20_1	gnl|CDD|227720	2.79e-42	30.579	348	1	121	1	121	121	121
k141_20_1	gnl|CDD|227720	5.90e-35	43.590	300	141	255	1	117	117	121
k141_20_2	gnl|CDD|224331	2.05e-11	34.921	132	19	81	39	101	63	335
k141_16_4	gnl|CDD|226699	4.01e-19	29.609	202	21	190	10	186	179	637
k141_16_3	gnl|CDD|226696	3.03e-55	38.350	438	19	222	3	207	206	207
k141_28_4	gnl|CDD|225250	2.15e-58	30.325	472	46	307	7	261	277	265
k141_13_2	gnl|CDD|223348	3.21e-78	25.799	619	1	406	3	328	407	328
```

```bash
$ python /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/COG_table.py -b /home/wzk/metagenome_data/assembly2/annotate/HMP_MOCK.out -m /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scgs/scg_cogs_min0.97_max1.03_unique_genera.txt -c /home/wzk/metagenome_data/assembly2/concoct/clustering_gt1000.csv  --cdd_cog_file /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scgs/cdd_to_cog.tsv > /home/wzk/metagenome_data/assembly2/clustering_gt1000_scg.csv

```

### install reshape
```bash
$ conda install -c r r-reshape 
```

### plot the result
```bash
$ Rscript /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/COGPlot.R -s /home/wzk/metagenome_data/assembly2/clustering_gt1000_scg.csv -o /home/wzk/metagenome_data/assembly2/clustering_gt1000_scg.pdf
 ```