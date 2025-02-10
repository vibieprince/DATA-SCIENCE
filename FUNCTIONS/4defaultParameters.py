def calculateProduct(a=1,b=1): 
    print(a*b)
    return a*b

calculateProduct() # 1
calculateProduct(6,7) # 42


def calculateProd(a,b=3): #default paramters always by end
    print(a*b)
    return a*b

calculateProd(5) #15
calculateProd(5,4) #20