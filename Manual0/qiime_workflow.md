
## qiime workflow

### Validate a mapping Check for errors
```
validate_mapping_file.py \
-m mapping_file.txt \
-o validate_map/
```


### Joining Paired End Reads
```
join_paired_ends.py \
-f sequences/forward_R1_001.fastq \
-r sequences/reverse_R3_001.fastq \
-b sequences/barcode_R2_001_fixedheaders.fastq \
-o join_pe_reads \
-m fastq-join \
-j 40 -p 75
```


### Extract barcodes
```
extract_barcodes.py -f temp/PE250_join/fastqjoin.join.fastq \
-m mappingfile.txt \
-o temp/PE250_barcode \
-c barcode_paired_stitched --bc1_len 0 --bc2_len 6 -a --rev_comp_bc2

```

### De-multiplexing Reads
```
split_libraries_fastq.py -i temp/PE250_barcode/reads.fastq \
-b temp/PE250_barcode/barcodes.fastq \
-m mappingfile.txt \
-o temp/PE250_split/ \
-q 20 --max_bad_run_length 3 --min_per_read_length_fraction 0.75 --max_barcode_errors 0 --barcode_type 6
```

### Remove adaptor
```
cutadapt -g AACMGGATTAGATACCCKG -a GGAAGGTGGGGATGACGT -e 0.15 -m 300 --discard-untrimmed temp/PE250_split/seqs.fna -o temp/PE250_P5.fa
```

### format to Usearch
```
sed 's/ .*/;/g;s/>.*/&&/g;s/;>/;barcodelabel=/g;s/_[0-9]*;$/;/g' temp/PE250_P5.fa > temp/seqs_usearch.fa

```

### Dereplication
```
./usearch10 -derep_fulllength temp/seqs_usearch.fa \
-fastaout temp/seqs_unique.fa \
-minuniquesize 2 -sizeout
```


### alpha significant
```
compare_alpha_diversity.py -i result/alpha-1.txt -o result/alpha_stat -m mappingfile.txt -t nonparametric -c Description
```


### beta diversity plot
```
beta_diversity_through_plots.py -i result/otu_table4.biom -m mappingfile.txt -t result/rep_seqs.tree  -o result/beta/plot
```
### beta significant
```
# Unweighted UniFrac stats
compare_categories.py \
-i bdiv_plots/unweight_unifrac_dm.txt \
-o bdiv_stats_adonis_unweighted/ \
-m mapping_file.txt \
-c SampleType \
--method adonis
```

### Creating 2D PCoA Beta Diversity Plots
```
make_2d_plots.py \
-i bdiv_plots/unweight_unifrac_pc.txt \
-o bdiv_2d_plot/ \
-m mapping_file.txt
```

### Making Distance Boxplots
```
make_distance_boxplots.py \
-d bdiv_plots/unweighted_unifrac_dm.txt \
-o bdiv_plots/unweighted_distance_boxplot
-m mapping_file.txt \
-f "SampleType" \
--save_raw_data
```

### Abundance Significance
```
group_significance.py  -i result/otu_table4.biom -o result/kruskal_wallis_test.txt -m mappingfile.txt -s kruskal_wallis -c genotype
```

###  Normalizing Sample Abundances
```
normalize_table.py -i result/otu_table4.biom -o result/otu_table4_deseq2_normalized.biom -a DESeq2 --DESeq_negatives_to_zero
```
### Correlating Taxa Abundances and a Variable
```
sed -n '1p' result/otu_table4.txt | xargs -n 1 > name
sed -i  '1i #SampleID' name
cat name | while read marker; do sed -n '/^'"$marker"'\t.*/p' mappingfile.txt; done > mappingfile-2.txt

observation_metadata_correlation.py -i result/otu_table4.biom -o result/otu_table4_correlation.txt -m mappingfile-2.txt  -c genotype -s spearman
```
### Abundance Heatmap
```
make_otu_heatmap.py -i result/otu_table4.biom -o result/otu_table4_heatmap.pdf -m mappingfile.txt -t result/rep_seqs.tree
```


