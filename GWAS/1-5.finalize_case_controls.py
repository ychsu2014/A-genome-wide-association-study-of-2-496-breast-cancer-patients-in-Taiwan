in_fam = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/BDC_removeIBD.fam"
in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_age_gender.txt"
out_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_list.txt"
out_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_list_forKeepCmd.txt"

in_impute2_fam = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_remove1785_keepClean.fam"


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
con_re_dict = {}    # key: age, value = [(sID, gender)]
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
        if (age,gender) in con_re_dict.keys():
            old_list = con_re_dict[(age, gender)]
            old_list.append(sID)
            con_re_dict[(age,gender)] = old_list
        else:
            con_re_dict[(age,gender)] = [sID]
    #else:
        #print("Something Wrong. Please check.")

print("bc count without filtering clean patient: " + str(total_bc_count))
print("bc count with filtering clean patient: " + str(len(bc_re_dict.keys())))
print(total_control_count)

def ageBiasedControls(inDict, inKey, inNum, inFile1, inFile2):
    if inKey in inDict.keys():
        allControls = inDict[inKey]
        comControls = allControls[:inNum]
        inNum = inNum - len(comControls)
        cage = inKey[0]
        cgender = inKey[1]
        for control in comControls:
            csID = control
            inFile1.write(csID + "\t" + cage + "\t" + cgender + "\t")
            inFile2.write(csID + "\t" + csID + "\t" + cage + "\t" + cgender + "\n")
            allControls.remove(control)
        inDict[inKey] = allControls
    return([inDict, inNum])

# select matched controls
# after running this script, checked the output file. All case/control are age-matched.
count = 0
for sID in bc_re_dict.keys():
    count += 1
    (age, gender) = bc_re_dict[sID]
    fout1.write("\t".join([sID, age, gender]) + "\t")
    fout2.write(sID + "\t" + sID + "\t" + age + "\t" + gender + "\n")
    qkey = (age, gender)
    if qkey in con_re_dict.keys():
        all_controls = con_re_dict[qkey]
        controls_4 = all_controls[:4]
        lack_num = 4-len(controls_4)
        for control in controls_4:
            c_sID = control
            fout1.write(c_sID + "\t" + age + "\t" + gender + "\t")
            fout2.write(c_sID + "\t" + c_sID + "\t" + age + "\t" + gender + "\n")
            all_controls.remove(control)
        con_re_dict[age] = all_controls
    else:
        lack_num = 4
    age_bias = 1
    age_biased = int(age) + age_bias
    if lack_num > 0:
        #print(lack_num)
        [con_re_dict, lack_num] = ageBiasedControls(con_re_dict, (str(age_biased), gender), lack_num, fout1, fout2)
    while lack_num > 0:
        #print(lack_num)
        if (age_biased - int(age)) > 0:
            age_biased = int(age) - age_bias
            [con_re_dict, lack_num] = ageBiasedControls(con_re_dict, (str(age_biased), gender), lack_num, fout1, fout2)
            age_bias += 1
        elif (age_biased - int(age)) < 0:
            age_biased = int(age) + age_bias
            [con_re_dict, lack_num] = ageBiasedControls(con_re_dict, (str(age_biased), gender), lack_num, fout1, fout2)
        else:
            print("Something wrong. Please check.")
    fout1.write("\n")

print(count)

f_fam.close()
f_bc.close()
f_control.close()
fout1.close()
fout2.close()
