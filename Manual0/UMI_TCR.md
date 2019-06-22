
## UMI for TCR

### install mixcr
```bash
conda install -c bioconda mixcr
```

### install mageri
```bash
wget https://codeload.github.com/mikessh/mageri/tar.gz/1.1.1
```

### [mitcr](https://github.com/milaboratory/mitcr)


reshape, ggplot2, gridExtra, FField,
ape, reshape2, MASS, plotrix, RColorBrewer,
scales

```bash
conda install -c r r-reshape
conda install -c r r-reshape2
conda install -c r r-ggplot2
conda install -c r r-gridextra
conda install -c r r-ape
conda install -c r r-mass 
conda install -c bioconda r-plotrix
conda install -c r r-rcolorbrewer
conda install -c r r-scales
wget https://cran.r-project.org/src/contrib/FField_0.1.0.tar.gz
R CMD INSTALL FField_0.1.0.tar.gz
conda install -c r r-stringi
conda install -c r r-rmarkdown
```

### barcode
```
S2-1-beta       AAAGAcagtggtatcaacgcagagtNNNNtNNNNtNNNNtctt
S2-2-beta       ATGTGcagtggtatcaacgcagagtNNNNtNNNNtNNNNtctt

AAAGACAGTGGTATCAACGCAGAGT
ATGTGCAGTGGTATCAACGCAGAGT
```


### migec
```bash
export JAVA_OPTS="-Xmx8G" # set memory limit
MIGEC="java -jar ../migec-1.2.1b.jar"
MITCR="java -jar ../mitcr.jar"
VDJTOOLS="java -jar ../vdjtools-1.0.2.jar"
```


#### de-multiplex
```
$MIGEC Checkout -ou barcodes.txt trb_R1.fastq.gz trb_R2.fastq.gz checkout/
```

#### analyze umi coverage
```
$MIGEC Histogram checkout/ histogram/
cd histogram/
wget https://raw.githubusercontent.com/mikessh/migec/master/util/histogram.R
Rscript histogram.R
cd ..
```

#### assemble
```
$MIGEC AssembleBatch --force-overseq 5 --force-collision-filter --default-mask 0:1 checkout/ histogram/ assemble/
```


#### different quality thresholds
```
for q in 20 25 30 35; do
   $MIGEC CdrBlast -R TRB -q $q checkout/S2-1-beta_R2.fastq cdrblast/S2-1-beta.raw$q.txt
done
```

#### second sample, Q35, for replica-based filtering
```
$MIGEC CdrBlast -R TRB -q 35 checkout/S2-2-beta_R2.fastq cdrblast/S2-2-beta.raw35.txt
```

####  frequency-based error correction (mitcr)
```
$MITCR -pset flex checkout/S2-1-beta_R2.fastq cdrblast/S2-1-beta.mitcr.txt
```

####  assembled data
```
$MIGEC CdrBlast -a -R TRB assemble/S2-1-beta_R2.t5.cf.fastq cdrblast/S2-1-beta.asm.txt
$MIGEC CdrBlast -a -R TRB assemble/S2-2-beta_R2.t5.cf.fastq cdrblast/S2-2-beta.asm.txt
```

####  finalize
```
# process both raw and assembled data
$MIGEC CdrBlastBatch -R TRB checkout/ assemble/ cdrblast/
# filter results from hot-spot PCR errors
$MIGEC FilterCdrBlastResultsBatch cdrblast/ cdrfinal/
# generate report
$MIGEC Report .
```

### vdjtools
#### convert
```
$VDJTOOLS Convert -S migec `ls cdrblast/S2-*-beta.raw*.txt` `ls cdrblast/S2-*-beta.asm.txt` convert/
$VDJTOOLS Convert -S mitcr cdrblast/S2-1-beta.mitcr.txt convert/
````

#### all rarefaction curves
```
$VDJTOOLS RarefactionPlot -f sample_id `ls convert/S2-1-beta.raw*.txt` convert/S2-1-beta.mitcr.txt rarefaction/qual-and-freq
```

#### plot curve for assembled data separately, as it uses #UMIs as count, not reads
```
$VDJTOOLS RarefactionPlot -f sample_id convert/S2-1-beta.asm.txt convert/S2-2-beta.asm.txt rarefaction/umi
```


#### overlapped replicas
```
$VDJTOOLS OverlapPair convert/S2-1-beta.raw35.txt convert/S2-2-beta.raw35.txt convert/
$VDJTOOLS RarefactionPlot -f sample_id convert/S2-1-beta.raw35.txt convert/S2-2-beta.raw35.txt convert/paired.strict.table.txt rarefaction/overlap

```


```bash
$ java -jar /home/wzk/anaconda3/envs/TCR/bin/migec.jar Checkout -ou barcodes.txt trb_R1.fastq.gz trb_R2.fastq.gz checkout/
$ java -jar /home/wzk/anaconda3/envs/TCR/bin/migec.jar Histogram  checkout histogram
cd histogram

