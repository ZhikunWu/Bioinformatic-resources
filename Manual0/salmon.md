## salmon


### install salmon
```bash
$ conda install -c bioconda salmon
```
or
```bash
$ wget https://github.com/COMBINE-lab/salmon/releases/download/v0.7.2/Salmon-0.7.2_linux_x86_64.tar.gz
```

#### run salmon
Grab the nucleotide (*ffn) predicted protein regions from Prokka and link them here
```
$ mkdir salmon
$ cd salmon/
$ ln -s /home/wzk/metagenome_data/prokka/Meta/Meta.ffn Meta.ffn
$ ln -s /home/wzk/metagenome_data/prokka/Meta/Meta.gff Meta.gff
$ ln -s /home/wzk/metagenome_data/prokka/Meta/Meta.tsv Meta.tsv
```

Create the salmon index:
```bash
$ salmon index -t Meta.ffn -i transcript_index --type quasi -k 31

```

output files
```
$ tree transcript_index/
transcript_index/
├── hash.bin
├── header.json
├── indexing.log
├── quasi_index.log
├── refInfo.json
├── rsd.bin
├── sa.bin
├── txpInfo.bin
└── versionInfo.json
```

grab the fastq files
```bash
$ ln -s /home/wzk/metagenome_data/raw/HMP_GUT_SRS052697.25M.1.fastq.gz HMP_GUT_SRS052697.25M.1.fastq.gz

$ ln -s /home/wzk/metagenome_data/raw/HMP_GUT_SRS052697.25M.2.fastq.gz HMP_GUT_SRS052697.25M.2.fastq.gz

$ ln -s /home/wzk/metagenome_data/raw/HMP_MOCK_SRR2726667_8.25M.1.fastq.gz HMP_MOCK_SRR2726667_8.25M.1.fastq.gz

$ ln -s /home/wzk/metagenome_data/raw/HMP_MOCK_SRR2726667_8.25M.2.fastq.gz HMP_MOCK_SRR2726667_8.25M.2.fastq.gz
```

quantify our reads against this reference
```bash
$ salmon quant -i transcript_index --libType IU -1 HMP_GUT_SRS052697.25M.1.fastq.gz -2 HMP_GUT_SRS052697.25M.2.fastq.gz -o HMP_GUT_SRS052697.25M

$ salmon quant -i transcript_index --libType IU -1 HMP_MOCK_SRR2726667_8.25M.1.fastq.gz -2 HMP_MOCK_SRR2726667_8.25M.2.fastq.gz -o HMP_MOCK_SRR2726667_8.25M
```

output files
```bash
$ tree HMP_GUT_SRS052697.25M
HMP_GUT_SRS052697.25M
├── aux_info
│   ├── ambig_info.tsv
│   ├── expected_bias.gz
│   ├── fld.gz
│   ├── meta_info.json
│   ├── observed_bias_3p.gz
│   └── observed_bias.gz
├── cmd_info.json
├── lib_format_counts.json
├── libParams
│   └── flenDist.txt
├── logs
│   └── salmon_quant.log
└── quant.sf

```

### Working with count data
Now, the quant.sf files actually contain the relevant information about expression – take a look:
```
$ head HMP_GUT_SRS052697.25M/quant.sf 
Name    Length  EffectiveLength TPM NumReads
LHAAMGIF_00001  174 40.746  0   0
LHAAMGIF_00002  216 59.4207 0   0
LHAAMGIF_00003  381 179.117 0   0
LHAAMGIF_00004  375 173.72  0   0
LHAAMGIF_00005  207 54.4501 0   0
LHAAMGIF_00006  405 201.454 0   0
LHAAMGIF_00007  531 324.636 0   0
LHAAMGIF_00008  207 54.4501 0   0
LHAAMGIF_00009  117 22.6463 0   0
```
The first column contains the transcript names, and the fourth column is what we will want down the road - the normalized counts (TPM). However, they’re not in a convenient location / format for use; let’s fix that.


### download the gather-counts.py script:
```bash
$ curl -L -O https://raw.githubusercontent.com/ngs-docs/2016-metagenomics-sio/master/gather-counts.py
```

```bash
$ python /home/wzk/anaconda3/envs/qiime/bin/gather-counts.py
```

output files:
```
HMP_GUT_SRS052697.25M.counts
HMP_MOCK_SRR2726667_8.25M.counts
```

details for output:
```
$ head HMP_GUT_SRS052697.25M.counts
transcript  count
LHAAMGIF_00001  0.0
LHAAMGIF_00002  0.0
LHAAMGIF_00003  0.0
LHAAMGIF_00004  0.0
LHAAMGIF_00005  0.0
LHAAMGIF_00006  0.0
LHAAMGIF_00007  0.0
LHAAMGIF_00008  0.0
LHAAMGIF_00009  0.0
```
This will give you a bunch of .counts files, which are processed from the quant.sf files and named for the directory from which they emanate

### merge them to one file:
```
$ sed -e 's/count/HMP_GUT_SRS052697.25M/g' HMP_GUT_SRS052697.25M.counts > temp1
$ sed -e 's/count/HMP_MOCK_SRR2726667_8.25M/g' HMP_MOCK_SRR2726667_8.25M.counts  > temp2
$ paste temp1 temp2 | cut -f 1,2,4 > Combined-counts.tab
```
