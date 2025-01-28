import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8])
np.random.shuffle(arr) #SHUFFLE
print(arr)

var = np.array([1,2,3,4,2,6,2,7])
x = np.unique(var) #UNIQUE
print(x)
x = np.unique(var,return_index=True)
print(x)
x = np.unique(var,return_counts=True)
print(x)

var = np.array([4,6,8,3,56,8,4,8,4])
print(var)
x = np.resize(var,(2,3)) #RESIZE
print(x)
x = np.resize(var,(3,3)) #RESIZE
print(x)
print()
print("Flatten : ",x.flatten(order="F"))
print("Ravel : ",x.ravel(order="F"))
print("Ravel : ",x.ravel(order="K"))
print("Ravel : ",x.ravel(order="A"))