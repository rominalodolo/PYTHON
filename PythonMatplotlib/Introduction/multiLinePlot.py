import matplotlib.pyplot as plt

x1 = [8,10,12,14,16]
y1 = [1,2,4,8,16]

x2 = [8,10,12,14,16]
y2 = [1,3,9,13,20]

x3 = [8,10,12,14,16]
y3 = [2,4,6,8,9]

plt.plot(x1, y1, 'ro--', label='students')
plt.plot(x2, y2, 'b^-', label='parents')
plt.plot(x3, y3, 'g-', label='visitors')
plt.legend(loc='best')

plt.title('Blue Collage Open Day')
plt.xlabel('Time of Arrival')
plt.ylabel('Foot Traffic')
plt.show()
