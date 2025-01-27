import numpy as np
var = np.array([1,2,3,4,5])
print("Min : ",np.min(var))
print("Max : ",np.max(var))

print("Max Position : ",np.argmax(var))
print("Min Position : ",np.argmin(var))

var1 = np.array([[1,2,4,2,4],[4,2,6,3,5]])
print(np.min(var1,axis=1))   #min(var,axis=1 means row , axis=0 means col))
print(np.min(var1,axis=0))

print("Square root : ",np.sqrt(var))
print("Square root : ",np.sqrt(var1))


# TRIGNOMETRIC FUNCTIONS
var2 = np.array([4,6,2,5,2])
print(np.sin(var2))
print(np.cos(var2))

# CUMULATIVE SUM --- used in finding median in statistics
# [1,2,3]
# [1,3,3] -- answer

var3 = np.array([1,4,2,435,2])
print(np.cumsum(var3))
