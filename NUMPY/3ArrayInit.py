import numpy as np
x = [1,2,3,4]
y = np.array(x)
print(y)

y = np.array([1,2,3,4])
print(y)
print(type(y))

l = []
for i in range(1,5):
    num = int(input("Enter number: "))
    l.append(num)

print(l)
print(y.ndim)
z = np.array([[1,2,3],[4,5,6]])
print(z)
print(z.ndim)

# multi-dimensional array
m = np.array([1,3,4,66,43],ndmin=10)
print(m)