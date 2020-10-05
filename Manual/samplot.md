
## [samplot](https://github.com/ryanlayer/samplot)

### install samplot

```
$ git clone https://github.com/ryanlayer/samplot.git
```

### samplot parameter
```
$ ./samplot.py --help
usage: samplot.py [-h] [--marker_size MARKER_SIZE] [-n TITLES [TITLES ...]]
                  [-r REFERENCE] [-z Z] -b BAMS [BAMS ...] -o OUTPUT_FILE -s
                  START -e END -c CHROM [-w WINDOW] [-d MAX_DEPTH]
                  [--minq MINQ] [-t SV_TYPE] [-T TRANSCRIPT_FILE]
                  [-A ANNOTATION_FILES [ANNOTATION_FILES ...]]
                  [--coverage_tracktype {stack,superimpose}] [-a]
                  [-H PLOT_HEIGHT] [-W PLOT_WIDTH] [-q MIN_MQUAL] [-j]
                  [--start_ci START_CI] [--end_ci END_CI]
                  [--long_read LONG_READ] [--min_event_size MIN_EVENT_SIZE]
                  [--xaxis_label_fontsize XAXIS_LABEL_FONTSIZE]
                  [--yaxis_label_fontsize YAXIS_LABEL_FONTSIZE]
                  [--legend_fontsize LEGEND_FONTSIZE]
                  [--annotation_fontsize ANNOTATION_FONTSIZE]
                  [--common_insert_size] [--hide_annotation_labels]
                  [--coverage_only] [--same_yaxis_scales]

SAMPLOT creates images of genome regions from CRAM/SAM alignments, optimized
for structural variant call review

optional arguments:
  -h, --help            show this help message and exit
  --marker_size MARKER_SIZE
                        Size of marks on pairs and splits (default 3)
  -n TITLES [TITLES ...], --titles TITLES [TITLES ...]
                        Space-delimited list of plot titles. Use quote marks
                        to include spaces (i.e. "plot 1" "plot 2")
  -r REFERENCE, --reference REFERENCE
                        Reference file for CRAM, required if CRAM files used
  -z Z, --z Z           Number of stdevs from the mean (default 4)
  -b BAMS [BAMS ...], --bams BAMS [BAMS ...]
                        Space-delimited list of BAM/CRAM file names
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name
  -s START, --start START
                        Start position of region/variant
  -e END, --end END     End position of region/variant
  -c CHROM, --chrom CHROM
                        Chromosome
  -w WINDOW, --window WINDOW
                        Window size (count of bases to include in view),
                        default(0.5 * len)
  -d MAX_DEPTH, --max_depth MAX_DEPTH
                        Max number of normal pairs to plot
  --minq MINQ           coverage from reads with MAPQ <= minq plotted in
                        lighter grey. To disable, pass in negative value
  -t SV_TYPE, --sv_type SV_TYPE
                        SV type. If omitted, plot is created without variant
                        bar
  -T TRANSCRIPT_FILE, --transcript_file TRANSCRIPT_FILE
                        GFF of transcripts
  -A ANNOTATION_FILES [ANNOTATION_FILES ...], --annotation_files ANNOTATION_FILES [ANNOTATION_FILES ...]
                        Space-delimited list of bed.gz tabixed files of
                        annotations (such as repeats, mappability, etc.)
  --coverage_tracktype {stack,superimpose}
                        type of track to use for low MAPQ coverage plot.
  -a, --print_args      Print commandline arguments
  -H PLOT_HEIGHT, --plot_height PLOT_HEIGHT
                        Plot height
  -W PLOT_WIDTH, --plot_width PLOT_WIDTH
                        Plot width
  -q MIN_MQUAL, --min_mqual MIN_MQUAL
                        Min mapping quality of reads to be included in plot
  -j, --json_only       Create only the json file, not the image plot
  --start_ci START_CI   confidence intervals of SV first breakpoint (distance
                        from the breakpoint). Must be a comma-separated pair
                        of ints (i.e. 20,40)
  --end_ci END_CI       confidence intervals of SV end breakpoint (distance
                        from the breakpoint). Must be a comma-separated pair
                        of ints (i.e. 20,40)
  --long_read LONG_READ
                        Min length of a read to be treated as a long-read
                        (default 1000)
  --min_event_size MIN_EVENT_SIZE
                        Min size of an event in long-read CIGAR to include
                        (default 100)
  --xaxis_label_fontsize XAXIS_LABEL_FONTSIZE
                        Font size for X-axis labels (default 6)
  --yaxis_label_fontsize YAXIS_LABEL_FONTSIZE
                        Font size for Y-axis labels (default 6)
  --legend_fontsize LEGEND_FONTSIZE
                        Font size for legend labels (default 6)
  --annotation_fontsize ANNOTATION_FONTSIZE
                        Font size for annotation labels (default 6)
  --common_insert_size  Set common insert size for all plots
  --hide_annotation_labels
                        Hide the label (fourth column text) from annotation
                        files, useful for region with many annotations
  --coverage_only       Hide all reads and show only coverage
  --same_yaxis_scales   Set the scales of the Y axes to the max of all

```

Error
```
$ /home/wuzhikun/anaconda3/envs/plots/bin/samplot/src/samplot.py -n M625-0 -b M625-0.bam -o 14_18901837_18902124.png -c 14 -s  18901837  -e 18902124 -t DEL
Traceback (most recent call last):
  File "/home/wuzhikun/anaconda3/envs/plots/bin/samplot/src/samplot.py", line 2186, in <module>
    max_coverage)   
  File "/home/wuzhikun/anaconda3/envs/plots/bin/samplot/src/samplot.py", line 1727, in plot_samples
    curr_max_insert_size)
  File "/home/wuzhikun/anaconda3/envs/plots/bin/samplot/src/samplot.py", line 1052, in plot_long_reads
    if max_gap*1.1 > curr_max_insert_size:
```


