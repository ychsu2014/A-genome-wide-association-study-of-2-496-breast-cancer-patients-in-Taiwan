in_vcf_path = "/home/iHiO10009/yuching/data/dbSNP"

import vcf

# list of chrom_pos  ex. NC_000001_pos
def dbSNPAnno(inFile, inVcfPath, outFile):
    print(inFile)
    f = open(inFile)
    fout = open(outFile, "w")
    lines = f.readlines()
    lines = lines[1:]
    chrPosDict = {}
    chromList = []
    for line in lines:
        cols = line.strip("\n").split("\t")
        chrom = cols[0]
        if len(chrom) == 1:
            chrom = "NC_00000" + chrom
        elif len(chrom) == 2:
            chrom = "NC_0000" + chrom
        else:
            print(chrom)
            print("Please check if the chrom is right.")
        chromList.append(chrom)
        pos = cols[2]
        temp = chrom + "_" + pos
        chrPosDict[temp] = line.strip("\n")
    chromList = list(set(chromList))
    # chrom = NC_0000xx or NC_00000x
    for chrom in chromList:
        print(chrom)
        vcf_reader = vcf.Reader(open(inVcfPath + "/" + chrom + ".vcf"))
        count = 0
        for record in vcf_reader:
            count += 1
            if count % 5000000 ==0:
                print(count)
            chrom = record.CHROM.split(".")[0]
            pos = str(record.POS)
            vcf_temp = chrom + "_" + pos
            if vcf_temp in chrPosDict.keys():
                old_line = chrPosDict[vcf_temp]
                alt_str_list = []
                for alt_temp in record.ALT:
                    alt_str_list.append(str(alt_temp))
                fout.write(old_line + "\t" + chrom + "\t" + pos + "\t" + str(record.ID) + "\t" + str(record.REF) + "\t" + ",".join(alt_str_list) + "\t")
                if "GENEINFO" in record.INFO.keys():
                    fout.write(record.INFO["GENEINFO"] + "\t")
                else:
                    fout.write("\t")
                if "PSEUDOGENEINFO" in record.INFO.keys():
                    fout.write(record.INFO["PSEUDOGENEINFO"] + "\t")
                else:
                    fout.write("\t")
                if "CLNSIG" in record.INFO.keys():
                    cln_str_list = []
                    for cln_temp in record.INFO["CLNSIG"]:
                        cln_str_list.append(str(cln_temp))
                    fout.write(",".join(cln_str_list) + "\n")
                else:
                    fout.write("\n")
    fout.close()
    f.close()


in_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_PRS_SNP_list.txt"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/ageMatch_PRS_SNP_list_anno.txt"

in_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_PRS_SNP_list.txt"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_PRS_SNP_list_anno.txt"

in_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_PRS_SNP_list.txt"
out_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_PRS_SNP_list_anno.txt"

in_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_PRS_SNP_list.txt"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_PRS_SNP_list_anno.txt"

in_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_PRS_SNP_list.txt"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_PRS_SNP_list_anno.txt"

dbSNPAnno(in_file1, in_vcf_path , out_file1) 
print(out_file1 + " done.")
dbSNPAnno(in_file2, in_vcf_path , out_file2)
print(out_file2 + " done.")
dbSNPAnno(in_file3, in_vcf_path , out_file3)
print(out_file3 + " done.")
dbSNPAnno(in_file4, in_vcf_path , out_file4)
print(out_file4 + " done.")
dbSNPAnno(in_file5, in_vcf_path , out_file5)
print(out_file5 + " done.")
