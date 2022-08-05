from prettytable import PrettyTable
import json,requests

url_todos='https://jsonplaceholder.typicode.com/todos/'
url_users='https://jsonplaceholder.typicode.com/users/'
#table=PrettyTable()

todos=requests.get(url_todos)
todos_json=todos.json()
users=requests.get(url_users)
users_json=users.json()

#print(todos_json)
#print(users_json)
names={}
for user in users_json:
    id=user['id']
    name=user['name']
    names[name]=id
#print(len(names))


for k,v in names.items():    
    #print(names[k])

    for todo in todos_json:
        userId=todo['userId']
        title=todo["title"]
        completed=todo["completed"]
        table=PrettyTable()
        for i in range(len(names)):
            
            table.field_names=[k,"TODO"]
            if names[k]==userId and completed==True:    
                #print(userId)
                #print(completed)
                table.add_row([title,"V"])
            if names[k]==userId and completed==False:
                table.add_row([title,"X"])        
        
    print(table)
     
