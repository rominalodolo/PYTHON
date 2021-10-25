import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.plot(x1, y1, 'mo--', label='Makeup Students')
plt.legend(loc='best')
plt.title('All the Students from Lovelies Beauty Academy')
plt.xlabel('Classes')
plt.ylabel('Amount of Students')
plt.grid(which='major',linestyle='-', color='#FD34BB')
plt.minorticks_on()
plt.grid(which='minor',linestyle='--', color='#FFC8ED', alpha=0.5)
plt.show()
