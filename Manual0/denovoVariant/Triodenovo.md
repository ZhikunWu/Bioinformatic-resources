## [Triodenovo](https://genome.sph.umich.edu/wiki/Triodenovo)

### install triodenovo
```
$ tar -zxf Triodenovo.0.06.tar.gz
$ cd triodenovo.0.06/
$ make
```



```
$ ln -s /home/wuzhikun/anaconda3/envs/WGS/bin/triodenovo.0.06/bin/triodenovo /home/wuzhikun/anaconda3/envs/WGS/bin/triodenovo
```


### triodenovo parameters
```
$ triodenovo

   *** This build (v.0.06) was compiled on Mar 26 2019, 17:36:28 ***

The following parameters are in effect:
                    Input files : --ped [], --in_vcf []
                   Output files : --out_vcf []
           Denovo mutation rate : --mu [1.0e-07]
           Scaled mutation rate : --theta [1.0e-03], --indel_theta [1.0e-04]
   Prior of de novo ts/tv ratio : --denovo_tstv [2.00]
            Non-autosome labels : --chrX [X]
                        Filters : --minDQ [5.00], --minTotalDepth,
                                  --maxTotalDepth, --minDepth [5], --maxDepth,
                                  --mixed_vcf_records [ON]


FATAL ERROR - 
Input and output VCF files are the same!
```



### run triodenovo

First you shold hava the ped file:
```
$ cat ../M625.ped
M625	M625-0	M625-1	M625-2	0	2
M625	M625-1	0	0	1	1
M625	M625-2	0	0	2	1
```


Run triodenovo
```
./triodenovo --ped ../example/trio.denovo.ped --in_vcf ../example/trio.denovo.vcf  --out_vcf ../example/test.denovo.out.vcf

   *** This build (v.0.06) was compiled on Mar 26 2019, 17:36:28 ***

The following parameters are in effect:
                    Input files : --ped [../example/trio.denovo.ped],
                                  --in_vcf [../example/trio.denovo.vcf]
                   Output files : --out_vcf [../example/test.denovo.out.vcf]
           Denovo mutation rate : --mu [1.0e-07]
           Scaled mutation rate : --theta [1.0e-03], --indel_theta [1.0e-04]
   Prior of de novo ts/tv ratio : --denovo_tstv [2.00]
            Non-autosome labels : --chrX [X]
                        Filters : --minDQ [5.00], --minTotalDepth,
                                  --maxTotalDepth, --minDepth [5], --maxDepth,
                                  --mixed_vcf_records [ON]

Total samples in both VCF and PED files: 3

make[1]: Leaving directory `/home/wuzhikun/anaconda3/envs/WGS/bin/triodenovo.0.06/src'
Compiling finished successfully.\n
Type ./bin/triodenovo to invoke the command and see the command line options.\n

```



#### output details

input file
```
$ grep 1009955 M625_10.vcf
10	1009955	.	T	A	3829.13	.	AC=5;AF=0.833;AN=6;BaseQRankSum=-8.460e-01;ClippingRankSum=0.00;DP=88;ExcessHet=3.0103;FS=0.000;MLEAC=5;MLEAF=0.833;MQ=60.11;MQRankSum=0.00;QD=31.50;ReadPosRankSum=-1.041e+00;SOR=0.297	GT:AD:DP:GQ:PGT:PID:PL	0/1:1,24:25:85:0|1:1009926_A_T:1092,0,85	1/1:0,20:20:60:1|1:1009926_A_T:900,60,0	1/1:0,41:41:99:1|1:1009924_G_T:1868,126,0
```


output file
```
$ grep 1009955 M625_10_denovo.vcf
10	1009955	.	T	A	3829.13	.	DP=86	GT:DQ:DGQ:DP:PL	A/A:5.69:100:20:900,60,0	A/A:5.69:100:41:1868,126,0	A/T:5.69:100:25:1092,0,85

```



### Filt data
```
$ less M625_10_denovo.vcf  | egrep "DQ|#" | perl -lane 'print if /#/; next if length($F[3])>1 || length($F[4])>1 || $F[4]=~/,/; next if $F[5]<30; $F[9] =~ /([A-Z])\/([A-Z])/; next if $1 ne $2; next if $F[10] !~ /$1\/$1/; $F[11]=~/([A-Z])\/([A-Z])/; next if $1 eq $2; $F[11] =~ /(\d+),(\d+),(\d+)/; next if $2 != 0 || $1<30 || $3<30; print' | less

```

