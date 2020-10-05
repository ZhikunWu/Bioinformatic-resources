## minimap2 manual

### minimap2 index 

```
minimap2 -t 20  -k 15  -d Homo_sapiens.GRCh38.dna.primary_assembly.fa.mmi  Homo_sapiens.GRCh38.dna.primary_assembly.fa
```



```
$ minimap2 --MD -a -x map-ont -t 20 /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa /home/husong/SRR_data/AshkenazimTrio/son/nanopore/combined_2018-05-18.fastq.gzip  > minimap_Ashkenazim_son.sam
[M::mm_idx_gen::9.499*1.00] collected minimizers
[M::mm_idx_gen::10.144*1.62] sorted minimizers
[M::main::10.144*1.62] loaded/built the index for 1 target sequence(s)
[M::mm_mapopt_update::10.547*1.60] mid_occ = 213
[M::mm_idx_stat] kmer size: 15; skip: 10; is_hpc: 0; #seq: 1
[M::mm_idx_stat::10.814*1.59] distinct minimizers: 24196618 (73.29% are singletons); average occurrences: 1.795; average spacing: 5.732
[M::main] Version: 2.15-r905
[M::main] CMD: minimap2 --MD -a -x map-ont -t 20 /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa /home/husong/SRR_data/AshkenazimTrio/son/nanopore/combined_2018-05-18.fastq.gzip
[M::main] Real time: 2219.418 sec; CPU: 37316.424 sec; Peak RSS: 15.546 GB
```

