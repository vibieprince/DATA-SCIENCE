# SAVEFIG
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,3,6,4]

plt.plot(x,y,color='r')
plt.savefig("line",dpi=2000,facecolor='g',transparent=True,bbox_inches="tight") # or .jpg/.pdf
plt.show()