list_txt=["ciao","come","stai",",","tutto","bene","?","si","grazie",".","tu","?","non","male",".","stop"]
#list_txt=["bene","?","si",".","tu","?","male"]

def rev(list):
    rev_list=[]
    length_list=len(list)-1
    for i in range(length_list,-1,-1):
        rev_list.append(list[i])
    return print(rev_list)

#rev(list_txt)

for i in range(-10,10):
    
    if i<0:
        # print(f"Number {i} is negative!")
        False       
    else:
        # print(f"Number {i} is positive!")       
        True

# x = 50
# y = 20

# print(x % y)




















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