# generate PRS
#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_targetData --score /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_baseData_logistic_filterMAF_updateEffect.txt 2 4 15 header --q-score-range range_list /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_SNP.pvalue --extract /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_target.valid.snp --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS

# First, we need to perform prunning
#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_targetData
# Then we calculate the first 6 PCs
#plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_targetData --extract /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_targetData
plink --bfile /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_targetData --extract /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_targetData
plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_targetData --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_targetData
plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_targetData --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_targetData
plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_targetData --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_targetData
plink --bfile /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_targetData --extract /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_targetData_pca
