in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_control_age_gender.txt"

input_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keepMultipleControls_v2.genome"
out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_BC_multipleControls_IBD_removal_list_v2.txt"

#input_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_v2.genome"
#out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_BC_65yoControls_IBD_removal_list_v2.txt"

f = open(input_file)
f_bc = open(in_bc)
f_control = open(in_control)
fout = open(out_file, "w")

# BC list
lines = f_bc.readlines()
bc_list = []
for line in lines:
    cols = line.strip("\n").split("\t")
    bc_list.append(cols[0])

# control list
lines = f_control.readlines()
c_list = []
for line in lines:
    cols = line.strip("\n").split("\t")
    c_list.append(cols[0])

# control/case: control first
# both case: write to the other file for further check
# both control: randomly pick one
count = 0
for line in f:
    count += 1
    if count == 1:
        continue
    while "  " in line:
        line = line.replace("  ", " ")
    cols = line.strip("\n").strip(" ").split(" ")
    sID1 = cols[0]
    sID2 = cols[2]
    IBD_score = cols[9]
    if float(IBD_score) > 0.1875:
        if sID1 in c_list and sID2 in c_list:
            fout.write("\t".join([sID1, sID1, sID2, sID2, IBD_score, "control", "control"]) + "\n")
        elif sID1 in c_list and sID2 in bc_list:
            fout.write("\t".join([sID1, sID1, sID2, sID2, IBD_score, "control", "BC"]) + "\n")
        elif sID1 in bc_list and sID2 in c_list:
            fout.write("\t".join([sID2, sID2, sID1, sID1, IBD_score, "control", "BC"]) + "\n")
        elif sID1 in bc_list and sID2 in bc_list:
            fout.write("\t".join([sID1, sID1, sID2, sID2, IBD_score, "BC", "BC"]) + "\n")

f.close()
f_bc.close()
f_control.close()
fout.close()
