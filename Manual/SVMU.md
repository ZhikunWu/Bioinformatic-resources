## [SVMU](https://github.com/mahulchak/svmu)

### install mummer and svmu

##### install mummer4 and LASTZ

```
conda install -c bioconda mummer4

conda install -c bioconda lastz
```

##### install svmu

```
git clone https://github.com/mahulchak/svmu.git
cd svmu && make
```



#### Alignment using nucmer
```
$ nucmer --threads 20 --prefix M671-2  /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  M671-2_assembly_polish.fasta.gz
```


output file:
```
$ head M671-2.delta
/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/Population/Assembly/pangenome/M671-2_assembly_polish.fasta
NUCMER
>6 ctg18 170805979 13223659
141184 141371 3571193 3571382 25 25 0
-34
-1
0
772377 773447 11525916 11526968 142 142 0
12
10

```


#### Filt the dalta

```
delta-filter -1 M671-2.delta > M671-2_filter.delta
```

### run svmu

```

$ svmu M671-2_filter.delta /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/Population/Assembly/pangenome/M671-2_assembly_polish.fasta snp_mode l M671-2_filter
```

output files
```
-rw-rw-r-- 1  61K Sep  2 20:48 cm.M671-2_filter.txt
-rw-rw-r-- 1    0 Sep  2 20:48 cnv_all.M671-2_filter.txt
-rw-rw-r-- 1 753K Sep  2 20:48 cords.M671-2_filter.txt

$ head -n 5  cm.M671-2_filter.txt
10  18570484    18705154    ctg206  2984734 2851783 
10  18704834    18741524    ctg206  2851954 2815666 
10  18741676    19171963    ctg206  2815665 2390173 
10  19172059    19215735    ctg206  2390172 2347035 
10  19215872    19238593    ctg206  2347033 2324580 

$ head -n 5  cords.M671-2_filter.txt
10  46093381    46094544    ctg1021 1248    122     0   0
10  46136072    46141579    ctg1021 56868   62260       0   0
10  46209032    46237587    ctg1021 61202   33160       0   0
10  46251367    46267407    ctg1021 17079   1567        0.257481    0
10  46297438    46298531    ctg1021 1   1060        0   0

```

