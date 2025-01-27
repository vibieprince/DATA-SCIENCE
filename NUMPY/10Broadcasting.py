import numpy as np
var1 = np.array([1,3,2,4])
var2 = np.array([2,1,4]) #less elements

# print(var1+var2) # Broadcasting error
# RULES
# 1. Same Dimension
# 2. If different dimension then row of one and col of other should be same 

# print(np.shape(var1))
print(var1.shape)
print(var1)
var2 = np.array([[1],[2],[3]])
print(var2.shape)
print(var2)

print()
print(var1+var2)

var3 = np.array([[2],[1]])
print(var3.shape)

y = np.array([[1,2,3],[4,5,6]])
print(y.shape)
print(var3+y)