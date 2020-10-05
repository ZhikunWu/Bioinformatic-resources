
### install R for no root
```
$ ./configure --prefix=/home/wzk/anaconda3/envs/RMeta --enable-R-shlib

checking if libcurl is version 7 and >= 7.22.0... yes
checking if libcurl supports https... no
configure: error: libcurl >= 7.22.0 library and headers are required with support for https
```


### [R mirror](https://cran.r-project.org/mirrors.html)
```
> getOption("repos")

> R.home()
[1] "/home/wzk/anaconda3/envs/RMeta/lib/R"

> chooseCRANmirror()
> options(repos = c(CRAN="https://mirrors.ustc.edu.cn/CRAN/"))

> source("https://bioconductor.org/biocLite.R")
> biocLite("DESeq2")


```



### choose mirror for bioconductor or CRAN
for bioconductor
```
> chooseBioCmirror(graphics=FALSE)
HTTPS BioC mirror 

1: 0-Bioconductor (World-wide) [https]
2: Brazil/Latin America (Ribeirão Preto) [https]
3: Germany (Dortmund) [https]
4: United Kingdom (Hinxton) [https]
5: Japan (Tachikawa) [https]
6: Japan (Wako) [https]
7: China (Anhui) [https]
8: Australia (Sydney) [https]
9: (HTTP mirrors)

```
for CRAN
```
getCRANmirrors()

> chooseCRANmirror()
HTTPS CRAN mirror 

 1: 0-Cloud [https]                   2: Algeria [https]                
 3: Australia (Canberra) [https]      4: Australia (Melbourne 1) [https]
 5: Australia (Melbourne 2) [https]   6: Australia (Perth) [https]      
 7: Austria [https]                   8: Belgium (Ghent) [https]        
 9: Brazil (PR) [https]              10: Brazil (RJ) [https]            
11: Brazil (SP 1) [https]            12: Bulgaria [https]               
13: Canada (MB) [https]              14: Chile 1 [https]                
15: Chile 2 [https]                  16: China (Beijing) [https]        
17: China (Hefei) [https]            18: China (Lanzhou) [https]        
19: Colombia (Cali) [https]          20: Czech Republic [https]         
21: Denmark [https]                  22: Estonia [https]                
23: France (Lyon 1) [https]          24: France (Lyon 2) [https]        
25: France (Marseille) [https]       26: France (Montpellier) [https]   
27: France (Paris 2) [https]         28: Germany (Göttingen) [https]    
29: Germany (Münster) [https]        30: Greece [https]                 
31: Iceland [https]                  32: India [https]                  
33: Indonesia (Jakarta) [https]      34: Ireland [https]                
35: Italy (Padua) [https]            36: Japan (Tokyo) [https]          
37: Malaysia [https]                 38: Mexico (Mexico City) [https]   
39: New Zealand [https]              40: Norway [https]                 
41: Philippines [https]              42: Serbia [https]                 
43: Spain (A Coruña) [https]         44: Spain (Madrid) [https]         
45: Sweden [https]                   46: Switzerland [https]            
47: Taiwan (Chungli) [https]         48: Turkey (Denizli) [https]       
49: Turkey (Mersin) [https]          50: UK (Bristol) [https]           
51: UK (Cambridge) [https]           52: UK (London 1) [https]          
53: USA (CA 1) [https]               54: USA (IA) [https]               
55: USA (IN) [https]                 56: USA (KS) [https]               
57: USA (MI 1) [https]               58: USA (OR) [https]               
59: USA (TN) [https]                 60: USA (TX 1) [https]             
61: Vietnam [https]                  62: (HTTP mirrors) 
```


## [Read Rectangular Text Data](https://www.rdocumentation.org/packages/readr/versions/1.1.1)

### installation

```
# The easiest way to get readr is to install the whole tidyverse:
install.packages("tidyverse")

# Alternatively, install just readr:
install.packages("readr")

# Or the the development version from GitHub:
# install.packages("devtools")
devtools::install_github("tidyverse/readr")
```

### readr usage

readr is part of the core tidyverse, so load it with:

```
library(tidyverse)
```

readr supports seven file formats with seven read_ functions:
```
read_csv(): comma separated (CSV) files
read_tsv(): tab separated files
read_delim(): general delimited files
read_fwf(): fixed width files
read_table(): tabular files where colums are separated by white-space.
read_log(): web log files
```


