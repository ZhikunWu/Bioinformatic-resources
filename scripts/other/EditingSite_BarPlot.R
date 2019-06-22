#!/usr/bin/env Rscript

args <- commandArgs(TRUE)

if (length(args) < 4 ){
	stop("Usage: Rscript EditingSite_BarPlot.R <editing_summary_file> <editing_count_file> <editing_feature.pdf> <editing_type.pdf>", call.=FALSE)
}

library("ggplot2")

feature_bar_plot <- function(file){
	file_data <- read.table(file,header=T,quote="")
	melt_dt <- reshape2::melt(file_data)
	Feature_order <- factor(melt_dt$Feature, order=TRUE, levels=c("5'UTR", "Exon", "Intron", "3'UTR", "Intergenic"))
	p <- ggplot(melt_dt,aes(x=Feature_order,y=value,fill=Feature_order)) +
		geom_bar(stat="identity",width=0.7,position=position_dodge(0.3))+
		xlab("") + ylab("Editing sites for gene feature") +
		geom_text(aes(label=value),vjust=-0.2) + facet_grid(variable~., scales = "free_y")
	p
}

bar_plot <- function(file){
	file_data  <- read.table(file,header=T,quote="")
	colnames(file_data) <- c("Type", "Alu", "nonAlu")
	melt_dt <- reshape2::melt(file_data)
	p <- ggplot(melt_dt,aes(x=Type,y=value,fill=Type)) +
		geom_bar(stat="identity",width=0.7,position=position_dodge(0.3))+
		xlab("") + ylab("Counts for editing type ") +
		geom_text(aes(label=value),vjust=-0.2, size=2.5) + facet_grid(variable~., scales = "free_y")
	p
}


summary_file <- args[1]
count_file <- args[2]

pdf(args[3])
feature_bar_plot(summary_file)
dev.off()

pdf(args[4])
bar_plot(count_file)
dev.off()
