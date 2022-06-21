input_file = "/home/iHiO10009/Dataset/data/quantitative_traits.csv"
in_BC = "/home/iHiO10009/Dataset/data/BC_2648_deID.csv"
in_rmBC1 = "/home/iHiO10009/Dataset/data/BC_Diag_4252_deID.csv"
in_rmBC2 = "/home/iHiO10009/Dataset/data/BC_Majorillness_3938_deID.csv"
out_file1 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_age_gender.txt"
out_file2 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_age_gender.txt"

f = open(input_file)
f_BC = open(in_BC)
fout1 = open(out_file1, "w")
fout2 = open(out_file2, "w")
f_rmbc1 = open(in_rmBC1)
f_rmbc2 = open(in_rmBC2)

all_bc_list = []
def allBCList(inFile, inList):
    lines = inFile.readlines()
    lines = lines[1:]
    for line in lines:
        cols = line.strip("\n").split(",")
        ID = cols[0]
        inList.append(ID)
    return(inList)

all_bc_list = allBCList(f_rmbc1, all_bc_list)
all_bc_list = allBCList(f_rmbc2, all_bc_list)

lines = f.readlines()
lines = lines[1:]

all_age_gender_dict = {}
for line in lines:
    cols = line.replace('"', '').strip("\n").split(",")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    all_age_gender_dict[sID] = (age, gender)

lines2 = f_BC.readlines()
lines2 = lines2[1:]
BC_list = []
BC_diagAge_dict = {}
for line in lines2:
    cols = line.replace('"', '').strip("\n").split(" ")
    sID = cols[0]
    BC_diagAge_dict[sID] = cols[5]
    BC_list.append(sID)

rm_BC_count = 0
for sID in all_age_gender_dict.keys():
    if sID in BC_list:
        diagAge = BC_diagAge_dict[sID]
        age,gender = all_age_gender_dict[sID]
        if gender != "2":
            print(gender)
        fout1.write(sID + "\t" + diagAge + "\t" + gender + "\n")
    else:
        if sID not in all_bc_list:
            age,gender = all_age_gender_dict[sID]
            fout2.write(sID + "\t" + age + "\t" + gender + "\n")
        else:
            rm_BC_count += 1
            #print(sID + "is breast cancer. Remove from control list.")

print(rm_BC_count)

f.close()
f_BC.close()
fout1.close()
fout2.close()

