## [cutesv](https://github.com/tjiangHIT/cuteSV)

Long read based human genomic structural variation detection with cuteSV


### install cuteSV
```
conda install -c bioconda cutesv
```

or

```
git clone https://github.com/tjiangHIT/cuteSV.git && cd cuteSV/ && pip install .
```


### cuteSV parameters
```
$ cuteSV --help
usage: cuteSV [-h] [-t THREADS] [-b BATCHES] [-S SAMPLE] [-g GENOTYPE]
              [-p MAX_SPLIT_PARTS] [-q MIN_MAPQ] [-r MIN_READ_LEN]
              [-s MIN_SUPPORT] [-l MIN_SIZE] [-L MIN_SIGLENGTH]
              [--max_cluster_bias_INS MAX_CLUSTER_BIAS_INS]
              [--diff_ratio_merging_INS DIFF_RATIO_MERGING_INS]
              [--diff_ratio_filtering_INS DIFF_RATIO_FILTERING_INS]
              [--max_cluster_bias_DEL MAX_CLUSTER_BIAS_DEL]
              [--diff_ratio_merging_DEL DIFF_RATIO_MERGING_DEL]
              [--diff_ratio_filtering_DEL DIFF_RATIO_FILTERING_DEL]
              [--max_cluster_bias_INV MAX_CLUSTER_BIAS_INV]
              [--max_cluster_bias_DUP MAX_CLUSTER_BIAS_DUP]
              [--max_cluster_bias_TRA MAX_CLUSTER_BIAS_TRA]
              [--diff_ratio_filtering_TRA DIFF_RATIO_FILTERING_TRA]
              [BAM] output temp_dir

	Long read based fast and accurate SV detection with cuteSV.
	
	Current version: v1.0.1
	Author: Tao Jiang
	Contact: tjiang@hit.edu.cn

	Suggestions:

	For PacBio CLR data:
		--max_cluster_bias_INS		100
		--diff_ratio_merging_INS	0.2
		--diff_ratio_filtering_INS	0.6
		--diff_ratio_filtering_DEL	0.7
	For PacBio CCS(HIFI) data:
		--max_cluster_bias_INS		200
		--diff_ratio_merging_INS	0.65
		--diff_ratio_filtering_INS	0.65
		--diff_ratio_filtering_DEL	0.35

	

positional arguments:
  [BAM]                 Sorted .bam file form NGMLR or Minimap2.
  output                the path of [Output]
  temp_dir              temporary directory to use for distributed jobs

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        Number of threads to use.[16]
  -b BATCHES, --batches BATCHES
                        A batches of reads to load.[10000000]
  -S SAMPLE, --sample SAMPLE
                        Sample name/id
  -g GENOTYPE, --genotype GENOTYPE
                        Enable generate genotype (True/False).[False]

Collection of SV signatures:
  -p MAX_SPLIT_PARTS, --max_split_parts MAX_SPLIT_PARTS
                        Maximum number of split segments a read may be aligned
                        before it is ignored.[7]
  -q MIN_MAPQ, --min_mapq MIN_MAPQ
                        Minimum mapping quality value of alignment to be taken
                        into account.[20]
  -r MIN_READ_LEN, --min_read_len MIN_READ_LEN
                        Ignores reads that only report alignments with not
                        longer then bp.[500]

Generation of SV clusters:
  -s MIN_SUPPORT, --min_support MIN_SUPPORT
                        Minimum number of reads that support a SV to be
                        reported.[3]
  -l MIN_SIZE, --min_size MIN_SIZE
                        Minimum size of SV to be reported.[30]
  -L MIN_SIGLENGTH, --min_siglength MIN_SIGLENGTH
                        Minimum length of SV signal to be extracted.[10]

Advanced:
  --max_cluster_bias_INS MAX_CLUSTER_BIAS_INS
                        Maximum distance to cluster read together for
                        insertion.[100]
  --diff_ratio_merging_INS DIFF_RATIO_MERGING_INS
                        Do not merge breakpoints with basepair identity more
                        than [0.2] for insertion.
  --diff_ratio_filtering_INS DIFF_RATIO_FILTERING_INS
                        Filter breakpoints with basepair identity less than
                        [0.6] for insertion.
  --max_cluster_bias_DEL MAX_CLUSTER_BIAS_DEL
                        Maximum distance to cluster read together for
                        deletion.[200]
  --diff_ratio_merging_DEL DIFF_RATIO_MERGING_DEL
                        Do not merge breakpoints with basepair identity more
                        than [0.3] for deletion.
  --diff_ratio_filtering_DEL DIFF_RATIO_FILTERING_DEL
                        Filter breakpoints with basepair identity less than
                        [0.7] for deletion.
  --max_cluster_bias_INV MAX_CLUSTER_BIAS_INV
                        Maximum distance to cluster read together for
                        inversion.[500]
  --max_cluster_bias_DUP MAX_CLUSTER_BIAS_DUP
                        Maximum distance to cluster read together for
                        duplication.[500]
  --max_cluster_bias_TRA MAX_CLUSTER_BIAS_TRA
                        Maximum distance to cluster read together for
                        translocation.[50]
  --diff_ratio_filtering_TRA DIFF_RATIO_FILTERING_TRA
                        Filter breakpoints with basepair identity less than


```



