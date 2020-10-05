## [canvas](https://github.com/Illumina/canvas)

Copy number variant (CNV) calling from DNA sequencing data

### canvas parameter

```
$ Canvas SmallPedigree-WGS --help
Canvas 1.35.1.1316+master Copyright © Illumina 2018
 
SmallPedigree-WGS - CNV calling of a small pedigree from whole genome sequencing data
 
Usage: Canvas.exe SmallPedigree-WGS [OPTIONS]+
 
Mode-specific options:
  -b, --bam=VALUE1 VALUE2 VALUE3
                             bam [pedigree-member] [sample-name] Option can 
                               be specified multiple times. (required)
                               
                               bam: sample .bam file (required)
                               
                               pedigree-member: Pedigree member type (either 
                               proband, mother, father or other). Default is 
                               other
                               
                               sample-name: sample name. Default is SM tag in 
                               RG header of the .bam (required)
      --ploidy-vcf=VALUE     multisample .vcf file containing regions of 
                               known ploidy. Copy number calls matching the 
                               known ploidy in these regions will be considered 
                               non-variant
      --sample-b-allele-vcf=VALUE
                             multisample .vcf file containing SNV b-allele 
                               sites (only sites with PASS in the filter column 
                               will be used) (either this option or option 
                               population-b-allele-vcf is required)
      --population-b-allele-vcf=VALUE
                             vcf containing SNV b-allele sites in the 
                               population (only sites with PASS in the filter 
                               column will be used) (either this option or 
                               option sample-b-allele-vcf is required)
      --common-cnvs-bed=VALUE
                             .bed file containing regions of known common CNVs
 
 
Common options:
  -o, --output=VALUE         output directory. Will be created if it doesn't 
                               exist. (required)
  -r, --reference=VALUE      Canvas-ready reference fasta file (required)
  -g, --genome-folder=VALUE  folder that contains both genome.fa and 
                               GenomeSize.xml (required)
  -f, --filter-bed=VALUE     .bed file of regions to skip (required)
      --custom-parameters=VALUE
                             use custom parameter for command-line tool. 
                               VALUE must contain the tool name followed by a 
                               comma and then the custom parameters. Option can 
                               be specified multiple times.
  -c=VALUE                   continue analysis starting at the specified 
                               checkpoint. VALUE can be the checkpoint name or 
                               number
  -s=VALUE                   stop analysis after the specified checkpoint is 
                               complete. VALUE can be the checkpoint name or 
                               number
 
 
Other options:
  -h, --help                 show this message and exit
  -v, --version              print version and exit

```


### download the datasets

```
wget http://canvas-cnv-public.s3.amazonaws.com/GRCh38/WholeGenomeFasta/GenomeSize.xml
wget http://canvas-cnv-public.s3.amazonaws.com/GRCh38/kmer.fa
wget http://canvas-cnv-public.s3.amazonaws.com/GRCh38/GRCh38/filter13.bed
```



```
$ head filter13.bed
1	122026460	125184587	centromere
2	92188146	94090557	centromere
3	90772459	93655574	centromere
4	49708101	51743951	centromere
5	46485901	50059807	centromere
6	58553889	59829934	centromere
7	58169654	60828234	centromere
8	44033745	45877265	centromere
9	43236168	45518558	centromere
10	39686683	41593521	centromere

```


```
$ head GenomeSize.xml
<sequenceSizes genomeName="Homo sapiens (GRCh38)">
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="1" totalBases="248956422" build="GRCh38" isCircular="false" md5="2648ae1bacce4ec4b6cf337dcae37816" ploidy="2" species="Homo_sapiens" knownBases="230481012" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="10" totalBases="133797422" build="GRCh38" isCircular="false" md5="907112d17fcb73bcab1ed1c72b97ce68" ploidy="2" species="Homo_sapiens" knownBases="133262962" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="11" totalBases="135086622" build="GRCh38" isCircular="false" md5="1511375dc2dd1b633af8cf439ae90cec" ploidy="2" species="Homo_sapiens" knownBases="134533742" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="12" totalBases="133275309" build="GRCh38" isCircular="false" md5="e81e16d3f44337034695a29b97708fce" ploidy="2" species="Homo_sapiens" knownBases="133137816" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="13" totalBases="114364328" build="GRCh38" isCircular="false" md5="17dab79b963ccd8e7377cef59a54fe1c" ploidy="2" species="Homo_sapiens" knownBases="97983125" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="14" totalBases="107043718" build="GRCh38" isCircular="false" md5="acbd9552c059d9b403e75ed26c1ce5bc" ploidy="2" species="Homo_sapiens" knownBases="90568149" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="15" totalBases="101991189" build="GRCh38" isCircular="false" md5="f036bd11158407596ca6bf3581454706" ploidy="2" species="Homo_sapiens" knownBases="84641325" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="16" totalBases="90338345" build="GRCh38" isCircular="false" md5="24e7cabfba3548a2bb4dff582b9ee870" ploidy="2" species="Homo_sapiens" knownBases="81805943" type="Autosome"/>
  <chromosome fileName="Homo_sapiens.GRCh38.dna.primary_assembly.fa" contigName="17" totalBases="83257441" build="GRCh38" isCircular="false" md5="a8499ca51d6fb77332c2d242923994eb" ploidy="2" species="Homo_sapiens" knownBases="82920204" type="Autosome"/>

```



#### Get the target dataset by based on genomne

Split the genome to chromosomes

```
faSplit byname Homo_sapiens.GRCh38.dna.primary_assembly.fa Chrs/

```


#### get the GenomeSize file
```
python ~/github/NanoHub/src/NanoHub/GenomeSize.py --fasta 
Homo_sapiens.GRCh38.dna.primary_assembly.fa --out GenomeSize.xml --target "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X,Y"
```



#### get vcf file with SNV record, FILT column must be "PASS"

```
$ sed 's/\t\.\tAC/\t\PASS\tAC/g' M625.all.vcf > M625.all_temp.vcf
```


### convert genome to kmer3
```
$ /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/Tools/FlagUniqueKmers/FlagUniqueKmers --help
Usage info:
  FlagUniqueKmers $InputFASTA $OutputFASTA

```



### run Canvas for a trio


```
Canvas SmallPedigree-WGS --bam=M625-0/M625-0.bqsr.bam --bam=M625-1/M625-1.bqsr.bam  --bam=M625-2/M625-2.bqsr.bam  --sample-b-allele-vcf  /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa -g /home/wuzhikun/database/genome/GRCh38/CanvasGenome  -f /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -o M625_pred
```


output files:
```
-rw-rw-r-- 1    0 May 24 20:00 CanvasError.txt
-rw-rw-r-- 1  96K May 24 20:37 CanvasLog.txt
drwxrwxr-x 1 4.0K May 24 20:34 CanvasPedigreeCaller
drwxrwxr-x 1 4.0K May 24 20:37 Checkpoints
-rw-rw-r-- 1  64K May 24 20:36 CNV.vcf.gz
drwxrwxr-x 1 4.0K May 24 20:34 Logging
drwxrwxr-x 1 4.0K May 24 20:26 TempCNV
drwxrwxr-x 1 4.0K May 24 20:36 TempCNV_M625-0
drwxrwxr-x 1 4.0K May 24 20:37 TempCNV_M625-1
drwxrwxr-x 1 4.0K May 24 20:37 TempCNV_M625-2
drwxrwxr-x 1 4.0K May 24 20:36 VisualizationTempM625-0
drwxrwxr-x 1 4.0K May 24 20:37 VisualizationTempM625-1
drwxrwxr-x 1 4.0K May 24 20:37 VisualizationTempM625-2

```

### get CNV bed
```

grep -v 'Canvas:REF' CNV.vcf | grep -v '^#' |  cut -f 3 | cut -d ":" -f 3-4 | sed 's/:/\t/g' | sed 's/-/\t/g'  > CNV.bed

awk '{print $0"\t"$1"_"$2"_"$3}' CNV.bed  > temp
```


