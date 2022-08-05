from prettytable import PrettyTable
import json,requests

url_todos='https://jsonplaceholder.typicode.com/todos/'
url_users='https://jsonplaceholder.typicode.com/users/'


todos=requests.get(url_todos)
todos_json=todos.json()
users=requests.get(url_users)
users_json=users.json()

#print(todos_json)
#print(users_json)

for user in users_json:
    id=user['id']
    name=user['name']
    table=PrettyTable()
    table.field_names=[name,"TODO"]
    #print(table)

    for todo in todos_json:
        userId=todo['userId']
        title=todo["title"]
        completed=todo["completed"]
        
        if id==userId and completed==True:    
            table.add_row([title,"V"])
        
        if id==userId and completed==False:
            table.add_row([title,"X"])        
        
    print(table)
     
