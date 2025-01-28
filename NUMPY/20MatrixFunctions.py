import numpy as np
mat = np.matrix([[2,3,4],[5,6,7],[6,4,8]])
print(mat)
print()
print(np.transpose(mat))
print()
# OR USE 
print(mat.T)

# SWAPAXES (similar to transpose)
print(np.swapaxes(mat,0,1))

# INVERSE
print(np.linalg.inv(mat))

# POWER OF MATRIX
# A^2 = A*A
print(np.linalg.matrix_power(mat,n=0)) # n = 0 --> IDENTITY 
print(np.linalg.matrix_power(mat,n=3)) # n > 0 --> POWER (multiplication) 
print(np.linalg.matrix_power(mat,n=-2)) # n < 0 --> INVERSE * POWER

print()
print(np.linalg.det(mat))