```
Parameter	Description	Default
--threads	Number of threads to use.	16
--batches	A batches of reads to load.	10,000,000
--sample	Sample name/id	NULL
--genotype	Optional genotyping (True/False).	False
--max_split_parts	Maximum number of split segments a read may be aligned before it is ignored.	7
--min_mapq	Minimum mapping quality value of alignment to be taken into account.	20
--min_read_len	Ignores reads that only report alignments with not longer then bp.	500
--min_support	Minimum number of reads that support a SV to be reported.	3
--min_length	Minimum length of SV to be reported.	30
--max_cluster_bias_INS	Maximum distance to cluster read together for insertion.	100
--diff_ratio_merging_INS	Do not merge breakpoints with basepair identity more than the ratio of default for insertion.	0.2
--diff_ratio_filtering_INS	Filter breakpoints with basepair identity less than the ratio of default for insertion.	0.6
--max_cluster_bias_DEL	Maximum distance to cluster read together for deletion.	200
--diff_ratio_merging_DEL	Do not merge breakpoints with basepair identity more than the ratio of default for deletion.	0.3
--diff_ratio_filtering_DEL	Filter breakpoints with basepair identity less than the ratio of default for deletion.	0.7
--max_cluster_bias_INV	Maximum distance to cluster read together for inversion.	500
--max_cluster_bias_DUP	Maximum distance to cluster read together for duplication.	500
--max_cluster_bias_TRA	Maximum distance to cluster read together for translocation.	50
--diff_ratio_filtering_TRA	Filter breakpoints with basepair identity less than the ratio of default for translocation.	0.6
```


### run cuteSV
```
$ mkdir /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M671-1_temp

$ cuteSV --threads 20 --sample M671-1 --genotype True  --max_split_parts 7 --min_size 50 --min_support 2  M671-1.bam /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M671-1_cuteSV  /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M671-1_temp

2019-10-19 10:28:46,290 [INFO] Running /home/wuzhikun/anaconda3/envs/NanoSV/bin/cuteSV --threads 20 --sample M671-1 --genotype True --max_split_parts 7 --min_size 50 --min_support 2 M671-1.bam /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M671-1_cuteSV /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M671-1_temp
2019-10-19 10:28:46,387 [INFO] The total number of chromsomes: 194


2019-10-19 10:32:03,761 [INFO] Finished Y:50000000-57227415.
2019-10-19 10:32:04,482 [INFO] Finished KI270438.1:0-112505.
2019-10-19 10:32:04,638 [INFO] Rebuilding signatures of structural variants.
2019-10-19 10:32:12,651 [INFO] Clustering structural variants.
2019-10-19 10:33:34,700 [INFO] Writing into disk.
2019-10-19 10:49:44,656 [INFO] Cleaning temporary files.
2019-10-19 10:49:46,890 [INFO] Finished in 1260.60 seconds.

```


