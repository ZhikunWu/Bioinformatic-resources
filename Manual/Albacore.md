## [Albacore](https://github.com/Albacore/albacore)

### [Albacore HowTo](http://www.taejoonlab.org/index.php/Albacore_HowTo)
### [Nanopore basecalling之Albacore](http://blog.sciencenet.cn/blog-2970729-1124496.html)]

### install albocore

#### [ont_albacore-2.3.3-cp36-cp36m-manylinux1_x86_64.whl](https://github.com/NGSchoolEU/2018/tree/master/src/whl)

```
$ pip install ont_albacore-2.3.3-cp36-cp36m-manylinux1_x86_64.whl
```

### parameters
```
$ read_fast5_basecaller.py --help
usage: read_fast5_basecaller.py [-h] [-l] [-v] [-i INPUT] -t WORKER_THREADS -s
                                SAVE_PATH [--resume [X]] [-f FLOWCELL]
                                [-k KIT] [--barcoding] [-c CONFIG]
                                [-d DATA_PATH] [-b] [-r]
                                [-n FILES_PER_BATCH_FOLDER] [-o OUTPUT_FORMAT]
                                [-q READS_PER_FASTQ_BATCH]
                                [--disable_filtering] [--disable_pings]

ONT Albacore Sequencing Pipeline Software

optional arguments:
  -h, --help            show this help message and exit
  -l, --list_workflows  List standard flowcell / kit combinations.
  -v, --version         Print the software version.
  -i INPUT, --input INPUT
                        Folder containing read fast5 files (if not present,
                        will expect file names on stdin).
  -t WORKER_THREADS, --worker_threads WORKER_THREADS
                        Number of worker threads to use.
  -s SAVE_PATH, --save_path SAVE_PATH
                        Path to save output.
  --resume [X]          Resume previous run for the given save path. Optional
                        parameter X is for debugging purposes only.
  -f FLOWCELL, --flowcell FLOWCELL
                        Flowcell used during the sequencing run.
  -k KIT, --kit KIT     Kit used during the sequencing run.
  --barcoding           Search for barcodes to demultiplex sequencing data.
  -c CONFIG, --config CONFIG
                        Optional configuration file to use.
  -d DATA_PATH, --data_path DATA_PATH
                        Optional path to model files.
  -b, --debug           Output additional debug information to the log.
  -r, --recursive       Recurse through subfolders for input data files.
  -n FILES_PER_BATCH_FOLDER, --files_per_batch_folder FILES_PER_BATCH_FOLDER
                        Maximum number of files in each batch subfolder. Set
                        to 0 to disable batch subfolders.
  -o OUTPUT_FORMAT, --output_format OUTPUT_FORMAT
                        desired output format, can be fastq,fast5 or only one
                        of these.
  -q READS_PER_FASTQ_BATCH, --reads_per_fastq_batch READS_PER_FASTQ_BATCH
                        number of reads per FastQ batch file. Set to 1 to
                        receive one reads per file and file names which
                        include the read ID. Set to 0 to have all reads per
                        run ID written to one file.
  --disable_filtering   Disable filtering into pass/fail folders
  --disable_pings       Do not send summary information about the run

```


### flowcell and kits

This produces a list of available configs:

