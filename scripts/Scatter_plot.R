library(ggplot2)
data<-read.table("Gene_expr_with_pval.xls",header = T,sep="\t")
data2<-data[,-3:-2]
a<-function(x){
  if(as.numeric(x[2])>1 && as.numeric(x[4])<0.05){
    x[7]<-"up"
    }else if(as.numeric(x[2])< -1 && as.numeric(x[4])<0.05){
        x[7]<-"down"
      }else{
        x[7]<-"nodiff"
      }
      
}    
category<-apply(data2,1,a)
c<-as.data.frame(category)
data2[,6]<-c


######################volcano plot##############
ggplot(data2,aes(x=data2[,2],y=-log10(data2[,4]),color=data2$category))+
  geom_point(shape=16)+
  xlab("logFC")+
  ylab("-log10(Pvalue)")+
  ggtitle("Volcano plot")+
  theme_bw()+
  theme(panel.grid =element_blank())+
  theme(plot.title = element_text(hjust = 0.5))+
  scale_color_manual(values = c("green","black","red"))+
  geom_hline(yintercept = 2, linetype="dashed")+
  geom_vline(xintercept = 1, linetype="dashed")+
  geom_vline(xintercept = -1, linetype="dashed")+
  guides(colour=FALSE)
ggsave("Volcano_plot.png",width = 8,height=8) 

############################scatter plot####################
#data3<-read.table("Rpkm.xls",header = T,sep="\t")
data3<-read.table('../../5.Expression/All_samples_Abundance.xls',header = T,sep="\t",row.names=1)
data3$Geneid<-row.names(data3)
#data3_2<-data3[,-3:-2]
data4<-data2[,c(1,6)]
data5<-merge(data4,data3,by="Geneid")
r <- round(cor(data3$Tre, data3$Con,method = "spearman"), digits=4)
txt <- paste0("pearson correlation : ", r)

ggplot(data5,aes(x=log2(data5[,3]),y=log2(data5[,4]),colour=data5$category))+
  geom_point(shape=16)+
  scale_color_manual(values = c("green","black","red"),labels=c("down-regulated genes(334)","no differential expressed(34669)","up-regulated genes(1469)"))+
  scale_y_continuous(limits=c(-5,15))+
  theme_bw()+
  theme(panel.grid =element_blank())+
  ggtitle("Scatter plot")+
  theme(plot.title = element_text(hjust = 0.5))+  
  guides(colour=guide_legend(title = NULL))+
  theme(legend.position = c(0.25,0.85))+
  theme(legend.text = element_text(size=13))+
  xlab("log2(Tre_Abundance)")+
  ylab("log2(Con_Abundance)")+
  theme(legend.background = element_blank(),legend.key = element_blank())+
  annotate("text",x=3,y=14.6,label=txt,size=4.5)
 ggsave("Scatter_plot.png",width = 8,height=8) 


 