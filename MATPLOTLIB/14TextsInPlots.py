import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [3,4,6,2,5]


plt.title("Python's Growth",fontsize=15)
plt.xlabel("Days",fontsize=15)
plt.ylabel("Growth",fontsize=15)

plt.text(2,4,"Python",fontsize=10,style="italic",bbox={"facecolor":"red"})
plt.text(3,6,"Peak",fontsize=10,style="italic",bbox={"facecolor":"yellow"})
plt.annotate("Lowest",xy=(4,2),xytext=(4,4),arrowprops=dict(facecolor="black",shrink=100))
plt.plot(x,y)
plt.legend(["Growth"],loc=2,edgecolor='r',framealpha=0.6,shadow=True)
plt.show()