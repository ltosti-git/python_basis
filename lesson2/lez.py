# loops - dictionaries and lists - functions

# while loop: if true then run the code


##############################################################################################
##############################################################################################


# condition=True
# var=0

# while condition:
#     #print(f"{var}")
#     if var<10:
#         print("Ciao!")
#         var+=1
#     else:
#         condition=False

print("_______________________________\n\n\n")
print ("Welcome to the the Python door's hell!")
print("_______________________________\n\n\n")

sub_list=["asfdadf","jsnlgs","sdjpoi","opteirph"]
i=0
'''while i<len(sub_list):
    print(sub_list[i])
    i+=1'''

## somma due liste di eguale lunghezza

list1=[101,22,43,74,58]
list2=[31,242,453,92,67]

if len(list1) == len(list2):
    sumList=[]
    lenLists=len(list2)
    for i in range(lenLists):
        sumList.append(list1[i]+list2[i])
        #sumList.append(list1[i])
        #sumList.append(list2[i])
else:
    print("lists length are different, man.")

print(sumList)
    