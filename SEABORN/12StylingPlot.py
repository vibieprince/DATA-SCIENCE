# STYLING PLOT
import matplotlib.pyplot as plt
import seaborn as sns
var = sns.load_dataset('tips')
# print(var)

# sns.boxplot(y=var['total_bill'])
# plt.show()

# sns.set_style('darkgrid') # ticks,dark,whitegrid
# plt.figure(figsize=(12,3)) # 12 : 3
# sns.barplot(x='day',y='total_bill',data=var)
# sns.despine() # Remove axis line
# plt.show()

sns.set_context('paper',font_scale=1) # poster
sns.barplot(x='day',y='total_bill',data=var,palette='cool')
plt.show()