#list_txt=["ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","stop"]
list_txt=["ciao","pippo","ciao","pluto","paperino","topolino","paperino"]

nList=[-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

## Generate a list with numbers in a foo
# maxRange=6
# def create_list(num):
#     nlist=[]
#     for i in range(-5,num):
#         nlist.append(i)
#         nlist.append(i+1)
#     return nlist
# print(create_list(maxRange))

def rev(list):
    rev_list=[]
    length_list=len(list)-1
    for i in range(length_list,-1,-1):
        rev_list.append(list[i])
    return rev_list

res_rev=rev(nList)
print(res_rev)

def is_positive(n):
    for i in range(len(n)):
        #print(n[i])
        if n[i]<0:
            print(f"Number {n[i]} is negative!")
            #return False
        else:
            print(f"Number {n[i]} is positive!")       
            #return True

res_is_positive=is_positive(nList)
print(res_is_positive)

# for i in range(-10,10):
    
#     if i<0:
#         # print(f"Number {i} is negative!")
#         False       
#     else:
#         # print(f"Number {i} is positive!")       
#         True

# x = 50
# y = 20

# print(x % y)


def no_duplicate(list):
    # set_list=set()
    # for i in range(len(list)):
    #     set_list.add(list[i])
    set_list=[]
    for word in list:
        if word not in set_list:
            set_list.append(word)
    return set_list
    
result_no_duplicate=no_duplicate(list_txt)
print(result_no_duplicate)



number=10
# def factorial(n):
#     fact=1
#     for i in range(n,0,-1):
#         fact*=i        
#     print(fact)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

result_fact=factorial(number)
print(result_fact)

palindrome="kayak"
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

res_is_palindrome=is_palindrome(palindrome)
print(res_is_palindrome)







# sum_words=0
# for i in range(len(list_txt)):
#     if not ("," in list_txt[i] or "." in list_txt[i] or "!" in list_txt[i] or "?" in list_txt[i] or "stop" in list_txt[i]):    
#         sum_words+=1
#         #print(i)
# print(sum_words)

# txt="Ciao \t\"Enkk\", prova"
# print("Ciao" or "prova" in txt)


# txt2="Silicon Valley"
# print(txt2.split("i"))

# x="-".join(["code","is","ok"])
# x="-".join(txt2)
# print(x)