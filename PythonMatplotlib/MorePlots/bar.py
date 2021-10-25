import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

colors = [ '#FFC8ED', '#FFAAE3', '#FF90DA', '#FC65CA', '#FD34BB']

plt.bar(x1,y1,edgecolor='aqua',color=colors, linewidth=2)
plt.title('Bar Chart')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.show()

