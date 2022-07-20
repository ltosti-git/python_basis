def main():
    print("calls other functions")
    list_txt=["ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","stop"]
    res_rev=rev(list_txt)
    print(f"reverse list is:\n{res_rev}")

    res_is_positive=is_positive(3202)

    if res_is_positive == True or res_is_positive == False:
        print("is_positive function working out correctly")
    else:
        print("is_positive function not properly working")
    
    nList=[-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

    result_no_duplicate=no_duplicate(nList)
    print(result_no_duplicate)
    
    number=5
    result_fact=factorial(number)
    print(f"Factorial of {number} is: {result_fact}")


def rev(list):
    rev_list=[]
    length_list=len(list)-1
    for i in range(length_list,-1,-1):
        rev_list.append(list[i])
    return rev_list


def is_positive(n):
    
    if n<0:
        print(f"Number {n} is negative!")       
        return False   
    else:
        print(f"Number {n} is positive!")
        return True       

def no_duplicate(list):
    set_list=set()
    for i in range(len(list)):
        set_list.add(list[i])
    return set_list

# def factorial(n):
#     fact=1
#     for i in range(n,0,-1):
#         fact*=i        
#     return fact

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)



if __name__=="__main__":
    # try:
    print("main foo")
    main()
    # except:
    #     print("troubles")