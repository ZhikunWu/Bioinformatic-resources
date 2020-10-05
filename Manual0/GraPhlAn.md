## GraPhlAn Manual

## [GraPhlAn tutorial](https://bitbucket.org/nsegata/graphlan/wiki/Home#rst-header-download-and-installation)

guide.txt
```
$ head guide.txt 
Bacillaceae.Anoxybacillus.Aflavithermus
Bacillaceae.Bacillus.Bamyloliquefaciens
Bacillaceae.Bacillus.Banthracis
Bacillaceae.Bacillus.Batrophaeus
Bacillaceae.Bacillus.Bcellulosilyticus
Bacillaceae.Bacillus.Bcereus
Bacillaceae.Bacillus.Bclausii
Bacillaceae.Bacillus.Bcoagulans
Bacillaceae.Bacillus.Bcoahuilensis
Bacillaceae.Bacillus.Bhalodurans
```


### step0
annotation file:
```bash
$ head  annot_0.txt 
clade_separation    0.5
branch_thickness    1.5
branch_bracket_depth    0.8
branch_bracket_width    0.25
clade_marker_size   40
clade_marker_edge_color #555555
clade_marker_edge_width 1.2
```

* clade_separation specify a fractional separation between clades which is proportional to the branch distance between subtrees. It option can be used to visually separate more clades that are reciprocally deep branching. Default is 0.0
* branch_thickness set the global thickness of the lines connecting taxa. Default is 0.75
* branch_bracket_depth set the relative position of the branch bracket which is the radial segment from which the child taxa branches originate. Default is 0.25
* branch_bracket_width set the width of the branch bracket relative to the position of the most separated child roots. Default is 1.0
* clade_marker_size set the size of the marker representing the root of the clade inside the tree. Default is 20.0
* clade_marker_edge_color set the color of the markers' border. Default is #000000 (i.e. black)
* clade_marker_edge_width set the thickness of the border for clade markers. Default is 0.5

script
```
$ graphlan.py guide.txt step_0.png --dpi 300 --size 3.5
```

### step1
```
$ head annot_1.txt 
Banthracis  clade_marker_color  b
Banthracis  clade_marker_size   80
Saureus clade_marker_color  r
Saureus clade_marker_size   125
Bacillus    clade_marker_color  b
Bacillus    clade_marker_size   120
Bacillus    clade_marker_shape  h
Pcurdlanolyticus    clade_marker_color  #20DD20
Plarvae clade_marker_color  #008000
Pmucilaginosus  clade_marker_color  #057005 
```
[clade_name{+|*|^}]   graphical_tree_option   graphical_tree_option_value

If the clade name is omitted the option is applied to ALL clades. The clade can be specified with the full label comprising all names from the root of the tree or with the last level only (if last level names are not unique, multiple matching clades will be affected by the command). Optionally, at the end of the clade name, one of the following character can be added: +, *, ^. Where * means that the specified clade and all its descendants are affected by the property; + means that the specified clade and all its terminal nodes are affected; and ^ means that all (an only) the terminal nodes of the specified clade are affected.


The `graphical_tree_option` used in the `annot_1.txt` are:
* `clade_marker_size` is the size of the marker representing the root of the clade inside the tree. Default is 20.0
* `clade_marker_color` specify the fill color of the marker representing the root of the clade inside the tree. Default is #FFFFFF (i.e. white)
* `clade_marker_shape` provides the shape of the clade marker. See the "MARKER SHAPES" table in the readme.txt file for more information. Default is 'o' (i.e. circle)

### default plot
```
graphlan_annotate.py --annot annot_0.txt guide.txt guide_1.xml
graphlan.py guide_1.xml step_1.svg --dpi 300 --size 3.5
```

or 
```
graphlan_annotate.py gut_microbiome.txt gut_microbiome.annot.xml --annot annot.txt
graphlan.py gut_microbiome.annot.xml gut_microbiome.png --dpi 300 --size 4.5 --pad 0
```



### output files
```
$ head gut_microbiome.txt 
p__Actinobacteria.c__Actinobacteria asds
p__Firmicutes.c__Clostridia.o__Clostridiales.f__Clostridiales_Family_XI_Incertae_Sedis.g__Anaerococcus.s__Anaerococcus_unclassified
p__Bacteroidetes.c__Bacteroidia.o__Bacteroidales.f__Bacteroidaceae.g__Bacteroides.s__Bacteroides_salanitronis
p__Proteobacteria.c__Gammaproteobacteria.o__Enterobacteriales.f__Enterobacteriaceae.g__Escherichia.s__Escherichia_coli
p__Actinobacteria.c__Actinobacteria.o__Bifidobacteriales.f__Bifidobacteriaceae.g__Bifidobacterium
p__Firmicutes.c__Bacilli.o__Lactobacillales.f__Streptococcaceae.g__Streptococcus.s__Streptococcus_salivarius
p__Actinobacteria
p__Firmicutes.c__Bacilli.o__Lactobacillales.f__Lactobacillaceae.g__Lactobacillus.s__Lactobacillus_salivarius
p__Firmicutes.c__Erysipelotrichi.o__Erysipelotrichales.f__Erysipelotrichaceae.g__Turicibacter
p__Proteobacteria.c__Alphaproteobacteria
```