```
Parsing config files in /opt/albacore.
Available flowcell + kit combinations are:
flowcell    kit         barcoding  config file
FLO-MIN106  SQK-LSK108             r94_450bps_linear.cfg
FLO-MIN106  SQK-LSK208             r94_250bps_2d.cfg
FLO-MIN106  SQK-LWB001  included   r94_450bps_linear.cfg
FLO-MIN106  SQK-LWP001             r94_450bps_linear.cfg
FLO-MIN106  SQK-NSK007             r94_250bps_nsk007_2d.cfg
FLO-MIN106  SQK-RAB201  included   r94_450bps_linear.cfg
FLO-MIN106  SQK-RAD002             r94_450bps_linear.cfg
FLO-MIN106  SQK-RAS201             r94_450bps_linear.cfg
FLO-MIN106  SQK-RBK001  included   r94_450bps_linear.cfg
FLO-MIN106  SQK-RLB001  included   r94_450bps_linear.cfg
FLO-MIN106  SQK-RLI001             r94_450bps_linear.cfg
FLO-MIN106  SQK-RNA001             r94_70bps_rna_linear.cfg
FLO-MIN106  VSK-VBK001             r94_450bps_linear.cfg
FLO-MIN107  SQK-LSK108             r95_450bps_linear.cfg
FLO-MIN107  SQK-LSK308             r95_450bps_linear.cfg
FLO-MIN107  SQK-LWB001  included   r95_450bps_linear.cfg
FLO-MIN107  SQK-LWP001             r95_450bps_linear.cfg
FLO-MIN107  SQK-RAB201  included   r95_450bps_linear.cfg
FLO-MIN107  SQK-RAD002             r95_450bps_linear.cfg
FLO-MIN107  SQK-RAS201             r95_450bps_linear.cfg
FLO-MIN107  SQK-RBK001  included   r95_450bps_linear.cfg
FLO-MIN107  SQK-RLB001  included   r95_450bps_linear.cfg
FLO-MIN107  SQK-RLI001             r95_450bps_linear.cfg
FLO-MIN107  VSK-VBK001             r95_450bps_linear.cfg
```


### fast5 to fastq

Finally, as base-calling is such a very compute intensive operation, we should only do this on a subset of files. A command might look like this:
```
read_fast5_basecaller.py -i /vol/raw_fast5/ \
                         -r \
                         -t 4 \
                         -s basecalled_dir \
                         -o fastq,fast5 \
                         -c r94_450bps_linear.cfg \
                         --barcoding
```


* look for fast5 in /vol/raw_fast5/
* look recursively
* use four threads
* output in basecalled_dir
* output both fastq and fast5
* use config “r94_450bps_linear.cfg” (FLO-MIN106 SQK-LSK108)
* search for barcodes and demultiplex


complete command line is:
```
read_fast5_basecaller.py -f FLO-MIN107 -k SQK-LSK308 -t 14 -s ~/workdir/1D_basecall_small -o fastq -q 100000 -i ~/workdir/Data/Nanopore_small/
```

and similar for the 1D² basecalling:

```
full_1dsq_basecaller.py -f  FLO-MIN107 -k SQK-LSK308 -t 14 -s ~/workdir/1D2_basecall_small -o fastq -q 100000 -i ~/workdir/Data/Nanopore_small/
```


#### for RNA
```
$ read_fast5_basecaller.py --input /home/wuzhikun/data/RNA/Caenorhabditis_elegans/experiments/nanopore_datasets/L1/bio1/tech1/data/fast5/11 --recursive --worker_threads 20 --flowcell FLO-MIN106  --kit SQK-RNA001  --save_path /home/wuzhikun/data/RNA/Caenorhabditis_elegans/fastq

```

output files:
```
-rw-rw-r-- 1 1.7K Jun 24 16:56 configuration.cfg
-rw-rw-r-- 1 1.1M Jun 24 17:07 pipeline.log
-rw-rw-r-- 1 1.1M Jun 24 17:07 sequencing_summary.txt
-rw-rw-r-- 1 248K Jun 24 17:07 sequencing_telemetry.js
drwxrwxr-x 1 4.0K Jun 24 16:57 workspace

```


