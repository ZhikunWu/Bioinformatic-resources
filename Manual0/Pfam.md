## The use of Pfam for prediction of coding and non-coding of RNA
### Install HMMER3 
Download the source of [HMMER3](http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2.tar.gz) or the [binary](http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz) format

```
wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz
tar -zxvf hmmer-3.1b2-linux-intel-x86_64.tar.gz
```
If you are a non-root user, then you can install it in your own path
```
cd hmmer-3.1b2-linux-intel-x86_64/
./configure --prefix /home/wzk/bin
make
make check
make install
```
Then it was install in the path '/home/wzk/bin/bin', and you should add it to the environment variables like this:
```
echo 'export PATH=/home/wzk/bin/bin:$PATH ' >>  ~/.bashrc
source ~/.bashrc
```
### Install module Moose for perl
Firstly you should download 'CPANM' for your linux, You can also install it as the non-root user :
```
wget -O- http://cpanmin.us | perl - -l ~/perl5 App::cpanminus local::lib
eval `perl -I ~/perl5/lib/perl5 -Mlocal::lib`
echo 'eval `perl -I ~/perl5/lib/perl5 -Mlocal::lib`' >> ~/.profile
echo 'export MANPATH=$HOME/perl5/man:$MANPATH' >> ~/.profile
source ~/.profile
```
In this step ~/.profile may be the file .bash_profile or .bashrc, it depend on your linux 

Then you can install Moose using the platform 'CPANM':
```
cpanm Moose
```
This time you should also install 'IPC::Run':
```
cpanm IPC::Run
```

### Install Pfam
You can doanload [Pfam](ftp://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/PfamScan.tar.gz) like this:

```
wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/PfamScan.tar.gz
tar -zxvf PfamScan.tar.gz
```
And put the path of Pfam to the lib path of Perl 
```
echo 'export PERL5LIB=/home/wzk/bin/PfamScan:$PERL5LIB ' >>  ~/.bashrc
source  ~/.bashrc
```
And you should download the [database](ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release)
```
wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz
wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.dat.gz
```
Put these files in a dir and then uncompress them

### The use of Pfam


```
perl /home/wzk/bin/PfamScan/pfam_scan.pl -fasta ambiguous_genes.fa -dir /home/wzk/bin/PfamScan/Pfam_db_zfc  -out /home/wzk/test_cufflinks/cuffcompare/novel/novel/ambiguous_genes_pfam_annotate -cpu 20
```
* -fasta: The fasta file which derived from .gtf file
* -dir: the dir contain the database you download
* -out: the out file of the result

