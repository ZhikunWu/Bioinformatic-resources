
## [strelka](https://github.com/Illumina/strelka)

Germline and somatic small variant caller

### [Strelka User Guide](https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/README.md#somatic-configuration-example)

### demo germline workflow 

```

 ./runStrelkaGermlineWorkflowDemo.bash 

**** Starting demo configuration and run.
**** Configuration cmd: './configureStrelkaGermlineWorkflow.py --bam='./../share/demo/strelka/data/NA12891_demo20.bam' --bam='./../share/demo/strelka/data/NA12892_demo20.bam' --referenceFasta='./../share/demo/strelka/data/demo20.fa' --callMemMb=1024 --exome --disableSequenceErrorEstimation --runDir=./strelkaGermlineDemoAnalysis'


Successfully created workflow run script.
To execute the workflow, run the following script and set appropriate options:

/home/wuzhikun/anaconda3/envs/Assembly/bin/strelka-2.9.10.centos6_x86_64/bin/strelkaGermlineDemoAnalysis/runWorkflow.py

**** Completed demo configuration.


**** Starting demo workflow execution.
**** Workflow cmd: './strelkaGermlineDemoAnalysis/runWorkflow.py -m local -j 1 -g 4'

[2019-05-29T02:20:49.039290Z] [mu01] [31686_1] [WorkflowRunner] Initiating pyFlow run
[2019-05-29T02:20:49.237301Z] [mu01] [31686_1] [WorkflowRunner] pyFlowClientWorkflowClass: StrelkaGermlineWorkflow
[2019-05-29T02:20:49.270538Z] [mu01] [31686_1] [WorkflowRunner] pyFlowVersion: 1.1.20
[2019-05-29T02:20:49.289678Z] [mu01] [31686_1] [WorkflowRunner] pythonVersion: 2.7.15.final.0
[2019-05-29T02:20:49.323021Z] [mu01] [31686_1] [WorkflowRunner] WorkingDir: '/home/wuzhikun/anaconda3/envs/Assembly/bin/strelka-2.9.10.centos6_x86_64/bin'
[2019-05-29T02:20:49.375250Z] [mu01] [31686_1] [WorkflowRunner] ProcessCmdLine: './strelkaGermlineDemoAnalysis/runWorkflow.py -m local -j 1 -g 4'
[2019-05-29T02:20:49.408537Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] mode: local
[2019-05-29T02:20:49.612289Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] nCores: 1
[2019-05-29T02:20:49.667976Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] memMb: 4096
[2019-05-29T02:20:49.890306Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] dataDir: /home/wuzhikun/anaconda3/envs/Assembly/bin/strelka-2.9.10.centos6_x86_64/bin/strelkaGermlineDemoAnalysis/workspace/pyflow.data
[2019-05-29T02:20:49.948470Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] isDryRun: False
[2019-05-29T02:20:50.012334Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] isContinue: False
[2019-05-29T02:20:50.031371Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] isForceContinue: True
[2019-05-29T02:20:50.081708Z] [mu01] [31686_1] [WorkflowRunner] [RunParameters] mailTo: ''
[2019-05-29T02:20:50.117614Z] [mu01] [31686_1] [TaskRunner:masterWorkflow] Starting task specification for master workflow
[2019-05-29T02:20:50.150363Z] [mu01] [31686_1] [StrelkaGermlineWorkflow] Initiating Strelka germline workflow version: 2.9.10
[2019-05-29T02:20:50.210140Z] [mu01] [31686_1] [WorkflowRunner] Adding sub-workflow task 'CallGenome' to master workflow
[2019-05-29T02:20:50.305758Z] [mu01] [31686_1] [TaskManager] Launching sub-workflow task: 'CallGenome' from master workflow
[2019-05-29T02:20:50.661603Z] [mu01] [31686_1] [TaskRunner:masterWorkflow] Finished task specification for master workflow
[2019-05-29T02:20:51.679684Z] [mu01] [31686_1] [TaskRunner:CallGenome] Starting task specification for sub-workflow
[2019-05-29T02:20:52.763141Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+makeTmpDir' to sub-workflow 'CallGenome'
[2019-05-29T02:20:53.776227Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+callGenomeSegment_chromId_000_demo20_0000' to sub-workflow 'CallGenome'
[2019-05-29T02:20:54.805520Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_variants' to sub-workflow 'CallGenome'
[2019-05-29T02:20:55.840687Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S1' to sub-workflow 'CallGenome'
[2019-05-29T02:20:56.671477Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+makeTmpDir' from sub-workflow 'CallGenome'
[2019-05-29T02:20:57.413164Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S2' to sub-workflow 'CallGenome'
[2019-05-29T02:20:58.180962Z] [mu01] [31686_1] [TaskRunner:CallGenome+makeTmpDir] Task initiated on local node
[2019-05-29T02:20:58.699310Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+completedAllGenomeSegments' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.117727Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+variants_concat_vcf' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.396960Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+variants_index_vcf' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.459211Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+gVCF_S1_concat_vcf' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.482208Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+gVCF_S1_index_vcf' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.533212Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+addLegacyOutputLink' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.564974Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+gVCF_S2_concat_vcf' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.607242Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+gVCF_S2_index_vcf' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.665282Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+mergeRunStats' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.790564Z] [mu01] [31686_1] [WorkflowRunner] Adding command task 'CallGenome+removeTmpDir' to sub-workflow 'CallGenome'
[2019-05-29T02:20:59.826001Z] [mu01] [31686_1] [TaskRunner:CallGenome] Finished task specification for sub-workflow
[2019-05-29T02:21:00.566589Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+makeTmpDir' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:01.641313Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+callGenomeSegment_chromId_000_demo20_0000' from sub-workflow 'CallGenome'
[2019-05-29T02:21:02.332963Z] [mu01] [31686_1] [TaskRunner:CallGenome+callGenomeSegment_chromId_000_demo20_0000] Task initiated on local node
[2019-05-29T02:21:08.134083Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+callGenomeSegment_chromId_000_demo20_0000' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:08.934970Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S1' from sub-workflow 'CallGenome'
[2019-05-29T02:21:09.728169Z] [mu01] [31686_1] [TaskRunner:CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S1] Task initiated on local node
[2019-05-29T02:21:12.982390Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S1' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:13.007767Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_variants' from sub-workflow 'CallGenome'
[2019-05-29T02:21:13.102314Z] [mu01] [31686_1] [TaskRunner:CallGenome+compressGenomeSegment_chromId_000_demo20_0000_variants] Task initiated on local node
[2019-05-29T02:21:15.756575Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_variants' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:16.532976Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S2' from sub-workflow 'CallGenome'
[2019-05-29T02:21:16.757276Z] [mu01] [31686_1] [TaskRunner:CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S2] Task initiated on local node
[2019-05-29T02:21:19.560721Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+compressGenomeSegment_chromId_000_demo20_0000_gVCF_S2' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:19.584856Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+completedAllGenomeSegments' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:19.777489Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+gVCF_S1_concat_vcf' from sub-workflow 'CallGenome'
[2019-05-29T02:21:19.825026Z] [mu01] [31686_1] [TaskRunner:CallGenome+gVCF_S1_concat_vcf] Task initiated on local node
[2019-05-29T02:21:22.028465Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+gVCF_S1_concat_vcf' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:22.840898Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+gVCF_S2_concat_vcf' from sub-workflow 'CallGenome'
[2019-05-29T02:21:23.632003Z] [mu01] [31686_1] [TaskRunner:CallGenome+gVCF_S2_concat_vcf] Task initiated on local node
[2019-05-29T02:21:29.532683Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+gVCF_S2_concat_vcf' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:29.651865Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+mergeRunStats' from sub-workflow 'CallGenome'
[2019-05-29T02:21:29.709011Z] [mu01] [31686_1] [TaskRunner:CallGenome+mergeRunStats] Task initiated on local node
[2019-05-29T02:21:31.210154Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+mergeRunStats' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:31.606804Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+gVCF_S1_index_vcf' from sub-workflow 'CallGenome'
[2019-05-29T02:21:31.734292Z] [mu01] [31686_1] [TaskRunner:CallGenome+gVCF_S1_index_vcf] Task initiated on local node
[2019-05-29T02:21:36.592404Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+gVCF_S1_index_vcf' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:36.622234Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+addLegacyOutputLink' from sub-workflow 'CallGenome'
[2019-05-29T02:21:36.726619Z] [mu01] [31686_1] [TaskRunner:CallGenome+addLegacyOutputLink] Task initiated on local node
[2019-05-29T02:21:41.877276Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+addLegacyOutputLink' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:42.635313Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+variants_concat_vcf' from sub-workflow 'CallGenome'
[2019-05-29T02:21:43.514695Z] [mu01] [31686_1] [TaskRunner:CallGenome+variants_concat_vcf] Task initiated on local node
[2019-05-29T02:21:46.268506Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+variants_concat_vcf' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:46.297640Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+variants_index_vcf' from sub-workflow 'CallGenome'
[2019-05-29T02:21:46.365777Z] [mu01] [31686_1] [TaskRunner:CallGenome+variants_index_vcf] Task initiated on local node
[2019-05-29T02:21:48.117961Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+variants_index_vcf' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:48.142526Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+gVCF_S2_index_vcf' from sub-workflow 'CallGenome'
[2019-05-29T02:21:48.188947Z] [mu01] [31686_1] [TaskRunner:CallGenome+gVCF_S2_index_vcf] Task initiated on local node
[2019-05-29T02:21:54.541806Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+gVCF_S2_index_vcf' launched from sub-workflow 'CallGenome'
[2019-05-29T02:21:55.499241Z] [mu01] [31686_1] [TaskManager] Launching command task: 'CallGenome+removeTmpDir' from sub-workflow 'CallGenome'
[2019-05-29T02:21:56.499285Z] [mu01] [31686_1] [TaskRunner:CallGenome+removeTmpDir] Task initiated on local node
[2019-05-29T02:22:00.851348Z] [mu01] [31686_1] [TaskManager] Completed command task: 'CallGenome+removeTmpDir' launched from sub-workflow 'CallGenome'
[2019-05-29T02:22:04.753090Z] [mu01] [31686_1] [TaskManager] Completed sub-workflow task: 'CallGenome' launched from master workflow
[2019-05-29T02:22:09.838141Z] [mu01] [31686_1] [WorkflowRunner] Strelka germline workflow successfully completed.
[2019-05-29T02:22:09.838141Z] [mu01] [31686_1] [WorkflowRunner] 
[2019-05-29T02:22:09.838141Z] [mu01] [31686_1] [WorkflowRunner] 	workflow version: 2.9.10
[2019-05-29T02:22:09.865602Z] [mu01] [31686_1] [WorkflowRunner] 
[2019-05-29T02:22:09.899551Z] [mu01] [31686_1] [WorkflowRunner] Workflow successfully completed all tasks
[2019-05-29T02:22:09.954072Z] [mu01] [31686_1] [WorkflowRunner] Elapsed time for full workflow: 81 sec

**** Completed demo workflow execution.


**** Demo/verification successfully completed

```

