### [Distance-based Redundancy Analysis](https://rdrr.io/cran/vegan/man/capscale.html)
### [用ggvegan包进行db-RDA微生物环境因子分析](用ggvegan包进行db-RDA微生物环境因子分析)
### [sRDA](https://github.com/acsala/sRDA): Sparse Redundancy Analysis for high dimensional (biomedical) data
### ['ggplot2' Plots for the 'vegan' Package](https://www.rdocumentation.org/packages/ggvegan/versions/0.0-9)

```R
> library(vegan)
Loading required package: permute
Loading required package: lattice
This is vegan 2.4-3
Warning message:
In fun(libname, pkgname) :
  Package “nlme” installed with old R version 3.2.3 should not be used with R version 3.3.2
  Rather re-install it with this version of R.

> otu.tab <- read.csv("otutab.txt", row.names = 1, header=T, sep="\t")
> env.data <- read.csv("new_meta.txt", row.names = 1, fill = T, header=T, sep="\t")
> otu <- t(otu.tab)
> env.data.log <- log1p(env.data)
> env <- na.omit(env.data.log)
> otu.hell <- decostand(otu, "hellinger")
> sel <- decorana(otu.hell)
> sel

Call:
decorana(veg = otu.hell) 

Detrended correspondence analysis with 26 segments.
Rescaling of axes with 4 iterations.

                   DCA1    DCA2     DCA3     DCA4
Eigenvalues     0.03080 0.01437 0.009782 0.010397
Decorana values 0.03114 0.01356 0.009399 0.007405
Axis lengths    0.63859 0.48214 0.484781 0.450656

> otu.tab.0 <- rda(otu.hell ~ 1, env)
> otu.tab.0
Call: rda(formula = otu.hell ~ 1, data = env)

              Inertia Rank
Total         0.06949     
Unconstrained 0.06949   17
Inertia is variance 

Eigenvalues for unconstrained axes:
     PC1      PC2      PC3      PC4      PC5      PC6      PC7      PC8 
0.017525 0.008406 0.005754 0.005232 0.004463 0.004338 0.003433 0.003229 
(Showed only 8 of all 17 unconstrained eigenvalues)

> otu.tab.1<- rda(otu.hell ~ ., env)
> otu.tab.1
Call: rda(formula = otu.hell ~ N + P + K + Ca + Mg + S + Al + Fe + Mn +
Zn + Mo + pH, data = env)

              Inertia Proportion Rank
Total         0.06949    1.00000     
Constrained   0.05047    0.72629   12
Unconstrained 0.01902    0.27371    5
Inertia is variance 

Eigenvalues for constrained axes:
    RDA1     RDA2     RDA3     RDA4     RDA5     RDA6     RDA7     RDA8 
0.013965 0.006622 0.005498 0.004640 0.004182 0.003284 0.003046 0.002338 
    RDA9    RDA10    RDA11    RDA12 
0.002058 0.001706 0.001654 0.001478 

Eigenvalues for unconstrained axes:
     PC1      PC2      PC3      PC4      PC5 
0.007350 0.003965 0.003136 0.002492 0.002078 

> vif.cca(otu.tab.1)
         N          P          K         Ca         Mg          S         Al 
  1.884364  12.841264  65.736392  43.429669  30.265501 191.395325  55.272552 
        Fe         Mn         Zn         Mo         pH 
 17.273946  15.175988   4.566956  19.005296   4.844339 
> otu.tab.1 <- rda(otu.hell ~ N+P+K+Ca+Mg+pH+Al+Fe+Mn+Zn+Mo, env.data.log)
> vif.cca(otu.tab.1)
        N         P         K        Ca        Mg        pH        Al        Fe 
 1.873607 10.392774 14.394371 43.381951 13.355345  4.840044 31.794251 16.073678 
       Mn        Zn        Mo 
12.190179  4.441104 15.466885 
> otu.tab.1 <- rda(otu.hell ~ N+P+K+Mg+pH+Al+Fe+Mn+Zn+Mo, env.data.log)
> vif.cca(otu.tab.1)
        N         P         K        Mg        pH        Al        Fe        Mn 
 1.841487 10.310605 14.272564  4.205915  4.534061 27.787706 14.268419  9.445083 
       Zn        Mo 
 3.954073  8.112553 
> otu.tab.1 <- rda(otu.hell ~ N+P+K+Mg+pH+Fe+Mn+Zn+Mo, env.data.log)
> vif.cca(otu.tab.1)
       N        P        K       Mg       pH       Fe       Mn       Zn 
1.688095 7.981366 9.111230 3.883939 4.528069 5.402742 6.256847 3.520125 
      Mo 
5.596306 
> 
>
> mod.u <- step(otu.tab.0, scope = formula(otu.tab.1), test = "perm")
Start:  AIC=-47.03
otu.hell ~ 1


       Df     AIC      F Pr(>F)  
+ Mg    1 -47.215 2.0680  0.030 *
<none>    -47.027                
+ N     1 -46.717 1.5749  0.065 .
+ pH    1 -46.422 1.2893  0.170  
+ K     1 -46.243 1.1183  0.245  
+ P     1 -46.204 1.0818  0.305  
+ Mn    1 -46.157 1.0370  0.330  
+ Zn    1 -46.110 0.9928  0.410  
+ Mo    1 -45.836 0.7358  0.750  
+ Fe    1 -45.700 0.6098  0.950  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Step:  AIC=-47.21
otu.hell ~ Mg

       Df     AIC      F Pr(>F)   
<none>    -47.215                 
+ K     1 -47.066 1.6248  0.050 * 
- Mg    1 -47.027 2.0680  0.010 **
+ N     1 -46.771 1.3543  0.095 . 
+ Mn    1 -46.618 1.2159  0.190   
+ pH    1 -46.572 1.1749  0.245   
+ Zn    1 -46.367 0.9920  0.400   
+ Mo    1 -46.171 0.8189  0.680   
+ Fe    1 -46.047 0.7096  0.840   
+ P     1 -45.980 0.6512  0.930   
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1


> mod.d <- step(otu.tab.0, scope = (list(lower = formula(otu.tab.0), upper = formula(otu.tab.1Start:  AIC=-47.03
otu.hell ~ 1

       Df     AIC
+ Mg    1 -47.215
<none>    -47.027
+ N     1 -46.717
+ pH    1 -46.422
+ K     1 -46.243
+ P     1 -46.204
+ Mn    1 -46.157
+ Zn    1 -46.110
+ Mo    1 -45.836
+ Fe    1 -45.700

Step:  AIC=-47.21
otu.hell ~ Mg

       Df     AIC
<none>    -47.215
+ K     1 -47.066
- Mg    1 -47.027
+ N     1 -46.771
+ Mn    1 -46.618
+ pH    1 -46.572
+ Zn    1 -46.367
+ Mo    1 -46.171
+ Fe    1 -46.047
+ P     1 -45.980



> mod.d
Call: rda(formula = otu.hell ~ Mg, data = env)

               Inertia Proportion Rank
Total         0.069492   1.000000     
Constrained   0.007954   0.114459    1
Unconstrained 0.061538   0.885541   16
Inertia is variance 

Eigenvalues for constrained axes:
    RDA1 
0.007954 

Eigenvalues for unconstrained axes:
     PC1      PC2      PC3      PC4      PC5      PC6      PC7      PC8 
0.014116 0.007499 0.005530 0.005173 0.004360 0.003714 0.003247 0.003000 
     PC9     PC10     PC11     PC12     PC13     PC14     PC15     PC16 
0.002512 0.002411 0.002088 0.001829 0.001645 0.001608 0.001450 0.001355 



> otu.rda.f <- rda(otu.hell ~ N+P+K+Mg+pH+Fe+Mn+Zn+Mo, env)
> 
> 
> anova(otu.rda.f)
Permutation test for rda under reduced model
Permutation: free
Number of permutations: 999

Model: rda(formula = otu.hell ~ N + P + K + Mg + pH + Fe + Mn + Zn + Mo, data = env)
         Df Variance     F Pr(>F)  
Model     9 0.041038 1.282  0.068 .
Residual  8 0.028454               
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
> anova(otu.rda.f, by = "term")
Permutation test for rda under reduced model
Terms added sequentially (first to last)
Permutation: free
Number of permutations: 999

Model: rda(formula = otu.hell ~ N + P + K + Mg + pH + Fe + Mn + Zn + Mo, data = env)
         Df  Variance      F Pr(>F)  
N         1 0.0062274 1.7509  0.044 *
P         1 0.0040558 1.1403  0.269  
K         1 0.0037937 1.0666  0.326  
Mg        1 0.0077251 2.1720  0.015 *
pH        1 0.0033237 0.9345  0.496  
Fe        1 0.0033545 0.9431  0.499  
Mn        1 0.0044936 1.2634  0.173  
Zn        1 0.0034465 0.9690  0.478  
Mo        1 0.0046177 1.2983  0.167  
Residual  8 0.0284540                
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
> anova(otu.rda.f, by = "axis")
Permutation test for rda under reduced model
Marginal tests for axes
Permutation: free
Number of permutations: 999

Model: rda(formula = otu.hell ~ N + P + K + Mg + pH + Fe + Mn + Zn + Mo, data = env)
         Df  Variance      F Pr(>F)   
RDA1      1 0.0137649 3.8701  0.009 **
RDA2      1 0.0062371 1.7536  0.068 . 
RDA3      1 0.0047516 1.3359  0.198   
RDA4      1 0.0040140 1.1286  0.366   
RDA5      1 0.0034140 0.9599  0.481   
RDA6      1 0.0030849 0.8673  0.584   
RDA7      1 0.0021580 0.6067  0.840   
RDA8      1 0.0019272 0.5418  0.883   
RDA9      1 0.0016863 0.4741  0.922   
Residual  8 0.0284540                 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1


```


