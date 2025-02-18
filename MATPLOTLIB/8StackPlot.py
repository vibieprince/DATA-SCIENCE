# AREA or STACK PLOT
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
area = [2,3,2,5,4]
area1 = [2,3,4,5,6]
area2 = [1,3,2,4,2]
l = ["Area","Area1","Area2"]
c = ['r','g','y']
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Python")
plt.stackplot(x,area,area1,area2,labels=l,colors=c,baseline="zero") #winle / sym
plt.legend()
plt.show()