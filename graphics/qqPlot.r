args<-commandArgs(TRUE)
x <- read.table(args[1],header=TRUE)

qqPlot <- function(x) {
attach(x)
o <- -log10(sort(p,decreasing=F))
e <- -log10(1:length(o)/length(o))
png(paste('qqPlot',args[1],'png',sep='.'),width=420,height=500)
plot(e,o,xlim=c(0,max(e)),ylim=c(0,max(o)+1),xlab='',ylab='',cex.axis=1.5,col="darkblue",pch=20,frame=F,cex=0.4,xaxs="i",yaxs="i",main="",cex.main=2.0,font.main=1,family="Times New Roman")
#main=levels(trait)
#ylim=c(0,max(o))
mtext(expression(paste('Expected',' ',-log[10](italic(P)),sep=' ')),1,2.5,cex=2.0,family="Times New Roman")
mtext(expression(paste('Observed',' ',-log[10](italic(P)),sep=' ')),2,2.5,cex=2.0,family="Times New Roman")
abline(a=0,b=1,lty=1,col="red")
abline(h=-log10(1/length(o)),lty=2,col='grey50')
dev.off()
}
