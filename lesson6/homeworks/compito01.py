import json, requests, random

def get_albums(id):
    api_url="https://api.deezer.com/artist"
    response=requests.get(f"{api_url}/{id}").json()
    album_nr=response['nb_album']
    return album_nr
    
ARTISTS_PATH='lesson6/data/artists.json'

with open(ARTISTS_PATH) as file:
    artists_dict=json.load(file)
    artists_name = artists_dict.keys()
keep_asking="Y"

while keep_asking.upper()=="Y":
    two_artists=random.sample(artists_name, 2)
    
    try:
        answer=input(f"Which has released the most albums between {two_artists[0]} (1) e {two_artists[1]} (2)? ")
        
        if answer not in ["1","2"]:                
            raise Exception("You must digit just number 1 or number 2!")
            
        artist_id1=artists_dict[two_artists[0]]
        artist_id2=artists_dict[two_artists[1]]
            
        
        artist01_albums=get_albums(artist_id1)
        artist02_albums=get_albums(artist_id2)

        solution="1" if artist01_albums > artist02_albums else "2" 
        
        feedback="Correct!" if answer==solution else "Not correct!"

        feedback+=f" First artist {two_artists[0]} have {artist01_albums}, while second one {two_artists[1]} have {artist02_albums}.\nDo you wanna continue (Y/n)?"

        keep_asking=input(feedback)

    except ValueError as type_error:
        print("You must digit an integer!")
    except Exception as exception:
        print(exception)

    