awk 'NR!=1{print $3}' /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_targetData_clump.clumped >  /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_target.valid.snp
awk '{print $2,$13}' /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_baseData_logistic_filterMAF_updateEffect.txt >  /home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_SNP.pvalue

#echo "0.001 0 0.001" > range_list 
#echo "0.05 0 0.05" >> range_list
#echo "0.1 0 0.1" >> range_list
#echo "0.2 0 0.2" >> range_list
#echo "0.3 0 0.3" >> range_list
#echo "0.4 0 0.4" >> range_list
#echo "0.5 0 0.5" >> range_list
