in_file = "/home/iHiO10009/Dataset/data/BC_2648_deID.csv"
in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_control_list_v2.txt"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS/subtypes/BC_subtypes_all_2648.txt"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS/subtypes/BC_subtypes_2516.txt"

import csv

f_bc = open(in_bc)
fout1 = open(out_file1, "w")
fout2 = open(out_file2, "w")

# breast cancer
lines = f_bc.readlines()
sID_2516_dict = {}
age_list = []
for line in lines:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    sID_2516_dict[sID] = (age, gender)
    age_list.append(age)

uni_age_list = list(set(age_list))
uni_age_list.sort()
for i in uni_age_list:
    temp = age_list.count(i)
    print(i + " " + str(temp))

count = 0
lumA_count = 0
lumB_count = 0
basal_like = 0
her2_enriched = 0
NA_count = 0
subtype_2516_list = []
with open(in_file, newline = "\n") as csvfile:
    rows = csv.reader(csvfile, delimiter = " ")
    for row in rows:
        count += 1
        if count > 1:
            sID = row[0]
            ER = row[53]
            PR = row[54]
            her2 = row[59]
            if ER != "NA" and PR != "NA" and her2 != "NA":
                ER = int(ER)
                PR = int(PR)
                her2 = int(her2)
                if ER >= 1 and PR >= 1 and her2 == 0:
                    lumA_count += 1
                    subtype = "Luminal A"
                elif ER >= 1 and PR >= 1 and her2 >= 1:
                    lumB_count += 1
                    subtype = "Luminal B"
                elif ER == 0 and PR == 0 and her2 == 0:
                    basal_like += 1
                    subtype = "Basal-like"
                elif ER == 0 and PR == 0 and her2 >= 1:
                    her2_enriched += 1
                    subtype = "Her2-enriched"
                else:
                    NA_count += 1
                    subtype = "NA"
                fout1.write(sID + "\t" + str(ER) + "\t" + str(PR) + "\t" + str(her2) + "\t" + subtype + "\n")
            else:
                NA_count += 1
                subtype = "NA"
                fout1.write(sID + "\t" + str(ER) + "\t" + str(PR) + "\t" + str(her2) + "\t" + subtype + "\n")
            if sID in sID_2516_dict.keys():
                (age, gender) = sID_2516_dict[sID]
                subtype_2516_list.append(subtype)
                fout2.write("\t".join([sID, age, gender, str(ER), str(PR), str(her2), subtype]) + "\n")

print("luminal A: " + str(lumA_count))
print("luminal B: " + str(lumB_count))
print("basal-like: " + str(basal_like))
print("Her2-enriched: " + str(her2_enriched))
print("NA: " +str(NA_count))

print("luminal A")
print(subtype_2516_list.count("Luminal A"))
print("luminal B")
print(subtype_2516_list.count("Luminal B"))
print("basal-like")
print(subtype_2516_list.count("Basal-like"))
print("Her2-enriched")
print(subtype_2516_list.count("Her2-enriched"))
print("NA")
print(subtype_2516_list.count("NA"))

f_bc.close()
fout1.close()
fout2.close()
