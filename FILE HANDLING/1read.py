f = open("FILE HANDLING/demo.txt","r")
# data = f.read()

data = f.read(5) # read first 5 characters ---> I am
print(data)
print(type(data))

data = f.readline() # read first line but there's a catch----- since we have read first 5 characters at line 4, so it will start reading from 6th character. i.e ---> learning 
print(data)
f.close() # as a responsible programmer we should close the file after reading or writing the file.