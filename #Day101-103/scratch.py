import json
import requests


response = requests.get('https://jsonplaceholder.typicode.com/todos')
response.text

todos = json.loads(response.text)

todos['completed']


todos_by_user  = {}

for todo in todos:
    if todo['completed']==True:
        try:
            todos_by_user[todo['userId']] += 1 
        except KeyError:
            todos_by_user[todo['userId']] = 1

top_users = sorted(todos_by_user.items(),key = lambda x: x[1],reverse = True)
max_complete = top_users[0][1]


users = []

for user, num_complete in top_users:
    if num_complete< max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)


