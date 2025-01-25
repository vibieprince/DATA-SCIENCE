import numpy as np
zero = np.zeros(4) #array filled with zeroes with length 4
zero1 = np.zeros((3,4))
print(zero)
print()
print(zero1)

one = np.ones(4) #array filled with ones with length 4
print(one)

# Empty array creation
emp = np.empty(5)
print(emp)

# range arrau creation 
range = np.arange(5)
print(range)

# diagonal filled with ones (IDENTITY MATRIX)
dia = np.eye(3,4)
print(dia)

ide = np.identity(4) # works only for square matrix
print(ide)

arr_lin = np.linspace(1,10,num=5) #array with special interval values
print(arr_lin)

arr_lin = np.linspace(0,20,num=5) #array with special interval values
print(arr_lin)

arr_lin = np.linspace(0,10,num=4) #array with special interval values
print(arr_lin)
