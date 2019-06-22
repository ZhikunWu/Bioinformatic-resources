### refGene
```
$ head  hg38_refGene.txt
1147	NR_045512	chr7	+	73683567	73698221	73698221	73698221	11	73683567,73683766,73686635,73686817,73686998,73692595,73693328,73693623,73693991,73697604,73697831,	73683673,73683804,73686731,73686900,73687095,73692646,73693414,73693669,73694050,73697694,73698221,	0	BUD23	unk	unk	-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
585	NR_024540	chr1	-	14361	29370	29370	29370	11	14361,14969,15795,16606,16857,17232,17605,17914,18267,24737,29320,	14829,15038,15947,16765,17055,17368,17742,18061,18366,24891,29370,	0	WASH7P	unk	unk	-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
932	NR_104645	chrX	+	45505387	45523644	45523644	45523644	3	45505387,45510496,45521607,	45505465,45510595,45523644,	0	LINC01204	unk	unk	-1,-1,-1,
1078	NR_104148	chr7	+	64666082	64687830	64687830	64687830	4	64666082,64669036,64679176,64684334,	64666285,64669178,64679336,64687830,	0	ZNF107	unk	unk	-1,-1,-1,-1,
678	NR_104179	chr19	+	12195014	12207576	12207576	12207576	2	12195014,12207331,12195143,12207576,	0	LOC100289333	unk	unk	-1,-1,
1267	NR_120406	chr11	-	89488852	89491565	89491565	89491565	3	89488852,89490457,89491189,	89488993,89490553,89491565,	0	NOX4	unk	unk	-1,-1,-1,
585	NR_026818	chr1	-	34610	36081	36081	36081	3	34610,35276,35720,	35174,35481,36081,	0 FAM138A	unk	unk	-1,-1,-1,
585	NR_026822	chr1	-	34610	36081	36081	36081	3	34610,35276,35720,	35174,35481,36081,	0 FAM138C	unk	unk	-1,-1,-1,
585	NM_001005484	chr1	+	69090	70008	69090	70008	1	69090,	70008,	0	OR4F5	cmpl	cmpl	0,
586	NR_039983	chr1	-	134772	140566	140566	140566	3	134772,139789,140074,	139696,139847,140566,	0 LOC729737	unk	unk	-1,-1,-1,

```

### knownGene
```
$ head   hg38_knownGene.txt
uc031tla.1	chr1	-	17368	17436	17368	17368	1	17368,	17436,		ENST00000619216.1
uc057aty.1	chr1	+	29553	31097	29553	29553	3	29553,30563,30975,	30039,30667,31097,		ENST00000473358.1
uc057atz.1	chr1	+	30266	31109	30266	30266	2	30266,30975,	30667,31109,		ENST00000469289.1
uc031tlb.1	chr1	+	30365	30503	30365	30365	1	30365,	30503,		ENST00000607096.1
uc001aak.4	chr1	-	34553	36081	34553	34553	3	34553,35276,35720,	35174,35481,36081,		ENST00000417324.1
uc057aua.1	chr1	-	35244	36073	35244	35244	2	35244,35720,	35481,36073,		ENST00000461467.1
uc001aal.1	chr1	+	69090	70008	69090	70008	1	69090,	70008,	Q8NH21	ENST00000335137.3
uc057aub.1	chr1	-	89294	120932	89294	89294	4	89294,92090,112699,120774,	91629,92240,112804,120932,ENST00000466430.5
uc057auc.1	chr1	-	89550	91105	89550	89550	2	89550,90286,	90050,91105,		ENST00000495576.1
uc057aud.1	chr1	-	92229	129217	92229	92229	4	92229,112699,120720,129054,	92240,112804,120932,129217ENST00000477740.5
```

### esp6500siv2_all

```
$ head  hg38_esp6500siv2_all.txt
1	69428	69428	T	G	0.0306	rs140739101
1	69476	69476	T	C	0.0002	rs148502021
1	69496	69496	G	A	0.0024	rs150690004
1	69511	69511	A	G	0.7598	rs75062661
1	69590	69590	T	A	0.0001	rs141776804
1	69594	69594	T	C	0.0002	rs144967600
1	69620	69621	TA	T	0.0003	.
1	69621	69621	A	-	0.0003	.
1	69761	69761	A	T	0.0925	rs200505207
1	802177	802177	T	TCC	0.0007	.

```


