from prettytable import PrettyTable
import json,requests

url_todos='https://jsonplaceholder.typicode.com/todos/'
url_users='https://jsonplaceholder.typicode.com/users/'
table=PrettyTable()

todos=requests.get(url_todos)
todos_json=todos.json()
users=requests.get(url_users)
users_json=users.json()

#print(todos_json)
#print(users_json)

for user in users_json:
    name=user['name']
    id=user['id']
    #print(userid)
    table.field_names=[name,"TODO"]
    


for todo in todos_json:
    userId=todo['userId']
    title=todo["title"]
    completed=todo["completed"]
    print(id)

    if id==userId and completed==True:
        table.add_row([title,"V"])
    else:
        table.add_row([title,"X"])

        
        #print(todo['userId'],todo["title"],todo["completed"])   
    print(table)
     

#print(table)



