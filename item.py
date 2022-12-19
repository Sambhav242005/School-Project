import json
import model
import pandas as pd

file_path = 'item.json'

def add_item():
    with open(file_path,'w') as write:
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
        if model.check(file_path):
            data = [item]
            json.dump(data, write,indent=4)
        else:
            with open(file_path,'r') as read:
               data = json.load(read)
            data.append(item)
            json.dump(data,write,indent=4)
def get_list():
    if model.check(file_path) == False:
        with open(file_path,'r') as read:
            data = json.load(read)
        Item_Name=[]
        Item_Type=[]
        Item_Company=[]
        Item_Date=[]
        for item in data:
            Item_Name.append(item['item_name'])
            Item_Type.append(item['item_type'])
            Item_Company.append(item['item_company'])
            Item_Date.append(item['item_date'])
        dist= {
            'Item Name':Item_Name,
            'Item Type': Item_Type,
            'Item Company':Item_Company,
            'Item Date':Item_Date
        }
        df = pd.DataFrame(dist)
        print(df)
def delete_item():
    if model.check(file_path) == False:
        get_list()
        with open(file_path,'r') as read:
            data = json.load(read)
        select = int(input('\nSelect Item To Delete '))
        new_data = []
        num=1 
        for i in data:
            if num != select:
                new_data.append(i)
            num = num +1
        with open(file_path,'w') as write:
            json.dump(new_data, write,indent=4)
            get_list()
def update_item():
    if model.check(file_path) == False:
        get_list()
        with open(file_path,'r') as read:
            data = json.load(read)
        select = int(input('\nSelect Item To Delete '))
        print("\n------------------------------------------------------")
        dirt = {1:"Edit Item Name",
        2:"Edit Company Name ",
        3:"Edit Date",4:"Edit Type"}
        model.show_list(dirt)
        method = int(input('\nEdit Item About ' ))
        value = input('\nEdit Value')
        new_data = []
        num=1 
        for i in data:
            if num != select:
                new_data.append(i)
            else:
                item_name = i['item_name']
                item_type = i['item_type']
                item_company = i['item_company']
                item_date = i['item_date']
                if method == 1:
                    item_name = value
                elif method == 2:
                    item_company = value
                elif method == 3:
                    item_date = value
                elif method == 4:
                    item_type = value
                item = {
                'item_name': item_name,
                'item_type':item_type,
                'item_company':item_company,
                'item_date':item_date
                }
                new_data.append(item)
    
            num = num +1
        
        with open(file_path,'w') as write:
            json.dump(new_data, write,indent=4)