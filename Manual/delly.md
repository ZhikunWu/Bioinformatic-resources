
## delly

### install delly
```
conda update -n base conda

conda install -c bioconda delly
```

### Delly multi-threading mode

You can set the number of threads using the environment variable OMP_NUM_THREADS.
```
export OMP_NUM_THREADS=2
```


### parameters
```
(NanoSV) wuzhikun@fat01 11:13:04 ^_^ /home/wuzhikun/software 
$ ./delly_v0.8.1_linux_x86_64bit call

Usage: delly call [OPTIONS] -g <ref.fa> <sample1.sort.bam> <sample2.sort.bam> ...

Generic options:
  -? [ --help ]                     show help message
  -t [ --svtype ] arg (=ALL)        SV type to compute [DEL, INS, DUP, INV, 
                                    BND, ALL]
  -g [ --genome ] arg               genome fasta file
  -x [ --exclude ] arg              file with regions to exclude
  -o [ --outfile ] arg (="sv.bcf")  SV BCF output file

Discovery options:
  -q [ --map-qual ] arg (=1)        min. paired-end (PE) mapping quality
  -r [ --qual-tra ] arg (=20)       min. PE quality for translocation
  -s [ --mad-cutoff ] arg (=9)      insert size cutoff, median+s*MAD (deletions
                                    only)
  -c [ --minclip ] arg (=25)        min. clipping length
  -m [ --minrefsep ] arg (=50)      min. reference separation
  -n [ --maxreadsep ] arg (=10)     max. read separation

Genotyping options:
  -v [ --vcffile ] arg              input VCF/BCF file for genotyping
  -u [ --geno-qual ] arg (=5)       min. mapping quality for genotyping
  -d [ --dump ] arg                 gzipped output file for SV-reads (optional)

```


### run delly

```
samtools view --threads 20 -b  M671-2.bqsr.bam 22 > M671-2.bqsr_chr22.bam
```


```
/home/wuzhikun/software/delly_v0.8.1_linux_x86_64bit call --svtype  ALL  --genome /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --outfile  M671-2.bcf   M671-2.bqsr.bam 
```

or

```
$ delly call   --genome /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --outfile  M671-2.bcf   M671-2.bqsr_chr22.bam 
[2019-Dec-24 12:02:05] delly call --genome /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --outfile M671-2.bcf M671-2.bqsr_chr22.bam 
[2019-Dec-24 12:02:12] Paired-end clustering

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
[2019-Dec-24 12:18:36] Split-read alignment

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
[2019-Dec-24 12:18:55] Generate REF and ALT probes

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
[2019-Dec-24 12:18:57] SV annotation

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
[2019-Dec-24 12:19:45] Genotyping

0%   10   20   30   40   50   60   70   80   90   100%
|----|----|----|----|----|----|----|----|----|----|
***************************************************
[2019-Dec-24 12:19:45] Library statistics
Sample: M671-2
RG: ID=M671-2,ReadSize=150,Median=213,MAD=60,UniqueDiscordantPairs=4681
[2019-Dec-24 12:19:45] Done.

```

#### output files:
```
M671-2.bcf
M671-2.bcf.csi 
```

change bcf to vcf
```
bcftools view M671-2.bcf > M671-2.vcf
```


### Somatic SV calling

At least one tumor sample and a matched control sample are required for SV discovery
```
delly call -x hg19.excl -o t1.bcf -g hg19.fa tumor1.bam control1.bam
```


Somatic pre-filtering requires a tab-delimited sample description file where the first column is the sample id (as in the VCF/BCF file) and the second column is either tumor or control
```
delly filter -f somatic -o t1.pre.bcf -s samples.tsv t1.bcf
```


Genotype pre-filtered somatic sites across a larger panel of control samples to efficiently filter false postives and germline SVs. For performance reasons, this can be run in parallel for each sample of the control panel and you may want to combine multiple pre-filtered somatic site lists from multiple tumor samples.
```
delly call -g hg19.fa -v t1.pre.bcf -o geno.bcf -x hg19.excl tumor1.bam control1.bam ... controlN.bam
```

Post-filter for somatic SVs using all control samples.
```
delly filter -f somatic -o t1.somatic.bcf -s samples.tsv geno.bcf
```


### Germline SV calling

SV calling is done by sample for high-coverage genomes or in small batches for low-coverage genomes
```
delly call -g hg19.fa -o s1.bcf -x hg19.excl sample1.bam
```


