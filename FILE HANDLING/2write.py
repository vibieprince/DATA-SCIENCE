f = open("FILE HANDLING/demo1.txt","w") # if demo1.txt won't exist, python will create it automatically and open it in write mode
f.write("Tomorrow i will learn JavaScript")
f.close()
f = open("FILE HANDLING/demo1.txt","a")
# f.write("Then i will learn React") # Since no newline character given, so this will be appended in the same line 
f.write("\nAnd then Node Js")
f.close()