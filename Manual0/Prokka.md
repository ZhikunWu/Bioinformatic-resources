
## [Prokka](http://www.vicbioinformatics.com/software.prokka.shtml): Annotating metagenome


### Install Prokka

I like the Prokka Annotation Software Program to annotate your assembled metagenome.

We have to download and install a lot of stuff, though -- estimated ~15-20 minutes.

First, we need to install BioPerl and NCBI BLAST+; because we're using an Amazon EC2 ubuntu machine, we'll use the Debian Linux package installer `apt-get`.
```bash
$ apt-get update
$ apt-get -y install bioperl ncbi-blast+
```

Now you want to download and unpack Prokka:
```bash
$ cd /mnt
$ curl -O http://www.vicbioinformatics.com/prokka-1.7.tar.gz
$ tar xzf prokka-1.7.tar.gz 
$ curl -O http://www.vicbioinformatics.com/prokka-1.7.2
$ cp prokka-1.7.2 prokka-1.7/bin/prokka
```

#### install Prokka using conda
```
$ conda install -c bioconda prokka 
```

### Prokka depends on a lot of other software
We'll need to install those tools:

Install [HMMER](http://hmmer.org/):
```bash
cd /mnt
curl -O ftp://selab.janelia.org/pub/software/hmmer3/3.1b1/hmmer-3.1b1.tar.gz
tar xzf hmmer-3.1b1.tar.gz 
cd hmmer-3.1b1/
./configure --prefix=/usr && make && make install
```

Install [Aragorn](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC373265/):
```bash
cd /mnt
curl -O http://mbio-serv2.mbioekol.lu.se/ARAGORN/Downloads/aragorn1.2.36.tgz
tar -xvzf aragorn1.2.36.tgz
cd aragorn1.2.36/
gcc -O3 -ffast-math -finline-functions -o aragorn aragorn1.2.36.c
cp aragorn /usr/local/bin
```



Install [Prodigal](https://github.com/hyattpd/Prodigal):
```bash
cd /mnt
curl -O http://prodigal.googlecode.com/files/prodigal.v2_60.tar.gz
tar xzf prodigal.v2_60.tar.gz 
cd prodigal.v2_60/
make
cp prodigal /usr/local/bin
```

Install [tbl2asn](https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2/):
```bash
cd /mnt
curl -O ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux64.tbl2asn.gz
gunzip linux64.tbl2asn.gz 
mv linux64.tbl2asn tbl2asn
chmod +x tbl2asn
cp tbl2asn /usr/local/bin
```

Install [GNU Parallel](https://www.biostars.org/p/63816/):
```bash
cd /mnt
curl -O http://ftp.gnu.org/gnu/parallel/parallel-20130822.tar.bz2
tar xjvf parallel-20130822.tar.bz2
cd parallel-20130822/
ls
./configure && make && make install
```

Install [Infernal](http://eddylab.org/infernal/):
```bash
cd /mnt
curl -O http://selab.janelia.org/software/infernal/infernal-1.1rc4.tar.gz
tar xzf infernal-1.1rc4.tar.gz 
cd infernal-1.1rc4/
ls
./configure && make && make install
```


### the list of database
```bash
$ prokka --listdb
[21:20:11] Looking for databases in: /home/wzk/anaconda3/envs/qiime/bin/../db
[21:20:11] * Kingdoms: Archaea Bacteria Mitochondria Viruses
[21:20:11] * Genera: Enterococcus Escherichia Staphylococcus
[21:20:11] * HMMs: HAMAP
[21:20:11] * CMs: Bacteria Viruses


$ tree /home/wzk/anaconda3/envs/qiime/bin/../db -L 1
/home/wzk/anaconda3/envs/qiime/bin/../db
├── cm
├── genus
├── hmm
└── kingdom
```


### Running Prokka at the command line

First we'll use the [khmer](http://khmer.readthedocs.io/en/v2.1.1/#) tool to remove all the sequences with 'N's in them (since prodigal fails if there are too many, and prokka uses prodigal):

install kmer
```bash
$ conda install -c bioconda khmer 
```

```bash
$ python /usr/local/share/khmer/sandbox/remove-N.py final-assembly.fa metagenome.fa
```

Now, run Prokka::
```bash
$ /mnt/prokka-1.7/bin/prokka  metagenome.fa --outdir annotation --prefix assembly --metagenome
```

There will be a bunch of files in the directory `annotation`. Probably the most interesting is `assembly/assembly.faa`, which will contain a set of annotated protein sequences derived from the metagenome.

Let's look at some of the files now!



### [parameters pf prokka](https://github.com/tseemann/prokka#invoking-prokka)

### run prokka
```bash
$ prokka Meta.contigs.fa --outdir /home/wzk/metagenome_data/prokka/Meta --prefix Meta --cpus 20
```


output files
```bash
$ tree /home/wzk/metagenome_data/prokka/Meta
/home/wzk/metagenome_data/prokka/Meta
├── Meta.err
├── Meta.faa
├── Meta.ffn
├── Meta.fna
├── Meta.fsa
├── Meta.gbk
├── Meta.gff
├── Meta.log
├── Meta.sqn
├── Meta.tbl
├── Meta.tsv
└── Meta.txt

```

explanation of output file
```
Extension   Description
.gff    This is the master annotation in GFF3 format, containing both sequences and annotations. It can be viewed directly in Artemis or IGV.
.gbk    This is a standard Genbank file derived from the master .gff. If the input to prokka was a multi-FASTA, then this will be a multi-Genbank, with one record for each sequence.
.fna    Nucleotide FASTA file of the input contig sequences.
.faa    Protein FASTA file of the translated CDS sequences.
.ffn    Nucleotide FASTA file of all the prediction transcripts (CDS, rRNA, tRNA, tmRNA, misc_RNA)
.sqn    An ASN1 format "Sequin" file for submission to Genbank. It needs to be edited to set the correct taxonomy, authors, related publication etc.
.fsa    Nucleotide FASTA file of the input contig sequences, used by "tbl2asn" to create the .sqn file. It is mostly the same as the .fna file, but with extra Sequin tags in the sequence description lines.
.tbl    Feature Table file, used by "tbl2asn" to create the .sqn file.
.err    Unacceptable annotations - the NCBI discrepancy report.
.log    Contains all the output that Prokka produced during its run. This is a record of what settings you used, even if the --quiet option was enabled.
.txt    Statistics relating to the annotated features found.
.tsv    Tab-separated file of all features: locus_tag,ftype,gene,EC_number,product
```
