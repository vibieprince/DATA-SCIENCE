# DIST PLOT
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var = sns.load_dataset("penguins")
# print(var)

# sns.displot(var['flipper_length_mm'],bins=[170,180,190,200,210,220,230,240],kde=True)
# plt.show()

sns.displot(var['flipper_length_mm'],kde=True,rug=True,color='g')#log_scale=True)
plt.show()