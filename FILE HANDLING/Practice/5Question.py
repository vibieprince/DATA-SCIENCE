# From a file containing numbers separated by commas,print the count of even numbers.

# with open("FILE HANDLING/Practice/practice.txt") as file:
#     data = file.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if data[i] == ",":
#             print(num)
#             num = ""
#         else:
#             num += data[i]

with open("FILE HANDLING/Practice/practice.txt","r") as f:
    data = f.read()
    print(data)
    count = 0
    nums = data.split(',')
    for val in nums:
        if(int(val)%2==0):
            count += 1

print(count)