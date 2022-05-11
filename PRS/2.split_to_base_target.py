in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_control_list_v2.txt"
in_bc_65 = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/final_BC_65yocontrol_list_v2.txt"
in_subtypes = "/home/iHiO10009/yuching/data/2.PRS/subtypes/BC_subtypes_2516.txt"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list.txt"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list.txt" 
out_file3 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_base_sID_list.txt"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_target_sID_list.txt"
out_file5 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_forKeepCmd.txt"
out_file6 = "/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_target_sID_list_forKeepCmd.txt"

out_file7 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list_forKeepCmd.txt"
out_file8 = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list_forKeepCmd.txt"
out_file9 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_base_sID_list_forKeepCmd.txt"
out_file10 = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_target_sID_list_forKeepCmd.txt"


import random

f_sub = open(in_subtypes)
fout5 = open(out_file5, "w")
fout6 = open(out_file6, "w")

# sub_ER_PR_her2_dict: key=sID, value = [subtype, ER, PR, her2]
f = open(in_subtypes)
lines = f.readlines()
sub_ER_PR_her_dict = {}
for line in lines:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    age = cols[1]
    gender = cols[2]
    ER = cols[3]
    PR = cols[4]
    her2 = cols[5]
    subtype = cols[6]
    sub_ER_PR_her_dict[sID] = [subtype, ER, PR, her2, age, gender]

# age_bc_dict: key = age, value = [female_sID_list, male_sID_list]
# subtype_dict: key = age, value = [female_dict, male_dict]
# female_dict[subtype] = [sID], male_dict[subtype] = [sID]
# bc_line_dict: key = sID, value = [age, gender, [[c_sID, ...], [c_sID, ...]]]
def parseToDict(inBCFile, inSubDict = sub_ER_PR_her_dict):
    f_bc = open(inBCFile)
    lines = f_bc.readlines()
    age_bc_dict = {}
    subtype_dict = {}
    bc_line_dict = {}
    for line in lines:
        new_line = line.strip("\n")
        cols = new_line.split("\t")
        bc_sID = cols[0]
        bc_age = cols[1]
        bc_gender = cols[2]
        bc_subtype = inSubDict[bc_sID][0]
        # age_bc_dict
        if bc_age in age_bc_dict.keys():
            f_list = age_bc_dict[bc_age][0]
            m_list = age_bc_dict[bc_age][1]
            if bc_gender == "2":
                f_list.append(bc_sID)
                age_bc_dict[bc_age] = [f_list, m_list]
            else:
                m_list.append(bc_sID)
                age_bc_dict[bc_age] = [f_list, m_list]
        else:
            f_list = []
            m_list = []
            if bc_gender == "2":
                f_list.append(bc_sID)
                age_bc_dict[bc_age] = [f_list, m_list]
            else:
                m_list.append(bc_sID)
                age_bc_dict[bc_age] = [f_list, m_list]
        #sutype_dict
        if bc_subtype != "NA":
            if bc_age in subtype_dict.keys():
                f_dict = subtype_dict[bc_age][0]
                m_dict = subtype_dict[bc_age][1]
                if bc_gender == "2":
                    if bc_subtype in f_dict.keys():
                        old_list = f_dict[bc_subtype]
                        old_list.append(bc_sID)
                        f_dict[bc_subtype] = old_list
                    else:
                        f_dict[bc_subtype] = [bc_sID]
                else:
                    if bc_subtype in m_dict.keys():
                        old_list = m_dict[bc_subtype]
                        old_list.append(bc_sID)
                        m_dict[bc_subtype] = old_list
                    else:
                        m_dict[bc_subtype] = [bc_sID]
                subtype_dict[bc_age] = [f_dict, m_dict]
            else:
                f_dict = {}
                m_dict = {}
                if bc_gender == "2":
                    f_dict[bc_subtype] = [bc_sID]
                else:
                    m_dict[bc_subtype] = [bc_sID]
                subtype_dict[bc_age] = [f_dict, m_dict]
        # bc_line_dict
        start_idx = 3
        control_list = []
        for i in range(4):
            c_sID = cols[start_idx]
            c_age = cols[start_idx + 1]
            c_gender = cols[start_idx + 2]
            control_list.append([c_sID, c_age, c_gender])
            start_idx = start_idx + 3
        bc_line_dict[bc_sID] = [bc_age, bc_gender, control_list]
    return([age_bc_dict, subtype_dict, bc_line_dict])