### Identifying differentially abundant OTUs (not Normalizing)
#### install DESeq2
```
source("https://bioconductor.org/biocLite.R")
biocLite("DESeq2")
```

```
differential_abundance.py -i otu_table.biom -o diff_otus.txt -m example_map.txt -a DESeq2_nbinom -c Env -x Rock -y Soil -d
```
and -x and -y are the two categories you are comparing OTU counts between.

output files
```
OTU	baseMean	log2FoldChange	lfcSE	stat	pvalue	padj	taxonomy
New.CleanUp.ReferenceOTU1	344.264896992611	-7.56413295150909	0.896632640419114	-8.43615613633403	3.27944626692551e-17	8.6249436820141e-15	k__Archaea; p__Euryarchaeota; c__Halobacteria; o__Halobacteriales; f__Halobacteriaceae; g__; s__
1106797	375.62436208403	-7.52492047816268	0.918347169604749	-8.19398232740386	2.52722187085528e-16	3.3232967601747e-14	k__Archaea; p__Euryarchaeota; c__Halobacteria; o__Halobacteriales; f__Halobacteriaceae; g__Haloterrigena; s__
New.CleanUp.ReferenceOTU21	123.485073162181	-6.52374730020925	0.873690031326847	-7.46688993383824	8.21123947029121e-14	7.19851993562196e-12	k__Archaea; p__Euryarchaeota; c__Halobacteria; o__Halobacteriales; f__Halobacteriaceae; g__Haloterrigena; s__
3862609	86.8415956377759	-6.1805885862336	0.857896613133417	-7.20435130715735	5.83208253243469e-13	3.83459426507581e-11	k__Archaea; p__Euryarchaeota; c__Halobacteria; o__Halobacteriales; f__Halobacteriaceae; g__Halobacteriaceae; NA
```
p-values and (much more importantly) multiple hypothesis corrected p-values for each differentially observed feature.


### [Normalizing the OTU Table](https://github.com/alexcritschristoph/Qiime16sTutorial)
paper: [Robust methods for differential abundance analysis in marker gene surveys](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4010126/)
```
normalize_table.py -i otu_table.biom -a CSS -o CSS_normalized_otu_table.biom
```


### Core Diversity Analysis
```
core_diversity_analyses.py  -i result/otu_table4.biom -o result/otu_diversity_core -m mappingfile.txt  -c genotype -t  result/rep_seqs.tree -e 1000 --recover_from_failure

    raise RuntimeError('Invalid DISPLAY variable')
RuntimeError: Invalid DISPLAY variable

```

### greendatabase
```
/home/wzk/database/greengenes_release/gg_13_5/gg_13_8_otus/taxonomy/97_otu_taxonomy.txt
```


### losed reference OTU's.
```
filter_otus_from_otu_table.py -i result/otu_table4.biom -o result/closed_otu_table.biom --negate_ids_to_exclude -e /home/wzk/database/greengenes_release/gg_13_5/gg_13_8_otus/taxonomy/97_otu_taxonomy.txt
```

### pick_closed_reference_otus
```
/home/wzk/anaconda3/envs/qiime/lib/python2.7/site-packages/qiime_default_reference/gg_13_8_otus/taxonomy/97_otu_taxonomy.txt
```

### convert biom format
* Convert biom format to tab-delimited table format:

```
biom convert -i result/otu_table4.biom -o result/otu_table5.txt --to-tsv
```
* Convert a tab-delimited table to a HDF5 or JSON biom format. Note that you must specify the type of table here:

```
biom convert -i table.txt -o table.from_txt_json.biom --table-type="OTU table" --to-json
biom convert -i table.txt -o table.from_txt_hdf5.biom --table-type="OTU table" --to-hdf5
```
* Convert biom format to classic format, including the taxonomy observation metadata as the last column of the classic format table. Because the BIOM format can support an arbitrary number of observation (or sample) metadata entries, and the classic format can support only a single observation metadata entry, you must specify which of the observation metadata entries you want to include in the output table:

