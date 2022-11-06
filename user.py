import json
import datetime
import model


def get_user():
    file_path = 'users.json'
    with open(file_path, 'r') as read:
        data = json.load(read)
    
    num =1

    for i in data:
        print("\nUsername Number "+ ' {'+ str(num)+'} \n')
        print("\nUsersname :"+i['usersname']+'\n')
        print("\nEmail :"+i['email']+'\n')
        print("\nDate :"+i['date']+'\n\n')
        num = num + 1
    model.back_or_exit()

def add_user():
    file_path = 'users.json'
    with open(file_path, 'r') as read:
       data = json.load(read)

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
        data.append(users)
        json.dump(data,write_file,indent=4)
    model.back_or_exit()

def delete_user():
    get_user()
    new_data = []
    delete = int(input("\nSelect UserName To Delete "))
    with open('users.json','r') as read:
        data = json.load(read)
    num =1
    for i in data:
        if(num != delete):
            new_data.append(i)
        num = num + 1
    with open('users.json','w') as write:
        json.dump(new_data, write,indent=4)
    model.back_or_exit()
def update_user():
    get_user()
    new_data = []

    user_to_edit = int(input('Enter Users To Edit Number: '))
    
    dist = {1:"Edit Usersname",2:"Edit Email" }

    model.show_list(dist)

    select = int(input("\nSelect Option "))

    edit = input("\nEdit Valuse ")


    with open('users.json','r') as read:
        data = json.load(read)

    

    num =1
    for i in data:
        if(num != user_to_edit):
            new_data.append(i)
        else:
            usersname = i['usersname']
            email =i['email']
            if(select == 1):
               username = edit 
            elif(select ==2):
                email = edit
            edit_user = {
                    "usersname":usersname,
                    "email":email,
                    "date":i['date']
                }
            new_data.append(edit_user)
        num = num + 1
    with open('users.json','w') as write:
        json.dump(new_data, write,indent=4)
    model.back_or_exit()
