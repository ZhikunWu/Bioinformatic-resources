#!/usr/bin/env R
library(stringr)
library(ggplot2)

args <- commandArgs(TRUE)
if (length(args) < 2) {
  stop("Usage: Rscript GO_3Catrgory_plot.r <infile> <outfile> <top_num>")
}

select_top <- function(BP,top_number){
	if(nrow(BP) <= top_number){
		return(BP)
	}else{
		BP <- BP[1:top_number,]
		return(BP)
	}
}

GO_plot <- function(in_file,top_number){
	top_number <- as.integer(top_number)
	GO <- read.table(in_file,header=T,sep="\t",quote="")
	order_GO <- GO[with(GO,order(Category,-Count)),]
	BP <- subset(order_GO,Category=="GOTERM_BP_FAT")
	CC <- subset(order_GO,Category=="GOTERM_CC_FAT")
	MF <- subset(order_GO,Category=="GOTERM_MF_FAT")
	GO_top <- rbind(select_top(BP,top_number),select_top(CC,top_number),select_top(MF,top_number))
	GO_top_split <- str_split_fixed(GO_top$Term,'~',2)
	colnames(GO_top_split) <- c("Term_num","Term_name")
	new_GO_top <- cbind(GO_top,GO_top_split)
	new_GO_top <- new_GO_top[with(new_GO_top,order(Category,-Count)),]
	order_num <- as.data.frame(rep(1:(top_number*3)))
	colnames(order_num) <- "order"
	new_GO_top <-  cbind(order_num,new_GO_top)
	levels(new_GO_top$Category)
	p <- ggplot(new_GO_top, aes(x = order,y=Count,fill=Category)) + 
		#scale_fill_manual(values=c(GOTERM_BP_FAT = "red", GOTERM_CC_FAT = "blue", GOTERM_MF_FAT = "green")) +
		#theme(axis.text.x = element_text(colour = new_GO_top$Category)) + 
		#scale_colour_manual(values=c("red","blue","green")) +
		geom_bar(stat="identity")+ scale_x_discrete(limits = new_GO_top$Term_name) + 
		theme(axis.text.x = element_text(angle=90,hjust=1,vjust=0.3)) + xlab("") + 
		scale_fill_discrete(labels=c("Biological process", "Cellular component", "Molecular function"))
	p
	
} 



pdf(paste(args[2],"pdf",sep="."),12,9)
GO_plot(args[1],20)
dev.off()

# tiff(paste(args[2],"tif",sep="."),3000, 2400, res = 300, compression = "lzw")
# GO_plot(args[1],20)
# dev.off()


