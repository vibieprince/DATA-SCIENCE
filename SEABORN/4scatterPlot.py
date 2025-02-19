# Scatter Plot
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
var = sns.load_dataset('penguins')
print(var)

m = {"Male":"*","Female":"o"}
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex',style='sex',size='sex',sizes=[60,40],palette="icefire",alpha=0.5,markers=m)#markers=['*','<'])
plt.show()