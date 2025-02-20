# MULTIPLE PLOT - FACET GRID
import matplotlib.pyplot as plt
import seaborn as sns
var = sns.load_dataset('tips')
# print(var)

# fg = sns.FacetGrid(var,col='sex',hue='day')
# fg.map(plt.scatter,'total_bill','tip').add_legend()
# plt.show()

fg = sns.FacetGrid(var,col='day',hue='sex')
fg.map(plt.bar,'total_bill','tip',edgecolor='r').add_legend()
plt.show()