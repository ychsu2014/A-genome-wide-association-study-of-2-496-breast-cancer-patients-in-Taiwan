# ref_control, control, ref_case, case
dat2 <- matrix(c(32,32,7,9), nrow = 2, ncol = 2)
colnames(dat2) <- c("control", "case")
rownames(dat2) <- c("0-20%", "80%-100%")

library(epitools)
epitools::oddsratio(dat2, correction = F)
