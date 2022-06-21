in_path = "/home/iHiO10009/yuching/data/2.PRS_v2"
in_folder = ["case_ageMatchControl_PRS", "subtype_PRS"]

import os

for afolder in in_folder:
    f_path = in_path + "/" + afolder
    files = os.listdir(f_path)
    for afile in files:
        if "SNP_list" in afile:
            out_file = afile.split("_")[0] + "_SNP_list_forExtractCmd.txt"
            f = open(f_path + "/" + afile)
            fout = open(f_path + "/" + out_file, "w")
            lines = f.readlines()
            lines = lines[1:]
            for line in lines:
                cols = line.strip("\n").split("\t")
                SNP_ID = cols[1]
                fout.write(SNP_ID + "\n")
            print(out_file)
            f.close()
            fout.close()

