# Get reads based on FLAG for bam

### Flag description for bam:
```
Flag        Chr     Description
0x0001      p       the read is paired in sequencing
0x0002      P       the read is mapped in a proper pair
0x0004      u       the query sequence itself is unmapped
0x0008      U       the mate is unmapped
0x0010      r       strand of the query (1 for reverse)
0x0020      R       strand of the mate
0x0040      1       the read is the first read in a pair
0x0080      2       the read is the second read in a pair
0x0100      s       the alignment is not primary
0x0200      f       the read fails platform/vendor quality checks
0x0400      d       the read is either a PCR or an optical duplicate
```

#### Get reads based on flag

Get the unmapped reads from a bam:
```
samtools view -b -f 4 file.bam > unmapped.bam
```

To get only the mapped reads use the parameter 'F', which works like -v of grep and skips the alignments for a specific flag.
```
samtools view -b -F 4 file.bam > mapped.bam
```


Get all the reads where both mapped:
```
samtools view -F 12 whatever.bam
```


Get all the reads that did not map, but whose mate mapped:
```
samtools view -f 4 -F 8 whatever.bam
```


Get all the reads that mapped, but whose mates did not:
```
samtools view -f 8 -F 4 whatever.bam
```

Get all the reads where neither one mapped:
```
samtools view -f 12 whatever.bam
```


