import sys
import math
import numbers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib

assoc = sys.argv[1]
title = sys.argv[2]
output_file = sys.argv[3]

#matplotlib.use('Agg')

gap=10
col_chr="CHR"
col_bp="BP"
col_p='P'
col_snp="SNP"
cmapVar = 25
suggestiveline=-np.log10(1e-5)
genomewideline=-np.log10(5e-8)
xtick_size=10
ytick_size=10
xrotation=0
yrotation=0
label_size=15
title_size=20

yuching_cmap = matplotlib.colors.ListedColormap(["blue", "green", "red", "blueviolet", "coral", "pink", "magenta", "cyan", "yellow", "orange", "grey", "lime", "peru", "deeppink", "saddlebrown", "lightseagreen", "olive", "plum", "lightgreen", "darkcyan", "gold", "lightsteelblue", "moccasin", "lightcoral", "navy"], name='from_list', N=None)

df_assoc = pd.read_csv(assoc, header=0, delim_whitespace=True)
df_assoc[col_chr] = df_assoc[col_chr].astype('category')
df_assoc[col_bp] = df_assoc[col_bp].astype(int)
df_assoc[col_p] = df_assoc[col_p].astype(float)
df_assoc = df_assoc.sort_values([col_chr,col_bp])

chr_len = list()
for cChr in df_assoc[col_chr].unique():
    chr_len.append(len(df_assoc[df_assoc[col_chr]==cChr]))
weight_gap = int(min(chr_len)/100)

list_ind = list()
for cChr in df_assoc[col_chr].unique():
    if len(list_ind) == 0:
        last_ind = 0
    else:
        last_ind = (list_ind[-1]+1)+(gap*weight_gap)
    list_ind += [last_ind+num for num in range(len(df_assoc[df_assoc[col_chr]==cChr]))]

df_assoc['IND'] = list_ind
df_assoc["LOG_P"] = -np.log10(df_assoc[col_p])

x_ticks,x_labels = list(),list()

fig, ax = plt.subplots(nrows=1, ncols=1, figsize = (12,12))

list_color = list()
step = int(len(yuching_cmap.colors) / cmapVar) 
for i, color in enumerate(yuching_cmap.colors):
    if i % step == 0:
        list_color.append(colors.to_hex(color))

for i, cChr in enumerate(df_assoc[col_chr].unique()):
    ind = df_assoc[df_assoc[col_chr]==cChr]['IND']  
    log_p = df_assoc[df_assoc[col_chr]==cChr]['LOG_P']
    ax.scatter(ind, log_p, s=50, color=list_color[i%cmapVar])
    x_ticks.append(ind.iloc[0]+(ind.iloc[-1]-ind.iloc[0])/2)
    x_labels.append(cChr)

x_padding = len(list_ind)/20
xlim_min = list_ind[0]-x_padding
xlim_max = list_ind[-1]+x_padding

if suggestiveline:
    ax.plot([xlim_min,xlim_max],[suggestiveline,suggestiveline],'b-')
if genomewideline:
    ax.plot([xlim_min,xlim_max],[genomewideline,genomewideline],'r-')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels)

ax.set_ylim(bottom=0)
ax.set_xlim([xlim_min,xlim_max])

ax.tick_params(axis='x', labelsize=xtick_size, labelrotation=xrotation)
ax.tick_params(axis='y', labelsize=ytick_size, labelrotation=yrotation)

ax.set_xlabel("Chromosomes",fontsize=label_size)
ax.set_ylabel(r'$-log_{10}(p)$',fontsize=label_size)

ax.set_title(title,fontsize=title_size)
fig.tight_layout()
#plt.show()
plt.savefig(output_file)
