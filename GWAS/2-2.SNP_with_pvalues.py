input_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_logistic.assoc.logistic"
out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_keepFinalBCControls_updateSex_logistic_sigPvalues.txt"

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

SNPwithSigPvalues(input_file, out_file)
