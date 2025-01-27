import numpy as np
var = np.array([1,2,3,4])
var_add = var + 3
print(var_add)

arr1 = np.array([4,2,6,2])
arr2 = np.array([42,24,2,5])
print(arr1+arr2) #np.add

print(arr1-arr2) # np.subtract

print(arr1*arr2) #np.multiply

print(arr1/arr2) # np.divide

print(arr1%arr2) # np.mod

var_new = np.reciprocal(arr1)
print("Reciprocal : ",var_new)
var2 = np.array([[1,2,3,4],[1,2,3,4]])
var3 = np.array([[5,6,7,8],[1,5,8,5]])
print(var2)
print()
print(var3)
print()
var_add = var2 + var3
print(var_add)
