# This has to be run in the folder of PRSice
Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS_result_v2

Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_PRS_result_v2

Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_luminalA_baseData_logistic_filterMAF_updateEffect.txt \
        --target /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_PRS_result_v2

Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_luminalB_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_PRS_result_v2

Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_basal_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_PRS_result_v2

Rscript /home/iHiO10009/PRSice/PRSice.R \
	--prsice /home/iHiO10009/PRSice/PRSice_linux \
	--base /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_her2_baseData_logistic_filterMAF_updateEffect.txt \
	--target /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_targetData \
	--binary-target T \
	--pheno /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_pheno_data.txt \
	--cov /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_targetData.covariate \
	--base-maf MAF:0.01 \
	--base-info INFO:0.8 \
	--stat OR \
	--or \
	--print-snp \
	--out /home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_PRS_result_v2
