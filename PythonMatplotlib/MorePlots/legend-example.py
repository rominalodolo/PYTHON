import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]
y2 = [1,1,2,3,5]

plt.plot(x1, y1, 'mo-', label='students')
plt.plot(x1, y2, 'y^-', label='teachers')

plt.subplots_adjust(left=0.3, bottom=0.3)
plt.legend(bbox_to_anchor=(-0.15, 0.17), loc='best')

plt.title('School Attendance during Covid')
plt.xlabel('Days')
plt.ylabel('Total number pressent')
plt.grid(True)
plt.show()
