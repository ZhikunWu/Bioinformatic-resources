

### [mutect manual](https://software.broadinstitute.org/gatk/documentation/tooldocs/3.6-0/org_broadinstitute_gatk_tools_walkers_cancer_m2_MuTect2.php)

```
$ java -Xmx100g  -jar /home/wuzhikun/anaconda3/envs/WGS/bin/GenomeAnalysisTK.jar -T MuTect2 -nct 24  -R /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -I:tumor M625-0/M625-0.bqsr.bam -I:normal M625-1/M625-1.bqsr.bam -o M625_mutect.vcf

```


Tumor/Normal variant calling
```
   java -jar GenomeAnalysisTK.jar \
     -T MuTect2 \
     -R reference.fasta \
     -I:tumor tumor.bam \
     -I:normal normal.bam \
     [--dbsnp dbSNP.vcf] \
     [--cosmic COSMIC.vcf] \
     [-L targets.interval_list] \
     -o output.vcf
```


Normal-only calling for panel of normals creation
```
 java -jar GenomeAnalysisTK.jar \
     -T MuTect2 \
     -R reference.fasta \
     -I:tumor normal1.bam \
     [--dbsnp dbSNP.vcf] \
     [--cosmic COSMIC.vcf] \
     --artifact_detection_mode \
     [-L targets.interval_list] \
     -o output.normal1.vcf
 
```

For full PON creation, call each of your normals separately in artifact detection mode as shown above. Then use CombineVariants to output only sites where a variant was seen in at least two samples:
```
   java -jar GenomeAnalysisTK.jar \
     -T CombineVariants \
     -R reference.fasta \
     -V output.normal1.vcf -V output.normal2.vcf [-V output.normal2.vcf ...] \
     -minN 2 \
     --setKey "null" \
     --filteredAreUncalled \
     --filteredrecordsmergetype KEEP_IF_ANY_UNFILTERED \
     [-L targets.interval_list] \
     -o MuTect2_PON.vcf
 
```
