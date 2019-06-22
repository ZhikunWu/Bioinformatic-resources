
## aspera manual

### [Aspera工具安装与使用](https://www.jianshu.com/p/a6ac81456c01)

### install aspera
```
$ conda install -c hcc aspera-cli
```

or
```
$ wget https://download.asperasoft.com/download/sw/connect/3.8.1/ibm-aspera-connect-3.8.1.161274-linux-g2.12-64.tar.gz
```

如果安装报错，提示openssl版本过旧，那么我们还需要重新安装一个最近的openssl

```
#卸载旧版本的openssl
sudo apt-get remove openssl libssl-dev

#下载最近版本的openssl-1.0.2l.tar.gz

#安装openssl
./config
make
make install

#建立软连接
ln -s /usr/local/ssl/bin/openssl    /usr/bin/openssl
ln -s /usr/local/ssl/include/openssl    /usr/include/openssl

```


### aspera parameters
```
$ ascp --help
Usage: ascp [OPTION] SRC... DEST
          SRC to DEST, or multiple SRC to DEST dir
          SRC, DEST format: [[user@]host:]PATH
  -h,--help                       Display usage
  -A,--version                    Display version.
  -T                              Disable encryption
  -d                              Create target directory, implied for file/file-pair lists
  -p                              Preserve file timestamp
  -q                              Disable progress display
  -v                              Verbose mode
  -6                              Use IPv6
  -D...                           Debug level
  -l MAX-RATE                     Max transfer rate
  -m MIN-RATE                     Min transfer rate
                                  RATE: G/g(gig),M/m(meg),K/k(kilo)
  -u USER-STRING                  User-specific string
  -i PRIVATE-KEY-FILE             Private-key file name (id_rsa)
  -w DIRECTION                    Test bandwidth. DIRECTION: r,f
  -K PROBE-RATE                   Bandwidth measurement, probes/sec
  -k RESUME-LEVEL                 Resume criterion: 0,3,2,1
  -Z DATAGRAM-SIZE                Manually set MTU
  -g READ-SIZE                    File read-block size
  -G WRITE-SIZE                   File write-block size
                                  SIZE: K (kilo), M (meg), or just bytes
  -L LOCAL-LOG-DIR                Local logging directory path
  -R REMOTE-LOG-DIR               Remote logging directory path
  -S REMOTE-ASCP                  Name of remote ascp command line
  -e PRE-POST                     Pre and Post command file path
  -O FASP-PORT                    UDP port used for FASP transport
  -P SSH-PORT                     TCP port used for SSH authentication
  -C M-ID:N-COUNT                 Multi-session transfer, move only Mth of N parts
  -N PATTERN                      Inclusion pattern. Repeat for more.
  -E PATTERN                      Exclusion pattern. Repeat for more.
  -f CONFIG-FILE                  Configuration-file name
  -W TOKEN-STRING                 Specify TOKEN-STRING for transfer
  -@ RANGE-LOW:RANGE-HIGH         Transfer only a range of bytes within file
  -X REXMSG-SIZE                  Size of retransmit request
  -c CIPHER                       File data cipher:  aes128, aes192 or aes256
  --mode=MODE                     MODE: send, recv
  --user=USERNAME
  --host=HOSTNAME
  --policy=TRANSFER_POLICY        TRANSFER_POLICY: fixed,high,fair,low
  --file-list=FILENAME            File with list of sources
  --file-pair-list=FILENAME       File with list of src/dest pairs
  --source-prefix=PREFIX          Prepend to each SRC path
  --symbolic-links=METHOD         METHOD: follow,copy,copy+force,skip
  --remove-after-transfer         Remove SRC files after transfer success
  --move-after-transfer=ARCHIVE   Move SRC files under path ARCHIVE after transfer success
  --remove-empty-directories      Remove empty SRC subdirectories
  --remove-empty-source-directory Also remove the source directory itself if empty
  --save-before-overwrite         Rename file instead of overwrite
  --skip-special-files
  --file-manifest=OUTPUT          OUTPUT: text,none
  --file-manifest-path=DIRECTORY
  --file-manifest-inprogress-suffix=SUFFIX
  --precalculate-job-size
  --overwrite=METHOD              METHOD: never,always,older,diff,diff+older
  --file-crypt=CRYPT              CRYPT: encrypt,decrypt
  --file-checksum=HASH            HASH: sha-512,sha-384,sha-256,sha1,md5,none
  --partial-file-suffix=SUFFIX    Default is set to "" disabling
                                  the partial file usage
  --src-base=NAME                 Preserve directory structure of SRC
                                    arguments below NAME
  --proxy=URL
  --preserve-file-owner-uid
  --preserve-file-owner-gid
  --ignore-host-key               Ignore server SSH host key fingerprint
  --check-sshfp=FINGERPRINT       Required server SSH host key fingerprint
  --apply-local-docroot           Apply local docroot
  --preserve-xattrs=MODE          MODE: native,metafile,none
  --remote-preserve-xattrs=MODE   MODE: native,metafile,none
  --preserve-acls=MODE            MODE: native,metafile,none
  --remote-preserve-acls=MODE     MODE: native,metafile,none
  --multi-session-threshold=THRESHOLD
                                  Skip multi-session if file size
                                  is less than threshold
  --delete-before-transfer        Delete extraneous files from DEST
                                  before any files are transferred

  HTTP fallback only options:
  -y 0/1                          1 = Allow HTTP fallback (default = 0)
  -Y FILENAME                     HTTPS key file name
  -I FILENAME                     HTTPS certificate file name
  -t PORT                         HTTP fallback server port
  -x PROXYSERVER-ADDR[:PORT]      Proxy address and port (default 80)

```