### config file
tails of runWorkflow.py.config.pickle
```
p90
I12
sS'bgzipBin'
p91
S'/home/wuzhikun/anaconda3/envs/Assembly/bin/strelka-2.9.10.centos6_x86_64/libexec/bgzip'
p92
sS'configCommandLine'
p93
(lp94
S'./configureStrelkaGermlineWorkflow.py'
p95
aS'--bam=./../share/demo/strelka/data/NA12891_demo20.bam'
p96
aS'--bam=./../share/demo/strelka/data/NA12892_demo20.bam'
p97
aS'--referenceFasta=./../share/demo/strelka/data/demo20.fa'
p98
aS'--callMemMb=1024'
p99
aS'--exome'
p100
aS'--disableSequenceErrorEstimation'
p101
aS'--runDir=./strelkaGermlineDemoAnalysis'
p102

```



### output files
```
drwxrwxr-x 1 4.0K May 29 10:20 results
-rwxr-xr-x 1 7.9K May 29 10:20 runWorkflow.py
-rw-rw-r-- 1 4.8K May 29 10:20 runWorkflow.py.config.pickle
-rw-rw-r-- 1    0 May 29 10:20 workflow.error.log.txt
-rw-rw-r-- 1    2 May 29 10:22 workflow.exitcode.txt
-rw-rw-r-- 1    0 May 29 10:20 workflow.warning.log.txt
drwxrwxr-x 1 4.0K May 29 10:21 workspace

```


