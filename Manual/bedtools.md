## bedtools

### intersect

```
bedtools intersect -a /home/wuzhikun/Project/NanoTrio/IGV/Sniffles/M671_denovo_SV_proband_Sniffles.bed -b /home/wuzhikun/database/FANTOM5/hg38_fair+new_CAGE_peaks_phase1and2_dechr.bed   -wa -wb > temp

```


outfile:
```
1 198506695 198517930 1_198506695_198517930_INS 1 198510307 198510705 chr1:198510307-198510705  2 . 198510505 198510506 0,0,0 2  1
,1  0,3971  198506695 198517930 1_198506695_198517930_INS 1 198515561 198515887 chr1:198515561-198515887  5 . 198515613 198515614 0,0,0 2  1
,222  0,10414 38493108  38497066  14_38493108_38497066_DEL  14  38496557  38496848  chr14:38496557-38496848 10  . 38496702  38496703  0,0,0 2 1,10
,29
```

### merge
```
sort -k1,1 -k2,2n foo.bed > foo.sort.bed
bedtools merge -i foo.sort.bed | head -n 20
```

out file:
```
bedtools merge -i exons.bed -c 1 -o count | head -n 20
chr1    11873   12227   1
chr1    12612   12721   1
chr1    13220   14829   2
chr1    14969   15038   1
chr1    15795   15947   1
```
