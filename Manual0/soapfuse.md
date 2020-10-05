
### soapfuse
```
conda install -c isotex soapfuse
```


tools

```
cd /home/wzk/anaconda3/envs/py35/bin &&  ls | grep SOAP

SOAPfuse-RUN.pl
SOAPfuse-S00-Generate_SOAPfuse_database.pl
SOAPfuse-v1.26
```


arguments:
```
$ SOAPfuse-RUN.pl

 Usage:
    perl SOAPfuse-RUN.pl [Options]
 Version:
    V1.19 at 2016-01-18
 Options:
    -c   [s]  Config File of SOAPfuse pipeline. <required>
    -fd  [s]  Directory which stores Paired-end Sequenced Read Files. <required>
                Sequenced Reads Format can be fastq or fasta.
                Files could be compressed by gzip or just readable text-format.
    -l   [s]  The informations list of samples you want to deal. <required>
                This list can include infomations of one or more samples, prepare it according to Format below.
                It is suggested to include one sample/patient in each sample list file.
    -o   [s]  Directory which will store all results. 
                It has the first priority, or you should set it in config file (find 'PD_all_out' and set).
    -fs  [i]  The step you want to start from. [1]
    -es  [i]  The step you want to end at. [9]
                Step 9 is the last step of the SOAPfuse pipeline.
    -tp  [s]  The name-postfix of temp dir stores config and shells. [`data +%s`.'_'.int(rand(1000)+1)]
                Donot set same string for different Sample-info-list('-l').
                It is suggested to set this parameter as same as SampleID for distinguishing the scripts of 
                different samples easily in the general case that sample-info-list just includes one sample.
    -fm       Sign to enable perl fork management. [disabled]
    -h        Display this help info.
 Format:
    -l  (one line one lane, 4 columns)
       1        2      3        4
    SampleID   Lib   Lane   readlength

 Author:
    Wenlong Jia (jiawenlong@genomics.org.cn, wenlongkxm@gmail.com)
```
