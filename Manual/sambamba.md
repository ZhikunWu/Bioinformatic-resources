## sambamba

### sambamba view
```
sambamba view --sam-input --nthreads 20 --format bam --output-filename nanopore_test_sambamba.bam  nanopore_test.sam
```

### sort bam file
```
sambamba sort --nthreads 20 -o nanopore_test_sorted_sambamba.bam nanopore_test_sambamba.bam
```


