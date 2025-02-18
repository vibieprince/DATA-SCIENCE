# BOX & WHISKEY PLOT
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60,70,120,200]
# plt.boxplot(x)
# plt.show()

# plt.boxplot(x,notch=True,vert=True,widths=0.2,tick_labels=["Python"],patch_artist=False,showmeans=True,whis=4)
# plt.show()

x = [10,20,30,40,50,60,70,120]
# plt.boxplot(x,tick_labels=["Python"],sym="g+",boxprops=dict(color='r'),capprops=dict(color='b'),whiskerprops=dict(color='g'),flierprops=dict(markeredgecolor='y'))
# plt.show()

x1 = [10,20,40,50,30,60,90]
y = [x,x1]
plt.boxplot(y,tick_labels=["Python","c++"],showmeans=True,sym='g+',boxprops=dict(color='r'),capprops=dict(color='b'),whiskerprops=dict(color='g'))
plt.show()