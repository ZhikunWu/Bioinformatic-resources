
## [CONCOCT manual](https://concoct.readthedocs.io/en/latest/complete_example.html)

### install CONCOCT and other tools
```bash

$ conda install cython numpy scipy biopython pandas nose pip scikit-learn 
$ wget https://github.com/BinPro/CONCOCT/archive/0.4.0.tar.gz
$ mv 0.4.0.tar.gz CONCOCT_0.4.0.tar.gz
$ tar -zxf CONCOCT_0.4.0.tar.gz
$ cd CONCOCT-0.4.0
$ python setup.py install

```

or 
```
$ conda install -c bioconda concoct
```

```
$ less requirements.txt
argparse>=1.2.1
bcbio-gff>=0.4
biopython>=1.63
distribute>=0.6.49
nose>=1.3.0
numpy>=1.8.0
pandas>=0.13.0
pysam>=0.7.7
python-dateutil>=2.2
pytz>=2013.9
scikit-learn>=0.14.1
scipy>=0.13.3
```



###  download data
```bash
wget https://github.com/BinPro/CONCOCT-test-data/archive/0.3.2.tar.gz
tar -zxf 0.3.2.tar.gz
cd CONCOCT-test-data-0.3.2
cat reads/Sample*_R1.fa > reads/All_R1.fa
cat reads/Sample*_R2.fa > reads/All_R2.fa
```

### assemble the reads
```bash
velveth velveth_k71 71 -fasta -shortPaired -separate reads/All_R1.fa reads/All_R2.fa
```
output files:
```
$ tree velveth_k71/
velveth_k71/
├── Log
├── Roadmaps
└── Sequences
```
```bash
velvetg velveth_k71 -ins_length 400 -exp_cov auto -cov_cutoff auto
```
output files
```
[37.710955] Writing contigs into velveth_k71/contigs.fa...
[38.453593] Writing into stats file velveth_k71/stats.txt...
[38.459679] Writing into graph file velveth_k71/LastGraph...
[39.271009] Estimated Coverage = 7.049479
[39.271024] Estimated Coverage cutoff = 3.524740
Final graph has 504 nodes and n50 of 290573, max 615599, total 6859245, using 1930151/3200000 reads


$ tree velveth_k71/
velveth_k71/
├── contigs.fa
├── Graph2
├── LastGraph
├── Log
├── PreGraph
├── Roadmaps
├── Sequences
└── stats.txt
```

### cut contig to 10k
```bash
python /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/cut_up_fasta.py -c 10000 -o 0 -m  velveth_k71/contigs.fa > velveth_k71/contigs_c10k.fa
```

### Map the Reads onto the Contigs
```bash
cp velveth_k71/contigs_c10k.fa  contigs/velvet_71_c10K.fa
bowtie2-build contigs/velvet_71_c10K.fa contigs/velvet_71_c10K.fa
```

output index:
```
contigs
├── velvet_71_c10K.fa
├── velvet_71_c10K.fa.1.bt2
├── velvet_71_c10K.fa.2.bt2
├── velvet_71_c10K.fa.3.bt2
├── velvet_71_c10K.fa.4.bt2
├── velvet_71_c10K.fa.rev.1.bt2
├── velvet_71_c10K.fa.rev.2.bt2

```
#### align using bowtie2
```bash
$ cp -r  contigs ../
$ cd ..
$ echo 'export MRKDUP=/home/wzk/anaconda3/envs/qiime/bin/picard-tools/MarkDuplicates.jar' >> ~/.bashrc
$ source  ~/.bashrc
$ source activate qiime

$ for f in /home/wzk/concoct_test/data/CONCOCT-test-data-0.3.2/reads/*_R1.fa; do
>     mkdir -p /home/wzk/concoct_test/data/map/$(basename $f);
>     cd /home/wzk/concoct_test/data/map/$(basename $f);
>     bash /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/map-bowtie2-markduplicates.sh -ct 1 -p '-f' $f $(echo $f | sed s/R1/R2/) pair /home/wzk/concoct_test/data/contigs/velvet_71_c10K.fa asm bowtie2;
>     cd ../..;
> done
Using: /home/wzk/anaconda3/envs/qiime/bin/bowtie2
Using: /home/wzk/anaconda3/envs/qiime/bin/samtools
Using: /home/wzk/anaconda3/envs/qiime/bin/genomeCoverageBed

```

COG database
```
/home/wzk/database/COG_database/Cog_LE
```

### COG analysis
```
$ /home/wzk/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/RPSBLAST.sh -f /home/wzk/metagenome_data/annotate/MetaContig.faa -p -c 20 -r 1
```


du MetaContig-1.faa | sed 's/\([0-9]*\)\(.*\)/\1/'


```
$ cat MetaContig.faa | parallel --block 10k --recstart '>' --pipe rpsblast -outfmt ' "6 qseqid sseqid evalue pident score qstart qend sstart send length slen" ' -max_target_seqs 1 -evalue 0.00001 -num_threads 8  -db  /home/wzk/database/COG_database/Cog_LE/Cog  -query -  -out MetaContig.faa.out
```

