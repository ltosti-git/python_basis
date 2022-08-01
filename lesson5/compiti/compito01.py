import json

FILE_PATH='lesson5/data/01_data.json'

with open(FILE_PATH,'r') as f:
    data=json.load(f)
#     email=[]
# for i in range(len(data)):        
#     email.append(data[i]['email'])
# emails="\n".join([x for x in email])
# print(f"the mail are the followin':\n{emails}")

for index in data:
    print(index['email'])

email = "hollandoliver@electonic.com"
for index in data:
    if index['email']==email:
        print(len(index['friends']))