## [prodigal](https://github.com/hyattpd/Prodigal)

Prodigal Gene Prediction Software

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