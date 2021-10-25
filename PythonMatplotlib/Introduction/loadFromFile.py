X = []
Y = []

with open('PythonMatplotlib/Introduction/values.txt','r') as myfile:
    for line in myfile:
        Y.append( int(line) )

X = list(range(0,len(Y)+1))
print(X)
print(Y)