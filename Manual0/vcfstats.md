### install vcfstats
```
$ git clone "https://github.com/lindenb/jvarkit.git"
$ cd jvarkit
$ make vcfstats
```

```
$ mkdir -p lib/com/github/samtools/htsjdk/2.13.0/ && curl -Lk  -o "lib/com/github/samtools/htsjdk/2.13.0/htsjdk-2.13.0.jar" "http://central.maven.org/maven2/com/github/samtools/htsjdk/2.13.0/htsjdk-2.13.0.jar"
curl: (48) An unknown option was passed in to libcurl
maven.mk:145: recipe for target 'lib/com/github/samtools/htsjdk/2.13.0/htsjdk-2.13.0.jar' failed
make: *** [lib/com/github/samtools/htsjdk/2.13.0/htsjdk-2.13.0.jar] Error 48
```

```
$ wget http://central.maven.org/maven2/com/github/samtools/htsjdk/2.13.0/htsjdk-2.13.0.jar


$ mkdir -p lib/commons-logging/commons-logging/1.1.1/ && curl -Lk  -o "lib/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar" "http://central.maven.org/maven2/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar"


$ wget http://central.maven.org/maven2/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar
$ cp  commons-logging-1.1.1.jar  lib/commons-logging/commons-logging/1.1.1/

$ wget http://central.maven.org/maven2/gov/nih/nlm/ncbi/ngs-java/1.2.4/ngs-java-1.2.4.jar
$ cp ngs-java-1.2.4.jar lib/gov/nih/nlm/ncbi/ngs-java/1.2.4/

$ wget http://central.maven.org/maven2/org/apache/commons/commons-compress/1.4.1/commons-compress-1.4.1.jar
$ cp commons-compress-1.4.1.jar lib/org/apache/commons/commons-compress/1.4.1/

$ wget http://central.maven.org/maven2/org/apache/commons/commons-jexl/2.1.1/commons-jexl-2.1.1.jar
$ cp commons-jexl-2.1.1.jar lib/org/apache/commons/commons-jexl/2.1.1/

$ wget http://central.maven.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar
$ cp xz-1.5.jar lib/org/tukaani/xz/1.5/

$ wget http://central.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.4/snappy-java-1.1.4.jar
$ cp snappy-java-1.1.4.jar  lib/org/xerial/snappy/snappy-java/1.1.4/

$ wget http://central.maven.org/maven2/com/beust/jcommander/1.64/jcommander-1.64.jar
$ cp jcommander-1.64.jar lib/com/beust/jcommander/1.64/

```

### run vcfstats
### [vcfstats manual](http://lindenb.github.io/jvarkit/VcfStats.html)
```
$ vcfstats ERR2173373_ERR2173372.vcf --output out
```

output files:
```
-rw-r--r-- 1   19 Mar 21 07:07 ALL.affectedSamples.tsv
-rw-r--r-- 1   21 Mar 21 07:07 ALL.countAltAlleles.tsv
-rw-r--r-- 1  407 Mar 21 07:07 ALL.countDepthBySample.tsv
-rw-r--r-- 1  349 Mar 21 07:07 ALL.countDepth.tsv
-rw-r--r-- 1  228 Mar 21 07:07 ALL.countDistancesBySample.tsv
-rw-r--r-- 1  198 Mar 21 07:07 ALL.countDistances.tsv
-rw-r--r-- 1  119 Mar 21 07:07 ALL.countIndelSize.tsv
-rw-r--r-- 1  11K Mar 21 07:07 ALL.genscan.tsv
-rw-r--r-- 1   25 Mar 21 07:07 ALL.gtConcordance.tsv
-rw-r--r-- 1 3.0K Mar 21 07:07 ALL.sample2contig.tsv
-rw-r--r-- 1   84 Mar 21 07:07 ALL.sample2gtype.tsv
-rw-r--r-- 1   54 Mar 21 07:07 ALL.transvers.tsv
-rw-r--r-- 1 3.0K Mar 21 07:07 ALL.variant2contigs.tsv
-rw-r--r-- 1   55 Mar 21 07:07 ALL.variant2type.tsv
-rw-r--r-- 1  12K Mar 21 07:07 Makefile
```

```
$ cat  ALL.variant2type.tsv
Type    Count
INDEL   1446168
MIXED   1267
MNP 793
SNP 280322

```

