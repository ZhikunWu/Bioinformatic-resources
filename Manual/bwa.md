

##### bwa index
```
$ bwa index Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa
[bwa_index] Pack FASTA... 2.36 sec
[bwa_index] Construct BWT for the packed sequence...
[BWTIncCreate] textLength=497912844, availableWord=47034604
[BWTIncConstructFromPacked] 10 iterations done. 76325452 characters processed.
[BWTIncConstructFromPacked] 20 iterations done. 142216380 characters processed.
[BWTIncConstructFromPacked] 30 iterations done. 200776364 characters processed.
[BWTIncConstructFromPacked] 40 iterations done. 252820604 characters processed.
[BWTIncConstructFromPacked] 50 iterations done. 299073676 characters processed.
[BWTIncConstructFromPacked] 60 iterations done. 340179500 characters processed.
[BWTIncConstructFromPacked] 70 iterations done. 376710428 characters processed.
[BWTIncConstructFromPacked] 80 iterations done. 409175164 characters processed.
[BWTIncConstructFromPacked] 90 iterations done. 438025868 characters processed.
[BWTIncConstructFromPacked] 100 iterations done. 463664428 characters processed.
[BWTIncConstructFromPacked] 110 iterations done. 486447996 characters processed.
[bwt_gen] Finished constructing BWT in 116 iterations.
[bwa_index] 219.97 seconds elapse.
[bwa_index] Update BWT... 1.51 sec
[bwa_index] Pack forward-only FASTA... 1.58 sec
[bwa_index] Construct SA from BWT and Occ... 62.23 sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa index Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa
[main] Real time: 291.296 sec; CPU: 287.657 sec
```

output files:
```
-rw-rw-r-- 1 2.5K Mar 13 09:23 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.amb
-rw-rw-r-- 1   42 Mar 13 09:23 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.ann
-rw-rw-r-- 1 238M Mar 13 09:23 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.bwt
-rw-rw-r-- 1  60M Mar 13 09:23 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.pac
-rw-rw-r-- 1 119M Mar 13 09:24 Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.sa
```


md5 values of bwa index files:

```
47997f660faccd1be87233bbad329fa7  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa
6739d5324c62df1f2eb2111ec7805883  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.amb
be6c479b42a059dd2f0e1ef22c3dab99  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.ann
4bb7ca0c4e6e83affbbdce8e9f167ab3  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.bwt
51eb8221d49a2feed5014be302712f1c  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.pac
f246f56edc0e66ed9d233d8184d86776  Homo_sapiens.GRCh38.dna.primary_assembly_chr1.fa.sa
```

