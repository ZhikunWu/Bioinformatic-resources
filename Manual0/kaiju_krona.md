## [kaiju](https://github.com/bioinformatics-centre/kaiju): Fast taxonomic classification of metagenomic sequencing reads using a protein reference database

A program for the taxonomic classification of metagenomic high-throughput sequencing reads. Each read is directly assigned to a taxon within the NCBI taxonomy by comparing it to a reference database containg microbial and viral protein sequences. By default, Kaiju uses either the available complete genomes from NCBI RefSeq or the microbial subset of the non-redundant protein database nr used by NCBI BLAST, optionally also including fungi and microbial eukaryotes.

### install kaiju
```
$ conda install -c bioconda kaiju
```

or


```bash
$ git clone https://github.com/bioinformatics-centre/kaiju.git
$ cd kaiju/src
$ make
```


### Creating the reference database and index
For creating a local index, the program makeDB.sh in the bin/ directory will download the reference genomes and taxonomy files from the NCBI FTP server, convert them into a protein database and construct Kaiju's index (the Burrows-Wheeler transform and the FM-index) in one go.

```
$ mkdir kaijudb
$ cd kaijudb
$ makeDB.sh [-r|-p|-n|-e]
```

### Different reference

##### Complete Reference Genomes from NCBI RefSeq
Download only completely assembled and annotated reference genomes of Archaea and Bacteria from the NCBI RefSeq database.

```
makeDB.sh -r
```

Additionally, viral genomes from NCBI RefSeq can be added by using the option `-v`.

As of October 2016, this database contains ca. 20M protein sequences, which amounts to a requirement of 14GB RAM for running Kaiju.


##### Representative genomes from proGenomes

```
makeDB.sh -p
```

Download the protein sequences belonging to the representative set of genomes from the proGenomes database. This dataset generally covers a broader phylogenenic range compared to the RefSeq dataset, and is therefore recommended, especially for environmental samples.

Additionally, viral genomes from NCBI RefSeq can be added by using the option -v.

As of October 2016, this database contains ca. 19M protein sequences, which amounts to a requirement of 13GB RAM for running Kaiju.

##### Virus Genomes from NCBI RefSeq
```
makeDB.sh -v
```

##### Non-redundant protein database nr
```
makeDB.sh -n
```
Download the nr database that is used by NCBI BLAST and extract proteins belonging to Archaea, Bacteria and Viruses.


#### Index construction
When using option -r, makeDB.sh downloads and extracts 5 genomes from the NCBI FTP server in parallel. This number can be changed by modifying the appropriate variables at the beginning of the script.

By default, makeDB.sh uses 5 parallel threads for constructing the index, which can be changed by using the option -t. Note that a higher number of threads increases the memory usage during index construction, while reducing the number of threads decreases memory usage.

