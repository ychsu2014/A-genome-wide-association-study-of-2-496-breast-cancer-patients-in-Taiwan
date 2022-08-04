in_file = "/home/iHiO10009/Dataset/data/BC_2648_deID.csv"
in_BC1 = "/home/iHiO10009/Dataset/data/BC_Diag_4252_deID.csv"
in_BC2 = "/home/iHiO10009/Dataset/data/BC_Majorillness_3938_deID.csv"
out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/BC_toBeRemove_list.txt"

f = open(in_file)
lines = f.readlines()
lines = lines[1:]
list_2648 = []
for line in lines:
    cols = line.replace('"', '').split(" ")
    ID = cols[0]
    list_2648.append(ID)
f.close()

f_bc1 = open(in_BC1)
lines = f_bc1.readlines()
lines = lines[1:]
BC_IDs = []
BC_1_list = []
for line in lines:
    cols = line.strip("\n").split(",")
    ID = cols[0]
    BC_IDs.append(ID)
    BC_1_list.append(ID)
f_bc1.close()

f_bc2 = open(in_BC2)
lines = f_bc2.readlines()
lines = lines[1:]
BC_2_list = []
for line in lines:
    cols = line.strip("\n").split(",")
    ID = cols[0]
    BC_IDs.append(ID)
    BC_2_list.append(ID)
f_bc2.close()

print(len(set(BC_1_list)))
print(len(set(BC_2_list)))
print(len(set(BC_1_list)-set(BC_2_list)))
print(len(set(BC_2_list)-set(BC_1_list)))

ID_to_remove = list(set(BC_IDs) - set(list_2648))
print(len(set(list_2648)-set(BC_IDs)))
print(len(set(list_2648)-set(BC_1_list)))
print(len(set(list_2648)-set(BC_2_list)))
print(len(set(list_2648)&set(BC_1_list)&set(BC_2_list)))
print(len(ID_to_remove))

fout = open(out_file, "w")
for i in ID_to_remove:
    fout.write(i + "\t" + i + "\n")
fout.close()
