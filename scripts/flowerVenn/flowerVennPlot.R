#!/usr/bin/env Rscript
library(ggplot2)
library(argparser)
library(readr)
library(plotrix)

#usage: Rscript flowerVennPlot.R --input C186_group_special_OTUs.xls --svg C186_group_special_OTUs.svg --width 10 --height 10


arg <- arg_parser('Arguments for ploting alpha diversity.')
arg <- add_argument(arg, '--input', help="The input file.")
arg <- add_argument(arg, '--svg', help="The output svg file.")
arg <- add_argument(arg, '--width', help='The width of picture.')
arg <- add_argument(arg, '--height', help='The height of picture.')
argv <- parse_args(arg)


### input file:
# Sample  Core_OTU    Special_OTU All_OTU
# g1  9   41  856
# g2  9   3   1023
# g3  9   3   939


flower_plot2 <- function(sample, value, All, start, a, b,  
                    ellipse_col = rgb(135, 206, 235, 150, max = 255), 
                    circle_col = rgb(0, 162, 214, max = 255),
                    circle_text_cex = 1, labels=labels) {
par( bty = "n", ann = F, xaxt = "n", yaxt = "n", mar = c(1,1,1,1))
plot(c(0,10),c(0,10),type="n")
n   <- length(sample)
deg <- 360 / n
res <- lapply(1:n, function(t){
    ellipse_col <- ellipse_col[t]
    plotrix::draw.ellipse(x = 5 + cos((start + deg * (t - 1)) * pi / 180), 
                          y = 5 + sin((start + deg * (t - 1)) * pi / 180), 
                          col = ellipse_col,
                          border = ellipse_col,
                          a = a, b = b, angle = deg * (t - 1))
    text(x = 5 + 2.5 * cos((start + deg * (t - 1)) * pi / 180),
         y = 5 + 2.5 * sin((start + deg * (t - 1)) * pi / 180),
         value[t]
    )

    text(x = 5 + 3.1 * cos((start + deg * (t - 1)) * pi / 180),
         y = 5 + 3.1 * sin((start + deg * (t - 1)) * pi / 180),
         All[t]
    )


    # ### sample all value
    # if (deg * (t - 1) < 180 && deg * (t - 1) > 0 ) {
    #     text(x = 5 + 3.1 * cos((start + deg * (t - 1)) * pi / 180),
    #          y = 5 + 3.1 * sin((start + deg * (t - 1)) * pi / 180),
    #          All[t],
    #          srt = deg * (t - 1) - start,
    #          adj = 1,
    #          cex = circle_text_cex
    #     )

    # } else {
    #     text(x = 5 + 3.1 * cos((start + deg * (t - 1)) * pi / 180),
    #          y = 5 + 3.1 * sin((start + deg * (t - 1)) * pi / 180),
    #          All[t],
    #          srt = deg * (t - 1) + start,
    #          adj = 0,
    #          cex = circle_text_cex
    #     )
    # }



    ### sample name
    if (deg * (t - 1) < 180 && deg * (t - 1) > 0 ) {
        text(x = 5 + 3.6 * cos((start + deg * (t - 1)) * pi / 180),
             y = 5 + 3.6 * sin((start + deg * (t - 1)) * pi / 180),
             sample[t],
             srt = deg * (t - 1) - start,
             adj = 1,
             cex = circle_text_cex
        )

    } else {
        text(x = 5 + 3.6 * cos((start + deg * (t - 1)) * pi / 180),
             y = 5 + 3.6 * sin((start + deg * (t - 1)) * pi / 180),
             sample[t],
             srt = deg * (t - 1) + start,
             adj = 0,
             cex = circle_text_cex
        )
    }


})
plotrix::draw.circle(x = 5, y = 5, r = 1.5, col = circle_col, border = circle_col )

# tune location by x and y.
text(x = 4.9, y = 5, labels=labels)
}


data <- read_tsv(argv$input)
samples <- data$Sample
specialOTU <- data$Special_OTU
coreOTU <- data$Core_OTU
sampleOTU <- data$All_OTU


width <- as.numeric(argv$width)
height <- as.numeric(argv$height)

svg(argv$svg, width=width, height=height)

flower_plot2(samples,
        specialOTU, sampleOTU, 90, 0.5, 2, labels=coreOTU,
        ellipse_col = topo.colors(13, alpha = 0.3), 
        circle_col = topo.colors(1, alpha = 0.7) )

dev.off()

