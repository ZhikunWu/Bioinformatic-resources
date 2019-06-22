
## PBS


### qsub job script

```
#PBS -N exome_hg19
#PBS -j oe
#PBS -l nodes=1:ppn=20
#PBS -l walltime=50000:00:00
cd $PBS_O_WORKDIR

export PATH=/public/software/bcbio-nextgen/anaconda/bin:$PATH
export PATH=/public/software/bcbio-nextgen/tools/bin:$PATH
export LD_LIBRARY_PATH=/public/software/bcbio-nextgen/anaconda/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/public/software/bcbio-nextgen/tools/lib:$LD_LIBRARY_PATH
export PERL5LIB=/public/software/bcbio-nextgen/tools/lib/perl5:$PERL5LIB

bcbio_nextgen.py ../config/ZQJ_wes_2.yaml -n 20
```

```
$ pbsnodes -l free
```


#### PBS作业参数
```
#!/bin/bash
#PBS -l nodes=1:ppn=16
#PBS -l walltime=1000:00:00
#PBS -q high
#PBS -N Job_Name
#PBS -oe
your_commands_goes_here
```


#### 提交交互式作业
我们可以通过-I选项提交一个交互式的作业，效果类似直接ssh登录到计算节点
```
qsub -I -N stdin -l nodes=1:ppn=16 -l walltime=1000:00:00 -q high
```


#### 批量提交作业

template.sh
```
#!/bin/bash
#PBS -j oe
#PBS -q high
#PBS -l nodes=1:node:ppn=4
#PBS walltime=1000:00:00
hisat2 -p 4 -x hg19 -1 ./reads/${sample}_1.fq.gz -2 ./reads/${sample}_2.fq.fz -t | samtools view -bS > ./align/${sample}.bam

```



任务参数文件 job_params.csv
```
sample1
sample2
sample3

```


任务投递脚本：qsub.py
```
#!/usr/bin/env python
import csv
import subprocess
import time
param_file = './job_params.csv'
cwd = '/home/kevinzjy/RNA-seq'
with open(param_file, 'r') as f:
    reader = csv.reader(f)
    for sample in reader:
        qsub_cmd = 'qsub -N {0} -d {1} -v SAMPLE={0} template.sh'.format(sample, cwd)
        # print qsub_cwd
        exit_status = subprocess.call(qsub_cmd, shell=True)
        if exit_status is 1:
            print 'Job "{}" failed to submit'.format(qsub_cwd)
        time.sleep(1)
print "Done submitting jobs!"
```




### pbs command

```
$ qstat -a

mu01: 
                                                                                  Req'd       Req'd       Elap
Job ID                  Username    Queue    Jobname          SessID  NDS   TSK   Memory      Time    S   Time
----------------------- ----------- -------- ---------------- ------ ----- ------ --------- --------- - ---------
53523.mu01              wuzhikun    batch    TrioWGS             --      1     40     350gb  72:00:00 Q       -- 
```

```
$ qstat -q

server: mu01

Queue            Memory CPU Time Walltime Node  Run Que Lm  State
---------------- ------ -------- -------- ----  --- --- --  -----
batch              --      --       --      --   14   1 --   E R
                                               ----- -----
                                                  14     1

```


```
qdel -W 15 211            15秒后删除作业号为211的作业
```

```
$ qstat -a 

mu01: 
                                                                                  Req'd       Req'd       Elap
Job ID                  Username    Queue    Jobname          SessID  NDS   TSK   Memory      Time    S   Time
----------------------- ----------- -------- ---------------- ------ ----- ------ --------- --------- - ---------
53529.mu01              wuzhikun    batch    TrioWGS           22046     1     24     120gb  10:00:00 R  00:00:05

```

#### 批量删除作业
如果要删除一个用户所有的作业，可以使用qselect结合xargs命令，进行作业编号的提取和对指定编号作业的删除
```
qselect -u user_id | xargs qdel
```

删除某用户所有正在排队的任务：
```
qselect -u user_name -s Q | xargs qdel
```



