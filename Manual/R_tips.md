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