#### record of running
```
2019-05-24T20:00:04+08:00, 
2019-05-24T20:00:04+08:00,Running checkpoint 01: Validate input
2019-05-24T20:00:05+08:00,Running Canvas SmallPedigree-WGS 1.40.0.1613+master
2019-05-24T20:00:05+08:00,Command-line arguments: SmallPedigree-WGS --bam=M625-0/M625-0.bqsr.bam --bam=M625-1/M625-1.bqsr.bam --bam=M625-2/M625-2.bqsr.bam --sample-b-allele-vcf /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa -g /home/wuzhikun/database/genome/GRCh38/CanvasGenome -f /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -o M625_pred
Invoking 24 processor jobs...for sample M625-0
CanvasSNV start for sample M625-0
2019-05-24T20:00:05+08:00,Checkpoint 01 Validate input complete. Elapsed time (hh/mm/ss): 00:00:00.4
2019-05-24T20:00:06+08:00, 
2019-05-24T20:00:06+08:00,Running checkpoint 02: CanvasSNV
2019-05-24T20:00:06+08:00, 
2019-05-24T20:00:06+08:00,Running checkpoint 03: CanvasBin
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'1':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 1 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/1-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'11':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 11 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/11-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'15':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 15 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/15-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'12':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 12 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/12-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'2':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 2 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/2-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'18':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 18 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/18-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'16':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 16 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/16-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'10':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 10 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/10-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'17':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 17 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/17-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'19':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 19 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/19-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'13':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 13 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/13-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:00:06+08:00,Launching process for job CanvasSNV-'M625-0'-'14':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 14 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/14-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:03:14+08:00,Job CanvasSNV-'M625-0'-'14' duration: 00:03:08.3
2019-05-24T20:03:14+08:00,Launching process for job CanvasSNV-'M625-0'-'20':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 20 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/20-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:03:17+08:00,Job CanvasSNV-'M625-0'-'19' duration: 00:03:11.3
2019-05-24T20:03:17+08:00,Launching process for job CanvasSNV-'M625-0'-'21':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 21 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/21-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:03:18+08:00,Job CanvasSNV-'M625-0'-'13' duration: 00:03:12.2
2019-05-24T20:03:18+08:00,Launching process for job CanvasSNV-'M625-0'-'22':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 22 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/22-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:03:24+08:00,Job CanvasSNV-'M625-0'-'15' duration: 00:03:17.6
2019-05-24T20:03:24+08:00,Launching process for job CanvasSNV-'M625-0'-'3':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 3 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/3-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:03:43+08:00,Job CanvasSNV-'M625-0'-'17' duration: 00:03:37.4
2019-05-24T20:03:43+08:00,Launching process for job CanvasSNV-'M625-0'-'4':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 4 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/4-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:03:46+08:00,Job CanvasSNV-'M625-0'-'16' duration: 00:03:40.0
2019-05-24T20:03:46+08:00,Launching process for job CanvasSNV-'M625-0'-'5':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 5 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/5-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:03:49+08:00,Job CanvasSNV-'M625-0'-'11' duration: 00:03:43.0
2019-05-24T20:03:49+08:00,Launching process for job CanvasSNV-'M625-0'-'6':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 6 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/6-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:04:00+08:00,Job CanvasSNV-'M625-0'-'18' duration: 00:03:54.0
2019-05-24T20:04:00+08:00,Launching process for job CanvasSNV-'M625-0'-'7':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 7 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/7-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:04:01+08:00,Job CanvasSNV-'M625-0'-'10' duration: 00:03:54.7
2019-05-24T20:04:01+08:00,Launching process for job CanvasSNV-'M625-0'-'8':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 8 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/8-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:04:09+08:00,Job CanvasSNV-'M625-0'-'12' duration: 00:04:02.7
2019-05-24T20:04:09+08:00,Launching process for job CanvasSNV-'M625-0'-'9':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 9 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/9-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:05:43+08:00,Job CanvasSNV-'M625-0'-'2' duration: 00:05:37.3
2019-05-24T20:05:43+08:00,Launching process for job CanvasSNV-'M625-0'-'X':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c X -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/X-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:05:48+08:00,Job CanvasSNV-'M625-0'-'1' duration: 00:05:42.2
2019-05-24T20:05:48+08:00,Launching process for job CanvasSNV-'M625-0'-'Y':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c Y -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/Y-M625-0.SNV.txt.gz -n M625-0
2019-05-24T20:06:01+08:00,Job CanvasSNV-'M625-0'-'22' duration: 00:02:42.4
2019-05-24T20:06:01+08:00,Launching process for job M625-0_0_1.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 1 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_1.dat" 
2019-05-24T20:06:04+08:00,Job CanvasSNV-'M625-0'-'21' duration: 00:02:46.4
2019-05-24T20:06:04+08:00,Launching process for job M625-0_0_2.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 2 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_2.dat" 
2019-05-24T20:06:46+08:00,Job CanvasSNV-'M625-0'-'20' duration: 00:03:31.3
2019-05-24T20:06:46+08:00,Launching process for job M625-0_0_3.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 3 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_3.dat" 
2019-05-24T20:07:36+08:00,Job CanvasSNV-'M625-0'-'9' duration: 00:03:26.9
2019-05-24T20:07:36+08:00,Launching process for job M625-0_0_4.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 4 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_4.dat" 
2019-05-24T20:07:56+08:00,Job CanvasSNV-'M625-0'-'7' duration: 00:03:55.4
2019-05-24T20:07:56+08:00,Launching process for job M625-0_0_5.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 5 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_5.dat" 
2019-05-24T20:07:59+08:00,Job CanvasSNV-'M625-0'-'Y' duration: 00:02:11.1
2019-05-24T20:07:59+08:00,Launching process for job M625-0_0_6.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 6 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_6.dat" 
2019-05-24T20:08:03+08:00,Job CanvasSNV-'M625-0'-'8' duration: 00:04:02.2
2019-05-24T20:08:03+08:00,Launching process for job M625-0_0_7.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 7 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_7.dat" 
2019-05-24T20:08:22+08:00,Job CanvasSNV-'M625-0'-'5' duration: 00:04:35.8
2019-05-24T20:08:22+08:00,Launching process for job M625-0_0_X.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c X -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_X.dat" 
2019-05-24T20:08:32+08:00,Job CanvasSNV-'M625-0'-'6' duration: 00:04:42.7
2019-05-24T20:08:32+08:00,Launching process for job M625-0_0_8.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 8 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_8.dat" 
2019-05-24T20:08:34+08:00,Job CanvasSNV-'M625-0'-'3' duration: 00:05:10.0
2019-05-24T20:08:34+08:00,Launching process for job M625-0_0_9.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 9 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_9.dat" 
2019-05-24T20:08:45+08:00,Job M625-0_0_1.dat duration: 00:02:44.5
2019-05-24T20:08:45+08:00,Launching process for job M625-0_0_11.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 11 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_11.dat" 
2019-05-24T20:08:55+08:00,Job M625-0_0_2.dat duration: 00:02:51.4
2019-05-24T20:08:55+08:00,Launching process for job M625-0_0_10.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 10 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_10.dat" 
2019-05-24T20:09:12+08:00,Job CanvasSNV-'M625-0'-'X' duration: 00:03:28.7
2019-05-24T20:09:12+08:00,Launching process for job M625-0_0_12.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 12 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_12.dat" 
2019-05-24T20:09:17+08:00,Job M625-0_0_3.dat duration: 00:02:31.2
2019-05-24T20:09:17+08:00,Launching process for job M625-0_0_13.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 13 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_13.dat" 
2019-05-24T20:09:21+08:00,Job CanvasSNV-'M625-0'-'4' duration: 00:05:37.7
CanvasSNV complete for sample M625-0
2019-05-24T20:09:21+08:00,Launching process for job M625-0_0_14.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 14 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_14.dat" 
2019-05-24T20:09:32+08:00,Begin converting '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/VFResultsM625-0.txt.gz.baf' to '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/ballele.bedgraph.gz'
2019-05-24T20:09:34+08:00,Job M625-0_0_X.dat duration: 00:01:11.9
2019-05-24T20:09:34+08:00,Launching process for job M625-0_0_15.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 15 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_15.dat" 
2019-05-24T20:10:02+08:00,Job M625-0_0_7.dat duration: 00:01:58.9
2019-05-24T20:10:02+08:00,Launching process for job M625-0_0_16.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 16 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_16.dat" 
2019-05-24T20:10:05+08:00,Job M625-0_0_4.dat duration: 00:02:29.3
2019-05-24T20:10:05+08:00,Launching process for job M625-0_0_17.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 17 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_17.dat" 
2019-05-24T20:10:07+08:00,Job M625-0_0_6.dat duration: 00:02:07.5
2019-05-24T20:10:07+08:00,Launching process for job M625-0_0_18.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 18 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_18.dat" 
2019-05-24T20:10:10+08:00,Job M625-0_0_9.dat duration: 00:01:35.9
2019-05-24T20:10:10+08:00,Launching process for job M625-0_0_20.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 20 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_20.dat" 
2019-05-24T20:10:13+08:00,Job M625-0_0_5.dat duration: 00:02:17.5
2019-05-24T20:10:13+08:00,Launching process for job M625-0_0_19.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 19 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_19.dat" 
2019-05-24T20:10:23+08:00,Job M625-0_0_11.dat duration: 00:01:37.2
2019-05-24T20:10:23+08:00,Launching process for job M625-0_0_Y.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c Y -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_Y.dat" 
2019-05-24T20:10:23+08:00,Job M625-0_0_8.dat duration: 00:01:51.1
2019-05-24T20:10:23+08:00,Launching process for job M625-0_0_22.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 22 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_22.dat" 
2019-05-24T20:10:36+08:00,Job M625-0_0_10.dat duration: 00:01:40.3
2019-05-24T20:10:36+08:00,Launching process for job M625-0_0_21.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 21 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_21.dat" 
2019-05-24T20:10:39+08:00,Job M625-0_0_14.dat duration: 00:01:17.4
2019-05-24T20:10:39+08:00,Launching process for job M625-1_1_1.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 1 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_1.dat" 
2019-05-24T20:10:39+08:00,Job M625-0_0_13.dat duration: 00:01:21.9
2019-05-24T20:10:39+08:00,Launching process for job M625-1_1_2.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 2 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_2.dat" 
2019-05-24T20:10:44+08:00,Job M625-0_0_15.dat duration: 00:01:09.7
2019-05-24T20:10:44+08:00,Launching process for job M625-1_1_3.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 3 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_3.dat" 
2019-05-24T20:11:01+08:00,Job M625-0_0_12.dat duration: 00:01:49.2
2019-05-24T20:11:01+08:00,Launching process for job M625-1_1_4.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 4 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_4.dat" 
2019-05-24T20:11:02+08:00,Job M625-0_0_Y.dat duration: 00:00:39.0
2019-05-24T20:11:02+08:00,Launching process for job M625-1_1_5.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 5 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_5.dat" 
2019-05-24T20:11:02+08:00,Job M625-0_0_22.dat duration: 00:00:39.1
2019-05-24T20:11:02+08:00,Launching process for job M625-1_1_6.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 6 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_6.dat" 
2019-05-24T20:11:06+08:00,Job M625-0_0_19.dat duration: 00:00:53.1
2019-05-24T20:11:06+08:00,Launching process for job M625-1_1_7.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 7 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_7.dat" 
2019-05-24T20:11:07+08:00,Job M625-0_0_20.dat duration: 00:00:57.1
2019-05-24T20:11:07+08:00,Launching process for job M625-1_1_X.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c X -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_X.dat" 
2019-05-24T20:11:19+08:00,Job M625-0_0_17.dat duration: 00:01:13.9
2019-05-24T20:11:19+08:00,Launching process for job M625-1_1_8.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 8 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_8.dat" 
2019-05-24T20:11:19+08:00,Job M625-0_0_16.dat duration: 00:01:17.0
2019-05-24T20:11:19+08:00,Launching process for job M625-1_1_9.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 9 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_9.dat" 
2019-05-24T20:11:21+08:00,Job M625-0_0_18.dat duration: 00:01:14.0
2019-05-24T20:11:21+08:00,Launching process for job M625-1_1_11.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 11 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_11.dat" 
2019-05-24T20:11:24+08:00,Job M625-0_0_21.dat duration: 00:00:48.1
2019-05-24T20:11:24+08:00,Launching process for job M625-1_1_10.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 10 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_10.dat" 
2019-05-24T20:12:24+08:00,Job M625-1_1_X.dat duration: 00:01:17.1
2019-05-24T20:12:24+08:00,Launching process for job M625-1_1_12.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 12 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_12.dat" 
2019-05-24T20:12:57+08:00,Job M625-1_1_9.dat duration: 00:01:38.2
2019-05-24T20:12:57+08:00,Launching process for job M625-1_1_13.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 13 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_13.dat" 
2019-05-24T20:13:00+08:00,Job M625-1_1_11.dat duration: 00:01:39.1
2019-05-24T20:13:00+08:00,Launching process for job M625-1_1_14.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 14 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_14.dat" 
2019-05-24T20:13:05+08:00,Job M625-1_1_10.dat duration: 00:01:41.0
2019-05-24T20:13:05+08:00,Launching process for job M625-1_1_15.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 15 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_15.dat" 
2019-05-24T20:13:12+08:00,Job M625-1_1_7.dat duration: 00:02:06.1
2019-05-24T20:13:12+08:00,Launching process for job M625-1_1_16.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 16 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_16.dat" 
2019-05-24T20:13:13+08:00,Job M625-1_1_6.dat duration: 00:02:10.6
2019-05-24T20:13:13+08:00,Launching process for job M625-1_1_17.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 17 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_17.dat" 
2019-05-24T20:13:17+08:00,Job M625-1_1_8.dat duration: 00:01:58.2
2019-05-24T20:13:17+08:00,Launching process for job M625-1_1_18.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 18 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_18.dat" 
2019-05-24T20:13:24+08:00,Job M625-1_1_3.dat duration: 00:02:40.4
2019-05-24T20:13:24+08:00,Launching process for job M625-1_1_20.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 20 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_20.dat" 
2019-05-24T20:13:25+08:00,Job M625-1_1_5.dat duration: 00:02:23.7
2019-05-24T20:13:25+08:00,Launching process for job M625-1_1_19.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 19 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_19.dat" 
2019-05-24T20:13:39+08:00,Job M625-1_1_1.dat duration: 00:02:59.8
2019-05-24T20:13:39+08:00,Launching process for job M625-1_1_Y.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c Y -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_Y.dat" 
2019-05-24T20:13:41+08:00,Job M625-1_1_4.dat duration: 00:02:40.0
2019-05-24T20:13:41+08:00,Launching process for job M625-1_1_22.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 22 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_22.dat" 
2019-05-24T20:13:51+08:00,Job M625-1_1_2.dat duration: 00:03:11.8
2019-05-24T20:13:51+08:00,Launching process for job M625-1_1_21.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 21 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_21.dat" 
2019-05-24T20:14:02+08:00,Job M625-1_1_12.dat duration: 00:01:38.5
2019-05-24T20:14:03+08:00,Launching process for job M625-2_2_1.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 1 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_1.dat" 
2019-05-24T20:14:11+08:00,Job M625-1_1_14.dat duration: 00:01:11.1
2019-05-24T20:14:11+08:00,Launching process for job M625-2_2_2.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 2 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_2.dat" 
2019-05-24T20:14:15+08:00,Job M625-1_1_19.dat duration: 00:00:49.4
2019-05-24T20:14:15+08:00,Launching process for job M625-2_2_3.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 3 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_3.dat" 
2019-05-24T20:14:16+08:00,Job M625-1_1_15.dat duration: 00:01:11.4
2019-05-24T20:14:16+08:00,Launching process for job M625-2_2_4.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 4 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_4.dat" 
2019-05-24T20:14:17+08:00,Job M625-1_1_13.dat duration: 00:01:19.2
2019-05-24T20:14:17+08:00,Launching process for job M625-2_2_5.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 5 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_5.dat" 
2019-05-24T20:14:21+08:00,Job M625-1_1_Y.dat duration: 00:00:42.4
2019-05-24T20:14:21+08:00,Launching process for job M625-2_2_6.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 6 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_6.dat" 
2019-05-24T20:14:24+08:00,Job M625-1_1_22.dat duration: 00:00:42.6
2019-05-24T20:14:24+08:00,Launching process for job M625-2_2_7.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 7 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_7.dat" 
2019-05-24T20:14:24+08:00,Job M625-1_1_17.dat duration: 00:01:11.4
2019-05-24T20:14:24+08:00,Launching process for job M625-2_2_X.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c X -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_X.dat" 
2019-05-24T20:14:26+08:00,Job M625-1_1_16.dat duration: 00:01:13.6
2019-05-24T20:14:27+08:00,Launching process for job M625-2_2_8.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 8 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_8.dat" 
2019-05-24T20:14:27+08:00,Job M625-1_1_20.dat duration: 00:01:03.1
2019-05-24T20:14:27+08:00,Launching process for job M625-2_2_9.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 9 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_9.dat" 
2019-05-24T20:14:31+08:00,Job M625-1_1_18.dat duration: 00:01:13.8
2019-05-24T20:14:31+08:00,Launching process for job M625-2_2_11.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 11 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_11.dat" 
2019-05-24T20:14:43+08:00,Job M625-1_1_21.dat duration: 00:00:52.4
2019-05-24T20:14:43+08:00,Launching process for job M625-2_2_10.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 10 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_10.dat" 
2019-05-24T20:16:50+08:00,Job M625-2_2_9.dat duration: 00:02:22.6
2019-05-24T20:16:50+08:00,Launching process for job M625-2_2_12.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 12 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_12.dat" 
2019-05-24T20:16:53+08:00,Job M625-2_2_11.dat duration: 00:02:21.4
2019-05-24T20:16:53+08:00,Launching process for job M625-2_2_13.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 13 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_13.dat" 
2019-05-24T20:17:02+08:00,Job M625-2_2_10.dat duration: 00:02:18.9
2019-05-24T20:17:02+08:00,Launching process for job M625-2_2_14.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 14 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_14.dat" 
2019-05-24T20:17:09+08:00,Job M625-2_2_8.dat duration: 00:02:41.7
2019-05-24T20:17:09+08:00,Launching process for job M625-2_2_15.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 15 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_15.dat" 
2019-05-24T20:17:13+08:00,Job M625-2_2_7.dat duration: 00:02:49.2
2019-05-24T20:17:13+08:00,Launching process for job M625-2_2_16.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 16 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_16.dat" 
2019-05-24T20:17:14+08:00,Job M625-2_2_X.dat duration: 00:02:50.1
2019-05-24T20:17:14+08:00,Launching process for job M625-2_2_17.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 17 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_17.dat" 
2019-05-24T20:17:18+08:00,Job M625-2_2_6.dat duration: 00:02:57.1
2019-05-24T20:17:18+08:00,Launching process for job M625-2_2_18.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 18 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_18.dat" 
2019-05-24T20:17:28+08:00,Job M625-2_2_5.dat duration: 00:03:11.4
2019-05-24T20:17:28+08:00,Launching process for job M625-2_2_20.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 20 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_20.dat" 
2019-05-24T20:17:38+08:00,Job M625-2_2_3.dat duration: 00:03:22.8
2019-05-24T20:17:38+08:00,Launching process for job M625-2_2_19.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 19 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_19.dat" 
2019-05-24T20:17:40+08:00,Job M625-2_2_4.dat duration: 00:03:23.5
2019-05-24T20:17:40+08:00,Launching process for job M625-2_2_Y.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c Y -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_Y.dat" 
2019-05-24T20:17:59+08:00,Job M625-2_2_1.dat duration: 00:03:56.8
2019-05-24T20:17:59+08:00,Launching process for job M625-2_2_22.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 22 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_22.dat" 
2019-05-24T20:18:00+08:00,Job M625-2_2_Y.dat duration: 00:00:20.2
2019-05-24T20:18:00+08:00,Launching process for job M625-2_2_21.dat:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -c 21 -m TruncatedDynamicRange -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_21.dat" 
2019-05-24T20:18:19+08:00,Job M625-2_2_2.dat duration: 00:04:07.8
2019-05-24T20:18:19+08:00,Launching process for job tabix-index-tmp-ballele.bedgraph.gz.1:
bash -o pipefail -c " /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/tabix -p bed -f /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/ballele.bedgraph.gz  "
2019-05-24T20:18:25+08:00,Job M625-2_2_13.dat duration: 00:01:32.4
2019-05-24T20:18:26+08:00,Job tabix-index-tmp-ballele.bedgraph.gz.1 duration: 00:00:06.6
Invoking 24 processor jobs...for sample M625-1
CanvasSNV start for sample M625-1
2019-05-24T20:18:26+08:00,Finished converting '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/VFResultsM625-0.txt.gz.baf' to '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/ballele.bedgraph.gz'. Elapsed time: 00:08:54.0
2019-05-24T20:18:26+08:00,Launching process for job CanvasSNV-'M625-1'-'1':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 1 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/1-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:26+08:00,Launching process for job CanvasSNV-'M625-1'-'10':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 10 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/10-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:27+08:00,Job M625-2_2_14.dat duration: 00:01:25.1
2019-05-24T20:18:27+08:00,Launching process for job CanvasSNV-'M625-1'-'11':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 11 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/11-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:34+08:00,Job M625-2_2_15.dat duration: 00:01:24.7
2019-05-24T20:18:34+08:00,Launching process for job CanvasSNV-'M625-1'-'12':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 12 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/12-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:36+08:00,Job M625-2_2_18.dat duration: 00:01:17.5
2019-05-24T20:18:36+08:00,Launching process for job CanvasSNV-'M625-1'-'13':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 13 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/13-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:38+08:00,Job M625-2_2_20.dat duration: 00:01:09.9
2019-05-24T20:18:38+08:00,Launching process for job CanvasSNV-'M625-1'-'14':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 14 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/14-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:38+08:00,Job M625-2_2_19.dat duration: 00:01:00.6
2019-05-24T20:18:39+08:00,Launching process for job CanvasSNV-'M625-1'-'15':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 15 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/15-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:39+08:00,Job M625-2_2_16.dat duration: 00:01:25.0
2019-05-24T20:18:39+08:00,Launching process for job CanvasSNV-'M625-1'-'16':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 16 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/16-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:40+08:00,Job M625-2_2_17.dat duration: 00:01:25.5
2019-05-24T20:18:40+08:00,Launching process for job CanvasSNV-'M625-1'-'17':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 17 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/17-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:44+08:00,Job M625-2_2_22.dat duration: 00:00:44.4
2019-05-24T20:18:44+08:00,Launching process for job CanvasSNV-'M625-1'-'18':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 18 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/18-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:49+08:00,Job M625-2_2_12.dat duration: 00:01:58.9
2019-05-24T20:18:49+08:00,Launching process for job CanvasSNV-'M625-1'-'19':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 19 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/19-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:18:54+08:00,Job M625-2_2_21.dat duration: 00:00:53.5
Start deserialization:
Start deserialization:
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_1.dat
2019-05-24T20:18:54+08:00,Launching process for job CanvasSNV-'M625-1'-'2':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 2 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/2-M625-1.SNV.txt.gz -n M625-1
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_1.dat
Time elapsed: 00:00:03.4592020
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_2.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_2.dat
Time elapsed: 00:00:02.0898334
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_3.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_3.dat
Time elapsed: 00:00:02.0720335
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_4.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_4.dat
Time elapsed: 00:00:01.1741000
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_5.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_5.dat
Time elapsed: 00:00:02.2005697
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_6.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_6.dat
Time elapsed: 00:00:00.6385778
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_7.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_7.dat
Time elapsed: 00:00:01.0594423
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_X.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_X.dat
Time elapsed: 00:00:01.3293022
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_8.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_8.dat
Time elapsed: 00:00:01.2481007
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_9.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_9.dat
Time elapsed: 00:00:01.5108325
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_11.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_11.dat
Time elapsed: 00:00:00.9585610
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_10.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_10.dat
Time elapsed: 00:00:01.2889790
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_12.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_12.dat
Time elapsed: 00:00:01.3976133
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_13.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_13.dat
Time elapsed: 00:00:01.3456022
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_14.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_14.dat
Time elapsed: 00:00:00.6251376
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_15.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_15.dat
Time elapsed: 00:00:01.1011346
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_16.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_16.dat
Time elapsed: 00:00:00.4122514
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_17.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_17.dat
Time elapsed: 00:00:00.6951986
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_18.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_18.dat
Time elapsed: 00:00:00.5345820
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_20.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_20.dat
Time elapsed: 00:00:00.6713319
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_19.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_19.dat
Time elapsed: 00:00:00.6199362
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_Y.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_Y.dat
Time elapsed: 00:00:00.7170079
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_22.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_22.dat
Time elapsed: 00:00:00.4317727
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_21.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_21.dat
Time elapsed: 00:00:00.6010108
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_1.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_1.dat
Time elapsed: 00:00:01.6099645
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_2.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_2.dat
Time elapsed: 00:00:01.6880168
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_3.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_3.dat
Time elapsed: 00:00:01.7123551
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_4.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_4.dat
Time elapsed: 00:00:01.7403853
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_5.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_5.dat
Time elapsed: 00:00:01.4999769
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_6.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_6.dat
Time elapsed: 00:00:01.6939641
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_7.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_7.dat
Time elapsed: 00:00:01.1953367
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_X.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_X.dat
Time elapsed: 00:00:00.9427032
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_8.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_8.dat
Time elapsed: 00:00:00.8600430
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_9.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_9.dat
Time elapsed: 00:00:01.8008431
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_11.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_11.dat
Time elapsed: 00:00:01.3644564
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_10.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_10.dat
Time elapsed: 00:00:01.0134046
2019-05-24T20:20:56+08:00,Job CanvasSNV-'M625-1'-'19' duration: 00:02:07.1
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_12.dat
2019-05-24T20:20:57+08:00,Job CanvasSNV-'M625-1'-'15' duration: 00:02:18.8
2019-05-24T20:20:57+08:00,Launching process for job CanvasSNV-'M625-1'-'20':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 20 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/20-M625-1.SNV.txt.gz -n M625-1
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_12.dat
Time elapsed: 00:00:01.2746370
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_13.dat
2019-05-24T20:21:01+08:00,Job CanvasSNV-'M625-1'-'14' duration: 00:02:22.5
2019-05-24T20:21:01+08:00,Launching process for job CanvasSNV-'M625-1'-'21':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 21 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/21-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:21:01+08:00,Launching process for job CanvasSNV-'M625-1'-'22':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 22 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/22-M625-1.SNV.txt.gz -n M625-1
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_13.dat
Time elapsed: 00:00:00.9538528
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_14.dat
2019-05-24T20:21:01+08:00,Job CanvasSNV-'M625-1'-'17' duration: 00:02:21.2
2019-05-24T20:21:03+08:00,Launching process for job CanvasSNV-'M625-1'-'3':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 3 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/3-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:21:03+08:00,Job CanvasSNV-'M625-1'-'16' duration: 00:02:24.3
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_14.dat
Time elapsed: 00:00:01.8719888
2019-05-24T20:21:03+08:00,Launching process for job CanvasSNV-'M625-1'-'4':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 4 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/4-M625-1.SNV.txt.gz -n M625-1
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_15.dat
2019-05-24T20:21:06+08:00,Job CanvasSNV-'M625-1'-'13' duration: 00:02:29.7
2019-05-24T20:21:06+08:00,Launching process for job CanvasSNV-'M625-1'-'5':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 5 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/5-M625-1.SNV.txt.gz -n M625-1
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_15.dat
Time elapsed: 00:00:00.9638629
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_16.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_16.dat
Time elapsed: 00:00:00.5632645
2019-05-24T20:21:09+08:00,Job CanvasSNV-'M625-1'-'18' duration: 00:02:25.3
2019-05-24T20:21:09+08:00,Launching process for job CanvasSNV-'M625-1'-'6':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 6 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/6-M625-1.SNV.txt.gz -n M625-1
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_17.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_17.dat
Time elapsed: 00:00:00.7836821
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_18.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_18.dat
Time elapsed: 00:00:00.7317061
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_20.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_20.dat
Time elapsed: 00:00:00.6363867
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_19.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_19.dat
Time elapsed: 00:00:00.3886583
2019-05-24T20:21:17+08:00,Job CanvasSNV-'M625-1'-'11' duration: 00:02:49.4
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_Y.dat
2019-05-24T20:21:17+08:00,Launching process for job CanvasSNV-'M625-1'-'7':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 7 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/7-M625-1.SNV.txt.gz -n M625-1
2019-05-24T20:21:17+08:00,Job CanvasSNV-'M625-1'-'10' duration: 00:02:51.1
2019-05-24T20:21:17+08:00,Launching process for job CanvasSNV-'M625-1'-'8':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 8 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/8-M625-1.SNV.txt.gz -n M625-1
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_Y.dat
Time elapsed: 00:00:00.8623265
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_22.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_22.dat
Time elapsed: 00:00:00.7525251
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_21.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_21.dat
Time elapsed: 00:00:00.3983318
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_1.dat
2019-05-24T20:21:24+08:00,Job CanvasSNV-'M625-1'-'12' duration: 00:02:49.8
2019-05-24T20:21:24+08:00,Launching process for job CanvasSNV-'M625-1'-'9':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 9 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/9-M625-1.SNV.txt.gz -n M625-1
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_1.dat
Time elapsed: 00:00:02.2925952
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_2.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_2.dat
Time elapsed: 00:00:02.6381049
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_3.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_3.dat
Time elapsed: 00:00:01.3906198
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_4.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_4.dat
Time elapsed: 00:00:01.4685963
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_5.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_5.dat
Time elapsed: 00:00:01.0201624
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_6.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_6.dat
Time elapsed: 00:00:01.4219040
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_7.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_7.dat
Time elapsed: 00:00:00.8803733
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_X.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_X.dat
Time elapsed: 00:00:01.2261798
2019-05-24T20:21:57+08:00,Job CanvasSNV-'M625-1'-'1' duration: 00:03:30.6
2019-05-24T20:21:57+08:00,Launching process for job CanvasSNV-'M625-1'-'X':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c X -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/X-M625-1.SNV.txt.gz -n M625-1
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_8.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_8.dat
Time elapsed: 00:00:01.5101729
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_9.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_9.dat
Time elapsed: 00:00:01.6945562
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_11.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_11.dat
Time elapsed: 00:00:00.9033976
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_10.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_10.dat
Time elapsed: 00:00:01.4161139
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_12.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_12.dat
Time elapsed: 00:00:01.1375256
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_13.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_13.dat
Time elapsed: 00:00:00.7374263
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_14.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_14.dat
Time elapsed: 00:00:00.6511874
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_15.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_15.dat
Time elapsed: 00:00:01.2250755
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_16.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_16.dat
Time elapsed: 00:00:01.1156674
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_17.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_17.dat
Time elapsed: 00:00:00.8478244
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_18.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_18.dat
Time elapsed: 00:00:00.6888346
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_20.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_20.dat
Time elapsed: 00:00:00.8849630
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_19.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_19.dat
Time elapsed: 00:00:00.6994405
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_Y.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_Y.dat
Time elapsed: 00:00:00.4551813
2019-05-24T20:22:34+08:00,Job CanvasSNV-'M625-1'-'2' duration: 00:03:40.2
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_22.dat
2019-05-24T20:22:34+08:00,Launching process for job CanvasSNV-'M625-1'-'Y':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c Y -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/Y-M625-1.SNV.txt.gz -n M625-1
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_22.dat
Time elapsed: 00:00:00.7956411
CanvasBin /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_21.dat
File: /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_21.dat
Time elapsed: 00:00:00.2966677
5/24/19 8:22:37 PM Deserialization complete
1181 binSize
2019-05-24T20:23:02+08:00,Job CanvasSNV-'M625-1'-'22' duration: 00:02:01.1
2019-05-24T20:23:07+08:00,Job CanvasSNV-'M625-1'-'21' duration: 00:02:06.4
2019-05-24T20:23:19+08:00,Job CanvasSNV-'M625-1'-'20' duration: 00:02:21.4
2019-05-24T20:23:19+08:00,Launching process for job M625-1_1.binned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-1/M625-1.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1.binned" -z 1181 -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_1.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_2.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_3.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_4.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_5.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_6.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_7.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_X.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_8.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_9.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_11.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_10.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_12.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_13.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_14.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_15.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_16.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_17.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_18.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_20.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_19.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_Y.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_22.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1_21.dat" -m TruncatedDynamicRange 
2019-05-24T20:23:56+08:00,Job CanvasSNV-'M625-1'-'9' duration: 00:02:32.2
2019-05-24T20:24:03+08:00,Job CanvasSNV-'M625-1'-'8' duration: 00:02:45.2
2019-05-24T20:24:03+08:00,Launching process for job M625-0_0.binned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-0/M625-0.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0.binned" -z 1181 -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_1.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_2.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_3.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_4.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_5.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_6.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_7.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_X.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_8.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_9.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_11.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_10.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_12.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_13.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_14.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_15.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_16.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_17.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_18.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_20.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_19.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_Y.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_22.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0_21.dat" -m TruncatedDynamicRange 
2019-05-24T20:24:12+08:00,Job CanvasSNV-'M625-1'-'6' duration: 00:03:02.7
2019-05-24T20:24:12+08:00,Job CanvasSNV-'M625-1'-'7' duration: 00:02:55.2
2019-05-24T20:24:13+08:00,Job CanvasSNV-'M625-1'-'5' duration: 00:03:07.3
2019-05-24T20:24:14+08:00,Job CanvasSNV-'M625-1'-'3' duration: 00:03:11.1
2019-05-24T20:24:24+08:00,Job CanvasSNV-'M625-1'-'4' duration: 00:03:20.5
2019-05-24T20:24:27+08:00,Job CanvasSNV-'M625-1'-'Y' duration: 00:01:53.2
2019-05-24T20:24:33+08:00,Job CanvasSNV-'M625-1'-'X' duration: 00:02:36.0
CanvasSNV complete for sample M625-1
2019-05-24T20:24:33+08:00,Launching process for job M625-2_2.binned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2.binned" -z 1181 -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_1.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_2.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_3.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_4.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_5.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_6.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_7.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_X.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_8.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_9.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_11.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_10.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_12.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_13.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_14.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_15.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_16.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_17.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_18.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_20.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_19.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_Y.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_22.dat" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2_21.dat" -m TruncatedDynamicRange 
2019-05-24T20:24:43+08:00,Begin converting '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/VFResultsM625-1.txt.gz.baf' to '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/ballele.bedgraph.gz'
2019-05-24T20:25:55+08:00,Job M625-1_1.binned duration: 00:02:36.4
2019-05-24T20:25:55+08:00,Launching process for job tabix-index-tmp-ballele.bedgraph.gz.2:
bash -o pipefail -c " /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/tabix -p bed -f /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/ballele.bedgraph.gz  "
2019-05-24T20:25:59+08:00,Job tabix-index-tmp-ballele.bedgraph.gz.2 duration: 00:00:03.6
Invoking 24 processor jobs...for sample M625-2
CanvasSNV start for sample M625-2
2019-05-24T20:25:59+08:00,Finished converting '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/VFResultsM625-1.txt.gz.baf' to '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/ballele.bedgraph.gz'. Elapsed time: 00:01:16.0
2019-05-24T20:25:59+08:00,Launching process for job CanvasSNV-'M625-2'-'10':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 10 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/10-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:25:59+08:00,Launching process for job CanvasSNV-'M625-2'-'14':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 14 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/14-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:25:59+08:00,Launching process for job CanvasSNV-'M625-2'-'1':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 1 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/1-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:25:59+08:00,Launching process for job CanvasSNV-'M625-2'-'11':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 11 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/11-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:25:59+08:00,Launching process for job CanvasSNV-'M625-2'-'13':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 13 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/13-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:25:59+08:00,Launching process for job CanvasSNV-'M625-2'-'12':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 12 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/12-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:25:59+08:00,Launching process for job CanvasSNV-'M625-2'-'15':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 15 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/15-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:26:21+08:00,Job M625-0_0.binned duration: 00:02:18.1
2019-05-24T20:26:21+08:00,Launching process for job CanvasSNV-'M625-2'-'16':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 16 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/16-M625-2.SNV.txt.gz -n M625-2
Created callset
2019-05-24T20:26:21+08:00,Launching process for job CanvasSNV-'M625-2'-'17':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 17 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/17-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:26:21+08:00,Job M625-2_2.binned duration: 00:01:48.1
2019-05-24T20:26:21+08:00,Launching process for job CanvasSNV-'M625-2'-'18':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 18 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/18-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:26:21+08:00,Launching process for job CanvasSNV-'M625-2'-'2':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 2 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/2-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:26:21+08:00,Launching process for job CanvasSNV-'M625-2'-'19':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 19 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/19-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:26:22+08:00, 
2019-05-24T20:26:22+08:00,Running checkpoint 04: CanvasClean
2019-05-24T20:26:27+08:00,Checkpoint 03 CanvasBin complete. Elapsed time (hh/mm/ss): 00:26:21.7
2019-05-24T20:28:27+08:00,Job CanvasSNV-'M625-2'-'15' duration: 00:02:28.1
2019-05-24T20:28:27+08:00,Launching process for job CanvasSNV-'M625-2'-'20':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 20 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/20-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:28:28+08:00,Job CanvasSNV-'M625-2'-'14' duration: 00:02:29.4
2019-05-24T20:28:29+08:00,Launching process for job CanvasSNV-'M625-2'-'21':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 21 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/21-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:28:34+08:00,Job CanvasSNV-'M625-2'-'13' duration: 00:02:35.2
2019-05-24T20:28:34+08:00,Launching process for job CanvasSNV-'M625-2'-'22':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 22 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/22-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:28:38+08:00,Job CanvasSNV-'M625-2'-'19' duration: 00:02:16.6
2019-05-24T20:28:38+08:00,Launching process for job CanvasSNV-'M625-2'-'3':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 3 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/3-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:28:52+08:00,Job CanvasSNV-'M625-2'-'17' duration: 00:02:31.5
2019-05-24T20:28:52+08:00,Launching process for job CanvasSNV-'M625-2'-'4':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 4 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/4-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:28:56+08:00,Job CanvasSNV-'M625-2'-'16' duration: 00:02:35.2
2019-05-24T20:28:56+08:00,Launching process for job CanvasSNV-'M625-2'-'5':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 5 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/5-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:28:58+08:00,Job CanvasSNV-'M625-2'-'18' duration: 00:02:36.5
2019-05-24T20:28:58+08:00,Launching process for job CanvasSNV-'M625-2'-'6':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 6 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/6-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:28:59+08:00,Job CanvasSNV-'M625-2'-'11' duration: 00:03:00.3
2019-05-24T20:28:59+08:00,Launching process for job CanvasSNV-'M625-2'-'7':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 7 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/7-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:29:02+08:00,Job CanvasSNV-'M625-2'-'10' duration: 00:03:03.3
2019-05-24T20:29:02+08:00,Launching process for job CanvasSNV-'M625-2'-'8':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 8 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/8-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:29:11+08:00,Job CanvasSNV-'M625-2'-'12' duration: 00:03:11.8
2019-05-24T20:29:11+08:00,Launching process for job CanvasSNV-'M625-2'-'9':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 9 -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/9-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:29:52+08:00,Job CanvasSNV-'M625-2'-'1' duration: 00:03:53.2
2019-05-24T20:29:52+08:00,Launching process for job CanvasSNV-'M625-2'-'X':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c X -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/X-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:30:16+08:00,Job CanvasSNV-'M625-2'-'2' duration: 00:03:55.0
2019-05-24T20:30:16+08:00,Launching process for job CanvasSNV-'M625-2'-'Y':
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c Y -v /home/wuzhikun/Project/Illumina_Trio/Trio/M625.all_temp.vcf -b /home/wuzhikun/Project/Illumina_Trio/mapping/M625-2/M625-2.bqsr.bam -o /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/Y-M625-2.SNV.txt.gz -n M625-2
2019-05-24T20:30:39+08:00,Job CanvasSNV-'M625-2'-'22' duration: 00:02:04.3
2019-05-24T20:30:39+08:00,Launching process for job M625-0.cleaned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasClean/CanvasClean.dll -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-0_0.binned" -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/M625-0.cleaned" -g -s -r --local-sd-metric-file "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/LocalSdMetric.txt"
2019-05-24T20:30:45+08:00,Job CanvasSNV-'M625-2'-'21' duration: 00:02:16.2
2019-05-24T20:30:55+08:00,Job CanvasSNV-'M625-2'-'20' duration: 00:02:27.9
2019-05-24T20:30:59+08:00,Job M625-0.cleaned duration: 00:00:20.2
Run InvokeCanvasClean
Created callset
2019-05-24T20:30:59+08:00,Launching process for job M625-1.cleaned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasClean/CanvasClean.dll -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-1_1.binned" -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/M625-1.cleaned" -g -s -r --local-sd-metric-file "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/LocalSdMetric.txt"
2019-05-24T20:31:18+08:00,Job M625-1.cleaned duration: 00:00:18.8
Run InvokeCanvasClean
Created callset
2019-05-24T20:31:18+08:00,Launching process for job M625-2.cleaned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasClean/CanvasClean.dll -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV/M625-2_2.binned" -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/M625-2.cleaned" -g -s -r --local-sd-metric-file "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/LocalSdMetric.txt"
2019-05-24T20:31:37+08:00,Job M625-2.cleaned duration: 00:00:19.5
Run InvokeCanvasClean
2019-05-24T20:31:37+08:00, 
2019-05-24T20:31:37+08:00,Running checkpoint 05: CanvasPartition
2019-05-24T20:31:38+08:00,Checkpoint 04 CanvasClean complete. Elapsed time (hh/mm/ss): 00:05:15.9
Merge and normalize CanvasClean bed files
count 2049626
count 2050687
count 2049441
/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/M625-0.cleaned
2019-05-24T20:31:49+08:00,Job CanvasSNV-'M625-2'-'Y' duration: 00:01:32.7
/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/M625-1.cleaned
/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/M625-2.cleaned
2019-05-24T20:31:55+08:00,Job CanvasSNV-'M625-2'-'9' duration: 00:02:43.6
create GenomeBin intervals
2019-05-24T20:32:06+08:00,Job CanvasSNV-'M625-2'-'8' duration: 00:03:03.8
2019-05-24T20:32:12+08:00,Job CanvasSNV-'M625-2'-'7' duration: 00:03:12.1
2019-05-24T20:32:21+08:00,Job CanvasSNV-'M625-2'-'3' duration: 00:03:43.2
2019-05-24T20:32:23+08:00,Launching process for job M625-0.partitioned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasPartition/CanvasPartition.dll -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/M625-0.cleaned" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/M625-1.cleaned" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/M625-2.cleaned" -b "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/M625-0.partitioned" -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/M625-1.partitioned" -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/M625-2.partitioned" -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome" -m PerSampleHMM
2019-05-24T20:32:23+08:00,Job CanvasSNV-'M625-2'-'5' duration: 00:03:27.1
2019-05-24T20:32:23+08:00,Job CanvasSNV-'M625-2'-'6' duration: 00:03:25.8
2019-05-24T20:32:41+08:00,Job CanvasSNV-'M625-2'-'4' duration: 00:03:48.3
2019-05-24T20:33:42+08:00,Job CanvasSNV-'M625-2'-'X' duration: 00:03:50.0
CanvasSNV complete for sample M625-2
2019-05-24T20:33:53+08:00,Begin converting '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/VFResultsM625-2.txt.gz.baf' to '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/ballele.bedgraph.gz'
2019-05-24T20:34:15+08:00,Launching process for job tabix-index-tmp-ballele.bedgraph.gz.3:
bash -o pipefail -c " /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/tabix -p bed -f /home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/ballele.bedgraph.gz  "
2019-05-24T20:34:17+08:00,Job tabix-index-tmp-ballele.bedgraph.gz.3 duration: 00:00:02.0
2019-05-24T20:34:17+08:00,Finished converting '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/VFResultsM625-2.txt.gz.baf' to '/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/ballele.bedgraph.gz'. Elapsed time: 00:00:23.9
2019-05-24T20:34:17+08:00,Checkpoint 02 CanvasSNV complete. Elapsed time (hh/mm/ss): 00:34:11.0
2019-05-24T20:34:44+08:00,Job M625-0.partitioned duration: 00:02:21.6
2019-05-24T20:34:44+08:00, 
2019-05-24T20:34:44+08:00,Running checkpoint 06: Variant calling
2019-05-24T20:34:44+08:00,Checkpoint 05 CanvasPartition complete. Elapsed time (hh/mm/ss): 00:03:06.9
2019-05-24T20:34:44+08:00,Launching process for job CanvasPedigreeCaller:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasPedigreeCaller/CanvasPedigreeCaller.dll -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/M625-0.partitioned" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/M625-1.partitioned" -i "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/M625-2.partitioned" -v "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-0/VFResultsM625-0.txt.gz" -n "M625-0" -t "Other" -v "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-1/VFResultsM625-1.txt.gz" -n "M625-1" -t "Other" -v "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred/TempCNV_M625-2/VFResultsM625-2.txt.gz" -n "M625-2" -t "Other" -o "/home/wuzhikun/Project/Illumina_Trio/mapping/M625_pred" -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome" 
2019-05-24T20:37:15+08:00,Job CanvasPedigreeCaller duration: 00:02:30.2
2019-05-24T20:37:15+08:00,Checkpoint 06 Variant calling complete. Elapsed time (hh/mm/ss): 00:02:30.4

```



