
## Genomic Data Commons

### download data using GenomicDataCommons in R
### [Protocol To Downlad TCGA Data From GDC](https://www.biostars.org/p/204092/)
```
conda install -c bioconda bioconductor-genomicdatacommons
```

#### find data 
```
library(GenomicDataCommons)
library(magrittr)
ge_manifest = files() %>% 
    filter( ~ cases.project.project_id == 'TCGA-OV' &
                type == 'gene_expression' &
                analysis.workflow_type == 'HTSeq - Counts') %>%
    manifest()
    
```

#### download data
```
destdir = tempdir()
fnames = lapply(ge_manifest$id,gdcdata,
                destination_dir=destdir,overwrite=TRUE,
                progress=FALSE)
```






### download data using gdc-client

### [GDCdownload: Download GDC data](https://rdrr.io/bioc/TCGAbiolinks/man/GDCdownload.html)

#### [Protocol To Downlad TCGA Data From GDC](https://www.biostars.org/p/204092/)

* Downloading Data Using a Manifest File (gdc_manifest.lungCancer.txt)

```
gdc-client download -m gdc_manifest.lungCancer.txt
```

* Downloading Single Data Using a UUID (UUID can be found in manifest file)

```
gdc-client download 22a29915-6712-4f7a-8dba-985ae9a1f005
```

* Downloading Controlled Data (user authentication token is required)

```
gdc-client download -m gdc_manifest_controled.txt -t gdc-user-passwdcode.txt
```

