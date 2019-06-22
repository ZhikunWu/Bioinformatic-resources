
### variants calling
```
$ samtools faidx TGACv1_scaffold_576745_7BL.fa

$ java -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar CreateSequenceDictionary REFERENCE=TGACv1_scaffold_576745_7BL.fa OUTPUT=TGACv1_scaffold_576745_7BL.dict

$ java -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar  AddOrReplaceReadGroups I=T01_partial.sorted.bam O=T01_partial.sorted_group.bam SORT_ORDER=coordinate  RGID=T01 RGLB=1  RGPL=illumina RGPU=1  RGSM=T01
$ java -jar /home/wzk/anaconda3/envs/evolution/bin/picard-2.8.2.jar  MarkDuplicates I=T01_partial.sorted_group.bam O=T01_partial.sorted_group_dedup.bam CREATE_INDEX=true VALIDATION_STRINGENCY=SILENT M=T01.metrics.txt

$ java -jar /home/wzk/anaconda3/envs/evolution/bin/GenomeAnalysisTK.jar -T SplitNCigarReads -R TGACv1_scaffold_576745_7BL.fa  -I T01_partial.sorted_group_dedup.bam   -o T01_partial.sorted_group_dedup_splitN.bam  -rf ReassignOneMappingQuality -RMQF 255 -RMQT 60 -U ALLOW_N_CIGAR_READS

$ java -Xmx10g -jar /home/wzk/anaconda3/envs/evolution/bin/GenomeAnalysisTK.jar  -T UnifiedGenotyper -R TGACv1_scaffold_576745_7BL.fa  -nct 10  -I T01_partial.sorted_group_dedup_splitN.bam  --genotyping_mode DISCOVERY  -o T01_partial.vcf


$ bedtools bamtofastq -i T01_partial.sorted.bam -fq T01.R1.fastq -fq2 T01.R2.fastq


$ java -jar ./GATK3/GenomeAnalysisTK.jar -T HaplotypeCaller -R reference.fasta -I sample.bam -stand_call_conf 30 -stand_emit_conf 10 -o GATK.vcf 

$ samtools mpileup -uf reference.fasta sample.bam | ./bcftools/bcftools call -m -v -o bcftools.vcf


$ samtools mpileup -g  -f /home/wzk/database/wheat_genome/Triticum_3.1/Triticum_3.1.c.fa  Picard/T01_dedupped.bam > Picard/T01_dedupped.bcf

$ bcftools view ../bcf/test.bcf | vcfutils.pl varFilter -D 8000 > test.vcf
```