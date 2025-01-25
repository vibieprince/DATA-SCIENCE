import numpy as np
# var = np.random.rand()
var = np.random.rand(4) #RAND
print(var) # the function is used to generate a random value between 0 to 1

var1 = np.random.rand(2,5)
print(var1) # the function is used to generate a random value close to zero. This may return positive or negative numbers as well

var2 = np.random.randn(5) #RANDN
print(var2) # the function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half-open interval (0,0,1,0)

var3 = np.random.ranf(4) #RANF
print(var3) # the function is used to generate a random number between a given range.

var4 = np.random.randint(10,20,5) #RANDINT (min,max,size)
print(var4)