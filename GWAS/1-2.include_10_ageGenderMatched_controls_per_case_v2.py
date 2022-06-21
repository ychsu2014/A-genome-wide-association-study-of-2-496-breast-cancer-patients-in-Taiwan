in_fam = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/impute2_remove1785_keepClean.fam"
in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_age_gender.txt"
out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/case_10Control_list.txt"
out_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/case_10Control_list_forKeepCommand.txt"

f_fam = open(in_fam)
f_bc = open(in_bc)
f_control = open(in_control)
fout = open(out_file, "w")
fout2 = open(out_file2, "w")

clean_sbj_list = []
# clean subject list
lines = f_fam.readlines()
for line in lines:
    cols = line.strip("\n").split(" ")
    sID = cols[0]
    clean_sbj_list.append(sID)

# control dict
lines = f_control.readlines()
BC_control_dict = {}
for line in lines:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    if age not in BC_control_dict.keys():
        BC_control_dict[age] = [(sID, gender)]
    else:
        old_list = BC_control_dict[age]
        old_list.append((sID, gender))
        BC_control_dict[age] = old_list

def writeControlList(inDict, inFile1, inFile2, inAge, inGender):
    if inAge in inDict.keys():
        controlList = inDict[inAge]
        controlList2 = []
        c_count = 0
        for control in controlList:
            gender = control[1]
            if gender == inGender and c_count < 10:
                controlList2.append(control)
                c_count += 1
        for control in controlList2:
            sID = control[0]
            gender = control[1]
            inFile1.write(sID + "\t" + inAge + "\t" + gender + "\t")
            inFile2.write(sID + "\t" + sID + "\t" + inAge + "\t" + gender + "\n")
            controlList.remove(control)
        if controlList != []:
            inDict[inAge] = controlList
        else:
            inDict.pop(inAge)
    return(inDict)

# breast cancer
lines = f_bc.readlines()
print(len(lines))
count = 0
for line in lines:
    count += 1
    if count % 1000 == 0:
        print(count)
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    fout.write(sID + "\t" + age + "\t" + gender + "\t")
    fout2.write(sID + "\t" + sID + "\t" + age + "\t" + gender + "\n")
    BC_control_dict = writeControlList(BC_control_dict, fout, fout2, age, gender)
    # include age +/- 3
    # checked data after running this code, all case/control are age-matched.
    # codes below are not really used.
    age_bias = 1
    age = int(age)
    age_biased = age + age_bias
    #BC_control_dict = writeControlList(BC_control_dict, fout, str(age_biased))
    while age_bias <= 3:
        if (age_biased - age) > 0:
            age_biased = age - age_bias
            #BC_control_dict = writeControlList(BC_control_dict, fout, str(age_biased))
            age_bias = age_bias + 1
        elif (age_biased - age) < 0:
            age_biased = age + age_bias
            #BC_control_dict = writeControlList(BC_control_dict, fout, str(age_biased))
        else:
            print("Something wrong. Please check.")
    fout.write("\n")

f_fam.close()
f_bc.close()
f_control.close()
fout.close()
fout2.close()
