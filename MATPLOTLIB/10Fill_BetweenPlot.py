# FILL BETWEEN PLOT
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

plt.title("Python")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x,y,color='r')

# plt.fill_between(x=[2,4],y1=2,y2=5,color='g')
plt.fill_between(x,y,color='g',where=(x>=2) & (x<=4),alpha=0.3)
plt.show()