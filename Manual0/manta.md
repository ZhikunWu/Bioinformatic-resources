

INFO列详解:

* END：SV的结束位置；
* SVTYPE：SV类型；“DEL”（deletion）或“BND​”（translocation）
* SVLEN：SV长度​；该长度与REF和ALT的长度差一致；也与POS和END的位置信息一致；
* GIGAR：SV的gigar值；
* SOMATIC：指示该variant是somatic variant；
* SOMATICSCORE：该somatic variant的得分；
* MATEID：与该variant对应的断点ID；当SVTYPE=“BND”时，有该值；
* CIPOS：confidence interval around POS；
* HOMELEN：Length of base pair identical homology at event breakpoints​
* HOMSEQ：Sequence of base pair identical homology at event breakpoints
* BND_DEPTH：支持该BND的Reads数；
* MATE_BND_DEPTH：支持mateBND的Reads数。

