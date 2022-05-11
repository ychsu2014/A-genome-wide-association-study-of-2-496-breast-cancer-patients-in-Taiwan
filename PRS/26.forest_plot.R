library(forestplot)
test_data <- structure(list(
   # ageMatch
   #mean = c(NA, 0.37, 0.73, 1.16, 1.69),
   #lower = c(NA, -0.06, 0.33, 0.78, 1.33),
   #upper = c(NA, 0.81, 1.15, 1.56, 2.07)
   # 65yoControl
   #mean = c(NA, 0.11, -0.03, 0.03, 0.08),
   #lower = c(NA, -0.2, -0.35, -0.28, -0.23),
   #upper = c(NA, 0.42, 0.29, 0.35, 0.39)
   # luminalA
   #mean = c(NA, 0.42, 0.87, 1.27, 1.91),
   #lower = c(NA, -0.25, 0.25, 0.69, 1.35),
   #upper = c(NA, 1.13, 1.53, 1.91, 2.52)
   # luminalB
   #mean = c(NA, 0.48, 0.70, 0.95, 0.95),
   #lower = c(NA, -0.72, -0.45, -0.13, -0.13),
   #upper = c(NA, 1.78, 1.97, 2.19, 2.19)
   # basal
   #mean = c(NA, 0.78, 0, 1.06, 1.35),
   #lower = c(NA, -0.45, -1.56, -0.11, 0.22),
   #upper = c(NA, 2.20, 1.56, 2.45, 2.70)
   # her2
   mean = c(NA, 0.53, 0.24, -0.81, 0.24),
   lower = c(NA, -0.52, -0.87, -2.47, -0.87),
   upper = c(NA, 1.64, 1.40, 0.59, 1.40)
   
   ),
   .Names = c("mean", "lower", "upper"),
   row.names = c(NA, -5L),
   class = "data.frame")

tabletext <- cbind(
   c("PRS", "20-40%", "40-60%", "60-80%", "80-100%"),
   # ageMatch
   #c("OR(log)", "0.37(-0.06,0.81)" , "0.73(0.33,1.15)", "1.16(0.78,1.56)", "1.69(1.33,2.07)")
   # 65yoControl
   #c("OR(log)", "0.11(-0.2,0.42)", "-0.03(-0.35,0.29)", "0.03(-0.28,0.35)", "0.08(-0.23,0.39)")
   # luminal A
   #c("OR(log)", "0.42(-0.25,1.13)", "0.87(0.25,1.53)", "1.27(0.69,1.91)", "1.91(1.35,2.52)")
   # luminal B
   #c("OR(log)", "0.48(-0.72,1.78)", "0.70(-0.45,1.97)", "0.95(-0.13,2.19)", "0.95(-0.13,2.19)")
   # basal
   #c("OR(log)", "0.78(-0.45,2.20)", "0.00(-1.56,1.56)", "1.06(-0.11,2.45)", "1.35(0.22,2.70)")
   # her2
   c("OR(log)", "0.53(-0.52,1.64)", "0.24(-0.87,1.40)", "-0.81(-2.47,0.59)", "0.24(-0.87,1.40)")
)

ticks <- seq(-3,3,0.5)
attr(ticks, "labels") <- as.character(ticks)

forestplot(tabletext,
           test_data,
           new_page = TRUE,
           xlog = FALSE,
           boxsize = 0.1,
           cex = 0.8,
           xticks = ticks,
           txt_gp = fpTxtGp(label=gpar(fontsize=10), 
                          ticks=gpar(fontsize=10),
                          xlab=gpar(fontsize=10),
                          title=gpar(fontsize=10))
)

