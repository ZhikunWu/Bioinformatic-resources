#!/usr/bin/env R

args <- commandArgs(TRUE)

library(grid)
library(futile.logger)
library(VennDiagram)

# Rscript venn_4categories.R commonDown commonDown.svg svg 15 15 2.5

venn_plot <- function(data_file, out_name, out_type, out_height, out_width, text_cex){
    col_names <- colnames(data_file)
    A = levels(data_file[, col_names[1]])
    B = levels(data_file[, col_names[2]])
    C = levels(data_file[, col_names[3]])
    D = levels(data_file[, col_names[4]])
    venn.diagram(
        x = list(A = A, B = B, C = C, D = D),
        category.names = col_names,
        filename = out_name,
        imagetype = out_type, #"svg", "png"
        height = out_height, #15, 3000
        width = out_width, #15, 3000
        col = "transparent",
        fill = c("cornflowerblue", "seagreen3", "orange", "darkorchid1"),
        alpha = 0.50,
        label.col = c("white", "white", "white", "white", 
            "white", "white", "white", "white", "white", "white", 
            "white", "white", "white", "white", "white"),
        cex = text_cex, #2.5, 1
        fontfamily = "serif",
        fontface = "bold",
        cat.col = c("cornflowerblue", "darkgreen", "orange", "darkorchid1"),
        cat.pos = c(-120,120,-60,60),
        cat.dist = c(0.25,0.25,0.20,0.20),
        cat.fontfamily = "serif", 
        cat.cex = text_cex, #2.5, 1
        rotation.degree = 0,
        margin = 0.2 )

}

data_file <- read.table(args[1],header=TRUE,sep="\t",quote="")

#venn_plot(data_file, "noncoding.svg", "svg", 15, 15, 2.5)
#venn_plot(data_file, "noncoding.png", "png", 3000, 3000, 1)

venn_plot(data_file, args[2], args[3], as.numeric(args[4]), as.numeric(args[5]), as.numeric(args[6]))