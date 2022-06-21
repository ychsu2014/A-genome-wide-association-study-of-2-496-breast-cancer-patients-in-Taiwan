#run 7-1(PCA), 7-2(pheno, cov files) before running this script

#cov_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_cov_data.txt"
#pca_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/BC_targetData_pca.eigenvec"
#covar_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_targetData.covariate"

#cov_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_cov_data.txt"
#pca_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData_pca.eigenvec"
#covar_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData.covariate"

#cov_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_cov_data.txt"
#pca_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData_pca.eigenvec"
#covar_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData.covariate"

#cov_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_cov_data.txt"
#pca_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData_pca.eigenvec"
#covar_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData.covariate"

cov_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_cov_data.txt"
pca_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData_pca.eigenvec"
covar_file <- "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData.covariate"

covariate <- read.table(cov_file, header=T)
pcs <- read.table(pca_file, header=F)
colnames(pcs) <- c("FID","IID", paste0("PC",1:6))
cov <- merge(covariate, pcs, by=c("FID", "IID"))
write.table(cov, covar_file, quote=F, row.names=F)