After makeDB.sh is finished, only the files `kaiju_db.fmi` (or `kaiju_db_nr.fmi` / `kaiju_db_nr_euk.fmi`), `nodes.dmp`, and `names.dmp` are needed to run Kaiju. The remaining files and the `genomes/`` directory containing the downloaded genomes can be deleted.

```
$ find ./genomes -name "*.gbff.gz" | xargs -n 1 -P 20 -i gbk2faa.pl '{}' '{}'.faa
$ cat genomes/*.faa | perl -lsne 'BEGIN{open(F,$m);while(<F>){@F=split(/[\|\s]+/);$h{$F[0]}=$F[1]}}if(/(>.+)_(\d+)/){print $1,"_",defined($h{$2})?$h{$2}:$2;}else{print}' -- -m=merged.dmp  >kaiju_db.faa
$ mkbwt -n 30  -e 3 -a ACDEFGHIKLMNPQRSTVWY -o kaiju_db kaiju_db.faa

# infilename= kaiju_db.faa
# outfilename= kaiju_db
# Alphabet= ACDEFGHIKLMNPQRSTVWY
# nThreads= 30
# length= 0.000000
# checkpoint= 3
# caseSens=OFF
# revComp=OFF
# term= *
# revsort=OFF
# help=OFF
Sequences read time = 73.069738s
SLEN 9605251543
NSEQ 29704977
ALPH *ACDEFGHIKLMNPQRSTVWY
SA NCHECK=0
Sorting done,  time = 8679.070672s


$ mkfmi kaiju_db
# filenm= kaiju_db
# removecmd= NULL (null)
# help=OFF
Reading BWT from file kaiju_db.bwt ... DONE
BWT of length 9337906740 has been read with 29704977 sequencs, alphabet=*ACDEFGHIKLMNPQRSTVWY
Reading suffix array from file kaiju_db.sa ... DONE
Writing BWT header and SA to file  kaiju_db.fmi ... DONE
Constructing FM index
10% ... 20% ... 30% ... 40% ... 50% ... 60% ... 70% ... 80% ... 90% ... 100% ... index2 done ... 
DONE
Writing FM index to file ... DONE

  !!  You can now delete files kaiju_db.bwt and kaiju_db.sa  !!


```


### Custom database
It is also possible to make a custom database from a collection of protein sequences. The format needs to be a FASTA file in which the headers are the numeric NCBI taxon identifiers of the protein sequences, which can optionally be prefixed by another identifier (e.g. a counter) followed by an underscore, for example:
```
>1_1358
MAQQRRGGFKRRKKVDFIAANKIEVVDYKDTELLKRFISERGKILPRRVTGTSAKNQRKVVNAIKRARVMALLPFVAEDQN
>2_44689
MASTQNIVEEVQKMLDTYDTNKDGEITKAEAVEYFKGKKAFNPERSAIYLFQVYDKDNDGKITIKELAGDIDFDKALKEYKEKQAKSKQQEAEVEEDIEAFILRHNKDDNTDITKDELIQGFKETGAKDPEKSANFILTEMDTNKDGTITVKELRVYYQKVQKLLNPDQ
>3_352472
MKTKSSNNIKKIYYISSILVGIYLCWQIIIQIIFLMDNSIAILEAIGMVVFISVYSLAVAINGWILVGRMKKSSKKAQYEDFYKKMILKSKILLSTIIIVIIVVVVQDIVINFILPQNPQPYVYMIISNFIVGIADSFQMIMVIFVMGELSFKNYFKFKRIEKQKNHIVIGGSSLNSLPVSLPTVKSNESNESNTISINSENNNSKVSTDDTINNVM
>4_91061
MTNPFENDNYTYKVLKNEEGQYSLWPAFLDVPIGWNVVHKEASRNDCLQYVENNWEDLNPKSNQVGKKILVGKR
...
```
The taxon identifiers must be contained in the NCBI taxonomy files nodes.dmp and names.dmp. Then, Kaiju's index is created using the programs `mkbwt` and `mkfmi`. For example, if the database FASTA file is called `proteins.faa`, then run:
```bash
mkbwt -n 5 -a ACDEFGHIKLMNPQRSTVWY -o proteins proteins.faa
mkfmi proteins
```
which creates the file proteins.fmi that is used by Kaiju. Note that the protein sequences may only contain the uppercase characters of the standard 20 amino acids, all other characters need to be removed.


### run kaiju
```
$ kaiju -t  /home/wzk/database/kaiju/nodes.dmp -f /home/wzk/database/kaiju/kaiju_db.fmi -z 20 -i clean/SOIL_NATCOMM_25M.clean.paired.R1.fq.gz -j clean/SOIL_NATCOMM_25M.clean.paired.R2.fq.gz -o kaiju/kaiju
```
or
```bash
$ kaiju -t /home/wzk/database/kaiju/nodes.dmp -f /home/wzk/database/kaiju/kaiju_db.fmi -z 20 -i /home/wzk/metagenome_data/raw_test/TARA_OCEAN.25M.1.fastq -j /home/wzk/metagenome_data/raw_test/TARA_OCEAN.25M.2.fastq -o /home/wzk/metagenome_data/raw_test/TARA_OCEAN.25M.out
```


##### output file:
```
$ head kaiju/kaiju 
C	SRR908279.25002	1224
C	SRR908279.25073	710696
U	SRR908279.25133	0
C	SRR908279.25146	1736675
C	SRR908279.25172	1912856
U	SRR908279.25188	0
U	SRR908279.25212	0
U	SRR908279.25228	0
C	SRR908279.25240	2
U	SRR908279.25271	0
```


### kaiju report
```
$ kaijuReport   -t  /home/wzk/database/kaiju/nodes.dmp -n  /home/wzk/database/kaiju/names.dmp  -i kaiju/kaiju  -r species  -u -p -o kaiju/kaiju.report.txt

```

output file:
```
$ head  kaiju/kaiju.report.txt
        %	    reads	species
-------------------------------------------
 0.965068	     3981	cellular organisms; Bacteria; Proteobacteria; Alphaproteobacteria; Rhizobiales; Hyphomicrobiaceae; Devosia; Devosia sp. A16; 
 0.833434	     3438	cellular organisms; Bacteria; Terrabacteria group; Actinobacteria; Actinobacteria; Corynebacteriales; Gordoniaceae; Gordonia; Gordonia polyisoprenivorans; 
 0.816223	     3367	cellular organisms; Bacteria; Terrabacteria group; Actinobacteria; Actinobacteria; Propionibacteriales; Nocardioidaceae; Nocardioides; Nocardioides sp. JS614; 
 0.809435	     3339	cellular organisms; Bacteria; Proteobacteria; Alphaproteobacteria; Rhizobiales; Rhizobiaceae; Rhizobium/Agrobacterium group; Neorhizobium; Neorhizobium galegae; 
 0.708589	     2923	cellular organisms; Bacteria; Proteobacteria; Alphaproteobacteria; Rhizobiales; Rhizobiaceae; Rhizobium/Agrobacterium group; Rhizobium; Rhizobium sp. NT-26; 
 0.693559	     2861	cellular organisms; Bacteria; Terrabacteria group; Actinobacteria; Thermoleophilia; Solirubrobacterales; Conexibacteraceae; Conexibacter; Conexibacter woesei; 
 0.677317	     2794	cellular organisms; Bacteria; Proteobacteria; Alphaproteobacteria; Rhizobiales; Hyphomicrobiaceae; Devosia; Devosia sp. H5989; 
 0.673923	     2780	cellular organisms; Bacteria; Terrabacteria group; Actinobacteria; Actinobacteria; Propionibacteriales; Nocardioidaceae; Pimelobacter; Pimelobacter simplex;
 ```
 



#### Creating input file for Krona
```
$ kaiju2krona -t /home/wzk/database/kaiju/nodes.dmp -n /home/wzk/database/kaiju/names.dmp -i /home/wzk/metagenome_data/raw_test/TARA_OCEAN.25M.out -o /home/wzk/metagenome_data/raw_test/TARA_OCEAN.25M.out.krona
```

output file:
```
$ head /home/wzk/metagenome_data/raw_test/TARA_OCEAN.25M.out.krona
1   root    cellular organisms  Bacteria    Terrabacteria group Firmicutes  Bacilli Lactobacillales Streptococcaceae    Streptococcus   Streptococcus pneumoniae    Streptococcus pneumoniae gamPNI0373
1   root    cellular organisms  Bacteria    Proteobacteria  Gammaproteobacteria Legionellales   Coxiellaceae    Coxiella    Coxiella burnetii   Coxiella burnetii Z3055
1   root    cellular organisms  Bacteria    Terrabacteria group Firmicutes  Bacilli Bacillales  Bacillaceae Bacillus    Bacillus cereus group   Bacillus thuringiensis  Bacillus thuringiensis HD-789
1   root    cellular organisms  Bacteria    Terrabacteria group Firmicutes  Clostridia  Clostridiales   Clostridiales incertae sedis
1   root    cellular organisms  Bacteria    Terrabacteria group Actinobacteria  Actinobacteria  Bifidobacteriales   Bifidobacteriaceae  Bifidobacterium Bifidobacterium longum  Bifidobacterium longum DJO10A
2   root    cellular organisms  Bacteria    Terrabacteria group Firmicutes  Bacilli Lactobacillales Lactobacillaceae    Lactobacillus   Lactobacillus sakei Lactobacillus sakei subsp. sakei    Lactobacillus sakei subsp. sakei DSM 20017 = JCM 1157
1   root    cellular organisms  Bacteria    Terrabacteria group Firmicutes  Bacilli Bacillales  Bacillaceae Bacillus    Bacillus cereus group   Bacillus anthracis  Bacillus anthracis str. Sterne
1   root    cellular organisms  Bacteria    Proteobacteria  Betaproteobacteria  unclassified Betaproteobacteria Kinetoplastibacterium   Kinetoplastibacterium blastocrithidii   Candidatus Kinetoplastibacterium blastocrithidii (ex Strigomonas culicis)
1   root    cellular organisms  Archaea TACK group  Crenarchaeota   Thermoprotei    Sulfolobales    Sulfolobaceae   Sulfolobus  Sulfolobus solfataricus Sulfolobus solfataricus 98/2
1   root    cellular organisms  Bacteria    Proteobacteria  Gammaproteobacteria Enterobacterales    Enterobacteriaceae  Salmonella  Salmonella enterica Salmonella enterica subsp. enterica Salmonella enterica subsp. enterica serovar Schwarzengrund  Salmonella enterica subsp. enterica serovar Schwarzengrund str. CVM19633

```


#### install Krona
```bash
$ conda install -c bioconda krona

Fetching package metadata .................
Solving package specifications: .

Package plan for installation in environment /home/wzk/anaconda3/envs/qiime:

The following NEW packages will be INSTALLED:

    krona: 2.7-pl5.22.0_1 bioconda

Proceed ([y]/n)? y

krona-2.7-pl5. 100% |##################################################| Time: 0:00:12  11.29 kB/s

Krona installed.  You still need to manually update the taxonomy
databases before Krona can generate taxonomic reports.  The update
script is ktUpdateTaxonomy.sh.  The default location for storing
taxonomic databases is /home/wzk/anaconda3/envs/qiime/opt/krona/taxonomy

If you would like the taxonomic data stored elsewhere, simply replace
this directory with a symlink.  For example:

rm -rf /home/wzk/anaconda3/envs/qiime/opt/krona/taxonomy
mkdir /path/on/big/disk/taxonomy
ln -s /path/on/big/disk/taxonomy /home/wzk/anaconda3/envs/qiime/opt/krona/taxonomy
ktUpdateTaxonomy.sh

```

#### convert to html using Krona
```bash
$ ktImportText -o TARA_OCEAN.25M.out.html TARA_OCEAN.25M.out.krona
```

#### Creating classification summary
The program can also filter out taxa with low abundances, e.g. for only showing genera that comprise at least 1 percent of the total reads:
```bash
$ kaijuReport -t  /home/wzk/database/kaiju/nodes.dmp -n /home/wzk/database/kaiju/names.dmp -i TARA_OCEAN.25M.out -r genus -m 1 -o TARA_OCEAN.25M.out.summary
```

or for showing genera comprising at least 1 percent of all classified reads:
```bash
$ kaijuReport -t  /home/wzk/database/kaiju/nodes.dmp -n /home/wzk/database/kaiju/names.dmp -i TARA_OCEAN.25M.out -r genus -m 0.01 -u -o TARA_OCEAN.25M.out.summary
```
output files:
```
$ head  TARA_OCEAN.25M.out.summary
        %       reads   genus
-------------------------------------------
22.191372     2613758   Prochlorococcus
 9.346055     1100803   Candidatus Pelagibacter
 0.679243       80003   Candidatus Fonsibacter
 0.512563       60371   Pseudomonas
 0.470749       55446   Candidatus Puniceispirillum
 0.409135       48189   Synechococcus
 0.337851       39793   Alteromonas
 0.271076       31928   Bacillus

```

Option -p will print the full taxon path instead of just the taxon name.
```bash
$ kaijuReport -t  /home/wzk/database/kaiju/nodes.dmp -n /home/wzk/database/kaiju/names.dmp -i TARA_OCEAN.25M.out -r genus -m 0.01 -u -p -o TARA_OCEAN.25M.out.summary

```

output file:
```
$ head  TARA_OCEAN.25M.out.summary
        %       reads   genus
-------------------------------------------
22.191372     2613758   cellular organisms; Bacteria; Terrabacteria group; Cyanobacteria/Melainabacteria group; Cyanobacteria; Synechococcales; Prochloraceae; Prochlorococcus; 
 9.346055     1100803   cellular organisms; Bacteria; Proteobacteria; Alphaproteobacteria; Pelagibacterales; Pelagibacteraceae; Candidatus Pelagibacter; 
 0.679243       80003   cellular organisms; Bacteria; Proteobacteria; Alphaproteobacteria; Pelagibacterales; Candidatus Fonsibacter; 
 0.512563       60371   cellular organisms; Bacteria; Proteobacteria; Gammaproteobacteria; Pseudomonadales; Pseudomonadaceae; Pseudomonas; 
 0.470749       55446   cellular organisms; Bacteria; Proteobacteria; Alphaproteobacteria; unclassified Alphaproteobacteria; SAR116 cluster; Candidatus Puniceispirillum; 
 0.409135       48189   cellular organisms; Bacteria; Terrabacteria group; Cyanobacteria/Melainabacteria group; Cyanobacteria; Synechococcales; Synechococcaceae; Synechococcus; 
 0.337851       39793   cellular organisms; Bacteria; Proteobacteria; Gammaproteobacteria; Alteromonadales; Alteromonadaceae; Alteromonas; 
 0.271076       31928   cellular organisms; Bacteria; Terrabacteria group; Firmicutes; Bacilli; Bacillales; Bacillaceae; Bacillus; 
 ```

 #### Adding taxa names
```bash
$ addTaxonNames  -t  /home/wzk/database/kaiju/nodes.dmp -n /home/wzk/database/kaiju/names.dmp -i TARA_OCEAN.25M.out -r -u -p -o TARA_OCEAN.25M.out_name.summary
Error: Please use either option -r or -p, but not both of them.

```
