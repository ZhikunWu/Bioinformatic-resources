
## [IGV-snapshot-automator](https://github.com/stevekm/IGV-snapshot-automator)

### [IGV_Batch_Screenshots.md](https://gist.github.com/dfjenkins3/5c6dc1e55e78fa17b931)
### [igv_test_bat.md](https://gist.github.com/stevekm/ac76c0c2fa4ee89db8ce2421cc6fbffc)

### install
```
$ git clone https://github.com/stevekm/IGV-snapshot-automator.git
$ cd IGV-snapshot-automator/bin/ && make
```


### parameters
```
$ python /home/wuzhikun/anaconda3/envs/NanoSV/bin/IGV-snapshot-automator/make_IGV_snapshots.py --help
usage: make_IGV_snapshots.py [-h] [-r regions] [-g genome] [-ht image height]
                             [-o output directory] [-bin IGV bin path]
                             [-mem IGV memory MB] [-nosnap] [-suffix SUFFIX]
                             [-nf4] [-onlysnap ONLYSNAP] [-s]
                             input_files [input_files ...]

IGV snapshot automator

positional arguments:
  input_files           pathes to the files to create snapshots from e.g.
                        .bam, .bigwig, etc.

optional arguments:
  -h, --help            show this help message and exit
  -r regions            BED file with regions to create snapshots over
  -g genome             Name of the reference genome, Defaults to hg19
  -ht image height      Height for the IGV tracks
  -o output directory   Output directory for snapshots
  -bin IGV bin path     Path to the IGV jar binary to run
  -mem IGV memory (MB)  Amount of memory to allocate to IGV, in Megabytes (MB)
  -nosnap               Don't make snapshots, only write batchscript and exit
  -suffix SUFFIX        Filename suffix to place before '.png' in the
                        snapshots
  -nf4                  'Name field 4' mode; uses the value in the fourth
                        field of the regions file as the filename for each
                        region snapshot
  -onlysnap ONLYSNAP    Path to batchscript file to run in IGV. Performs no
                        error checking or other input evaluation, only runs
                        IGV on the batchscript and exits.
  -s, -group_by_strand  Group reads by forward/reverse strand.
```


### run make_IGV_snapshots
```
python /home/wuzhikun/anaconda3/envs/NanoSV/bin/IGV-snapshot-automator/make_IGV_snapshots.py    -r /home/wuzhikun/Project/NanoTrio/IGV_test/target_region.bed  -g hg38 -o /home/wuzhikun/Project/NanoTrio/IGV_test  -nf4  /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M625-0.bam
```


outoput batch file
```
$ cat IGV_snapshots.bat
new
genome /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa
snapshotDirectory /home/wuzhikun/Project/NanoTrio/IGV_test
load /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M625-0.bam
maxPanelHeight 500
goto 2:95931297-95931496
snapshot chr2
goto 14:18901837-18902124
snapshot chr14
exit
```


### run batch file using IGV

* open IGV of windows platform
* open the genome and bam file, and then select  **File -> Save Session** to save the file `igv_session.xml` (just once for all)
* select **Tool -> Run Batch Script** to run the batch scripts previously created





## Run batch scripts on linux (not sucessful)



### download igvtools
```
wget http://data.broadinstitute.org/igv/projects/downloads/2.5/IGV_Linux_2.5.0.zip
```


