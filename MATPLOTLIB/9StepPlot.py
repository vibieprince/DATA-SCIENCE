# STEP PLOT
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [2,7,3,5,4,6]

plt.title("Python")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.step(x,y,color='r',marker='o',ms=10,mfc='b',label="Python")
plt.legend(loc=1)
plt.grid()
plt.show()