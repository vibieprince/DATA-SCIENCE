import numpy as np
x = np.array([[53,5,3,6,3],[5,3,8,4,6]])
print(x)
print()
print(x.shape)

var1 = np.array([2,4,6,2,5],ndmin=4)
print(var1)
print(var1.ndim)
print()
print(var1.shape)

# RESHAPE
one_d = np.array([1,2,3,4,5,6])
two_d = one_d.reshape(3,2)
print(one_d)
print(one_d.ndim)
print(two_d)
print(two_d.ndim)

one_d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
three_d = one_d.reshape(2,3,2)
print(three_d)

three_d  = one_d.reshape(4,3,1)
print(three_d)

one_d = three_d.reshape(-1)
print(one_d)
print(one_d.ndim)