#### configuration file
```
$ cat configuration.cfg
[pipeline]
basecall_type = linear
min_qscore_1d = 7.0
desc_file = /home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/albacore/data_versioned/layout_raw_basecall_1d.jsn

[data_trimmer]
ev_window = 20
ev_threshold = 5
min_events = 3
delta = 2
min_samples_out = 10000
trim_strategy = rna_tether
dmean_win_size = 400
dmean_threshold = 10
jump_threshold = 2
max_trimming = 0.5

[basecaller]
model = template_r9.4.1_70bps_5mer_rna_raw.jsn
min_events = 100
max_events = 10000
overlap = 50
min_quality = -100.0
min_prob = 1e-5
scaling_start = 0.5
scaling_end = 0.95
u_substitution = 1
reverse_direction = 1
homopolymer_correct = 0
model_path = /home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/albacore/data_versioned

[call_handler]
record_base = read
qscore_adjuster_slope = 1.2
qscore_adjuster_intercept = 0.8

[calib_detector]
method = minimap2_library
reference = /home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/albacore/data_versioned/yhr174w.mmidx
min_sequence_length = 1300
max_sequence_length = 1550
min_coverage = 0.6
reverse_direction = true

[barcode_detector]

[fastq]
identifier = {read_id}
header = {identifier} runid={run_id} read={read_number} ch={channel_id} start_time={start_time_utc}
header_with_barcoding = {identifier} runid={run_id} read={read_number} ch={channel_id} start_time={start_time_utc} barcode={barcode_id}
batch_file_name = fastq_runid_{run_id}_{batch_counter}.{extension}
single_file_name = {read_id}.{extension}
all_file_name = fastq_runid_{run_id}.{extension}

[fast5]
basecall_columns = mean,start,stdv,length,model_state,move,p_model_state,weights

[aligner]
method = 

```


#### summary
```
$ head  sequencing_summary.txt
filename	read_id	run_id	channel	start_time	duration	num_events	passes_filtering	template_start	num_events_template	template_duration	num_called_template	sequence_length_template	mean_qscore_template	strand_score_template	calibration_strand_genome_template	calibration_strand_identity_template	calibration_strand_accuracy_template	calibration_strand_speed_bps_template
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch101_read17369.fast5	0c3b5620-c861-4910-b361-305e34a84060	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	101	52235.74668	6.47676	1300	False	0.0	1300	6.47676	1300	172	6.755	-0.0012	filtered_out	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch101_read1336.fast5	34db20ce-74cd-435c-b442-49adb85a7ac0	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	101	4118.7241	14.61189	2253	True	3.39044	2253	11.22145	2253	696 7.372	-0.0006	filtered_out	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch102_read23458.fast5	3aac6679-e894-4600-8ba9-3d694a16d32c	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	102	60321.42131	9.001	1807	False	0.0	1807	9.001	1807	72	4.892	-0.001	filtered_out	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch101_read4018.fast5	3f92a2ce-2e32-4195-a14f-c5a49646f7fb	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	101	12362.74469	11.5747	1856	False	2.33167	1856	9.24303	1856	628	6.788	-0.0008	filtered_out	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch101_read3120.fast5	41a48e05-bbbb-41d6-9f26-c4d49473405f	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	101	9403.18293	7.28121	979	True	2.40139	979	4.87981	979	448	7.137	-0.0019	filtered_out	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch101_read18510.fast5	51ac3ca7-1adc-4ad8-8e69-c5552ab5ecc3	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	101	55338.48772	40.41069	7017	True	5.46248	7017	34.94821	7017	15478.668	-0.0002	*	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch101_read5491.fast5	5c3fe9d1-195b-474c-933b-135967f70763	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	101	17161.06308	22.65571	3767	True	3.89475	3767	18.76096	3767	14957.681	-0.0004	*	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch102_read2267.fast5	94a3beef-028b-4f44-81da-b43f5f9e47ce	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	102	4729.51826	15.09761	2017	True	5.05146	2017	10.04615	2017	500 8.228	-0.0001	filtered_out	-1.0	-1.0	0.0
shard_20180326_FAH61609_GA10000_sequencing_run_180326_ce_L1_BR1TR1_69868_ch101_read3126.fast5	99f44ecb-54d9-4225-8bdc-d60246114471	6f23fbc7b6dfc4f658a86a182c54d9eca8202cb5	101	9421.8496	6.71912	1349	False	0.0	1349	6.71912	1349	189	6.303	-0.0005	filtered_out	-1.0	-1.0	0.0

```


#### run
```
read_fast5_basecaller.py --input /home/wuzhikun/data/RNA/Caenorhabditis_elegans/experiments/nanopore_datasets/L1/bio1/tech1/data/fast5 --recursive --worker_threads 24 --flowcell FLO-MIN106 --kit SQK-RNA001 --save_path /home/wuzhikun/data/RNA/Caenorhabditis_elegans/fastq
```