output results
```
results/
├── stats
│   ├── runStats.tsv
│   └── runStats.xml
└── variants
    ├── genome.S1.vcf.gz
    ├── genome.S1.vcf.gz.tbi
    ├── genome.S2.vcf.gz
    ├── genome.S2.vcf.gz.tbi
    ├── genome.vcf.gz -> genome.S1.vcf.gz
    ├── genome.vcf.gz.tbi -> genome.S1.vcf.gz.tbi
    ├── variants.vcf.gz
    └── variants.vcf.gz.tbi

```



### vcf file
```
$ less   variants.vcf.gz

#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  NA12891 NA12892
demo20  991     .       C       G       38      PASS    SNVHPOL=2;MQ=59 GT:GQ:GQX:DP:DPF:AD:ADF:ADR:SB:FT:PL    0/1:71:38:9:1:5,4:1,4:4,0:2.8:PASS:72,0,123     0/0:33:33:12:0:12,0:9,0:3,0:0.0:PASS:0,36,258
demo20  1148    .       C       CTAT    72      PASS    CIGAR=1M3I;RU=TAT;REFREP=1;IDREP=2;MQ=60        GT:GQ:GQX:DPI:AD:ADF:ADR:FT:PL  0/1:114:72:20:11,8:5,3:6,5:PASS:111,0,147       0/0:69:69:28:24,0:12,0:12,0:PASS:0,72,443
demo20  1271    .       A       G       134     PASS    SNVHPOL=4;MQ=60 GT:GQ:GQX:DP:DPF:AD:ADF:ADR:SB:FT:PL    0/1:126:126:18:0:8,10:7,6:1,4:-18.6:PASS:169,0,123      0/0:75:75:26:0:26,0:18,0:8,0:0.0:PASS:0,78,370
demo20  1508    .       A       G       156     PASS    SNVHPOL=3;MQ=60 GT:GQ:GQX:DP:DPF:AD:ADF:ADR:SB:FT:PL    0/1:172:156:22:1:10,12:4,6:6,6:-21.5:PASS:191,0,169     0/0:108:108:37:2:37,0:19,0:18,0:0.0:PASS:
0,111,370
demo20  1706    .       C       T       304     PASS    SNVHPOL=2;MQ=59 GT:GQ:GQX:DP:DPF:AD:ADF:ADR:SB:FT:PL    1/1:54:54:19:0:0,19:0,8:0,11:-35.5:PASS:342,57,0        0/0:90:90:31:2:31,0:7,0:24,0:0.0:PASS:0,9
3,370
demo20  1744    .       C       T       156     PASS    SNVHPOL=3;MQ=59 GT:GQ:GQX:DP:DPF:AD:ADF:ADR:SB:FT:PL    0/1:159:154:21:0:9,12:5,6:4,6:-20.7:PASS:191,0,156      0/0:78:78:27:0:27,0:6,0:21,0:0.0:PASS:0,8
1,370
demo20  1846    .       C       T       83      PASS    SNVHPOL=3;MQ=60 GT:GQ:GQX:DP:DPF:AD:ADF:ADR:SB:FT:PL    0/1:116:83:24:1:16,8:13,5:3,3:-12.4:PASS:117,0,224      0/0:60:60:21:0:21,0:14,0:7,0:0.0:PASS:0,6
3,370
demo20  1873    .       C       T       122     PASS    SNVHPOL=3;MQ=60 GT:GQ:GQX:DP:DPF:AD:ADF:ADR:SB:FT:PL    0/0:60:60:21:0:21,0:15,0:6,0:0.0:PASS:0,63,360  0/1:155:122:23:0:13,10:8,7:5,3:-14.9:PASS:157,0,1

```


