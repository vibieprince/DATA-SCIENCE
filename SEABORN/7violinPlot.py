import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var = sns.load_dataset('tips')
# print(var)

# sns.violinplot(x='day',y='total_bill',data=var,hue='time',linewidth=3,palette='Dark2')
# plt.show()

# sns.violinplot(x='time',y='total_bill',data=var,order=['Dinner','Lunch'],hue='time',palette='Accent')
# plt.show()

# sns.violinplot(y='day',x='total_bill',data=var,hue='sex',split=True,density_norm='width',inner='quart') # inner='box'/'stick'
# plt.show()

# sns.violinplot(x=var['total_bill'])
# plt.show()