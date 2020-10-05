# BSA分析中G statistics

<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

## G statistics算法

G statistics算法来自文章**[The Statistics of Bulk Segregant Analysis Using Next Generation Sequencing](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002255)**

计算公式如下：

$$\color{black}{ G = 2 * \sum _{i=1} ^4 n _i * ln(\frac {obs(n _i)} {exp(n _i)}) } $$

\\( n _i \\) 中i取值1到4，分别为两个混池中参考基因组等位和变异等位的覆盖度，如下表：

Allele    | High bulk| Low bulk
----------|----------|---------
Reference | n1       | n2
Alternate | n3       | n4

obs为观测值，exp为理论值，各个等位的理论值计算公式如下：

$$ exp(n _1) = \frac{(n _1 + n _2) * (n _1 + n _3)} {(n _1 + n _2 + n _3 + n _4)}  $$
$$ exp(n _2) = \frac{(n _2 + n _1) * (n _2 + n _4)} {(n _1 + n _2 + n _3 + n _4)}  $$
$$ exp(n _3) = \frac{(n _3 + n _1) * (n _3 + n _4)} {(n _1 + n _2 + n _3 + n _4)}  $$
$$ exp(n _4) = \frac{(n _4 + n _2) * (n _4 + n _3)} {(n _1 + n _2 + n _3 + n _4)}  $$


## G statistics的计算

G statistics的python代码实现如下：

```python
def G_statistics(s1_ref, s1_alt, s2_ref, s2_alt):
    total = s1_ref + s1_alt + s2_ref + s2_alt
    exp1 = (s1_ref + s2_ref) * (s1_ref + s1_alt) / total
    exp2 = (s2_ref + s1_ref) * (s2_ref + s2_alt) / total
    exp3 = (s1_alt + s1_ref) * (s1_alt + s2_alt) / total
    exp4 = (s2_alt + s1_alt) * (s2_alt + s2_ref) / total
    ### numpy.log() is same to ln()
    Gstat = 2 * (s1_ref * np.log(s1_ref/exp1) + s2_ref * np.log(s2_ref/exp2) + s1_alt * np.log(s1_alt/exp3) + s2_alt * np.log(s2_alt/exp4))
    Gstat = '%.3f' % Gstat
    return Gstat
```

结果文件如下，前四列分别为变异的染色体编号、物理位置、ref等位、alt等位；随后两列为混池1和混池2中ref和alt两个等位的覆盖度；最后一列为计算得到的G值。
```
$ sort -k 7nr T01_T02_Gstatistics_pre.txt | head

Chr     Pos     Ref     Alt     T01_depth       T02_depth       G_Stats
chr2B   233268742   G   A   1824_3073   4630_1134   2119.414
chr2B   210652242   G   A   2145_3079   3883_699    2084.936
chr2B   233268891   C   T   1161_2233   3054_763    1609.921
chr2B   44311534    T   C   2912_3910   4807_1603   1452.935
chr2B   97441940    T   G   1822_3001   3097_1011   1309.122
chr2B   44311161    G   A   3125_3592   5267_1704   1236.212
chr2B   44311152    G   A   3087_3513   5189_1661   1212.975
chr2B   44311129    T   C   2928_3632   4911_1737   1190.010
chr2B   44311030    G   A   2482_3297   4507_1633   1157.112
chr2B   44310964    C   G   2765_3436   4642_1692   1084.585

```

## 原G statistics存在的问题

仔细观察我们会发现结果存在一定的问题，G值的大小与该变异位点总的覆盖度显著相关，假如测序不是均匀的覆盖整个基因组，则计算的G值可能存在很大的偏差。

因此我们可以考虑计算得到的G值除以该位点所有等位的覆盖度之和，得到矫正后的G值。
矫正G值python代码如下：

```python
def G_statistics(s1_ref, s1_alt, s2_ref, s2_alt):
    total = s1_ref + s1_alt + s2_ref + s2_alt
    exp1 = (s1_ref + s2_ref) * (s1_ref + s1_alt) / total
    exp2 = (s2_ref + s1_ref) * (s2_ref + s2_alt) / total
    exp3 = (s1_alt + s1_ref) * (s1_alt + s2_alt) / total
    exp4 = (s2_alt + s1_alt) * (s2_alt + s2_ref) / total
    ### numpy.log() is same to ln()
    all_exp =  2 * (s1_ref * np.log(s1_ref/exp1) + s2_ref * np.log(s2_ref/exp2) + s1_alt * np.log(s1_alt/exp3) + s2_alt * np.log(s2_alt/exp4)) /total
    Gstat = '%.3f' % all_exp
    return Gstat
```

原检测位点得到的矫正的G值（最后一列）如下：
```
Chr     Pos     Ref     Alt     T01_depth       T02_depth       G_Stats
chr2B   233268742   G   A   1824_3073   4630_1134   0.199
chr2B   210652242   G   A   2145_3079   3883_699    0.213
chr2B   233268891   C   T   1161_2233   3054_763    0.223
chr2B   44311534    T   C   2912_3910   4807_1603   0.110
chr2B   97441940    T   G   1822_3001   3097_1011   0.147
chr2B   44311161    G   A   3125_3592   5267_1704   0.090
chr2B   44311152    G   A   3087_3513   5189_1661   0.090
```

我们将得到的所有位点的结果进行排序，结果如下：

```
$ sort -k 7nr T01_T02_Gstatistics.txt | head
Chr     Pos     Ref     Alt     T01_depth       T02_depth       G_Stats
chr2B   742466512   T   C   3_82    74_14   0.778
chr2B   666485600   A   G   1_21    12_2    0.763
chr2B   666485601   A   T   1_21    12_2    0.763
chr2B   666485599   G   A   1_20    11_2    0.734
chr2B   679031209   G   A   6_47    54_6    0.706
chr2B   690588616   A   T   1_17    20_4    0.687
chr2B   690588623   A   G   1_16    20_4    0.673
chr2B   710900233   A   C   1_12    10_2    0.657
chr2B   493251505   A   G   1_12    6_1 0.655
chr2B   741858727   A   G   4_32    32_5    0.641
```

此时较大的G值仅与两个混池中两个等位覆盖度的相对比例有关，而与总覆盖度无关。

通过将G值与snp_index进行比较，也证实了矫正后的G值更可靠。

