# age=[23, 32, 36, 21]
# #print(eta[0])


# min=age[0]
# max=age[0]
# for x in age:
#     if x<min:
#         min=x
#     if x>max:
#         max=x
# print(min, max)

# nickname="pri"
# list=[{'nickname': 'pri', 'age': 21, 'gender': 'F'}, {'nickname': 'sec', 'age': 23, 'gender': 'M'}, {'nickname': 'ter', 'age': 24, 'gender': 'F'}]
# #print(list[0]["nickname"])

# for dict in list:
#     if dict["nickname"]==nickname:
#         print(f"nickname {nickname} già usato!")
#     else:
#         print("ok si può inserire")

# games=input(f"Please, input the favourite games of user nr., separed by a comma: ").split(",")

# for i in range(len(games)):
#     games[i]=games[i].strip()
# print(games)

users=[{'nickname': 'pri', 'age': 23, 'gender': 'F', 'games': ['blackjack', 'poker', 'slot']}, {'nickname': 'sec', 'age': 24, 'gender': 'M', 'games': ['slot', 'blackjack', 'roulette']}, {'nickname': 'ter', 'age': 34, 'gender': 'F', 'games': ['chess', 'blackjack', 'poker']}]

# print(users[0]["games"][0])
# print(users[1]["games"][0])
gamesPrefs={}
for user in users:
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
print(prefGame,max)