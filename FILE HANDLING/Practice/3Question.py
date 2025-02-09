# Search if the word "learning" exists in the file or not
with open("FILE HANDLING/Practice/practice.txt","r") as file:
    data = file.read()
    if(data.find("learning")!=-1):
        print("Found")
    else:
        print("Not Found")