### somatic CNV
```
dotnet Canvas.exe Tumor-normal-enrichment -b $WORKDIR/testing/files/HCC2218C_S1.bam --normal-bam=$WORKDIR/testing/files/HCC2218BL_S1.bam --reference=$WORKDIR/testing/hg19/kmer.fa --manifest=$WORKDIR/testing/files/NexteraRapidCapture_Exome_TargetedRegions_v1.2Used.txt -g $WORKDIR/testing/hg19/ -n HCC2218C -f $WORKDIR/testing/hg19/filter13.bed -o $WORKDIR/testing/HCC2218_v2 --b-allele-vcf=$WORKDIR/testing/files/HCC2218BL_S1.vcf --custom-parameters=CanvasBin,-m=TruncatedDynamicRange
```

### [Paired Somatic WGS?](https://github.com/Illumina/canvas/issues/60)
```
We don't (currently) normalize against the normal sample coverage. This means any germline events may show up in our somatic calls. We do take into account b allele sites from the normal sample though (through the command line) so indirectly it is a T/N analysis.

Other that removing germline events from the somatic call set we do not suspect normalization from a matched normal to provide significant benefits for WGS analysis. For enrichment data coverage normalization is critical though. If there is evidence that coverage normalization for T/N WGS analysis would be beneficial we would be interested in taking a look.
```

