def main():
    print("calls other functions")
    list_txt=["ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","stop"]
    #list_txt=["bene","?","si",".","tu","?","male"]
    rev(list_txt)

    num=-2
    print(is_positive(num))


def rev(list):
    rev_list=[]
    length_list=len(list)-1
    for i in range(length_list,-1,-1):
        rev_list.append(list[i])
    return print(rev_list)


def is_positive(n):
    
    if n<0:
        # print(f"Number {i} is negative!")
        return False       
    else:
        # print(f"Number {i} is positive!")       
        return True



if __name__=="__main__":
    try:
        print("main foo")
        main()
    except:
        print("troubles")