import numpy as np
var = np.array([8,40,3,22,24,5])
for i in var:
    print(i)

var = np.array([[3,2,68,4],[5,35,25,6]])
for i in var:
    print(i)

for i in var:
    for k in i:
        print(k)

var3 = np.array([[[3,5,3,6,3],[3,3,2,6,4]]])
print(var3)
print(var3.ndim)
# for i in var3:
#     for j in i:
#         for k in j:
#             print(k)

# to cure this for loop method again and again
# use nditer

for i in np.nditer(var3):
    print(i)

# for i in np.nditer(var3,flags=['buffered'],op_dtypes=["S"]):
#     print(i)

# iteration with indexing
for i in np.ndenumerate(var3):
    print(i)