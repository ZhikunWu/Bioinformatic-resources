#!/usr/bin/env R
library(grid)
library(futile.logger)
library(VennDiagram)
library(argparser)

#usage: Rscript vennPlot.R --input commonDown --out commonDown.svg --type svg --height 15 --width 15 --cex 2.5

arg <- arg_parser('Arguments for ploting alpha diversity.')
arg <- add_argument(arg, '--input', help='The input file.')
arg <- add_argument(arg, '--out', help='The output file.')
arg <- add_argument(arg, '--type', help='The output type: svg or png.')
arg <- add_argument(arg, '--height', help='The height of the picture.')
arg <- add_argument(arg, '--width', help='The width of the picture.')
arg <- add_argument(arg, '--cex', help='The text cex for the label')
argv <- parse_args(arg)


venn_category_two <- function(data_file, out_name, out_type, out_height, out_width, text_cex){
    out_height <- as.numeric(out_height)
    out_width <- as.numeric(out_width)
    text_cex <- as.numeric(text_cex)

    col_names <- colnames(data_file)
    A = levels(data_file[, col_names[1]])
    B = levels(data_file[, col_names[2]])

    venn.diagram(
        x = list(A = A, B = B),
        category.names = col_names,
        filename = out_name,
        imagetype = out_type, #"svg", "png"
        height = out_height, #15, 3000
        width = out_width, #15, 3000
        col = "transparent",
        fill = c("cornflowerblue", "seagreen3"),
        alpha = 0.50,
        label.col = c("white", "white", "white"),
        cex = text_cex, #2.5, 1
        fontfamily = "serif",
        fontface = "bold",
        cat.col = c("cornflowerblue", "darkgreen"),
        cat.pos = c(-60,60),
        cat.dist = c(0.1,0.1),
        cat.fontfamily = "serif", 
        cat.cex = text_cex, #2.5, 1
        rotation.degree = 0,
        margin = 0.2,
        force.unique = TRUE)

}

venn_category_three <- function(data_file, out_name, out_type, out_height, out_width, text_cex){
    out_height <- as.numeric(out_height)
    out_width <- as.numeric(out_width)
    text_cex <- as.numeric(text_cex)

    col_names <- colnames(data_file)
    A = levels(data_file[, col_names[1]])
    B = levels(data_file[, col_names[2]])
    C = levels(data_file[, col_names[3]])

    venn.diagram(
        x = list(A = A, B = B, C = C),
        category.names = col_names,
        filename = out_name,
        imagetype = out_type, #"svg", "png"
        height = out_height, #15, 3000
        width = out_width, #15, 3000
        col = "transparent",
        fill = c("cornflowerblue", "seagreen3", "orange"),
        alpha = 0.50,
        label.col = c("white", "white", "white", "white", 
            "white", "white", "white"),
        cex = text_cex, #2.5, 1
        fontfamily = "serif",
        fontface = "bold",
        cat.col = c("cornflowerblue", "darkgreen", "orange"),
        cat.pos = c(-60,60,180),
        cat.dist = c(0.1,0.1,0.1),
        cat.fontfamily = "serif", 
        cat.cex = text_cex, #2.5, 1
        rotation.degree = 0,
        margin = 0.2,
        force.unique = TRUE)

}

venn_category_four <- function(data_file, out_name, out_type, out_height, out_width, text_cex){
    out_height <- as.numeric(out_height)
    out_width <- as.numeric(out_width)
    text_cex <- as.numeric(text_cex)

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



data_file <- read.table(argv$input,header=TRUE,sep="\t",quote="")
colNum <- length(colnames(data_file))

if (colNum == 2) {
    venn_category_two(data_file, argv$out, argv$type, argv$height, argv$width, argv$cex)
} else if (colNum == 3){
    venn_category_three(data_file, argv$out, argv$type, argv$height, argv$width, argv$cex)
} else if (colNum == 4){
    venn_category_four(data_file, argv$out, argv$type, argv$height, argv$width, argv$cex)
}



