import json
import datetime
import model
import pandas as pd

file_path = 'users.json'
def get_user():
    if model.check(file_path) == False:
        with open(file_path, 'r') as read:
            data = json.load(read)
        usersname=[]
        email =[]
        date =[]
        for users in data:
            usersname.append(users['usersname'])
            email.append(users['email'])
            date.append(users['date'])
        dist={
            'Username': usersname,
            'Email': email,
            'Date': date
        }
        df = pd.DataFrame(dist)
        print (df)
def add_user():
    with open(file_path, 'w') as write_file:
    
        name = input('Enter Username ')
        email = input('\nEnter Email ')
        print()
        date = str(datetime.datetime.now())
        users ={
            'usersname':name,
            'email':email,
            'date':date
        }
        if model.check(file_path):
            data = [users]
            json.dump(data,write_file,indent=4)
        else:
            with open(file_path, 'r') as read:
                data = json.load(read)
            data.append(users)
            json.dump(data,write_file,indent=4)

def delete_user():
    if model.check(file_path) == False:
        get_user()
        new_data = []
        delete = int(input("\nSelect UserName To Delete "))
        with open(file_path,'r') as read:
            data = json.load(read)
        num =1
        for i in data:
            if num != delete:
                new_data.append(i)
            num = num + 1
        with open(file_path,'w') as write:
            json.dump(new_data, write,indent=4)
def update_user():
    if model.check(file_path) == False:
        get_user()
        new_data = []
        user_to_edit = int(input('Enter Users To Edit Number: '))
        dist = {1:"Edit Usersname",2:"Edit Email" }
        model.show_list(dist)
        select = int(input("\nSelect Option "))
        edit = input("\nEdit Valuse ")
        with open(file_path,'r') as read:
            data = json.load(read)
        num =1
        for i in data:
            if num != user_to_edit:
                new_data.append(i)
            else:
                usersname = i['usersname']
                email =i['email']
                if select == 1:
                   usersname = edit 
                elif select ==2:
                    email = edit
                edit_user = {
                        "usersname":usersname,
                        "email":email,
                        "date":i['date']
                    }
                new_data.append(edit_user)
            num = num + 1
        with open(file_path,'w') as write:
            json.dump(new_data, write,indent=4)
    