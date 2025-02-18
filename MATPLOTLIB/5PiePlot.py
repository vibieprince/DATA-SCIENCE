# PIE PLOT
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ['c','c++','Java','Python']
# plt.pie(x)
# plt.show()

# plt.pie(x,labels=y)
# plt.show()

ex = [0.4,0.0,0.0,0.0]
c = ['r','b','g','y']
# plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.2f%%",shadow=True,radius=0.8,labeldistance=1.2)
# plt.show()

plt.pie(x,labels=y,explode=ex,autopct="%0.1f%%",shadow=True,startangle=270,textprops={"fontsize":10},counterclock=False,wedgeprops={"linewidth" : 4,"edgecolor":'m'},rotatelabels=True)
plt.title("Bar Chart")
# plt.legend(loc=3)
# plt.show()

# plt.pie([1])
# plt.show() # DOT PIE CHART

# DONUT PIE CHART
x1 = [40,52,65,63]
plt.pie(x,labels=y,radius = 1.5)
# plt.pie(x1,radius=0.8,colors=c)
plt.pie([1],colors='w') # RING PE CHART
plt.show()

plt.pie(x,labels=y,radius=1.5)
cr = plt.Circle(xy=(0,0),radius=1,facecolor='w')
plt.gca().add_artist(cr)
plt.show()  # RING PIE CHART