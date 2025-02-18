# SCATTER PLOT
import matplotlib.pyplot as plt
day = [1,2,3,4,5,6,7]
no = [2,3,6,4,8,4,3]
no2 = [6,5,7,3,2,7,7]
colors = [67,46,84,45,89,36,57]
c = ["r","y","b","m","g","b","y"] 
sizes = [67,35,62,168,427,93,718]
# plt.scatter(day,no,c=colors,s=sizes,alpha=0.5,cmap="viridis",marker="*") #cmap = BrBg,BuGn,Greens,viridis etc # S for square default  : circle
plt.scatter(day,no,c=colors,s=sizes,alpha=0.5,cmap="viridis")
plt.scatter(day,no2,color="r",s=sizes,alpha=0.5)
# can use edgeline edgecolor linewidth as used in previous programs 
t = plt.colorbar()
t.set_label("colorbar",fontsize=15)
plt.title("Scatter Plot",fontsize=15)
plt.xlabel("Day",fontsize=15)
plt.ylabel("Number",fontsize=15)
plt.show()