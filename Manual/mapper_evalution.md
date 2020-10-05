## [men-mapper (liheng)](https://github.com/lh3/mem-paper)



$ time bwa mem hs37m.fa r1.fa r2.fa > r12.mem.sam

[main] Version: 0.6.2-r311-beta
[main] CMD: ../bwa mem ../hs37m.fa r1.fa r2.fa
[main] Real time: 496.932 sec; CPU: 496.640 sec

real    8m17.012s
user    8m13.530s
sys     0m3.111s

$ time cat r1.fa r2.fa | bwa mem hs37m.fa - > r12-se.mem.sam

[main] Version: 0.6.2-r311-beta
[main] CMD: ../bwa mem ../hs37m.fa -
[main] Real time: 467.947 sec; CPU: 467.539 sec

real    7m48.012s
user    7m44.845s
sys     0m2.784s

$ time cat r1.fa r2.fa | gem-mapper -I hs37m-gem.gem -e 0.04 -m 0.04 -s 1 > r12-se.gem.map

real    5m14.239s
user    5m11.665s
sys     0m1.814s

$ time cat r1.fa r2.fa | gem-mapper -I hs37m-gem.gem -e5 -m5 -s1 > r12-se.gem-e5.map

real    7m11.411s
user    7m7.904s
sys     0m1.853s

$ time gem-mapper -I hs37m-gem.gem -1 r1.fa -2 r2.fa -e5 -m5 -s1 -pb > r12-se.gem-bp-e5-s1.map

real    8m51.228s
user    8m47.692s
sys     0m2.027s

$ time bowtie2 -x hs37m-bt2 -1 r1.fa -2 r2.fa -X 650 -f > r12-pe.bt2.sam

real    9m5.345s
user    9m2.610s
sys     0m2.005s

$ time cat r1.fa r2.fa | bowtie2 -x hs37m-bt2 -f - > r12-se.bt2.sam

real    9m45.121s
user    9m40.919s
sys     0m1.861s

$ (bwa aln default)

[main] Version: 0.6.2-r301-beta
[main] CMD: ../bwa aln ../hs37m.fa r1.fa
[main] Real time: 504.406 sec; CPU: 504.268 sec

real    8m24.408s
user    8m22.990s
sys     0m1.280s

[main] Version: 0.6.2-r301-beta
[main] CMD: ../bwa aln ../hs37m.fa r2.fa
[main] Real time: 507.282 sec; CPU: 507.142 sec

real    8m27.286s
user    8m25.868s
sys     0m1.275s

$ time bwa sampe hs37m.fa r1.bwa.sai r2.bwa.sai r1.fa r2.fa > r12.bwa.sam

[main] Version: 0.6.2-r301-beta
[main] CMD: ../bwa sampe ../hs37m.fa r1.bwa.sai r2.bwa.sai r1.fa r2.fa
[main] Real time: 83.975 sec; CPU: 81.579 sec

real    1m23.979s
user    1m13.906s
sys     0m7.673s

$ time bwa bwasw hs37m.fa r1.fa r2.fa

[main] Version: 0.6.2-r301-beta
[main] CMD: ../bwa bwasw ../hs37m.fa r1.fa r2.fa
[main] Real time: 1043.532 sec; CPU: 1043.139 sec

real    17m23.536s
user    17m17.776s
sys     0m5.364s

$ time cat r1.fa r2.fa | bwa bwasw hs37m.fa -

[main] Version: 0.6.2-r303-beta
[main] CMD: ../bwa bwasw ../hs37m.fa -
[main] Real time: 1004.568 sec; CPU: 1002.234 sec

$ time ../bwa mem -r 100 ../hs37m.fa r1.fa r2.fa > r12-pe.mem-fast.sam

[main] Version: 0.6.2-r311-beta
[main] CMD: ../bwa mem -r 100 ../hs37m.fa r1.fa r2.fa
[main] Real time: 287.196 sec; CPU: 285.622 sec

real    4m48.083s
user    4m42.895s
sys     0m2.727s

$ time cat r1.fa r2.fa | ../bwa mem -r 100 ../hs37m.fa - > r12-se.mem-fast.sam

[main] Version: 0.6.2-r311-beta
[main] CMD: ../bwa mem -r 100 ../hs37m.fa -
[main] Real time: 254.896 sec; CPU: 252.576 sec

real    4m14.899s
user    4m9.941s
sys     0m2.726s

$ (bwa samse, twice)

