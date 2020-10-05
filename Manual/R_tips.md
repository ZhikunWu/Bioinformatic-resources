### install an R package from source

```
install.packages(path_to_file, repos = NULL, type="source")
install.packages("RJSONIO", repos = "http://www.omegahat.org/R", type="source")
install.packages("http://cran.r-project.org/src/contrib/Archive/RNetLogo/RNetLogo_0.9-6.tar.gz", repo=NULL, type="source")
```

```
R CMD INSTALL RJSONIO_0.2-3.tar.gz
```


In addition, you can build the binary package using the --binary option.
```
R CMD build --binary RJSONIO_0.2-3.tar.gz
```


### Filter rows that contain a string from a vector
We can use **grep**
```
df1[grep(paste(v1, collapse="|"), df1$animal),]
```

Or using **dplyr**
```
df1 %>%  filter(grepl(paste(v1, collapse="|"), animal))
```


Using dplyr, you can try the following, assuming your table is df:
```
library(dplyr)
library(stringr)
animalList <- c("cat", "dog")
filter(df, str_detect(animal, paste(animalList, collapse="|")))
```



### R, Bioconductor and other R packages

```
# R - need to add R repo first
echo "deb https://www.stats.bris.ac.uk/R/bin/linux/ubuntu $(lsb_release -c | xargs | cut -f2 -d' ')/" | sudo tee -a /etc/apt/sources.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
sudo apt-get update && sudo apt upgrade && sudo apt install libcurl4-openssl-dev libxml2-dev libcairo2-dev libxt-dev libssl-dev
sudo apt install r-base r-base-dev

# install R packages for all users
sudo R | tee -a /tmp/r.log

# CRAN packages
install.packages('tidyverse')
install.packages('data.table')

# devtools ie to install from github
install.packages('devtools')
devtools::install_github('gabraham/flashpca/flashpcaR')

# bioconductor
source("https://bioconductor.org/biocLite.R") 
biocLite('BiocInstaller');
biocLite('GenomicRanges'); 
```



