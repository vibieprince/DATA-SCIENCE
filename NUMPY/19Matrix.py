import numpy as np
mat1 = np.matrix([[1,2,3],[1,2,3]])
mat2 = np.matrix([[1,2],[3,4],[5,6]])
var = np.array([[1,2,3],[1,2,3]])
print(mat1)
print(type(mat1))
print(type(var))

# NO DIFFERENCE IN ADDITION % SUBTRCTION OPERATION OF MATRIX AND ARRAY
# print(mat1+mat2)
# print(mat1-mat2)
# print(mat1*mat2) # ERROR

print(mat1.dot(mat2))
print(var*var)
