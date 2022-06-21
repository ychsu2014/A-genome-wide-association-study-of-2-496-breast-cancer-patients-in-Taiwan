#FID     IID     Disease age     gender  pc1     pc2     pc3     pc4     pc5     pc6     pc7     pc8     pc9     pc10
in_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list_forKeepCmd.txt"
in_pca2 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/impute2_keepFinalBCControls_updateSex_baseData_forPCA.eigenvec"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_pheCov_file.txt"

in_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_base_list_forKeepCmd.txt"
in_pca3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalA_baseData_forPCA.eigenvec"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_pheCov_file.txt"

in_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_base_list_forKeepCmd.txt"
in_pca4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_luminalB_baseData_forPCA.eigenvec"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_pheCov_file.txt"

in_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_base_list_forKeepCmd.txt"
in_pca5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_basal_baseData_forPCA.eigenvec"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_pheCov_file.txt"

in_file6 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_base_list_forKeepCmd.txt"
in_pca6 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/impute2_keepFinalBCControls_updateSex_her2_baseData_forPCA.eigenvec"
out_file6 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_pheCov_file.txt"

# 1 = unaffected (control), 2 = affected (case)
def write_to_file(inID, inStatus, inAge, inGender, inDict, inFile):
    pca_list = inDict[inID]
    inFile.write(inID + "\t" + inID + "\t" + inStatus + "\t" + inAge + "\t" + inGender)
    for i in pca_list:
        inFile.write("\t" + i)
    inFile.write("\n")

def makePheCovFile(inFile, inPCA, outFile):
    f = open(inFile)
    f_pca = open(inPCA)
    fout = open(outFile, "w")
    fout.write("FID\tIID\tDisease\tage\tgender\tpc1\tpc2\tpc3\tpc4\tpc5\tpc6\tpc7\tpc8\tpc9\tpc10\n")
    lines = f_pca.readlines()
    # PCA dict
    pca_dict = {}
    for line in lines:
        while "  " in line:
            line = line.replace("  ", " ")
        cols = line.strip("\n").strip(" ").split(" ")
        sID = cols[0]
        pc1 = cols[2]
        pc2 = cols[3]
        pc3 = cols[4]
        pc4 = cols[5]
        pc5 = cols[6]
        pc6 = cols[7]
        pc7 = cols[8]
        pc8 = cols[9]
        pc9 = cols[10]
        pc10 = cols[11]
        pca_dict[sID] = [pc1, pc2, pc3, pc4, pc5, pc6, pc7, pc8, pc9, pc10]
    # write to file
    lines = f.readlines()
    for line in lines:
        cols = line.strip("\n").split("\t")
        sID = cols[0]
        age = cols[len(cols)-2]
        gender = cols[len(cols)-1]
        #Case/control phenotypes are expected to be encoded as 1=unaffected (control), 2=affected (case); 0 is accepted as an alternate missing value encoding.
        if len(cols) > 6:
            write_to_file(sID, "2", age, gender, pca_dict, fout)
        else:
            write_to_file(sID, "1", age, gender, pca_dict, fout)
    f.close()
    f_pca.close()
    fout.close()

makePheCovFile(in_file2, in_pca2, out_file2)
makePheCovFile(in_file3, in_pca3, out_file3)
makePheCovFile(in_file4, in_pca4, out_file4)
makePheCovFile(in_file5, in_pca5, out_file5)
makePheCovFile(in_file6, in_pca6, out_file6)