### temp signatures

```
$ head  M671-1_temp/signatures/_12_100000000_110000000.bed
DEL	12	100040910	64	66359712-c8cc-43ae-8daa-f3e63c838068
DEL	12	100069434	53	45f970aa-d2a5-4667-9a54-3f9997ef6149
DEL	12	100045677	1136	465378e9-71ce-42ff-9373-f19f1c7d2873
DEL	12	100121847	85	54a79dbd-c858-4eb3-b857-dfd4494e91e8
DEL	12	100173466	55	688f139c-ada8-4e16-aacc-563e247b7484
DEL	12	100217932	72	7330618a-2c8f-4b8b-b13f-301cd0a34dae
DEL	12	100311733	73	ef79db7e-cb75-4da1-b5e2-ba9cead1b091
DEL	12	100379084	66	83c9d2d7-09d9-44ee-a9c9-f12b4412db83
DEL	12	100382197	58	83c9d2d7-09d9-44ee-a9c9-f12b4412db83
DEL	12	100573123	983	821653fa-2eaf-426a-aa49-1754658cb28d


INS     12      101210373       73      6f46a456-88c0-443d-8e43-f8d83769eedd
INS     12      101248344       79      aa664402-3878-4ff7-9e70-31f8ca08a183
INS     12      101360218       232     cc63b0c9-af62-4689-b771-0520b299ebde

INV     12      103605031       103603867       36653430-3de0-4927-81e2-565108603edc
INV     12      103615438       103621364       fdfb253f-a365-49c5-8d05-30cda31d65b9
INV     12      103615066       103609666       fdfb253f-a365-49c5-8d05-30cda31d65b9

TRA     12      C       108129589       19      25388721        3d8e1007-e694-47a4-afcc-b5325a1e1830
TRA     12      D       108183275       8       140150626       3c0a2fe0-526b-4020-9701-30455e80160c
TRA     12      C       108257927       4       171693903       1eb27d41-b20a-448f-b241-79fc4be8b674
TRA     12      B       108438074       14      102457922       80c46f42-2a11-4050-9ab4-6a0c99f27f91

DUP	12	95148485	103507279	957022d9-bb66-4afb-8509-47bafb91cab1
DUP	12	103686651	103686999	b18628c5-4583-4baf-83a8-b5393aad6b5a
DUP	12	104284979	104286714	23ff0405-0dba-4641-b7f7-ae68707e54cf
DUP	12	104304658	131995181	89a0c92a-f34d-4cf0-a132-02703fa583fa
DUP	12	67661451	104397680	2d67e697-cdea-4c58-9660-12fe87416f22
DUP	12	104945817	104948597	e0774945-c3ab-4d5a-b900-e6379064f5bf
DUP	12	28004080	104989990	ff6e5f56-9d43-491e-81d1-82162cb91366
```


#### sorted signinatures
```
$ head M671-1_temp/DEL.sigs 
DEL	1	58220	137	f5c56809-4875-4fe2-87f7-1f45b08f10c6
DEL	1	83807	62	25c1d619-8ec6-45cb-ace3-df2febb9935b
DEL	1	90047	236	2f99665d-2243-4145-b453-5f71561551f6
DEL	1	90175	232	6b09dad6-2788-46ff-ab85-1152e598b8b5
DEL	1	103672	374	2fbcb7dd-6cf6-43cc-8f7f-c72cc79705b1
DEL	1	115292	80	7f3b1f9d-5840-4750-ab68-96303e488b61
DEL	1	128054	68	6c7b29c5-e226-48ad-932b-14aa9588faf4
DEL	1	173015	54	c275c31a-82c8-40e4-8a8a-7f5f282b29ed
DEL	1	180106	152	e17df4f9-41ac-44c7-a9ad-15ff57e38b15
DEL	1	180176	208	bac7b9c0-328b-4c3e-b083-21893bbf6845
```