### cytoBand
```
$ head  hg38_cytoBand.txt
chr1	0	2300000	p36.33	gneg
chr1	2300000	5300000	p36.32	gpos25
chr1	5300000	7100000	p36.31	gneg
chr1	7100000	9100000	p36.23	gpos25
chr1	9100000	12500000	p36.22	gneg
chr1	12500000	15900000	p36.21	gpos50
chr1	15900000	20100000	p36.13	gneg
chr1	20100000	23600000	p36.12	gpos25
chr1	23600000	27600000	p36.11	gneg
chr1	27600000	29900000	p35.3	gpos25

```


### clinvar
```
$ head hg38_clinvar_20180603.txt
#Chr	Start	End	Ref	Alt	CLNALLELEID	CLNDN	CLNDISDB	CLNREVSTAT	CLNSIG
1	1	1	0	0	104943	not_provided	MedGen:CN517202	no_assertion_provided	not_provided
1	1	1	0	0	106000	not_provided	MedGen:CN517202	no_assertion_provided	not_provided
1	1	1	0	0	139985	Primary_familial_hypertrophic_cardiomyopathy|Dilated_cardiomyopathy_1AA|not_specified	MedGen:C0949658\x2cOrphanet:ORPHA155\x2cSNOMED_CT:83978005|MedGen:C2677338\x2cOMIM:612158|MedGen:CN169374	criteria_provided\x2c_multiple_submitters\x2c_no_conflicts	Benign
1	1	1	0	0	139986	Primary_familial_hypertrophic_cardiomyopathy|Dilated_cardiomyopathy_1AA|not_specified	MedGen:C0949658\x2cOrphanet:ORPHA155\x2cSNOMED_CT:83978005|MedGen:C2677338\x2cOMIM:612158|MedGen:CN169374	criteria_provided\x2c_multiple_submitters\x2c_no_conflicts	Benign
1	1	1	0	0	141597	not_specified	MedGen:CN169374	criteria_provided\x2c_multiple_submitters\x2c_no_conflicts	Benign
1	1	1	0	0	141598	not_specified	MedGen:CN169374	criteria_provided\x2c_multiple_submitters\x2c_no_conflicts	Benign
1	1	1	0	0	141601	not_specified	MedGen:CN169374	criteria_provided\x2c_multiple_submitters\x2c_no_conflicts	Benign
1	1	1	0	0	142232	Cryopyrin_associated_periodic_syndrome|not_specified	MedGen:C2316212\x2cOrphanet:ORPHA208650\x2cSNOMED_CT:430079001|MedGen:CN169374	criteria_provided\x2c_multiple_submitters\x2c_no_conflicts	Benign
1	1	1	0	0	172894	not_specified	MedGen:CN169374	criteria_provided\x2c_single_submitter	Benign

```


### cosmic
```
$ head hg38_cosmic70.txt
1	69345	69345	C	A	ID=COSM911918;OCCURENCE=1(endometrium)
1	69523	69523	G	T	ID=COSM426644;OCCURENCE=1(breast)
1	69538	69538	G	A	ID=COSM75742;OCCURENCE=1(ovary)
1	69539	69539	T	C	ID=COSM1343690;OCCURENCE=1(large_intestine)
1	69540	69540	G	T	ID=COSM1560546;OCCURENCE=1(large_intestine)
1	69569	69569	T	C	ID=COSM1599955;OCCURENCE=2(central_nervous_system)
1	69591	69591	C	T	ID=COSM3419425;OCCURENCE=1(large_intestine)
1	629946	629946	G	A	ID=COSN228104;OCCURENCE=1(skin)
1	632106	632106	T	C	ID=COSN202132,COSN204014;OCCURENCE=2(large_intestine)
1	925922	925922	G	A	ID=COSN213381;OCCURENCE=1(breast)
```


