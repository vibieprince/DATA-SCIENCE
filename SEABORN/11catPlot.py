# CAT PLOT
import matplotlib.pyplot as plt
import seaborn as sns
var = sns.load_dataset('tips').head(60)
# print(var)

# sns.catplot(x='tip',y='size',data=var,hue='sex',palette='PuOr',height=4)
# plt.show()

sns.catplot(x='day',y='size',data=var,hue='sex',palette='PuOr',kind='boxen') #bar
plt.show()