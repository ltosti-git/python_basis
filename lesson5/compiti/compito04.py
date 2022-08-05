import json, datetime, requests

PROVINCE_PATH="lesson5/data/province.json"
api_meteo="https://api.open-meteo.com/v1/"
call="forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
hours = datetime.datetime.now().strftime("%H")
#print(hours)

try:
    province_name=input("Digitare il nome della provincia: ")
   
    with open(PROVINCE_PATH, 'r') as p:
        p_json=json.load(p)
    
    if province_name.title() not in p_json.keys():
        raise Exception("Provincia non trovata!")

    for k,v in p_json.items():
        #print(k)
        if province_name.title() in k: 
            print("Provincia trovata!")
            lat=v['lat']
            lon=v['lon']
            res=requests.get(f"{api_meteo}forecast?latitude={lat}&longitude={lon}&hourly={hours}")
            # print(res)

            api_call=res.json()
            print(api_call)

except Exception as exception:
    print(exception)