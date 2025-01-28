import numpy as np
var = np.array([3,5,6,7,8,12,41,67])
x = np.where(var==4)
print(x)
x = np.where(var%2==0)
print(x)

var = np.array([4,6,7,8,9])
x = np.searchsorted(var,5)
x = np.searchsorted(var,3,side="right")
x = np.searchsorted(var,[8,8,9],side="right")
print(x)

# SORT
var = np.array([4,6,3,6,7,3,7,3,7,2])
x = np.sort(var)
print(x)

var = np.array(["a","t","s","b","r","m"])
x = np.sort(var)
print(x)

var = np.array([[1,2,7,4,6],[6,3,7,25,5],[6,2,78,35,5]])
x = np.sort(var)
print(x)

var = np.array([5,7,3,5,7])
var = np.array(["a","t","s","b","r"])
f = [True,False,True,False,True]
x = var[f]
print(x)
print(type(x))