### somatic variants
```
$ python configureStrelkaSomaticWorkflow.py --allHelp
Usage: configureStrelkaSomaticWorkflow.py [options]

Version: 2.9.10

This script configures Strelka somatic small variant calling.
You must specify an alignment file (BAM or CRAM) for each sample of a matched tumor-normal pair.

Configuration will produce a workflow run script which
can execute the workflow on a single node or through
sge and resume any interrupted execution.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --config=FILE         provide a configuration file to override defaults in
                        global config file (/home/wuzhikun/anaconda3/envs/Asse
                        mbly/bin/strelka-2.9.10.centos6_x86_64/bin/configureSt
                        relkaSomaticWorkflow.py.ini)
  --allHelp             show all extended/hidden options

  Workflow options:
    --normalBam=FILE    Normal sample BAM or CRAM file. (no default)
    --tumorBam=FILE, --tumourBam=FILE
                        Tumor sample BAM or CRAM file. [required] (no default)
    --outputCallableRegions
                        Output a bed file describing somatic callable regions
                        of the genome
    --referenceFasta=FILE
                        samtools-indexed reference fasta file [required]
    --indelCandidates=FILE
                        Specify a VCF of candidate indel alleles. These
                        alleles are always evaluated but only reported in the
                        output when they are inferred to exist in the sample.
                        The VCF must be tabix indexed. All indel alleles must
                        be left-shifted/normalized, any unnormalized alleles
                        will be ignored. This option may be specified more
                        than once, multiple input VCFs will be merged.
                        (default: None)
    --forcedGT=FILE     Specify a VCF of candidate alleles. These alleles are
                        always evaluated and reported even if they are
                        unlikely to exist in the sample. The VCF must be tabix
                        indexed. All indel alleles must be left-
                        shifted/normalized, any unnormalized allele will
                        trigger a runtime error. This option may be specified
                        more than once, multiple input VCFs will be merged.
                        Note that for any SNVs provided in the VCF, the SNV
                        site will be reported (and for gVCF, excluded from
                        block compression), but the specific SNV alleles are
                        ignored. (default: None)
    --exome, --targeted
                        Set options for exome or other targeted input: note in
                        particular that this flag turns off high-depth filters
    --callRegions=FILE  Optionally provide a bgzip-compressed/tabix-indexed
                        BED file containing the set of regions to call. No VCF
                        output will be provided outside of these regions. The
                        full genome will still be used to estimate statistics
                        from the input (such as expected depth per
                        chromosome). Only one BED file may be specified.
                        (default: call the entire genome)
    --runDir=DIR        Name of directory to be created where all workflow
                        scripts and output will be written. Each analysis
                        requires a separate directory. (default:
                        StrelkaSomaticWorkflow)

  Extended options:
    These options are either unlikely to be reset after initial site
    configuration or only of interest for workflow development/debugging.
    They will not be printed here if a default exists unless --allHelp is
    specified

    --noiseVcf=FILE     Noise vcf file (submit argument multiple times for
                        more than one file)
    --scanSizeMb=INT    Maximum sequence region size (in megabases) scanned by
                        each task during genome variant calling. (default: 12)
    --region=REGION     Limit the analysis to one or more genome region(s) for
                        debugging purposes. If this argument is provided
                        multiple times the union of all specified regions will
                        be analyzed. All regions must be non-overlapping to
                        get a meaningful result. Examples: '--region chr20'
                        (whole chromosome), '--region chr2:100-2000 --region
                        chr3:2500-3000' (two regions)'. If this option is
                        specified (one or more times) together with the
                        --callRegions BED file, then all region arguments will
                        be intersected with the callRegions BED track.
    --callMemMb=INT     Set variant calling task memory limit (in megabytes).
                        It is not recommended to change the default in most
                        cases, but this might be required for a sample of
                        unusual depth.
    --retainTempFiles   Keep all temporary files (for workflow debugging)
    --disableEVS        Disable empirical variant scoring (EVS).
    --reportEVSFeatures
                        Report all empirical variant scoring features in VCF
                        output.
    --snvScoringModelFile=FILE
                        Provide a custom empirical scoring model file for SNVs
                        (default: /home/wuzhikun/anaconda3/envs/Assembly/bin/s
                        trelka-2.9.10.centos6_x86_64/share/config/somaticSNVSc
                        oringModels.json)
    --indelScoringModelFile=FILE
                        Provide a custom empirical scoring model file for
                        indels (default: /home/wuzhikun/anaconda3/envs/Assembl
                        y/bin/strelka-2.9.10.centos6_x86_64/share/config/somat
                        icIndelScoringModels.json)

```


