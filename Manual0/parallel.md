## parallel

### install parallel
```
$ conda install -c bioconda parallel
```


### [parallel example](https://linux.cn/article-9718-1.html)
```
$ find . -name "*jpeg" | parallel -I% --max-args 1 convert % %.png
```
* find . -name "*jpeg" 查找当前目录下以 jpeg 结尾的所有文件。
parallel 调用 GNU Parallel。
* -I% 创建了一个占位符 %，代表 find 传递给 Parallel 的内容。如果不使用占位符，你需要对 find 命令的每一个结果手动编写一个命令，而这恰恰是你想要避免的。
* --max-args 1 给出 Parallel 从队列获取新对象的速率限制。考虑到 Parallel 运行的命令只需要一个文件输入，这里将速率限制设置为 1。假如你需要执行更复杂的命令，需要两个文件输入（例如 cat 001.txt 002.txt > new.txt），你需要将速率限制设置为 2。
* convert % %.png 是你希望 Parallel 执行的命令。

```
$ ls -1 | parallel --max-args=2 cat {1} {2} ">" {1}_{2}.person
```

### parallel manual
```
$ cat /home/wzk/Project/C128/annotate/Mix/sprot.faa | parallel --gnu --plain -j 10 --block 2504139 --recstart '>' --pipe blastp -query - -db /home/wzk/anaconda3/envs/qiime/bin/../db/kingdom/Bacteria/sprot -evalue 1e-06 -num_threads 1 -num_descriptions 1 -num_alignments 1 -seg no > /home/wzk/Project/C128/annotate/Mix/sprot.blast 2> /dev/null
```

### parallel example

```
$ less gene_association.tair

TAIR    locus:2150931   TDP1            GO:0000012      TAIR:Communication:501741973    IBA     PANTHER:PTN000275870    P       AT5G15170       AT5G15170|TDP1|tyrosyl-DNA phosphodiesterase 1|F8M21.60|F8M21_60        protein taxon:3702      20161023        GOC             
TAIR    locus:2045437   RAD50           GO:0000014      TAIR:Communication:501741973    IBA     PANTHER:PTN000429848    F       AT2G31970       AT2G31970|RAD50|ATRAD50|F22D22.28|F22D22_28|dna repair-recombination protein    protein taxon:3702      20160323        GOC             
```


```
$ parallel --pipe --block 2M grep TDP1  <  gene_association.tair
```

```
$ parallel -j100% --pipepart --block 100M -a <very large SEEKABLE file> grep <...>
```