```
$ head  cog-annotations/velvet_71_c10K.out 
NODE_505_length_906976_cov_6.853119.77_1    gnl|CDD|225718  2e-38   28.35   344 11  249 89  340 254 348
NODE_505_length_906976_cov_6.853119.77_2    gnl|CDD|225718  8e-11   30.38   132 1   77  6   84  79  348
NODE_505_length_906976_cov_6.853119.77_6    gnl|CDD|227668  1e-66   36.22   540 1   306 1   312 312 319
NODE_505_length_906976_cov_6.853119.77_11   gnl|CDD|224872  4e-14   21.01   162 1   225 1   204 238 222
NODE_505_length_906976_cov_6.853119.78_5    gnl|CDD|225253  2e-16   19.53   187 7   335 6   309 343 311
NODE_505_length_906976_cov_6.853119.78_6    gnl|CDD|224314  2e-06   25.30   93  13  94  5   87  83  120
NODE_505_length_906976_cov_6.853119.78_7    gnl|CDD|223541  2e-36   28.17   349 6   413 150 587 458 596
NODE_505_length_906976_cov_6.853119.79_2    gnl|CDD|223510  4e-06   29.67   107 219 302 368 455 91  520
NODE_505_length_906976_cov_6.853119.79_5    gnl|CDD|223655  6e-09   16.67   128 102 418 3   309 324 309
NODE_505_length_906976_cov_6.853119.79_6    gnl|CDD|224314  1e-06   38.71   101 150 211 4   63  62  120

```

```
$ head  concoct-output/clustering_gt1000.csv 
NODE_261_length_321461_cov_8.199894.30,0
NODE_261_length_321461_cov_8.199894.31,0
NODE_361_length_352602_cov_6.831901.29,2
NODE_390_length_121514_cov_8.358864.8,0
NODE_390_length_121514_cov_8.358864.2,3
NODE_390_length_121514_cov_8.358864.0,3
NODE_322_length_13952_cov_8.311927,3
NODE_390_length_121514_cov_8.358864.7,0
NODE_390_length_121514_cov_8.358864.4,3
NODE_390_length_121514_cov_8.358864.5,0

```

```
$ head  ~/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scgs/scg_cogs_min0.97_max1.03_unique_genera.txt
COG0016
COG0060
COG0184
COG0049
COG0088
COG0092
COG0094
COG0197
COG0201
COG0532

```

```
$ head  ~/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scgs/cdd_to_cog.tsv 
223080  COG0001
223081  COG0002
223082  COG0003
223083  COG0004
223084  COG0005
223085  COG0006
223086  COG0007
223087  COG0008
223088  COG0009
223089  COG0010

```


```
$ source activate qiime
(qiime) wzk@ubuntu 01:46:18 ^_^ /home/wzk/concoct_test/data/CONCOCT-test-data-0.3.2/annotations 
$ ~/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/COG_table.py
usage: Example usage:

    Step 1: Run PROKKA_XXXXXXXX.faa with rpsblast against the  Cog database
    with following format:
            rpsblast -query PROKKA_XXXXXXXX.faa -db Cog -evalue 0.00001
            -outfmt "6 qseqid sseqid evalue pident score qstart qend
            sstart send length slen" -out blast_output.out

    Step 2: Run this script to generate the table with marker gene abundance per cluster.:
            ./COG_table.py -g PROKKA_XXXXXXXX.gff -b blast_output.out -e mail@example.com
             -c clustering_gt1000.csv -m marker_genes.txt > scg_table.tsv

Refer to rpsblast tutorial: http://www2.warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/rpsblast/
COG_table.py: error: argument -b/--blastoutfile is required

```


```
$ ~/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/COG_table.py  -b /home/wzk/concoct_test/data/CONCOCT-test-data-0.3.2//annotations/cog-annotations/velvet_71_c10K.out -m ~/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scgs/scg_cogs_min0.97_max1.03_unique_genera.txt -c  /home/wzk/concoct_test/data/CONCOCT-test-data-0.3.2/concoct-output/clustering_gt1000.csv --cdd_cog_file ~/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scgs/cdd_to_cog.tsv  > clustering_gt1000_scg.tab
```
output file:
```
Cluster Contigs Num_contigs     COG0016 COG0048 COG0049 COG0051 COG0052 COG0060 COG0072 COG0080 COG0081 COG0087 COG0088 COG0089 COG0
0       NODE_106_length_2172_cov_16.183702|NODE_108_length_1232_cov_16.167208|NODE_111_length_80116_cov_8.871636.0|NODE_111_length_8
1       NODE_100_length_1535_cov_6.691205|NODE_301_length_1017_cov_2.447394|NODE_500_length_1625_cov_5.125538|NODE_501_length_2698_c
2       NODE_216_length_305319_cov_6.901228.0|NODE_216_length_305319_cov_6.901228.1|NODE_216_length_305319_cov_6.901228.10|NODE_216_
3       NODE_103_length_20202_cov_8.395357.0|NODE_103_length_20202_cov_8.395357.1|NODE_107_length_7609_cov_8.569195|NODE_111_length
```

### plot
```
$ Rscript ~/anaconda3/envs/qiime/bin/CONCOCT-0.4.0/scripts/COGPlot.R -s clustering_gt1000_scg.tab -o clustering_gt1000_scg.tab.pdf
```


