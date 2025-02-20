# PAIR PLOT
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

var = sns.load_dataset('tips')
print(var)

# sns.pairplot(var,vars=['total_bill','tip'],hue='sex',hue_order=['Female','Male'],palette='PuOr')
# plt.show()

# sns.pairplot(var,hue='sex',hue_order=['Female','Male'],palette='PuOr',x_vars=['total_bill','tip'],y_vars=['total_bill','tip'])
# plt.show()

sns.pairplot(var,hue='sex',hue_order=['Female','Male'],kind='reg',diag_kind='hist',markers=['<','o']) # kde
plt.show()