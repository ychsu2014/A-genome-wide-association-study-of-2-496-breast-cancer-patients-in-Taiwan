in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_control_age_gender.txt"

in_fam = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/BDC_210820_removeConSNP_auto_keep65yoControls_removeIBD_v2.fam"
in_impute2_fam = "/home/iHiO10009/yuching/data/1.QC/impute2_keepCleanSbj.fam"
out_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_list_v2.txt"
out_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_list_forKeepCmd_v2.txt"

import random

f_fam = open(in_fam)
f_bc = open(in_bc)
f_control = open(in_control)
f_impute2_fam = open(in_impute2_fam)
fout1 = open(out_file1, "w")
fout2 = open(out_file2, "w")

# clean patient list
clean_patient_list = []
lines = f_impute2_fam.readlines()
for line in lines:
    cols = line.strip("\n").split(" ")
    sID = cols[0]
    clean_patient_list.append(sID)

print(len(clean_patient_list))

# bc dict: key = sID, value = (age, gender)
lines = f_bc.readlines()
bc_dict = {}
for line in lines:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    bc_dict[sID] = (age, gender)

print(len(bc_dict.keys()))

# control dict: key = sID, value = (age, gender)
lines = f_control.readlines()
control_dict = {}
for line in lines:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    control_dict[sID] = (age, gender)

# samples remained
lines = f_fam.readlines()
print("fam line num: " + str(len(lines)))
bc_re_dict = {}     # key: sID, value = (age, gender)
#con_re_list = []    # [[sID, age, gender], [sID, age, gender], ...]
con_re_dict = {}    # key: gender, value" [[sID, age], [sID, age], ...]
total_control_count = 0
total_bc_count = 0
for line in lines:
    cols = line.strip("\n").split(" ")
    sID = cols[0]
    if sID in bc_dict.keys():
        total_bc_count += 1
    if sID in bc_dict.keys() and sID in clean_patient_list:
        bc_re_dict[sID] = bc_dict[sID]
    elif sID in control_dict.keys() and sID in clean_patient_list:
        total_control_count += 1
        (age, gender) = control_dict[sID]
        if gender in con_re_dict.keys():
            old_list = con_re_dict[gender]
            old_list.append([sID, age])
            con_re_dict[gender] = old_list
        else:
            con_re_dict[gender] = [[sID, age]]

print("total bc remained: " + str(len(bc_re_dict.keys())))
#print("total controls remained: " + str(len(con_re_list)))

# write bc records
# randomly select 65 y/o controls
count = 0
for sID in bc_re_dict.keys():
    count += 1
    (age, gender) = bc_re_dict[sID]
    fout1.write("\t".join([sID, age, gender]))
    fout2.write(sID + "\t" + sID + "\t" + age + "\t" + gender + "\n")
    con_re_list = con_re_dict[gender]
    for i in range(4):
        idx = random.randint(0, len(con_re_list)-1)
        con_temp = con_re_list[idx]
        [c_sID, c_age] = con_temp
        c_gender = gender
        fout1.write("\t" + c_sID + "\t" + c_age + "\t" + c_gender)
        fout2.write(c_sID + "\t" + c_sID + "\t" + c_age + "\t" + c_gender + "\n")
        con_re_list.remove(con_temp)
    con_re_dict[gender] = con_re_list
    fout1.write("\n")

f_fam.close()
f_bc.close()
f_control.close()
fout1.close()
fout2.close()
