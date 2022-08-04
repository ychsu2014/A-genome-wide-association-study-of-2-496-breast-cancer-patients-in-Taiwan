in_file = "/home/iHiO10009/Dataset/other_data/clean.subjects_2NTU.csv"
out_file = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/clean_subjects_for_keep.txt"

f = open(in_file)
fout = open(out_file, "w")

lines = f.readlines()
lines = lines[1:]
for line in lines:
    ID = line.replace('"','').strip("\n")
    fout.write(ID + "\t" + ID + "\n")

f.close()
fout.close()