### exac
```
$ head hg38_exac03.txt
#Chr	Start	End	Ref	Alt	ExAC_ALL	ExAC_AFR	ExAC_AMR	ExAC_EAS	ExAC_FIN	ExAC_NFE  ExAC_OTH	ExAC_SAS
1	13372	13372	G	C	0.0002	0	0	0	0	0	0	0.0004
1	13380	13380	C	G	0.0033	0.0381	0.0096	0	0	0	0	0
1	13382	13382	C	G	0.0002	0	0	0	0	0	0	0.0003
1	13402	13402	G	C	0	0	0	0	.	0	0	0
1	13404	13404	G	A	0	0	0	0	.	0	0	0
1	13404	13404	G	T	0.0007	0	0	0	.	0	0	0.0012
1	13417	13417	C	CGAGA	0.1743	0.0333	0.2	0.0758	0	0.2	0.0714	0.2052
1	13417	13417	-	GAGA	0.1743	0.0333	0.2	0.0758	0	0.2	0.0714	0.2052
1	13418	13418	G	A	0	0	0	0	0	0	0	0

```


```
perl /home/wuzhikun/software/annovar/table_annovar.pl /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.vcf /home/wuzhikun/database/Annovar/hg38  --buildver hg38 --outfile /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9 --remove --protocol "GeneName" --operation "r"  --nastring .
```

```
Error: the required database file /home/wuzhikun/database/Annovar/hg38_GeneName.txt does not exist.

```


```
$ perl /home/wuzhikun/software/annovar/table_annovar.pl /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.vcf /home/wuzhikun/database/Annovar/hg38   --buildver hg38 --outfile /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9 --remove --protocol "cytoband,exac03,clinvar_20180603" --operation "f,f,f"   --nastring . 
-----------------------------------------------------------------
NOTICE: Processing operation=f protocol=cytoband

NOTICE: Running system command <annotate_variation.pl -filter -dbtype cytoband -buildver hg38 -outfile /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9 /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.vcf /home/wuzhikun/database/Annovar/hg38>
NOTICE: the --dbtype cytoband is assumed to be in generic ANNOVAR database format
NOTICE: Variants matching filtering criteria are written to /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.hg38_cytoBand_dropped, other variants are written to /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.hg38_cytoBand_filtered
NOTICE: Variants with invalid input format were written to /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.invalid_input
-----------------------------------------------------------------
NOTICE: Multianno output file is written to /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.hg38_multianno.txt

```

output files:
```
-rw-rw-r-- 1 5.6M Mar 23 17:21 M625_9.hg38_multianno.txt
-rw-rw-r-- 1  81M Mar 23 17:21 M625_9.invalid_input

```

```
$ grep -v '^#' /home/wuzhikun/Project/Illumina_Trio/Trio/M625_9.hg38_multianno.txt | head
Chr	Start	End	Ref	Alt	cytoband
9	10237	.	CCCCTAACCCCTAACCCTAA	C	.
9	10340	.	TACCCTA	T	.
9	10392	.	GAACCCGAACCCGAACCCT	G	.
9	10435	.	C	A	.
9	10712	.	A	G	.
9	10869	.	C	G	.
9	10935	.	C	G	.
9	10960	.	A	C	.
9	10968	.	G	A	.

```



### Annovar test

```
perl /home/wuzhikun/software/annovar/table_annovar.pl test/example.simple_region /home/wuzhikun/database/Annovar/hg38 --buildver hg38 --outfile test/example.simple_region_anno --remove --protocol refGene,cytoband,exac03,clinvar_20180603,cosmic70 --operation  gx,r,f,f,f --nastring .
```



