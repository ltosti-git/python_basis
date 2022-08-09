'''
Modificare il Compito 1 in modo da chiedere di indovinare chi ha più fan e non chi ha più album. Aggiungere anche nuovi artisti e testare che le chiamate API funzionino.
'''

import json, requests, random

def get_fans(id):
    api_url="https://api.deezer.com/artist"
    response=requests.get(f"{api_url}/{id}").json()
    album_nr=response['nb_fan']
    return album_nr
    
ARTISTS_PATH='lesson6/data/artists.json'

with open(ARTISTS_PATH) as file:
    artists_dict=json.load(file)
    artists_name=artists_dict.keys()
keep_asking="Y"

while keep_asking.upper()=="Y":
    two_artists=random.sample(artists_name, 2)
    
    try:
        answer=input(f"Which artist has the most fans between {two_artists[0]} (1) e {two_artists[1]} (2)? ")
        
        if answer not in ["1","2"]:                
            raise Exception("You must digit just number 1 or number 2!")
            
        artist_id1=artists_dict[two_artists[0]]
        artist_id2=artists_dict[two_artists[1]]            
        
        artist01_fans=get_fans(artist_id1)
        artist02_fans=get_fans(artist_id2)

        solution="1" if artist01_fans > artist02_fans else "2" 
        
        feedback="Correct!" if answer==solution else "Not correct!"

        feedback+=f" First artist {two_artists[0]} has {artist01_fans}, while second one {two_artists[1]} has {artist02_fans}.\nDo you wanna continue (Y/n)?"

        keep_asking=input(feedback)

    except ValueError as type_error:
        print("You must digit an integer!")
    except Exception as exception:
        print(exception)
    