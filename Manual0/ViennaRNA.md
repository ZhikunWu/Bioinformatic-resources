### [ViennaRNA](http://rna.tbi.univie.ac.at/)

### install
Installing from sourcecode is the recommended way to get most out of the ViennaRNA Package. For best portability the ViennaRNA package uses the GNU tools autoconf, automake, and libtool and can thus be compiled and installed on almost every computer platform. See the [INSTALL](https://www.tbi.univie.ac.at/RNA/documentation.html#install)
```
wget https://www.tbi.univie.ac.at/RNA/download/sourcecode/2_4_x/ViennaRNA-2.4.0.tar.gz
tar -zxf ViennaRNA-2.4.0.tar.gz
cd ViennaRNA-2.4.0/
./configure --prefix=/home/wzk/anaconda3/envs/py35
make
make install
```

or install via **conda**
```
$ conda install -c bioconda viennarna
```


### run RNAfolder
* specify output
```
RNAfold -i test.fasta -o test_fold
```

creat two files

```
test_fold_CTC-459F4.1.fold
test_fold_CTC-459F4.1_ss.ps
```

* not specify output
```
 RNAfold -i test.fa 
```
creat one file
```
CTC-459F4.1_ss.ps
```

### plot the fold
```
RNAplot -o svg <  test_fold_CTC-459F4.1.fold
```
creat the svg file
```
test_fold_CTC-459F4.1_ss.svg
```

### ps2pdf

convert the file to pdf format

```
ps2pdf test_fold_CTC-459F4.1_ss.ps test_fold_CTC-459F4.1_ss.pdf
```


```
RNAfold -i seq > RP5-857K21.4__1-776069-776143_ss.fold

RNAplot -o svg < RP5-857K21.4__1-776069-776143_ss.fold

ps2pdf RP5-857K21.4__1-776069-776143_ss.fold RP5-857K21.4__1-776069-776143_ss.pdf


```
