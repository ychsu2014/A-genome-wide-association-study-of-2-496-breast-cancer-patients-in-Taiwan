in_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS_result_v2.snp"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS_SNP_list.txt"
in_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_PRS_result_v2.snp"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/yo65Control_PRS_SNP_list.txt"
in_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_PRS_result_v2.snp"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalA_PRS_SNP_list.txt"
in_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_PRS_result_v2.snp"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/luminalB_PRS_SNP_list.txt"
in_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_PRS_result_v2.snp"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/basal_PRS_SNP_list.txt"
in_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_PRS_result_v2.snp"
out_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/her2_PRS_SNP_list.txt"

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

# BC vs. age-matched controls
getSNPList(in_file1, out_file1, 0.00000005)
# BC vs. 65yo controls
getSNPList(in_file2, out_file2, 0.00220005)
# luminal A BC
getSNPList(in_file3, out_file3, 0.00000005)
# luminal B BC
getSNPList(in_file4, out_file4, 0.00030005)
# basal-like BC
getSNPList(in_file5, out_file5, 0.00470005)
# her2-enriched BC
getSNPList(in_file6, out_file6, 0.0121501)
