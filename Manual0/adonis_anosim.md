### adonis_results.txt
```
$ cat -A  adonis_results.txt
$
Call:$
adonis(formula = as.dist(qiime.data$distmat) ~ qiime.data$map[[opts$category]],      permutations = opts$num_permutations) $
$
Permutation: free$
Number of permutations: 999$
$
Terms added sequentially (first to last)$
$
                                Df  SumsOfSqs    MeanSqs F.Model      R2 Pr(>F)$
qiime.data$map[[opts$category]]  2 0.00144785 0.00072393  17.759 0.59676  0.001$
Residuals                       24 0.00097832 0.00004076         0.40324       $
Total                           26 0.00242617                    1.00000       $
                                   $
qiime.data$map[[opts$category]] ***$
Residuals                          $
Total                              $
---$
Signif. codes:  0 M-bM-^@M-^X***M-bM-^@M-^Y 0.001 M-bM-^@M-^X**M-bM-^@M-^Y 0.01 M-bM-^@M-^X*M-bM-^@M-^Y 0.05 M-bM-^@M-^X.M-bM-^@M-^Y 0.1 M-bM-^@M-^X M-bM-^@M-^Y 1$

```


### anosim_results.txt
```
$ cat -A anosim_results.txt
method name^IANOSIM$
test statistic name^IR$
sample size^I27$
number of groups^I3$
test statistic^I0.59068739521414415$
p-value^I0.001$
number of permutations^I999$
```

### permanova_results.txt
```
$ cat -A permanova_results.txt
method name^IPERMANOVA$
test statistic name^Ipseudo-F$
sample size^I27$
number of groups^I3$
test statistic^I17.759307716244663$
p-value^I0.001$
number of permutations^I999$
```

### mrpp_results.txt
```
$ cat -A mrpp_results.txt
$
Call:$
mrpp(dat = as.dist(qiime.data$distmat), grouping = qiime.data$map[[opts$category]],      permutations = opts$num_permutations) $
$
Dissimilarity index: $
Weights for groups:  n $
$
Class means and counts:$
$
      KO       OE       WT    $
delta 0.007943 0.009679 0.0083$
n     9        9        9     $
$
Chance corrected within-group agreement A: 0.3088 $
Based on observed delta 0.008641 and expected delta 0.0125 $
$
Significance of delta: 0.001 $
Permutation: free$
Number of permutations: 999$
$
```

### dbrda_results.txt
```
$ cat -A dbrda_results.txt
Call: capscale(formula = as.dist(qiime.data$distmat) ~ factor, data =$
factors.frame)$
$
                 Inertia Proportion Rank$
Total          2.426e-03                $
Real Total     2.512e-03  1.000e+00     $
Constrained    1.453e-03  5.786e-01    2$
Unconstrained  1.059e-03  4.214e-01   19$
Imaginary     -8.582e-05               7$
Inertia is squared Unknown distance $
$
Eigenvalues for constrained axes:$
     CAP1      CAP2 $
0.0014125 0.0000409 $
$
Eigenvalues for unconstrained axes:$
     MDS1      MDS2      MDS3      MDS4      MDS5      MDS6      MDS7      MDS8 $
0.0004471 0.0001206 0.0001080 0.0000671 0.0000588 0.0000454 0.0000438 0.0000378 $
(Showed only 8 of all 19 unconstrained eigenvalues)$
$
$
Permutation test for capscale $
$
Permutation: free$
Number of permutations: 999$
 $
Call: capscale(formula = as.dist(qiime.data$distmat) ~ factor, data =$
factors.frame)$
Permutation test for all constrained eigenvalues$
Pseudo-F:^I 16.47399 (with 2, 24 Degrees of Freedom)$
Significance:^I 0.001 $
$
```