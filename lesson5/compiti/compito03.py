from prettytable import PrettyTable
import requests

# do the requests and parsing in json
url_todos='https://jsonplaceholder.typicode.com/todos/'
url_users='https://jsonplaceholder.typicode.com/users/'

todos_json=requests.get(url_todos).json()
users_json=requests.get(url_users).json()

# get the datas and instantiate a table for each user 
for user in users_json:
    id=user['id']
    name=user['name']
    table=PrettyTable()
    table.field_names=[name,"TODO"]

    # get the todos and check the IDs to add rows for each user table
    for todo in todos_json:
        userId=todo['userId']
        title=todo["title"]
        completed=todo["completed"]
        
        if id==userId and completed==True:    
            table.add_row([title,"V"])
        
        if id==userId and completed==False:
            table.add_row([title,"X"])        
    
    #print all user tables 
    print(table)
     
