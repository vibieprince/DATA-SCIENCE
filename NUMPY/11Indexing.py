import numpy as np
var = np.array([4,2,6,8,3]) # 1-D
print(var[3])
print(var[-2])

var1 = np.array([[4,5,6,7],[3,8,3,6]]) # 2-D
print(var1.ndim)
print(var1[0][2])
print(var1[1][2])

var2 = np.array([[[3,4,5],[3,2,7]]])
print(var2)
print(var2.ndim)
print(var2[0][0][2])