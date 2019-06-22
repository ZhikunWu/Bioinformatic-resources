## 数据优化
### 数据优化与统计

### OTU聚类

#### 分析方法

OTU（Operational Taxonomic Units）是在系统发生学或群体遗传学研究中，为了便于进行分析，人为给某一 个分类单元（品系，属，种、 分组等）设置的同一标志。 要了解一个样本测序结果中的菌种、 菌属等数目信息，就需要对序列进行归类操作（cluster）。 通过归类操作，将序列按照彼此的相似性分归为许多小组，一个小组就是一个 OTU。可根据不同的相似度水平，对所有序列进行 OTU 划分，通常在 97%的相似水平下的 OTU 进行生 物信息统计分析。

分析步骤如下：
* 对优化序列提取非重复序列，便于降低分析中间过程冗余计算量
* 去除没有重复的单序列
* 按照 97%相似性对非重复序列（不含单序列）进行 OTU聚类
* 聚类后中去除嵌合体，得到 OTU 的代表序列
* 将所有优化序列 map 至 OTU 代表序列，选出与 OTU 代表序列相似性在 97%以上的序列，生成 OTU 表格


### 分类学分析（Taxonomy）

#### 分析方法

为了得到每个 OTU 对应的物种分类信息，采用 RDP classifier 贝叶斯算法对 97%相似水平的 OTU 代表序列进行分类学分析，并分别在各个分类水平：domain（域），kingdom（界），phylum（门），class（纲），order（目），family（科），genus（属），species（种）统计各样本的群落组成。 比对数据库为[Greengene](http://greengenes.secondgenome.com/)。



### 样本多样性分析
群落生态学中研究微生物多样性，通过单样本的多样性分析（Alpha 多样性）可以反映微生物群落的丰度和多样性，包括一系列统计学分析指数估计环境群落的物种丰度和多样性。

* 计算菌群丰度（Community richness）的指数有：
  [Chao](http://www.mothur.org/wiki/Chao) - the Chao1 estimator
    [Ace](http://www.mothur.org/wiki/Ace) - the ACE estimator

* 计算菌群多样性（Community diversity）的指数有:
  [Shannon](http://www.mothur.org/wiki/Shannon) - the Shannon index
    [Simpson](http://www.mothur.org/wiki/Simpson) - the Simpson index
    
### 稀释性曲线（Rarefactioncurve）
稀释性曲线是从样本中随机抽取一定数量的个体，统计这些个体所代表的物种数目，并以个体数与物种 数来构建曲线。 它可以用来比较测序数据量不同的样本中物种的丰富度，也可以用来说明样本的测序数据量是否 合理。采用对序列进行随机抽样的方法，以抽到的序列数与它们所能代表 OTU 的数目构建 rarefaction curve，当 曲线趋向平坦时，说明测序数据量合理，更多的数据量只会产生少量新的 OTU，反之则表明继续测序还可能产 生较多新的OTU。 因此，通过作稀释性曲线，可得出样本的测序深度情况。本研究使用 97%相似度的 OTU，利用 qiime 做 rarefaction 分析，利用 R 语言工具制作曲线图。


### Rank-Abundance 曲线
Rank-abundance曲线是分析多样性的一种方式。 构建方法是统计单一样本中，每一个 OTU 所含的序列 数，将 OTUs 按丰度（所含有的序列条数）由大到小等级排序，再以 OTU 等级为横坐标，以每个 OTU 中所含的 序列数（也可用OTU中序列数的相对百分含量）为纵坐标做图。

Rank-abundance 曲线可用来解释多样性的两个方面，即物种丰度和物种均匀度。 在水平方向，物种的丰度由 曲线的宽度来反映，物种的丰度越高，曲线在横轴上的范围越大；曲线的形状（平滑程度）反映了样本中物种的 均度，曲线越平缓，物种分布越均匀。

### Specaccum物种累积曲线
物种累积曲线( species accumulation curves)[14] 是用于描述随着样本量的加大物种增加的状况，是调查样本的物种组成和预测样本中物种丰度的有效工具，在生物多样性和群落调查中，被广泛用于样本量是否充分的判断以及物种丰富度( species richness) 的估计。 因此，通过物种累积曲线不仅可以判断样本量是否充分，在样本量充分的前提下，运用物种累积曲线还可以对物种丰富度进行预测（默认在样本量大于 8 个时分析）。


## 物种组成分析
###  群落结构组分图

根据分类学分析结果，可以得知一个或多个样本在各分类水平上的分类学比对情况。 在结果中，包含了两个信息：
* 样本中含有何种微生物
* 样本中各微生物的序列数，即各微生物的相对丰度

因此，可以使用统计学的分析方法，观测样本在不同分类水平上的群落结构。 将多个样本的群落结构分析放在一起对比时，还可以观测其变化情况。 根据研究对象是单个或多个样本，结果可能会以不同方式展示。 通常使 用较直观的饼图或柱状图等形式呈现[19]。 群落结构的分析可在任一分类水平进行。

### 群落 Heatmap 图
Heatmap可以用颜色变化来反映二维矩阵或表格中的数据信息，它可以直观地将数据值的大小以定义的 颜色深浅表示出来。 常根据需要将数据进行物种或样本间丰度相似性聚类，将聚类后数据表示在 heatmap 图上， 可将高丰度和低丰度的物种分块聚集，通过颜色梯度及相似程度来反映多个样本在各分类水平上群落组成的相似 性和差异性。结果可有彩虹色和黑红色两种选择。

软件及算法：R 语言 vegan 包，vegdist 和 hclust 进行距离计算和聚类分析；距离算法：Bray-Curtis，聚类方 法：complete。 图中颜色梯度可自定为两种或两种以上颜色渐变色。 样本间和物种间聚类树枝可自定是否画出。

## Beta多样性分析
### PCA分析
PCA 分析(Principal Component Analysis)[12]，即主成分分析，是一种对数据进行简化分析的技术，这种方法 可以有效的找出数据中最“主要”的元素和结构，去除噪音和冗余，将原有的复杂数据降维，揭示隐藏在复杂数据 背后的简单结构。 其优点是简单且无参数限制。 通过分析不同样本 OTU（97%相似性）组成可以反映样本间的差 异和距离，PCA 运用方差分解，将多组数据的差异反映在二维坐标图上，坐标轴取能够最大反映方差值的两个特征值。 如样本组成越相似，反映在 PCA 图中的距离越近。 不同环境间的样本可能表现出分散和聚集的分布情况，PCA 结果中对样本差异性解释度最高的两个或三个成分可以用于对假设因素进行验证。

### PCoA 分析
PCoA 分析，即主坐标分析（principal co-ordinates analysis），也是一种非约束性的数据降维分析方法，可用 来研究样本群落组成的相似性或差异性，与 PCA 分析类似；主要区别在于，PCA 基于欧氏距离，PCoA 基于除 欧氏距离以外的其它距离，通过降维找出影响样本群落组成差异的潜在主成分。

PCoA 分析，首先对一系列的特征值和特征向量进行排序，然后选择排在前几位的最主要特征值，并将其表 现在坐标系里，结果相当于是距离矩阵的一个旋转，它没有改变样本点之间的相互位置关系，只是改变了坐标系统。

### 基于 Beta 多样性距离的非度量多维尺度分析(NMDS)
非度量多维尺度法是一种将多维空间的研究对象（样本或变量）简化到低维空间进行定位、 分析和归类， 同时又保留对象间原始关系的数据分析方法。 适用于无法获得研究对象间精确的相似性或相异性数据，仅能得到 他们之间等级关系数据的情形。 其基本特征是将对象间的相似性或相异性数据看成点间距离的单调函数，在保持 原始数据次序关系的基础上，用新的相同次序的数据列替换原始数据进行度量型多维尺度分析。 换句话说，当资 料不适合直接进行变量型多维尺度分析时，对其进行变量变换，再采用变量型多维尺度分析，对原始资料而言， 就称之为非度量型多维尺度分析。 其特点是根据样本中包含的物种信息，以点的形式反映在多维空间上，而对不同样本间的差异程度，则是通过点与点间的距离体现的，最终获得样本的空间定位点图。

#### 多样本相似度树状图
利用树枝结构描述和比较多个样本间的相似性和差异关系。 首先使用描述群落组成关系和结构的算法计算样 本间的距离，即根据 beta 多样性距离矩阵进行层次聚类（Hierarchical cluatering）分析，使用非加权组平均法UPGMA（Unweighted pair group method with arithmetic mean）算法构建树状结构，得到树状关系形式用于可视化 分析。


#### ANOSIM 相似性分析
相似性分析(ANOSIM)是一种非参数检验，用来检验组间（两组或多组）的差异是否显著大于组内差异，从而判断分组是否有意义。 首先利用 Bray-Curtis 算法计算两两样品间的距离，然后将所有距离从小到大进行排序，按以下公式计算 R 值，之后将样品进行置换，重新计算 R*值，R*大于 R 的概率即为 P 值。

#### Adonis多因素方差分析
Adonis 又称置换多因素方差分析（permutational MANOVA）或非参数多因素方差分析（nonparametricMANOVA）。 它利用半度量(如 Bray-Curtis) 或度量距离矩阵(如 Euclidean)对总方差进行分解，分析不同分组因素对样品差异的解释度，并使用置换检验对划分的统计学意义进行显著性分析。


## 系统发生进化树
在分子进化研究中，系统发生的推断能够揭示出有关生物进化过程的顺序，了解生物进化历史和机制，可以 通过某一分类水平上序列间碱基的差异构建进化树。

本研究使用[FastTree](http://www.microbesonline.org/fasttree/)，通过选择 OTU 或某一水平 上分类信息对应的序列根据最大似然法（approximately-maximum-likelihood phylogenetic trees）构建进化树，使用 R 语言作图绘制进化树。 结果可以用列图或者圈图的形式呈现。

## 差异分析
### LEfSE 分析

LEfSe[30]是一种用于发现高维生物标识和揭示基因组特征的软件。 包括基因，代谢和分类，用于区别两个 或两个以上生物条件（或者是类群）。 该算法强调的是统计意义和生物相关性。 让研究人员能够识别不同丰度的 特征以及相关联的类别。

LEfSe 通过生物学统计差异使其具有强大的识别功能。 然后，它执行额外的测试，以评估这些差异是否符合预期的生物学行为。 具体来说，首先使用 non-parametric factorial Kruskal-Wallis (KW) sum-rank test（非参数因子 克鲁斯卡尔—沃利斯和秩验检）检测具有显著丰度差异特征，并找到与丰度有显著性差异的类群。 最后，LEfSe 采用线性判别分析（LDA）来估算每个组分（物种）丰度对差异效果影响的大小。



### Mutmap

Mutmap定位的适用条件?
化学诱变或者是物理诱变引起的点突变；野生型亲本重测序+突变型子代混池测序；有参考基因组；任何发生性状分离的家系群体

MutMap-Gap是什么？
之前的MutMap和MutMap+方法，我们都需要知道亲本的参考序列。但是在大多数情况下，研究的品系可能与数据库中该物种的参考基因组有一些区别。比如这个岛国团队，他们研究的水稻品种是“Hitomebore”，但是水稻的参考基因组来自另外一个品种“Nipponbare”。

由于计算SNP-index时需要比对到亲本的参考序列上，如果EMS诱导的突变发生在一个参考基因组没有的基因上，那么用上述的MutMap和MutMap+就无法找出该候选基因。而MutMap-Gap的方法就是结合了MutMap和de novo组装的一种基因定位方法，从而解决参考基因缺失位点上的基因突变问题。


•基于SNP-index的分析方法
基于SNP-index的策略主要是日本IwateBiotechnologyResearch Center的一个团队创立，其中也取得了一些出色的工作。他们开发出了MutMap（Abe,A. et al., 2012）、QTL-seq（Takagi,H. et al., 2013）、MutMap+（R Fekih etal., 2013）、MutMap-Gap（Takagi,H. et al., 2013）等，在后面我们会分别讲到他们的原理和怎么使用他们。
•BSR-seq
BSR-seq基于Bayesian方式来来计算SNP标记和目的基因之间的重组概率。同时采用混合RNA测序，可以大大的降低费用，也能获得比较好的定位效果。
PoPoolation2
•PoPoolation2通过比较两个混合群体SNP的频率，从而对两个群体进行候选基因定位， 这个方法也可以用于GWAS分析。
G分布预测群体QTL
这个方法是最早的在植物里面应用BSA方法鉴定QTL，被Paul等2011年发表在 Plos Computational Biology，似乎后面实际应用并不是很多。


### 基于GraPhlAn的分类学组成信息可视化

使用GraPhlAn这一最近涌现的可视化工具(Asnicar et al., 2015)，对样本总体在各分类水平的组成构建等级树，同时以不同颜色区分各分类单元，并通过节点大小反映它们的丰度分布。与MEGAN相比，GraPhlAn绘制的分类等级树提供了一种从复杂的群落数据中，快速发现优势微生物类群的方法。

`r fig_box(dir = "../16S/GraPhlAn", file = "GraPhlAn.png", fixed=FALSE, title="基于GraPhlAn的样本总体分类等级树图")`


`r notes(c('注：分类等级树展示了样本总体中，从门到属（从内圈到外圈依次排列）所有分类单元（以节点表示）的等级关系，节点大小对应于该分类单元的平均相对丰度，相对丰度前20位的分类单元还将在图中以字母标识（从门到属按照从外层到内层依次排列），字母上的阴影颜色同对应节点颜色一致。'))`




# 转录本拼接

对于lincRNA的搜索，首先需要对比对后的reads进行拼接，来寻找新的转录本。我们采用Cufflinks(Trapnell et al,2013)软件对比对结果进行组装，在此基础上进行lncRNA的筛选。

## 基于cufflinks的拼接

cufflinks使用概率模型，可同时组装和量化尽可能小的isoform集的表达水平，提供表达数据在给定位点的最大似然说明，针对链特异性文库有特定的参数可准确提供链的信息。cufflinks拼接结果展示如下：

`r readtb("../novel_transcript/cufflinks/293TW2_virus/transcripts.gtf.xls", title="cuffliks拼接结果展示（部分）", n=10)`

`r list_path("../novel_transcript/cufflinks", "transcripts.gtf",fixed=TRUE)`

`r notes(c( 
"表格说明：",
"Chr：染色体编号；",
"Source：来源描述；",
"Type：类型；",
"Start_Site：在参考基因组上的起始坐标；",
"End_Site：在参考基因组上的终止坐标；",
"Score：每个基因中丰度最高的异构体记为1000，较低风度异构体则为其比值；",
"Strand：在参考基因组上的+或-比对信息；",
"Frame：Cufflinks不对编码框其实位点进行预测，因此此处为. ；",
"Attributes：转录本或类型对应id等相关描述信息；"))`


我们将所有样本组装的转录本与参考基因组的转录本进行了比较，对拼接的转录本的类型（class code）进行了统计，结果展示如下：

`r single_fig("../novel_transcript/cuffcompare/mode_stat.png", title="拼接转录本的类型分布情况")`
 
 `r notes(c("图片说明：",".：转录本所属类别不明；","c：组装的转录本被包含在参考基因组注释的转录本中；","e：组装的转录本只有一个exon，且与参考基因组注释的转录本至少有10bp重叠；","eq：与参考基因组注释的转录本完全相同；","i：组装的转录本全部在考基因组注释的转录本的内含子中；","j：组装的转录本与参考基因组注释的转录本至少有一个共同的剪接位点；","o：组装的转录本与参考基因组注释的转录本的外显子有重叠","p：该转录本可能是聚合酶结合位点，位于参考基因组注释的转录本上游2kb以内；","s：组装的转录本与参考基因组注释的转录本的反义链有overlap，可能是mapping错误造成的；","u：组装的转录本与参考基因组注释的转录本没有任何重叠，处于基因间区；","x：组装的转录本与参考基因组注释的转录本外显子的反义链有重叠区。"))`


 ### 新转录本差异表达分析
 新转录本


 ### 新转录本的编码能力筛选

 转录本初步的筛选并不能决定我们拼接得到的转录本是lincRNA。事实上，是否具有编码潜能是判断转录本是否为lncRNA的关键条件，为了确定初步筛选得到的转录本是否具有编码潜能，我们分别进行了如下四个方面的分析，主要包括：CPC 分析、CNCI 分析、CPAT分析、PhyloCSF分析。

 ####   CPC分析

 CPC（ CodingPotential Calculator）主要是基于序列的特征（特征主要包括：序列开放阅读框的长度和质量、与Uniprot非冗余蛋白数据库比对的质量），采用支持向量机（Support Vector Mechine， SVM）方法对序列进行分类，分类值小于0则认为非编码，大于0则认为是编码序列，结果展示如下：

 `r readtb("../novel_transcript/coding_potential/CPC/CPC_potential.xls", title="CPC编码能力评价结果展示（部分）", shape="nomal")`


 `r notes(c("表格说明：","transcript_id：转录本编号；","length：转录本长度；","coding/nocoding：是否编码；","coding_score：编码得分；"))`

 `r list_path("../novel_transcript/coding_potential/CPC","CPC_potential.xls")`

 #### CNCI分析

 CNCI(Coding-Non-Coding Index)也是基于支持向量机分类模型来对序列进行分类的方法，结果展示如下：

 `r readtb("../novel_transcript/coding_potential/CNCI/CNCI.index", title="CNCI编码能力评价结果展示（部分）", shape="small")`


 `r notes(c("表格说明：","transcript_id：转录本编号；","index：编码能力评价结果；", "score:编码能力评价值，该值大于0则为coding，小于0则为noncoding；","start：转录本序列起始位点；","end：转录本序列终止位点；"))`

 #### CPAT分析

 CPAT是针对序列的开放阅读框长度、开放阅读框覆盖度、Fickett统计、六碱基使用偏好性等四种特征建立逻辑回归模型，对转录本的编码能力进行预测。检测编码能力具有较强的敏感性。通过大量数计算编码和非编码基因来确定coding_prob的阈值。
  

  `r readtb("../novel_transcript/coding_potential/CPAT/CPAT_result", title="Pfam注释结果展示（部分）")`

  `r notes(c("表格主要内容说明：","mRNA_size：转录本编号；","ORF_size",))`

  #### phyloCSF序列保守性分析

  phyloCSF(phylogenetic codon substitution frequency)进化密码子置换频率分析，利用多物种间的全基因组序列比对文件定义一段基因组区域是否有编码潜能。

  其主要是通过建立这样一个模型：先通过对一段序列进行开放阅读框的搜索，然后基于多物种在该序列处的多序列比对文件进行密码子置换频率分析，然后建立“密码子置换频率”与“该段序列是保守序列的可能性”之间的关系，这个关系由EM算法的后验概率给出，然后取对数值。如果该值小于0，则认为该段序列是非保守序列的可能性要高于该序列是保守性序列的可能性；反之大于0，则认为该序列更可能是保守序列。通常不同的物种间phyloCSF保守性阈值不能完全以0为划分标准，不同物种的阈值不尽相同，本项目物种为人，根据经验值我们确定保守性阈值为100。

  以下表格具体展示了我们候选lincRNA基于PhyloCSF保守性分析的得分值： 

  `r readtb("../novel_transcript/coding_potential/PhyloCSF/PhyloCSF_potential.xls", title="PhyloCSF保守性评分结果展示（部分）")`


  `r notes(c("表格说明：","trans_script_id：转录本编号；","max_score(decibans)：PhyloCSF保守性评分，分值的单位为decibans；","orf_start：PhyloCSF预测得到的该段序列最长的开发阅读框起始位置；","orf_end：PhyloCSF预测得到的该段序列最长的开发阅读框终止位置；","strand：所在参考序列的+/-链情况；","orf_pep：PhyloCSF预测该段序列最长开发阅读框可能翻译出来的多肽序列；"))`

  经过以上CPC、CNCI、CPAT、PhyloCSF四种工具的预测，我们将四种预测工具得到的lincRNA求交集，作为我们novel预测的lincRNA。 


  `r single_fig("../novel_transcript/coding_potential/noncoding.png", title="4种方法结果维恩图展示noncoding转录本", shape="big")`


  `r single_fig("../novel_transcript/coding_potential/coding.png", title="4种方法结果维恩图展示coding转录本", shape="big")`


  "Sample：样品名称；",
  "Seq_number：序列数目；",
  "Total_length：总序列长度：",
  "Min_length：最短序列长度；",
  "Max_length：最长序列长度；",
  "N50(bp)：N50长度，表示所有序列中50%的序列都大于该长度；",
  "N70(bp)：N70长度；",
  "N90(bp)：N90长度；"





### reference
```
Aßhauer K P,Wemheuer B, Daniel R, et al. Tax4Fun: predicting functional profiles  from metagenomic 16S rRNA data[J]. Bioinformatics, 2015, 31(17):  2882-2884.
Gibbons S M. Microbial community ecology: Function over phylogeny[J].  NatureEcology & Evolution, 2017, 1: 0032.
Louca S,Parfrey L W, Doebeli M. Decoupling function and taxonomy in the global  oceanmicrobiome[J]. Science, 2016, 353(6305): 1272-1277.
Nelson M B, Martiny A C, Martiny J B H. Global biogeography of microbial nitrogen-  cycling traits in soil[J]. Proceedingsof the National Academy of  Sciences, 2016,  113(29): 8033-8040.
Sun B, Wang X, Bernstein S, et al. Marked variation between winter and spring  gutmicrobiota in free-ranging Tibetan Macaques (Macaca thibetana)  [J].  Scientificreports, 2016, 6.
Thomas A M,Jesus E C, Lopes A, et al. Tissue-associated bacterial  alterations in  rectalcarcinoma patients revealed by 16S rRNA community  profiling[J]. Frontiersin  Cellular and Infection Microbiology, 2016, 6.
Wang K, Ye X, Zhang H, et al. Regional variations in the diversity and  predictedmetabolic potential of benthic prokaryotes in coastalnorthern  Zhejiang, East  China Sea[J]. Scientific Reports, 2016, 6: 38709
Choi J J, Kim S H. A genome Tree of Life for theFungi kingdom[J]. Proceedings of the National Academy of Sciences, 2017, 114(35):9391-9396.
```


### structure variation
GT：基因型。GL: 三种基因型的质量值。GQ：基因型质量数。FT：是否通过基因型过滤，PASS表示通过。RC：支持结构变异高质量序列数。RCL：左边控制区域高质量序列数。RCR：右边控制区域高质量序列数。CN：常染色体基于序列深度的拷贝数估计。DR：高质量参照对数。DV：高质量变异对数。RR：高质量与参考一致的跨越序列数。RV：高质量与变异一致的跨越序列数。

