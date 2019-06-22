#  [RNA-Seq Alignment](https://www.cell.com/cancer-cell/fulltext/S1535-6108(18)30306-4)

All previously downloaded RNA-seq samples were individually aligned using a uniform processing pipeline based on the STAR aligner (Dobin et al., 2013). Due to the long duration of the whole project and the extensive analyses, we used two different alignment strategies to include further samples in a second run. While almost all analyses were performed with both strategies, the sQTL analysis was completed on strategy 1 only and the neoepitope analysis was completed on the junctions resulting from the intersection of strategies 1 and 2., For the remaining analysis, we compared all results and found no significant differences between the two alignment strategies.

## Strategy 1
The STAR software (version 2.4.0i) was used in a 2-pass setup, where the first alignment pass was used to identify non-annotated junctions in the input data, allowing for the construction of a genome index containing non-annotetd junctions. The second pass alignment was then performed against the junction-aware index, allowing for a more sensitive recovery of non-annotated splice junction from the data. A complete set of command line parameters:

### 1st Pass
```

STAR --genomeDir GENOME --readFilesIn READ1 READ2 --runThreadN 4 --outFilterMultimapScoreRange 1 --outFilterMultimapNmax 20 --outFilterMismatchNmax 10 --alignIntronMax 500000 --alignMatesGapMax 1000000 --sjdbScore 2 --alignSJDBoverhangMin 1 --genomeLoad NoSharedMemory --readFilesCommand cat --outFilterMatchNminOverLread 0.33 --outFilterScoreMinOverLread 0.33 --sjdbOverhang 100 --outSAMstrandField intronMotif --outSAMtype None --outSAMmode None
```

### Re-indexing
```
STAR --runMode genomeGenerate --genomeDir GENOME_TMP --genomeFastaFiles GENOME_FASTA --sjdbOverhang 100 --runThreadN 4 --sjdbFileChrStartEnd SJ.out.tab
```

### 2nd Pass
```
STAR --genomeDir GENOME_TMP --readFilesIn READ1 READ2 --runThreadN 4 --outFilterMultimapScoreRange 1 --outFilterMultimapNmax 20 --outFilterMismatchNmax 10 --alignIntronMax 500000 --alignMatesGapMax 1000000 --sjdbScore 2 --alignSJDBoverhangMin 1 --genomeLoad NoSharedMemory --limitBAMsortRAM 70000000000 --readFilesCommand cat --outFilterMatchNminOverLread 0.33 --outFilterScoreMinOverLread 0.33 --sjdbOverhang 100 --outSAMstrandField intronMotif --outSAMattributes NH HI NM MD AS XS --outSAMunmapped Within --outSAMtype BAM SortedByCoordinate --outSAMheaderHD @HD VN:1.4 --outSAMattrRGline ID SM:
```

## Strategy 2
Again, this strategy comprises a two-pass alignment approach. As a difference to strategy 1, a newer version of the STAR aligner was used (2.5.3a), that re-creates the index augmented with non-annotated junctions on the fly and does not require manual rebuild of the reference genome index. Hence only a single run per sample was necessary. The full list of command line parameters was as follows:

```
STAR --genomeDir GENOME --readFilesIn READ1 READ2 --runThreadN 4 --outFilterMultimapScoreRange 1 --outFilterMultimapNmax 20 --outFilterMismatchNmax 10 --alignIntronMax 500000 --alignMatesGapMax 1000000 --sjdbScore 2 --alignSJDBoverhangMin 1 --genomeLoad NoSharedMemory --limitBAMsortRAM 70000000000 --readFilesCommand cat --outFilterMatchNminOverLread 0.33 --outFilterScoreMinOverLread 0.33 --sjdbOverhang 100 --outSAMstrandField intronMotif --outSAMattributes NH HI NM MD AS XS --sjdbGTFfile GENCODE_ANNOTATION --limitSjdbInsertNsj 2000000 --outSAMunmapped None --outSAMtype BAM SortedByCoordinate --outSAMheaderHD @HD VN:1.4 --outSAMattrRGline ID::<ID> --twopassMode Basic --outSAMmultNmax 1
```