```
I've actually never needed to do this due to the fact that germline samples tend to have much fewer events than tumor samples. I thought bcftools isec with the -C option could work, but because CNVs are imprecise events I don't think the exact start/stop positions will line up. It looks like it will need to be a custom script (e.g. python) to exclude events when there is high reciprocal overlap (e.g. >90%).
```



### CanvasSNV


```
$ /home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSNV/CanvasSNV.dll  -c 1 -v /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf -b /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/1-SRR6_germline.SNV.txt.gz
>>>Command-line arguments:
-c 1 -v /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf -b /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/1-SRR6_germline.SNV.txt.gz 
6/1/19 9:39:22 AM Loading variants of interest from /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf
Retained 23930 variants, out of 26331 records for 1
6/1/19 9:39:23 AM Looping over bam records from /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam
Jump to refid 0 1
Record 1000000 at 22509100...
Record 2000000 at 51421764...
Record 3000000 at 103662777...
Record 4000000 at 145680763...
Record 5000000 at 152308480...
Record 6000000 at 173839388...
Record 7000000 at 216247116...
Looped over 7736122 bam records in all
6/1/19 9:39:48 AM Results written to /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/1-SRR6_germline.SNV.txt.gz
6/1/19 9:39:48 AM Results written to /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/1-SRR6_germline.SNV.txt.gz.baf
```


