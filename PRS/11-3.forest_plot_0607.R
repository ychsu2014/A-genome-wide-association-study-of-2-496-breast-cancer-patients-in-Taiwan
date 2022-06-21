png("D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/all_BC.png", width = 500, height = 200)
afile <- "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_allBC.txt"
df <- read.csv(afile, sep = "\t")
test_data <- structure(list(
  mean = c(NA, round(log(df[1,1]),2), round(log(df[1,2]),2), round(log(df[1,3]),2), round(log(df[1,4]),2)),
  lower = c(NA, round(log(df[2,1]),2), round(log(df[2,2]),2), round(log(df[2,3]),2), round(log(df[2,4]),2)),
  upper = c(NA, round(log(df[3,1]),2), round(log(df[3,2]),2), round(log(df[3,3]),2), round(log(df[3,4]),2))
),
.Names = c("mean", "lower", "upper"),
row.names = c(NA, -5L),
class = "data.frame")

print(test_data)
# labels
mean1 <- formatC(round(log(df[1,1]), 2), format='f', digits=2)
lower1 <- formatC(round(log(df[2,1]), 2), format='f', digits=2)
upper1 <- formatC(round(log(df[3,1]), 2), format='f', digits=2)
group_20_40 <- paste(mean1, "(", lower1, ",", upper1, ")", sep = "")
mean2 <- formatC(round(log(df[1,2]), 2), format='f', digits=2)
lower2 <- formatC(round(log(df[2,2]), 2), format='f', digits=2)
upper2 <- formatC(round(log(df[3,2]), 2), format='f', digits=2)
group_40_60 <- paste(mean2, "(", lower2, ",", upper2, ")", sep = "")
mean3 <- formatC(round(log(df[1,3]), 2), format='f', digits=2)
lower3 <- formatC(round(log(df[2,3]), 2), format='f', digits=2)
upper3 <- formatC(round(log(df[3,3]), 2), format='f', digits=2)
group_60_80 <- paste(mean3, "(", lower3, ",", upper3, ")", sep = "")
mean4 <- formatC(round(log(df[1,4]), 2), format='f', digits=2)
lower4 <- formatC(round(log(df[2,4]), 2), format='f', digits=2)
upper4 <- formatC(round(log(df[3,4]), 2), format='f', digits=2)
group_80_100 <- paste(mean4, "(", lower4, ",", upper4, ")", sep = "")
tabletext <- cbind(
  c("PRS", "20-40%", "40-60%", "60-80%", "80-100%"),
  c("log(OR)", group_20_40, group_40_60, group_60_80, group_80_100)
)
print(tabletext)
# tick
ticks <- seq(-3,3,0.5)
attr(ticks, "labels") <- as.character(ticks)
# forest plot
forestplot(tabletext, 
           test_data, 
           new_page = TRUE, 
           xlog = FALSE, 
           boxsize = 0.1,
           cex = 0.8,
           xticks = ticks,
           txt_gp = fpTxtGp(label=gpar(fontsize=14),
                            ticks=gpar(fontsize=24),
                            xlab=gpar(fontsize=14),
                            title=gpar(fontsize=14))
)
dev.off()

# luminal A
png("D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/luminalA.png", width = 500, height = 200)
afile <- "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_luminalA.txt"
df <- read.csv(afile, sep = "\t")
test_data <- structure(list(
  mean = c(NA, round(log(df[1,1]),2), round(log(df[1,2]),2), round(log(df[1,3]),2), round(log(df[1,4]),2)),
  lower = c(NA, round(log(df[2,1]),2), round(log(df[2,2]),2), round(log(df[2,3]),2), round(log(df[2,4]),2)),
  upper = c(NA, round(log(df[3,1]),2), round(log(df[3,2]),2), round(log(df[3,3]),2), round(log(df[3,4]),2))
),
.Names = c("mean", "lower", "upper"),
row.names = c(NA, -5L),
class = "data.frame")

