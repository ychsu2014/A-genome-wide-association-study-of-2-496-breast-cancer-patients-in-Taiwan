in_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_list.txt"
in_pca = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_pca.eigenvec"
out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_pheCov_file.txt"

f = open(in_file)
f_pca = open(in_pca)
fout = open(out_file, "w")

fout.write("FID\tIID\tDisease\tage\tgender\tpc1\tpc2\tpc3\tpc4\tpc5\tpc6\tpc7\tpc8\tpc9\tpc10\n")

lines = f_pca.readlines()

# PCA dict
pca_dict = {}
for line in lines:
    cols = line.strip("\n").split(" ")
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

# 1 = unaffected (control), 2 = affected (case)
def write_to_file(inID, inStatus, inAge, inGender, inDict, inFile):
    pca_list = inDict[inID]
    inFile.write(inID + "\t" + inID + "\t" + inStatus + "\t" + inAge + "\t" + inGender)
    for i in pca_list:
        inFile.write("\t" + i)
    inFile.write("\n")

# write to file
lines = f.readlines()
for line in lines:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    c_sID1 = cols[3]
    c_age1 = cols[4]
    c_gender1 = cols[5]
    c_sID2 = cols[6]
    c_age2 = cols[7]
    c_gender2 = cols[8]
    c_sID3 = cols[9]
    c_age3 = cols[10]
    c_gender3 = cols[11]
    c_sID4 = cols[12]
    c_age4 = cols[13]
    c_gender4 = cols[14]
    #Case/control phenotypes are expected to be encoded as 1=unaffected (control), 2=affected (case); 0 is accepted as an alternate missing value encoding.
    write_to_file(sID, "2", age, gender, pca_dict, fout)
    write_to_file(c_sID1, "1", c_age1, c_gender1, pca_dict, fout)
    write_to_file(c_sID2, "1", c_age2, c_gender2, pca_dict, fout)
    write_to_file(c_sID3, "1", c_age3, c_gender3, pca_dict, fout)
    write_to_file(c_sID4, "1", c_age4, c_gender4, pca_dict, fout)

f.close()
f_pca.close()
fout.close()
