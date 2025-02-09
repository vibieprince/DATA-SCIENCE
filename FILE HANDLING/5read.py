with open("FILE HANDLING/demo1.txt","r") as f:
    data = f.read()
    print(data)

with open("FILE HANDLING/demo.txt","w") as f:
    f.write("New data")