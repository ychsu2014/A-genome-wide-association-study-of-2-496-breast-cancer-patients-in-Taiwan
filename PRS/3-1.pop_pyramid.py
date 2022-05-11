in_base_file = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_base_sID_list.txt"
in_target_file = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_ageMatchControl_target_sID_list.txt"
b_out_png = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_matchedAge_base_data_popPyramid.png"
b_x_ticks = [0, 255, 50]#[-250, 255, 50]
b_y_ticks = [20, 105, 10]

t_out_png = "/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/case_matchedAge_target_data_popPyramid.png"
t_x_ticks = [0, 75, 10]#[-70, 75, 10]
t_y_ticks = [20, 105, 10]

#in_base_file = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_base_sID_list.txt"
#in_target_file = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yoControl_target_sID_list.txt"

#b_out_png = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yo_base_data_popPyramid.png"
#b_x_ticks = [0, 355, 50]#[-350, 355, 50]
#b_y_ticks = [20, 115, 10]

#t_out_png = "/home/iHiO10009/yuching/data/2.PRS/case_65yoControl_PRS/case_65yo_target_data_popPyramid.png"
#t_x_ticks = [0, 95, 10]#[-90, 95, 10]
#t_y_ticks = [20, 115, 10]


import numpy as np
import matplotlib.pyplot as plt

def parseToDicts(inFile):
    # age_sID_dict: key: age, value: [sID]
    f = open(inFile)
    lines = f.readlines()
    female_dict = {}
    male_dict = {}
    for line in lines:
        cols = line.strip("\n").split("\t")
        start_idx = 0
        for i in range(5):
            sID = cols[start_idx]
            age = int(cols[start_idx + 1])
            gender = cols[start_idx + 2]
            start_idx += 3
            if gender == "1":
                if age in male_dict.keys():
                    old_list = male_dict[age]
                    old_list.append(sID)
                    male_dict[age] = old_list
                else:
                    male_dict[age] = [sID]
            else:
                if age in female_dict.keys():
                    old_list = female_dict[age]
                    old_list.append(sID)
                    female_dict[age] = old_list
                else:
                    female_dict[age] = [sID]
    female_count_dict = {}
    male_count_dict = {}
    for age in female_dict.keys():
        pnum = len(female_dict[age])
        female_count_dict[age] = pnum
    for age in male_dict.keys():
        pnum = len(male_dict[age])
        male_count_dict[age] = -pnum
    return([female_count_dict, male_count_dict])

# key: age, value: pnum
def popPyramid(inFemaleDict, inMaleDict, inTitle, outFigName, inXticks, inYticks):
    all_age_list = list(inFemaleDict.keys()) + list(inMaleDict.keys())
    all_age_list.sort()
    female_age = []
    male_age = []
    for age in all_age_list:
        if age in inFemaleDict.keys():
            female_age.append(inFemaleDict[age])
        else:
            female_age.append(0)
        if age in inMaleDict.keys():
            male_age.append(inMaleDict[age])
        else:
            male_age.append(0)
    women_pop = np.array(female_age)
    men_pop = np.array(male_age)
    X = np.array(all_age_list)
    ax1 = plt.barh(X, women_pop, color = 'r')
    ax2 = plt.barh(X, men_pop, color = 'b')
    plt.title(inTitle)
    # left, right, step
    plt.xticks(np.arange(inXticks[0], inXticks[1], inXticks[2]))
    # bottom, top, step
    #plt.yticks(np.arange(min(X), max(X)+1, 10))
    plt.yticks(np.arange(inYticks[0], inYticks[1], inYticks[2]))
    plt.xlabel("patient counts", fontsize = 14)
    plt.ylabel("age", fontsize = 14)
    plt.tight_layout()
    plt.legend([ax1,ax2], ["female", "male"])
    plt.savefig(outFigName)

[b_female_dict, b_male_dict] = parseToDicts(in_base_file)
[t_female_dict, t_male_dict] = parseToDicts(in_target_file)

base_title = "Base data"
popPyramid(b_female_dict, b_male_dict, base_title, b_out_png, b_x_ticks, b_y_ticks)
plt.close()

target_title = "Target data"
popPyramid(t_female_dict, t_male_dict, target_title, t_out_png, t_x_ticks, t_y_ticks)
plt.close()
