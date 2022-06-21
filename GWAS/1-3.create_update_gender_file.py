in_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_age_gender.txt"
in_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_age_gender.txt"
out_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_updateGender.txt"
out_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_updateGender.txt"

def updateGenderFile(inFile, outFile):
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    for line in lines:
        cols = line.strip("\n").split("\t")
        sID = cols[0]
        gender = cols[2]
        fout.write(sID + "\t" + sID + "\t" + gender + "\n")
    f.close()
    fout.close()

updateGenderFile(in_file1, out_file1)
updateGenderFile(in_file2, out_file2)
