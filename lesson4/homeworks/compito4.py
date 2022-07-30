#import numpy as np

f1_path='lesson4/data/file_compito4.txt'
f2_path='lesson4/data/file_compito4_matrice.txt'

l1=[]
l2=[]
matrix=[]

with open(f1_path,'r') as f_01:
    line1=f_01.readline()
    line2=f_01.readline()
    
    l1=[int(x) for x in line1.strip("\n").split(",")]
    l2=[int(x) for x in line2.strip("\n").split(",")]

#print(l1,l2)

#matrix=np.zeros((len(l1), len(l2)), dtype=np.int16)
#print(matrix.dtype)
# matrix[0][0]=(l1[0]+l2[0])
# matrix[1][1]=(l1[1]+l2[1])
# matrix[-1][-1]=(l1[2]+l2[2])

# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if i == j:
#             matrix[i][i]=l1[i]+l2[i]

for i in range(len(l1)):
    line=[0] * len(l1)
    line[i]=l1[i]+l2[i]
    matrix.append(line)
#print(matrix)

# for line in matrix:
#     for x in line:
#         line=str(x)
#         print(line)

with open(f2_path,'w') as f_02:
    for line in matrix:
        f_02.write(" ".join([str(x) for x in line]))
        f_02.write('\n')

#print(matrix)



