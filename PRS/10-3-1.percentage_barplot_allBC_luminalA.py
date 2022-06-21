in_path = "/home/iHiO10009/yuching/data/2.PRS_v2"
in_folder = ["case_ageMatchControl_PRS", "subtype_PRS"]
in_bc = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_BC_age_gender.txt"
in_control = "/home/iHiO10009/yuching/data/1.QC_GWAS_v3/all_control_age_gender.txt"
pattern = "_ind_list.list"
png_suffix = "_ind_list_percentage.png"

#group_pattern = "ageMatch"
#fig_title = "BC vs. Age-matched controls"
#total_pnum = 2496

group_pattern = "luminalA"
fig_title = "Luminal A"
total_pnum = 1172


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

def convertToAlleleNumPnumDict(inDict, maxNum):
    outDict = {}
    for alleleNum in inDict.keys():
        plist = inDict[alleleNum]
        pnum = len(plist)
        outDict[alleleNum] = pnum
    alleleNum_sorted = []
    pnum_list = []
    for i in range(maxNum + 1):
        alleleNum_sorted.append(i)
        if i in outDict.keys():
            pnum = 100 * (outDict[i]/total_pnum)
            pnum_list.append(pnum)
        else:
            pnum_list.append(0)
    return([alleleNum_sorted, pnum_list])

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
            print("max alleleNum: " + str(max_alleleNum))
            bc_min = min(bc_alleleNum_sID_dict.keys())
            control_min = min(bc_alleleNum_sID_dict.keys())
            min_alleleNum = min([bc_min, control_min])
            print("min alleleNum: " + str(min_alleleNum))
            [bc_alleleNum_list, bc_pnum_list] = convertToAlleleNumPnumDict(bc_alleleNum_sID_dict, max_alleleNum)
            [con_alleleNum_list, con_pnum_list] = convertToAlleleNumPnumDict(control_alleleNum_sID_dict, max_alleleNum)
            # plot figure
            fig = plt.figure()
            ax = fig.add_axes([0.1,0.1,0.8,0.8])
            x = np.arange(max_alleleNum + 1)
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
            ax.set_xticklabels(bc_alleleNum_list)
            ax.legend()
            plt.ylim(0, max_pnum)
            plt.xlabel("Number of alleles")
            plt.ylabel("Individuals(%)")
            plt.title(fig_title)
            #plt.tight_layout()
            plt.savefig(fpath + "/" + out_file)
            plt.close()
            print(fpath + "/" + out_file)
            f.close()





            
                