Merge SV sites into a unified site list
```
delly merge -o sites.bcf s1.bcf s2.bcf ... sN.bcf
```

Genotype this merged SV site list across all samples. This can be run in parallel for each sample.
```
delly call -g hg19.fa -v sites.bcf -o s1.geno.bcf -x hg19.excl s1.bam

delly call -g hg19.fa -v sites.bcf -o sN.geno.bcf -x hg19.excl sN.bam
```


Merge all genotyped samples to get a single VCF/BCF using bcftools merge
```
bcftools merge -m id -O b -o merged.bcf s1.geno.bcf s2.geno.bcf ... sN.geno.bcf
```

Apply the germline SV filter which requires at least 20 unrelated samples
```
delly filter -f germline -o germline.bcf merged.bcf
```


### examples
```

samtools index $i.recal.bam
~/cc/biosoft/delly/delly_v0.7.8_linux_x86_64bit call -g $DB/hg19_chr.fa -x exc1.excl -o delly_out/$i.exc1.bcf $i.recal.bam

#bcftools view $i.target.bcf >$i.target.vcf 

#Merge SV sites into a unified site list
delly merge -o sites.bcf s1.bcf s2.bcf ... sN.bcf

#Genotype this merged SV site list across all samples. This can be run in parallel for each sample.
delly call -g $DB/target-ref.fa -v sites.bcf -o s1.geno.bcf  s1.bam

#Merge all genotyped samples to get a single VCF/BCF using bcftools merge
bcftools merge -m id -O b -o merged.bcf s1.geno.bcf s2.geno.bcf ... sN.geno.bcf

#Apply the germline SV filter which requires at least 20 unrelated samples
delly filter -f germline -o germline.bcf merged.bcf
bcftools view germline.bcf >germline.vcf
```


```
git clone --recursive https://github.com/dellytools/svprops.git
cd svprops/
./svprops germline.vcf >germline.tab #size分布，各类型
./sampleprops germline.vcf >sample.tab #每个样本在多少SV中是RR，RA，AA（基因型统计）

#绘图
Rscript R/svprops.R germline.tab
Rscript R/sampleprops.R sample.tab

head -3germline.tab
#chr    start   chr2    end id  size    vac vaf singleton   missingrate svtype  ct  precise ci  inslen  homlen  ce  refgq   altgq   gqsum   rdratio medianrc    refratio    altratio    maxaltratio PEsupport   SRsupport   supportsum
#chr22  17900897    chr22   17900914    DEL00000000 18  7   0.152174    NA  0   DEL 3to5    1   6   0   5   1.93828 75  10000   41614   0.563525    632 0   0.721311    0.787879    0   228 737
#chr22  18003439    chr22   18004197    DEL00000006 759 9   0.195652    NA  0   DEL 3to5    0   174 0   0   0   15  45  558 0.658926    107 0   0.25    0.333333    11  0   123

head -3 sample.tab
#sample missing homref  het homalt
#sample1    0   76  37  14
#sample2    0   69  47  11
```


```
germline.tab各列信息如下

vac: variant allele count (across all samples)
vaf: variant allele frequency (across all samples)
singleton: N/A if present in multiple samples or sample name if only present in one
missingrate: how many samples have a missing genotype (useful after GQ calibration)
ct: Delly's INFO:CT，Paired-end signature induced connection type
precise: 1 if INFO:PRECISE，Precise structural variation
ci: Delly's INFO:CIPOS，PE confidence interval around POS
inslen: insertion length
homlen: homology length
ce: Delly's INFO:CE，Consensus sequence entropy
refgq: median reference genotype quality for all SV non-carriers (GT==0/0)
altgq: median alternative genotype quality for het. SV carriers
gqsum: total GQ sum (useful to flag repetitive sites that are poorly genotyped)
rdratio: read-depth ratio of SV carriers to non-carriers (useful for filtering CNVs)
medianrc: median coverage
refratio: median REF support for non-carriers
altratio: median ALT support for carriers
maxaltratio： max. ALT support for carriers
PEsupport： total paired end support across all samples
SRsupport： total split-read support across all samples
supportsum： total depth across all samples
sample.tab各列信息如下

missing：该个体有多少位点的genotype为missing
homref：该个体有多少位点为ref的纯合位点
het:该个体有多少位点为杂合位点
homalt:该个体有多少位点为alt的纯合位点


```




