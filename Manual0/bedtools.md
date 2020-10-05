## bedtools

### install bedtools
```
$ conda install -c bioconda bedtools 
```

### bedtools get fasta
```
$ bedtools getfasta -fi Oryza_sativa.IRGSP-1.0.dna.toplevel.fa -bed fasta.bed -fo rice_chr1

$ bedtools getfasta -fi Oryza_sativa.IRGSP-1.0.dna.toplevel.fa -bed fasta.bed | fold -w 60 > rice_chr1
```


```
$ bedtools getfasta -fi /home/wzk/database/GENOME/rice/Oryza_indica/Oryza_indica.ASM465v1.dna.toplevel.fa -bed fasta.bed | fold -w 60 > Oryza_indica_chr1_trunced.fasta

$ bedtools getfasta -fi /home/wzk/database/GENOME/rice/Oryza_sativa/Oryza_sativa.IRGSP-1.0.dna.toplevel.fa  -bed fasta.bed | fold -w 60 > Oryza_sativa_chr1_trunced.fasta

$ lastz Oryza_indica_chr1_trunced.fasta Oryza_sativa_chr1_trunced.fasta --gfextend --chain --gapped --format=maf
```

