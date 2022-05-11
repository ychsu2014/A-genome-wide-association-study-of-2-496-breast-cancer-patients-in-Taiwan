input_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_assoc_v2.assoc.logistic"
input_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_assoc_v2.assoc.logistic"
input_file3 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_assoc_noPara1_v2.assoc.logistic"
input_file4 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_assoc_noPara1_v2.assoc.logistic"


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
