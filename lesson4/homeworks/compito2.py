f1_path='lesson4/data/file_03_1.txt'
f2_path='lesson4/data/file_03_2.txt'
f3_path='lesson4/data/file_03_3.txt'

def common_lines(file_01,file_02):
    f1_list=[]
    f2_list=[]
    f3_list=[]
    rev_f3_list=[]
    with open(file_01,'r') as f_01:
        f1_list=[word.strip('\n') for word in f_01.readlines()]
    with open(file_02,'r') as f_02:
        f2_list=[word.strip('\n') for word in f_02.readlines()]
    
    f3_list = [word for word in f1_list if word in f2_list]
    
    rev_f3_list=rev(f3_list)
    
    with open(f3_path,'w') as file_03:
        for line in rev_f3_list:
            file_03.write(line)
            file_03.write('\n')

    return file_03

## get reverse of a list
def rev(list=list):
    rev_list=[]
    length_list=len(list)-1
    for i in range(length_list,-1,-1):
        rev_list.append(list[i])
    return rev_list

common_lines(f1_path,f2_path)