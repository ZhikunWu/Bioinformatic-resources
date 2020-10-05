### 查看ubuntu硬件架构
```
$ uname -a
Linux ubuntu 4.4.0-62-generic #83-Ubuntu SMP Wed Jan 18 14:10:15 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

$ dpkg --print-architecture
amd64

$ getconf LONG_BIT
64

$ arch
x86_64

```

### Linux批量杀死包含某个关键字的进程
```
$ ps -ef | grep ./amplxe-gui | grep -v grep | cut -c 9-15 | xargs kill -9
```
批量杀死包含关键字“./amplxe-gui”的进程。

* "ps -ef" ——查看所有进程
* "grep ./amplxe-gui" ——列出所有含有关键字"./amplxe-gui"的进程
* "grep -v grep" ——在列出的进程中去除含有关键字"grep"的进程（因为我们在前一步生成的grep进程也包含关键字）
* "cut -c 9-15" ——截取输入行的第9个字符到第15个字符，而这正好是进程号PID
* "xargs kill -9" ——xargs 命令是用来把前面命令的输出结果（PID）作为"kill -9"命令的参数，并执行该命令。"kill -9"会强行杀掉指定进程。


### filt data
```
$ awk '{if($3>0.95 || $3 < -0.95){print $0}}' Treatment_correlation.txt > Treatment_correlation_sig.txt
```

### insert string
```
$ sed -i 's/^[^>]\s*$//g' SILVA_132_SSUParc_tax_silva_DNA_species_modify.fasta
```




### [C compiler cannot create executables](http://blog.51cto.com/11072323/1731178)
### [C compiler cannot create executables ](https://github.com/skycocker/chromebrew/issues/142)
```
export CC=/usr/bin/gcc
```

```
checking for Boost headers version >= 1.46.0... no
configure: cannot find Boost headers version >= 1.46.0
## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ##
## Could not find a working installation of Boost. Set BOOST_ROOT to the path where the Boost headers are installed or set BOOST_ROOT=install to have it downloaded from the Internet and installed locally. For example: BOOST_ROOT=install ./install.sh 

```

```
$ conda install -c conda-forge boost
Fetching package metadata ...................
Solving package specifications: .

Package plan for installation in environment /home/wzk/anaconda3/envs/evolution:

The following packages will be UPDATED:

    blasr_libcpp: 1.1-boost1.60_0   bioconda                                                        --> 1.1-boost1.64_1   bioconda   
    boost:        1.60.0-py36_0     https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free         --> 1.64.0-py36_4     conda-forge

The following packages will be SUPERSEDED by a higher-priority channel:

    boost-cpp:    1.65.1-0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge --> 1.64.0-1          conda-forge
    h5py:         2.7.1-py36_2      https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge --> 2.7.0-np112py36_0 conda-forge

The following packages will be DOWNGRADED:

    augustus:     3.2.3-boost1.60_1 bioconda                                                        --> 3.2.2-0           bioconda   
    busco:        3.0.2-py36_5      bioconda                                                        --> 3.0.1-py36_0      bioconda   
    hdf5:         1.10.1-1          conda-forge                                                     --> 1.8.17-11         conda-forge

```
