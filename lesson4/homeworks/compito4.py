import numpy as np

f1_path='lesson4/data/file_compito4.txt'
f2_path='lesson4/data/file_compito4_matrice.txt'

l1=[]
l2=[]

with open(f1_path,'r') as f_01:
    line1=f_01.readline()
    line2=f_01.readline()
    
    l1=[int(x) for x in line1.strip("\n").split(",")]
    l2=[int(x) for x in line2.strip("\n").split(",")]

#print(l1,l2)

matrix=np.zeros((3, 3), dtype=np.int16)
#print(matrix.dtype)
matrix[0][0]=(l1[0]+l2[0])
matrix[1][1]=(l1[1]+l2[1])
matrix[-1][-1]=(l1[2]+l2[2])


with open(f2_path,'w') as f_02:
    for line in matrix:
        line=str(line)
        line=line.strip("[").strip("]")

        f_02.write(line)
        f_02.write('\n')

#print(matrix)