$ Rscript  /home/wzk/anaconda3/envs/TCR/bin/histogram.R 
/home/wzk/anaconda3/envs/TCR/lib/R/bin/exec/R: /home/wzk/anaconda3/envs/TCR/lib/R/bin/exec/../../lib/../../libtinfo.so.5: no version information available (required by /lib/x86_64-linux-gnu/libreadline.so.6)
Loading required package: ggplot2
Loading required package: reshape
Using V1 as id variables
Using V1 as id variables
`geom_smooth()` using method = 'loess'
Using V1 as id variables
Using V1 as id variables
`geom_smooth()` using method = 'loess'

cd ..

$ java -jar /home/wzk/anaconda3/envs/TCR/bin/migec.jar AssembleBatch --force-overseq 5 --force-collision-filter  checkout/ histogram/ assemble/
Executing com.milaboratory.migec.AssembleBatch --force-overseq 5 --force-collision-filter --default-mask 0:1 checkout/ histogram/ assemble/
[Wed Oct 11 03:00:52 EDT 2017 com.milaboratory.migec.AssembleBatch] Starting batch assembly..
Executing com.milaboratory.migec.Assemble -m 5 -q 15 --mask 0:1 --filter-collisions /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-1-beta_R1.fastq /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-1-beta_R2.fastq assemble/
[Wed Oct 11 03:00:52 EDT 2017 com.milaboratory.migec.Assemble] Pre-loading data for /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-1-beta_R1.fastq, /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-1-beta_R2.fastq..
[Wed Oct 11 03:00:53 EDT 2017 com.milaboratory.migec.Assemble] Processed 192464 reads, unique UMIs 14012
[Wed Oct 11 03:00:53 EDT 2017 com.milaboratory.migec.Assemble] Starting assembly..
[Wed Oct 11 03:00:55 EDT 2017 com.milaboratory.migec.Assemble] Processed 10000 MIGs, 142577 reads total, 1347 collisions detected, assembled so far: S2-1-beta_R2.t5.cf 333 MIGs, 118696 reads
[Wed Oct 11 03:00:55 EDT 2017 com.milaboratory.migec.Assemble] Processed 14012 MIGs, 190923 reads total, 1862 collisions detected, assembled so far: S2-1-beta_R2.t5.cf 489 MIGs, 176147 reads
[Wed Oct 11 03:00:55 EDT 2017 com.milaboratory.migec.Assemble] Finished
Executing com.milaboratory.migec.Assemble -m 5 -q 15 --mask 0:1 --filter-collisions /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-2-beta_R1.fastq /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-2-beta_R2.fastq assemble/
[Wed Oct 11 03:00:55 EDT 2017 com.milaboratory.migec.Assemble] Pre-loading data for /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-2-beta_R1.fastq, /home/wzk/anaconda3/envs/TCR/bin/repseq-tutorial/part1/checkout/S2-2-beta_R2.fastq..
[Wed Oct 11 03:00:58 EDT 2017 com.milaboratory.migec.Assemble] Processed 482011 reads, unique UMIs 24107
[Wed Oct 11 03:00:58 EDT 2017 com.milaboratory.migec.Assemble] Starting assembly..
[Wed Oct 11 03:00:58 EDT 2017 com.milaboratory.migec.Assemble] Processed 10000 MIGs, 202900 reads total, 1883 collisions detected, assembled so far: S2-2-beta_R2.t5.cf 222 MIGs, 155039 reads
[Wed Oct 11 03:00:59 EDT 2017 com.milaboratory.migec.Assemble] Processed 20000 MIGs, 395504 reads total, 3761 collisions detected, assembled so far: S2-2-beta_R2.t5.cf 490 MIGs, 352584 reads
[Wed Oct 11 03:00:59 EDT 2017 com.milaboratory.migec.Assemble] Processed 24107 MIGs, 479852 reads total, 4584 collisions detected, assembled so far: S2-2-beta_R2.t5.cf 628 MIGs, 451033 reads
[Wed Oct 11 03:00:59 EDT 2017 com.milaboratory.migec.Assemble] Finished

$ grep '^@' S2-1-beta_R2.t5.cf.fastq |  cut -d':' -f 2   | sort | uniq > S2-1-beta_R2.t5.cf.MGI



$ java -jar /home/wzk/anaconda3/envs/TCR/bin/migec.jar CdrBlastBatch --default-gene TRA  checkout/  assemble/  VDJ

$ java -jar /home/wzk/anaconda3/envs/TCR/bin/migec.jar FilterCdrBlastResultsBatch VDJ/ VDJ_filter


$ java -jar /home/wzk/anaconda3/envs/TCR/bin/migec.jar Report VDJ_filter/
Executing com.milaboratory.migec.Report VDJ_filter/
[ERROR] See log below:
/home/wzk/anaconda3/envs/TCR/lib/R/bin/exec/R: /home/wzk/anaconda3/envs/TCR/lib/R/bin/exec/../../lib/../../libtinfo.so.5: no version information available (required by /lib/x86_64-linux-gnu/libreadline.so.6)
Loading required package: rmarkdown
Warning message:
In library(package, lib.loc = lib.loc, character.only = TRUE, logical.return = TRUE,  :
  there is no package called ‘rmarkdown’
Error in render("VDJ_filter//migec_summary.Rmd") : 
  could not find function "render"
Execution halted

[NOTE] Intermediate files were not deleted


$ conda install -c r r-rmarkdown 

$ java -jar /home/wzk/anaconda3/envs/TCR/bin/migec.jar Report VDJ_filter/
```

