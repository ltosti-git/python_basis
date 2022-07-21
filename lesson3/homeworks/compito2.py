def main():
    print("calls other functions")
    print("_______________________________________________\n")

    list_txt=["ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","stop"]
    res_rev=rev(list_txt)
    print(f"reverse list is:\n{res_rev}")

    res_is_positive=is_positive(3202)

    if res_is_positive == True or res_is_positive == False:
        print("is_positive function working out correctly")
    else:
        print("is_positive function not properly working")

    result_no_duplicate=no_duplicate(list_txt)
    print(result_no_duplicate)
    
    palindrome="Was it a car or a cat I saw"
    res_is_palindrome=is_palindrome(palindrome)
    print(f"This '{palindrome}' is a palindrome? {res_is_palindrome}")

    number=6
    result_fact=factorial(number)
    print(f"Factorial of {number} is: {result_fact}")

## get reverse of a list
def rev(list):
    rev_list=[]
    length_list=len(list)-1
    for i in range(length_list,-1,-1):
        rev_list.append(list[i])
    return rev_list

## check if a number positive or negative
def is_positive(n):
    
    if n<0:
        #print(f"Number {n} is negative!")       
        return False   
    else:
        #print(f"Number {n} is positive!")
        return True       

## remove duplicates in a list
def no_duplicate(list):
    set_list=[]
    for word in list:
        if word not in set_list:
            set_list.append(word)
    return set_list

## calculates a factorial of a number n!
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

## check if a string is palindrome
def is_palindrome(string):
    string=string.strip().lower().replace(" ","")
    rev_string=""
    length_string=len(string)-1
    for i in range(length_string,-1,-1):
        rev_string+=string[i]
    if string == rev_string:
        return True
    else:
        return False         


if __name__=="__main__":
    # try:
    print("\nmain foo")
    print("_______________________________________________\n")
    main()
    # except:
    #     print("troubles")