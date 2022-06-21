# First, we need to perform prunning
# Then we calculate the first 6 PCs

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/BC_targetData
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/BC_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/BC_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData_pca

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_targetData --indep-pairwise 200 50 0.25 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData.prune.in --pca 6 --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData_pca
