# run 1. 2.

### split base/target data
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_baseData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_targetData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_baseData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_targetData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_baseData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_targetData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_baseData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_targetData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_base_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_baseData

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_target_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_targetData


### pca
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_baseData --extract /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_baseData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_baseData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_baseData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_baseData --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_her2_baseData_forPCA

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_baseData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_her2_baseData_forPCA.prune.in --pca --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_her2_baseData_forPCA

# run 4.make_pheCov_file.py

### base data GWAS
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_baseData --pheno /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_logistic

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_baseData --pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_logistic

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_baseData --pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_logistic

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_baseData --pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_logistic

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_baseData --pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updatedSex_her2_baseData_logistic

### calculate MAF
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_freq

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_freq

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_freq

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_freq

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_baseData --freq --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_her2_baseData_freq