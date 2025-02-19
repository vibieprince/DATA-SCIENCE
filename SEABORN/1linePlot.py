# LINE PLOT
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

var = [1,2,3,4,5,6,7]
var_1 = [2,3,4,2,5,6,7]
# df = pd.DataFrame({"var":var,"var_1":var_1})
# sns.lineplot(x="var",y="var_1",data=df)
# plt.show()

# plt.plot(var,var_1)
# plt.show()

# sns.lineplot(x=var,y=var_1)
# plt.show()

y = sns.load_dataset("penguins")
# print(y)

# sns.lineplot(x="bill_length_mm",y="flipper_length_mm",data=y)
# plt.show()

sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y,hue="sex",size=10,style="sex",palette="Accent",markers=["o",">"],dashes=False,legend=False)
plt.grid()
plt.title("Python")
plt.show()