### Build the workflow
```
$ python /home/wuzhikun/anaconda3/envs/Assembly/bin/strelka-2.9.10.centos6_x86_64/bin/configureStrelkaSomaticWorkflow.py --normalBam=M625-1/M625-1.bqsr.bam  --tumorBam=M625-0/M625-0.bqsr.bam  --referenceFasta=/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --runDir=/home/wuzhikun/Project/Illumina_Trio/mapping/M625_strelka

Successfully created workflow run script.
To execute the workflow, run the following script and set appropriate options:

/home/wuzhikun/Project/Illumina_Trio/mapping/M625_strelka/runWorkflow.py

```



```

$ python /home/wuzhikun/anaconda3/envs/Assembly/bin/strelka-2.9.10.centos6_x86_64/bin/configureStrelkaSomaticWorkflow.py --normalBam=mapping/SRR62/SRR62.bqsr.bam --tumorBam=mapping/SRR60/SRR60.bqsr.bam --referenceFasta=/home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa  --runDir=/home/wuzhikun/Project/WGSSomatic/strelka

Successfully created workflow run script.
To execute the workflow, run the following script and set appropriate options:

/home/wuzhikun/Project/WGSSomatic/strelka/runWorkflow.py
```


#### workflow parameters
```
$ /home/wuzhikun/Project/WGSSomatic/strelka/runWorkflow.py --help
Usage: runWorkflow.py [options]

Version: 2.9.10

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -m MODE, --mode=MODE  select run mode (local|sge)
  -q QUEUE, --queue=QUEUE
                        specify scheduler queue name
  -j JOBS, --jobs=JOBS  number of jobs, must be an integer or 'unlimited'
                        (default: Estimate total cores on this node for local
                        mode, 128 for sge mode)
  -g MEMGB, --memGb=MEMGB
                        gigabytes of memory available to run workflow -- only
                        meaningful in local mode, must be an integer (default:
                        Estimate the total memory for this node for local
                        mode, 'unlimited' for sge mode)
  -d, --dryRun          dryRun workflow code without actually running command-
                        tasks
  --quiet               Don't write any log output to stderr (but still write
                        to workspace/pyflow.data/logs/pyflow_log.txt)

  development debug options:
    --rescore           Reset task list to re-run hypothesis generation and
                        scoring without resetting graph generation.

  extended portability options (should not be needed by most users):
    --maxTaskRuntime=hh:mm:ss
                        Specify scheduler max runtime per task, argument is
                        provided to the 'h_rt' resource limit if using SGE (no
                        default)

Note this script can be re-run to continue the workflow run in case of
interruption. Also note that dryRun option has limited utility when
task definition depends on upstream task results -- in this case the
dry run will not cover the full 'live' run task set.


```


