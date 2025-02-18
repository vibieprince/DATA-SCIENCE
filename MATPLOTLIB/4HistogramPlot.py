import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(10,60,(50))
print(x)

no = [34, 35, 39, 48, 16, 16, 51, 13, 47, 43, 12, 31, 42, 34, 10, 44, 58,
       20, 16, 48, 53, 55, 38, 12, 25, 43, 54, 39, 57, 52, 54, 47, 32, 56,
       11, 17, 36, 35, 35, 25, 43, 36, 56, 13, 37, 43, 30, 32, 35, 15]
plt.title("Histogram")
plt.xlabel("Python")
plt.ylabel("Number")
# plt.hist(no,color='g',edgecolor='r',rwidth=0.5)
# plt.show()

# list = [10,20,30,40,50,60]
# plt.hist(no,color='g',bins=list,edgecolor='r')
# plt.show()

# plt.hist(no,"auto",[0,100],edgecolor='r')
# plt.show()

# list = [10,20,30,40,50,60]
# plt.hist(no,color='g',edgecolor='r',cumulative=-1,bottom=10,log=True) # starts x axis from 10

# plt.hist(no,color='g',edgecolor='r',histtype="step",orientation="horizontal") # barstack, stepfilled,bar etc
# plt.show()

plt.hist(no,color='g',edgecolor='r',label="Python")
plt.axvline(45,color='b',label="line")
plt.grid()
plt.legend()
plt.show()