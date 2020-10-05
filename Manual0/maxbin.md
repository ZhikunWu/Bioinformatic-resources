## [maxbin](https://downloads.jbei.org/data/microbial_communities/MaxBin/MaxBin.html): https://github.com/upendrak/MaxBin-2.2

### install maxbin
```bash
$ conda install -c bioconda maxbin2 
```

## Binning the assembly
```bash
$ samtools idxstats ../mapping/HMP_GUT_SRS052697.25M.mapped.sorted.bam >  HMP_GUT_SRS052697.25M.idxstats.txt

$ samtools idxstats ../mapping/HMP_MOCK_SRR2726667_8.25M.mapped.sorted.bam > HMP_MOCK_SRR2726667_8.25M.idxstats.txt

$ cut -f1,3 HMP_GUT_SRS052697.25M.idxstats.txt > HMP_GUT_SRS052697.25M.counts
$ cut -f1,3 HMP_MOCK_SRR2726667_8.25M.idxstats.txt > HMP_MOCK_SRR2726667_8.25M.counts
$ ls *counts > abundance.list

$ run_MaxBin.pl -contig ../assembly/Meta.contigs_cut.fa -abund_list abundance.list -max_iteration 5 -out mbin -thread 20
```

output files:
```
$ tree
.
├── mbin.001.fasta
├── mbin.002.fasta
├── mbin.003.fasta
├── mbin.004.fasta
├── mbin.005.fasta
├── mbin.006.fasta
├── mbin.007.fasta
├── mbin.008.fasta
├── mbin.009.fasta
├── mbin.010.fasta
├── mbin.abundance
├── mbin.log
├── mbin.marker
├── mbin.marker_of_each_bin.tar.gz
├── mbin.noclass
├── mbin.summary
└── mbin.tooshort
```

generate a concatenated file that contains all of our genome bins put together.
```bash
for file in mbin.*.fasta
  do
    num=${file//[!0-9]/}
    sed -e "/^>/ s/$/ ${num}/" mbin.$num.fasta >> binned.concat.fasta
  done
 ```

And finally make an annotation file for visualization:
```bash
echo label > annotation.list
grep ">" binned.concat.fasta |cut -f2 -d ' '>> annotation.list
```


problem
```
run_MaxBin.pl -contig /home/wzk/meta_test/assembly/merged/MetaContig.fa -abund_list /home/wzk/meta_test/maxBin/count_list.txt -max_iteration 5 -out /home/wzk/meta_test/maxBin/bin -thread 4 2>>/home/wzk/meta_test/log/maxbin/mix.log
MaxBin 2.2.1
Input contig: /home/wzk/meta_test/assembly/merged/MetaContig.fa
Max iteration: 5
out header: /home/wzk/meta_test/maxBin/bin
Thread: 4
Located abundance file [/home/wzk/meta_test/maxBin/HMP_GUT_SRS052697.25M.count.txt]
Located abundance file [/home/wzk/meta_test/maxBin/HMP_MOCK_SRR2726667_8.25M.count.txt]
Located abundance file [/home/wzk/meta_test/maxBin/mix.count.txt]
Searching against 107 marker genes to find starting seed contigs for [/home/wzk/meta_test/assembly/merged/MetaContig.fa]...
Running FragGeneScan....
Running HMMER hmmsearch....
Try harder to dig out marker genes from contigs.
Marker gene search reveals that the dataset cannot be binned (the medium of marker gene number <= 1). Program stop.

```
