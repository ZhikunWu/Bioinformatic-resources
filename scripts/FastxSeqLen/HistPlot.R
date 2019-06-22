#!/usr/bin/env Rscript
library(ggplot2)
library(argparser)

#usage:  Rscript ~/github/zkwu/kcMeta/script/HistPlot.R --input representive_gene_length_hist.xls --pdf representive_gene_length_hist.pdf --width 6 --height 4

arg <- arg_parser('Box plot for mutiple sample.')
arg <- add_argument(arg, '--input', help='The input file.')
arg <- add_argument(arg, '--pdf', help='output file with pdf format.')
arg <- add_argument(arg, '--width', help='The width of picture.')
arg <- add_argument(arg, '--height', help='The height of picture.')
argv <- parse_args(arg)


HistPlot <- function(in_file, pdf_file, height, width){
    height <- as.numeric(height)
    width <- as.numeric(width)
    data <- read.table(in_file, header=TRUE, sep="\t")
    # pdf(pdf_file, height=height, width=width)
    hist <- ggplot(data, aes(x=Length, y=Count)) + geom_bar(stat="identity", fill="cadetblue") + 
        theme_bw() + 
        theme(plot.title = element_blank()) + 
        theme(axis.line = element_line(colour = "black"), panel.background = element_blank(),panel.border=element_blank(),panel.grid.major = element_blank(),panel.grid.minor = element_blank()) +
        theme(plot.margin = margin(1,1,1,1, "cm"))
    hist
    ggsave(pdf_file, height=height, width=width)
    # dev.off()

}


HistPlot(argv$input, argv$pdf, argv$height, argv$width)