### get private key
```
$ locate asperaweb_id_dsa.putty
/home/wzk/anaconda3/envs/qiime/opt/aspera/connect/etc/asperaweb_id_dsa.putty
/home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.putty
```

they are with identical md5 value
```
$ md5sum /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.putty /home/wzk/anaconda3/envs/qiime/opt/aspera/connect/etc/asperaweb_id_dsa.putty
53a34869873db3baf1e640c830cbd205  /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.putty
53a34869873db3baf1e640c830cbd205  /home/wzk/anaconda3/envs/qiime/opt/aspera/connect/etc/asperaweb_id_dsa.putty
```

### run

```
$ /home/wzk/anaconda3/envs/qiime/bin/ascp -T -w f -k1 -l 100M -P 33001  -i /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/SRR576/SRR576938/SRR576938.fastq.gz   /home/wzk 


Measuring bottleneck bandwidth from 193.62.193.135 to 219.140.149.68
SRR576938.fastq.gz                                                                                                     100%  244MB  112Mb/s    00:20    
Completed: 249998K bytes transferred in 21 seconds
 (94969K bits/sec), in 1 file.
Warning: interruption coalescing detected,bw measurement results may be highly inaccurate
Bandwidth measurement yields no results due to interrupt coalescing


```




```
$ /home/wzk/anaconda3/envs/qiime/bin/ascp -T -w f -P 33001    -i /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.openssh anonftp@ftp-private.ncbi.nlm.nih.gov:/sra/sra-instant/reads/ByExp/sra/SRX/SRX189/SRX189773/SRR576933/SRR576933.sra    /home/wzk
```


其次，还可以使用批量下载方法，首先我们需要创建一个记录了下载链接的文件file-list,其内容如下
```
/vol1/fastq/SRR576/SRR576933/SRR576933.fastq.gz
/vol1/fastq/SRR576/SRR576934/SRR576934.fastq.gz
```

and then run:
```
$ ascp -QT -k1 -l 100M -i ~/asperaweb_id_dsa.openssh --mode recv --host fasp.sra.ebi.ac.uk --user era-fasp --file-list file-list
```

### FAQ

* 若使用ssh登录服务器，运行命令后提示你要passphrase
```
Key passphrase:

```
将秘钥文件（**asperaweb_id_dsa.putty**）改成**asperaweb_id_dsa.openssh**

* 端口的问题
```
ascp: Failed to open TCP connection for SSH, exiting.

Session Stop  (Error: Failed to open TCP connection for SSH)
```

添加参数-P，默认端口30001



* **Session Stop**添加参数-T可以解决该问题
```
Session Stop  (Error: Server aborted session: Client requests stronger encryption than server allows)
```


* aspera默认不支持断点续传，要支持这个功能添加参数
```
ascp -k 1 
```


### download in a batch

以EBI上的SRR346368这套数据为例。首先到EBI页面里，找到你想要下载的文件，将指针移到这个文件的”ftp”这一列，即可看到其ftp地址，例如: ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR346/SRR346368/SRR346368.fastq.gz。

NCBI的SRA数据库也是同样的方法，即可获取其ascp下载地址.

#### download with a EBI ftp site
```
ftp.sra.ebi.ac.uk/vol1/run/ERR218/ERR2184694/FAF15586-82266371-Bham-R9.4-Ultra.tar.gz
```

we need change **ftp.sra.ebi.ac.uk** to **era-fasp@fasp.sra.ebi.ac.uk:**, and run like this:

```
$ /home/wzk/anaconda3/envs/qiime/bin/ascp -TQ -k1 -l 100M -P 33001  -i /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/run/ERR218/ERR2184694/FAF15586-82266371-Bham-R9.4-Ultra.tar.gz    /home/wzk 

FAF15586-82266371-Bham-R9.4-Ultra.tar.gz                                                                                 0%  126MB 96.7Mb/s    45:03 ETA
```


#### download in a bantch
the file with ftp sites:
```
$ cat PRJEB23027_test_run
/vol1/run/ERR218/ERR2184691/FAB42451-4239353418-Notts-R9.4-Ligation.tar.gz
/vol1/run/ERR218/ERR2184692/FAF15665-16056159-Notts-R9.4-Ultra.tar.gz
/vol1/run/ERR218/ERR2184693/FAF09701-4249180049-Bham-R9.4-Ultra.tar.gz
```

then run:
```
$ /home/wzk/anaconda3/envs/qiime/bin/ascp -TQ -k1 -l 100M -P 33001  -i /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.openssh --mode recv --host fasp.sra.ebi.ac.uk --user era-fasp --file-list PRJEB23027_test_run /home/wzk/Project/Other/NA12878

FAF09701-4249180049-Bham-R9.4-Ultra.tar.gz                                                                               1%  300MB 97.1Mb/s    44:21 ETA
```

### example

```
/home/wzk/anaconda3/envs/qiime/bin/ascp -TQ -k1 -l 100M -P 33001  -i /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.openssh --mode recv --host fasp.sra.ebi.ac.uk --user era-fasp --file-list sites /disk1/Project/KC2018-C128/PRJEB26791
```


```
$ cut -f 10  ERS2544835.txt | sed '1d' | sed 's/ftp\.sra\.ebi\.ac\.uk//g' > ERS2544835_sites.txt

$ /home/wzk/anaconda3/envs/qiime/bin/ascp -TQ -k1 -l 100M -P 33001  -i /home/wzk/anaconda3/pkgs/aspera-connect-3.7.2-0/opt/aspera/connect/etc/asperaweb_id_dsa.openssh --mode recv --host fasp.sra.ebi.ac.uk --user era-fasp --file-list ERS2544835_sites.txt /disk1/Project/KC2018-C128/PRJEB26791
```

