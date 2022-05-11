input_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_assoc_v2.assoc.logistic"
input_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_assoc_v2.assoc.logistic"
out_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_sigPvalues_v2.txt"
out_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_sigPvalues_v2.txt"

def SNPwithSigPvalues(inFile, outFile):
    threshold = 0.00000005
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    lines = lines[1:]
    for line in lines:
        while "  " in line:
            line = line.replace("  ", " ")
        cols = line.strip("\n").strip(" ").split(" ")
        pvalues = cols[11]
        if pvalues != "NA":
            if float(pvalues) < threshold:
                fout.write("\t".join(cols) + "\n")
    f.close()
    fout.close()

SNPwithSigPvalues(input_file1, out_file1)
SNPwithSigPvalues(input_file2, out_file2)
