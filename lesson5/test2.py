## TEST compito 04
import json, datetime, requests

PROVINCE_PATH="lesson5/data/province.json"
api_meteo="https://api.open-meteo.com/v1/"
#call="forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&hourly=apparent_temperature&timezone=CET"
hour = int(datetime.datetime.now().strftime("%H"))

# get user input and check if it exists in loaded json file
try:
    province_name=input("Digitare il nome della provincia: ")
   
    with open(PROVINCE_PATH, 'r') as p:
        p_json=json.load(p)
    
    if province_name.title() not in p_json.keys():
        raise Exception("Provincia non trovata!")

    # loop in json, checking the province name and getting lat and lon
    for k,v in p_json.items():
  
        if province_name.title() in k: 
            print("Provincia trovata!")
            lat=v['lat']
            lon=v['lon']

            # request to api with obtained datas and parsing response in json
            api_call=requests.get(f"{api_meteo}forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&hourly=apparent_temperature&timezone=CET").json()

            # print requested infos
            time=api_call["hourly"]["time"][hour]
            temp=api_call["hourly"]["temperature_2m"][hour]
            app_temp=api_call["hourly"]["apparent_temperature"][hour]
            print(f"La temperatura alle ore {hour}: {temp} °C\nLa temperatura percepita alle ore {hour}: {app_temp} °C")
           

except Exception as exception:
    print(exception)