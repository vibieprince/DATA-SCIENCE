# BAR PLOT
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset("penguins")
print(var)

# sns.barplot(x=var.island,y=var.bill_length_mm)
o = ["Dream","Torgersen","Biscoe"]
# sns.barplot(x="island",y="bill_length_mm",data=var,hue="sex",order=o,hue_order=["Female","Male"],errorbar=('ci',10),n_boot=12) # orient="h" ---> error : Horizontal orientation requires numeric 'x' variable
# plt.show()

sns.set(style='darkgrid')
sns.barplot(x='bill_length_mm',y='bill_depth_mm',data=var,orient='h',saturation=0.4,err_kws={'color':'g'},capsize=0.3,dodge=False)
# Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `y` variable to `hue` and set `legend=False` for the same effect.
plt.show()