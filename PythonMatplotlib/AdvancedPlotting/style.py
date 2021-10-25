import matplotlib.pyplot as plt

plt.style.use('seaborn-deep')
print(plt.style.available)

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.bar(x1,y1)
plt.title('Seaborn-deep Theme')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.show()
