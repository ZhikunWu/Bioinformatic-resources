## [DeepSignal](https://github.com/bioinfomaticsCSU/deepsignal)

A deep-learning method for detecting DNA methylation state from Oxford Nanopore sequencing reads

### Install DeepSignal

#### create the environment
```
conda create -n DeepLerning python=3
```


### install deepsiginal
```
(DeepSignal) wuzhikun@mu01 19:45:49 ^_^ /home/wuzhikun/anaconda3/envs/DeepSignal/share 
$ git clone https://github.com/bioinfomaticsCSU/deepsignal.git

$ cd deepsignal/

$ python setup.py install

```

It will download the dependencies and install them automatically

or install the dependencies like this

```
conda install -c bioconda ont-tombo
conda install -c conda-forge numpy
conda install -c conda-forge h5py
conda install -c conda-forge statsmodels
conda install -c conda-forge scikit-learn
conda install -c anaconda tensorflow-gpu 
```

