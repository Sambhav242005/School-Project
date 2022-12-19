import json

with open('users.json','r') as file:
    data = json.load(file)
    name=''
    name = data['usersname']
    print(name)