```
$ java -Djava.awt.headless=true -Dproduction=true -Djava.net.preferIPv4Stack=true -Dsun.java2d.noddraw=true  -jar /home/wuzhikun/anaconda3/envs/NanoSV/bin/IGV-snapshot-automator/bin/IGV_2.3.81/igv.jar    -b IGV_snapshots.bat
INFO [2019-04-04 10:42:39,028]  [DirectoryManager.java:169] [main]  IGV Directory: /home/wuzhikun/igv
INFO [2019-04-04 10:42:39,028] [DirectoryManager.java:169]  IGV Directory: /home/wuzhikun/igv
INFO [2019-04-04 10:42:39,033]  [Main.java:133] [main]  Startup  IGV Version 2.3.81 (127)08/30/2016 02:20 PM
INFO [2019-04-04 10:42:39,033]  [Main.java:134] [main]  Java 1.8.0_192
INFO [2019-04-04 10:42:39,034]  [DirectoryManager.java:72] [main]  Fetching user directory... 
INFO [2019-04-04 10:42:39,116]  [Main.java:135] [main]  Default User Directory: /home/wuzhikun
INFO [2019-04-04 10:42:39,116]  [Main.java:136] [main]  OS: Linux
ERROR [2019-04-04 10:42:39,274]  [Main.java:199] [main]  Error checking version
java.net.UnknownHostException: www.broadinstitute.org
	at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:184)
	at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392)
	at java.net.Socket.connect(Socket.java:589)
	at sun.net.NetworkClient.doConnect(NetworkClient.java:175)
	at sun.net.www.http.HttpClient.openServer(HttpClient.java:463)
	at sun.net.www.http.HttpClient.openServer(HttpClient.java:558)
	at sun.net.www.http.HttpClient.<init>(HttpClient.java:242)
	at sun.net.www.http.HttpClient.New(HttpClient.java:339)
	at sun.net.www.http.HttpClient.New(HttpClient.java:357)
	at sun.net.www.protocol.http.HttpURLConnection.getNewHttpClient(HttpURLConnection.java:1220)
	at sun.net.www.protocol.http.HttpURLConnection.plainConnect0(HttpURLConnection.java:1199)
	at sun.net.www.protocol.http.HttpURLConnection.plainConnect(HttpURLConnection.java:1050)
	at sun.net.www.protocol.http.HttpURLConnection.connect(HttpURLConnection.java:984)
	at sun.net.www.protocol.http.HttpURLConnection.getInputStream0(HttpURLConnection.java:1564)
	at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1492)
	at java.net.HttpURLConnection.getResponseCode(HttpURLConnection.java:480)
	at org.broad.igv.util.HttpUtils.openConnection(HttpUtils.java:718)
	at org.broad.igv.util.HttpUtils.openConnection(HttpUtils.java:623)
	at org.broad.igv.util.HttpUtils.openConnection(HttpUtils.java:619)
	at org.broad.igv.util.HttpUtils.getContentsAsString(HttpUtils.java:143)
	at org.broad.igv.util.HttpUtils.getContentsAsString(HttpUtils.java:136)
	at org.broad.igv.ui.Main.checkVersion(Main.java:172)
	at org.broad.igv.ui.Main.initApplication(Main.java:147)
	at org.broad.igv.ui.Main.main(Main.java:87)
ERROR [2019-04-04 10:42:39,280]  [DefaultExceptionHandler.java:49] [main]  Unhandled exception
java.awt.HeadlessException
	at java.awt.GraphicsEnvironment.checkHeadless(GraphicsEnvironment.java:204)
	at java.awt.Window.<init>(Window.java:536)
	at java.awt.Frame.<init>(Frame.java:420)
	at java.awt.Frame.<init>(Frame.java:385)
	at javax.swing.JFrame.<init>(JFrame.java:189)
	at org.broad.igv.ui.Main.main(Main.java:89)
INFO [2019-04-04 10:42:39,282]  [ShutdownThread.java:51] [Thread-2]  Shutting down
```

```
$ java -Djava.awt.headless=true -Dproduction=true -Djava.net.preferIPv4Stack=true   -jar /home/wuzhikun/anaconda3/envs/NanoSV/bin/IGV-snapshot-automator/bin/IGV_2.3.81/igv.jar   -b /home/wuzhikun/Project/NanoTrio/IGV_test/IGV_snapshots.bat

INFO [2019-04-10 09:11:49,579]  [DirectoryManager.java:169] [main]  IGV Directory: /home/wuzhikun/igv
INFO [2019-04-10 09:11:49,579] [DirectoryManager.java:169]  IGV Directory: /home/wuzhikun/igv
INFO [2019-04-10 09:11:49,584]  [Main.java:133] [main]  Startup  IGV Version 2.3.81 (127)08/30/2016 02:20 PM
INFO [2019-04-10 09:11:49,584]  [Main.java:134] [main]  Java 1.8.0_121
INFO [2019-04-10 09:11:49,584]  [DirectoryManager.java:72] [main]  Fetching user directory... 
INFO [2019-04-10 09:11:49,655]  [Main.java:135] [main]  Default User Directory: /home/wuzhikun
INFO [2019-04-10 09:11:49,655]  [Main.java:136] [main]  OS: Linux
INFO [2019-04-10 09:11:53,309]  [Main.java:184] [main]  A later version of IGV is available (2.3.93)
ERROR [2019-04-10 09:11:53,319]  [DefaultExceptionHandler.java:49] [main]  Unhandled exception
java.awt.HeadlessException
	at java.awt.GraphicsEnvironment.checkHeadless(Unknown Source)
	at java.awt.Window.<init>(Unknown Source)
	at java.awt.Frame.<init>(Unknown Source)
	at java.awt.Frame.<init>(Unknown Source)
	at javax.swing.JFrame.<init>(Unknown Source)
	at org.broad.igv.ui.Main.main(Main.java:89)
INFO [2019-04-10 09:11:53,324]  [ShutdownThread.java:51] [Thread-2]  Shutting down
```




### run IGV

you should get into the directory "/home/wuzhikun/anaconda3/envs/NanoSV/bin/IGV-snapshot-automator"

```
$ python make_IGV_snapshots.py    -r /home/wuzhikun/Project/NanoTrio/IGV_test/target_region.bed  -g hg38 -o /home/wuzhikun/Project/NanoTrio/IGV_test  -nf4  /home/wuzhikun/Project/NanoTrio/mapping/minimap2/M625-0.bam

~~~ IGV SNAPSHOT AUTOMATOR ~~~

Reference genome:
hg38

Track height:
500

IGV binary file:
bin/IGV_2.3.81/igv.jar

Output directory will be:
/home/wuzhikun/Project/NanoTrio/IGV_test

Batchscript file will be:
/home/wuzhikun/Project/NanoTrio/IGV_test/IGV_snapshots.bat

Region file:
/home/wuzhikun/Project/NanoTrio/IGV_test/target_region.bed

Input files to snapshot:

/home/wuzhikun/Project/NanoTrio/mapping/minimap2/M625-0.bam

Making the output directory...

Writing IGV batch script to file:
/home/wuzhikun/Project/NanoTrio/IGV_test/IGV_snapshots.bat


Getting regions from BED file...

Read 2 regions

Open Xvfb port found on:
1


IGV command is:
xvfb-run --auto-servernum --server-num=1 java -Xmx4000m -jar bin/IGV_2.3.81/igv.jar -b /home/wuzhikun/Project/NanoTrio/IGV_test/IGV_snapshots.bat


Current time is:
2019-04-03 18:39:35.104975


Running the IGV command...
/bin/sh: xvfb-run: command not found
b''

IGV finished; elapsed time is:
0:00:00.012704

```



