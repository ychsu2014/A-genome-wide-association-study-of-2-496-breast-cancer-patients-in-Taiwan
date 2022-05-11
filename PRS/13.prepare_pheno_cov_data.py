in_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list_forKeepCmd.txt"
out_file1_1 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_pheno_data.txt"
out_file1_2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_cov_data.txt"

in_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_target_sID_list_forKeepCmd.txt"
out_file2_1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_pheno_data.txt"
out_file2_2 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_cov_data.txt"

in_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_target_list_forKeepCmd.txt"
out_file3_1 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_pheno_data.txt"
out_file3_2 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_cov_data.txt"

in_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_target_list_forKeepCmd.txt"
out_file4_1 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_pheno_data.txt"
out_file4_2 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_cov_data.txt"


in_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_target_list_forKeepCmd.txt"
out_file5_1 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_pheno_data.txt"
out_file5_2 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_cov_data.txt"

in_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_target_list_forKeepCmd.txt"
out_file6_1 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_pheno_data.txt"
out_file6_2 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_cov_data.txt"

def createPhenoCovData(inFile, outFile1, outFile2):
    f = open(inFile)
    fout1 = open(outFile1, "w")
    fout2 = open(outFile2, "w")
    fout1.write("FID\tIID\tPhenotype\n")
    fout2.write("FID\tIID\tAge\tGender\n")
    lines = f.readlines()
    for line in lines:
        cols = line.strip("\n").split("\t")
        sID = cols[0]
        group = cols[2]
        age = cols[len(cols)-2]
        gender = cols[len(cols)-1]
        if group == "BC":
            group_index = "1"
        elif group == "Control":
            group_index = "0"
        else:
            print(sID)
        fout1.write(sID + "\t" + sID + "\t" + group_index + "\n")
        fout2.write(sID + "\t" + sID + "\t" + age + "\t" + gender + "\n")
    f.close()
    fout1.close()
    fout2.close()


#createPhenoCovData(in_file1, out_file1_1, out_file1_2)
createPhenoCovData(in_file2, out_file2_1, out_file2_2)
createPhenoCovData(in_file3, out_file3_1, out_file3_2)
createPhenoCovData(in_file4, out_file4_1, out_file4_2)
createPhenoCovData(in_file5, out_file5_1, out_file5_2)
createPhenoCovData(in_file6, out_file6_1, out_file6_2)
