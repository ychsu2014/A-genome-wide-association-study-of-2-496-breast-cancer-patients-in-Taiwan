in_file = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/PRS_group_count.txt"
out_file1 = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_allBC.txt"
out_file2 = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_luminalA.txt"
out_file3 = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_luminalB.txt"
out_file4 = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_basal.txt"
out_file5 = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/odds_ratio/odds_ratio_her2.txt"

library(epitools)

file_list = c(out_file1, out_file2, out_file3, out_file4, out_file5)
df = read.csv(in_file, sep = "\t")
for (i in 1:5){
	mat = matrix(, nrow = 5, ncol = 4)
	colnames(mat) = c("20_40%", "40_60%", "60_80%", "80_100%")
	rownames(mat) = c("OR", "OR_lower", "OR_upper", "chi_p", "fisher_p")
	for (j in 3:6){
		count1 = df[i,2]
		count2 = df[i,j]
		count3 = df[i,7]
		count4 = df[i,j+5]
		dat2 <- matrix(c(count1,count2,count3,count4), nrow = 2, ncol = 2)
		colnames(dat2) <- c("control", "case")
		rownames(dat2) <- c("0-20%", "80%-100%")
		print(dat2)
		odds = epitools::oddsratio(dat2, correction = F)
		OR_mean = odds$measure[2,1]
		OR_lower = odds$measure[2,2]
		OR_upper = odds$measure[2,3]
		chi_p = odds$p.value[2,3]
		fisher_p = odds$p.value[2,2]
		temp_m = matrix(c(OR_mean, OR_lower, OR_upper, chi_p, fisher_p), nrow = 5, ncol = 1)
		mat[,j-2] = temp_m
	}
	output_file = file_list[i]
	print(output_file)
	write.table(mat, output_file, sep = "\t", quote = FALSE)
}
