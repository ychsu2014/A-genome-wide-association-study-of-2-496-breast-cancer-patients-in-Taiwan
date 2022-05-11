input_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData_logistic_assoc.assoc.logistic"
input_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData_logistic_assoc.assoc.logistic"
input_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_logistic_assoc.assoc.logistic"
input_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_logistic_assoc.assoc.logistic"
input_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_logistic_assoc.assoc.logistic"
input_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_logistic_assoc.assoc.logistic"


def checkNA(inFile):
    f = open(inFile)
    lines = f.readlines()
    NA_count = 0
    for line in lines:
        nline = line.strip("\n")
        while "  " in nline:
            nline = nline.replace("  ", " ")
        cols = nline.split(" ")
        if cols[8] == "NA":
            NA_count += 1
    print(inFile)
    print("line num of the file: " + str(len(lines)))
    print("NA num: " + str(NA_count))
    f.close()

checkNA(input_file1)
checkNA(input_file2)
checkNA(input_file3)
checkNA(input_file4)
checkNA(input_file5)
checkNA(input_file6)
