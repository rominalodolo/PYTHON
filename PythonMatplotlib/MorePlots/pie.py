import matplotlib.pyplot as plt

values = [16,18,4,8]
pielabels = ['Malibu', 'Barbie', 'Pink', 'Girly']
piecolors = ['#FFC8ED','#FFAAE3','#FF90DA','#FC65CA']
pieexplode = [0,0.1,0,0]

plt.pie(values, labels=pielabels,explode=pieexplode,colors=piecolors,startangle=0,shadow=True)
plt.title('Pink Pie Chart')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.legend(loc='best')
plt.show()
