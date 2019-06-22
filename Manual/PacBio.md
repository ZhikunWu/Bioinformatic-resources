
### PacBio三代测序专业术语解读
* circular consensus sequencing (CCS) read: 环形一致性序列，这种一致性序列通过对来自单个ZMW中的subreads进行比对产生。注意产生的CCS read不包括或不需要与参考序列比对。产生的CCS reads使用CCS算法需要至少两轮读取来自插入片段的subreads。
* full-pass subread:指的是subread开始于一端的adapter然后在另一端的adapter序列终止。full-pass subread不会从插入序列的中间部位起始或终止。 
* mapped polymerase read length: 过滤后，可比对至参考基因组序列上的测序reads的长度，Polymerase Read是包含adapters的。
* mapped subread length: 比对到目标参考序列的subread的长度，其中不含接头序列。
* N50 read length metric: 指的是测序得到的reads中，50%的reads长度长于或等于这个值
* paired barcodes: 在SMRTbell™ template中插入序列两端的barcode序列均不一致的barcode序列。barcoding分析软件使用独特的barcodes对来区分和分析reads。
* polymerase read: 即高质量测序reads，包含adaptors以及测多次获得multiple subreads。
* polymerase read length: 去除低质量区域后一个零模波导孔中产生的总碱基数。其中可能包含接头序列。
* polymerase read quality: 测序reads中，single-pass read的平均质量值。
* preassembled long read (PLR): 在HGAP预装配步骤中输出的read。
* productivity: 对来自一个ZMW的reads的计算。P=1表示来从ZMW产生了一条polymerase read。P=0表示这个ZMW没有产生read，其可能原因是缺少聚合酶。P=2表示其他情况，此测序数据不可用，可能是ZMW中存在多个模板-聚合酶复合物，较高的背景信号等原因。
* read quality (RQ): 对来自一个零模波导孔的subreads的准确度进行预测。有时也用QC Score或Read Score代替。
* subread: 每一个polymerase read被分割形成一个或多个subreads，这些subreads包含来自被聚合酶测通的插入片段单条链的序列但不包含接头序列。
* symmetric barcodes: 在SMRTbell template插入片段两端序列都相同的barcode序列。
* zero-mode waveguide (ZMW): 即零模波导孔，其为一种用于将光线限制在小的观测体积的纳米光学设备，这是一种具有导电层的小孔。这种小孔由于直径太小而限制光线在用于检测的波长范围内传播。其为SMRT Cell的一部分。
* MagBead: 小的超顺磁性磁珠，粒径2-3 um，将DNA-聚合酶复合物结合在磁珠上，然后能用于在偶联步骤洗去上清中的污染物。DNA-聚合酶/磁珠复合物能被用于仪器固定步骤。
* SMRT® Cells: 由零模波导孔纳米结构阵列组成的基底。SMRT Cells连同DNA Sequencing Kit一起用于仪器的DNA测序。


### Pacbio三代全长转录组(Iso-Seq ) 数据合并
三代转录组测序数据，如果要进行多个数据合并（比如加测一次），以合并subreads.bam为例:

* 需要采用SMRT中的pbmerge, 不能采用samtools 的merge 

* 需要采用pbindex 对bam 文件进行index, 也不能采用samtools index  构建index 

构建的index 文件（pbi后缀）非常的重要，因为后面的分析中，有些步骤虽然采用的是subreads.bam 文件，但是如果没有index 的pbi 文件，命令执行就会失败，而且没有提示(大坑）。


.h5 files contain a lot more than just basecalls and quality scores 
```
 h5dump –n <smrtcell_data_file>.bax.h5
```



### pacbio adapter

This is the "smartbell" adapter:

ATCTCTCTCTTTTCCTCCTCCTCCGTTGTTGTTGTTGAGAGAGAT

However, it's hard to remove because of the high rate of indels. You should use PacBio's adapter-removal tools from SmartPortal since they are tuned for the error profile.


```
removesmartbell in=reads.fq out=clean.fq split=t adapter=ATCTCTCTCTTTTCCTCCTCCTCCGTTGTTGTTGTTGAGAGAGAT
```




