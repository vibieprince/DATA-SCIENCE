# Write a function to find the factorial of n. (n is the parameter)

def findFactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

findFactorial(6)