def splitIDList(insIDList, inBaseList, inTargetList):
    while len(insIDList) >= 5:
        for i in range(4):
            bIdx = random.sample(range(len(insIDList)), 1)[0]
            bc_case = insIDList[bIdx]
            inBaseList.append(bc_case)
            insIDList.remove(bc_case)
        tIdx = random.sample(range(len(insIDList)), 1)[0]
        bc_target = insIDList[tIdx]
        inTargetList.append(bc_target)
        insIDList.remove(bc_target)
    if len(insIDList) != 0:
        for sID in insIDList:
            if len(inTargetList) == 0:
                inTargetList.append(sID)
            elif len(inBaseList)/len(inTargetList) > 4:
                inTargetList.append(sID)
            elif len(inBaseList)/len(inTargetList) <= 4:
                inBaseList.append(sID)
    return([inBaseList, inTargetList])

# split case for age-matched and 65 y/o controls
[age_bc_dict, subtype_dict, bc_line_dict] = parseToDict(in_bc)
[age_bc_65_dict, subtype_65_dict, bc_line_65_dict] = parseToDict(in_bc_65)
age_list = list(age_bc_dict.keys())
age_list.sort()
base_sID_list = []
target_sID_list = []
for age in age_list:
    [f_list, m_list] = age_bc_dict[age]
    [base_sID_list, target_sID_list] = splitIDList(f_list, base_sID_list, target_sID_list)
    [base_sID_list, target_sID_list] = splitIDList(m_list, base_sID_list, target_sID_list)

print(len(base_sID_list))
print(len(target_sID_list))

# split case for subtype
sub_age_list = list(subtype_dict.keys())
sub_age_list.sort()
sub_base_list = []
sub_target_list = []
for age in sub_age_list:
    [f_dict, m_dict] = subtype_dict[age]
    for subtype in f_dict.keys():
        f_sub_list = f_dict[subtype]
        [sub_base_list, sub_target_list] = splitIDList(f_sub_list, sub_base_list, sub_target_list)
    for subtype in m_dict.keys():
        m_sub_list = m_dict[subtype]
        [sub_base_list, sub_target_list] = splitIDList(m_sub_list, sub_base_list, sub_target_list)

print(len(sub_base_list))
print(len(sub_target_list))

def writeLine(inList, inDict, inFile):
    for sID in inList:
        [bcAge, bcGender, controlList] = inDict[sID]
        inFile.write(sID + "\t" + bcAge + "\t" + bcGender)
        for control in controlList:
            inFile.write("\t" + "\t".join(control))
        inFile.write("\n")

# write to file
def writeToFile(inBase, inTarget, inBaseList, inTargetList, insIDDict):
    foutB = open(inBase, "w")
    foutTar = open(inTarget, "w")
    writeLine(inBaseList, insIDDict, foutB)
    writeLine(inTargetList, insIDDict, foutTar)
    foutB.close()
    foutTar.close()

def writeLineKeep(inList, inDict, inFile):
    for sID in inList:
        [bcAge, bcGender, controlList] = inDict[sID]
        inFile.write(sID + "\t" + sID + "\t" + bcAge + "\t" + bcGender + "\tBC\n")
        for control in controlList:
            c_sID = control[0]
            inFile.write(c_sID + "\t" + "\t".join(control) + "\tControl\n")

def writeForKeepCommand(inBase, inTarget, inBaseList, inTargetList, insIDDict):
    foutB = open(inBase, "w")
    foutTar = open(inTarget, "w")
    writeLineKeep(inBaseList, insIDDict, foutB)
    writeLineKeep(inTargetList, insIDDict, foutTar)
    foutB.close()
    foutTar.close()

# write for subtype
def writeSubLineKeep(inList, inDict, inFile):
    for sID in inList:
        # traitList = [subtype, ER, PR, her2, age, gender]
        traitList = inDict[sID]
        inFile.write(sID + "\t" + sID + "\t" + "\t".join(traitList) + "\n")

def writeSubtypeForKeepCommand(inSubBase, inSubTarget, inSubBaseList, inSubTarList, inSubDict):
    foutB = open(inSubBase, "w")
    foutTar = open(inSubTarget, "w")
    writeSubLineKeep(inSubBaseList, inSubDict, foutB)
    writeSubLineKeep(inSubTarList, inSubDict, foutTar)
    foutB.close()
    foutTar.close()

writeToFile(out_file1, out_file2, base_sID_list, target_sID_list, bc_line_dict)
writeToFile(out_file3, out_file4, base_sID_list, target_sID_list, bc_line_65_dict)

writeForKeepCommand(out_file7, out_file8, base_sID_list, target_sID_list, bc_line_dict)
writeForKeepCommand(out_file9, out_file10, base_sID_list, target_sID_list, bc_line_65_dict)

writeSubtypeForKeepCommand(out_file5, out_file6, sub_base_list, sub_target_list, sub_ER_PR_her_dict)
