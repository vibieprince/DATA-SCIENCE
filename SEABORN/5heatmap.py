# HEAT MAP
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

var = np.linspace(1,10,20).reshape(4,5)

# sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True)
# plt.show()

data = sns.load_dataset('anagrams')
x = data.drop(columns='attnr')
# print(x)

# sns.heatmap(x)
# plt.show()

var = np.linspace(1,10,10).reshape(2,5)
# print(var)

# sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True)
# plt.show()

ar = np.array([['a0','a1','a2','a3','a4'],['b0','b1','b2','b3','b4']])
# print(ar)

y = {'fontsize':10,'color':'r'}
v = sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=ar,fmt='s',annot_kws=y,linewidth=10,linecolor='y',cbar=False)
# xtickslabel, ytickslabel
v.set(xlabel='Python',ylabel='Growth')
sns.set(font_scale=5)
plt.show()