print(test_data)
# labels
mean1 <- formatC(round(log(df[1,1]), 2), format='f', digits=2)
lower1 <- formatC(round(log(df[2,1]), 2), format='f', digits=2)
upper1 <- formatC(round(log(df[3,1]), 2), format='f', digits=2)
group_20_40 <- paste(mean1, "(", lower1, ",", upper1, ")", sep = "")
mean2 <- formatC(round(log(df[1,2]), 2), format='f', digits=2)
lower2 <- formatC(round(log(df[2,2]), 2), format='f', digits=2)
upper2 <- formatC(round(log(df[3,2]), 2), format='f', digits=2)
group_40_60 <- paste(mean2, "(", lower2, ",", upper2, ")", sep = "")
mean3 <- formatC(round(log(df[1,3]), 2), format='f', digits=2)
lower3 <- formatC(round(log(df[2,3]), 2), format='f', digits=2)
upper3 <- formatC(round(log(df[3,3]), 2), format='f', digits=2)
group_60_80 <- paste(mean3, "(", lower3, ",", upper3, ")", sep = "")
mean4 <- formatC(round(log(df[1,4]), 2), format='f', digits=2)
lower4 <- formatC(round(log(df[2,4]), 2), format='f', digits=2)
upper4 <- formatC(round(log(df[3,4]), 2), format='f', digits=2)
group_80_100 <- paste(mean4, "(", lower4, ",", upper4, ")", sep = "")
tabletext <- cbind(
  c("PRS", "20-40%", "40-60%", "60-80%", "80-100%"),
  c("log(OR)", group_20_40, group_40_60, group_60_80, group_80_100)
)
print(tabletext)
# tick
ticks <- seq(-3,3,0.5)
attr(ticks, "labels") <- as.character(ticks)
# forest plot
forestplot(tabletext, 
           test_data, 
           new_page = TRUE, 
           xlog = FALSE, 
           boxsize = 0.1,
           cex = 0.8,
           xticks = ticks,
           txt_gp = fpTxtGp(label=gpar(fontsize=14),
                            ticks=gpar(fontsize=24),
                            xlab=gpar(fontsize=14),
                            title=gpar(fontsize=14))
)
dev.off()

# luminal B
png("D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/luminalB.png", width = 500, height = 200)
afile <- "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_luminalB.txt"
df <- read.csv(afile, sep = "\t")
test_data <- structure(list(
  mean = c(NA, round(log(df[1,1]),2), round(log(df[1,2]),2), round(log(df[1,3]),2), round(log(df[1,4]),2)),
  lower = c(NA, round(log(df[2,1]),2), round(log(df[2,2]),2), round(log(df[2,3]),2), round(log(df[2,4]),2)),
  upper = c(NA, round(log(df[3,1]),2), round(log(df[3,2]),2), round(log(df[3,3]),2), round(log(df[3,4]),2))
),
.Names = c("mean", "lower", "upper"),
row.names = c(NA, -5L),
class = "data.frame")

print(test_data)
# labels
mean1 <- formatC(round(log(df[1,1]), 2), format='f', digits=2)
lower1 <- formatC(round(log(df[2,1]), 2), format='f', digits=2)
upper1 <- formatC(round(log(df[3,1]), 2), format='f', digits=2)
group_20_40 <- paste(mean1, "(", lower1, ",", upper1, ")", sep = "")
mean2 <- formatC(round(log(df[1,2]), 2), format='f', digits=2)
lower2 <- formatC(round(log(df[2,2]), 2), format='f', digits=2)
upper2 <- formatC(round(log(df[3,2]), 2), format='f', digits=2)
group_40_60 <- paste(mean2, "(", lower2, ",", upper2, ")", sep = "")
mean3 <- formatC(round(log(df[1,3]), 2), format='f', digits=2)
lower3 <- formatC(round(log(df[2,3]), 2), format='f', digits=2)
upper3 <- formatC(round(log(df[3,3]), 2), format='f', digits=2)
group_60_80 <- paste(mean3, "(", lower3, ",", upper3, ")", sep = "")
mean4 <- formatC(round(log(df[1,4]), 2), format='f', digits=2)
lower4 <- formatC(round(log(df[2,4]), 2), format='f', digits=2)
upper4 <- formatC(round(log(df[3,4]), 2), format='f', digits=2)
group_80_100 <- paste(mean4, "(", lower4, ",", upper4, ")", sep = "")
tabletext <- cbind(
  c("PRS", "20-40%", "40-60%", "60-80%", "80-100%"),
  c("log(OR)", group_20_40, group_40_60, group_60_80, group_80_100)
)
print(tabletext)
# tick
ticks <- seq(-3,3,0.5)
attr(ticks, "labels") <- as.character(ticks)
# forest plot
forestplot(tabletext, 
           test_data, 
           new_page = TRUE, 
           xlog = FALSE, 
           boxsize = 0.1,
           cex = 0.8,
           xticks = ticks,
           txt_gp = fpTxtGp(label=gpar(fontsize=14),
                            ticks=gpar(fontsize=24),
                            xlab=gpar(fontsize=14),
                            title=gpar(fontsize=14))
)
dev.off()

# basal
png("D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/basal.png", width = 500, height = 200)
afile <- "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_basal.txt"
df <- read.csv(afile, sep = "\t")
test_data <- structure(list(
  mean = c(NA, round(log(df[1,1]),2), round(log(df[1,2]),2), round(log(df[1,3]),2), round(log(df[1,4]),2)),
  lower = c(NA, round(log(df[2,1]),2), round(log(df[2,2]),2), round(log(df[2,3]),2), round(log(df[2,4]),2)),
  upper = c(NA, round(log(df[3,1]),2), round(log(df[3,2]),2), round(log(df[3,3]),2), round(log(df[3,4]),2))
),
.Names = c("mean", "lower", "upper"),
row.names = c(NA, -5L),
class = "data.frame")

