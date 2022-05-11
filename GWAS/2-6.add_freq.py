in_all_freq = "/home/iHiO10009/Dataset/IMPUTE2_Genotyping_deID_release_20210823/plink.frq"
in_BC_freq = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_v2_freq.frq"
in_BC_65_freq = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_v2_freq.frq"
#in_BC = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_sigPvalues_annotated_v2.txt"
in_BC65 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_sigPvalues_annotated_v2.txt"
##out_BC = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBCControls_updatedSex_logistic_sigPvalues_annotated_maf_v2.txt"
out_BC65 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/impute2_keepFinalBC65yoControls_updatedSex_logistic_sigPvalues_annotated_maf_v2.txt"

# parse frequency file to dict
# key: snp_id, value: maf
def parseToDict(inFile):
    f = open(inFile)
    lines = f.readlines()
    outDict = {}
    for line in lines:
        while "  " in line:
            line = line.replace("  ", " ")
        line = line.strip("\n").strip(" ")
        cols = line.split(" ")
        snp_id = cols[1]
        allele = cols[2]
        maf = cols[4]
        outDict[snp_id] = [allele, maf]
    f.close()
    return(outDict)

# add frequency to the end of the annotation file, and output a new file
def addFreqToFile(inAllFreq, inBCFreq, inBC, outFile):
    all_freq_dict = parseToDict(inAllFreq)
    bc_freq_dict = parseToDict(inBCFreq)
    f_bc = open(inBC)
    fout = open(outFile, "w")
    lines = f_bc.readlines()
    print(len(lines))
    count = 0
    for line in lines:
        count += 1
        if count % 10 ==0:
            print(count)
        cols = line.strip("\n").split("\t")
        snp_id = cols[1]
        if snp_id in all_freq_dict.keys():
            [allele, maf] = all_freq_dict[snp_id]
            new_line = line.strip("\n") + "\t" + allele + "\t" + maf + "\t"
        else:
            print(snp_id)
            print("Please check.")
            new_line = line.strip("\n") + "\t\t\t"
        if snp_id in bc_freq_dict.keys():
            [allele, maf] = bc_freq_dict[snp_id]
            new_line = new_line + allele + "\t" + maf + "\n"
            fout.write(new_line)
        else:
            print(snp_id)
            print("Please check.")
            new_line = new_line + "\t\n"
            fout.write(new_line)
    f_bc.close()
    fout.close()

#addFreqToFile(in_all_freq, in_BC_freq, in_BC, out_BC)
addFreqToFile(in_all_freq, in_BC_65_freq, in_BC65, out_BC65)
