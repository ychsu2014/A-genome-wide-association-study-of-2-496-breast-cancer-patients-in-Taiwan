## remove control SNPs
#plink --bfile /home/iHiO10009/Dataset/BDC_TWB2_array_deID_release_210820/BDC_TWB2_array_deID_release_210820 --exclude /home/iHiO10009/yuching/data/1.QC/TWB2.0_control_SNP_AffyID.txt --make-bed --allow-extra-chr --out /home/iHiO10009/yuching/data/1.QC/BDC_210820_removeConSNP

#run 1-1~ 1-3

# sex check
# update gender
#plink --bfile /home/iHiO10009/yuching/data/1.QC/BDC_210820_removeConSNP --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_control_updateGender.txt --allow-extra-chr --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_BC_updateGender.txt --allow-extra-chr --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex --allow-extra-chr --check-sex --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex
#grep "PROBLEM" /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex.sexcheck > /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex_sexCheck_rmInd.txt

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex --remove /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex_sexCheck_rmInd.txt --allow-extra-chr --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex_rmSexInd

## remove non-autosomal SNPs
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_updateSex_rmSexInd --chr 0-22 --make-bed --allow-extra-chr --out /home/iHiO10009/yuching/data/1.QC/BDC_210820_removeConSNP_auto


## keep case and multiple controls
#plink --bfile /home/iHiO10009/yuching/data/1.QC/BDC_210820_removeConSNP_auto --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v2/case_allControl_list_forKeepCommand_v2.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2

##### >65 y/o controls
#plink --bfile /home/iHiO10009/yuching/data/1.QC/BDC_210820_removeConSNP_auto --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v2/case_65yo_control_list_forKeepCommand_v2.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2

## IBD
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2 --indep-pairwise 50 5 0.2 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2

##### >65 y/o controls
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2 --indep-pairwise 50 5 0.2 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2 --extract /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2.prune.in --all --genome --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2

##### >65 y/o controls
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2 --extract /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2.prune.in --all --genome --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2

# run 1-4
# manually check 1-3 output file 
# To keep the same bc patients, I checked the two files. The 65yoControls & multiple controls will remove the same BC patients, so use the origial files for removing removing related individuals.

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2 --remove /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_BC_multipleControls_IBD_removal_list_v2.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_removeIBD_v2

##### >65 y/o controls
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2 --remove /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_BC_65yoControls_IBD_removal_list_v2.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_removeIBD_v2

# run 1-5

# imputed data
# keep clean subjects(run once)
#plink --bfile /home/iHiO10009/Dataset/IMPUTE2_Genotyping_deID_release_20210823/IMPUTE2_Genotyping_deID_release_20210823 --keep /home/iHiO10009/yuching/data/1.QC/clean_subjects.txt  --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepCleanSbj

# keep BC and controls
#plink --bfile /home/iHiO10009/Dataset/IMPUTE2_Genotyping_deID_release_20210823/IMPUTE2_Genotyping_deID_release_20210823 --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_control_list_forKeepCmd_v2.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_v2

##### >65 y/o controls
#plink --bfile /home/iHiO10009/Dataset/IMPUTE2_Genotyping_deID_release_20210823/IMPUTE2_Genotyping_deID_release_20210823 --keep /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_list_forKeepCmd_v2.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_v2

# pca
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_v2 --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_for_pca_v2

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_v2 --extract /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_for_pca_v2.prune.in --pca --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_pca_v2

##### >65 y/o controls
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_v2 --indep-pairwise 200 5 0.2 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_for_pca_v2

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_v2 --extract /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_for_pca_v2.prune.in --pca --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_pca_v2


# update gender 
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_v2 --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_control_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2
#<F9>plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_BC_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_v2 --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_control_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2 --update-sex /home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_BC_updateGender.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2

# run 1-6

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2 --pheno /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_pheCov_file_v2.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_assoc_v2

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --pheno /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_control_pheCov_file_v2.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_control_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --parameters 1 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_assoc_v2 

#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --pheno /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_control_pheCov_file_v2.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_control_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_assoc_noPara1_v2

# (no use)
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2 --keep /home/iHiO10009/yuching/scripts/temp/test/QC_GWAS_v2/test_data_pID_list.txt --make-bed --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2v_testdata

# still no A2, get A1/A2 from bim file (no use)
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2v_testdata --keep-allele-order --pheno /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_pheCov_file_v2.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_assoc_noPara1_v2_testdata

# no A2, but SE appeared! (used)
#plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2 --pheno /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_pheCov_file_v2.txt --pheno-name Disease --covar /home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_pheCov_file_v2.txt --covar-name age, gender, pc1, pc2, pc3, pc4, pc5, pc6, pc7,pc8, pc9, pc10 --logistic hide-covar --ci 0.95 --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_assoc_noPara1_v2

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2 --freq --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2_freq

plink --bfile /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2 --freq --out /home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2_freq
