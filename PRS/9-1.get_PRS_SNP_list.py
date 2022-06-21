in_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_PRS_result.snp"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_PRS_SNP_list.txt"
in_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_PRS_result.snp"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_PRS_SNP_list.txt"
in_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_PRS_result.snp"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_PRS_SNP_list.txt"
in_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_PRS_result.snp"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_PRS_SNP_list.txt"
in_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_PRS_result.snp"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_PRS_SNP_list.txt"

def getSNPList(inFile, outFile, threshold):
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    # header
    fout.write(lines[0])
    lines = lines[1:]
    for line in lines:
        cols = line.strip("\n").split("\t")
        P = float(cols[3])
        if P < threshold:
            fout.write(line)
    f.close()
    fout.close()

getSNPList(in_file1, out_file1, 0.00000005)
getSNPList(in_file2, out_file2, 0.00000005)
getSNPList(in_file3, out_file3, 0.00030005)
getSNPList(in_file4, out_file4, 0.00020005)
getSNPList(in_file5, out_file5, 0.00605005)
