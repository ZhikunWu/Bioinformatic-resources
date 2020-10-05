---
output:
  kctemp2::kc_render:
    before_parts: [1.Info]
---


```{r echo=FALSE, warning=FALSE,message=FALSE}
library(kctemp2)
```


#合同内容

`r contract_tb("edit/contract.yaml")`

<!-- <br>
**物种信息**
<br> -->


<!--`r readtb('edit/species.xls',shape='small')`-->

<br>
**建库类型及测序**
<br>

`r readtb('edit/lib_info.xls',shape='big')`

<br>
**服务内容**
<br>

`r list_vector("service_content", file="edit/contract.yaml")`

# 分析流程
首先对高通量测序的原始下机数据根据reads中碱基质量进行检测，去除reads两端的测序接头和低质量序列。获得高质量序列的reads后，根据UID序列对reads进行聚类，去除重复的reads（PCR过程中产生）。然后合并双末端（pair-end）reads得到一致性序列。同时我们根据SILVA数据库中注释到种的16S rDNA序列，并提取NCBI细菌基因组中的16S rDNA序列构建数据库。我们将一致性序列比对到该数据库，得到其OTU及其对应的菌种，同时计算其丰度。
我们根据OTU在不同样本中的丰度分布，评估每个样本的多样性水平。随后，对各样本（组）在不同分类水平的具体组成进行分析（并检验组间是否具有统计学差异）。在上述分析结果的基础上，通过多种多变量统计学分析工具，进一步衡量不同样本（组）间的群落结构差异及与差异相关的OTU，构建丰度分布高度相关的OTU关联网络。

`r single_fig("reserved/16SrDNA_workflow.svg", shape='big',title="16S rDNA流程")`


# 数据质控
## 数据预处理及分析



数据质控是指对高通量测序产生的海量数据质量进行评估，筛选掉无用数据，保留高质量数据，为后续转录组拼接及相关生物信息分析提供良好的基础。一般来说，测序质量越高，后续数据分析质量也越高，分析结果也更加精确，详实。


将Illumina Hiseq测序得到的原始图像数据经过Base Calling转化为序列数据，即FASTQ格式，得到最原始的测序数据文件。FASTQ格式文件可记录所测读段（read）的碱基及其质量分数。FASTQ格式以测序读段为单位进行存储，每条读段占4行，其中第一行和第三行由文件识别标志（sequence identifiers）和读段名（ID）组成（第一行以“@”开头而第三行以“+”开头；第三行中ID可以省略，但“+”不能省略），第二行为碱基序列，第四行为对应位置碱基的测序质量分数。


`r sys_fig('reserved/fastq_fig.png', title='FASTQ格式文件说明', shape='big')`