annot_2.txt:
```
Bacillus        annotation      Bacillus
Bacillaceae     annotation      Bacillaceae
Bacillus        annotation_background_color     b
Bacillaceae     annotation_background_color     b
Paenibacillaceae        annotation      Paenibacillaceae
Paenibacillaceae        annotation_background_color     g
Staphylococcus  annotation      Staphylococcus
Staphylococcus  annotation_background_color     r
Saureus annotation      S. aureus
Saureus annotation_background_color     r
Paenibacillus   annotation      Paenibacillus
Paenibacillus   annotation_background_color     g
Staphylococcaceae       annotation      Staphylococcaceae
Staphylococcaceae       annotation_background_color     r
Brevibacillus   annotation      Brevibacillus
Brevibacillus   annotation_background_color     g
Bbrevis annotation      a:Brevibacillus brevis
Bbrevis annotation_background_color     g
Blaterosporus   annotation      b:Brevibacillus laterosporus
Blaterosporus   annotation_background_color     g
Banthracis      annotation      Bacillus anthracis
Banthracis      annotation_background_color     b
Bsubtilis       annotation      Bacillus subtilis
Bsubtilis       annotation_background_color     b
```





### [export2graphlan - tutorial](https://bitbucket.org/nsegata/graphlan/wiki/export2graphlan%20-%20tutorial)
### export2graphlan
```
$ cd export2graphlan/
wzk@ubuntu 21:54:45 ^_^ /home/wzk/metaphlan_data/export2graphlan 
```

download the data
```
$ wget http://huttenhower.sph.harvard.edu/webfm_send/129 -O hmp_aerobiosis_small.txt
```

the file format
```
$ less -S hmp_aerobiosis_small.txt

oxygen_availability     High_O2 Mid_O2  Low_O2  Mid_O2  Low_O2  Low_O2  High_O2 Mid_O2  High_O2 Mid_O2  High_O2 High_O2 High_O2 Mid_O2  Mid_O2  High_O2 High_O2 High_O2 High_O2 
body_site       ear     oral    gut     oral    gut     gut     nasal   vagina  skin    oral    ear     ear     nasal   oral    oral    nasal   ear     skin    ear     skin    
subject_id      158721788       158721788       159146620       159005010       159166850       158742018       159005010       159005010       159005010       159146620       
Archaea|Euryarchaeota|Methanobacteria|Methanobacteriales|Methanobacteriaceae|Methanobrevibacter 2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     
Bacteria        0.999994        0.99999 0.99999 0.999984        0.999988        0.999995        0.999966        0.999988        0.999927        0.999981        0.999993        
Bacteria|Acidobacteria  5.0412e-05      8.65194e-05     8.39666e-05     0.000133753     0.000105843     4.42918e-05     0.000514972     9.93365e-05     0.000616591     0.000158
Bacteria|Acidobacteria|Acidobacteria_Gp10|Gp10  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp11|Gp11  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp16|Gp16  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp17|Gp17  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp1|Gp1    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp22|Gp22  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp3|Gp3    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      0.000241838     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp4|Gp4    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp5|Gp5    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp6|Gp6    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
```


```
$ less -S  hmp_aerobiosis_small.txt

oxygen_availability     High_O2 Mid_O2  Low_O2  Mid_O2  Low_O2  Low_O2  High_O2 Mid_O2  High_O2 Mid_O2  High_O2 High_O2 High_O2 Mid_O2  Mid_O2  High_O2 High_O2 High_O2 High_O2 
body_site       ear     oral    gut     oral    gut     gut     nasal   vagina  skin    oral    ear     ear     nasal   oral    oral    nasal   ear     skin    ear     skin    
subject_id      158721788       158721788       159146620       159005010       159166850       158742018       159005010       159005010       159005010       159146620       
Archaea|Euryarchaeota|Methanobacteria|Methanobacteriales|Methanobacteriaceae|Methanobrevibacter 2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     
Bacteria        0.999994        0.99999 0.99999 0.999984        0.999988        0.999995        0.999966        0.999988        0.999927        0.999981        0.999993        
Bacteria|Acidobacteria  5.0412e-05      8.65194e-05     8.39666e-05     0.000133753     0.000105843     4.42918e-05     0.000514972     9.93365e-05     0.000616591     0.000158
Bacteria|Acidobacteria|Acidobacteria_Gp10|Gp10  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp11|Gp11  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp16|Gp16  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp17|Gp17  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp1|Gp1    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp22|Gp22  2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp3|Gp3    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      0.000241838     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp4|Gp4    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp5|Gp5    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp6|Gp6    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp7|Gp7    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
Bacteria|Acidobacteria|Acidobacteria_Gp9|Gp9    2.96541e-06     5.08937e-06     4.93921e-06     7.86782e-06     6.22604e-06     2.6054e-06      1.70709e-05     5.84333e-06     
```

