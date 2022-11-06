import json
import model


def add_item():
    with open('item.json','r') as read:
        data = json.load(read) 
    name = input('\nName Item ')
    type = input('\nType Item ')
    company = input('\nItem Company ')
    date = input('\nItem Date ')
    print()
    item = {
        'item_name': name,
        'item_type':type,
        'item_company':company,
        'item_date':date
    }
    data.append(item)
    with open('item.json','w') as write:
        json.dump(data,write,indent=4)
    model.back_or_exit()
def get_list():
    with open('item.json','r') as read:
        data = json.load(read)
        num =1
        for item in data:
            print("\nItem Number : "+' {'+ str(num)+'} '+'\n')
            print("\nItem Name : "+ item['item_name']+'\n')
            print("\nItem Type : "+ item['item_type']+'\n')
            print("\nItem Company : "+ item['item_company']+'\n')
            print("\nItem Date : "+ item['item_date']+'\n')
            num = num +1
    model.back_or_exit()
def delete_item():

    get_list()

    with open('item.json','r') as read:
        data = json.load(read)
    
    select = int(input('\nSelect Item To Delete '))

    new_data = []
    num=1 

    for i in data:

        if(num != select):
            new_data.append(i)
        num = num +1
    
    with open('item.json','w') as write:
        json.dump(new_data, write,indent=4)
    model.back_or_exit()
def update_item():

    get_list()

    with open('item.json','r') as read:
        data = json.load(read)
    
    select = int(input('\nSelect Item To Delete '))
    print()

    dirt = {1:"Edit Item Name",2:"Edit Company Name ",3:"Edit Date",4:"Edit Type"}

    model.show_list(dirt)

    method = int(input('\nEdit Item About ' ))
    value = input('\nEdit Value')

    new_data = []
    num=1 

    for i in data:

        if(num != select):
            new_data.append(i)
        else:
            item_name = i['item_name']
            item_type = i['item_type']
            item_company = i['item_company']
            item_date = i['item_date']
            if(method == 1):
                item_name = value
            elif(method == 2):
                item_company = value
            elif(method == 3):
                item_date = value
            elif(method == 4):
                item_type = value
            item = {
            'item_name': item_name,
            'item_type':item_type,
            'item_company':item_company,
            'item_date':item_date
            }
            new_data.append(item)

        num = num +1
    
    with open('item.json','w') as write:
        json.dump(new_data, write,indent=4)
    model.back_or_exit()