### install  ggvegan
```
> devtools::install_git("https://github.com/gavinsimpson/ggvegan.git",  branch = "master")
Downloading git repo https://github.com/gavinsimpson/ggvegan.git
Installing ggvegan

'/home/wzk/anaconda3/envs/qiime/lib/R/bin/R' --no-site-file --no-environ  \
  --no-save --no-restore --quiet CMD INSTALL  \
  '/tmp/RtmpMlK8YJ/filefe0cf1a25b9' --library='/usr/lib/R/library'  \
  --install-tests 

Error: ERROR: no permission to install to directory ‘/usr/lib/R/library’
Error: Command failed (1)
```



### test data
```
> head(varespec)
   Callvulg Empenigr Rhodtome Vaccmyrt Vaccviti Pinusylv Descflex Betupube
18     0.55    11.13     0.00     0.00    17.80     0.07     0.00        0
15     0.67     0.17     0.00     0.35    12.13     0.12     0.00        0
24     0.10     1.55     0.00     0.00    13.47     0.25     0.00        0
27     0.00    15.13     2.42     5.92    15.97     0.00     3.70        0
23     0.00    12.68     0.00     0.00    23.73     0.03     0.00        0
19     0.00     8.92     0.00     2.42    10.28     0.12     0.02        0
   Vacculig Diphcomp Dicrsp Dicrfusc Dicrpoly Hylosple Pleuschr Polypili
18     1.60     2.07   0.00     1.62     0.00      0.0     4.67     0.02
15     0.00     0.00   0.33    10.92     0.02      0.0    37.75     0.02
24     0.00     0.00  23.43     0.00     1.68      0.0    32.92     0.00
27     1.12     0.00   0.00     3.63     0.00      6.7    58.07     0.00
23     0.00     0.00   0.00     3.42     0.02      0.0    19.42     0.02
19     0.00     0.00   0.00     0.32     0.02      0.0    21.03     0.02
   Polyjuni Polycomm Pohlnuta Ptilcili Barbhatc Cladarbu Cladrang Cladstel
18     0.13     0.00     0.13     0.12     0.00    21.73    21.47     3.50
15     0.23     0.00     0.03     0.02     0.00    12.05     8.13     0.18
24     0.23     0.00     0.32     0.03     0.00     3.58     5.52     0.07
27     0.00     0.13     0.02     0.08     0.08     1.42     7.63     2.55
23     2.12     0.00     0.17     1.80     0.02     9.08     9.22     0.05
19     1.58     0.18     0.07     0.27     0.02     7.23     4.95    22.08
   Cladunci Cladcocc Cladcorn Cladgrac Cladfimb Cladcris Cladchlo Cladbotr
18     0.30     0.18     0.23     0.25     0.25     0.23     0.00     0.00
15     2.65     0.13     0.18     0.23     0.25     1.23     0.00     0.00
24     8.93     0.00     0.20     0.48     0.00     0.07     0.10     0.02
27     0.15     0.00     0.38     0.12     0.10     0.03     0.00     0.02
23     0.73     0.08     1.42     0.50     0.17     1.78     0.05     0.05
19     0.25     0.10     0.25     0.18     0.10     0.12     0.05     0.02
   Cladamau Cladsp Cetreric Cetrisla Flavniva Nepharct Stersp Peltapht Icmaeric
18     0.08   0.02     0.02     0.00     0.12     0.02   0.62     0.02        0
15     0.00   0.00     0.15     0.03     0.00     0.00   0.85     0.00        0
24     0.00   0.00     0.78     0.12     0.00     0.00   0.03     0.00        0
27     0.00   0.02     0.00     0.00     0.00     0.00   0.00     0.07        0
23     0.00   0.00     0.00     0.00     0.02     0.00   1.58     0.33        0
19     0.00   0.00     0.00     0.00     0.02     0.00   0.28     0.00        0
   Cladcerv Claddefo Cladphyl
18        0     0.25        0
15        0     1.00        0
24        0     0.33        0
27        0     0.15        0
23        0     1.97        0
19        0     0.37        0
```

