f = open("FILE HANDLING/demo1.txt","r+") # Here file willl not be created automatically if it doesn't exist
f.write("I am learning Python") # This will overwrite the content of the file from starting 
print(f.read())
f.close()
f = open("FILE HANDLING/demo.txt","a+")

print(f.read()) # does not prints anything as the cursor is at the end of the file
f.write("I am learning Python") # This will append the content of the file from the end
print(f.read()) # does not prints anything as the cursor is at the end of the file
f.close()