[main] Version: 0.6.2-r311-beta
[main] CMD: ../bwa samse ../hs37m.fa r1.bwa.sai r1.fa
[main] Real time: 24.007 sec; CPU: 21.996 sec

[main] Version: 0.6.2-r311-beta
[main] CMD: ../bwa samse ../hs37m.fa r2.bwa.sai r2.fa
[main] Real time: 24.096 sec; CPU: 22.040 sec

$ ./tmap mapall -f hs37m.fa -r r12.fa -n 1  -v stage1 map4 > r12-se.tmap.sam

real    11m37.692s
user    11m33.818s
sys     0m2.515s

$ time ./tmap mapall -f hs37m.fa -r ../101/r1.fa -r ../101/r2.fa -n 1 -Q 2 -L -l 3.0 -v stage1 map4 > r12-pe.tmap.sam

real    14m56.838s
user    14m50.425s
sys     0m2.854s

$ time ./novoalign -i 500 50 -oSAM -rRandom -dhs37m.novo -f ../101/r1.fq > r1-se.novo.sam

real    31m51.528s
user    31m45.881s
sys     0m4.216s

$ time ./novoalign -i 500 50 -oSAM -rRandom -dhs37m.novo -f ../101/r2.fq > r2-se.novo.sam

real    34m9.094s
user    34m4.498s
sys     0m3.851s

$ time ./novoalign -i 500 50 -oSAM -rRandom -dhs37m.novo -f ../101/r1.fq ../101/r2.fq > r12-pe.novo.sam

real    42m8.130s
user    42m1.657s
sys     0m4.954s

$ time cat r1.fq r2.fq | smalt-0.7.2/smalt_x86_64 map -f samsoft -o r12-se.smalt.sam ../hs37-smalt-k20s13 /dev/stdin

real    64m19.301s
user    64m15.500s
sys     0m3.790s

$ time smalt-0.7.2/smalt_x86_64 map -f samsoft -o r12-pe.smalt.sam -i 650 -j 450 ../hs37-smalt-k20s13 r1.fq r2.fq

real    28m27.861s
user    28m22.985s
sys     0m2.449s

$ time cat r1.fa r2.fa | bowtie2 --local -x ../../mapeval/hs37m-bt2 -f - > r12-se.bt2l.sam

real    13m16.911s
user    13m12.581s
sys     0m1.955s

$ time bowtie2 --local -x ../../mapeval/hs37m-bt2 -f -1 r1.fa -2 r2.fa -X 650 > r12-pe.bt2l.sam

real    16m52.420s
user    16m43.899s
sys     0m2.548s

$ time lastal -Q1 ../hs37-last r1.fq >r1-se.last.maf

real    25m50.591s
user    25m8.976s
sys     0m24.424s

$ time lastal -Q1 ../hs37-last r2.fq >r2-se.last.maf

real    25m9.357s
user    24m44.161s
sys     0m14.731s

$ time cat r1-se.last.maf r2-se.last.maf | last-278/scripts/last-map-probs.py -m 0.5 - | last-278/scripts/maf-convert.py sam - > r12-se.last.sam

real    16m38.894s
user    20m34.778s
sys     0m28.410s

$ time last-278/scripts/last-pair-probs.py -m 0.5 r1-se.last.maf r2-se.last.maf | last-278/scripts/maf-convert.py sam - > r12-pe.last.sam

real    98m10.114s
user    38m33.687s
sys     0m33.484s

$ time cushaw2-v2.1.8/cushaw2 -r ../../index/cushaw2/hs37m.fa -f r1.fa -o r1-se.cushaw.sam

real    7m59.908s
user    7m57.283s
sys     0m1.667s

$ time cushaw2-v2.1.8/cushaw2 -r ../../index/cushaw2/hs37m.fa -f r2.fa -o r2-se.cushaw.sam

real    8m8.601s
user    8m2.948s
sys     0m1.693s

$ time cushaw2-v2.1.8/cushaw2 -r ../../index/cushaw2/hs37m.fa -q r1.fa r2.fa -o r12-pe.cushaw.sam

real    17m11.156s
user    17m3.952s
sys     0m2.778s

$ time 0.5-r123_x86_64/seqalto_basic align ../../index/seqalto/hs37m.alto -1 r1.fa > r1-se.alto.sam

real    7m19.280s
user    7m3.337s
sys     0m2.546s

real    7m9.942s
user    7m1.116s
sys     0m2.343s

