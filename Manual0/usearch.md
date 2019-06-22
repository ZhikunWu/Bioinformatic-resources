## usearch

### normalization for OTU abundance
```
$ usearch -otutab_norm otu_table.txt -sample_size 10000 -output otutab10k.txt
```

```
$ head otu_table.txt
#OTU ID A1-1    A1-2    A1-4    A2-1    A2-2    A2-4    A3-1    A3-2    A3-4    A4-1    A4-2    A4-4    B1-1    B1-2    B1-4   B2-1 B2-2    B2-4    B3-1    B3-2    B3-4    B4-1    B4-2    B4-4    D1-1    D1-2    D1-4    D2-1    D2-2    D2-4    D3-1   D3-2 D3-4    D4-1    D4-2    D4-4
OTU_1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      361  163 29  291 132 0   0   65
OTU_10  14  10  3   1   8   8   20  10  8   3   78  4   5   10  7      28   34  3   5   5   1   19  139 39  0   10  8   5   5   1   14     23   28  0   5   0
OTU_100 4   6   3   3   6   2   18  6   4   4   3   0   40  19  7      35   1   6   7   3   1   3   5   1   33  13  0   18  2   19  0      17
OTU_1000    2   32  3   6   20  0   0   0   6   0   0   4   0   4      21   0   1   0   9   0   18  0   0   0   1   0   21  0   0   18     17   0   0
OTU_1001    3   0   0   0   0   0   33  0   0   3   0   1   0   0      32   0   0   1   0   0   0   0   0   0   5   0   0   0   0
OTU_1002    0   6   0   0   0   16  0   0   10  0   7   5   0   0      23   0   0   0
OTU_1003    4   0   12  0   5   48  6   1   1   8   24  0   0   1      67   0   4   1   0   29  42  0   2   2   2   1   1   3   4   12     2
OTU_1004    0   0   0   0   0   8   2   0   0   0   0   0   0   28     0
OTU_1005    5   1   0   2   6   3   5   0   1   0   0   4   7   4      10   1   1   7   2   6   0   0   0   3   0   2   6   3   23  0      
```

```
$ head otutab10k.txt
#OTU ID A1-1    A1-2    A1-4    A2-1    A2-2    A2-4    A3-1    A3-2    A3-4    A4-1    A4-2    A4-4    B1-1    B1-2    B1-4   B2-1 B2-2    B2-4    B3-1    B3-2    B3-4    B4-1    B4-2    B4-4    D1-1    D1-2    D1-4    D2-1    D2-2    D2-4    D3-1   D3-2 D3-4    D4-1    D4-2    D4-4
OTU_1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0      57   30  5   61  21  0   0   15
OTU_10  3   2   1   0   1   1   4   2   2   1   12  1   1   2   1      25   7   0   2   2   1   1   0   2   5   4   0   1   0
OTU_100 1   1   1   1   1   0   4   1   1   1   0   0   8   3   1      4
OTU_1000    0   6   1   1   4   0   0   0   1   0   0   1   0   1      0
OTU_1001    1   0   0   0   0   0   7   0   0   1   0   0   0   0      0
OTU_1002    0   1   0   0   0   3   0   0   2   0   1   1   0   0      0
OTU_1003    1   0   2   0   1   8   1   0   0   2   4   0   0   0      15   0   1   0   0   5   7   0   0   0   0   0   0   0   1   2      0
OTU_1004    0   0   0   0   0   1   0   0   0   0   0   0   0   5      0
OTU_1005    1   0   0   0   1   0   1   0   0   0   0   1   1   1      
```


### compare for two files
我们统计一下抽样前后的比较

```
$ usearch -otutab_stats otu_table.txt -output otutab.stat

```


```
$ cat  otutab.stat
   1917290  Reads (1.9M)
        36  Samples
      1536  OTUs

     55296  Counts
     26868  Count  =0  (48.6%)
      5356  Count  =1  (9.7%)
     11999  Count >=10 (21.7%)

        99  OTUs found in all samples (6.4%)
       240  OTUs found in 90% of samples (15.6%)
       787  OTUs found in 50% of samples (51.2%)

Sample sizes: min 43066, lo 47821, med 52869, mean 53258.1, hi 60139, max 64197
```



