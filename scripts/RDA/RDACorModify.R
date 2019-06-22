#!/usr/bin/env Rscript
library(vegan)
library(psych)
library(pheatmap)
library(argparser)
# library(ggvegan)
library(ggrepel)
library(ggplot2)

arg <- arg_parser('Calculate correlation and RDA statistics.')
arg <- add_argument(arg, '--species', help='The input species file.')
arg <- add_argument(arg, '--factor', help='The input factors file.')
arg <- add_argument(arg, '--outdir', help='The out directory.')
arg <- add_argument(arg, '--correlation', help='The output correlation file.')
arg <- add_argument(arg, '--pvalue', help='The output pvalue file.')
arg <- add_argument(arg, '--heatmap', help='The output heatmap pdf file.')
arg <- add_argument(arg, '--width', help='The width of the picture.')
arg <- add_argument(arg, '--height', help='The height of the picture')
argv <- parse_args(arg)


#usage: Rscript ~/github/zkwu/kcMeta/pipeline/RDACorModify.R --species taxonomy_significant_abundance_test.xls  --factor sample_factors_test.txt --correlation species_factor_correlation.xls --pvalue species_factor_pvalue.xls --heatmap  species_factor_correlation.pdf --width 10 --height 50 --outdir  test


DEG_heatmap2 <- function(DEG_any){
pheatmap(DEG_any, 
    clustering_method = "ward.D",
    cluster_rows=TRUE,
    show_rownames=TRUE,
    cluster_cols = TRUE,
    scale = "row",
    cellwidth = 20,
    color=colorRampPalette(rev(c("red","black","green")))(500))
}

heatmap2 <- function(data_matrix){
    heatmap.2(data_matrix,  
        density.info="none", 
        trace="none",  
        key=TRUE, 
        keysize=0.75, 
        key.title =NA, 
        lhei = c(1,90), #the relative height of key color to heatmap
        lwid=c(2,3.5), 
        key.xlab="Correlation", 
        cexRow = 0.75, 
        cexCol = 0.75, 
        margins =c(15,20),  
        notecex=1.0, 
        col=coul, 
        key.par = list(cex=0.5), ) 
}




