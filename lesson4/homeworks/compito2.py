## get file path
f1_path='lesson4/data/file_03_1.txt'
f2_path='lesson4/data/file_03_2.txt'
f3_path='lesson4/data/file_03_3.txt'

## define a function with two args
def reverse_common_lines(file_01,file_02):
    f1_list=[]
    f2_list=[]
    f3_list=[]

    ## read from the two file and lines in two lists
    with open(file_01,'r') as f_01:
        f1_list=[word.strip('\n') for word in f_01.readlines()]
    with open(file_02,'r') as f_02:
        f2_list=[word.strip('\n') for word in f_02.readlines()]

    ## insert the common words in the third list and reverse it
    f3_list = [word for word in f1_list if word in f2_list]
    f3_list.reverse()
    
    ## write the third list in the third file and return le third list
    with open(f3_path,'w') as f_03:
        f_03=[f_03.write(line) and f_03.write('\n') for line in f3_list]

    return f_03

reverse_common_lines(f1_path,f2_path)