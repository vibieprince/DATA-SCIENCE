import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,5,6,8,3]

# plt.stem(x,y)
# plt.show()

plt.stem(x,y,linefmt=":",markerfmt="or",bottom=2,basefmt='g',label="Python",orientation="horizontal") # +r
plt.legend()
plt.show()