output file 

```
$ less /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/1-SRR6_germline.SNV.txt.gz

#Chromosome     Position        Ref     Alt     CountRef        CountAlt
1       63268   T       C       0       2
1       69270   A       G       0       45
1       69511   A       G       0       230
1       69897   T       C       0       7
1       183697  G       A       6       5
1       183937  G       A       6       14
1       184184  C       T       1       2
1       191852  C       T       1       2
1       191870  C       A       2       2
1       531197  C       T       0       2

```


```
$ less /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/1-SRR6_germline.SNV.txt.gz.baf

Chromosome,Position,BAF
1,63268,0
1,69270,0
1,69511,0
1,69897,0
1,183697,0.454545454545455
1,183937,0.7
1,184184,0.666666666666667
1,191852,0.666666666666667
1,191870,0.5
1,531197,1
1,669365,1

```


### canvasbin
```
$ /home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasBin/CanvasBin.dll -b "/home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam" -p -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa" -f "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -d 100 -o "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/SRR6_germline_0.binned" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_1.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_2.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_3.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_4.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_5.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_6.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_7.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_X.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_8.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_9.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_11.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_10.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_12.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_13.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_14.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_15.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_16.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_17.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_18.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_20.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_19.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_Y.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_22.dat" -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_21.dat" -m TruncatedDynamicRange
>>>Command-line arguments:
-b /home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam -p -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa -f /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -d 100 -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6_germline/SRR6_germline_0.binned -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_1.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_2.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_3.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_4.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_5.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_6.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_7.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_X.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_8.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_9.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_11.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_10.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_12.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_13.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_14.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_15.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_16.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_17.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_18.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_20.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_19.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_Y.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_22.dat -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_21.dat -m TruncatedDynamicRange 
CanvasBin 1.40.0.1613
6/1/19 9:42:36 AM Parsed command-line
Start deserialization:
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_1.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_1.dat
Time elapsed: 00:00:30.5373945
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_2.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_2.dat
Time elapsed: 00:00:24.9640637
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_3.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_3.dat
Time elapsed: 00:00:31.1347181
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_4.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_4.dat
Time elapsed: 00:01:15.4540828
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_5.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_5.dat
Time elapsed: 00:01:48.7435266
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_6.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_6.dat
Time elapsed: 00:00:59.7566087
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_7.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_7.dat
Time elapsed: 00:00:47.8930937
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_X.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_X.dat
Time elapsed: 00:01:06.6872447
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_8.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_8.dat
Time elapsed: 00:01:15.8992305
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_9.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_9.dat
Time elapsed: 00:01:02.7593767
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_11.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_11.dat
Time elapsed: 00:00:40.7662974
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_10.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_10.dat
Time elapsed: 00:01:13.9859236
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_12.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_12.dat
Time elapsed: 00:00:59.3878001
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_13.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_13.dat
Time elapsed: 00:00:24.6843529
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_14.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_14.dat
Time elapsed: 00:00:30.9257838
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_15.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_15.dat
Time elapsed: 00:00:17.9548615
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_16.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_16.dat
Time elapsed: 00:00:11.6746068
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_17.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_17.dat
Time elapsed: 00:00:23.1247499
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_18.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_18.dat
Time elapsed: 00:00:05.0618889
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_20.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_20.dat
Time elapsed: 00:00:07.9551667
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_19.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_19.dat
Time elapsed: 00:00:10.8118460
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_Y.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_Y.dat
Time elapsed: 00:00:01.9224010
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_22.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_22.dat
Time elapsed: 00:00:01.8176613
CanvasBin /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_21.dat
File: /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV/SRR6_germline_0_21.dat
Time elapsed: 00:00:01.7449679
6/1/19 9:58:24 AM Deserialization complete
13634 binSize
6/1/19 10:00:46 AM Launch BinCountsForChromosome jobs...

6/1/19 10:00:53 AM Completed BinCountsForChromosome jobs.

6/1/19 10:00:53 AM Output binned counts:
6/1/19 10:00:53 AM Output complete

```


