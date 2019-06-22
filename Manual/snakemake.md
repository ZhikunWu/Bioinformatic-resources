
### [Invoking the snakemake workflow on a cluster](https://shahlab.ca/projects/TitanCNA/scripts/snakemake/): 

#### qsub

There are 2 separate files in use for qsub, which are provided as a template: config/cluster_qsub.sh - This file contains other qsub parameters. Note that these settings are used for the Broad’s UGER cluster so users will need to modify this for their own clusters.
config/cluster_qsub.yaml - This file contains the memory, runtime, and number of cores for certain tasks.

To invoke the snakemake pipeline for qsub:

```
snakemake -s TitanCNA.snakefile --jobscript config/cluster_qsub.sh --cluster-config config/cluster_qsub.yaml --cluster-sync "qsub -l h_vmem={cluster.h_vmem},h_rt={cluster.h_rt} -pe {cluster.pe} -binding {cluster.binding}" -j 50
```

#### slurm

There is only one file in use for slurm: config/cluster_slurm.yaml - This file contains the memory, runtime, and number of cores for certain tasks. To invoke the snakemake pipeline for qsub:

```
snakemake -s TitanCNA.snakefile --cluster-config config/cluster_slurm.yaml --cluster "sbatch -p {cluster.partition} --mem={cluster.mem} -t {cluster.time} -c {cluster.ncpus} -n {cluster.ntasks} -o {cluster.output}" -j 50
```

### [qsub and snakemake](https://biolearnr.blogspot.com/2016/05/qsub-and-snakemake.html)




### snakemake in cluster
```
snakemake -s /home/wuzhikun/github/MinION_pipeline/pipeline/NanoBenchmark.pipeline.py --configfile /home/wuzhikun/github/MinION_pipeline/pipeline/NanoBenchmark.pipeline.yaml -j 20 --rerun-incomplete --cluster "qsub -l nodes=cu01:ppn=8+cu02:ppn=8"
```

But the tasks just run in one node


```
snakemake -j 16 \
--local-cores 4 \
-w 90 \
--max-jobs-per-second 8 \
--cluster-config cluster.json \
--cluster "qsub -k eo -m n -l nodes=1:ppn={cluster.n} -l mem={cluster.mem}gb -l walltime={cluster.time}" \
--directory "$@"
```

* -j 16: Runs no more than 16 jobs concurrently. If you have 96 samples that each need to get FastQC'd, it will only run 16 of these jobs at a time.

* --local-cores 4: For rules specified as local rules (like linking files), limits to use of 4 CPUs at a time.

* -w 90: Waits for at most 90 seconds after a job executes for the output files to be available. This has to do with tolerating latency on the filesystem: sometimes a file is created by a job but isn't immediately visible to the Snakemake process that's scheduling things.

* --max-jobs-per-second 8: Limits the rate at which Snakemake is sending jobs to the cluster.

* --cluster-config cluster.json Looks in the current directory for a file called cluster.json that contains information about how many resources to request from the cluster for each rule type.

* --cluster "qsub -k eo [...]": This tells Snakemake how to send a job to the cluster scheduler, and how to request the specific resources defined in the cluster.json file.

* --directory "$@": This passes all the input provided after bash launch.sh as further input to Snakemake. Because it comes right after the --directory flag, it's going to expect the first element of that input to be the path to the working directory where Snakemake should execute.

### [snakemake-mothur](https://github.com/AAFC-BICoE/snakemake-mothur): Example of a snakemake workflow implementation of the mothur MiSEQ SOP