```
biom convert -i table.biom -o table.from_biom_w_taxonomy.txt --to-tsv --header-key taxonomy
```
* Convert biom format to classic format, including the taxonomy observation metadata as the last column of the classic format table, but renaming that column as ConsensusLineage. This is useful when using legacy tools that require a specific name for the observation metadata column.:

```
biom convert -i table.biom -o table.from_biom_w_consensuslineage.txt --to-tsv --header-key taxonomy --output-metadata-id "ConsensusLineage"
```
* In specific cases, see this comment, it is still useful to convert our biom table to tsv so we can open in Excel, make some changes to the file and then convert back to biom. For this cases you should follow this steps:

```
biom convert -i otu_table.biom -o otu_table.txt --to-tsv --header-key taxonomy
biom convert -i otu_table.txt -o new_otu_table.biom --to-hdf5 --table-type="OTU table" --process-obs-metadata taxonomy
```


## Running PICRUSt
In your working directory you should have an OTU table called "otus.biom" and a mapping file "map.tsv". The OTU table has been produced within QIIME using the greengenes reference database. The mapping file is just a tab-delimited text file that has sample ids in the first column and a couple of additional columns with metadata for each sample.
* pepare database

```
/home/wzk/anaconda3/envs/qiime/bin/picrust-1.1.2/picrust/data/ko_13_5_precalculated.tab
/home/wzk/anaconda3/envs/qiime/bin/picrust-1.1.2/picrust/data/16S_13_5_precalculated.tab.gz

$ sed -n '1,5p' 16S_13_5_precalculated.tab | cut -f 1-5
\#OTU_IDs	16S_rRNA_Count
228054	1.0
228057	1.0
378462	5.0
89370	9.0

$ sed -n '1,5p' ko_13_5_precalculated.tab | cut -f 1-5
\#OTU_IDs	K01365	K01364	K01361	K01360
142199	0.0	0.0	0.0	0.0
4314756	0.0	0.0	0.0	0.0
4314754	0.0	0.0	0.0	0.0
4314750	0.0	0.0	0.0	0.0
```
The reference data should be compressed with suffix of .gz
```
gzip /home/wzk/anaconda3/envs/qiime/bin/picrust-1.1.2/picrust/data/ko_13_5_precalculated.tab
gzip /home/wzk/anaconda3/envs/qiime/bin/picrust-1.1.2/picrust/data/16S_13_5_precalculated.tab
```


###  Normalize OTU Table
```
normalize_by_copy_number.py -i result/otu_table5-1.txt (txt/biom) -o result/otu_table4_normalize.biom
biom convert -i result/otu_table4_normalize.biom -o result/otu_table4_normalize.biom.txt --to-tsv
```
note: for input file result/otu_table5-1.txt (or biom format), the first column must be ID which is identical to that of the database /home/wzk/anaconda3/envs/qiime/bin/picrust-1.1.2/picrust/data/ko_13_5_precalculated.tab

* compare the results 

```
$ less  result/otu_table4_normalize.biom.txt
\# Constructed from biom file
\#OTU ID KO6     KO3     KO5     WT8     WT6     KO2     KO7     OE2     WT1     WT2
228054  73.0    40.0    62.0    15.0    16.0    29.0    91.0    1.0     23.0    30.0
228057  73.0    85.0    23.0    32.0    29.0    16.0    35.0    5.0     6.0     16.0
378462  360.6   2209.6  465.0   477.8   466.0   308.2   786.6   25.6    818.0   638.6
89370   12.5555555556   16.6666666667   69.3333333333   7.11111111111   57.3333333333

$ less  result/otu_table4_normalize.biom.txt
\# Constructed from biom file
\#OTU ID KO6     KO3     KO5     WT8     WT6     KO2     KO7     OE2     WT1     WT2
228054  73.0    40.0    62.0    15.0    16.0    29.0    91.0    1.0     23.0    30.0
228057  73.0    85.0    23.0    32.0    29.0    16.0    35.0    5.0     6.0     16.0
378462  360.6   2209.6  465.0   477.8   466.0   308.2   786.6   25.6    818.0   638.6
89370   12.5555555556   16.6666666667   69.3333333333   7.11111111111   57.3333333333
```

