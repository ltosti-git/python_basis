import json, requests, random

ARTISTS_PATH='lesson6/data/artists.json'

with open(ARTISTS_PATH) as file:
    artists_dict=json.load(file)
    #print(len(artists))

random_num1=random.randint(0,len(artists_dict)-1)
random_num2=random.randint(0,len(artists_dict)-1)
if random_num1 == random_num2:
    random_num2=random.randint(0,len(artists_dict)-1)

artists_list=[key for key in artists_dict.keys()]
    
try:
    question01=int(input(f"Chi ha pubblicato più album fra {artists_list[random_num1]} (1) e {artists_list[random_num2]} (2)? "))
    
    if question01 == 1 or question01 == 2:                
        artist_id1=artists_dict[artists_list[random_num1]]        
        artist_id2=artists_dict[artists_list[random_num2]]
    else:
        raise Exception("You must digit just number 1 or number 2!")
    
    api_url="https://api.deezer.com/artist"

    response01=requests.get(f"{api_url}/{artist_id1}").json()
    response02=requests.get(f"{api_url}/{artist_id2}").json()
    if response01['nb_album'] > response02['nb_album']:
        print(response01['name'])
    else:
        print(response02['name'])
        

    question02=input("Digit [Y] if you wanna continue: ")
    if question02 == "Y":
        print("Ok")
    else:
        raise Exception("You must digit [Y]")

except ValueError as type_error:
    print("You must digit an integer!")
except Exception as exception:
    print(exception)

    