### [Expecting ploidyVcfFile in CanvasPartition](https://github.com/Illumina/canvas/issues/89)


#### Error

```
Hi,

In the latest version 1.38 when I am running Somatic-WGS workflow, it is expecting a ploidyVcfFile at the 5th step 'CanvasPartition'.

So the command has:
${DOTNET}/dotnet {$CANVAS}/CanvasPartition/CanvasPartition.dll -p ""

So instead of NULL the script is taking it as an empty string and still trying to validate the VCF and erroring out.

Can you please check if that is actually an issue?

The way I am running CANVAS is:

{$DOTNET}/dotnet {$CANVAS}/Canvas.dll Somatic-WGS 
--bam=$TUMOR_BAMFILE 
--output=$outdir 
--reference=$CANVAS_data/kmer.fa 
--genome-folder=$CANVAS_data/WholeGenomeFasta 
--sample-name=$SAMPLE 
--filter-bed=$CANVAS_data/filter13.bed 
--sample-b-allele-vcf=$NORMAL_VCF 
--somatic-vcf=$TUMOR_VCF
```



```

$ Canvas Germline-WGS --bam=/home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam  --sample-b-allele-vcf /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa -g /home/wuzhikun/database/genome/GRCh38/CanvasGenome -f /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline --sample-name SRR62
2019-06-01T10:43:27+08:00, 
2019-06-01T10:43:27+08:00,Running checkpoint 01: Validate input
2019-06-01T10:43:27+08:00,Running Canvas Germline-WGS 1.40.0.1613+master
2019-06-01T10:43:27+08:00,Command-line arguments: Germline-WGS --bam=/home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam --sample-b-allele-vcf /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa -g /home/wuzhikun/database/genome/GRCh38/CanvasGenome -f /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline --sample-name SRR62
2019-06-01T10:43:27+08:00,Checkpoint 01 Validate input complete. Elapsed time (hh/mm/ss): 00:00:00.4
2019-06-01T10:43:27+08:00,Normal Vcf path: /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf


2019-06-01T10:45:59+08:00,Launching process for job SRR62.partitioned:
/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasPartition/CanvasPartition.dll  -v /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR62/VFResultsSRR62.txt.gz -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR62/SRR62.cleaned" -b "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -o "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR62/SRR62.partitioned"  -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome"  -p ""  -g
2019-06-01T10:46:01+08:00,Job SRR62.partitioned duration: 00:00:02.3

```


