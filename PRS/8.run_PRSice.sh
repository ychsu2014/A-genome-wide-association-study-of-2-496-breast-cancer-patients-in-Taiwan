# This has to be run in the folder of PRSice

# all BC
Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_PRS_result

# luminal A
Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_logistic_filterMAF_updateEffect.txt \
    --target /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalA_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_PRS_result

# luminal B
Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_luminalB_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_PRS_result

# basal-like
Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_basal_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_PRS_result

# her2
Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updatedSex_her2_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_her2_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_PRS_result
