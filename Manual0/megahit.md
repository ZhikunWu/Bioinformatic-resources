## [megahit](https://github.com/voutcn/megahit)

An ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph

### [manual of metahit](https://github.com/chrisquince/metag-rev-sup)

### assembly 
```bash
$ megahit -1 raw/HMP_GUT_SRS052697.25M.1.fastq.gz -2 raw/HMP_GUT_SRS052697.25M.2.fastq.gz --num-cpu-threads 20 --continue --out-dir  assembly --out-prefix HMP_GUT

251.0Gb memory in total.
Using: 226.512Gb.
MEGAHIT v1.1.2
--- [Wed Oct 11 23:22:16 2017] Start assembly. Number of CPU threads 20 ---
--- [Wed Oct 11 23:22:16 2017] Available memory: 270239932416, used: 243215939174
--- [Wed Oct 11 23:22:16 2017] Converting reads to binaries ---
    [read_lib_functions-inl.h  : 209]     Lib 0 (raw/HMP_GUT_SRS052697.25M.1.fastq.gz,raw/HMP_GUT_SRS052697.25M.2.fastq.gz): pe, 50000000 reads, 100 max length
    [utils.h                   : 126]     Real: 171.9064	user: 41.9920	sys: 3.9640	maxrss: 156908
--- [Wed Oct 11 23:25:08 2017] k-max reset to: 119 ---
--- [Wed Oct 11 23:25:08 2017] k list: 21,29,39,59,79,99,119 ---
--- [Wed Oct 11 23:25:08 2017] Extracting solid (k+1)-mers for k = 21 ---
```

### download scripts
```bash
$ source actiavet meta3
$ cd /home/wzk/anaconda3/envs/meta3/bin
$ git clone https://github.com/chrisquince/metag-rev-sup.git
$ conda install -c conda-forge perl

$ perl /home/wzk/anaconda3/envs/meta3/bin/metag-rev-sup/scripts/contig-stats.pl  final.contigs.fa
sequence #: 63507	total length: 116194192	max length: 217183	N50: 5093	N90: 608


$ python /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/cut_up_fasta.py -c 10000 -o 0 -m assembly2/HMP_MOCK.contigs.fa  > assembly2/HMP_MOCK.contigs_10k.fa

$ cd assembly2
$ bwa index HMP_MOCK.contigs_10k.fa

$ bwa mem -t 20 /home/wzk/metagenome_data/assembly2/HMP_MOCK.contigs_10k.fa raw/HMP_MOCK_SRR2726667_8.25M.1.fastq.gz raw/HMP_MOCK_SRR2726667_8.25M.2.fastq.gz > /home/wzk/metagenome_data/assembly2/HMP_MOCK_SRR2726667.sam

$ python /home/wzk/anaconda3/envs/qiime/bin/metag-rev-sup/scripts/Lengths.py -i assembly2/HMP_MOCK.contigs_10k.fa > assembly2/HMP_MOCK.contigs_10k.len

$ samtools view -h -b -S assembly2/HMP_MOCK_SRR2726667.sam > assembly2/HMP_MOCK_SRR2726667.bam

$ samtools view -b -F 4 assembly2/HMP_MOCK_SRR2726667.bam > assembly2/HMP_MOCK_SRR2726667.mapped.bam

$ samtools sort  assembly2/HMP_MOCK_SRR2726667.mapped.bam assembly2/HMP_MOCK_SRR2726667.mapped.sorted
```
output assembly2/HMP_MOCK_SRR2726667.mapped.sorted.bam

### stastics of coverage
```bash

$ bedtools genomecov -ibam assembly2/HMP_MOCK_SRR2726667.mapped.sorted.bam -g assembly2/HMP_MOCK.contigs_10k.len > assembly2/HMP_MOCK_cov.txt

$ awk -F"\t" '{l[$1]=l[$1]+($2 *$3);r[$1]=$4} END {for (i in l){print i","(l[i]/r[i])}}' assembly2/HMP_MOCK_cov.txt > assembly2/HMP_MOCK_cov.csv

perl  /home/wzk/anaconda3/envs/qiime/bin/metag-rev-sup/scripts/Collate.pl /home/wzk/metagenome_data/assembly2 | tr "," "\t" > assembly2/HMP_MOCK_cov.tsv

# sed 's/,/\t/g' assembly2/HMP_MOCK_cov.csv > assembly2/HMP_MOCK_cov.tsv
```

```bash
$ mkdir assembly2/concoct && cd assembly2/concoct
$ concoct --coverage_file /home/wzk/metagenome_data/assembly2/HMP_MOCK_cov.tsv --composition_file /home/wzk/metagenome_data/assembly2/HMP_MOCK.contigs_10k.fa


$ cut -d"," -f2 /home/wzk/metagenome_data/assembly2/concoct/clustering_gt1000.csv | sort | uniq -c | wc
```

