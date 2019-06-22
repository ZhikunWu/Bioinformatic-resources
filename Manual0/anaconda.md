## anaconda

### conda channel
the  channel in ~/.condarc
```bash
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://nanomirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - hcc
  - biocore
  - bioconda
  - r
show_channel_urls: true
```



### conda manual

#### conda 添加镜像
```
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

$ conda config --add channels https://nanomirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/

$ conda config --set show_channel_urls yes
```

#### export the environment
```
$ conda env export --name qiime > qiime.yaml
```


#### 创建环境
```
#创建一个名为python34的环境，指定Python版本是3.4
$ conda create --name python34 python=3.4

# 指定python版本为2.7，注意至少需要指定python版本或者要安装的包# 后一种情况下，自动安装最新python版本
$ conda create -n env_name python=2.7

# 同时安装必要的包
$ conda create -n env_name numpy matplotlib python=2.7
```

#### 删除一个已有的环境
```
$ conda remove --name python34 --all
```

#### 查看已安装的环境
```
$ conda info -e
```

#### conda 包管理
```
# 安装xxxx
$ conda install xxxx

# 查看当前环境下已安装的包
$ conda list

# 查看某个指定环境的已安装包
$ conda list -n python34

# 查找package信息
$ conda search numpy


```

#### Conda 更新
```bash
# 更新package
$ conda update -n python34 numpy

# 删除package
$ conda remove -n python34 numpy

# 更新conda，保持conda最新
$ conda update conda

# 更新anaconda
$ conda update anaconda

# 更新python
$ conda update python
```
