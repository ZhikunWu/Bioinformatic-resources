## [Assemblytics](https://github.com/MariaNattestad/Assemblytics)


### install assemblytics

```
conda install -c bioconda assemblytics
```




Assemblytics was  based on the result of mummer

```
$ Assemblytics M671-2_filter.delta  OUT 10000 50 10000000
Input delta file: M671-2_filter.delta
Output prefix: OUT
Unique anchor length: 10000
Minimum variant size to call: 50
Maximum variant size to call: 10000000
Logging progress updates in OUT/progress.log
script path: /home/wuzhikun/anaconda3/envs/pangenome/libexec/assemblytics
1. Filter delta file

2. Finding variants between alignments
Loaded 14337 alignments
3. Finding variants within alignments
Detected gzipped delta file. Reading...


Header (2 lines):
/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa /home/wuzhikun/Project/Population/Assembly/pangenome/M671-2_assembly_polish.fasta
NUCMER


4. Combine variants between and within alignments
Warning messages:
1: Removed 12 rows containing missing values (geom_bar). 
2: Removed 12 rows containing missing values (geom_bar). 
3: Removed 12 rows containing missing values (geom_bar). 
4: Removed 12 rows containing missing values (geom_bar). 
5: Removed 12 rows containing missing values (geom_bar). 
6: Removed 12 rows containing missing values (geom_bar). 
null device 
          1 
  adding: OUT.Assemblytics_assembly_stats.txt (deflated 39%)
  adding: OUT.Assemblytics.Dotplot_filtered.png (deflated 16%)
  adding: OUT.Assemblytics.Nchart.pdf (deflated 8%)
  adding: OUT.Assemblytics.Nchart.png (deflated 5%)
  adding: OUT.Assemblytics.size_distributions.all_variants.500-1e+07.pdf (deflated 14%)
  adding: OUT.Assemblytics.size_distributions.all_variants.500-1e+07.png (deflated 16%)
  adding: OUT.Assemblytics.size_distributions.all_variants.50-500.pdf (deflated 7%)
  adding: OUT.Assemblytics.size_distributions.all_variants.50-500.png (deflated 16%)
  adding: OUT.Assemblytics.size_distributions.all_variants.log_all_sizes.pdf (deflated 11%)
  adding: OUT.Assemblytics.size_distributions.all_variants.log_all_sizes.png (deflated 18%)
  adding: OUT.Assemblytics_structural_variants.bed (deflated 74%)
  adding: OUT.Assemblytics_structural_variants.summary (deflated 80%)
  adding: OUT.Assemblytics_structural_variants.summary.csv (deflated 68%)
  adding: OUT.Assemblytics.unique_length_filtered_l10000.delta.gz (deflated 0%)


```


output files:
```
drwxrwxr-x 1 4.0K Sep  3 08:51 OUT
-rw-rw-r-- 1  327 Sep  3 08:53 OUT.Assemblytics_assembly_stats.txt
-rw-rw-r-- 1 100K Sep  3 08:56 OUT.Assemblytics.Dotplot_filtered.png
-rw-rw-r-- 1 108K Sep  3 08:56 OUT.Assemblytics.Nchart.pdf
-rw-rw-r-- 1  99K Sep  3 08:56 OUT.Assemblytics.Nchart.png
-rw-rw-r-- 1  42M Sep  3 08:56 OUT.Assemblytics_results.zip
-rw-rw-r-- 1 7.3K Sep  3 08:56 OUT.Assemblytics.size_distributions.all_variants.500-1e+07.pdf
-rw-rw-r-- 1  61K Sep  3 08:56 OUT.Assemblytics.size_distributions.all_variants.500-1e+07.png
-rw-rw-r-- 1 7.9K Sep  3 08:56 OUT.Assemblytics.size_distributions.all_variants.50-500.pdf
-rw-rw-r-- 1  64K Sep  3 08:56 OUT.Assemblytics.size_distributions.all_variants.50-500.png
-rw-rw-r-- 1 8.8K Sep  3 08:56 OUT.Assemblytics.size_distributions.all_variants.log_all_sizes.pdf
-rw-rw-r-- 1  62K Sep  3 08:56 OUT.Assemblytics.size_distributions.all_variants.log_all_sizes.png
-rw-rw-r-- 1 1.4M Sep  3 08:56 OUT.Assemblytics_structural_variants.bed
-rw-rw-r-- 1 2.8K Sep  3 08:56 OUT.Assemblytics_structural_variants.summary
-rw-rw-r-- 1 1.5K Sep  3 08:56 OUT.Assemblytics_structural_variants.summary.csv
-rw-rw-r-- 1  41M Sep  3 08:53 OUT.Assemblytics.unique_length_filtered_l10000.delta.gz
-rw-rw-r-- 1 1.1M Sep  3 08:53 OUT.coords.csv
-rw-rw-r-- 1  28K Sep  3 08:56 OUT.coords.query.genome
-rw-rw-r-- 1 1.5K Sep  3 08:56 OUT.coords.ref.genome
-rw-rw-r-- 1 836K Sep  3 08:53 OUT.coords.tab
-rw-rw-r-- 1   96 Sep  3 08:56 OUT.info.csv
-rw-rw-r-- 1 1.3M Sep  3 08:56 OUT.oriented_coords.csv
-rw-rw-r-- 1  35K Sep  3 08:56 OUT.query.index
-rw-rw-r-- 1  19K Sep  3 08:56 OUT.ref.index
-rw-rw-r-- 1 1.5K Sep  3 08:56 OUT.variant_preview.txt
-rw-rw-r-- 1 1.3M Sep  3 08:53 OUT.variants_between_alignments.bed
-rw-rw-r-- 1 172K Sep  3 08:56 OUT.variants_within_alignments.bed

```



```

$ head  OUT.Assemblytics_structural_variants.bed
#reference  ref_start   ref_stop    ID  size    strand  type    ref_gap_size    query_gap_size  query_coordinates   method
15  50495244    50495300    Assemblytics_w_1    56  +   Deletion    56  0   ctg1:988558-988558:+    within_alignment
15  53110126    53110126    Assemblytics_w_2    77  +   Insertion   0   77  ctg1:3572675-3572752:+  within_alignment
15  54552442    54552492    Assemblytics_w_3    50  +   Deletion    50  0   ctg1:4999655-4999655:+  within_alignment
15  56413263    56413263    Assemblytics_w_4    68  +   Insertion   0   68  ctg1:6836605-6836673:+  within_alignment
15  57275390    57275390    Assemblytics_w_5    71  +   Insertion   0   71  ctg1:7689135-7689206:+  within_alignment
15  60597537    60597588    Assemblytics_w_6    51  +   Deletion    51  0   ctg1:10968555-10968555:+ within_alignment
15  62683435    62683500    Assemblytics_w_7    65  +   Deletion    65  0   ctg1:13029785-13029785:+ within_alignment
15  63149544    63149621    Assemblytics_w_8    77  +   Deletion    77  0   ctg1:13490983-13490983:+ within_alignment
15  67609428    67609428    Assemblytics_w_9    58  +   Insertion   0   58  ctg1:17897468-17897526:+ within_alignment


$ cut -f 7 OUT.Assemblytics_structural_variants.bed | sort | uniq 
Deletion
Insertion
Repeat_contraction
Repeat_expansion
Tandem_contraction
Tandem_expansion

```

