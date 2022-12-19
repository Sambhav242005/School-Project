import json
import model
import pandas as pd
import matplotlib.pyplot as plt
import item

def get_item():
    name=''
    item.get_list()
    with open('item.json','r') as f:
        data = json.load(f)
    select = int(input("Select One Item"))
    num = 0
    for i in data:
        if num == select:
            name = i['item_name']
    return name
file_path = 'order.json'
def get_order_all():
    if model.check(file_path) == False:
        with open(file_path,'r') as read_json:
            data = json.load(read_json)
        order_item_name=[]
        order_by=[]
        order_item=[]
        order_qty=[]
        order_amount=[]
        order_date=[]
        for row in data:
            order_item_name.append (row['order_item_name'])
            order_by.append(row['order_by'])
            order_item.append(row['order_item'])
            order_qty.append(row['order_qty'])
            order_amount.append(row['order_amount'])
            order_date.append(row['order_date'])
        dist = {'Order Name':order_item_name,
        'Order By':order_by,
        'Order Amount':order_amount,
        'Order Date':order_date}
        df = pd.DataFrame(dist)
        print(df)
def add_order():
    with open(file_path,'w') as write:
        name = input('\nEnter your order name ')
        by = input('\nEnter your order by ')
        item = get_item()
        qty = int(input('\nEnter your order Quantity '))
        amount = int(input('\nEnter your order Amount '))
        date = input('\nEnter your order date ')
        print()
    
        order ={
            "order_item_name":name,
            "order_by":by,
            "order_item":item,
            "order_qty":qty,
            "order_amount":amount,
            "order_date":date
        }
        if model.check(file_path)== False:
            with open(file_path,'r') as read_json:
                data = json.load(read_json)
            data.append(order)
            json.dump(data,write,indent=4)
        else:
            data = [order]
            json.dump(data,write,indent=4)
    
def get_order_of_name(name):
    if model.check(file_path) == False:
        Order_Name=[]
        Order_By=[]
        Order_Item=[]
        Order_Qty=[]
        Order_Amount=[]
        Order_Date=[]
        with open(file_path,'r') as read_json:
            data = json.load(read_json)
        for row in data:
            if row['order_by'] == name:
                Order_Name.append(row['order_item_name'])
                Order_By.append(row['order_by'])
                Order_Item.append(row['order_item'])
                Order_Qty.append(row['order_qty'])
                Order_Amount.append(row['order_amount'])
                Order_Date.append(row['order_date'])
        dist = {'Order Name':Order_Name,
        'Order By':Order_By,
        'Order Item':Order_Item,
        'Order Amount':Order_Amount,
        'Order Date':Order_Date
        }
        df = pd.DataFrame(dist)
        print(df)
        count = model.sum(Order_Amount)
        plt.plot(Order_Amount,Order_Item)
        plt.xlabel("Amount")
        plt.ylabel("Item Name")
        plt.title("Users Order & Amount")
        plt.show()
        print ( "\nOrder Total Amount: "+str(count)+"\n\n")
        print("------------------------------------------------")
def delete_order():
    if model.check(file_path) == False:
        get_order_all()
        select = int(input('\nSelect Order to Delete '))
        print("------------------------------------------------")
        new_order =[]
        with open(file_path,"r") as read:
            data = json.load(read)
        num =1    
        for i in data:
            if num != select:
                new_order.append(i)
            num = num + 1
        with open(file_path,'w') as write:
            json.dump(new_order, write)
            get_order_all()

def update_order():
    if model.check(file_path) == False:
        get_order_all()
        select = int(input('\nSelect Order to Edit '))
        dirt = {1:"Order Name",2:"Order Date",3:"Order By"
        ,4:"Order Quantity",5:"Order Amount"}
        model.show_list(dirt)
        select_med = int(input('Select Edit Method '))
        value = input('Enter your Edit Value ')
        print("------------------------------------------------")
        new_order =[]
        with open(file_path,"r") as read:
            data = json.load(read)
        num =1    
        for i in data:
            if num != select:
                new_order.append(i)
            else:
                order__item_name = i['order_item_name']
                order_by =i['order_by']
                order_item = i['order_item']
                order_qty = i['order_qty']
                order_amount = i['order_amount']
                order_date = i['order_date']
                if select_med == 1:
                    order__item_name = value
                elif select_med == 2:
                    order_date = value
                elif select_med == 3:
                    order_by = value
                elif select_med == 4:
                    order_qty = value
                elif select_med == 5:
                    order_amount = value
                order ={
                        "order_item_name":order__item_name,
                        "order_by":order_by,
                        "order_item":order_item,
                        "order_qty":order_qty,
                        "order_amount":order_amount,
                        "order_date":order_date
                        }
                new_order.append(order)
            num = num + 1
        with open(file_path,'w') as write:
            json.dump(new_order, write,indent=4)
            get_order_all()