## GATK CNV

### CNV manual

* [使用gatk检测WES数据中的cnv](https://blog.csdn.net/yuqiuwang929/article/details/105770989)
* [Call common and rare germline copy number variants](https://gatk.broadinstitute.org/hc/en-us/articles/360035531152--How-to-Call-common-and-rare-germline-copy-number-variants)
* [Call germline Copy Number Variants with GATK in Snakemake](https://evodify.com/gatk-cnv-snakemake/)
* [gatk4-somatic-cnvs](https://github.com/gatk-workflows/gatk4-somatic-cnvs)
* [Somatic CNV Calling](https://pmbio.org/module-05-somatic/0005/04/01/Somatic_CNV_Calling/)
* [DetermineGermlineContigPloidy](https://gatk.broadinstitute.org/hc/en-us/articles/360037224772-DetermineGermlineContigPloidy)
* [GermlineCNVCaller](https://gatk.broadinstitute.org/hc/en-us/articles/360037426991-GermlineCNVCaller-BETA-)


### install tools

install GATK4
```
conda install -c bioconda gatk4
```


install gcnvkernel

```
conda install -c bioconda gcnvkernel
```


### index for reference
```
$ samtools faidx Homo_sapiens.GRCh38.dna.primary_assembly_chr.fa
$ java -jar /home/wuzhikun/anaconda3/envs/WGS/bin/picard.jar CreateSequenceDictionary  R=Homo_sapiens.GRCh38.dna.primary_assembly_chr.fa     O=Homo_sapiens.GRCh38.dna.primary_assembly_chr.dict
```


### prepare file

contig_ploidy_priors.tsv
```
CONTIG_NAME PLOIDY_PRIOR_0 PLOIDY_PRIOR_1 PLOIDY_PRIOR_2 PLOIDY_PRIOR_3
MT 0 0.01 0.97 0.01
1 0 0.01 0.97 0.01
2 0 0.01 0.97 0.01
3 0 0.01 0.97 0.01
4 0 0.01 0.97 0.01
5 0 0.01 0.97 0.01
6 0 0.01 0.97 0.01
7 0 0.01 0.97 0.01
8 0 0.01 0.97 0.01
9 0 0.01 0.97 0.01
10 0 0.01 0.97 0.01
11 0 0.01 0.97 0.01
12 0 0.01 0.97 0.01
13 0 0.01 0.97 0.01
14 0 0.01 0.97 0.01
15 0 0.01 0.97 0.01
16 0 0.01 0.97 0.01
17 0 0.01 0.97 0.01
18 0 0.01 0.97 0.01
19 0 0.01 0.97 0.01
20 0 0.01 0.97 0.01
21 0 0.01 0.97 0.01
22 0 0.01 0.97 0.01
X 0.01 0.49 0.49 0.01
Y 0.50 0.50 0.00 0.00
```


### GATK CNV

#### PreprocessIntervals
```
gatk PreprocessIntervals -R /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --padding 0 -imr OVERLAPPING_ONLY -O grch38.preprocessed.interval_list

Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar PreprocessIntervals -R /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --padding 0 -imr OVERLAPPING_ONLY -O grch38.preprocessed.interval_list
10:39:38.789 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar!/com/intel/gkl/native/libgkl_compression.so
Sep 05, 2020 10:39:39 AM shaded.cloud_nio.com.google.auth.oauth2.ComputeEngineCredentials runningOnComputeEngine
...
grch38.preprocessed.interval_list...
10:40:57.216 INFO  PreprocessIntervals - PreprocessIntervals complete.
10:40:57.216 INFO  PreprocessIntervals - Shutting down engine
[September 5, 2020 10:40:57 AM CST] org.broadinstitute.hellbender.tools.copynumber.PreprocessIntervals done. Elapsed time: 1.32 minutes.
Runtime.totalMemory()=3586129920
```

#### CollectReadCounts

```
$ gatk --java-options -Xmx30000m CollectReadCounts -L /home/wuzhikun/Project/RBIllumina/mapping/RB16-normal/CollectReadCounts/grch38.preprocessed.interval_list  --input /home/wuzhikun/Project/RBIllumina/mapping/RB16-normal/RB16-normal.sorted.bam --reference /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -format HDF5 --output /home/wuzhikun/Project/RBIllumina/mapping/RB16-normal/CollectReadCounts/RB16_readcount.hdf5 --interval-merging-rule OVERLAPPING_ONLY
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -Xmx30000m -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar CollectReadCounts -L /home/wuzhikun/Project/RBIllumina/mapping/RB16-normal/CollectReadCounts/grch38.preprocessed.interval_list --input /home/wuzhikun/Project/RBIllumina/mapping/RB16-normal/RB16-normal.sorted.bam --reference /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -format HDF5 --output /home/wuzhikun/Project/RBIllumina/mapping/RB16-normal/CollectReadCounts/RB16_readcount.hdf5 -imr OVERLAPPING_ONLY
10:45:01.220 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar!/com/intel/gkl/native/libgkl_compression.so
Sep 05, 2020 10:45:01 AM shaded.cloud_nio.com.google.auth.oauth2.ComputeEngineCredentials runningOnComputeEngine
INFO: Failed to detect whether we are running on Google Compute Engine.
...
11:09:28.176 INFO  CollectReadCounts - CollectReadCounts complete.
11:09:28.177 INFO  CollectReadCounts - Shutting down engine
[September 5, 2020 11:09:28 AM CST] org.broadinstitute.hellbender.tools.copynumber.CollectReadCounts done. Elapsed time: 24.45 minutes.
Runtime.totalMemory()=3576168448
```




#### Ploidy of normal cohort 

```
gatk --java-options -Xmx80g DetermineGermlineContigPloidy --contig-ploidy-priors /home/wuzhikun/Project/RBIllumina/contig_ploidy_priors.tsv --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB07-normal/RB07-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB08-normal/RB08-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB09-normal/RB09-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB10-normal/RB10-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB11-normal/RB11-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB12-normal/RB12-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB13-normal/RB13-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB14-normal/RB14-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB15-normal/RB15-normal_readCounts.hdf5 --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB16-normal/RB16-normal_readCounts.hdf5   --output /home/wuzhikun/Project/RBIllumina/CNV/Germline  --output-prefix NormalPanel --interval-merging-rule OVERLAPPING_ONLY > /home/wuzhikun/Project/RBIllumina/log/CohortPloid.log 2>&1

```


output files:
```
drwxrwxr-x. 1 4.0K Sep  5 17:24 NormalPanel-calls
drwxrwxr-x. 1 4.0K Sep  5 17:24 NormalPanel-model

```


```
$ tree NormalPanel-model
NormalPanel-model
├── contig_ploidy_prior.tsv
├── gcnvkernel_version.json
├── interval_list.tsv
├── mu_mean_bias_j_lowerbound__.tsv
├── mu_psi_j_log__.tsv
├── ploidy_config.json
├── std_mean_bias_j_lowerbound__.tsv
└── std_psi_j_log__.tsv


$ tree NormalPanel-calls
NormalPanel-calls
├── SAMPLE_0
│   ├── contig_ploidy.tsv
│   ├── global_read_depth.tsv
│   ├── mu_psi_s_log__.tsv
│   ├── sample_name.txt
│   └── std_psi_s_log__.tsv
├── SAMPLE_1
│   ├── contig_ploidy.tsv
│   ├── global_read_depth.tsv
│   ├── mu_psi_s_log__.tsv
│   ├── sample_name.txt
│   └── std_psi_s_log__.tsv

```




```
gatk --java-options "-Xmx30G" GermlineCNVCaller --run-mode COHORT -I /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 -I /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB07-normal/RB07-normal_readCounts.hdf5  --contig-ploidy-calls /home/wuzhikun/Project/RBIllumina/CNV/Germline/NormalPanel-calls --interval-merging-rule OVERLAPPING_ONLY -O /home/wuzhikun/Project/RBIllumina/CNV/Germline/Call --output-prefix RB06-normal
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -Xmx30G -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar GermlineCNVCaller --run-mode COHORT -I /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 -I /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB07-normal/RB07-normal_readCounts.hdf5 --contig-ploidy-calls /home/wuzhikun/Project/RBIllumina/CNV/Germline/NormalPanel-calls --interval-merging-rule OVERLAPPING_ONLY -O /home/wuzhikun/Project/RBIllumina/CNV/Germline/Call --output-prefix RB06-normal
09:08:49.855 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar!/com/intel/gkl/native/libgkl_compression.so
Sep 07, 2020 9:08:50 AM shaded.cloud_nio.com.google.auth.oauth2.ComputeEngineCredentials runningOnComputeEngine
INFO: Failed to detect whether we are running on Google Compute Engine.
09:08:50.976 INFO  GermlineCNVCaller - ------------------------------------------------------------
09:08:50.977 INFO  GermlineCNVCaller - The Genome Analysis Toolkit (GATK) v4.1.4.1
09:08:50.977 INFO  GermlineCNVCaller - For support and documentation go to https://software.broadinstitute.org/gatk/
09:08:50.978 INFO  GermlineCNVCaller - Executing as wuzhikun@fat02 on Linux v3.10.0-327.el7.x86_64 amd64
09:08:50.978 INFO  GermlineCNVCaller - Java runtime: OpenJDK 64-Bit Server VM v1.8.0_192-b01
09:08:50.979 INFO  GermlineCNVCaller - Start Date/Time: September 7, 2020 9:08:49 AM CST
09:08:50.979 INFO  GermlineCNVCaller - ------------------------------------------------------------
09:08:50.979 INFO  GermlineCNVCaller - ------------------------------------------------------------
09:08:50.980 INFO  GermlineCNVCaller - HTSJDK Version: 2.21.0
09:08:50.980 INFO  GermlineCNVCaller - Picard Version: 2.21.2
09:08:50.980 INFO  GermlineCNVCaller - HTSJDK Defaults.COMPRESSION_LEVEL : 2
09:08:50.980 INFO  GermlineCNVCaller - HTSJDK Defaults.USE_ASYNC_IO_READ_FOR_SAMTOOLS : false
09:08:50.980 INFO  GermlineCNVCaller - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_SAMTOOLS : true
09:08:50.980 INFO  GermlineCNVCaller - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_TRIBBLE : false
09:08:50.980 INFO  GermlineCNVCaller - Deflater: IntelDeflater
09:08:50.980 INFO  GermlineCNVCaller - Inflater: IntelInflater
09:08:50.981 INFO  GermlineCNVCaller - GCS max retries/reopens: 20
09:08:50.981 INFO  GermlineCNVCaller - Requester pays: disabled
09:08:50.981 INFO  GermlineCNVCaller - Initializing engine
09:12:19.724 INFO  GermlineCNVCaller - Done initializing engine
log4j:WARN No appenders could be found for logger (org.broadinstitute.hdf5.HDF5Library).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
09:12:22.865 INFO  GermlineCNVCaller - Retrieving intervals from read-count file (/home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5)...
09:12:23.516 INFO  GermlineCNVCaller - No annotated intervals were provided...
09:12:23.516 INFO  GermlineCNVCaller - No GC-content annotations for intervals found; explicit GC-bias correction will not be performed...
09:12:25.792 INFO  GermlineCNVCaller - Running the tool in COHORT mode...
09:12:25.792 INFO  GermlineCNVCaller - Validating and aggregating data from input read-count files...
09:12:26.145 INFO  GermlineCNVCaller - Aggregating read-count file /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 (1 / 2)
09:12:30.828 INFO  GermlineCNVCaller - Aggregating read-count file /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB07-normal/RB07-normal_readCounts.hdf5 (2 / 2)
20:35:34.260 INFO  GermlineCNVCaller - GermlineCNVCaller complete.
20:35:34.261 INFO  GermlineCNVCaller - Shutting down engine
[September 8, 2020 8:35:34 PM CST] org.broadinstitute.hellbender.tools.copynumber.GermlineCNVCaller done. Elapsed time: 2,126.75 minutes.
Runtime.totalMemory()=4196401152

```


output files:
```
drwxrwxr-x 1 4.0K Sep  8 20:34 RB06-normal-calls
drwxrwxr-x 1 4.0K Sep  8 20:30 RB06-normal-model
drwxrwxr-x 1 4.0K Sep  8 20:34 RB06-normal-tracking


RB06-normal-calls:
-rw-rw-r-- 1  222 Sep  8 20:30 calling_config.json
-rw-rw-r-- 1  449 Sep  8 20:30 denoising_config.json
-rw-rw-r-- 1   22 Sep  8 20:30 gcnvkernel_version.json
-rw-rw-r-- 1  59M Sep  8 20:34 interval_list.tsv
drwxrwxr-x 1 4.0K Sep  8 20:33 SAMPLE_0
drwxrwxr-x 1 4.0K Sep  8 20:34 SAMPLE_1

RB06-normal-model:
-rw-rw-r-- 1  222 Sep  8 20:28 calling_config.json
-rw-rw-r-- 1  449 Sep  8 20:28 denoising_config.json
-rw-rw-r-- 1   22 Sep  8 20:28 gcnvkernel_version.json
-rw-rw-r-- 1  59M Sep  8 20:30 interval_list.tsv
-rw-rw-r-- 1 117M Sep  8 20:28 log_q_tau_tk.tsv
-rw-rw-r-- 1  144 Sep  8 20:30 mu_ard_u_log__.tsv
-rw-rw-r-- 1  59M Sep  8 20:29 mu_log_mean_bias_t.tsv
-rw-rw-r-- 1  54M Sep  8 20:30 mu_psi_t_log__.tsv
-rw-rw-r-- 1 293M Sep  8 20:29 mu_W_tu.tsv
-rw-rw-r-- 1  150 Sep  8 20:30 std_ard_u_log__.tsv
-rw-rw-r-- 1  56M Sep  8 20:30 std_log_mean_bias_t.tsv
-rw-rw-r-- 1  53M Sep  8 20:30 std_psi_t_log__.tsv
-rw-rw-r-- 1 263M Sep  8 20:29 std_W_tu.tsv

RB06-normal-tracking:
-rw-rw-r-- 1 55K Sep  8 20:34 main_elbo_history.tsv
-rw-rw-r-- 1 53K Sep  8 20:34 warm_up_elbo_history.tsv

```



### Case  Ploidy
```
$ gatk --java-options -Xmx100g DetermineGermlineContigPloidy  --model /home/wuzhikun/Project/RBIllumina/CNV/Germline/NormalPanel-model -I /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 -O /home/wuzhikun/Project/RBIllumina/CNV/Germline/Ploidy  --output-prefix RB06-normal 
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -Xmx100g -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar DetermineGermlineContigPloidy --model /home/wuzhikun/Project/RBIllumina/CNV/Germline/NormalPanel-model -I /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 -O /home/wuzhikun/Project/RBIllumina/CNV/Germline/Ploidy --output-prefix RB06-normal
08:53:06.369 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar!/com/intel/gkl/native/libgkl_compression.so
Sep 10, 2020 8:53:07 AM shaded.cloud_nio.com.google.auth.oauth2.ComputeEngineCredentials runningOnComputeEngine
INFO: Failed to detect whether we are running on Google Compute Engine.
08:53:07.257 INFO  DetermineGermlineContigPloidy - ------------------------------------------------------------
08:53:07.258 INFO  DetermineGermlineContigPloidy - The Genome Analysis Toolkit (GATK) v4.1.4.1
08:53:07.258 INFO  DetermineGermlineContigPloidy - For support and documentation go to https://software.broadinstitute.org/gatk/
08:53:07.258 INFO  DetermineGermlineContigPloidy - Executing as wuzhikun@fat02 on Linux v3.10.0-327.el7.x86_64 amd64
08:53:07.258 INFO  DetermineGermlineContigPloidy - Java runtime: OpenJDK 64-Bit Server VM v1.8.0_192-b01
08:53:07.259 INFO  DetermineGermlineContigPloidy - Start Date/Time: September 10, 2020 8:53:05 AM CST
08:53:07.259 INFO  DetermineGermlineContigPloidy - ------------------------------------------------------------
08:53:07.259 INFO  DetermineGermlineContigPloidy - ------------------------------------------------------------
08:53:07.260 INFO  DetermineGermlineContigPloidy - HTSJDK Version: 2.21.0
08:53:07.260 INFO  DetermineGermlineContigPloidy - Picard Version: 2.21.2
08:53:07.260 INFO  DetermineGermlineContigPloidy - HTSJDK Defaults.COMPRESSION_LEVEL : 2
08:53:07.260 INFO  DetermineGermlineContigPloidy - HTSJDK Defaults.USE_ASYNC_IO_READ_FOR_SAMTOOLS : false
08:53:07.260 INFO  DetermineGermlineContigPloidy - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_SAMTOOLS : true
08:53:07.260 INFO  DetermineGermlineContigPloidy - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_TRIBBLE : false
08:53:07.261 INFO  DetermineGermlineContigPloidy - Deflater: IntelDeflater
08:53:07.261 INFO  DetermineGermlineContigPloidy - Inflater: IntelInflater
08:53:07.261 INFO  DetermineGermlineContigPloidy - GCS max retries/reopens: 20
08:53:07.261 INFO  DetermineGermlineContigPloidy - Requester pays: disabled
08:53:07.261 INFO  DetermineGermlineContigPloidy - Initializing engine
08:56:22.039 INFO  DetermineGermlineContigPloidy - Done initializing engine
08:56:22.060 INFO  DetermineGermlineContigPloidy - A contig-ploidy model was provided, running in case mode...
08:56:28.978 INFO  DetermineGermlineContigPloidy - Validating and aggregating coverage per contig from input read-count files...
08:56:29.673 INFO  DetermineGermlineContigPloidy - Aggregating read-count file /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 (1 / 1)
log4j:WARN No appenders could be found for logger (org.broadinstitute.hdf5.HDF5Library).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
09:02:21.556 INFO  DetermineGermlineContigPloidy - DetermineGermlineContigPloidy complete.
09:02:21.557 INFO  DetermineGermlineContigPloidy - Shutting down engine
[September 10, 2020 9:02:21 AM CST] org.broadinstitute.hellbender.tools.copynumber.DetermineGermlineContigPloidy done. Elapsed time: 9.26 minutes.
Runtime.totalMemory()=2984247296

```



### CNV with case
```
$ gatk --java-options "-Xmx300G" GermlineCNVCaller --run-mode CASE --contig-ploidy-calls /home/wuzhikun/Project/RBIllumina/CNV/Germline/NormalPanel-calls --model /home/wuzhikun/Project/RBIllumina/CNV/Germline/Call/RB06-normal-model --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5  --output /home/wuzhikun/Project/RBIllumina/CNV/Germline/Samples --output-prefix RB06-normal
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar



$ gatk --java-options "-Xmx100G" GermlineCNVCaller --run-mode CASE --contig-ploidy-calls /home/wuzhikun/Project/RBIllumina/CNV/Germline/Ploidy/RB06-normal-calls  --model /home/wuzhikun/Project/RBIllumina/CNV/Germline/Call/RB06-normal-model  --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5  --output /home/wuzhikun/Project/RBIllumina/CNV/Germline/Samples --output-prefix RB06-normal
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -Xmx100G -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar GermlineCNVCaller --run-mode CASE --contig-ploidy-calls /home/wuzhikun/Project/RBIllumina/CNV/Germline/Ploidy/RB06-normal-calls --model /home/wuzhikun/Project/RBIllumina/CNV/Germline/Call/RB06-normal-model --input /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 --output /home/wuzhikun/Project/RBIllumina/CNV/Germline/Samples --output-prefix RB06-normal
09:22:09.546 INFO  NativeLibraryLoader - Loading libgkl_compression.so from jar:file:/home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar!/com/intel/gkl/native/libgkl_compression.so
Sep 11, 2020 9:22:10 AM shaded.cloud_nio.com.google.auth.oauth2.ComputeEngineCredentials runningOnComputeEngine
INFO: Failed to detect whether we are running on Google Compute Engine.
09:22:10.489 INFO  GermlineCNVCaller - ------------------------------------------------------------
09:22:10.489 INFO  GermlineCNVCaller - The Genome Analysis Toolkit (GATK) v4.1.4.1
09:22:10.489 INFO  GermlineCNVCaller - For support and documentation go to https://software.broadinstitute.org/gatk/
09:22:10.490 INFO  GermlineCNVCaller - Executing as wuzhikun@fat01 on Linux v3.10.0-327.el7.x86_64 amd64
09:22:10.490 INFO  GermlineCNVCaller - Java runtime: OpenJDK 64-Bit Server VM v1.8.0_192-b01
09:22:10.490 INFO  GermlineCNVCaller - Start Date/Time: September 11, 2020 9:22:09 AM CST
09:22:10.490 INFO  GermlineCNVCaller - ------------------------------------------------------------
09:22:10.490 INFO  GermlineCNVCaller - ------------------------------------------------------------
09:22:10.491 INFO  GermlineCNVCaller - HTSJDK Version: 2.21.0
09:22:10.491 INFO  GermlineCNVCaller - Picard Version: 2.21.2
09:22:10.491 INFO  GermlineCNVCaller - HTSJDK Defaults.COMPRESSION_LEVEL : 2
09:22:10.491 INFO  GermlineCNVCaller - HTSJDK Defaults.USE_ASYNC_IO_READ_FOR_SAMTOOLS : false
09:22:10.491 INFO  GermlineCNVCaller - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_SAMTOOLS : true
09:22:10.491 INFO  GermlineCNVCaller - HTSJDK Defaults.USE_ASYNC_IO_WRITE_FOR_TRIBBLE : false
09:22:10.492 INFO  GermlineCNVCaller - Deflater: IntelDeflater
09:22:10.492 INFO  GermlineCNVCaller - Inflater: IntelInflater
09:22:10.492 INFO  GermlineCNVCaller - GCS max retries/reopens: 20
09:22:10.492 INFO  GermlineCNVCaller - Requester pays: disabled
09:22:10.492 INFO  GermlineCNVCaller - Initializing engine
09:26:10.756 INFO  GermlineCNVCaller - Done initializing engine
09:26:16.547 INFO  GermlineCNVCaller - Running the tool in CASE mode...
09:26:16.547 INFO  GermlineCNVCaller - Validating and aggregating data from input read-count files...
09:26:17.206 INFO  GermlineCNVCaller - Aggregating read-count file /home/wuzhikun/Project/RBIllumina/CNV/Germline/RB06-normal/RB06-normal_readCounts.hdf5 (1 / 1)
log4j:WARN No appenders could be found for logger (org.broadinstitute.hdf5.HDF5Library).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
17:09:17.546 INFO  GermlineCNVCaller - GermlineCNVCaller complete.
17:09:17.548 INFO  GermlineCNVCaller - Shutting down engine
[September 11, 2020 5:09:17 PM CST] org.broadinstitute.hellbender.tools.copynumber.GermlineCNVCaller done. Elapsed time: 467.14 minutes.
Runtime.totalMemory()=4439146496


```



output files:
```
/home/wuzhikun/Project/RBIllumina/CNV/Germline/Samples
├── RB06-normal-calls
│   ├── calling_config.json
│   ├── denoising_config.json
│   ├── gcnvkernel_version.json
│   ├── interval_list.tsv
│   └── SAMPLE_0
│       ├── baseline_copy_number_t.tsv
│       ├── log_c_emission_tc.tsv
│       ├── log_q_c_tc.tsv
│       ├── mu_denoised_copy_ratio_t.tsv
│       ├── mu_psi_s_log__.tsv
│       ├── mu_read_depth_s_log__.tsv
│       ├── mu_z_su.tsv
│       ├── sample_name.txt
│       ├── std_denoised_copy_ratio_t.tsv
│       ├── std_psi_s_log__.tsv
│       ├── std_read_depth_s_log__.tsv
│       └── std_z_su.tsv
└── RB06-normal-tracking
    └── elbo_history.tsv

```







### Parameters

#### DetermineGermlineContigPloidy

```
$ gatk DetermineGermlineContigPloidy
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar DetermineGermlineContigPloidy
USAGE: DetermineGermlineContigPloidy [arguments]

Determines the baseline contig ploidy for germline samples given counts data
Version:4.1.4.1


Required Arguments:

--input,-I:File               Input read-count files containing integer read counts in genomic intervals for all
                              samples.  Intervals must be identical and in the same order for all samples.  If only a
                              single sample is specified, an input ploidy-model directory must also be specified.   
                              This argument must be specified at least once. Required. 

--output,-O:File              Output directory.  This will be created if it does not exist.  Required. 

--output-prefix:String        Prefix for output filenames.  Required. 


Optional Arguments:

--adamax-beta-1:Double        Adamax optimizer first moment estimation forgetting factor.  Default value: 0.9. 

--adamax-beta-2:Double        Adamax optimizer second moment estimation forgetting factor.  Default value: 0.999. 

--arguments_file:File         read one or more arguments files and add them to the command line  This argument may be
                              specified 0 or more times. Default value: null. 

--caller-external-admixing-rate:Double
                              Admixing ratio of new and old called posteriors (between 0 and 1; larger values implies
                              using more of the new posterior and less of the old posterior) after convergence.  Default
                              value: 0.75. 

--caller-internal-admixing-rate:Double
                              Admixing ratio of new and old called posteriors (between 0 and 1; larger values implies
                              using more of the new posterior and less of the old posterior) for internal convergence
                              loops.  Default value: 0.75. 

--caller-update-convergence-threshold:Double
                              Maximum tolerated calling update size for convergence.  Default value: 0.001. 

--contig-ploidy-priors:File   Input file specifying contig-ploidy priors.  If only a single sample is specified, this
                              input should not be provided.  If multiple samples are specified, this input is required. 
                              Default value: null. 

--convergence-snr-averaging-window:Integer
                              Averaging window for calculating training signal-to-noise ratio (SNR) for convergence
                              checking.  Default value: 5000. 

--convergence-snr-countdown-window:Integer
                              The number of ADVI iterations during which the SNR is required to stay below the set
                              threshold for convergence.  Default value: 10. 

--convergence-snr-trigger-threshold:Double
                              The SNR threshold to be reached before triggering the convergence countdown.  Default
                              value: 0.1. 

--disable-annealing:Boolean   (advanced) Disable annealing.  Default value: false. Possible values: {true, false} 

--disable-caller:Boolean      (advanced) Disable caller.  Default value: false. Possible values: {true, false} 

--disable-sampler:Boolean     (advanced) Disable sampler.  Default value: false. Possible values: {true, false} 

--exclude-intervals,-XL:StringOne or more genomic intervals to exclude from processing  This argument may be specified 0
                              or more times. Default value: null. 

--gatk-config-file:String     A configuration file to use with the GATK.  Default value: null. 

--gcs-max-retries,-gcs-retries:Integer
                              If the GCS bucket channel errors out, how many times it will attempt to re-initiate the
                              connection  Default value: 20. 

--gcs-project-for-requester-pays:String
                              Project to bill when accessing "requester pays" buckets. If unset, these buckets cannot be
                              accessed.  Default value: . 

--global-psi-scale:Double     Prior scale of contig coverage unexplained variance.  If a single sample is provided, this
                              input will be ignored.  Default value: 0.001. 

--help,-h:Boolean             display the help message  Default value: false. Possible values: {true, false} 

--initial-temperature:Double  Initial temperature (for DA-ADVI).  Default value: 2.0. 

--interval-exclusion-padding,-ixp:Integer
                              Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. 

--interval-merging-rule,-imr:IntervalMergingRule
                              Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL,
                              OVERLAPPING_ONLY} 

--interval-padding,-ip:IntegerAmount of padding (in bp) to add to each interval you are including.  Default value: 0. 

--interval-set-rule,-isr:IntervalSetRule
                              Set merging approach to use for combining interval inputs  Default value: UNION. Possible
                              values: {UNION, INTERSECTION} 

--intervals,-L:String         One or more genomic intervals over which to operate  This argument may be specified 0 or
                              more times. Default value: null. 

--learning-rate:Double        Adamax optimizer learning rate.  Default value: 0.05. 

--log-emission-samples-per-round:Integer
                              Log emission samples drawn per round of sampling.  Default value: 2000. 

--log-emission-sampling-median-rel-error:Double
                              Maximum tolerated median relative error in log emission sampling.  Default value: 5.0E-4. 

--log-emission-sampling-rounds:Integer
                              Log emission maximum sampling rounds.  Default value: 100. 

--mapping-error-rate:Double   Typical mapping error rate.  Default value: 0.01. 

--max-advi-iter-first-epoch:Integer
                              Maximum ADVI iterations in the first epoch.  Default value: 1000. 

--max-advi-iter-subsequent-epochs:Integer
                              Maximum ADVI iterations in subsequent epochs.  Default value: 1000. 

--max-calling-iters:Integer   Maximum number of internal self-consistency iterations within each calling step.  Default
                              value: 1. 

--max-training-epochs:Integer Maximum number of training epochs.  Default value: 100. 

--mean-bias-standard-deviation:Double
                              Prior standard deviation of the contig-level mean coverage bias.  If a single sample is
                              provided, this input will be ignored.  Default value: 0.01. 

--min-training-epochs:Integer Minimum number of training epochs.  Default value: 20. 

--model:File                  Input ploidy-model directory.  If only a single sample is specified, this input is
                              required.  If multiple samples are specified, this input should not be provided.  Default
                              value: null. 

--num-thermal-advi-iters:Integer
                              Number of thermal ADVI iterations (for DA-ADVI).  Default value: 5000. 

--QUIET:Boolean               Whether to suppress job-summary info on System.err.  Default value: false. Possible
                              values: {true, false} 

--sample-psi-scale:Double     Prior scale of the sample-specific correction to the coverage unexplained variance. 
                              Default value: 1.0E-4. 

--tmp-dir:GATKPathSpecifier   Temp directory to use.  Default value: null. 

--use-jdk-deflater,-jdk-deflater:Boolean
                              Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false.
                              Possible values: {true, false} 

--use-jdk-inflater,-jdk-inflater:Boolean
                              Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false.
                              Possible values: {true, false} 

--verbosity,-verbosity:LogLevel
                              Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING,
                              INFO, DEBUG} 

--version:Boolean             display the version number for this tool  Default value: false. Possible values: {true,
                              false} 


Advanced Arguments:

--showHidden,-showHidden:Boolean
                              display hidden arguments  Default value: false. Possible values: {true, false} 


***********************************************************************

A USER ERROR has occurred: Argument input was missing: Argument 'input' is required.

***********************************************************************
Set the system property GATK_STACKTRACE_ON_USER_EXCEPTION (--java-options '-DGATK_STACKTRACE_ON_USER_EXCEPTION=true') to print the stack trace.

```



####  GermlineCNVCaller

```
$ gatk GermlineCNVCaller
Using GATK jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar
Running:
    java -Dsamjdk.use_async_io_read_samtools=false -Dsamjdk.use_async_io_write_samtools=true -Dsamjdk.use_async_io_write_tribble=false -Dsamjdk.compression_level=2 -jar /home/wuzhikun/anaconda3/envs/WGS/share/gatk4-4.1.4.1-1/gatk-package-4.1.4.1-local.jar GermlineCNVCaller
USAGE: GermlineCNVCaller [arguments]

Calls copy-number variants in germline samples given their counts and the output of DetermineGermlineContigPloidy
Version:4.1.4.1


Required Arguments:

--contig-ploidy-calls:File    Input contig-ploidy calls directory (output of DetermineGermlineContigPloidy).  Required. 

--input,-I:File               Input read-count files containing integer read counts in genomic intervals for all
                              samples.  All intervals specified via -L must be contained; if none are specified, then
                              intervals must be identical and in the same order for all samples.  This argument must be
                              specified at least once. Required. 

--output,-O:File              Output directory.  This will be created if it does not exist.  Required. 

--output-prefix:String        Prefix for output filenames.  Required. 

--run-mode:RunMode            Tool run-mode.  Required. Possible values: {COHORT, CASE} 


Optional Arguments:

--active-class-padding-hybrid-mode:Integer
                              If copy-number-posterior-expectation-mode is set to HYBRID, CNV-active intervals
                              determined at any time will be padded by this value (in the units of bp) in order to
                              obtain the set of intervals on which copy number posterior expectation is performed
                              exactly.  Default value: 50000. 

--adamax-beta-1:Double        Adamax optimizer first moment estimation forgetting factor.  Default value: 0.9. 

--adamax-beta-2:Double        Adamax optimizer second moment estimation forgetting factor.  Default value: 0.99. 

--annotated-intervals:File    Input annotated-intervals file containing annotations for GC content in genomic intervals
                              (output of AnnotateIntervals).  All intervals specified via -L must be contained.  This
                              input should not be provided if an input denoising-model directory is given (the latter
                              already contains the annotated-interval file).  Default value: null. 

--arguments_file:File         read one or more arguments files and add them to the command line  This argument may be
                              specified 0 or more times. Default value: null. 

--caller-external-admixing-rate:Double
                              Admixing ratio of new and old called posteriors (between 0 and 1; larger values implies
                              using more of the new posterior and less of the old posterior) after convergence.  Default
                              value: 1.0. 

--caller-internal-admixing-rate:Double
                              Admixing ratio of new and old called posteriors (between 0 and 1; larger values implies
                              using more of the new posterior and less of the old posterior) for internal convergence
                              loops.  Default value: 0.75. 

--caller-update-convergence-threshold:Double
                              Maximum tolerated calling update size for convergence.  Default value: 0.001. 

--class-coherence-length:Double
                              Coherence length of CNV-active and CNV-silent domains (in the units of bp).  Default
                              value: 10000.0. 

--cnv-coherence-length:Double Coherence length of CNV events (in the units of bp).  Default value: 10000.0. 

--convergence-snr-averaging-window:Integer
                              Averaging window for calculating training signal-to-noise ratio (SNR) for convergence
                              checking.  Default value: 500. 

--convergence-snr-countdown-window:Integer
                              The number of ADVI iterations during which the SNR is required to stay below the set
                              threshold for convergence.  Default value: 10. 

--convergence-snr-trigger-threshold:Double
                              The SNR threshold to be reached before triggering the convergence countdown.  Default
                              value: 0.1. 

--copy-number-posterior-expectation-mode:CopyNumberPosteriorExpectationMode
                              The strategy for calculating copy number posterior expectations in the coverage denoising
                              model.  Default value: HYBRID. Possible values: {MAP, EXACT, HYBRID} 

--depth-correction-tau:Double Precision of read depth pinning to its global value.  Default value: 10000.0. 

--disable-annealing:Boolean   (advanced) Disable annealing.  Default value: false. Possible values: {true, false} 

--disable-caller:Boolean      (advanced) Disable caller.  Default value: false. Possible values: {true, false} 

--disable-sampler:Boolean     (advanced) Disable sampler.  Default value: false. Possible values: {true, false} 

--enable-bias-factors:Boolean Enable discovery of bias factors.  Default value: true. Possible values: {true, false} 

--exclude-intervals,-XL:StringOne or more genomic intervals to exclude from processing  This argument may be specified 0
                              or more times. Default value: null. 

--gatk-config-file:String     A configuration file to use with the GATK.  Default value: null. 

--gc-curve-standard-deviation:Double
                              Prior standard deviation of the GC curve from flat.  Default value: 1.0. 

--gcs-max-retries,-gcs-retries:Integer
                              If the GCS bucket channel errors out, how many times it will attempt to re-initiate the
                              connection  Default value: 20. 

--gcs-project-for-requester-pays:String
                              Project to bill when accessing "requester pays" buckets. If unset, these buckets cannot be
                              accessed.  Default value: . 

--help,-h:Boolean             display the help message  Default value: false. Possible values: {true, false} 

--init-ard-rel-unexplained-variance:Double
                              Initial value of ARD prior precisions relative to the scale of interval-specific
                              unexplained variance.  Default value: 0.1. 

--initial-temperature:Double  Initial temperature (for DA-ADVI).  Default value: 1.5. 

--interval-exclusion-padding,-ixp:Integer
                              Amount of padding (in bp) to add to each interval you are excluding.  Default value: 0. 

--interval-merging-rule,-imr:IntervalMergingRule
                              Interval merging rule for abutting intervals  Default value: ALL. Possible values: {ALL,
                              OVERLAPPING_ONLY} 

--interval-padding,-ip:IntegerAmount of padding (in bp) to add to each interval you are including.  Default value: 0. 

--interval-psi-scale:Double   Typical scale of interval-specific unexplained variance.  Default value: 0.001. 

--interval-set-rule,-isr:IntervalSetRule
                              Set merging approach to use for combining interval inputs  Default value: UNION. Possible
                              values: {UNION, INTERSECTION} 

--intervals,-L:String         One or more genomic intervals over which to operate  This argument may be specified 0 or
                              more times. Default value: null. 

--learning-rate:Double        Adamax optimizer learning rate.  Default value: 0.01. 

--log-emission-samples-per-round:Integer
                              Log emission samples drawn per round of sampling.  Default value: 50. 

--log-emission-sampling-median-rel-error:Double
                              Maximum tolerated median relative error in log emission sampling.  Default value: 0.005. 

--log-emission-sampling-rounds:Integer
                              Log emission maximum sampling rounds.  Default value: 10. 

--log-mean-bias-standard-deviation:Double
                              Standard deviation of log mean bias.  Default value: 0.1. 

--mapping-error-rate:Double   Typical mapping error rate.  Default value: 0.01. 

--max-advi-iter-first-epoch:Integer
                              Maximum ADVI iterations in the first epoch.  Default value: 5000. 

--max-advi-iter-subsequent-epochs:Integer
                              Maximum ADVI iterations in subsequent epochs.  Default value: 200. 

--max-bias-factors:Integer    Maximum number of bias factors.  Default value: 5. 

--max-calling-iters:Integer   Maximum number of internal self-consistency iterations within each calling step.  Default
                              value: 10. 

--max-copy-number:Integer     Highest allowed copy-number state.  Default value: 5. 

--max-training-epochs:Integer Maximum number of training epochs.  Default value: 50. 

--min-training-epochs:Integer Minimum number of training epochs.  Default value: 10. 

--model:File                  Input denoising-model directory. In COHORT mode, this argument is optional; if provided,a
                              new model will be built using this input model to initialize. In CASE mode, this argument
                              is required and the denoising model parameters are set to this input model.  Default
                              value: null. 

--num-gc-bins:Integer         Number of bins used to represent the GC-bias curves.  Default value: 20. 

--num-thermal-advi-iters:Integer
                              Number of thermal ADVI iterations (for DA-ADVI).  Default value: 2500. 

--p-active:Double             Prior probability of treating an interval as CNV-active (in a CNV-active domains, all
                              copy-number states are equally likely to be called).  Default value: 0.01. 

--p-alt:Double                Total prior probability of alternative copy-number states (the reference copy-number is
                              set to the contig integer ploidy)  Default value: 1.0E-6. 

--QUIET:Boolean               Whether to suppress job-summary info on System.err.  Default value: false. Possible
                              values: {true, false} 

--sample-psi-scale:Double     Typical scale of sample-specific correction to the unexplained variance.  Default value:
                              1.0E-4. 

--tmp-dir:GATKPathSpecifier   Temp directory to use.  Default value: null. 

--use-jdk-deflater,-jdk-deflater:Boolean
                              Whether to use the JdkDeflater (as opposed to IntelDeflater)  Default value: false.
                              Possible values: {true, false} 

--use-jdk-inflater,-jdk-inflater:Boolean
                              Whether to use the JdkInflater (as opposed to IntelInflater)  Default value: false.
                              Possible values: {true, false} 

--verbosity,-verbosity:LogLevel
                              Control verbosity of logging.  Default value: INFO. Possible values: {ERROR, WARNING,
                              INFO, DEBUG} 

--version:Boolean             display the version number for this tool  Default value: false. Possible values: {true,
                              false} 


Advanced Arguments:

--showHidden,-showHidden:Boolean
                              display hidden arguments  Default value: false. Possible values: {true, false} 


***********************************************************************

A USER ERROR has occurred: Argument input was missing: Argument 'input' is required.

***********************************************************************
Set the system property GATK_STACKTRACE_ON_USER_EXCEPTION (--java-options '-DGATK_STACKTRACE_ON_USER_EXCEPTION=true') to print the stack trace.

```