```
TRA	1	A	416723	10	99868675	205ccbde-0e17-4fe1-ab5f-b13a0be0461d
TRA	1	A	2436604	10	102995139	c7481882-1502-499f-97df-ffb5a4350494
TRA	1	A	6757645	10	22958816	4173267b-1683-45a3-ae65-2d09f8532f22
TRA	1	A	9729270	10	115918966	28e5ce02-4dca-4c1f-afdf-2935e0dfad53
TRA	1	A	13445315	10	46526486	3f0cadf6-358e-454a-8a3e-b322994b0307
TRA	1	A	13830490	10	98555690	1c897407-e2d9-40ca-a25b-6bae1fe8d126
TRA	1	A	13830490	10	98555692	4e968538-bc87-40a7-bdf0-a98297bc2fb1
TRA	1	A	16635337	10	114620416	9dbb4ca5-5f2c-463c-953a-9862793a89da
TRA	1	A	18233479	10	78805142	51d4b684-7fe9-4997-a469-6166bb9e5783
TRA	1	A	18860842	10	48030151	bf591de7-124f-4a32-afb1-2e11b8ba5ab6

```


### out VCF file

```
$ grep -cv '^#' M671-1_cuteSV
29074

```


```
1       727193  cuteSV.INS.15   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=90;END=727194;BREAKPOINT_STD=0;SVLEN_STD=0;RE=2        GT:DR:DV        0/0:45:2
1       748220  cuteSV.INS.16   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=309;END=748221;BREAKPOINT_STD=0;SVLEN_STD=0;RE=6       GT:DR:DV        0/0:98:6
1       788748  cuteSV.DUP.0    N       <DUP>   .       PASS    PRECISE;SVTYPE=DUP;SVLEN=2923;END=791671;BREAKPOINT_STD=0;SVLEN_STD=0;RE=2      GT:DR:DV        0/0:13:2
1       820881  cuteSV.INS.17   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=240;END=820882;BREAKPOINT_STD=0;SVLEN_STD=0;RE=17      GT:DR:DV        1/1:0:17
1       866619  cuteSV.INS.18   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=141;END=866620;BREAKPOINT_STD=0;SVLEN_STD=0;RE=2       GT:DR:DV        0/0:15:2
1       866691  cuteSV.INS.19   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=64;END=866692;BREAKPOINT_STD=0;SVLEN_STD=0;RE=4        GT:DR:DV        0/0:12:4
1       866949  cuteSV.INS.20   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=90;END=866950;BREAKPOINT_STD=0;SVLEN_STD=0;RE=6        GT:DR:DV        0/1:11:6
1       873128  cuteSV.BND.5    N       N[18:9936654[   .       PASS    PRECISE;SVTYPE=BND;CHR2=18;END=9936654;RE=2     GT:DR:DV        0/0:18:2
1       875984  cuteSV.INS.21   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=1334;END=875985;BREAKPOINT_STD=0;SVLEN_STD=0;RE=4      GT:DR:DV        0/0:20:4
1       882644  cuteSV.DEL.4    N       <DEL>   .       PASS    PRECISE;SVTYPE=DEL;SVLEN=-86;END=882730;BREAKPOINT_STD=0;SVLEN_STD=0;RE=18      GT:DR:DV        0/1:24:18
1       883233  cuteSV.BND.6    N       N]22:11309631]  .       PASS    PRECISE;SVTYPE=BND;CHR2=22;END=11309631;RE=2    GT:DR:DV        0/0:40:2
1       883237  cuteSV.BND.7    N       N]20:29789162]  .       PASS    PRECISE;SVTYPE=BND;CHR2=20;END=29789162;RE=3    GT:DR:DV        0/0:38:3
1       883242  cuteSV.BND.8    N       N]20:29351525]  .       PASS    PRECISE;SVTYPE=BND;CHR2=20;END=29351525;RE=5    GT:DR:DV        0/0:33:5
1       904550  cuteSV.INS.22   N       <INS>   .       PASS    PRECISE;SVTYPE=INS;SVLEN=63;END=904551;BREAKPOINT_STD=0;SVLEN_STD=0;RE=9        GT:DR:DV   
```

