## dictionary in json with key->value 

dictionary={"name":"Luca","surname":"nekhrun"}
dictionary["age"]=39
print(dictionary)
print(dictionary["name"])
print(type(dictionary))
print(type(dictionary["age"]))
print(len(dictionary))
print(dictionary.keys())
print(dictionary.values())


print("surname" in dictionary.keys())
print("surname" in dictionary.values())

print(dictionary.items())

for key,value in dictionary.items():
    print(key)
    print(value)
