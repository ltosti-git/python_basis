# matrix of lists
matrix=[]
l1=[1,2,3,4,5]
for i in range(len(l1)):
    line=[0] * len(l1)
    matrix.append(line)
print(matrix)