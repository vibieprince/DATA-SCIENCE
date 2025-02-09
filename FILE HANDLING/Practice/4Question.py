# Write a function to find in which line of the file does the word "learning" occur first. PRint -1 if word not found.

def findOccurence(file):
    data = True
    line = 1
    with open(file,"r") as f:
        while data:
            data = f.readline()
            if "programming" in data:
                return line
            line += 1
    return -1
    
print(findOccurence("FILE HANDLING/Practice/practice.txt"))