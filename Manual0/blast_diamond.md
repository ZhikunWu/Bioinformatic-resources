## Blast for nulceotide sequence

### Install blast
```
$ conda install -c bioconda blast 
```

### Make the database for blast

```
$ makeblastdb -in miRNA.fa -dbtype nucl -parse_seqids
```

### Run blast
```
$ blastn -query /home/wzk/Project/B120_20180822/UID_16S/UID/LGP0-FB-1_test_cut45.R2.fasta  -db  /home/wzk/test/miRNA.fa  -outfmt "6 qseqid sseqid  evalue qlen length pident mismatch gapopen qstart qend sstart send  stitle" -max_target_seqs 5 -out /home/wzk/Project/B120_20180822/UID_16S/UID/LGP0-FB-1_test_cut45.R2_NT_miRNA_adapter_blast.txt -num_threads 10 -evalue 0.00001
```

## [Diomond](https://github.com/bbuchfink/diamond) for blasting amino acid sequence

### Install diamond
```
$ conda install -c bioconda diamond
```

### make the database for reference amino acid sequence
```
$ diamond makedb --in phi45.fas -d phi45
```

It created the database with name of **phi45.dmnd** based on the prefix name **phi45**

### run diamond
```
$ diamond blastp --db phi45.dmnd --query representive-1.faa --threads 20 --evalue 0.00001 --max-target-seqs 1 --out PHI_diamond_out.txt --outfmt 6 qseqid sseqid  evalue qlen length pident mismatch gapopen qstart qend sstart send  stitle
```

**note**: 

* Two steps, making the database and alignment of sequence should use the same version of diamond, or else it will go wrong.

* It can also align the nucleotides to amino acids, then it should use the mode **blastx**



