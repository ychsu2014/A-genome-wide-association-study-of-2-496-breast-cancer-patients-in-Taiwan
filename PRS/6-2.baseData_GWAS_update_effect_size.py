in_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_logistic_filterMAF.txt"
in_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_logistic_filterMAF.txt"
in_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updatedSex_her2_baseData_logistic_filterMAF.txt"
in_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_logistic_filterMAF.txt"
in_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_logistic_filterMAF.txt"

out_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_logistic_filterMAF_updateEffect.txt"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_logistic_filterMAF_updateEffect.txt"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updatedSex_her2_baseData_logistic_filterMAF_updateEffect.txt"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_logistic_filterMAF_updateEffect.txt"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_logistic_filterMAF_updateEffect.txt"


import math

def updateEffect(inFile, outFile):
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    header = lines[0].strip("\n").split("\t")
    header.append("BETA")
    fout.write("\t".join(header) + "\n")
    lines = lines[1:]
    for line in lines:
        cols = line.strip("\n").split("\t")
        OR = cols[7]
        if OR != "NA":
            beta = math.log(float(OR))
            cols.append(str(beta))
            fout.write("\t".join(cols) + "\n")

updateEffect(in_file1, out_file1)
updateEffect(in_file2, out_file2)
updateEffect(in_file3, out_file3)
updateEffect(in_file4, out_file4)
updateEffect(in_file5, out_file5)



