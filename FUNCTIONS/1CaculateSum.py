def calculateSum(a, b):
    sum = a + b
    print(sum)  # This will print the sum
    return sum

calculateSum(9, 29)  # Calls the first definition of calculateSum

def calculateSum(a, b):
    return a + b  # This overwrites the first definition

print(calculateSum(8, 40))  # Calls the second definition of calculateSum

def printHello():
    print("Hello")

printHello()  # Calls the definition of printHello