### convert the file in LEfSe format, and run LEfSe
```
$ /home/wzk/anaconda3/envs/qiime/bin/nsegata_lefse/format_input.py hmp_aerobiosis_small.txt hmp_aerobiosis_small.in -c 1 -s 2 -u 3 -o 1000000
$ run_lefse.py hmp_aerobiosis_small.in hmp_aerobiosis_small.res
```

#### error
```
rpy2.rinterface.RRuntimeError: Error in library(mvtnorm) : there is no package called ‘mvtnorm’
rpy2.rinterface.RRuntimeError: Error in library(modeltools) : there is no package called ‘modeltools’
rpy2.rinterface.RRuntimeError: Error in library(coin) : there is no package called ‘coin’

```

#### install the packages
```
conda install -c r r-mvtnorm
conda install -c r r-coin
conda install -c r r-modeltools
```

#### re-run
```
$ /home/wzk/anaconda3/envs/qiime/bin/nsegata_lefse/run_lefse.py   hmp_aerobiosis_small.in hmp_aerobiosis_small.res
Number of significantly discriminative features: 51 ( 131 ) before internal wilcoxon
Number of discriminative features with abs LDA score > 2.0 : 51

```

output file
```
$ head  hmp_aerobiosis_small.res
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales.Micromonosporaceae.Actinocatenispora 0.932620780672          -
Bacteria.Firmicutes.Bacilli.Bacillales.Planococcaceae.Paenisporosarcina 0.932620780672          -
Bacteria.Actinobacteria.Actinobacteria.Coriobacteriales.Coriobacteriaceae   4.1742722203            -
Bacteria.Firmicutes.Bacilli.Bacillales.Bacillaceae.Exiguobacterium  3.14961753202           -
Bacteria.Firmicutes.Clostridia.Clostridiales.Eubacteriaceae 3.01763255894           -
Bacteria.Firmicutes.Bacilli.Bacillales.Bacillaceae.Ureibacillus 0.932620780672          -
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales.Micromonosporaceae   1.93262078067           -
Bacteria.Proteobacteria.Alphaproteobacteria.Rhizobiales.Brucellaceae.Ochrobactrum   0.932620780672          -
Bacteria.Firmicutes.Bacilli.Lactobacillales.Lactobacillaceae.Paralactobacillus  0.932620780672          -
Bacteria.Proteobacteria.Gammaproteobacteria.Cardiobacteriales.Cardiobacteriaceae.Suttonella 0.932620780672          -

```

convert it
```
$ /home/wzk/anaconda3/envs/qiime/bin/graphlan/export2graphlan/export2graphlan.py -i hmp_aerobiosis_small.txt -o hmp_aerobiosis_small.res -t tree.txt -a annot.txt --title "HMP aerobiosis" --annotations 2,3 --external_annotations 4,5,6 --fname_row 0 --skip_rows 1,2 --ftop 200
```

output files
```
$ head  tree.txt
Bacteria
Bacteria.Acidobacteria
Bacteria.Actinobacteria
Bacteria.Actinobacteria.Actinobacteria
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales.Actinomycetaceae
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales.Actinomycetaceae.Actinomyces
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales.Corynebacteriaceae
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales.Corynebacteriaceae.Corynebacterium
Bacteria.Actinobacteria.Actinobacteria.Actinomycetales.Dietziaceae



$ less annot.txt

title   HMP aerobiosis
title_font_size 15

clade_separation        0.5
branch_bracket_depth    0.8
branch_bracket_width    0.2
annotation_legend_font_size     10
class_legend_font_size  10
class_legend_marker_size        1.5

MID O2  annotation      MID O2
MID O2  clade_marker_color      #2d19ff
MID O2  clade_marker_size       40

LOW O2  annotation      LOW O2
LOW O2  clade_marker_color      #29cc36
LOW O2  clade_marker_size       40

HIGH O2 annotation      HIGH O2
HIGH O2 clade_marker_color      #ff3333
HIGH O2 clade_marker_size       40

Bacteria        clade_marker_size       200.0
Acidobacteria   clade_marker_size       20.092173499
Actinobacteria  clade_marker_size       10.0
Actinobacteria  clade_marker_color      #ff3333
Actinobacteria  clade_marker_size       139.256500728
Actinobacteria  clade_marker_color      #f53131
Actinobacteria  annotation_background_color     #f53131
Actinobacteria  annotation      Actinobacteria
Actinobacteria  annotation_font_size    9

Actinomycetales clade_marker_size       138.073009561
Actinomycetales clade_marker_color      #f53131
Actinomycetales annotation_background_color     #f53131
Actinomycetales annotation      *:Actinomycetales
Actinomycetales annotation_font_size    9

```

### attach annotation to the tree
```
$ /home/wzk/anaconda3/envs/qiime/bin/graphlan/graphlan_annotate.py --annot annot.txt tree.txt outtree.txt
```

### generate the beautiful image
```

$ /home/wzk/anaconda3/envs/qiime/bin/graphlan/graphlan.py --dpi 300 --size 7.0 outtree.txt outimg.png --external_legends
```
output files
```
outimg_annot.png
outimg_legend.png
outimg.png
```



