in_folder = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/PRS_scores"
out_file = "D:/TIGP_bioinformatics/research/CMUH_breast_cancer/PRS_visualization_v2/PRS_group_count.txt"

import os
import math

fout = open(out_file, "w")
fout.write("filename\tcontrol1\tcontrol2\tcontrol3\tcontrol4\tcontrol5\tcase1\tcase2\tcase3\tcase4\tcase5\n")

files = ["ageMatch_PRS_score.txt", "luminalA_PRS_score.txt", "luminalB_PRS_score.txt", "basal_PRS_score.txt", "her2_PRS_score.txt"]
for afile in files:
    print(afile)
    f = open(in_folder + "/" + afile)
    lines = f.readlines()
    control_list = []
    case_list = []
    for line in lines:
        cols = line.strip("\n").split("\t")
        group = cols[0]
        score = float(cols[1])
        if group == "Control":
            control_list.append(score)
        elif group == "BC":
            case_list.append(score)
        else:
            print("Please check")
    # determine the control num for each group
    total_control_num = len(control_list)
    num_per_group = math.floor(total_control_num / 5)
    notUsed_num = total_control_num - num_per_group * 5
    control_num_list = [num_per_group] * 5
    for i in range(notUsed_num):
        control_num_list[i] += 1
    # get the threshold from control group
    control_list.sort()
    threshold_list = []
    threshold_list.append(-math.inf)
    cummu_num = 0
    for i in range(len(control_num_list)-1):
        cummu_num += control_num_list[i]
        threshold_idx = cummu_num
        print(threshold_idx)
        #print(len(control_list))
        threshold = control_list[threshold_idx]
        threshold_list.append(threshold)
    threshold_list.append(math.inf)
    print(threshold_list)
    # use the thresholds to group scores of case groups
    case_group_list = []
    for i in range(len(control_num_list)):
        case_group_list.append([])
    for score in case_list:
        for i in range(len(threshold_list)-1):
            lower = threshold_list[i]
            upper = threshold_list[i+1]
            if score >= lower and score < upper:
                temp_list = case_group_list[i]
                temp_list.append(score)
                case_group_list[i] = temp_list
    # calculate the case num for each group
    case_num_list = []
    for alist in case_group_list:
        case_num = len(alist)
        case_num_list.append(case_num)
    # write to file
    fout.write(afile)
    for i in control_num_list:
        fout.write("\t" + str(i))
    for i in case_num_list:
        fout.write("\t" + str(i))
    fout.write("\n")

fout.close()
