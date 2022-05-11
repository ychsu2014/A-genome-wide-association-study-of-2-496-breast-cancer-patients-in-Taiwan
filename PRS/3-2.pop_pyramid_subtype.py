import sys

in_base_file = sys.argv[1] #"/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_sID_list_forKeepCmd.txt"
in_target_file = sys.argv[2] #"/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_target_sID_list_forKeepCmd.txt"

b_out_png = sys.argv[3] #"/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_base_data_popPyramid_luminalA.png"
b_x_ticks = [0, 32, 5] #[-30, 32, 5]
b_y_ticks = [20, 85, 10]

t_out_png = sys.argv[4] #"/home/iHiO10009/yuching/data/2.PRS/subtype_PRS/subtype_target_data_popPyramid_luminalA.png"
t_x_ticks = [0, 10.5, 1]#[-10, 10.5, 1]
t_y_ticks = [20, 85, 10]

base_title = sys.argv[5]
target_title = sys.argv[6]

import numpy as np
import matplotlib.pyplot as plt

def addToDict(inDict, age, sID):
    if age in inDict.keys():
        old_list = inDict[age]
        old_list.append(age)
        inDict[age] = old_list
    else:
        inDict[age] = [sID]
    return(inDict)

def convertToPnumDict(inDict, mIdx = False):
    outDict = {}
    for age in inDict.keys():
        if mIdx != True:
            pnum = len(inDict[age])
        else:
            pnum = -len(inDict[age])
        outDict[age] = pnum
    return(outDict)

def parseToDicts(inFile):
    # age_sID_dict: key: age, value: [sID]
    f = open(inFile)
    lines = f.readlines()
    subtype_dict = {}
    for line in lines:
        cols = line.strip("\n").split("\t")
        if len(cols) >= 8:
            sID = cols[0]
            subtype = cols[3]
            age = int(cols[7])
            gender = cols[8]
        else:
            sID = cols[0]
            age = int(cols[3])
            gender = cols[4]
        subtype_dict = addToDict(subtype_dict, age, sID)
    subtype_pnum_dict = convertToPnumDict(subtype_dict)
    return(subtype_pnum_dict)

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

b_dict = parseToDicts(in_base_file)
t_dict = parseToDicts(in_target_file)

popPyramid(b_dict, {}, base_title, b_out_png, b_x_ticks, b_y_ticks)
popPyramid(t_dict, {}, target_title, t_out_png, t_x_ticks, t_y_ticks)
