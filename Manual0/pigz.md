## pigz

### parallele gzip 
```
$ conda install -c conda-forge pigz
```

### pigz
```
$ pigz 
Usage: pigz [options] [files ...]
  will compress files in place, adding the suffix '.gz'.  If no files are
  specified, stdin will be compressed to stdout.  pigz does what gzip does,
  but spreads the work over multiple processors and cores when compressing.

Options:
  -0 to -9, -11        Compression level (level 11, zopfli, is much slower)
  --fast, --best       Compression levels 1 and 9 respectively
  -b, --blocksize mmm  Set compression block size to mmmK (default 128K)
  -c, --stdout         Write all processed output to stdout (won't delete)
  -d, --decompress     Decompress the compressed input
  -f, --force          Force overwrite, compress .gz, links, and to terminal
  -F  --first          Do iterations first, before block split for -11
  -h, --help           Display a help screen and quit
  -i, --independent    Compress blocks independently for damage recovery
  -I, --iterations n   Number of iterations for -11 optimization
  -k, --keep           Do not delete original file after processing
  -K, --zip            Compress to PKWare zip (.zip) single entry format
  -l, --list           List the contents of the compressed input
  -L, --license        Display the pigz license and quit
  -M, --maxsplits n    Maximum number of split blocks for -11
  -n, --no-name        Do not store or restore file name in/from header
  -N, --name           Store/restore file name and mod time in/from header
  -O  --oneblock       Do not split into smaller blocks for -11
  -p, --processes n    Allow up to n compression threads (default is the
                       number of online processors, or 8 if unknown)
  -q, --quiet          Print no messages, even on error
  -r, --recursive      Process the contents of all subdirectories
  -R, --rsyncable      Input-determined block locations for rsync
  -S, --suffix .sss    Use suffix .sss instead of .gz (for compression)
  -t, --test           Test the integrity of the compressed input
  -T, --no-time        Do not store or restore mod time in/from header
  -v, --verbose        Provide more verbose output
  -V  --version        Show the version of pigz
  -z, --zlib           Compress to zlib (.zz) instead of gzip format
  --                   All arguments after "--" are treated as files

```

### unpigz
```
$ unpigz
Usage: pigz [options] [files ...]
  will compress files in place, adding the suffix '.gz'.  If no files are
  specified, stdin will be compressed to stdout.  pigz does what gzip does,
  but spreads the work over multiple processors and cores when compressing.

Options:
  -0 to -9, -11        Compression level (level 11, zopfli, is much slower)
  --fast, --best       Compression levels 1 and 9 respectively
  -b, --blocksize mmm  Set compression block size to mmmK (default 128K)
  -c, --stdout         Write all processed output to stdout (won't delete)
  -d, --decompress     Decompress the compressed input
  -f, --force          Force overwrite, compress .gz, links, and to terminal
  -F  --first          Do iterations first, before block split for -11
  -h, --help           Display a help screen and quit
  -i, --independent    Compress blocks independently for damage recovery
  -I, --iterations n   Number of iterations for -11 optimization
  -k, --keep           Do not delete original file after processing
  -K, --zip            Compress to PKWare zip (.zip) single entry format
  -l, --list           List the contents of the compressed input
  -L, --license        Display the pigz license and quit
  -M, --maxsplits n    Maximum number of split blocks for -11
  -n, --no-name        Do not store or restore file name in/from header
  -N, --name           Store/restore file name and mod time in/from header
  -O  --oneblock       Do not split into smaller blocks for -11
  -p, --processes n    Allow up to n compression threads (default is the
                       number of online processors, or 8 if unknown)
  -q, --quiet          Print no messages, even on error
  -r, --recursive      Process the contents of all subdirectories
  -R, --rsyncable      Input-determined block locations for rsync
  -S, --suffix .sss    Use suffix .sss instead of .gz (for compression)
  -t, --test           Test the integrity of the compressed input
  -T, --no-time        Do not store or restore mod time in/from header
  -v, --verbose        Provide more verbose output
  -V  --version        Show the version of pigz
  -z, --zlib           Compress to zlib (.zz) instead of gzip format
  --                   All arguments after "--" are treated as files
```

### compress files
#### compress files
```
$ pigz -6 -p 10 -k filename
```

output file filename.gz

#### compress directory
```
$ tar cv filename | pigz -6 -p 10 -k > filename.tar.gz
```
