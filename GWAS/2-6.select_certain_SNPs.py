# keep only significantly associated SNPs identified in GWAS
in_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_logistic_sigPvalues.txt"
infrq1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyCase_freq.frq"
outfrq1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/BC_onlyCase_freq_selected.txt"
infrq2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyControl_freq.frq"
outfrq2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/BC_onlyControl_freq_selected.txt"
infrq3 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyCase_freq_count.frq.counts"
outfrq3 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/BC_onlyCase_freq_count_selected.txt"
infrq4 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_onlyControl_freq_count.frq.counts"
outfrq4 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/BC_onlyControl_freq_count_selected.txt"

file_list = [[infrq1, outfrq1], [infrq2, outfrq2], [infrq3, outfrq3], [infrq4, outfrq4]]

f = open(in_file)
lines = f.readlines()
SNP_ID_list = []
for line in lines:
    cols = line.strip("\n").split("\t")
    SNP_ID = cols[1]
    SNP_ID_list.append(SNP_ID)

def frqWrite(inFile, outFile):
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    header = lines[0]
    fout.write(header)
    lines = lines[1:]
    out_dict = {}
    for line in lines:
        while "  " in line:
            line = line.replace("  ", " ")
        cols = line.strip("\n").strip(" ").split(" ")
        SNP_ID = cols[1]
        if SNP_ID in SNP_ID_list:
            fout.write(line)
    f.close()
    fout.close()

for file_pair in file_list:
    frqWrite(file_pair[0], file_pair[1])

f.close()