```
$ perl /home/wuzhikun/software/annovar/convert2annovar.pl --help
Usage:
     convert2annovar.pl [arguments] <variantfile>

     Optional arguments:
            -h, --help                      print help message
            -m, --man                       print complete documentation
            -v, --verbose                   use verbose output
                --format <string>           input format (default: pileup)
                --includeinfo               include supporting information in output
                --outfile <file>            output file name (default: STDOUT)
                --snpqual <float>           quality score threshold in pileup file (default: 20)
                --snppvalue <float>         SNP P-value threshold in GFF3-SOLiD file (default: 1)
                --coverage <int>            read coverage threshold in pileup file (default: 0)
                --maxcoverage <int>         maximum coverage threshold (default: none)
                --chr <string>              specify the chromosome (for CASAVA format)
                --chrmt <string>            chr identifier for mitochondria (default: M)
                --fraction <float>          minimum allelic fraction to claim a mutation (for pileup format)
                --altcov <int>              alternative allele coverage threshold (for pileup format)
                --allelicfrac               print out allelic fraction rather than het/hom status (for pileup format)
                --species <string>          if human, convert chr23/24/25 to X/Y/M (for gff3-solid format)
                --filter <string>           output variants with this filter (case insensitive, for vcf4 format)
                --confraction <float>       minimal fraction for two indel calls as a 0-1 value (for vcf4old format)
                --allallele                 print all alleles rather than first one (for vcf4old format)
                --withzyg                   print zygosity/coverage/quality when -includeinfo is used (for vcf4 format)
                --comment                   keep comment line in output (for vcf4 format)
                --allsample                 process all samples in file with separate output files (for vcf4 format)
                --genoqual <float>          genotype quality score threshold (for vcf4 format)
                --varqual <float>           variant quality score threshold (for vcf4 format)
                --dbsnpfile <file>          dbSNP file in UCSC format (for rsid format)
                --withfreq                  for --allsample, print frequency information instead (for vcf4 format)
                --withfilter                print filter information in output (for vcf4 format)
                --seqdir <string>           directory with FASTA sequences (for region format)
                --inssize <int>             insertion size (for region format)
                --delsize <int>             deletion size (for region format)
                --subsize <int>             substitution size (default: 1, for region format)
                --genefile <file>           specify the gene file from UCSC (for transcript format)
                --splicing_threshold <int>  the splicing threshold (for transcript format)
                --context <int>             print context nucleotide for indels (for casava format)
                --avsnpfile <file>          specify the avSNP file (for rsid format)
                --keepindelref              keep Ref/Alt alleles for indels (for vcf4 format)

     Function: convert variant call file generated from various software programs 
     into ANNOVAR input format
 
     Example: convert2annovar.pl -format pileup -outfile variant.query variant.pileup
              convert2annovar.pl -format cg -outfile variant.query variant.cg
              convert2annovar.pl -format cgmastervar variant.masterVar.txt
              convert2annovar.pl -format gff3-solid -outfile variant.query variant.snp.gff
              convert2annovar.pl -format soap variant.snp > variant.avinput
              convert2annovar.pl -format maq variant.snp > variant.avinput
              convert2annovar.pl -format casava -chr 1 variant.snp > variant.avinput
              convert2annovar.pl -format vcf4 variantfile > variant.avinput
              convert2annovar.pl -format vcf4 -filter pass variantfile -allsample -outfile variant
              convert2annovar.pl -format vcf4old input.vcf > output.avinput
              convert2annovar.pl -format rsid snplist.txt -dbsnpfile snp138.txt > output.avinput
              convert2annovar.pl -format region -seqdir humandb/hg19_seq/ chr1:2000001-2000003 -inssize 1 -delsize 2
              convert2annovar.pl -format transcript NM_022162 -gene humandb/hg19_refGene.txt -seqdir humandb/hg19_seq/

     Version: $Date: 2018-04-16 00:48:00 -0400 (Mon, 16 Apr 2018) $

```


```
~/biosoft/ANNOVAR/annovar/convert2annovar.pl -format vcf4old H3F3A.vcf >H3F3A.annovar 2>/dev/null

~/biosoft/ANNOVAR/annovar/annotate_variation.pl -buildver hg38 --geneanno --outfile H3F3A.anno H3F3A.annovar ~/biosoft/ANNOVAR/annovar/humandb/

~/biosoft/ANNOVAR/annovar/annotate_variation.pl -buildver hg38 --dbtype knownGene --geneanno --outfile H3F3A.anno H3F3A.annovar ~/biosoft/ANNOVAR/annovar/humandb/
```

```
dir=/home/jianmingzeng/biosoft/ANNOVAR/annovar
db=$dir/humandb/ 
ls $db 
perl $dir/table_annovar.pl \
-buildver hg38 \
for_annovar.input $db \
-out test \
-remove -protocol \
refGene,clinvar_20180603 \
-operation g,f \
-nastring NA 
## 这里只做两个数据库注释，举例说明。
```