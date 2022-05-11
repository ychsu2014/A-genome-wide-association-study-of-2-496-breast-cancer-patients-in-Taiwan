in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_control_age_gender.txt"
in_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_PRS_result.best"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_PRS_score.txt"
in_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS_result.best"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS_score.txt"
in_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_PRS_result.best"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_PRS_score.txt"
in_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_PRS_result.best"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_PRS_score.txt"
in_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_PRS_result.best"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_PRS_score.txt"
in_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_PRS_result.best"
out_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_PRS_score.txt"

# BC list
f_bc = open(in_bc)
bc_list = []
for line in f_bc:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    bc_list.append(sID)

# Control list
f_control = open(in_control)
control_list = []
for line in f_control:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    control_list.append(sID)

def outputPRSresults(inFile, outFile, bcList = bc_list, conList = control_list):
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    lines = lines[1:]
    for line in lines:
        cols = line.strip("\n").split(" ")
        sID = cols[0]
        PRS = cols[3]
        if sID in bcList:
            fout.write("BC\t" + PRS + "\n")
        elif sID in conList:
            fout.write("Control\t" + PRS + "\n")
    f.close()
    fout.close()

outputPRSresults(in_file1, out_file1)
outputPRSresults(in_file2, out_file2)
outputPRSresults(in_file3, out_file3)
outputPRSresults(in_file4, out_file4)
outputPRSresults(in_file5, out_file5)
outputPRSresults(in_file6, out_file6)

