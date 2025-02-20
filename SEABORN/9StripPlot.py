# STRIP PLOT
# A strip plot is very simple to understand. 
#It is basically a scatter plot that differentitates different categories.
#Strip plots are considered a good alternative to a box plot or a violin plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset('tips')
print(var)

# m = {"Male":"o","Female":"<"}
# sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='rocket_r',linewidth=1,jitter=1,size=5,marker='<')
# plt.show()

sns.stripplot(y=var['total_bill'])
plt.show()