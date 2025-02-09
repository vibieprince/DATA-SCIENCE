# Write a function that replaces all occurences of "Java" with "Python" in above file.

def replaceJavaWithPython(file):
    with open(file,"r+") as f: # read + overwrite
        data = f.read()
    
    newData = data.replace("Java","Python")
    print(newData)

    with open(file,"w") as f:
        f.write(newData)

replaceJavaWithPython("FILE HANDLING/Practice/practice.txt")