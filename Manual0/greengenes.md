## greengenes database

### greengenes_release 13.8

~/database/greengenes_release/gg_13_5/gg_13_8_otus/taxonomy
```
$ cut -f 1 97_otu_taxonomy.txt | sort | uniq | wc -l 
99322


$ cut -f 2 97_otu_taxonomy.txt | sort | uniq | wc -l 
4163


$ cut -f 2 97_otu_taxonomy.txt | sort | uniq -c | sort -k 1nr | head 
   4816 k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__; g__; s__
   3608 k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__; s__
   3053 k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__; s__
   2290 k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__; g__; s__
    969 k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__S24-7; g__; s__
    867 k__Bacteria; p__Proteobacteria; c__Alphaproteobacteria; o__Rhodobacterales; f__Rhodobacteraceae; g__; s__
    832 k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Prevotellaceae; g__Prevotella; s__
    791 k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
    704 k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__
    687 k__Bacteria; p__Proteobacteria; c__Alphaproteobacteria; o__Rhodospirillales; f__Rhodospirillaceae; g__; s__



$ grep 'k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__' 97_otu_taxonomy.txt | head

201026  k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
159621  k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
1662279 k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
278103  k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
151305  k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
711791  k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
154875  k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
556971  k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
4374562 k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__
1820255 k__Bacteria; p__Planctomycetes; c__Planctomycetia; o__Pirellulales; f__Pirellulaceae; g__; s__



1 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__
7 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
59 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Nitrosopumilus; s__
13 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Nitrosopumilus; s__pIVWA5


$ grep 'k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum' 97_otu_taxonomy.txt
155495  k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
155684  k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
1129716 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
36985   k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
238620  k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
1029    k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
4466258 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum


$ grep 'k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum' 99_otu_taxonomy.txt
31020   k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
155684  k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
1138988 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
153762  k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
36985   k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
1029    k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
1136866 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
155495  k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
1124628 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
1129716 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
69639   k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
4466258 k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum
238620  k__Archaea; p__Crenarchaeota; c__Thaumarchaeota; o__Cenarchaeales; f__Cenarchaeaceae; g__Cenarchaeum; s__symbiosum

```


```
$ cut -f 2 99_otu_taxonomy.txt | sort | uniq | wc -l 
5405
```


```
>>> f['155495'][:]
>155495
GATCCTGGCGGACCTGACTGCTATCGGATTGATACTAAGCCATGCGAGTCATTGCAGCAATGCAAGGCAGACGGCTCAGTAACGCGTAGTCAACCTAACCTATGGACGGGAATAACCTCGGGAAACTGAGAATAATGCCCGATAGAACACTATGCCTGGAATGGTTTATGGTCAAAATGATTTATCGCCATAGGATGGGACTGCGGTCTATCAGCTTGTTGGTGAGGTAATGGCCCACCAAGGCTATAACAGATACGGGCTCTGAGAGGAGAAGCCCGGAGATGGGTACTGAGACACGGACCCAGGTCCTATGGGGCGCAGCAGGCGAGAAAACTTTGCAATGTGCGAAAGCACGACAAGGTTAATCCGAGTGTTCTCTGCTAAAGAGATCTTTTGCCGGTCCTAAAAGCACCGGTGAATAAGGGGTGGGCAAGTTCTGGTGTCAGCCGCCGCGGTAAAACCAGCACCTCAAGTGGTCAGGAGGATTATTGGGCCTAAAGCATCCGTAGCCGGCTGTATAAGTTCTCGGTTAAATCTATGTGCTCAACACATAGGCTGCCGGGAATACTGTACAGCTAGGGAGTGGGAGAGGTAGACGGTACTTGGTAGGAAGGGGTAAAATCCTTTGATCTATTGATGACCACCTGTGGCGAAGGCGGTCTACTAGAACACGTCCGACGGTGAGGGATGAAAGCTGGGGGAGCAAACCGGATTAGATACCCGGGTAGTCCCAGCTGTAAACAATGCAAACTCAGTGATGCATTGGCTTGTGGCCAGTGCAGTGCCGCAGGGAAGCCGTTAAGTTTGCCGCCTGGGAAGTACGTACGCAAGTATGAAACTTAAAGGAATTGGCGGGGGAGCACCACAAGGGGTGAAGCCTGCGGTTCAATTGGAGTCAACGCCAGAAATCTTACCCGGAGAGACAGCAGAATGAAGGTCAAGCTGAAGACTTTACCAGACAAGCTGAGAGGTGGTGCATGGCCGTCGCCAGCTCGTGCCGTGAGATGTCCTGTTAAGTCAGGTAACGAGCGAGATCCTTGCCTCTAGTTGCCACCATTACTCCCCGGAGTAATGGGGCGAATTAGCGGGACTGCCGCAGTTAATGCGGAGGAAGGAGAGGGCTACGGCAGGTCAGTATGCCCCGAAACTCTGGGGCCACACGCGGGCTGCAATGGTAGTGACAATGGGTTCTAAATCCGAAAGGAGGAGGTAATCCCCAAACGCTACCACAGTTATGACTGAGGGCTGCAACTCGCCCTCACGAATATGGAATCCCTAGTAACCGCGTGTCATTATCGCGCAGTGAATACGTCCCTGCTCCTTGCACACACCG
```