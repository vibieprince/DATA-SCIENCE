# Write a recursive function to calculate the sum of first n natural numbers.

def sumN(n):
    if(n==0):
        return 0
    return n+sumN(n-1)

print(sumN(5)) # 15