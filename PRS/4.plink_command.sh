# split base/target data

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_base_sID_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_target_sID_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_targetData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_targetData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_targetData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_targetData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_targetData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --keep /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_targetData

# pca
#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData --extract /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData_forPCA


#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData --extract /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData_forPCA


#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_forPCA


#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData  --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_forPCA

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_forPCA

# run 5-1.

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_pheCov_file_v2.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData_logistic_assoc

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_pheCov_file_v2.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData_logistic_assoc

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_logistic_assoc

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_logistic_assoc

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_logistic_assoc

#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_logistic_assoc

# did not get what I want
#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_subtype_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_pheCov_file_v2.txt --pheno-name Subtype --all-pheno --covar /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_subtype_baseData_logistic_assoc

# can not work
#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_subtype_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_pheCov_file_v2.txt --pheno-name Subtype i--covar /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_subtype_baseData_logistic_assoc

# can not work
#plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_subtype_baseData --pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_pheCov_file_v2.txt --pheno-name Subtypie --covar /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --assoc --ci 0.95 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_subtype_baseData_asso

plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_freq

plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_freq

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_freq

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_freq

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_freq

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_freq

# run 6, 7, 8

