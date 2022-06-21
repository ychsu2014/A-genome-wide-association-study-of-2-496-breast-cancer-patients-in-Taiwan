in_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_logistic_addFrq.txt"
in_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_logistic_addFrq.txt"
in_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updatedSex_her2_baseData_logistic_addFrq.txt"
in_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_logistic_addFrq.txt"
in_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_logistic_addFrq.txt"

out_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_logistic_filterMAF.txt"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_logistic_filterMAF.txt"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updatedSex_her2_baseData_logistic_filterMAF.txt"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_logistic_filterMAF.txt"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_logistic_filterMAF.txt"

def filterMAF(inFile, outFile, header = True):
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    if header == True:
        header_line = lines[0]
        lines = lines[1:]
    fout.write(header_line)
    for line in lines:
        cols = line.strip("\n").split("\t")
        MAF = float(cols[13])
        if MAF >= 0.01:
            fout.write(line)
    f.close()
    fout.close()

filterMAF(in_file1, out_file1)
filterMAF(in_file2, out_file2)
filterMAF(in_file3, out_file3)
filterMAF(in_file4, out_file4)
filterMAF(in_file5, out_file5)
