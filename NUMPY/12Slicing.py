import numpy as np
arr = np.array([5,2,7,43,25,3])
print(arr)
print()
print("1 to 4 : ",arr[1:4]) # [start : stop : step]
print("1 to end : ",arr[1:])  
print("start to 4 : ",arr[:4])

# alternate
print("Alternate : ",arr[::2])

arr1 = np.array([[4,5,7,4],[3,8,2,6],[2,6,2,7]])
print(arr1.ndim)
print()
print("1 to 3 : ",arr1[0,1:3])
print("2 to 3 : ",arr1[1,2:3])