#From Swarchal
library(ggplot2)
library(reshape2)

df_expression <- read.csv("expression.csv")
df_molten <- melt(df_expression)
ggplot(data = df_molten,
       aes(x = variable, y = MouseID, fill = value)) + 
    geom_raster() +
    xlab("Protein") + 
    scale_fill_distiller(palette = "RdYlBu", trans = "log10") +
    theme(axis.text.x = element_text(angle = 90, hjust = 1),
          axis.text.y = element_blank()) + 
    ggtitle("ggplot heatmap")
