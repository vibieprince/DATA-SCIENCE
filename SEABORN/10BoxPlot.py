# BOX PLOT 
import seaborn as sns
import matplotlib.pyplot as plt
var = sns.load_dataset('tips')
# print(var)

# sns.set(style='whitegrid')
# sns.boxplot(x='day',y='total_bill',data=var,hue='sex',palette='plasma',showmeans=True,meanprops={'marker':'+','markeredgecolor':'r'},linewidth=2)
# plt.show()

# sns.boxplot(y='day',x='total_bill',data=var,hue='sex',palette='plasma',showmeans=True,meanprops={'marker':'+','markeredgecolor':'r'},linewidth=2)
# plt.show()

# sns.boxplot(data=var,showmeans=True,meanprops={'marker':'+','markeredgecolor':'r'},linewidth=2,palette='plasma',orient='h')
# plt.show()

sns.boxplot(y=var['total_bill'])
plt.show()