```
> head(varechem)
      N    P     K    Ca    Mg    S    Al   Fe    Mn   Zn  Mo Baresoil Humdepth
18 19.8 42.1 139.9 519.4  90.0 32.3  39.0 40.9  58.1  4.5 0.3     43.9      2.2
15 13.4 39.1 167.3 356.7  70.7 35.2  88.1 39.0  52.4  5.4 0.3     23.6      2.2
24 20.2 67.7 207.1 973.3 209.1 58.1 138.0 35.4  32.1 16.8 0.8     21.2      2.0
27 20.6 60.8 233.7 834.0 127.2 40.7  15.4  4.4 132.0 10.7 0.2     18.7      2.9
23 23.8 54.5 180.6 777.0 125.8 39.5  24.2  3.0  50.1  6.6 0.3     46.0      3.0
19 22.8 40.9 171.4 691.8 151.4 40.8 104.8 17.6  43.6  9.1 0.4     40.5      3.8
    pH
18 2.7
15 2.8
24 3.0
27 2.8
23 2.7
19 2.7
```

```
> vare.cap <- capscale(varespec ~ N + P + K + Condition(Al), varechem, dist="bray")
> vare.cap
Call: capscale(formula = varespec ~ N + P + K + Condition(Al), data =
varechem, distance = "bray")

              Inertia Proportion Eigenvals Rank
Total          4.5444     1.0000    4.8034     
Conditional    0.9726     0.2140    0.9772    1
Constrained    0.9731     0.2141    0.9972    3
Unconstrained  2.5987     0.5718    2.8290   15
Imaginary                          -0.2590    8
Inertia is squared Bray distance 

Eigenvalues for constrained axes:
  CAP1   CAP2   CAP3 
0.5413 0.3265 0.1293 

Eigenvalues for unconstrained axes:
  MDS1   MDS2   MDS3   MDS4   MDS5   MDS6   MDS7   MDS8   MDS9  MDS10  MDS11 
0.9065 0.5127 0.3379 0.2626 0.2032 0.1618 0.1242 0.0856 0.0689 0.0583 0.0501 
 MDS12  MDS13  MDS14  MDS15 
0.0277 0.0208 0.0073 0.0013



> anova(vare.cap)
Permutation test for capscale under reduced model
Permutation: free
Number of permutations: 999

Model: capscale(formula = varespec ~ N + P + K + Condition(Al), data = varechem, distance = "bray")
         Df SumOfSqs      F Pr(>F)   
Model     3  0.97314 2.3717  0.007 **
Residual 19  2.59866                 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1


```