### allele freq in cases
# keep only cases
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyCase

# MAF
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyCase --freq --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyCase_freq

# allele counts
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyCase --freq counts --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyCase_freq_count

### allele freq in controls
# keep only controls
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyControl

# MAF
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyControl --freq --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyControl_freq

# allele counts
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyControl --freq counts --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyControl_freq_count