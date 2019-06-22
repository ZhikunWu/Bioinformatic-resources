## gtf to genepred

### gtf to genepred

```
$ conda install -c bioconda ucsc-gtftogenepred
```


### gtfToGenePred parameters
```
$ gtfToGenePred 
gtfToGenePred - convert a GTF file to a genePred
usage:
   gtfToGenePred gtf genePred

options:
     -genePredExt - create a extended genePred, including frame
      information and gene name
     -allErrors - skip groups with errors rather than aborting.
      Useful for getting infomation about as many errors as possible.
     -ignoreGroupsWithoutExons - skip groups contain no exons rather than
      generate an error.
     -infoOut=file - write a file with information on each transcript
     -sourcePrefix=pre - only process entries where the source name has the
      specified prefix.  May be repeated.
     -impliedStopAfterCds - implied stop codon in after CDS
     -simple    - just check column validity, not hierarchy, resulting genePred may be damaged
     -geneNameAsName2 - if specified, use gene_name for the name2 field
      instead of gene_id.
     -includeVersion - it gene_version and/or transcript_version attributes exist, include the version
      in the corresponding identifiers.
```

### run gtfToGenePred

```
$ gtfToGenePred -genePredExt -geneNameAsName2 Homo_sapiens.GRCh38.95.gtf Homo_sapiens.GRCh38.95.genepred
```

output file:
```
$ head Homo_sapiens.GRCh38.95.genepred
ENST00000456328 1   +   11868   14409   14409   14409   3   11868,12612,13220,  12227,12721,14409,  0   DDX11L1 none    none    -1,-1,-1,
ENST00000450305 1   +   12009   13670   13670   13670   6   12009,12178,12612,12974,13220,13452,    12057,12227,12697,13052,13374,13670,    0   DDX11L1 none    none-1,-1,-1,-1,-1,-1,
ENST00000488147 1   -   14403   29570   29570   29570   11  14403,15004,15795,16606,16857,17232,17605,17914,18267,24737,29533,  14501,15038,15947,16765,17055,17368,17742,18061,18366,24891,29570,  0   WASH7P  none    none    -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
ENST00000619216 1   -   17368   17436   17436   17436   1   17368,  17436,  0   MIR6859-1   none    none    -1,
ENST00000473358 1   +   29553   31097   31097   31097   3   29553,30563,30975,  30039,30667,31097,  0   MIR1302-2HG none    none    -1,-1,-1,
ENST00000469289 1   +   30266   31109   31109   31109   2   30266,30975,    30667,31109,    0   MIR1302-2HG none    none    -1,-1,
ENST00000607096 1   +   30365   30503   30503   30503   1   30365,  30503,  0   MIR1302-2   none    none    -1,
ENST00000417324 1   -   34553   36081   36081   36081   3   34553,35276,35720,  35174,35481,36081,  0   FAM138A none    none    -1,-1,-1,
ENST00000461467 1   -   35244   36073   36073   36073   2   35244,35720,    35481,36073,    0   FAM138A none    none    -1,-1,
ENST00000606857 1   +   52472   53312   53312   53312   1   52472,  53312,  0   OR4G4P  none    none    -1,

```