species_factor_cor_RDA <- function(species_file, env_file, outdir, cor_file, pvalue_file,  heatmap_pdf, width, height){
        

    # species_file <- "/home/wzk/Project/C128/NCycTaxonomy/RDA/Samples_taxonomy_species.txt"
    # OTU J1-08   J2-08   J3-08   J4-08   J5-08   J6-08   J7-08   J8-08   J9-08
    # s__Rubritalea_squalenifaciens   0.0046847229961 0.00335664271473    0.00350236715858    0.00349054281398    0.00468657175951    0.00248410569345    0.00057952079   0.0 0.000448009208163
    # s__Arenimonas_SCN   0.000764279516878   0.00270382081667    0.00117564242939    0.00122616036121    0.00202423436981    0.0103055263961 0.00193668095552    0.002117764119560.00248307806301
    # s__Polaromonas_JS666    0.0163006875682 0.0182628198317 0.0206939944695 0.028092665865  0.0198616267703 0.0172278157835 0.0314195020547 0.0237187501073 0.0374468237179
    # s__Herpetosiphon_geysericola    0.00215683523235    0.00197650967296    0.003788284138850.00262201255813    0.00214381165841    0.0015773113272 0.00121407452042    0.001272634774210.000883910059349

    # env_file <- "/home/wzk/Project/C128/NCycTaxonomy/RDA/sample_factors.txt"
    # Sample  Tem DO  pH  w-NO3-
    # J1-08   28.13333333 7.543333333 8.393333333 1.200296693
    # J2-08   28.96666667 8.74    8.62    1.022466933
    # J3-08   29.06666667 8.326666667 8.366666667 0.604421653
    # J4-08   27.33333333 8.116666667 8.346666667 0.905280053
    # J5-08   28.53333333 11.17333333 8.606666667 0.888472373
    # J6-08   19.83333333 7.656666667 8   1.303061813
    # J7-08   16.4    8.703333333 8.1 1.218556533
    # J8-08   15.43333333 8.65    7.85    1.0707112
    # J9-08   16.3    8.463333333 8.206666667 1.15521648

    width <- as.numeric(width)
    height <- as.numeric(height)
    #species and sample file
    species <- read.csv(species_file, header=T, row.names=1, sep="\t", check.names = FALSE)
    species <- t(species)
    
    #sample and factors
    envs <- read.csv(env_file, header=T, row.names=1, sep="\t", check.names = FALSE)


    ################################ Calculate correlation ####################################
    # conbine data
    env_species <- cbind(species, envs)
    # calculate correlation
    env_species_cor <- corr.test(env_species, use="complete")
    # get correlation and p value
    cor_r <- env_species_cor$r
    cor_p <- env_species_cor$p

    species_names <- colnames(species)
    envs_names <- colnames(envs)

    # ############## get correlation using  psych
    # # get target correlation 
    # sub_cor_r <- cor_r[species_names,]
    # sub_cor_r2 <- sub_cor_r[, envs_names]

    # # get target p value
    # sub_cor_p <- cor_p[species_names,]
    # sub_cor_p2 <- sub_cor_p[, envs_names]
    # #############################################


    envs_number  <- ncol(envs)
    species_number <- ncol(species)

    env_names <- colnames(envs)
    species_names <- colnames(species)

    Corrs <- c()
    Pvalues <- c()

    for (i in 1:envs_number){
      for (j in 1:species_number){
        e <- envs[, i]
        s <- species[, j]
        correlation <- cor.test(e, s, method="spearman")
        corr <- correlation$estimate[[1]]
        Corrs <- c(Corrs, corr)
        pvalue <- correlation$p.value
        Pvalues <- c(Pvalues, pvalue)
      }
    }

    corr_matrix <- matrix(Corrs, ncol=envs_number, nrow=species_number, byrow=FALSE)
    corr_frame <-  as.data.frame(corr_matrix)
    colnames(corr_frame) <- env_names
    rownames(corr_frame) <- species_names


    pvalue_matrix <- matrix(Pvalues, ncol=envs_number, nrow=species_number, byrow=FALSE)
    pvalue_frame <-  as.data.frame(pvalue_matrix)
    colnames(pvalue_frame) <- env_names
    rownames(pvalue_frame) <- species_names

    # output target table
    write.table(corr_frame, paste0(outdir, "/", cor_file), sep="\t", quote=FALSE, row.names = TRUE)
    write.table(pvalue_frame, paste0(outdir, "/", pvalue_file), sep="\t", quote=FALSE, row.names = TRUE)

    pdf(paste0(outdir, "/", heatmap_pdf), width=width, height=height, onefile=FALSE)
    DEG_heatmap2(corr_frame)
    dev.off()

    #################### heatmap using heatmap.2 ####################
    # data_matrix <- as.matrix(corr_frame)
    # heatmap2(data_matrix)
    #################################################################


    ################################### Calculate RDA ############################################
    # calculate DCA to descide using RDA or CCA
    # 3 > first axis length : RDA
    # 3 < first axis length < 4 : RDA or CCA
    # 4 < first axis length : CCA

    species <- decostand(species, "hellinger")
    envs <- log10(envs)

    DCA <- decorana(species) 
    print(DCA)

    ### RDA
    species_rda <- rda(species ~ ., envs, scale=TRUE)
    CCA <- species_rda$CCA

    print(CCA$eig)

    RDA_sum <- sum(as.vector(CCA$eig))
    RDA1_ratio <- CCA$eig[[1]] / RDA_sum * 100
    RDA2_ratio <- CCA$eig[[2]] / RDA_sum * 100
    
    sample_RDA <- as.data.frame(CCA$u)[, 1:2]
    species_RDA <- as.data.frame(CCA$v)[, 1:2]
    factor_RDA <- as.data.frame(CCA$biplot)[, 1:2]
    write.table(sample_RDA, paste0(outdir, "/sample_RDA.xls"), sep="\t", quote=FALSE, row.names=TRUE)
    write.table(species_RDA, paste0(outdir, "/species_RDA.xls"), sep="\t", quote=FALSE, row.names=TRUE)
    write.table(factor_RDA, paste0(outdir, "/factor_RDA.xls"), sep="\t", quote=FALSE, row.names=TRUE)

    p1 <- ggplot() +
        geom_point(data = sample_RDA, aes(RDA1,RDA2), size = 4) +
        geom_text_repel(data = sample_RDA, aes(RDA1,RDA2, label=row.names(sample_RDA)), size=4)+

        geom_point(data = species_RDA, aes(RDA1,RDA2), size = 2, colour="red") +
        # geom_text_repel(data = species_RDA, aes(RDA1,RDA2, label=row.names(species_RDA)), size=2, colour="red")+
        geom_segment(data = factor_RDA, aes(x = 0, y = 0, xend = RDA1, yend = RDA2),  arrow = arrow(angle=22.5, length = unit(0.35,"cm"), type = "closed"), linetype=1, size=0.6, colour = "blue") + 
        geom_text_repel(data = factor_RDA, aes(RDA1,RDA2,label=row.names(factor_RDA)), colour="blue", size=4)+
        labs(x=paste("RDA 1 (", format(RDA1_ratio, digits=4), "%)", sep=""), y=paste("RDA 2 (", format(RDA2_ratio, digits=4), "%)", sep=""))+
        geom_hline(yintercept=0,linetype=3,size=1) + 
        geom_vline(xintercept=0,linetype=3,size=1)+
        guides(shape=guide_legend(title=NULL,color="black"),
        fill=guide_legend(title=NULL))+
        theme_bw()+theme(panel.grid=element_blank())
    p1

    ### ggvegan

    # p <- autoplot(species_rda, 
    #     arrows = TRUE,
    #     axes = c(1, 2), 
    #     geom =  c("point", "text"), 
    #     # layers = c( "species","sites", "biplot", "centroids"), 
    #     layers = c("species","sites", "biplot", "centroids"),
    #     legend.position = "right", 
    #     loadings.label.size = 5,
    #     title = "RDA")
    # p <- p + theme_bw()+ theme(panel.grid=element_blank())
    # p
    ggsave(paste0(outdir, "/RDA.pdf"), height=width, width=width)

}


species_factor_cor_RDA(argv$species, argv$factor, argv$outdir, argv$correlation, argv$pvalue, argv$heatmap, argv$width, argv$height)

