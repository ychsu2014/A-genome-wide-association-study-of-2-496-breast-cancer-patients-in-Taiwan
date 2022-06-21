in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/final_BC_control_list.txt"
in_subtypes = "/home/iHiO10009/yuching/data/2.PRS_v2/subtypes/BC_subtypes_afterQC_2496.txt"
out_file1 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list.txt"
out_file2 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list.txt" 
out_file3 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list_forKeepCmd.txt"
out_file4 = "/home/iHiO10009/yuching/data/2.PRS_v2/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list_forKeepCmd.txt"

out_f1 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_base_list_forKeepCmd.txt"
out_f2 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalA_target_list_forKeepCmd.txt"
out_f3 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_base_list_forKeepCmd.txt"
out_f4 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/luminalB_target_list_forKeepCmd.txt"
out_f5 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_base_list_forKeepCmd.txt"
out_f6 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/basal_target_list_forKeepCmd.txt"
out_f7 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_base_list_forKeepCmd.txt"
out_f8 = "/home/iHiO10009/yuching/data/2.PRS_v2/subtype_PRS/her2_target_list_forKeepCmd.txt"


import random

f_sub = open(in_subtypes)

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

# age_bc_dict: key = age, value = bc_sID_list
# subtype_dict: key = age, value = bc_dict
# bc_dict[subtype] = [sID]
# bc_line_dict: key = sID, value = [age, gender, [[c_sID, ...], [c_sID, ...]]]
def parseToDict(inBCFile, inSubDict = sub_ER_PR_her_dict):
    f_bc = open(inBCFile)
    lines = f_bc.readlines()
    subtype_dict = {}
    bc_line_dict = {}
    for line in lines:
        new_line = line.strip("\n")
        cols = new_line.split("\t")
        bc_sID = cols[0]
        bc_age = cols[1]
        bc_gender = cols[2]
        bc_subtype = inSubDict[bc_sID][0]
        #sutype_dict
        if bc_age in subtype_dict.keys():
            bc_dict = subtype_dict[bc_age]
            if bc_subtype in bc_dict.keys():
                old_list = bc_dict[bc_subtype]
                old_list.append(bc_sID)
                bc_dict[bc_subtype] = old_list
            else:
                bc_dict[bc_subtype] = [bc_sID]
            subtype_dict[bc_age] = bc_dict
        else:
            bc_dict = {}
            bc_dict[bc_subtype] = [bc_sID]
            subtype_dict[bc_age] = bc_dict
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
    return([subtype_dict, bc_line_dict])


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


[bc_subtype_dict, bc_line_dict] = parseToDict(in_bc)
# split case for subtype
# To keep same bc for ageMatch/65yoControls in the base data, only bc_subtype_dict will be used.
sub_age_list = list(bc_subtype_dict.keys())
sub_age_list.sort()
sub_base_list = []
sub_target_list = []
for age in sub_age_list:
    bc_dict = bc_subtype_dict[age]
    for subtype in bc_dict.keys():
        bc_sub_list = bc_dict[subtype]
        [sub_base_list, sub_target_list] = splitIDList(bc_sub_list, sub_base_list, sub_target_list)

luminalA_base_list_wo_NA = []
luminalA_target_list_wo_NA = []
luminalB_base_list_wo_NA = []
luminalB_target_list_wo_NA = []
basal_base_list_wo_NA = []
basal_target_list_wo_NA = []
her2_base_list_wo_NA = []
her2_target_list_wo_NA = []
for sID in sub_base_list:
    subtype = sub_ER_PR_her_dict[sID][0]
    if subtype == "Luminal A":
        luminalA_base_list_wo_NA.append(sID)
    elif subtype == "Luminal B":
        luminalB_base_list_wo_NA.append(sID)
    elif subtype == "Basal-like":
        basal_base_list_wo_NA.append(sID)
    elif subtype == "Her2-enriched":
        her2_base_list_wo_NA.append(sID)
for sID in sub_target_list:
    subtype = sub_ER_PR_her_dict[sID][0]
    if subtype == "Luminal A":
        luminalA_target_list_wo_NA.append(sID)
    elif subtype == "Luminal B":
        luminalB_target_list_wo_NA.append(sID)
    elif subtype == "Basal-like":
        basal_target_list_wo_NA.append(sID)
    elif subtype == "Her2-enriched":
        her2_target_list_wo_NA.append(sID)
print(len(sub_base_list))
print(len(sub_target_list))
print(len(luminalA_base_list_wo_NA))
print(len(luminalA_target_list_wo_NA))
print(len(luminalB_base_list_wo_NA))
print(len(luminalB_target_list_wo_NA))
print(len(basal_base_list_wo_NA))
print(len(basal_target_list_wo_NA))
print(len(her2_base_list_wo_NA))
print(len(her2_target_list_wo_NA))

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

def writeLineKeep(inList, inDict, inFile, inSubDict):
    for sID in inList:
        [bcAge, bcGender, controlList] = inDict[sID]
        traitList = inSubDict[sID]
        inFile.write(sID + "\t" + sID + "\tBC\t" + "\t".join(traitList) + "\n")
        for control in controlList:
            c_sID = control[0]
            inFile.write(c_sID + "\t" + c_sID + "\tControl\t" + "\t".join(control[1:]) + "\n")

def writeForKeepCommand(inBase, inTarget, inBaseList, inTargetList, insIDDict, inSubDict):
    foutB = open(inBase, "w")
    foutTar = open(inTarget, "w")
    writeLineKeep(inBaseList, insIDDict, foutB, inSubDict)
    writeLineKeep(inTargetList, insIDDict, foutTar, inSubDict)
    foutB.close()
    foutTar.close()


writeToFile(out_file1, out_file2, sub_base_list, sub_target_list, bc_line_dict)
writeForKeepCommand(out_file3, out_file4, sub_base_list, sub_target_list, bc_line_dict, sub_ER_PR_her_dict)

writeForKeepCommand(out_f1, out_f2, luminalA_base_list_wo_NA, luminalA_target_list_wo_NA, bc_line_dict, sub_ER_PR_her_dict)
writeForKeepCommand(out_f3, out_f4, luminalB_base_list_wo_NA, luminalB_target_list_wo_NA, bc_line_dict, sub_ER_PR_her_dict)
writeForKeepCommand(out_f5, out_f6, basal_base_list_wo_NA, basal_target_list_wo_NA, bc_line_dict, sub_ER_PR_her_dict)
writeForKeepCommand(out_f7, out_f8, her2_base_list_wo_NA, her2_target_list_wo_NA, bc_line_dict, sub_ER_PR_her_dict)
