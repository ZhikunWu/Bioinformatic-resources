
## [MOCAT2](http://mocat.embl.de)

### [MOCAT2 github](https://github.com/mocat2/mocat2)

### [MOCAT2 tutorial](http://mocat.embl.de/tutorial.html)

### install MOCAT2

first download the [MOCAT2 tool](http://vm-lux.embl.de/~kultima/share/MOCAT/v2.0/MOCAT2-lite.zip)

It may be that to run MOCAT you may need ot install the Perl5 File::Sync 
```bash
$ perl -MCPAN -e shell (and then: install File::Sync) 
```



```
drwxr-xr-x  5 4.0K Dec 16  2015 article_datasets
drwxrwxr-x  7 4.0K Dec 17  2015 bin
drwxr-xr-x  2 4.0K Nov  9  2017 data
drwxr-xr-x  5 4.0K Dec 13  2015 ext
drwxrwxr-x  2 4.0K Nov  9  2017 GETTING_STARTED
drwxr-xr-x  3 4.0K Dec 13  2015 lib
drwxrwxr-x  3 4.0K Dec 13  2015 mod
drwxrwxr-x  2 4.0K Jan 27  2017 scripts
-rwxr-xr-x  1  18K Dec 17  2015 setup.MOCAT.pl
drwxr-xr-x 11 4.0K Jan 27  2017 src

```

```
$ perl setup.MOCAT.pl 
=================================================================================
                  MOCAT - Metagenomics Analysis Toolkit                 v 2.0.0
 by Jens Roat Kultima, Luis Pedro Coelho, Shinichi Sunagawa @ Bork Group, EMBL
=================================================================================

SOFTWARE AGREEMENTS INFORMATION
To proceed you have to agree with the licence agreements of all included software
DOWNLOAD SIZE AND INSTALLATION TIME
The Human Genome 19 (hg19) database can be downloaded and built.
The download size is 6.5GB. The largest sample dataset to
download is the simulated dataset, which requires a 3.5GB download

Please type 'yes' and press Enter, if you agree with the licence agreements
for each software used by MOCAT, and wish to proceed (otherwise type 'no'):
(yes/no)
yes

SETUP THE CONFIG FILE
What queuing system do you use on your system?
This can be changed in the config file later.
If you don't know, type 'none'
('SGE', 'PBS', 'LSF' or 'none')
none

DOWNLOAD EXTERNAL DATABASES
Would you like to download and install the hg19 reference database (approx 6.5GB)? (yes/no)
This database is provided as a database to screen reads against (e.g. remove human contaminants).
(yes/no):
no

DOWNLOAD ARTICLE DATASETS AND EXAMPLE FILES
There are two different sample files that can be downloaded:
- The simulated metagenome (100 strains, used in MOCAT paper)
- The simulated metagenome (87 species, used in mOTU paper)
- the HMP mock community data

Would you like to download THE SIMULATED METAGENOME (100 strains) used inthe MOCAT paper (approx 3.5GB)? (yes/no)
no

Would you like to download THE SIMULATED METAGENOME (87 species) used in the mOTU paper (approx 2.3GB)? (yes/no)
no

Would you like to download THE MOCK COMMUNITY (approx 500 MB)? (yes/no)
no

Will you be running the SIMULATED METAGENOME or MOCK COMMUNITY on a system with less than 8 cores?
(yes/no)
no

DOWNLOADING AND SETTING UP DATABSES & DATASETS...
wget: /home/wzk/anaconda3/envs/kcmRNA/lib/libcrypto.so.1.0.0: no version information available (required by wget)
wget: /home/wzk/anaconda3/envs/kcmRNA/lib/libssl.so.1.0.0: no version information available (required by wget)
wget: /home/wzk/anaconda3/envs/kcmRNA/lib/libssl.so.1.0.0: no version information available (required by wget)
--2017-11-09 03:10:32--  http://vm-lux.embl.de/~kultima/share/MOCAT/data/1506MG.tar.gz
Resolving vm-lux.embl.de (vm-lux.embl.de)... 194.94.44.167
Connecting to vm-lux.embl.de (vm-lux.embl.de)|194.94.44.167|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 280755410 (268M) [application/x-gzip]
Saving to: ‘data/1506MG.tar.gz’

data/1506MG.tar.gz            100%[================================================>] 267.75M   113KB/s    in 54m 34s 

2017-11-09 04:05:07 (83.7 KB/s) - ‘data/1506MG.tar.gz’ saved [280755410/280755410]

Extracting 1506MG DB...
1506MG
1506MG.index.amb
1506MG.index.ann
1506MG.index.bwt
1506MG.index.fmv
1506MG.index.hot
1506MG.index.lkt
1506MG.index.pac
1506MG.index.rev.bwt
1506MG.index.rev.fmv
1506MG.index.rev.lkt
1506MG.index.rev.pac
1506MG.index.sa
1506MG.index.sai
sed: can't read article_datasets/make_and_annotate_gene_catalog/MOCAT.cfg: No such file or directory
sed: can't read article_datasets/make_and_annotate_gene_catalog/MOCAT.cfg: No such file or directory
CONFIG FILE INFORMATION
Changed MOCAT.cfg for this system.
Setup set the flag 'MOCAT_dir' to /home/wzk/anaconda3/envs/qiime/bin/MOCAT

UNIX / OSX STARTUP FILE CHANGES
Exported /home/wzk/anaconda3/envs/qiime/bin/MOCAT/src to $PERL5LIB and $PATH variable
to ~./bashrc and ~./bash_profile

=================================================================================
SUCCESS! MOCAT has now been setup and is ready to be used!
You start it by running 'MOCAT.pl' from any directory.
=================================================================================

LAST THING TO DO BEFORE RUNNING MOCAT.pl
Please execute commands below, to ensure Perl libraries are correctly loaded
EXECUTE: source ~/.bashrc; source ~/.bash_profile
and then you can run MOCAT using 'MOCAT.pl'
```

