### circos config files

```
$ cat bands.conf 
show_bands            = yes
fill_bands            = yes
band_stroke_thickness = 2
band_stroke_color     = white
band_transparency     = 0
```

```
$ cat ideogram.label.conf
show_label       = yes
label_font       = default
label_radius     = dims(ideogram,radius) + 0.075r
label_with_tag   = yes
label_size       = 36
label_parallel   = yes
label_case       = lower
label_format     = eval(sprintf("chr%s",var(label)))
```

```
$ cat ideogram.position.conf
radius           = 0.90r
thickness        = 100p
fill             = yes
fill_color       = black
stroke_thickness = 2
stroke_color     = black
```


```
$ cat ticks.conf

show_ticks          = yes
show_tick_labels    = yes

<ticks>

radius           = dims(ideogram,radius_outer)
orientation      = out
label_multiplier = 1e-6
color            = black
size             = 20p
thickness        = 3p
label_offset     = 5p

<tick>
spacing        = 1u
show_label     = no
</tick>

<tick>
spacing        = 5u
show_label     = yes
label_size     = 20p
format         = %d
</tick>

<tick>
spacing        = 10u
show_label     = yes
label_size     = 24p
format         = %d
</tick>

</ticks>

```

```
$ cat circos.conf

<<include colors_fonts_patterns.conf>>

<<include ideogram.conf>>
<<include ticks.conf>>

<image>
<<include etc/image.conf>>
</image>

karyotype   = data/karyotype/karyotype.human.txt

chromosomes_units = 1000000
chromosomes_display_default = no
chromosomes       = hs1;hs2;hs3;hs4

<links>

z      = 0
radius = 0.975r
crest  = 1
color  = vlgrey
bezier_radius        = 0r
bezier_radius_purity = 0.5
thickness  = 2

<link>

file       = data/5/segdup.txt

<rules>

<rule>
# multiple conditions are combined with AND 
# i.e. all conditions must be satisfied
condition  = var(interchr) 
condition  = within(hs2,40Mb,80Mb)
z          = 60
color      = red
thickness  = 5
</rule>

<rule>
condition  = max(var(size1),var(size2)) > 40kb
z          = 50
color      = green
thickness  = 5
</rule>

<rule>
condition  = max(var(size1),var(size2)) > 10kb
z          = 45
color      = dgrey
thickness  = 4
</rule>

<rule>
condition  = max(var(size1),var(size2)) > 5kb
z          = 40
color      = grey
thickness  = 3
</rule>

<rule>
condition  = max(var(size1),var(size2)) > 1000
z          = 35
color      = lgrey
thickness  = 2
</rule>

</rules>

</link>

</links>

<<include etc/housekeeping.conf>>
data_out_of_range* = trim
```



### data file

```
$ head  segdup.txt 
hs1 465 30596 hs2 114046768 114076456
hs1 486 76975 hs15 100263879 100338121
hs1 486 30596 hs9 844 30515
hs1 486 9707 hsY 57762276 57771573
hs1 486 9707 hsX 154903076 154912373
hs1 486 9707 hs16 427 9533
hs1 8256 76975 hs19 11001 79672
hs1 23908 30596 hs12 17641 24322
hs1 59871 76975 hs6 5001 22075
hs1 71096 76975 hs6 170824311 170830148

```
