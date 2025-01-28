import numpy as np
var = np.array([2,5,7,3,6,2,6])
print(var)
x = np.insert(var,2,40)
print(x)
x = np.insert(var,(2,5),80) # if you give decimal insertion, it will typecast it automatically into integer type
print(x)
print()
var1 = np.array([[5,6,2,7,3,6],[5,7,2,7,9,4]])
v1 = np.insert(var1,2,67)
v1 = np.insert(var1,2,67,axis=0)
v1 = np.insert(var1,2,67,axis=1)
v1 = np.insert(var1,2,(2,4,6,3,9,7),axis=0) # axis=1 will raise error
print(v1)

x = np.append(var,5.6)
print(x)

v1 = np.append(var1,[[4.4,8.3,9,3.2,6.7,4]],axis=0)
print(v1)

d = np.delete(var,3)
print(d)