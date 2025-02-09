# Create a new file practice.txt using python. Add the following data in it.
# Hi everyone
# we are learning File I/O 
# using Java.
# I like programming in Java.

# f = open("FILE HANDLING/Practice/practice.txt","w")
# f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
# f.close()

with open("FILE HANDLING/Practice/practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Python.\nI like programming in Python.")