###　Predict Functions For Metagenome
```
predict_metagenomes.py -i result/otu_table4_normalize.biom  -o result/metagenome_predictions.biom
```

* Output format can be changed from BIOM to tab delimited using ‘-f’ option:

```
predict_metagenomes.py -f -i result/otu_table4_normalize.biom  -o result/metagenome_predictions.tab.txt

$ less result/metagenome_predictions.tab.txt
\# Constructed from biom file
\#OTU ID KO6     KO3     KO5     WT8     WT6     KO2     KO7     OE2     WT1     WT2
K01365  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01364  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01361  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01360  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01362  738.0   2516.0  766.0   594.0   629.0   435.0   1169.0  42.0    907.0   765.0
K02249  13.0    17.0    69.0    7.0     57.0    8.0     40.0    4.0     8.0     4.0
K05841  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K05844  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K05845  721.0   4419.0  930.0   956.0   932.0   616.0   1573.0  51.0    1636.0  1277.0
K05846  1094.0  6645.0  1464.0  1441.0  1455.0  932.0   2399.0  80.0    2462.0  1920.0
K05847  721.0   4419.0  930.0   956.0   932.0   616.0   1573.0  51.0    1636.0  1277.0

```

* NSTI values for each sample can be obtained using the -a option. (We strongly recommend this step, as NSTI values are precalculated for common inputs):

```
predict_metagenomes.py -f -i result/otu_table4_normalize.biom  -o result/metagenome_predictions.tab.txt -o result/nsti_per_sample.tab
```

```
$ less result/nsti_per_sample.tab

\# Constructed from biom file
\#OTU ID KO6     KO3     KO5     WT8     WT6     KO2     KO7     OE2     WT1     WT2
K01365  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01364  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01361  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01360  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K01362  738.0   2516.0  766.0   594.0   629.0   435.0   1169.0  42.0    907.0   765.0
K02249  13.0    17.0    69.0    7.0     57.0    8.0     40.0    4.0     8.0     4.0
K05841  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K05844  0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
K05845  721.0   4419.0  930.0   956.0   932.0   616.0   1573.0  51.0    1636.0  1277.0
K05846  1094.0  6645.0  1464.0  1441.0  1455.0  932.0   2399.0  80.0    2462.0  1920.0
K05847  721.0   4419.0  930.0   956.0   932.0   616.0   1573.0  51.0    1636.0  1277.0
```

* Previous examples assume that KEGG Orthologs predictions are wanted. Other types of functions (e.g. COGs) can be specified using the --type_of_prediction option:

