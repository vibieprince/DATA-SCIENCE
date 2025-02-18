import matplotlib.pyplot as plt
import numpy as np
x = ["Python","c","c++","Java"]
y = [85,78,60,82]
z = [20,10,40,38]
plt.xlabel("language",fontsize=15)
plt.ylabel("Popularity",fontsize=15)
plt.title("Data Visualization",fontsize=15)
# plt.bar(x,y,width=0.3,color="r",label="Data Visuals 1")
# plt.bar(x,z,width=0.3,color="y",label="Data Visuals 2")
plt.legend()
# plt.show()

p = np.arange(len(x))
width = 0.2
p1 = [j+width for j in p]

# plt.bar(x,y,width,color="r",label="Data Visuals 1")
# plt.bar(p1,z,width,color="y",label="Data Visuals 2")

# plt.xticks(p+width/2,x,rotation=20)
plt.legend()
# plt.show()

plt.barh(x,y,width,color="r",label="Data Visuals 1")
plt.barh(p1,z,width,color="y",label="Data Visuals 2")

plt.legend()
plt.show()