#### Answer

--ploidy-vcf is quired


```
Thanks for pointing this out. It seems like we should make --ploidy-vcf a required parameter then.

If you don't care about proper sex chromosome calling for a male sample, you can provide an empty vcf file (don't forget the header lines) for this parameter and both X and Y will be treated as diploid.
```


Here is a template ploidy vcf for a female sample using Grch38 :
```
##fileformat=VCFv4.1
##INFO=<ID=END,Number=1,Type=Integer,Description="End position of the variant described in this record">
##FORMAT=<ID=CN,Number=1,Type=Integer,Description="Copy number genotype for imprecise events">
#CHROM  POS ID  REF ALT QUAL  FILTER  INFO  FORMAT  HCC1187-NovaSeq-Grch38
chrY  0 . N <CNV> . PASS  END=57227415  CN  0
```


Here is a template ploidy vcf for a male sample using GRCh38
```
##fileformat=VCFv4.1
##INFO=<ID=END,Number=1,Type=Integer,Description="End position of the variant described in this record">
##FORMAT=<ID=CN,Number=1,Type=Integer,Description="Copy number genotype for imprecise events">
#CHROM  POS ID  REF ALT QUAL  FILTER  INFO  FORMAT  MALE
chrX  0 . N <CNV> . PASS  END=10000 CN  1
chrX  2781479 . N <CNV> . PASS  END=155701382 CN  1
chrX  156030895 . N <CNV> . PASS  END=156040895 CN  1
chrY  0 . N <CNV> . PASS  END=57227415  CN  1
```




### germline CNV

```

$ Canvas Germline-WGS --bam=/home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SRR62.bqsr.bam  --sample-b-allele-vcf /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome/kmer.fa -g /home/wuzhikun/database/genome/GRCh38/CanvasGenome -f /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline --sample-name SRR62 --ploidy-vcf ploidy_male.vcf
```


output files:
```
-rw-rw-r-- 1    0 Jun  1 11:00 CanvasError.txt
-rw-rw-r-- 1  33K Jun  1 11:03 CanvasLog.txt
drwxrwxr-x 1 4.0K Jun  1 11:02 Checkpoints
-rw-rw-r-- 1 2.9M Jun  1 11:02 CNV.CoverageAndVariantFrequency.txt
-rw-rw-r-- 1  39K Jun  1 11:02 CNV.vcf.gz
drwxrwxr-x 1 4.0K Jun  1 11:02 Logging
drwxrwxr-x 1 4.0K Jun  1 11:01 TempCNV
drwxrwxr-x 1 4.0K Jun  1 11:02 TempCNV_SRR62

```




