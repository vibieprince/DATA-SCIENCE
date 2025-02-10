# Write the recursive function to print all elements in a list.
# Hint : Use list & index as parameters.

def printList(list,i):
    if(i==len(list)):
        return
    print(list[i])
    printList(list,i+1)

list = [1,2,3,4,5]
printList(list,0) # 1 2 3 4 5