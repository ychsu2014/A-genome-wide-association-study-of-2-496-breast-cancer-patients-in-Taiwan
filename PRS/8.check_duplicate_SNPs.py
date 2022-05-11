in_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_baseData_logistic_filterMAF.txt"
in_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_baseData_logistic_filterMAF.txt"
in_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_luminalA_baseData_logistic_filterMAF.txt"
in_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_luminalB_baseData_logistic_filterMAF.txt"
in_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_basal_baseData_logistic_filterMAF.txt"
in_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_her2_baseData_logistic_filterMAF.txt" 

def checkDuplicateSNP(inFile):
    f = open(inFile)
    lines = f.readlines()
    lines = lines[1:]
    SNP_count_dict = {}
    for line in lines:
        cols = line.strip("\n").split("\t")
        SNP_ID = cols[1]
        if SNP_ID not in SNP_count_dict.keys():
            SNP_count_dict[SNP_ID] = 1
        else:
            count = SNP_count_dict[SNP_ID]
            count += 1
            SNP_count_dict[SNP_ID] = count
            print(SNP_ID)
            print(count)

checkDuplicateSNP(in_file1)
checkDuplicateSNP(in_file2)
checkDuplicateSNP(in_file3)
checkDuplicateSNP(in_file4)
checkDuplicateSNP(in_file5)
checkDuplicateSNP(in_file6)
