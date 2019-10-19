## Eigenstrat


### input file

```
$ head  example.geno
11100
01212
21101
00122
21100
00111
22110


$ head  example.ind
             SAMPLE0 F       Case
             SAMPLE1 M       Case
             SAMPLE2 F    Control
             SAMPLE3 M    Control
             SAMPLE4 F    Control


$ head  example.snp
              rs0000  11        0.000000               0 A C
              rs1111  11        0.001000          100000 A G
              rs2222  11        0.002000          200000 A T
              rs3333  11        0.003000          300000 C A
              rs4444  11        0.004000          400000 G A
              rs5555  11        0.005000          500000 T A
              rs6666  11        0.006000          600000 G T

```



### run eigenstrat

```
$ perl /home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/smartpca.perl -i /home/wuzhikun/Project/NanoTrio/population/eigenstrat/Sample_SV.geno -a /home/wuzhikun/Project/NanoTrio/population/eigenstrat/Sample_SV.snp -b /home/wuzhikun/Project/NanoTrio/population/eigenstrat/Sample_SV.ind -k 10 -o example.pca -p example.plot -e example.eval -l example.log

smartpca -p example.pca.par >example.log
sh: smartpca: command not found
OOPS couldn't open file example.pca.evec for reading at /home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/smartpca.perl line 65.


```


```
$ cat  example.pca.par
genotypename: example.geno
snpname: example.snp
indivname: example.ind
evecoutname: example.pca.evec
evaloutname: example.eval
altnormstyle: NO
numoutevec: 2
numoutlieriter: 5
numoutlierevec: 2
outliersigmathresh: 6.0
qtmode: 0

```


#### Solution

```
$ sed -n '58p' /home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/smartpca.perl
$command = "smartpca";          # MUST put bin directory in path
(WGS) wuzhikun@fat02 20:18:53 ^_^ /home/wuzhikun/Project/NanoTrio/population 
$ sed -n '94p' /home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/smartpca.perl
$command = "ploteig";           # MUST put bin directory in path
(WGS) wuzhikun@fat02 20:19:46 ^_^ /home/wuzhikun/Project/NanoTrio/population 
$ sed -n '110p' /home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/smartpca.perl
  $command = "evec2pca-ped.perl $k $evec $b $o";
(WGS) wuzhikun@fat02 20:19:57 ^_^ /home/wuzhikun/Project/NanoTrio/population 
$ sed -n '113p' /home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/smartpca.perl
  $command = "evec2pca.perl $k $evec $b $o";

```


#### run eigenstrat

```
$ perl /home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/smartpca.perl -i /home/wuzhikun/Project/NanoTrio/population/eigenstrat/Sample_SV.geno -a /home/wuzhikun/Project/NanoTrio/population/eigenstrat/Sample_SV.snp -b /home/wuzhikun/Project/NanoTrio/population/eigenstrat/Sample_SV.ind -k 10 -o example.pca -p example.plot -e example.eval -l example.log
/home/wuzhikun/software/Eigensoft/EIG-7.2.1/src/eigensrc/smartpca -p example.pca.par >example.log
ploteig -i example.pca.evec -c 1:2  -p Control  -x  -y  -o example.plot.xtxt 
/home/wuzhikun/software/Eigensoft/EIG-7.2.1/bin/evec2pca.perl 10 example.pca.evec /home/wuzhikun/Project/NanoTrio/population/eigenstrat/Sample_SV.ind example.pca

```


output files:
```
$ head  example.eval
    3.006290
    1.819095
    1.264904
    1.197829
    1.130952
    0.885859
    0.868944
    0.812497
    0.798916
    0.792184


$ head example.pca
10
3.0060
1.8190
1.2650
1.1980
1.1310
0.8860
0.8690
0.8120
0.7990

```

