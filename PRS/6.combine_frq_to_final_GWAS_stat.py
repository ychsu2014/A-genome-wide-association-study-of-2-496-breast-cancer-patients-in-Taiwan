in_frq1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_freq.frq"
in_logit1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData_logistic_assoc.assoc.logistic"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_baseData_logistic_addFrq.txt"

in_frq2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_freq.frq"
in_logit2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData_logistic_assoc.assoc.logistic"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_baseData_logistic_addFrq.txt"

in_frq3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_freq.frq"
in_logit3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_logistic_assoc.assoc.logistic"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_luminalA_baseData_logistic_addFrq.txt"

in_frq4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_freq.frq"
in_logit4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_logistic_assoc.assoc.logistic"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_luminalB_baseData_logistic_addFrq.txt"

in_frq5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_freq.frq"
in_logit5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_logistic_assoc.assoc.logistic"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_basal_baseData_logistic_addFrq.txt"

in_frq6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_freq.frq"
in_logit6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_logistic_assoc.assoc.logistic"
out_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_her2_baseData_logistic_addFrq.txt"

def addFreq(inFrq, inLogit, outFile):
    f_frq = open(inFrq)
    f_logit = open(inLogit)
    fout = open(outFile, "w")
    # key: SNP, value: [A2, MAF]
    lines = f_frq.readlines()
    frq_dict = {}
    for line in lines:
        line = line.strip("\n")
        while "  " in line:
            line = line.replace("  ", " ")
        line = line.strip(" ")
        cols = line.split(" ")
        SNP = cols[1]
        A2 = cols[3]
        MAF = cols[4]
        frq_dict[SNP] = [A2, MAF]
    # key: SNP, value = [all cols]
    lines = f_logit.readlines()
    logit_dict = {}
    for line in lines:
        line = line.strip("\n")
        while "  " in line:
            line = line.replace("  ", " ")
        line = line.strip(" ")
        cols = line.split(" ")
        SNP = cols[1]
        [A2, MAF] = frq_dict[SNP]
        cols.insert(4, A2)
        cols.append(MAF)
        fout.write("\t".join(cols) + "\n")
    f_frq.close()
    f_logit.close()
    fout.close()

addFreq(in_frq1, in_logit1, out_file1)
addFreq(in_frq2, in_logit2, out_file2)
addFreq(in_frq3, in_logit3, out_file3)
addFreq(in_frq4, in_logit4, out_file4)
addFreq(in_frq5, in_logit5, out_file5)
addFreq(in_frq6, in_logit6, out_file6)
