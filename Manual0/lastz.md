## lastz

### install lastz
```
$ conda install -c bioconda lastz
```

### [lastz manual](http://www.bx.psu.edu/miller_lab/dist/README.lastz-1.02.00/README.lastz-1.02.00a.html#ex_self)

### run lastz 
```
$ lastz ERR2173372_partial.fasta ERR2173372_partial.fasta  --step=10 --seed=match12 --notransition --exact=20 --noytrim --match=1,5 --ambiguous=n --coverage=90 --identity=95 --format=general:name1,start1,end1,length1,strand1,name2,start2,end2,length2,strand2  > lastz_out.txt

$ lastz ERR2173372_partial.fasta ERR2173372_partial.fasta  --step=10 --seed=match12 --notransition --exact=20 --noytrim --match=1,5 --ambiguous=n --coverage=90 --identity=95 --format=maf > lastz_out.maf
```