### igv_session.xml

```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<Session genome="F:\课题\genome\Homo_sapiens.GRCh38.dna.primary_assembly.fa" hasGeneTrack="false" hasSequenceTrack="true" locus="1:154712587-154716775" path="F:\data\igv_session.xml" version="8">
    <Resources>
        <Resource path="F:\data\M625-2_chr1.bam"/>
        <Resource path="F:\data\M625-0_chr1.bam"/>
    </Resources>
    <Panel height="380" name="Panel1554792170992" width="1715">
        <Track autoScale="true" clazz="org.broad.igv.sam.CoverageTrack" color="175,175,175" colorScale="ContinuousColorScale;0.0;10.0;255,255,255;175,175,175" fontSize="10" id="F:\data\M625-0_chr1.bam_coverage" name="M625-0_chr1.bam Coverage" snpThreshold="0.2" visible="true">
            <DataRange baseline="0.0" drawBaseline="true" flipAxis="false" maximum="20.0" minimum="0.0" type="LINEAR"/>
        </Track>
        <Track clazz="org.broad.igv.sam.SpliceJunctionTrack" fontSize="10" height="60" id="F:\data\M625-0_chr1.bam_junctions" name="M625-0_chr1.bam Junctions" visible="false"/>
        <Track clazz="org.broad.igv.sam.AlignmentTrack" displayMode="EXPANDED" experimentType="OTHER" fontSize="10" id="F:\data\M625-0_chr1.bam" name="M625-0_chr1.bam" visible="true">
            <RenderOptions/>
        </Track>
    </Panel>
    <Panel height="366" name="Panel1554792189303" width="1715">
        <Track autoScale="true" clazz="org.broad.igv.sam.CoverageTrack" color="175,175,175" colorScale="ContinuousColorScale;0.0;10.0;255,255,255;175,175,175" fontSize="10" id="F:\data\M625-2_chr1.bam_coverage" name="M625-2_chr1.bam Coverage" snpThreshold="0.2" visible="true">
            <DataRange baseline="0.0" drawBaseline="true" flipAxis="false" maximum="20.0" minimum="0.0" type="LINEAR"/>
        </Track>
        <Track clazz="org.broad.igv.sam.SpliceJunctionTrack" fontSize="10" height="60" id="F:\data\M625-2_chr1.bam_junctions" name="M625-2_chr1.bam Junctions" visible="false"/>
        <Track clazz="org.broad.igv.sam.AlignmentTrack" displayMode="EXPANDED" experimentType="OTHER" fontSize="10" id="F:\data\M625-2_chr1.bam" name="M625-2_chr1.bam" visible="true">
            <RenderOptions/>
        </Track>
    </Panel>
    <Panel height="380" name="Panel1554792386077" width="1715">
        <Track autoScale="true" clazz="org.broad.igv.sam.CoverageTrack" color="175,175,175" colorScale="ContinuousColorScale;0.0;10.0;255,255,255;175,175,175" fontSize="10" id="F:\data\M625-0_chr1.bam_coverage" name="M625-0_chr1.bam Coverage" snpThreshold="0.2" visible="true">
            <DataRange baseline="0.0" drawBaseline="true" flipAxis="false" maximum="20.0" minimum="0.0" type="LINEAR"/>
        </Track>
        <Track clazz="org.broad.igv.sam.SpliceJunctionTrack" fontSize="10" height="60" id="F:\data\M625-0_chr1.bam_junctions" name="M625-0_chr1.bam Junctions" visible="false"/>
        <Track clazz="org.broad.igv.sam.AlignmentTrack" displayMode="EXPANDED" experimentType="OTHER" fontSize="10" id="F:\data\M625-0_chr1.bam" name="M625-0_chr1.bam" visible="true">
            <RenderOptions/>
        </Track>
    </Panel>
    <Panel height="22" name="FeaturePanel" width="1715">
        <Track clazz="org.broad.igv.track.SequenceTrack" fontSize="10" id="Reference sequence" name="Reference sequence" visible="true"/>
    </Panel>
    <PanelLayout dividerFractions="0.008928571428571428,0.33163265306122447,0.6862244897959183,0.9655612244897959"/>
    <HiddenAttributes>
        <Attribute name="DATA FILE"/>
        <Attribute name="DATA TYPE"/>
        <Attribute name="NAME"/>
    </HiddenAttributes>
</Session>


```