Read的质量分数以不同的字符来表示，其中每个字符对应的ASCII值减去33，即为对应的测序质量值。一般地，碱基质量从0-40，即对应的ASCII码为从“！”（0+33）到“I”(40+33）。如果测序错误率用E（%）表示，Illunima测序平台的碱基质量值用Q表示，则有下列关系：$Q=-10log_{10}(E)$。


`r readtb('reserved/E_Q_match.xls', title='测序错误率与测序质量值简明对应关系', shape='small')`



测序Reads的错误率会随着测序的进行而升高，是由测序过程中化学试剂的消耗造成，这是Illumina高通量测序平台通有的特征。

##原始数据质控

转录组测序项目在Illumina测序平台上完成，构建Illumina PE文库（~300bp）进行测序，对获得的测序数据进行质量控制，之后利用生物信息学手段对转录组数据进行分析。

Illumina测序属于第二代测序技术，单次运行能产生数十亿级的reads，如此海量的数据无法逐个展示每条Reads的质量情况；生物信息分析运用统计学的方法，对所有测序Reads的每个circle进行碱基分布和质量波动的统计，可以从宏观上直观地反映出样本的测序质量和文库构建质量。

转录组测序一般为双端测序（paired-end），简称PE测序，是针对建库产生的片段（fragments）从5’和3’端两端分别测序，产生的序列为paired-end reads，分别为Read 1和Read 2。

为了获知测序质量的高低，在测序数据下机后必须对测序数据进行质控,质控内容包括碱基质量分布、碱基平衡性分析和重复序列水平等方面。



###碱基质量分布

测序数据下机后，获得每个样品的原始测序序列，我们称为raw data或raw reads，以FASTQ（简写为fq）文件格式存储。对raw data进行质量评估（软件：FastQC），FastQC是一款数据质量可视化软件，其旨在提供一种简单的方式来评估数据质量来指导下游分析是否继续或如何进行。


`r fig_box('../result/qualityControl/raw',"per_base_quality.png", title='Raw Reads碱基质量分布', fig_name='', shape='QC', name_layer=2)`

`r notes(c("以盒形图的方式给出序列中每个位点对应的碱基质量分布的结果。","X轴是read中的碱基位置（1-150），Y轴是碱基质量；盒形图中间的红线表示中位数（median value）；黄色部分代表四分位距（25-75%）；上下分割线代表90%和10%的上下临界值；蓝色的线代表碱基质量的平均值。","碱基质量（Q值），-10*log10(p)，p为测错的概率。所以一条read某位置出错概率为0.01时，其quality就是20，通常认为Q20反映了数据的质量。Y轴将质量值被划分三部分：绿色（高质量），橘黄色（中等质量）和红色（低质量）。由于在每一个测序反应开始后，碱基的信号质量会逐渐降低，因此在每个读长最后的碱基通常都会处于橘黄色的中等质量区。"),"multi-p")`



###碱基平衡性分析

碱基平衡性分析主要用于检测测序数据是否存在AT、GC 分离现象。通常这种现象由建库或测序引入，并影响后续的生物信息分析结果，碱基分布结果见下图。

`r fig_box('../result/qualityControl/raw',"per_base_sequence_content.png", title='Raw Reads碱基平衡性', fig_name='', shape='QC', name_layer=2)`

`r notes(c("图为序列每个位点上碱基（A/T/C/G）含量统计的结果。","横坐标为read中的碱基位置（1-150bp），纵坐标为对应位点上单个碱基所占的比例。不同颜色代表不同的碱基类别。正常情况下四种碱基的出现频率应该是接近的，而且没有位置差异。因此好的样本中四条线应该平行且接近。当部分位置碱基的比例出现bias时，即四条线在某些位置纷乱交织，往往提示我们有overrepresented sequence的污染。当所有位置的碱基比例一致的表现出bias时，即四条线平行但分开，往往代表文库有bias (建库过程或本身特点)，或者是测序中的系统误差。"),"multi-p")`



###重复序列水平

测序深度越高，越容易产生一定程度的重复（duplication），这属于正常的现象。但如果duplication的程度很高，就提示我们可能有bias的存在（如建库过程中由于PCR扩增引起的 duplication）。


`r fig_box('../result/qualityControl/raw','duplication_levels.png', title='Raw Reads重复序列频率统计', fig_name='', shape='QC', name_layer=2)`

`r notes(c("","横坐标为reads重复的次数，纵坐标为重复次数对应的reads占unique reads的比例，以unique reads的总数作为100%。这里，我们仅对文件前2000，000个reads进行统计：对长度>75bp的reads将其截短为50bp，用于统计重复。"),"multi-p")`

`r list_path('../result/qualityControl/raw','_fastqc.html', link=TRUE, fixed=FALSE, name="sample")`

## clean后的数据质控 {#clean_QC}

测序数据包含一些带接头（adapter）、低质量的reads，这些序列会对后续的信息分析造成很大的干扰。为了保证后续信息分析质量，需要对测序数据进行进一步过滤。数据过滤的标准主要包括以下几点：

1、接头污染去除。去除3' 端的接头污染，至少10 bp overlap（AGATCGGAAG），允许20% 的碱基错误率；

2、reads过滤。去除含N（N表示无法确定碱基信息）较多（≥10%）的reads；

3、质量过滤。去除低质量的序列（Q≤10的碱基占整体序列碱基数目的50%以上，我们即认为是低质量的序列）。

我们使用Trimmomatic软件对raw data进行Clean。Trimmomatic软件是一种针对Illumina测序平台开发的一种处理测序原始数据的生物信息学软件。去掉接头、低质量的reads后，需要对clean reads进行新一轮质控，得到clean reads的数据信息。

###碱基质量分布

测序数据（clean data）碱基质量分布结果如下：


`r fig_box('../result/qualityControl/clean','per_base_quality.png', title='Clean Reads碱基质量分布', fig_name='', shape='QC', name_layer=2)`

`r notes(c("以盒形图的方式给出序列中每个位点对应的碱基质量分布的结果。","X轴是read中的碱基位置（1-150），Y轴是碱基质量；盒形图中间的红线表示中位数（median value）；黄色部分代表四分位距（25-75%）；上下分割线代表90%和10%的上下临界值；蓝色的线代表碱基质量的平均值。","碱基质量（Q值），-10*log10(p)，p为测错的概率。所以一条read某位置出错概率为0.01时，其quality就是20，通常认为Q20反映了数据的质量。Y轴将质量值被划分三部分：绿色（高质量），橘黄色（中等质量）和红色（低质量）。由于在每一个测序反应开始后，碱基的信号质量会逐渐降低，因此在每个读长最后的碱基通常都会处于橘黄色的中等质量区。"),"multi-p")`



###碱基平衡性分析
测序数据（clean data）碱基平衡性分析结果如下：


`r fig_box('../result/qualityControl/clean','per_base_sequence_content.png', title='Clean Reads碱基平衡性', fig_name='', shape='QC', name_layer=2)`

`r notes(c("图为序列每个位点上碱基（A/T/C/G）含量统计的结果。","横坐标为read中的碱基位置（1-150bp），纵坐标为对应位点上单个碱基所占的比例。不同颜色代表不同的碱基类别。正常情况下四种碱基的出现频率应该是接近的，而且没有位置差异。因此好的样本中四条线应该平行且接近。当部分位置碱基的比例出现bias时，即四条线在某些位置纷乱交织，往往提示我们有overrepresented sequence的污染。当所有位置的碱基比例一致的表现出bias时，即四条线平行但分开，往往代表文库有bias (建库过程或本身特点)，或者是测序中的系统误差。"),"multi-p")`


###重复序列水平

测序数据（clean data）重复序列水平结果如下：


`r fig_box('../result/qualityControl/clean','duplication_levels.png', title='Clean Reads重复序列频率统计', fig_name='', shape='QC', name_layer=2)`

`r notes(c("横坐标为reads重复的次数，纵坐标为重复次数对应的reads占unique reads的比例，以unique reads的总数作为100%。这里，我们仅对文件前2000，000个reads进行统计：对长度>75bp的reads将其截短为50bp，用于统计重复。"),"multi-p")`


`r list_path('../result/qualityControl/clean','_fastqc.html', link=TRUE, fixed=FALSE, name="sample")`


## Clean data质量信息 {#clean_state}

我们对clean data的质量信息进行统计，如下所示：


`r readtb('../result/qualityControl/QC_trim_stats.xls', title='clean data基本信息一览表')`


`r notes(c("表格说明：", "Sample：样品名称；", "Q20(%)，Q30(%)：分别计算过滤后序列中碱基质量大于20，30的碱基所占的比例；", "Deduplicated_Percentage：过滤后unique reads在clean reads中所占的比例；","GC(%)：过滤后序列的G和C的数量总和占总的碱基数量的比例；", "raw_read：原始序列总数；","clean_read：过滤后序列总数；", "clean2raw_read_ratio(%)：clean reads在原始序列中所占的比例（clean_reads * 100% / raw_reads）；","raw_base：原始序列碱基总数（raw_bases = raw_reads * sequence length）；","clean_base：过滤后序列的碱基总数；","clean2raw_base_ratio(%)：clean_bases 在原始序列碱基中所占的比例（clean_base * 100% / raw_base）。"))`


`r list_path('../result/qualityControl/QC_trim_stats.xls')`



# 物种鉴定及多样性分析

## 过滤后序列拼接
测序获得的下机数据通过 reads之间的 overlap关系拼接成长
序列，拼接成功的序列用于后期物种鉴定及其它分析。

拼接方法： 通过 qiime中fastq-join 脚本进行拼接。

拼接条件：（1）最小匹配长度为 8 bp；（2）重叠区域匹配率为 97%；



## OTU和分类鉴定结果统计

OTU（Operational Taxonomic Units）是在系统发生学研究或群体遗传学研究中，
为了便于进行分析，人为给某一个分类单元（品系，种，属，分组等）设置的同一
标志。在生物信息分析中，一般来说，测序得到的每一条序列来自一个菌。要了解
一个样品测序结果中的菌种、菌属等数目信息，就需要对序列进行归类操作（cluster）。
通过归类操作，将序列按照彼此的相似性分归为许多小组，一个小组就是一个 OTU。
可根据不同的相似度水平。

在此我们将合并的序列比对到注释至种名的数据库，最终均获得注释到种的OTU分类。

对于菌群数据，划分OTU获得的原始OTU丰度矩阵中，很可能包含大量丰度极低的OTU，这些OTU也往往仅在少数样本中偶尔出现（即出现频率低）；而高丰度的占优势的OTU则相对少得多。这一菌群组成分布的“两极分化”现象已被越来越多的研究所发现，而这些丰度和出现频率都非常低的“稀有”OTU相当于菌群数据中的“背景噪音”，极大地增加了数据分析的复杂度。通常情况下，去除这些稀有OTU对于解析整体菌群的影响微乎其微，却能显著改善菌群数据分析的效率（如果对稀有OTU感兴趣，建议对目标微生物单独进行富集，从而对它们的丰度和出现频率进行更精准的研究）。因此，为了保证分析结果的可靠准确，我们建议去除原始OTU丰度矩阵中包含的稀有OTU。在此我们过滤所有样本总read数小于5的OTU。

由于样本间测序的reads数目存在一定的差异，因此我们需要对菌种丰度进行归一化，然后方便进行组间的比较。在此我们根据clean的reads数目对丰度值进行归一化：normalized_abundance = abundance/read_number * 1000000。

此处abundance为样本中每个OTU的reads数，read_number为clean之后的read数。



同时基于已经构建好的注释到种的16S rDNA序列数据库，我们将reads比对到数据库进行物种归类， 在 Kingdom（界）、 Phylum（门）、 Class（纲）、 Order
（目）、 Family（科）、 Genus（属）、 Species（种）各个分类学水平上统计物种在各
个样品中的丰度，从而构建相应分类学水平上的 taxonomy profile。


### 样本中OTU丰度值

`r tb_box(dir = "../result/rankAbundance", file = "otu_table.txt", fixed=FALSE, title="各样品OTU丰度", n=5)`

`r notes(c('注：丰度值根据每个样品成功比对到数据库的reads数进行归一化。'))`

`r list_path('../result/rankAbundance', 'otu_table.txt', fixed=FALSE)`




`r tb_box(dir = "../result/Krona", file = "Species_number.xls", fixed=FALSE, title="OTU划分和分类地位鉴定结果统计表")`

`r notes(c('注：“Phylum”、“Class”、“Order”、“Family”、“Genus”、“Species”分别对应各样本中能分类至门、纲、目、科、属、种的OTU数。'))`

`r list_path('../result/Krona', 'Species_number.xls', fixed=FALSE)`



`r fig_box(dir = "../result/Krona", file = "Species_number.png", fixed=FALSE, title="OTU划分和分类地位鉴定结果统计图")`

`r list_path('../result/Krona', 'Species_number.xls', fixed=FALSE)`




### 各分类水平的分类学组成分析


`r fig_box(dir = "../result/summarizeTaxa/composition", file = "taxonomy_phylum_bar.png", fixed=FALSE, title="门水平分类学组成和丰度分布图")`

`r list_path('../result/summarizeTaxa/composition', 'taxonomy_phylum_bar.pdf', fixed=FALSE)`

将各分类水平的群落组成数据根据分类单元的丰度分布或样本间的相似程度加以聚类，根据聚类结果对分类单元和样本分别排序，并通过热图加以呈现。通过聚类，可以将高丰度和低丰度的分类单元加以区分，并以颜色梯度反映样本之间的群落组成相似度。本研究对丰度前20位的属进行聚类分析并绘制热图。

`r fig_box(dir = "../result/summarizeTaxa/composition", file = "taxonomy_phylum_heatmap.png", fixed=FALSE, title="结合聚类分析的门水平群落组成热图")`

`r notes(c('注：样本先按照彼此之间组成的相似度进行聚类，根据聚类结果横向依次排列。同理，分类单元也按照彼此在不同样本中分布的相似度进行聚类，根据聚类结果纵向依次排列。图中，红色代表在对应样本中丰度较高的门，绿色代表丰度较低的门。图中取该分类水平丰度最高的20个进行展示。'))`

`r list_path('../result/summarizeTaxa/composition', 'taxonomy_phylum_heatmap.pdf', fixed=FALSE)`


`r fig_box(dir = "../result/summarizeTaxa/composition", file = "taxonomy_species_bar.png", fixed=FALSE, title="种水平分类学组成和丰度分布图")`

`r list_path('../result/summarizeTaxa/composition', 'taxonomy_species_heatmap.pdf', fixed=FALSE)`


`r fig_box(dir = "../result/summarizeTaxa/composition", file = "taxonomy_species_heatmap.png", fixed=FALSE, title="结合聚类分析的种水平群落组成热图")`

`r notes(c('注：样本先按照彼此之间组成的相似度进行聚类，根据聚类结果横向依次排列。同理，分类单元也按照彼此在不同样本中分布的相似度进行聚类，根据聚类结果纵向依次排列。图中，红色代表在对应样本中丰度较高的种，绿色代表丰度较低的种。图中取该分类水平丰度最高的20个进行展示。'))`

`r list_path('../result/summarizeTaxa/composition', 'taxonomy_species_heatmap.pdf', fixed=FALSE)`



## 菌群Alpha多样性分析

### 丰度等级曲线

丰度等级曲线（Rank abundance curve）将每个样本中的OTU按其丰度大小沿横坐标依次排列，并以各自的丰度值为纵坐标，用折线或曲线将各OTU互相连接，从而反映各样本中OTU丰度的分布规律（详见https://en.wikipedia.org/wiki/Rank_abundance_curve）。对于微生物群落样本，该曲线可以直观地反映群落中高丰度和稀有OTU的数量。

`r fig_box(dir = "../result/rankAbundance", file = "rankAbundancePlot.png", fixed=FALSE, title="丰度等级曲线图")`


`r notes(c('注：横坐标为按丰度大小排列的OTU，纵坐标代表每个OTU在该样本中的丰度。每条折线代表一个样本的OTU丰度分布，折线在横轴上的长度反映了该样本中OTU数的多少，代表了群落的丰富度（Richness），折线越长，该样本中的OTU数越多；折线的平缓程度则反映了群落组成的均匀度（Evenness），折线越平缓，群落组成的均匀度越高，折线越陡峭，则群落中各OTU间的丰度差异越大，均匀度越低'))`

`r list_path('../result/rankAbundance', 'rankAbundancePlot.pdf', fixed=FALSE)`

### Alpha多样性指数计算


对于微生物群落而言，有多种指数来反映其Alpha多样性。不同的指数对于衡量群落多样性的侧重点各不相同，有些更侧重于体现群落的丰富度（即群落中微生物成员如OTU的数量），有些更倾向于反映群落的均匀度（即各成员间的丰度差异大小），也有一些多样性指数则综合考虑了以上两方面的因素。

常用的度量指数主要包括侧重于体现群落丰富度Chao1指数和ACE指数，以及兼顾群落均匀度的Shannon指数和Simpson指数（https://en.wikipedia.org/wiki/Diversity_index）。

Chao1丰富度估计指数（The Chao1 estimator，http://www.mothur.org/wiki/Chao）由Chao首先提出(Chao, 1984)，通过计算群落中只检测到1次和2次的OTU数（即“Singleton”和“Doubleton”），估计群落中实际存在的物种数。

ACE 丰富度估计指数（The ACE estimator，http://www.mothur.org/wiki/Ace）的计算方法更复杂，默认将序列量10以下的OTU都计算在内，从而估计群落中实际存在的物种数，同样由Chao提出(Chao and Yang, 1993)。

一般而言，Chao1或ACE指数越大，表明群落的丰富度越高。

与Chao1和ACE指数不同，Shannon多样性指数（Shannon diversity index，或称为Shannon-Wiener、Shannon-Weaver指数，http://www.mothur.org/wiki/Shannon）（Shannon, 1948a, b）综合考虑了群落的丰富度和均匀度。Shannon指数值越高，表明群落的多样性越高。

Simpson 多样性指数（The Simpson index，http://www.mothur.org/wiki/Simpson）也是评价群落多样性的常用指数之一，由Edward Hugh Simpson提出(Simpson, 1949)。Simpson指数值越高，表明群落多样性越高。
一般而言，Shannon指数对群落的丰富度以及稀有OTU更敏感，而Simpson指数对均匀度和群落中的优势OTU更敏感。

observed_otus 指数指数反映样品中群落的丰富度（species richness），即
简单指群落中物种的数量，而不考虑群落中每个物种的丰度情况。它对应的稀释曲
线还可以反映样品测序量是否足够。如果曲线趋于平缓或者达到平台期时也就可以认为测序
深度已经基本覆盖到样品中所有的物种；反之，则表示样品中物种多样性较高，还存在较多
未被测序检测到的物种。

`r tb_box(dir = "../result/alphaDiversity", file = "alpha.txt", fixed=FALSE, title="Alpha多样性指数表")`

`r notes(c(' 注：',
'Sample： 样品名；',
'chao1： chao1指数值；',
'Shannon： Shannon 指数值；',
'observed_otus：观测到的OTU数；',
'ace： ace 指数值；',
'simpson：simpson指数值。'))`


`r list_path('../result/alphaDiversity', 'alpha.txt', fixed=FALSE)`




Alpha多样性指数计图

`r fig_box(dir = "../result/alphaDiversity", file = "alpha.png", fixed=FALSE, title="Alpha多样性指数图")`

`r list_path('../result/alphaDiversity', 'alpha.pdf', fixed=FALSE)`





## 菌群结构的Beta多样性分析

### 基于UniFrac距离的PCoA主坐标分析
UniFrac距离是用于比较生物群落的距离度量，利用各样品间序列的进化信息来比较样品在特定的进化谱系中是否有显著的微生物群落差异。

UniFrac包括weighted UniFrac（加权UniFrac，定量）和unweighted UniFrac（未加权，定性），广泛用于微生物生态学。weighted UniFrac不仅考虑生物群落的存在与否，还要考虑其丰度，而unweighted UniFrac仅考虑它们的存在或不存在，不考虑丰度。

UniFrac可用于beta多样性分析，即对样品两两之间进行比较分析，得到样品间的unifrac距离矩阵。其计算方法为：首先利用来自不同环境样品的OTU代表序列构建一个进化树，Unifrac度量标准根据构建的进化树枝的长度计量两个不同环境样品之间的差异，差异通过0-1距离值表示，进化树上最早分化的树枝之间的距离为1，即差异最大，来自相同环境的样品在进化树中会较大几率集中在相同的节点下，即它们之间的树枝长度较短，相似性高。若两个群落完全相同，那么它们没有各自独立的进化过程，UniFrac值为0；若两个群落在进化树中完全分开，即它们是完全独立的两个进化过程，那么UniFrac值为1。


Unifrac分析得到的距离矩阵可用于多种分析方法，可通过多变量统计学方法PCoA（principal co-ordinates analysis） 分析，直观显示不同样品中微生物进化上的相似性及差异性。

PCoA（principal co-ordinates analysis）是一种研究数据相似性或差异性的可视化方法，通过一系列的特征值和特征向量进行排序后，选择主要排在前几位的特征值，PCoA可以找到距离矩阵中最主要的坐标，结果是数据矩阵的一个旋转，它没有改变样品点之间的相互位置关系，只是改变了坐标系统。通过PCoA 可以观察个体或群体间的差异。


`r fig_box(dir = "../result/betaDiversity", file = "weighted_unifrac.png", fixed=FALSE, title="PCA分析的样本二维排序图")`


`r fig_box(dir = "../result/betaDiversity", file = "otu_correlation_heatmap.png", fixed=FALSE, title=" ")`

`r list_path('../result/betaDiversity', 'otu_correlation_heatmap.pdf', fixed=FALSE)`

### 基于UniFrac距离的非度量多维尺度分析

非度量多维尺度法（NMDS）是一种将多维空间的研究对象（样本或变量）简化到低维空间进行定位、分析和归类，同时又保留对象间原始关系的数据分析方法。适用于无法获得研究对象间精确的相似性或相异性数据，仅能得到他们之间等级关系数据的情形。其基本特征是将对象间的相似性或相异性数据看成点间距离的单调函数，在保持原始数据次序关系的基础上，用新的相同次序的数据列替换原始数据进行度量型多维尺度分析。换句话说，当资料不适合直接进行变量型多维尺度分析时，对其进行变量变换，再采用变量型多维尺度分析，对原始资料而言，就称之为非度量型多维尺度分析。其特点是根据样品中包含的物种信息，以点的形式反映在多维空间上，而对不同样品间的差异程度，则是通过点与点间的距离体现的，最终获得样品的空间定位点图。

`r fig_box(dir = "../result/betaDiversity/NMDS", file = "weighted_unifrac_coords_NMDS1_2.png", fixed=FALSE, title="PCA分析的样本二维排序图")`

`r list_path('../result/betaDiversity/NMDS', 'weighted_unifrac_coords_NMDS1_2.pdf', fixed=FALSE)`


### 基于UniFrac距离的样本聚类分析


聚类分析主要指层次聚类（Hierarchical clustering）的分析方法，以等级树的形式展示样本间的相似度，通过聚类树的分枝长度衡量聚类效果的好坏。与MDS分析相同，聚类分析可以采用任何距离评价样本之间的相似度。常用的聚类分析方法包括非加权组平均法（Unweighted pair-group method with arithmetic means，UPGMA）、单一连接法（Single-linkage clustering）和完全连接法（Complete-linkage clustering）等。

Unifrac分析得到的距离矩阵可用于多种分析方法，通过层次聚类（Hierarchical cluatering）中的非加权组平均法UPGMA构建进化树等图形可视化处理，可以直观显示不同样品中微生物进化上的相似性及差异性。

UPGMA（Unweighted pair group method with arithmetic mean）假设在进化过程中所有核苷酸/氨基酸都有相同的变异率，即存在着一个分子钟。通过树枝的距离和聚类的远近可以观察样品间的进化距离。


`r fig_box(dir = "../result/betaDiversity/Tree", file = "beta_div_upgma_tree.png", fixed=FALSE, title="基于UniFrac距离矩阵的UPGMA聚类分析图")`


`r notes(c('注：样本根据彼此之间的相似度聚类，样本间的分枝长度越短，两样本越相似。'))`

`r list_path('../result/betaDiversity/Tree', 'beta_div_upgma_tree.pdf', fixed=FALSE)`


## 样本（组）间分类学组成的差异分析

### LEfSe分析
LEfSe为最近出现的一种基于线性判别分析（Linear discriminant analysis，LDA）效应量（Effect size）的分析方法，其本质是将线性判别分析与非参数的Kruskal-Wallis以及Wilcoxon秩和检验相结合，从而筛选关键的生物标记物（也就是关键群落成员）(Segata et al., 2011)。该方法由美国哈佛大学的Curtis Huttenhower课题组开发，它的一大特点是，不仅局限于对不同样本分组中的群落组成差异进行分析，更可以深入到不同的子分组（Subgroup）中，挑取在不同子分组中表现一致的关键微生物类群，因而目前已获得了广泛的应用。


`r tb_box(dir = "../result/LEfSe", file = "taxonomy_summary.res", fixed=FALSE, title="组间LEfSe分析结果表", n=5)`


`r notes(c('注：',
'Taxonomy：样本群落中所有分类单元列表，LEfSe会逐一判断这些分类单元的组间差异是否具有统计学显著性；',
'Highest_abundance：数值表明各分类单元所具有的最高组内相对丰度均值（为对数转换值）。如果该分类单元未体现出显著的组间差异，则后三列为空；',
'Group：对于具有统计学差异的分类单元，此处列出该分类单元对应的平均丰度最高的分组；',
'LDA_score：存在统计学差异时给出LDA差异分析的对数得分值（默认>2）',
'P_value：存在统计学差异时给出统计P值大小（默认< 0.05）。'))`

`r list_path('../result/LEfSe', 'taxonomy_summary.res', fixed=FALSE)`



`r fig_box(dir = "../result/LEfSe", file = "taxonomy_summary_LDA.png", fixed=FALSE, title="组间具有显著差异的分类单元")`

`r notes(c('注：纵坐标为组间具有显著差异的分类单元，横坐标则以条形图直观地展示对应分类单元的LDA差异分析对数得分值，并按照得分值大小进行排序，以此描述它们在不同分组样本中的差异大小。长度越长表明该分类单元的差异越显著，条形图的不同颜色指示了该分类单元所对应的丰度较高的样本分组。'))`

`r list_path('../result/LEfSe', 'taxonomy_summary_LDA.pdf', fixed=FALSE)`


`r fig_box(dir = "../result/LEfSe", file = "taxonomy_summary_cladogram.png", fixed=FALSE, title="基于分类等级树的组间差异分类单元展示图")`



`r notes(c('注：分类等级树展示了样本群落中从门到属（从内圈到外圈依次排列）所有分类单元的等级关系，节点大小对应于该分类单元的平均相对丰度，黄色节点代表未体现出显著的组间差异的分类单元，而其它色（如绿色和红色）则表明这些分类单元体现出显著的组间差异，且在该色所代表分组样本中丰度较高。字母则标识了组间存在显著差异的分类单元名称。'))`

`r list_path('../result/LEfSe', 'taxonomy_summary_cladogram.pdf', fixed=FALSE)`



### Anosim 分析

    ANOSIM (Analysis    of  similarities)分析也是一种非参数检验方法，与NMDS分析类似，通过对样本距离等级排序来判断样本组内和组间差异的大小，并通过置换检验评价原始样本组间差异的统计学显著性。
它是一种展示组别之间是否存在差异得方法。如果组别之间又差异，则组内差异小于组间差异。

Anosim 分析结果如下：


`r readtb('../result/anosimAdonis/anosim_results.txt', title='ANOSIM相似度分析', shape='small')`

`r notes(c('注：R值为ANOSIM的统计量，数值介于-1和1之间，表征组间差异与组内差异的差值大小。R值越接近1，表明组间差异越大，同时组内差异越小，分组效果越好；如果R=0，表明样本的分组效果等同于随机分配，各样本分组之间不具有可观测的统计学差异；如果R为负值，则表明组内差异超过了组间差异的大小，预示分组效果较差。P值则反映了ANOSIM分析结果的统计学显著性，P值越小，表明各样本分组之间的差异显著性越高。'))`


`r list_path('../result/anosimAdonis', 'anosim_results.txt', fixed=FALSE)`

`r fig_box(dir = "../result/anosimAdonis", file = "anosim_results.png", fixed=FALSE, title="Anosim 分析结果图")`


`r notes(c('注：Between 表示组件差异，其它表示组内差异'))`


`r list_path('../result/anosimAdonis', 'anosim_results.pdf', fixed=FALSE)`


### Kruskal-Wallis分析

下表是在不同组样本间有显著差异的 OTUs（P<0.05, Kruskal-Wallis test）


`r tb_box(dir = "../result/anosimAdonis", file = "kruskal_wallis.xls", fixed=FALSE, title="组间Kruskal-Wallis统计结果", n=5)`

`r notes(c(" 注；", 
"OTU：OTU编号",
"Test-Statistic：统计值",
"P：P值",
"FDR_P：FDR矫正后P值",
"Bonferroni_P：Bonferroni矫正后P值",
"group1_mean：group1平均值",
"group2_mean：group2平均值（依次类推至倒数第一列）",
"taxonomy：物种分类"))`


`r list_path('../result/anosimAdonis', 'kruskal_wallis.xls', fixed=FALSE)`


## 分类学组成展示

### 基于Krona的分类学组成信息交互展示

使用Krona软件（https://github.com/marbl/Krona/wiki）进行群落分类学组成的交互展示(Ondov et al., 2011)。相比于上述的MEGAN和GraPhlAn两种软件，Krona不仅可以对样本分类学组成进行可视化分析，更侧重于数据的交互展示。



<iframe src="../result/Krona/html/C02.html" width="710" height="700" >

<a href="included.html">你的浏览器不支持iframe页面嵌套，请点击这里访问页面内容。</a>

</iframe>

基于Krona的分类学组成信息交互展示图


`r notes(c('注：分类等级树展示了样本总体中，从门到属（从内圈到外圈依次排列）所有分类单元（以节点表示）的等级关系，节点大小对应于该分类单元的平均相对丰度，相对丰度前20位的分类单元还将在图中以字母标识（从门到属按照从外层到内层依次排列），字母上的阴影颜色同对应节点颜色一致。'))`

`r list_path('../result/Krona', '.html', fixed=FALSE)`


### 基于GraPhlAn的分类学组成信息可视化

使用GraPhlAn这一最近涌现的可视化工具，对样本总体在各分类水平的组成构建等级树，同时以不同颜色区分各分类单元，并通过节点大小反映它们的丰度分布。GraPhlAn绘制的分类等级树提供了一种从复杂的群落数据中，快速发现优势微生物类群的方法。

`r fig_box(dir = "../result/GraPhlAn", file = "GraPhlAn.png", fixed=FALSE, title="基于GraPhlAn的样本总体分类等级树图")`


`r notes(c('注：分类等级树展示了样本总体中，从门到属（从内圈到外圈依次排列）所有分类单元（以节点表示）的等级关系，节点大小对应于该分类单元的平均丰度，丰度前20位的分类单元还将在图中以字母标识（从门到属按照从外层到内层依次排列），字母上的阴影颜色同对应节点颜色一致。'))`


`r list_path('../result/GraPhlAn', 'GraPhlAn.png', fixed=FALSE)`



## 物种相关性分析

通过分析物种在不同样品的丰度变化一致性情况，来推测两个样品物种之间的作用关系。


将物种之间的关系，用一张网来表示。网的结点表示一个物种， 结点大小来表示物种丰度大小， 结点
颜色表示同一个“种”水平的物种，两个节点之间的连线表示这两个物种有关联。此处计算两个种之间的pearson相关性，仅考虑相关性大于0.95的物种对。


`r fig_box(dir = "../result/network/correlation_pdf", file = "correlation.txt.png", fixed=FALSE, title="物种相关性图")`


`r notes(c('注：'))`


`r list_path('../result/network/correlation_pdf', 'correlation.txt.pdf', fixed=FALSE)`
