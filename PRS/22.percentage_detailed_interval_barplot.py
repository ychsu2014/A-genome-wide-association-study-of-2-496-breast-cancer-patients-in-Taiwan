in_path = "/home/iHiO10009/yuching/data/2.PRS"
in_folder = ["case_65yoControl_PRS", "case_ageMatchControl_PRS", "subtype_PRS"]
in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC_GWAS_v2/all_control_age_gender.txt"
pattern = "_ind_list.list"
png_suffix = "_ind_list_detailed_percentage.png"

group_pattern = "yo65Control"
interval_num = 10
fig_title = "BC vs. Controls aged more than 65 y/o"
total_pnum = 2495

#group_pattern = "luminalB"
#interval_num = 5
#fig_title = "Luminal B"
#total_pnum = 245

#group_pattern = "basal"
#interval_num = 10
#fig_title = "Basal-like"
#total_pnum = 225

#group_pattern = "her2"
#interval_num = 20
#fig_title = "Her2-enriched"
#total_pnum = 200

import os
import matplotlib.pyplot as plt
import numpy as np

# BC list
f_bc = open(in_bc)
bc_list = []
for line in f_bc:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    bc_list.append(sID)

# Control list
f_control = open(in_control)
control_list = []
for line in f_control:
    cols = line.strip("\n").split("\t")
    sID = cols[0]
    control_list.append(sID)

def convertToAlleleNumSIDDict(inDict):
    outDict = {}
    for sID in inDict.keys():
        alleleNum = inDict[sID]
        if alleleNum in outDict.keys():
            old_list = outDict[alleleNum]
            old_list.append(sID)
            outDict[alleleNum] = old_list
        else:
            outDict[alleleNum] = [sID]
    return(outDict)

def convertToIntervalCount(inDict, maxNum, minNum, interval):
    outDict = {}
    for alleleNum in inDict.keys():
        plist = inDict[alleleNum]
        pnum = len(plist)
        outDict[alleleNum] = pnum
    binNum = int(maxNum / interval) + 1
    startBinNum = int(minNum / interval)
    steps = [startBinNum * interval]
    step_temp = startBinNum * interval
    for i in range(binNum-startBinNum):
        step_temp += interval
        steps.append(step_temp)
    outIntervalDict = {}
    outIntervalList = []
    for i in range(len(steps)-1):
        start = steps[i]
        end = steps[i+1]
        outIntervalDict[(start,end)] = 0
        outIntervalList.append((start,end))
    for alleleNum in range(maxNum + 1):
        include_idx = False
        for i in range(len(steps)-1):
            start = steps[i]
            end = steps[i+1]
            if alleleNum >= start and alleleNum < end:
                include_idx = True
                if alleleNum in outDict.keys():
                    pnum_temp = outDict[alleleNum]
                else:
                    pnum_temp = 0
                pnum = outIntervalDict[(start, end)]
                pnum += pnum_temp
                outIntervalDict[(start, end)] = pnum
    outIntervalPnumList = []
    for i in outIntervalList:
        pnum = 100 * (outIntervalDict[i]/total_pnum)
        outIntervalPnumList.append(pnum)
    return([outIntervalList, outIntervalPnumList])


for afolder in in_folder:
    fpath = in_path + "/" + afolder
    all_files = os.listdir(fpath)
    for afile in all_files:
        if pattern in afile and group_pattern in afile:
            print(fpath + "/" + afile)
            f = open(fpath + "/" + afile)
            out_file = afile.replace(pattern, "") + png_suffix
            bc_sID_alleleNum_dict = {}
            control_sID_alleleNum_dict = {}
            count = 0
            for line in f:
                count += 1
                if count % 100 ==0:
                    print(count)
                # CHROM  SNP_ID  genotype  FID1 IID1 FID2 IID2 FID3 IID3
                cols = line.strip("\n").split(" ")
                SNP_ID = cols[1]
                A1 = SNP_ID.split("/")[1]
                genotype = cols[2]
                allele_num = genotype.count(A1)
                sIDs = list(set(cols[3:]))
                for sID in sIDs:
                    if sID in bc_list:
                        if sID not in bc_sID_alleleNum_dict.keys():
                            bc_sID_alleleNum_dict[sID] = allele_num
                        else:
                            old_num = bc_sID_alleleNum_dict[sID]
                            old_num += allele_num
                            bc_sID_alleleNum_dict[sID] = old_num
                    elif sID in control_list:
                        if sID not in control_sID_alleleNum_dict.keys():
                            control_sID_alleleNum_dict[sID] = allele_num
                        else:
                            old_num = control_sID_alleleNum_dict[sID]
                            old_num += allele_num
                            control_sID_alleleNum_dict[sID] = old_num
            bc_alleleNum_sID_dict = convertToAlleleNumSIDDict(bc_sID_alleleNum_dict)
            control_alleleNum_sID_dict = convertToAlleleNumSIDDict(control_sID_alleleNum_dict)
            bc_max = max(bc_alleleNum_sID_dict.keys())
            control_max = max(control_alleleNum_sID_dict.keys())
            max_alleleNum = max([bc_max, control_max])
            print("max_alleleNum: " + str(max_alleleNum))
            bc_min = min(bc_alleleNum_sID_dict.keys())
            control_min = min(bc_alleleNum_sID_dict.keys())
            min_alleleNum = min([bc_min, control_min])
            print("min_alleleNum: " + str(min_alleleNum))
            [bc_inter_list, bc_pnum_list] = convertToIntervalCount(bc_alleleNum_sID_dict, max_alleleNum, min_alleleNum, interval_num)
            [con_inter_list, con_pnum_list] = convertToIntervalCount(control_alleleNum_sID_dict, max_alleleNum, min_alleleNum, interval_num)
            inter_list = []
            for i in bc_inter_list:
                i_str = []
                for i_temp in i:
                    i_str.append(str(i_temp))
                temp =  "~".join(list(i_str))
                inter_list.append(temp)
            # plot figure
            fig = plt.figure()
            ax = fig.add_axes([0.2,0.2,0.7,0.7])
            x = np.arange(len(con_pnum_list))
            pos_list = []
            for i in x:
                pos_list.append(i + 0.125)
            print(x + 0.00)
            print(con_pnum_list)
            #plt.bar(x + 0.00, con_pnum_list, 0.25, color = 'b')
            #plt.bar(x + 0.25, bc_pnum_list, 0.25, color = 'r')
            ax.bar(x + 0.00, con_pnum_list, color = 'b', width = 0.25, label = "Control")
            ax.bar(x + 0.25, bc_pnum_list, color = 'r', width = 0.25, label = "Case")
            bc_max_pnum = max(bc_pnum_list)
            con_max_pnum = max(con_pnum_list)
            max_pnum = max(bc_max_pnum, con_max_pnum) + 3
            ax.set_xticks(pos_list)
            ax.set_xticklabels(inter_list, rotation = 45)
            plt.ylim(0, max_pnum)
            plt.xlabel("Number of alleles")
            plt.ylabel("Individuals(%)")
            plt.title(fig_title)
            ax.legend()
            #plt.tight_layout()
            plt.savefig(fpath + "/" + out_file)
            plt.close()
            print(fpath + "/" + out_file)
            f.close()





            
                
