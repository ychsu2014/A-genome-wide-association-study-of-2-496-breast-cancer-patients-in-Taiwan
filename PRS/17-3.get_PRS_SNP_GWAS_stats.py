in_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS_SNP_list.txt"
in_file12 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updatedSex_v2_baseData_logistic_assoc.assoc.logistic"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS_SNP_list_GWAS_stats.txt"

in_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_PRS_SNP_list.txt"
in_file22 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/impute2_keepFinalBC65yoControls_updatedSex_v2_baseData_logistic_assoc.assoc.logistic"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_PRS_SNP_list_GWAS_stats.txt"

in_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_PRS_SNP_list.txt"
in_file32 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalA_baseData_logistic_assoc.assoc.logistic"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_PRS_SNP_list_GWAS_stats.txt"

in_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_PRS_SNP_list.txt"
in_file42 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_luminalB_baseData_logistic_assoc.assoc.logistic"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_PRS_SNP_list_GWAS_stats.txt"

in_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_PRS_SNP_list.txt"
in_file52 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_basal_baseData_logistic_assoc.assoc.logistic"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_PRS_SNP_list_GWAS_stats.txt"

in_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_PRS_SNP_list.txt"
in_file62 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/impute2_keepFinalBCControls_updatedSex_v2_her2_baseData_logistic_assoc.assoc.logistic"
out_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_PRS_SNP_list_GWAS_stats.txt"

def getGWASStats(inFile1, inFile2, outFile):
    f1 = open(inFile1)
    f2 = open(inFile2)
    fout = open(outFile, "w")
    # PRS SNP list
    lines1 = f1.readlines()
    inHeader1 = lines1[0]
    lines1 = lines1[1:]
    # GWAS results
    lines2 = f2.readlines()
    inHeader2 = lines2[0]
    print(inHeader2)
    while "  " in inHeader2:
        inHeader2 = inHeader2.replace("  ", " ")
    head_cols = inHeader2.strip("\n").strip(" ").split(" ")
    newH2 = "\t".join(head_cols[3:])
    lines2 = lines2[1:]
    outHeader = inHeader1.strip("\n") + "\t" + newH2 + "\n"
    print(outHeader)
    fout.write(outHeader)
    # GWAS dict
    # key: SNP_ID, value: line_needed
    GWASDict = {}
    for line in lines2:
        while "  " in line:
            line = line.replace("  ", " ")
        cols = line.strip("\n").strip(" ").split(" ")
        SNP_ID = cols[1]
        new_line = "\t".join(cols[3:])
        GWASDict[SNP_ID] = new_line
    # loop through the PRS SNP list
    for line in lines1:
        cols = line.strip("\n").split("\t")
        SNP_ID = cols[1]
        GWAS_line = GWASDict[SNP_ID]
        fout.write("\t".join(cols) + "\t" + GWAS_line + "\n")
    f1.close()
    f2.close()
    fout.close()

getGWASStats(in_file1, in_file12, out_file1)
print(out_file1)

getGWASStats(in_file2, in_file22, out_file2)
print(out_file2)

getGWASStats(in_file3, in_file32, out_file3)
print(out_file3)

getGWASStats(in_file4, in_file42, out_file4)
print(out_file4)

getGWASStats(in_file5, in_file52, out_file5)
print(out_file5)

getGWASStats(in_file6, in_file62, out_file6)
print(out_file6)
