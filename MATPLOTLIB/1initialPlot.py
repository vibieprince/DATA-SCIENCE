import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [2,4,6,8]

c = ["r","y","g","b"]
plt.bar(x,y,color=c) 
# plt.show()

x = ["Python","c","c++","Java"]
y = [85,78,60,82]
plt.bar(x,y)
# plt.show()

plt.xlabel("language",fontsize=15)
plt.ylabel("Popularity",fontsize=15)
plt.title("Data Visualization")
plt.bar(x,y)
# plt.show()

c = ["r","y","b","g"]
plt.bar(x,y,width=0.3,color=c,edgecolor="r",linewidth=4,linestyle=":",alpha=0.4) # align="edge" # default : center
# plt.show()

plt.bar(x,y,label="Data Visuals")
plt.legend()
plt.show()