
### [Quality trimming and adapter removal using TRIMMOMATIC](https://github.com/biomendi/TRANSCRIPTOME-ASSEMBLY-PIPELINE/wiki/4.-Quality-trimming-and-adapter-removal-using-TRIMMOMATIC)

```
java -Xmx1G -jar /path_to_trimmomatic/trimmomatic-0.32.jar PE -phred33 -threads 16 -trimlog logfile \
/path_to_sortmerna_results/reads_non_rRNA_1.fq /path_to_sortmerna_results/reads_non_rRNA_2.fq \
reads_left_P_qtrim.fq reads_left_U_qtrim.fq reads_right_P_qtrim.fq reads_right_U_qtrim.fq \
ILLUMINACLIP:/path_to_trimmomatic/TruSeq_adapters.fa:2:30:10 SLIDINGWINDOW:5:20 LEADING:5 TRAILING:5 MINLEN:50 
```

* PE: data is paired end.
* -phred33: Quality scores are 33 offset.
* -threads: number of threads to use.
* -trimlog logfile: name of logfile for summary information.
* brain_non_rRNA_1.fq: name of input fastq file for left reads.
* brain_non_rRNA_2.fq: name of input fastq file for right reads.
* brain_left_P_qtrim.fq: paired trimmed output fastq file for left reads.
* brain_left_U_qtrim.fq: unpaired trimmed output fastq file for left reads.
* brain_right_P_qtrim.fq: paired trimmed output fastq file for right reads.
* brain_right_U_qtrim.fq: unpaired trimmed output fastq file for right reads.
* ILLUMINACLIP: parameters for the adapter clipping.
* TruSeq_adapters.fa: text file of adapter sequences to search for.
* 2:30:10: adapter-read alignment settings – see manual.
* LEADING:5: cut bases off the start of a read, if quality score < 5.
* TRAILING:5: cut bases off the end of a read, if quality score < 5.
* MINLEN:50: drop the read if it's length < 50.

