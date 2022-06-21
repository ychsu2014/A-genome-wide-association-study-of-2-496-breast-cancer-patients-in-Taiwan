# exclude 1785 BC patients that does not meet the filtering criteria
plink --bfile /home/iHiO10009/Dataset/BDC_TWB2_array_deID_release_210820/BDC_TWB2_array_deID_release_210820 --remove /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BC_toBeRemove_list.txt --make-bed --allow-extra-chr --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785

# keep clean subjects
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785 --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v3/clean_subjects_for_keep.txt --make-bed --allow-extra-chr --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean

# remove control SNPs
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean --exclude /home/iHiO10009/yuching/data/1.QC/TWB2.0_control_SNP_AffyID.txt --make-bed --allow-extra-chr --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP

# imputed data
# exclude 1785 BC patients that does not meet the filtering criteria
plink --bfile /home/iHiO10009/Dataset/IMPUTE2_Genotyping_deID_release_20210823/IMPUTE2_Genotyping_deID_release_20210823 --remove /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BC_toBeRemove_list.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_remove1785

# keep clean subjects
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_remove1785 --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v3/clean_subjects_for_keep.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_remove1785_keepClean

#run 1-1~ 1-3

# sex check
# update gender
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_updateGender.txt --allow-extra-chr --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_updateGender.txt --allow-extra-chr --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex --allow-extra-chr --check-sex --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex

grep "PROBLEM" /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex.sexcheck > /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_sexCheck_rmInd.txt

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex --remove /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_sexCheck_rmInd.txt --allow-extra-chr --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd

# remove non-autosomal SNPs
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd --chr 0-22 --make-bed --allow-extra-chr --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto

# keep case and multiple controls
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v3/case_10Control_list_forKeepCommand.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto_keep10Controls

# IBD
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto_keep10Controls --indep-pairwise 50 5 0.2 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto_keep10Controls

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto_keep10Controls --extract /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto_keep10Controls.prune.in --all --genome --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto_keep10Controls

# run 1-4
# manually check 1-4 output file, no changes made

# remove cryptic relatedness
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_210820_remove1785_keepClean_rmConSNP_updateSex_rmSexInd_auto_keep10Controls --remove /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_BC_10Controls_IBD_removal_list.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_removeIBD

# run 1-5

# imputed data
# keep BC and controls
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_remove1785_keepClean --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_list_forKeepCmd.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls

# pca
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_for_pca

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls --extract /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_for_pca.prune.in --pca --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_pca

# update gender 
plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex

# run 1-6

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --pheno /home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_pheCov_file.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_pheCov_file.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_logistic

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex --freq --out /home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_freq