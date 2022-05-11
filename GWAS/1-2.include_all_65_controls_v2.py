in_fam = "/home/iHiO10009/yuching/data/1.QC/impute2_keepCleanSbj.fam"
in_bc = "/home/iHiO10009/yuching/data/1.QC/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC/all_control_age_gender.txt"
out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/case_65yo_control_list_forKeepCommand_v2.txt"

from random import randrange

f_fam = open(in_fam)
f_bc = open(in_bc)
f_control = open(in_control)
fout = open(out_file, "w")

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
    age = int(cols[1])
    gender = cols[2]
    if gender == "2":
        if age not in BC_control_dict.keys():
            BC_control_dict[age] = [(sID, gender)]
        else:
            old_list = BC_control_dict[age]
            old_list.append((sID, gender))
            BC_control_dict[age] = old_list

test_count = 0
for i in range(65, max(BC_control_dict.keys())):
    if i in BC_control_dict.keys():
        test_count += len(BC_control_dict[i])

print(test_count)

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
    fout.write(sID + "\t" + sID + "\t" + age + "\t" + gender + "\n")

# control
#control_num = count * 10
c_count = 0
#while control_num > 0:
for c_age in range(65, max(BC_control_dict.keys())):
    if c_age in BC_control_dict.keys():
        sID_list = BC_control_dict[c_age]
        for control in sID_list:
            c_sID = control[0]
            c_gender = control[1]
            fout.write(c_sID + "\t" + c_sID + "\t" + str(c_age) + "\t" + c_gender + "\n")
            c_count += 1
            if c_count % 10000 == 0:
                print(c_count)
#        control_num = control_num - 1
    else:
        continue

print(c_count)


f_fam.close()
f_bc.close()
f_control.close()
fout.close()
