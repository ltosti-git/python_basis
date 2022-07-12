print("_______________________________\n\n\n")
print ("Welcome to the user register page of the online casinò software!\n\n")
maxRange=int(input("How many account do you want to insert today? "))
fullUserList=[]
userDictionary={}

for i in range(maxRange):
    nickname=input(f"Please, input the nickname of user nr. {i+1}: ")

    if fullUserList!=[]:
        for dict in fullUserList:
            if dict["nickname"]==nickname:
                print(f"Error. Nickname {nickname} already used!")
                nickname=input(f"Please, input the nickname of user nr. {i+1}: ")
    
    age=int(input(f"Please, input the age of user nr. {i+1}: "))
    gender=input(f"Please, input the gender of user nr. {i+1}: ").upper()
    games=input(f"Please, input the favourite games of user nr. {i+1}, separed by a comma: ").split(",")

    for j in range(len(games)):
        games[j]=games[j].strip()
    
    userDictionary={"nickname" : nickname, "age" : age, "gender" : gender, "games": games}
    fullUserList.append(userDictionary)
    print(f"User nr {i+1} inserted!")

print("\n Users insert completed! \n Now, some useful info:")
print("You inserted {} account/s.".format(len(fullUserList)))
age = []
gender = []

for user in fullUserList:
    age.append(user["age"])
    gender.append(user["gender"])

f = 0
m = 0
for one_gender in gender:
    if one_gender == 'F':
        f+=1
    if one_gender == 'M':
        m+=1

sum_age = 0
for one_age in age:
    sum_age += one_age


print(f"The mid age is: {sum_age/len(fullUserList)} years.")
print(f"You inserted {f} female accounts.")
print(f"You inserted {m} male accounts.")

min=age[0]
max=age[0]
for x in age:
    if x<min:
        min=x
    if x>max:
        max=x

print(f"The min age is: {min} years.")
print(f"The max age is: {max} years.")

gamesPrefs={}
for user in fullUserList:
    for game in user["games"]:
        #print(game)
        if game in gamesPrefs.keys():
            gamesPrefs[game]+=1
        else:
            gamesPrefs[game]=1

#print(gamesPrefs)

max=0
prefGame=""

for game,game_count in gamesPrefs.items():
    #print(game,game_count)
    if game_count > max:
        max=game_count
        prefGame=game

print(f"The users' favourite game is: {prefGame} with {max} occurrences.")

#print(fullUserList)