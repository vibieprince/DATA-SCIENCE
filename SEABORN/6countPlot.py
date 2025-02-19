# COUNT PLOT
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
var = sns.load_dataset('tips')
# print(var)

sns.countplot(y='sex',data=var,hue='smoker',palette='bwr',saturation=0.5)
plt.show()

# sns.barplot(x='sex',y='size',data=var)
# plt.show()