$ time 0.5-r123_x86_64/seqalto_basic align ../../index/seqalto/hs37m.alto -i 650 -m 500 -1 r1.fa -2 r2.fa > r12-pe.alto.sam

real    14m45.028s
user    14m36.166s
sys     0m2.790s

$ time bwa mem ../hs37m.fa long-250k.fq > long-250k.mem.sam

real    4m4.531s
user    3m59.209s
sys     0m2.484s

$ time bowtie2 -x ../../index/bowtie2/hs37m-bt2 long-250k.fq > long-250k.bt2.sam

real    24m21.418s
user    24m12.825s
sys     0m2.107s

$ time gem-mapper -I ../../index/gem/hs37m-gem.gem -i long-250k.fq -q offset-33 -e 0.1 -s 1 > long-250k.gem-e0.1-s1.sam

real    6m34.689s
user    6m30.755s
sys     0m2.095s

$ time cushaw2-v2.1.8/cushaw2 -r ../../index/cushaw2/hs37m.fa -f long-250k.fq -o long-250k.cushaw.sam

real    27m11.074s
user    27m4.910s
sys     0m1.976s

$ time subread-1.3.1/bin/subread-align -i ../../index/subread/hs37m -r r12.fq -o 1.sam

real    2m14.643s
user    1m36.612s
sys     0m4.344s


# new bwa-mem speed:

[main] Version: 0.7.3-r375-beta
[main] CMD: bwa mem ../hs37m.fa r1.fa r2.fa
[main] Real time: 526.254 sec; CPU: 525.923 sec

real    8m46.396s
user    8m42.913s
sys     0m3.012s

[main] Version: 0.7.3-r375-beta
[main] CMD: bwa mem ../hs37m.fa -
[main] Real time: 503.374 sec; CPU: 503.197 sec

real    8m23.444s
user    8m20.584s
sys     0m2.714s

$ time ./STAR --genomeDir ../../index/star --readFilesIn r12.fq --runThreadN 1 --outFilterMultimapNmax 1 --chimSegmentMin 30 --genomeLoad LoadAndKeep

real    2m13.388s
user    2m0.694s
sys     0m7.499s

$ time gsnap --force-single-end -Asam -d hs37m r12.fq > r12-se.gsnap.sam

real    90m54.298s
user    86m45.446s
sys     5m48.105s

$ time gsnap -Asam -d hs37m r1.fq r2.fq > r12-pe.gsnap.sam

real    58m34.316s
user    54m12.621s
sys     5m22.857s

$ time alfalfa align -r ../../index/hs37m.fa -i ../../index/alfalfa/hs37m -0 r12.fq -o r12-se.alfalfa.sam

real    8m0.170s
user    7m18.372s
sys     0m5.101s

$ time alfalfa align -r ../../index/hs37m.fa -i ../../index/alfalfa/hs37m -1 r1.fq -2 r2.fq -I 350 -X 650 -o r12-pe.alfalfa.sam

real    8m14.903s
user    7m37.345s
sys     0m4.321s



# RNA-seq mapping; first-end only

$ time tophat-2.0.8.Linux_x86_64/tophat2 ../../index/bowtie2/hs37m-bt2 r1.fq > r1-se.tophat.sam

real    31m21.333s
user    31m20.378s
sys     0m15.236s

$ time tophat-2.0.8.Linux_x86_64/tophat2 -o tophat_fusion_out --fusion-search --bowtie1 --no-coverage-search -r 0 --max-intron-length 100000 --fusion-min-dist 100000 --fusion-anchor-length 13 ../../index/bowtie/hs37m r1.fq > r1-se.fusion.sam

real    23m56.235s
user    23m56.459s
sys     0m22.785s





$ wgsim -h -R 0.3 -1 600 -N 500000 -r 0.01 -S 11 ../../index/hs37m.fa r0.fq /dev/null

$ bwa mem ~/apes/bwadb/hs37m.fa r0.fq > r0.sam

[main] Version: 0.7.5a-r405
[main] CMD: bwa mem /net/eichler/vol8/home/lh3lh3/apes/bwadb/hs37m.fa r0.fq
[main] Real time: 2825.200 sec; CPU: 1226.223 sec

$ time alfalfa align -r ../../index/hs37m.fa -i ../../index/alfalfa/hs37m -0 r0.fq -o r0.alfa.sam

real    14m3.427s
user    9m1.294s
sys     0m8.065s