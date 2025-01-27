import numpy as np
var = np.array([1,2,3,4])
print("Data Type : ",var.dtype)

var = np.array([4.5,67.5,88.5,89.4])
print("Data type : ",var.dtype)

var = np.array(["A","S","D","F"])
print("Data type : ",var.dtype) #--> <U1 (string type)

var = np.array(["A","D",1,2,3]) 
print("Data type : ",var.dtype) # --> <U21 ()

x = np.array([1,2,3,4])
print("Data type : ",x.dtype)

x = np.array([1,2,3,4],dtype=np.int8)
print("Data type : ",x.dtype)

x = np.array([1,2,3,4],dtype="f")
print("Data type : ",x.dtype)

x = np.array([1,2,3,4])
new = np.float64(x)
new_one = np.int_(new)

print("Data type : ",x.dtype)
print("Data Type : ",new.dtype)
print("Data Type : ",new_one.dtype)

print(x)
print(new)
print(new_one)

x1 = np.array([1,2,3,4])
new_1 = x1.astype(float)
print("x1 :",x1)
print(new_1)