first we should download the reference data from [picrust](https://sourceforge.net/projects/picrust/files/precalculated_files/)
```
wget https://mirrors.netix.net/sourceforge/p/pi/picrust/precalculated_files/cog_13_5_precalculated.tab.gz
cp cog_13_5_precalculated.tab.gz /home/wzk/anaconda3/envs/qiime/bin/picrust-1.1.2/picrust/data/

predict_metagenomes.py --type_of_prediction cog -f -i result/otu_table4_normalize.biom  -o result/metagenome_predictions_cog.biom.txt


$ less result/metagenome_predictions_cog.biom.txt
\# Constructed from biom file
\#OTU ID KO6     KO3     KO5     WT8     WT6     KO2     KO7     OE2     WT1     WT2
COG0393 86.0    57.0    131.0   22.0    73.0    37.0    131.0   5.0     31.0    34.0
COG4055 0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
COG2043 0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
COG3010 434.0   2250.0  527.0   493.0   482.0   337.0   878.0   27.0    841.0   669.0
COG3011 446.0   2266.0  596.0   500.0   539.0   345.0   917.0   30.0    849.0   673.0
COG3012 0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
COG3013 0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
COG3014 0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0

```

### Analyzing PICRUSt predicted metagenomes
#### Collapse predictions into pathways
[categorize_by_function.py ](https://picrust.github.io/picrust/scripts/categorize_by_function.html#categorize-by-function): This script collapses hierarchical data to a specified level. For instance, often it is useful to examine KEGG results from a higher level within the pathway hierarchy. Many genes are sometimes involved in multiple pathways, and in these circumstances (also know as a one-to-many relationship), the gene is counted for each pathway. This has a side effect of increasing the total count of genes in the table.

* Collapse the thousands of predicted functions into higher categories (e.g KOs into KEGG Pathways).

```
$ predict_metagenomes.py -i result/otu_table4_normalize.biom  -o result/metagenome_predictions.biom
$ categorize_by_function.py -i result/metagenome_predictions.biom  -c KEGG_Pathways -l 3 -o result/predicted_metagenomes_KEGG.L3.biom
$ biom convert -i result/predicted_metagenomes_KEGG.L3.biom -o result/predicted_metagenomes_KEGG.L3.biom.txt --to-tsv
$ less result/predicted_metagenomes_KEGG.L3.biom.txt

\# Constructed from biom file
\#OTU ID KO6     KO3     KO5     WT8     WT6     KO2     KO7     OE2     WT1     WT2
1,1,1-Trichloro-2,2-bis(4-chlorophenyl)ethane (DDT) degradation 0.0     0.0     0.0
ABC transporters        38920.0 193764.0        50855.0 43296.0 47757.0 28957.0 76571.0
Adherens junction       0.0     0.0     0.0     0.0     0.0     0.0     0.0     0.0
Adipocytokine signaling pathway 544.0   2385.0  758.0   546.0   683.0   377.0   1031.0
African trypanosomiasis 73.0    85.0    23.0    32.0    29.0    16.0    35.0    5.0
Alanine, aspartate and glutamate metabolism     12054.0 54138.0 14943.0 12265.0 13558.0
Aldosterone-regulated sodium reabsorption       0.0     0.0     0.0     0.0     0.0
Alzheimer's disease     1257.0  4958.0  1308.0  1160.0  1224.0  770.0   2009.0  86.0
Amino acid metabolism   2609.0  11728.0 3204.0  2650.0  2885.0  1826.0  4857.0  176.0
Amino acid related enzymes      16948.0 79215.0 20877.0 17816.0 19163.0 12104.0 31992.0
Amino sugar and nucleotide sugar metabolism     17603.0 85473.0 21699.0 19106.0 20174.0
Aminoacyl-tRNA biosynthesis     14447.0 65775.0 17204.0 14874.0 15834.0 10071.0 26526.0
```

* or Change output to tab-delimited format (instead of BIOM).

```
$ categorize_by_function.py -f -i result/metagenome_predictions.biom  -c KEGG_Pathways -l 3 -o result/predicted_metagenomes_KEGG.L3.biom.txt
```

* Collapse predicted metagenome using taxonomy metadata (not one-to-many).

```
$ categorize_by_function.py -i result/metagenome_predictions.biom  -c taxonomy -l 1 -o result/predicted_metagenomes_KEGG.L1.biom
```

#### Determine which OTUs are contributing to particular functions
[metagenome_contributions.py](https://picrust.github.io/picrust/scripts/metagenome_contributions.html#metagenome-contributions): This script partitions metagenome functional contributions according to function, OTU, and sample, for a given OTU table 

* Partition the predicted contribution to the metagenomes from each organism in the given OTU table, limited to only  K01360,K01362,K02249

```
$ metagenome_contributions.py -i result/otu_table4_normalize.biom -l K01360,K01362,K02249  -o result/otu_table4_normalize.biom_contributions_ko.tab
Filtering the genome table to include only user-specified functions: ['K01360', 'K01362', 'K02249']

$ less result/otu_table4_normalize.biom_contributions_ko.tab
Gene    Sample  OTU     GeneCountPerGenome      OTUAbundanceInSample    CountContributedByOTU   ContributionPercentOfSample
K01362  KO6     89370   1.0     12.5555555556   12.5555555556   0.0170093626757 0.000846831426589
K01362  KO6     228054  3.0     73.0    219.0   0.296685432158  0.0147708384231
K01362  KO6     228057  2.0     73.0    146.0   0.197790288105  0.00984722561538
K01362  KO6     378462  1.0     360.6   360.6   0.488514917061  0.024321298335
K01362  KO3     89370   1.0     16.6666666667   16.6666666667   0.00662356930903        0.00112411251317
K01362  KO3     228054  3.0     40.0    120.0   0.047689699025  0.00809361009483
K01362  KO3     228057  2.0     85.0    170.0   0.0675604069521 0.0114659476343
K01362  KO3     378462  1.0     2209.6  2209.6  0.878126324714  0.149030340546
K01362  KO5     89370   1.0     69.3333333333   69.3333333333   0.0904741191823 0.00467630805479
```

* Partition the predicted contribution to the metagenomes from each organism in the given OTU table

```
$ metagenome_contributions.py -i result/otu_table4_normalize.biom -l COG0393,COG3011,COG3012 -t cog -o result/otu_table4_normalize.biom_contributions.tab

Filtering the genome table to include only user-specified functions: ['COG0393', 'COG3011', 'COG3012']

$ less result/otu_table4_normalize.biom_contributions.tab
Gene    Sample  OTU     GeneCountPerGenome      OTUAbundanceInSample    CountContributedByOTU   ContributionPercentOfSample
COG0393 KO6     89370   1.0     12.5555555556   12.5555555556   0.146753246753  0.01076703192
COG0393 KO6     228054  1.0     73.0    73.0    0.853246753247  0.0626012386851
COG0393 KO3     89370   1.0     16.6666666667   16.6666666667   0.294117647059  0.0142925202477
COG0393 KO3     228054  1.0     40.0    40.0    0.705882352941  0.0343020485946
COG0393 KO5     89370   1.0     69.3333333333   69.3333333333   0.527918781726  0.0594568842306
COG0393 KO5     228054  1.0     62.0    62.0    0.472081218274  0.0531681753216
COG0393 WT8     89370   1.0     7.11111111111   7.11111111111   0.321608040201  0.00609814197237
COG0393 WT8     228054  1.0     15.0    15.0    0.678391959799  0.012863268223
COG0393 WT6     89370   1.0     57.3333333333   57.3333333333   0.781818181818  0.0491662696522
```

### [Analyzing metagenomes with QIIME](https://picrust.github.io/picrust/tutorials/qiime_tutorial.html#qiime-tutorial)

* Many of [QIIME’s tutorials that describe diversity analyses](http://qiime.org/tutorials/index.html) are applicable to PICRUSt-predicted metagenome tables. Specific analysis tools that may be useful include:
```
alpha_diversity.py
beta_diversity.py
compute_core_microbiome.py
jackknifed_beta_diversity.py
make_distance_boxplots.py
alpha_rarefaction.py
beta_diversity_through_plots.py
group_significance.py
shared_phylotypes.py
```

* There are also a number of scripts in QIIME that may be useful for more general processing of your BIOM table. These include the following:

```
single_rarefaction.py
filter_otus_from_otu_table.py
filter_samples_from_otu_table.py
per_library_stats.py
filter_taxa_from_otu_table.py
merge_otu_tables.py
sort_otu_table.py
split_otu_table.py
split_otu_table_by_taxonomy.py
```