#### Error
```
2019-06-01T11:34:55+08:00,Command-line arguments: Germline-WGS --bam=/home/wuzhikun/Project/WGSSomatic/mapping/SRR62/SR
R62.bqsr.bam --sample-b-allele-vcf /home/wuzhikun/Project/WGSSomatic/CNV/Pair/SRR6_variants_temp.vcf -r /home/wuzhikun/
database/genome/GRCh38/CanvasGenome/kmer.fa -g /home/wuzhikun/database/genome/GRCh38/CanvasGenome -f /home/wuzhikun/dat
abase/genome/GRCh38/CanvasGenome/filter13.bed -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline --sample-name SRR6
 --ploidy-vcf /home/wuzhikun/Project/WGSSomatic/ploidy_male.vcf



/home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/Canvas
DiploidCaller/CanvasDiploidCaller.dll -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6/SRR6.partiti
oned" -v "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/germline/TempCNV_SRR6/VFResultsSRR6.txt.gz" -o "/home/wuzhikun/Pro
ject/WGSSomatic/CNV/SRR6/germline/CNV.vcf.gz" -n "SRR6" -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome" -p "/ho
me/wuzhikun/Project/WGSSomatic/ploidy_male.vcf" 
2019-06-01T11:37:31+08:00,Job CNV.vcf.gz duration: 00:00:02.5
2019-06-01T11:37:31+08:00,Checkpoint 06 Variant calling complete. Elapsed time (hh/mm/ss): 00:00:02.7
2019-06-01T11:46:50+08:00,ERROR: Job SomaticCNV-SRR6 failed with exit code 134. Job logs: 
        /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/Logging/SomaticCNV-SRR6.stdout
        /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/Logging/SomaticCNV-SRR6.stderr
Job error message:
Unhandled Exception: System.InvalidOperationException: Sequence contains no elements
   at System.Linq.Enumerable.Min(IEnumerable`1 source)
   at CanvasSomaticCaller.SomaticCaller.ModelOverallCoverageAndPurity(Int64 genomeLength, CanvasSomaticClusteringMode c
lusteringMode, Nullable`1 evennessScore) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\Canvas\CanvasSomaticCaller
\SomaticCaller.cs:line 1890
   at CanvasSomaticCaller.SomaticCaller.CallCNVUsingSNVFrequency(Nullable`1 localSDmetric, Nullable`1 evennessScore, St
ring referenceFolder, CanvasSomaticClusteringMode clusteringMode) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\C
anvas\CanvasSomaticCaller\SomaticCaller.cs:line 2556
   at CanvasSomaticCaller.SomaticCaller.CallVariants(String inFile, String variantFrequencyFile, String outputVCFPath, 
String referenceFolder, String name, Nullable`1 localSDmetric, Nullable`1 evennessScore, CanvasSomaticClusteringMode cl
usteringMode) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\Canvas\CanvasSomaticCaller\SomaticCaller.cs:line 407
   at CanvasSomaticCaller.Program.Main(String[] args) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\Canvas\Canvas
SomaticCaller\Program.cs:line 196
2019-06-01T11:46:51+08:00,ERROR: Canvas workflow error: Isas.Framework.WorkManagement.JobFailedException: Job SomaticCN
V-SRR6 failed with exit code 134
   at Isas.Framework.WorkManagement.JobLaunching.BasicJobLauncher.RunSystemProcessCheckExitAsync(JobInfo job, Action`1 
stdoutCallback, Action`1 stderrCallback)
   at Isas.Framework.WorkManagement.JobLaunching.RuntimeTrackingJobLauncher.LaunchJobAsync(JobInfo jobInfo, Action`1 st
doutCallback, Action`1 stderrCallback)
   at Isas.Framework.WorkManagement.IJobLauncherExtensions.LaunchJob(IJobLauncher jobLauncher, JobInfo jobInfo, Action`
1 stdoutCallback, Action`1 stderrCallback)
   at Isas.Framework.WorkManagement.IWorkDoerJobExtensions.<>c__DisplayClass0_0`1.<DoWork>b__0(WorkResources sr, IJobLa
uncher jobLauncher)
   at Isas.Framework.WorkManagement.ResourceManagement.ThreadedWorkResourceManager.<>c__DisplayClass11_0`1.<RunWithReso
urces>b__3(WorkResources resources)
--- End of stack trace from previous location where exception was thrown ---
   at Isas.Framework.WorkManagement.ResourceManagement.ThreadedWorkResourceManager.<RunWithResources>b__11_1[T](Task`1 
resourceRequestTask, Task`1 functionTask)
   at Isas.Framework.WorkManagement.AsTaskExtensions.Await[T](Task`1 task)
   at Canvas.CanvasRunner.RunSomaticCalling(IFileLocation partitionedPath, CanvasCallset callset, String canvasBedPath,
 String ploidyVcfPath, IFileLocation localSdMetricFile, IFileLocation evennessMetricFile, IFileLocation canvasSnvPath)
   at Canvas.CanvasRunner.<>c__DisplayClass38_0.<CallSampleInternal>b__5()
   at Isas.Framework.Checkpointing.Legacy.LegacyCheckpointRunner.<>c__DisplayClass0_0.<RunCheckpoint>b__0()
   at Isas.Framework.Checkpointing.Internals.SerializingCheckpointRunner.<>c__DisplayClass8_0`1.<RunCheckpoint>b__0(Che
ckpoint checkpoint)
   at Isas.Framework.Checkpointing.Internals.CoreCheckpointRunner.RunCheckpoint[TResult](String name, Func`2 run)
   at Isas.Framework.Checkpointing.Legacy.LegacyCheckpointRunner.RunCheckpoint(ICheckpointRunner runner, String name, A
ction a)
   at Canvas.CanvasRunner.CallSampleInternal(CanvasCallset callset)
   at Canvas.CanvasRunner.CallSample(CanvasCallset callset)
   at Canvas.ModeLauncher.Launch()

```




```
$ /home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasPartition/CanvasPartition.dll  -v /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/VFResultsSRR6.txt.gz -i "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/SRR6.cleaned" -b "/home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed" -o "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/SRR6.partitioned"  -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome"  -p "/home/wuzhikun/Project/WGSSomatic/ploidy_male.vcf" --evenness-metric-file "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/EvennessMetric.txt" 
>>>Command-line arguments:
-v /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/VFResultsSRR6.txt.gz -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/SRR6.cleaned -b /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/SRR6.partitioned -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome -p /home/wuzhikun/Project/WGSSomatic/ploidy_male.vcf --evenness-metric-file /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/EvennessMetric.txt 
>>> Loaded 24 intervals for 24 sequences
2019-06-01T13:10:56+08:00,Load variant frequencies from /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/VFResultsSRR6.txt.gz
2019-06-01T13:10:56+08:00,Done processing VAFs

6/1/19 1:10:56 PM Running Wavelet Partitioning
Unable to calculate an evenness score, using coverage for segmentation
6/1/19 1:10:56 PM Launching wavelet tasks
6/1/19 1:10:56 PM Completed wavelet tasks
6/1/19 1:10:56 PM Segmentation results complete
>>> Loaded 24 intervals for 24 sequences
6/1/19 1:10:57 PM CanvasPartition results written out

```

```
$ /home/wuzhikun/anaconda3/envs/WGS/bin/dotnet /home/wuzhikun/anaconda3/envs/WGS/bin/Canvas-1.40.0.1613+master_x64/CanvasSomaticCaller/CanvasSomaticCaller.dll  -v /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/VFResultsSRR6.txt.gz -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/SRR6.partitioned -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/CNV.vcf.gz -b /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -p /home/wuzhikun/Project/WGSSomatic/ploidy_male.vcf -n SRR6 --local-sd-metric-file "/home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/LocalSdMetric.txt" -r "/home/wuzhikun/database/genome/GRCh38/CanvasGenome"
>>>Command-line arguments:
-v /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/VFResultsSRR6.txt.gz -i /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/SRR6.partitioned -o /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/CNV.vcf.gz -b /home/wuzhikun/database/genome/GRCh38/CanvasGenome/filter13.bed -p /home/wuzhikun/Project/WGSSomatic/ploidy_male.vcf -n SRR6 --local-sd-metric-file /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/LocalSdMetric.txt -r /home/wuzhikun/database/genome/GRCh38/CanvasGenome 
>>>LoadReferencePloidy(/home/wuzhikun/Project/WGSSomatic/ploidy_male.vcf)
>>> Loaded 24 intervals for 24 sequences
6/1/19 1:53:14 PM CallVariants start:
2019-06-01T13:53:14+08:00,Read segments from /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/SRR6.partitioned
2019-06-01T13:53:15+08:00,Loaded 746 segments
2019-06-01T13:53:15+08:00,Load variant frequencies from /home/wuzhikun/Project/WGSSomatic/CNV/SRR6/somatic/TempCNV_SRR6/VFResultsSRR6.txt.gz
6/1/19 1:53:15 PM Initialize ploidy models...
6/1/19 1:53:15 PM Ploidy models prepared.
Modeling overall coverage/purity across 575 segments

Unhandled Exception: System.InvalidOperationException: Sequence contains no elements
   at System.Linq.Enumerable.Min(IEnumerable`1 source)
   at CanvasSomaticCaller.SomaticCaller.ModelOverallCoverageAndPurity(Int64 genomeLength, CanvasSomaticClusteringMode clusteringMode, Nullable`1 evennessScore) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\Canvas\CanvasSomaticCaller\SomaticCaller.cs:line 1890
   at CanvasSomaticCaller.SomaticCaller.CallCNVUsingSNVFrequency(Nullable`1 localSDmetric, Nullable`1 evennessScore, String referenceFolder, CanvasSomaticClusteringMode clusteringMode) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\Canvas\CanvasSomaticCaller\SomaticCaller.cs:line 2556
   at CanvasSomaticCaller.SomaticCaller.CallVariants(String inFile, String variantFrequencyFile, String outputVCFPath, String referenceFolder, String name, Nullable`1 localSDmetric, Nullable`1 evennessScore, CanvasSomaticClusteringMode clusteringMode) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\Canvas\CanvasSomaticCaller\SomaticCaller.cs:line 407
   at CanvasSomaticCaller.Program.Main(String[] args) in D:\TeamCity\buildAgent\work\a29a190a11771d97\Src\Canvas\CanvasSomaticCaller\Program.cs:line 196
Aborted (core dumped)

```