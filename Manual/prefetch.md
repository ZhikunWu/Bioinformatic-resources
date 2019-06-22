## prefetch


```
$ prefetch -h 
Usage:
  prefetch [options] <SRA accession | kart file> [...]
  Download SRA or dbGaP files and their dependencies

  prefetch [options] <SRA file> [...]
  Check SRA file for missed dependencies and download them

  prefetch --list <kart file> [...]
  List the content of a kart file

Options:
  -f|--force <value>               force object download one of: no, yes, 
                                   all. no [default]: skip download if the 
                                   object if found and complete; yes: download 
                                   it even if it is found and is complete; all: 
                                   ignore lock files (stale locks or it is 
                                   being downloaded by another process: use at 
                                   your own risk!) 

  -t|--transport <value>           transport: one of: ascp; http; both. (ascp 
                                   only; http only; first try ascp, use http 
                                   if cannot download by ascp). Default: both 
  -l|--list                        list the content of kart file 
  -n|--numbered-list               list the content of kart file with kart 
                                   row numbers 
  -s|--list-sizes                  list the content of kart file with target 
                                   file sizes 
  -R|--rows <rows>                 kart rows (default all). row list should be 
                                   ordered 
  -N|--min-size <size>             minimum file size to download in KB 
                                   (inclusive). 
  -X|--max-size <size>             maximum file size to download in KB 
                                   (exclusive). Default: 20G 
  -o|--order <value>               kart prefetch order: one of: kart, size. (in 
                                   kart order, by file size: smallest first), 
                                   default: size 
  -a|--ascp-path <ascp-binary|private-key-file>  path to ascp program and 
                                   private key file (asperaweb_id_dsa.putty) 
  --ascp-options <value>           arbitrary options to pass to ascp command 
                                   line 
  -p|--progress <value>            time period in minutes to display download 
                                   progress (0: no progress), default: 1 
  --eliminate-quals                don't download QUALITY column 

  -c|--check-all                   double-check all refseqs 

  -h|--help                        Output brief explanation for the program. 
  -V|--version                     Display the version of the program then 
                                   quit. 
  -L|--log-level <level>           Logging level as number or enum string. One 
                                   of (fatal|sys|int|err|warn|info|debug) or 
                                   (0-6) Current/default is warn 
  -v|--verbose                     Increase the verbosity of the program 
                                   status messages. Use multiple times for more 
                                   verbosity. Negates quiet. 
  -q|--quiet                       Turn off all status messages for the 
                                   program. Negated by verbose. 
  --option-file <file>             Read more options and parameters from the 
                                   file. 

prefetch : 2.5.7
```



```
$ /home/wuzhikun/anaconda3/envs/WGS/bin/prefetch     --ascp-path "/home/wuzhikun/.aspera/connect|/etc/asperaweb_id_dsa.putty" SRR576933
Maximum file size download limit is 20,971,520KB

2019-06-06T06:33:18 prefetch.2.5.7 err: path not found while resolving tree within virtual file system module - 'SRR576933' cannot be found.

```



### ascp
```
$ ~/.aspera/connect/bin/ascp --help
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
  --allow-password-prompt         Prompts for user password entry on ssh connection
  --ignore-host-key               Prompts for user password entry on ssh connection (deprecated)
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

### openssh
```
$ cat  ~/.aspera/connect/etc/asperaweb_id_dsa.openssh
-----BEGIN DSA PRIVATE KEY-----
MIIBuwIBAAKBgQDkKQHD6m4yIxgjsey6Pny46acZXERsJHy54p/BqXIyYkVOAkEp
KgvT3qTTNmykWWw4ovOP1+Di1c/2FpYcllcTphkWcS8lA7j012mUEecXavXjPPG0
i3t5vtB8xLy33kQ3e9v9/Lwh0xcRfua0d5UfFwopBIAXvJAr3B6raps8+QIVALws
yeqsx3EolCaCVXJf+61ceJppAoGAPoPtEP4yzHG2XtcxCfXab4u9zE6wPz4ePJt0
UTn3fUvnQmJT7i0KVCRr3g2H2OZMWF12y0jUq8QBuZ2so3CHee7W1VmAdbN7Fxc+
cyV9nE6zURqAaPyt2bE+rgM1pP6LQUYxgD3xKdv1ZG+kDIDEf6U3onjcKbmA6ckx
T6GavoACgYEAobapDv5p2foH+cG5K07sIFD9r0RD7uKJnlqjYAXzFc8U76wXKgu6
WXup2ac0Co+RnZp7Hsa9G+E+iJ6poI9pOR08XTdPly4yDULNST4PwlfrbSFT9FVh
zkWfpOvAUc8fkQAhZqv/PE6VhFQ8w03Z8GpqXx7b3NvBR+EfIx368KoCFEyfl0vH
Ta7g6mGwIMXrdTQQ8fZs
-----END DSA PRIVATE KEY-----

```