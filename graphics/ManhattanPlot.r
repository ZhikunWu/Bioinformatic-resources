#!/usr/bin/R
############################################
######Manhattan Plot for GWAS################


args<-commandArgs(TRUE)
x <- read.table(args[1],header=TRUE)
#Check the data structure

#Sort the data by the snp position and chromosomes
x<-x[order(x$pos),]
x<-x[order(x$chr),]
attach(x)

#Get the maximun postion of each chromosome
maxpos<-c(0,cumsum(as.numeric(aggregate(pos,list(chr),max)$x+sum(as.numeric(aggregate(pos,list(chr),max)$x))/200)))
#Set the point color for each chromosome
plot_col<-rep(c('red','black'),ceiling(max(unique(chr))/2))
#Get the point number of each chromosome
size<-aggregate(pos,list(chr),length)$x
a<-rep(maxpos[1],size[1])
b<-rep(plot_col[1],size[1])

for(i in 2:max(unique(chr))){
a<-c(a,rep(maxpos[i],size[i]))
b<-c(b,rep(plot_col[i],size[i]))}


xpos<-pos+a
col<-b
#col[p<(1/length(pos))]<-'red'
cex<-rep(1,length(pos))
 cex[p<(1/length(pos))]<- 1.5
if(max(-log10(p),na.rm=T)<8) {
	ylim<-c(0,8)
} else {
	if(ceiling(max(-log10(p),na.rm=T))%%2==0) {
		ylim=c(0,ceiling(max(-log10(p),na.rm=T)))
	} else {
		ylim=c(0,ceiling(max(-log10(p),na.rm=T))+1)
	}
}
d<-(aggregate(xpos,list(chr),min)$x+aggregate(xpos,list(chr),max)$x)/2


png(paste(args[1],'png',sep='.'),width=1000,height=500)
plot(xpos,-log10(p),col=col,ylim=ylim,pch=20,ylab='',cex=cex,cex.axis=1.5,family="Times New Roman",xaxs='i',yaxs='i',xaxt='n',las=1,xlab='',main=args[1],cex.main=2.0,font.main=1)
#plot(xpos,-log10(p),col=col,ylim=ylim,pch=20,ylab='',cex=cex,cex.axis=1.5,family="Times New Roman",xaxs='i',yaxs='i',xaxt='n',las=1,xlab='',main=levels(trait),cex.main=2.0)
#cex=cex,cex.axis=1.3,family="Times New Roman",
axis(1,tick=T,at=d,cex.axis=1.5,labels=c(1:12),family="Times New Roman")
#axis(1,tick=T,at=d,cex.axis=1.5,labels=c(paste('A',1:10,sep=''),paste('C',1:9,sep='')),family="Times New Roman")
mtext('Chromosome',1,3,cex=2.0,family="Times New Roman")
# axis(2,las=1)
mtext(expression(-log[10](italic(p))),2,2.3,cex=2.0,family="Times New Roman")
abline(h=-log10(1/length(pos)),lty=2,col='grey50')
# abline(v=qpos,lty=2,lwd=2)
dev.off()


