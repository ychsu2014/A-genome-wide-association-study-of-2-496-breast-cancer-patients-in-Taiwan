# extract SNPs used in PRS calculation
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_SNP_list_forExtractCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_targetData_extractPRS_SNPs

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_SNP_list_forExtractCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData_extractPRS_SNPs

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_SNP_list_forExtractCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData_extractPRS_SNPs

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_SNP_list_forExtractCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData_extractPRS_SNPs

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_targetData --extract /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_SNP_list_forExtractCmd.txt --make-bed --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData_extractPRS_SNPs

# get individual genotypes for subsequent visualization
plink --bfile /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_targetData_extractPRS_SNPs --recode list --out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_ind_list

plink --bfile /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData_extractPRS_SNPs --recode list --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_ind_list

plink --bfile /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData_extractPRS_SNPs --recode list --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_ind_list

plink --bfile /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData_extractPRS_SNPs --recode list --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_ind_list

plink --bfile /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData_extractPRS_SNPs --recode list --out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_ind_list