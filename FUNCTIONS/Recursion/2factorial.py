def findFact(n):
    if(n==0):
        return 1
    return n*findFact(n-1)

print(findFact(5)) # 120