### Run workflow

```
$ /home/wuzhikun/Project/WGSSomatic/strelka/runWorkflow.py --mode=local --jobs=24 --memGb=80



[2019-05-31T03:03:31.032319Z] [cu04] [15765_1] [WorkflowRunner] Initiating pyFlow run
[2019-05-31T03:03:33.639946Z] [cu04] [15765_1] [WorkflowRunner] pyFlowClientWorkflowClass: StrelkaSomaticWorkflow
[2019-05-31T03:03:36.356176Z] [cu04] [15765_1] [WorkflowRunner] pyFlowVersion: 1.1.20
[2019-05-31T03:03:39.051165Z] [cu04] [15765_1] [WorkflowRunner] pythonVersion: 2.7.15.final.0
[2019-05-31T03:03:41.179116Z] [cu04] [15765_1] [WorkflowRunner] WorkingDir: '/home/wuzhikun/Project/WGSSomatic'
[2019-05-31T03:03:44.012070Z] [cu04] [15765_1] [WorkflowRunner] ProcessCmdLine: '/home/wuzhikun/Project/WGSSomatic/strelka/runWorkflow.py --mode=local --jobs=24 --memGb=80'
[2019-05-31T03:03:46.698369Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] mode: local
[2019-05-31T03:03:49.411464Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] nCores: 24
[2019-05-31T03:03:51.651756Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] memMb: 81920
[2019-05-31T03:03:54.136119Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] dataDir: /home/wuzhikun/Project/WGSSomatic/strelka/workspace/pyflow.data
[2019-05-31T03:03:56.672287Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] isDryRun: False
[2019-05-31T03:03:59.378450Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] isContinue: False
[2019-05-31T03:04:02.197482Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] isForceContinue: True
[2019-05-31T03:04:04.526461Z] [cu04] [15765_1] [WorkflowRunner] [RunParameters] mailTo: ''
[2019-05-31T03:04:07.219720Z] [cu04] [15765_1] [TaskRunner:masterWorkflow] Starting task specification for master workflow
[2019-05-31T03:04:09.140175Z] [cu04] [15765_1] [StrelkaSomaticWorkflow] Initiating Strelka somatic workflow version: 2.9.10

```



output file:

```
drwxrwxr-x 1 4.0K May 31 11:00 results
-rwxr-xr-x 1 7.9K May 31 11:00 runWorkflow.py
-rw-rw-r-- 1 3.9K May 31 11:00 runWorkflow.py.config.pickle
-rw-rw-r-- 1    0 May 31 11:03 workflow.error.log.txt
-rw-rw-r-- 1    2 May 31 12:03 workflow.exitcode.txt
-rw-rw-r-- 1    0 May 31 11:03 workflow.warning.log.txt
drwxrwxr-x 1 4.0K May 31 12:03 workspace

```

tree of results
```
$ tree strelka/results/
strelka/results/
├── stats
│   ├── runStats.tsv
│   └── runStats.xml
└── variants
    ├── somatic.indels.vcf.gz
    ├── somatic.indels.vcf.gz.tbi
    ├── somatic.snvs.vcf.gz
    └── somatic.snvs.vcf.gz.tbi
```