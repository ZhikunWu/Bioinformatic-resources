#!/usr/bin/env Rscript

library('ggplot2')
library('argparser')

#usage: Rscript ../ClassStackBar.R --input /home/wzk/16S_package_test/Krona/PE250/Species_number.xls --pdf /home/wzk/16S_package_test/Krona/PE250/Species_number.pdf

arg <- arg_parser('Bar plot for variant of samples.')
arg <- add_argument(arg, '--input', help='The input file containing SNP number for each chr.')
arg <- add_argument(arg, '--pdf', help='The output pdf file.')
argv <- parse_args(arg)



SNP_Barplot <- function(in_file, pdf_file){
    # in_file <- '/home/wzk/temp/wheat_SNP.txt'
    # pdf_file <- '/home/wzk/temp/wheat_SNP.pdf'
    data <- read.table(in_file,header=T, quote="")
    out_pdf <- pdf_file
    melt_dt <- reshape2::melt(data)
    colnames(melt_dt) <- c('Chr', 'Pair', 'Value')
    p <- ggplot(melt_dt, aes(x=Chr, y=Value, fill=Pair))+
        geom_bar(stat="identity", width=0.7, position=position_dodge()) + 
        scale_fill_brewer(palette="Paired") + 
        labs(x="Chromosome", y="Percentage of variant count (%)") + 
        theme_bw() + 
        theme(axis.text.x = element_text(angle = 45, hjust = 1)) + 
        theme(panel.grid.minor.x=element_blank(), panel.grid.major.x=element_blank())
    ggsave(out_pdf, p, width=8, height=5)

}

SNP_Barplot(argv$input, argv$pdf)
