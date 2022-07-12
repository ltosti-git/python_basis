print("_______________________________\n\n\n")
print ("Welcome to the user register page of the online casinò software!")
maxRange=3
fullUserList=[]
userDictionary={}

for i in range(0,maxRange):
    nickname=input(f"Please, input the nickname of the user nr. {i+1}: ")
    age=int(input(f"Please, input the age of the user nr. {i+1}: "))
    gender=input(f"Please, input the gender of the user nr. {i+1}: ")
    
    if fullUserList==[]:
        print("if")
        userDictionary["nickname"]=nickname
        userDictionary["age"]=age
        userDictionary["gender"]=gender.capitalize()
    
        fullUserList.append(userDictionary)
        print(f"User nr {i+1} inserted!")
        userDictionary={}
    
    elif fullUserList!=[]:
        print("elif")
        print(fullUserList)
        while nickname in fullUserList:
            print("Error. Nickname already present!")
            nickname=input(f"Please, input the nickname of the user nr. {i+1}: ")
        
        userDictionary["nickname"]=nickname
        userDictionary["age"]=age
        userDictionary["gender"]=gender.capitalize()
        fullUserList.append(userDictionary)
        print(f"User nr {i+1} inserted!")
        userDictionary={}

    else:
        print("Something else goes wrong. Please, retry.")

print(fullUserList)
#print(len(fullUserList))

# for i in range(len(fullUserList)):
#     #print(fullUserList[i])
#     if fullUserList[i]["gender"]=="F":
#         females=[]
#         females.append(fullUserList[i]["gender"])
#         print(females)
# print(females.count("f"))

    

