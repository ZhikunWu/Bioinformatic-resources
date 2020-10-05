### [MISA - MIcroSAtellite identification tool](http://pgrc.ipk-gatersleben.de/misa/)
the specification file
```
$ cat misa.ini
definition(unit_size,min_repeats):                   2-6 3-5 4-5 5-5 6-5
interruptions(max_difference_between_2_SSRs):        100
 
 ```

 ### run MISA
 ```
 $ perl /home/wzk/anaconda3/envs/evolution/bin/misa.pl  /home/wzk/Project/AtGenome/pilon/ERR2173373/ERR2173372.fasta misa.ini
 ```

 output file **/home/wzk/Project/AtGenome/pilon/ERR2173373/ERR2173372.fasta.statistics**
 ```
 $ less

 RESULTS OF MICROSATELLITE SEARCH
 ================================

 Total number of sequences examined:              62
 Total size of examined sequences (bp):           119588202
 Total number of identified SSRs:                 15560
 Number of SSR containing sequences:              52
 Number of sequences containing more than 1 SSR:  39
 Number of SSRs present in compound formation:    1179


 Distribution to different repeat type classes
 ---------------------------------------------

 Unit size       Number of SSRs
 2       9454
 3       5655
 4       162
 5       48
 6       241

 Frequency of identified SSR motifs
 ----------------------------------

 Repeats 5       6       7       8       9       10      11      12      13      14      15      16      17      18      19      20      21      22
 AC      -       124     74      30      28      15      8       5       3       1               1       3               1                       
 AG      -       451     246     168     88      47      25      13      12      7       13      6       3       3       3       3       1       

 ```