print(test_data)
# labels
mean1 <- formatC(round(log(df[1,1]), 2), format='f', digits=2)
lower1 <- formatC(round(log(df[2,1]), 2), format='f', digits=2)
upper1 <- formatC(round(log(df[3,1]), 2), format='f', digits=2)
group_20_40 <- paste(mean1, "(", lower1, ",", upper1, ")", sep = "")
mean2 <- formatC(round(log(df[1,2]), 2), format='f', digits=2)
lower2 <- formatC(round(log(df[2,2]), 2), format='f', digits=2)
upper2 <- formatC(round(log(df[3,2]), 2), format='f', digits=2)
group_40_60 <- paste(mean2, "(", lower2, ",", upper2, ")", sep = "")
mean3 <- formatC(round(log(df[1,3]), 2), format='f', digits=2)
lower3 <- formatC(round(log(df[2,3]), 2), format='f', digits=2)
upper3 <- formatC(round(log(df[3,3]), 2), format='f', digits=2)
group_60_80 <- paste(mean3, "(", lower3, ",", upper3, ")", sep = "")
mean4 <- formatC(round(log(df[1,4]), 2), format='f', digits=2)
lower4 <- formatC(round(log(df[2,4]), 2), format='f', digits=2)
upper4 <- formatC(round(log(df[3,4]), 2), format='f', digits=2)
group_80_100 <- paste(mean4, "(", lower4, ",", upper4, ")", sep = "")
tabletext <- cbind(
  c("PRS", "20-40%", "40-60%", "60-80%", "80-100%"),
  c("log(OR)", group_20_40, group_40_60, group_60_80, group_80_100)
)
print(tabletext)
# tick
ticks <- seq(-3,3,0.5)
attr(ticks, "labels") <- as.character(ticks)
# forest plot
forestplot(tabletext, 
           test_data, 
           new_page = TRUE, 
           xlog = FALSE, 
           boxsize = 0.1,
           cex = 0.8,
           xticks = ticks,
           txt_gp = fpTxtGp(label=gpar(fontsize=14),
                            ticks=gpar(fontsize=24),
                            xlab=gpar(fontsize=14),
                            title=gpar(fontsize=14))
)
dev.off()

# her2
png("D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/her2.png", width = 500, height = 200)
afile <- "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_her2.txt"
df <- read.csv(afile, sep = "\t")
test_data <- structure(list(
  mean = c(NA, round(log(df[1,1]),2), round(log(df[1,2]),2), round(log(df[1,3]),2), round(log(df[1,4]),2)),
  lower = c(NA, round(log(df[2,1]),2), round(log(df[2,2]),2), round(log(df[2,3]),2), round(log(df[2,4]),2)),
  upper = c(NA, round(log(df[3,1]),2), round(log(df[3,2]),2), round(log(df[3,3]),2), round(log(df[3,4]),2))
),
.Names = c("mean", "lower", "upper"),
row.names = c(NA, -5L),
class = "data.frame")

print(test_data)
# labels
mean1 <- formatC(round(log(df[1,1]), 2), format='f', digits=2)
lower1 <- formatC(round(log(df[2,1]), 2), format='f', digits=2)
upper1 <- formatC(round(log(df[3,1]), 2), format='f', digits=2)
group_20_40 <- paste(mean1, "(", lower1, ",", upper1, ")", sep = "")
mean2 <- formatC(round(log(df[1,2]), 2), format='f', digits=2)
lower2 <- formatC(round(log(df[2,2]), 2), format='f', digits=2)
upper2 <- formatC(round(log(df[3,2]), 2), format='f', digits=2)
group_40_60 <- paste(mean2, "(", lower2, ",", upper2, ")", sep = "")
mean3 <- formatC(round(log(df[1,3]), 2), format='f', digits=2)
lower3 <- formatC(round(log(df[2,3]), 2), format='f', digits=2)
upper3 <- formatC(round(log(df[3,3]), 2), format='f', digits=2)
group_60_80 <- paste(mean3, "(", lower3, ",", upper3, ")", sep = "")
mean4 <- formatC(round(log(df[1,4]), 2), format='f', digits=2)
lower4 <- formatC(round(log(df[2,4]), 2), format='f', digits=2)
upper4 <- formatC(round(log(df[3,4]), 2), format='f', digits=2)
group_80_100 <- paste(mean4, "(", lower4, ",", upper4, ")", sep = "")
tabletext <- cbind(
  c("PRS", "20-40%", "40-60%", "60-80%", "80-100%"),
  c("log(OR)", group_20_40, group_40_60, group_60_80, group_80_100)
)
print(tabletext)
# tick
ticks <- seq(-3,3,0.5)
attr(ticks, "labels") <- as.character(ticks)
# forest plot
forestplot(tabletext, 
           test_data, 
           new_page = TRUE, 
           xlog = FALSE, 
           boxsize = 0.1,
           cex = 0.8,
           xticks = ticks,
           txt_gp = fpTxtGp(label=gpar(fontsize=14),
                            ticks=gpar(fontsize=24),
                            xlab=gpar(fontsize=14),
                            title=gpar(fontsize=14))
)
dev.off()