
## Admixture
```
(NanoSV) wuzhikun@mu01 16:25:02 O_O /home/wuzhikun/software/admixture_linux-1.3.0 
$ ./admixture --help
****                   ADMIXTURE Version 1.3.0                  ****
****                    Copyright 2008-2015                     ****
****           David Alexander, Suyash Shringarpure,            ****
****                John  Novembre, Ken Lange                   ****
****                                                            ****
****                 Please cite our paper!                     ****
****   Information at www.genetics.ucla.edu/software/admixture  ****

                                                                              
  ADMIXTURE basic usage:  (see manual for complete reference)                 
    % admixture [options] inputFile K                                         
                                                                              
  where:                                                                      
    K is the number of populations; and                                       
    inputFile may be:                                                         
      - a PLINK .bed file                                                     
      - a PLINK "12" coded .ped file                                        
                                                                              
  Output will be in files inputBasename.K.Q, inputBasename.K.P                
                                                                              
  General options:                                                            
    -jX          : do computation on X threads                                
    --seed=X     : use random seed X for initialization                       
                                                                              
  Algorithm options:                                                          
     -m=                                                                      
    --method=[em|block]     : set method.  block is default                   
                                                                              
     -a=                                                                      
    --acceleration=none   |                                                   
                   sqs<X> |                                                   
                   qn<X>      : set acceleration                              
                                                                              
  Convergence criteria:                                                       
    -C=X : set major convergence criterion (for point estimation)             
    -c=x : set minor convergence criterion (for bootstrap and CV reestimates) 
                                                                              
  Bootstrap standard errors:                                                  
    -B[X]      : do bootstrapping [with X replicates]    
```

```
$ /home/wuzhikun/software/admixture_linux-1.3.0/admixture Sample_SV_geno.ped 2
```


### ped to bed
```
$ plink --file Sample_SV_geno  --make-bed --out  Sample_SV_geno


PLINK v1.90b4 64-bit (20 Mar 2017)             www.cog-genomics.org/plink/1.9/
(C) 2005-2017 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to Sample_SV_geno.log.
Options in effect:
  --file Sample_SV_geno
  --make-bed
  --out Sample_SV_geno

128495 MB RAM detected; reserving 64247 MB for main workspace.
.ped scan complete (for binary autoconversion).
Performing single-pass .bed write (149940 variants, 20 people).
--file: Sample_SV_geno-temporary.bed + Sample_SV_geno-temporary.bim +
Sample_SV_geno-temporary.fam written.
149940 variants loaded from .bim file.
20 people (10 males, 10 females) loaded from .fam.
20 phenotype values loaded from .fam.
Using 1 thread (no multithreaded calculations invoked).
Before main variant filters, 20 founders and 0 nonfounders present.
Calculating allele frequencies... done.
Warning: 1 het. haploid genotype present (see Sample_SV_geno.hh ); many
commands treat these as missing.
Warning: Nonmissing nonmale Y chromosome genotype(s) present; many commands
treat these as missing.
149940 variants and 20 people pass filters and QC.
Among remaining phenotypes, 0 are cases and 20 are controls.
--make-bed to Sample_SV_geno.bed + Sample_SV_geno.bim + Sample_SV_geno.fam ...
done.
```


```
$ /home/wuzhikun/software/admixture_linux-1.3.0/admixture Sample_SV_geno.bed 2
****                   ADMIXTURE Version 1.3.0                  ****
****                    Copyright 2008-2015                     ****
****           David Alexander, Suyash Shringarpure,            ****
****                John  Novembre, Ken Lange                   ****
****                                                            ****
****                 Please cite our paper!                     ****
****   Information at www.genetics.ucla.edu/software/admixture  ****

Random seed: 43
Point estimation method: Block relaxation algorithm
Convergence acceleration algorithm: QuasiNewton, 3 secant conditions
Point estimation will terminate when objective function delta < 0.0001
Estimation of standard errors disabled; will compute point estimates only.
Size of G: 20x149940
Performing five EM steps to prime main algorithm
1 (EM)  Elapsed: 0.138  Loglikelihood: -1.57047e+06 (delta): 3.5611e+06
2 (EM)  Elapsed: 0.126  Loglikelihood: -1.47243e+06 (delta): 98038.3
3 (EM)  Elapsed: 0.12 Loglikelihood: -1.44967e+06 (delta): 22763.7
4 (EM)  Elapsed: 0.121  Loglikelihood: -1.43892e+06 (delta): 10745.2
5 (EM)  Elapsed: 0.121  Loglikelihood: -1.43303e+06 (delta): 5890.77
Initial loglikelihood: -1.43303e+06
Starting main algorithm
1 (QN/Block)  Elapsed: 0.636  Loglikelihood: -1.40173e+06 (delta): 31303.1
2 (QN/Block)  Elapsed: 0.633  Loglikelihood: -1.39214e+06 (delta): 9590.12
3 (QN/Block)  Elapsed: 0.711  Loglikelihood: -1.388e+06 (delta): 4139.2
4 (QN/Block)  Elapsed: 0.697  Loglikelihood: -1.38569e+06 (delta): 2308.1
5 (QN/Block)  Elapsed: 0.776  Loglikelihood: -1.38467e+06 (delta): 1023.34
6 (QN/Block)  Elapsed: 0.781  Loglikelihood: -1.38448e+06 (delta): 186.841
7 (QN/Block)  Elapsed: 0.775  Loglikelihood: -1.38447e+06 (delta): 6.96211
8 (QN/Block)  Elapsed: 0.779  Loglikelihood: -1.38447e+06 (delta): 0.0169406
9 (QN/Block)  Elapsed: 0.779  Loglikelihood: -1.38447e+06 (delta): 0
Summary: 
Converged in 9 iterations (7.639 sec)
Loglikelihood: -1384471.466895
Fst divergences between estimated populations: 
  Pop0  
Pop0  
Pop1  0.067 
Writing output files.

```


out files:
```
$ head Sample_SV_geno.2.P
0.999990 0.900000
0.900000 0.999990
0.900000 0.900000
0.999990 0.900000
0.999990 0.900000
0.999990 0.900000
0.950000 0.999990
0.950000 0.999990
0.999990 0.900000
0.999990 0.900000

```


```
$ head Sample_SV_geno.2.Q
0.000010 0.999990
0.999990 0.000010
0.000010 0.999990
0.000010 0.999990
0.999990 0.000010
0.000010 0.999990
0.999990 0.000010
0.999990 0.000010
0.000010 0.999990
0.999990 0.000010

```



### CV (cross-validation)

A good value of K will exhibit a low
cross-validation error compared to other K values. 

```
$ for K in 1 2 3 4 5; do /home/wuzhikun/software/admixture_linux-1.3.0/admixture  --cv   Sample_SV_geno.bed $K  -j8 | tee log${K}.out; done
```

get CV values
```
$ grep -h CV log*.out
CV error (K=1): 0.85701
CV error (K=2): 0.97211
CV error (K=3): 1.11213
CV error (K=4): 1.32585
CV error (K=5): 1.34502

```

