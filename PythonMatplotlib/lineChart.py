import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [2,4,6,8,14,16,4]

plt.plot(x, y, 'y^')
# To creat different types/ colors of lines b-. or r--  or y:  y^  ect.
# you can also specify line width   linewidth=4.0
plt.axis([0,5,0,10])
plt.xlabel("Horizontal Label")
plt.ylabel("Vertical Label")
plt.title("Line Chart")
plt.show()