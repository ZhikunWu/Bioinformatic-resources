## [novoCaller](https://github.com/bgm-cwg/novoCaller)

### install
```
git clone https://github.com/bgm-cwg/novoCaller.git
cd novoCaller
g++ novoCaller.cpp -o novoCaller
```

### parameters
```
$ novoCaller --help
infilename=
trio_ID_filename=
outfilename=
X_choice=
PP_thresh=2.1417e-317
ExAC_thresh=0

```

### run novoCaller
```
./novoCaller \
-I <path to vcf file> \
-O <path to output file for layer 1> \
-T <path to file containing sample IDs of the trios, the IDs are in the order:parent1(TAB)parent2(TAB)proband> \
-X <put 1 if you want to run on X chromosome as well, 0 otherwise> \
-P <threshold on posterior probability. Calls are made if the PP is above threshold. Use a low value like 0.005 so that a large number of calls are made for the second layer> \
-E <threshold on the ExAC allele frequency, e.g. 0.0001>
```