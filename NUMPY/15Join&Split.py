import numpy as np
arr1 = np.array([3,6,8,3,5])
arr2 = np.array([9,8,7,6,5])

arr = np.concatenate((arr1,arr2))
print(arr)

arr1 = [[1,4,6,2,4],[8,4,27,5,4]]
arr2 = [[9,4,7,3,7],[7,2,8,3,6]]
arr = np.concatenate((arr1,arr2),axis=1)
print(arr1)
print()
print(arr)

arr = np.stack((arr1,arr2),axis=0)
# arr = np.hstack((arr1,arr2)) # Merge along row
# arr = np.vstack((arr1,arr2)) # Merge along column
# arr = np.dstack((arr1,arr2)) # Merge along height
print(arr)

# SPLIT
var = np.array([5,2,5,4,3])
print(var)
sp = np.array_split(var,3)
print(sp)
print(type(sp))

var1 = np.array([[8,3,6,3,6],[8,2,5,8,5]])
print(var1)
sp = np.array_split(var1,3,axis=1)
print(sp)