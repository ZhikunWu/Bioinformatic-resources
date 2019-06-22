#!/usr/bin/R
require("veenDiagram")
tiff(filename = "Triple_Venn_diagram.tiff", compression = "lzw")
#grid.newpage()
venn.plot <- draw.triple.venn(
area1 = 65,
area2 = 75,
area3 = 85,
n12 = 35,
n23 = 15,
n13 = 25,
n123 = 5,
category = c("First", "Second", "Third"),
fill = c("blue", "red", "green"),
lty = "blank",
cex = 2,
cat.cex = 2,
cat.col = c("blue", "red", "green")
)
grid.draw(venn.plot)
dev.off()


##########optional method 
#grid.newpage()
#draw.triple.venn(area1 = nrow(subset(d, Dog == 1)), area2 = nrow(subset(d, Cat == 
#    1)), area3 = nrow(subset(d, Lizard == 1)), n12 = nrow(subset(d, Dog == 1 & 
#    Cat == 1)), n23 = nrow(subset(d, Cat == 1 & Lizard == 1)), n13 = nrow(subset(d, 
#    Dog == 1 & Lizard == 1)), n123 = nrow(subset(d, Dog == 1 & Cat == 1 & Lizard == 
#    1)), category = c("Dog People", "Cat People", "Lizard People"), lty = "blank", 
#	fill = c("skyblue", "pink1", "mediumorchid"))
	
