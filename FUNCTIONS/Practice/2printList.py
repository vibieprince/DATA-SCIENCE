# Write a function to print the elements of a list in a single line. (list is the parameter)


cities = ["Delhi","Mumbai","Kolkata","Chennai","Bangalore"]
heroes = ["thor","ironman","captain america","black widow","hulk","spiderman"]


def printList(list):
    for i in list:
        print(i,end=" ")
    
printList(heroes)