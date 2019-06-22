
### pbs script
```
#!/bin/sh
# Grid Engine options (lines prefixed with #$)
#$ -cwd
#$ -N dumping
#$ -l h_rt=6:00:00
#$ -l h_vmem=1G
#$ -pe sharedmem 4
. /etc/profile.d/modules.sh
module load anaconda/2.3.0
module load igmm/apps/sratoolkit/2.8.2-1
source activate Hi-C

prefetch $1 &&
parallel-fastq-dump --sra-id $1 --threads 4 --outdir . --split-files --gzip &&
rm /exports/eddie/scratch/s1529682/tmp/sra/sra/$1.sra

```
