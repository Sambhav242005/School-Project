import json
import model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_order_all():
    with open('order.json','r') as read_json:
        data = json.load(read_json)
        num =1
        for row in data:
            print('\nOrder Number '+' {'+ str(num)+'} '+'\n')
            print ( "\nOrder Name: "+row['order__item_name']+'\n')
            print ( "\nOrder By: "+row['order_by']+'\n')
            print ( "\nOrder Item: "+row['order_item']+'\n')
            print ( "\nOrder Qty: "+row['order_qty']+'\n')
            print ( "\nOrder Amount: "+row['order_amount']+'\n')
            print ( "\nOrder Date: "+row['order_date']+'\n\n')
            num = num+1
    model.back_or_exit()

def add_order():
    with open('order.json','r') as read_json:
        data = json.load(read_json)
    name = input('\nEnter your order name ')
    by = input('\nEnter your order by ')
    item = input('\nEnter your order item ')
    qty = input('\nEnter your order Quantity ')
    amount = input('\nEnter your order Amount ')
    date = input('\nEnter your order date ')
    print()

    order ={
        "order__item_name":name,
        "order_by":by,
        "order_item":item,
        "order_qty":qty,
        "order_amount":amount,
        "order_date":date
    }
    data.append(order)
    with open('order.json','w') as write:
        json.dump(data,write,indent=4)
    model.back_or_exit()
def get_order_of_name(name):
    list_amount =[]
    list_item=[]
    with open('order.json','r') as read_json:
        data = json.load(read_json)
        for row in data:
            if row['order_by'] == name:
                list_amount.append(row['order_amount'])
                list_item.append(row['order_item'])
                print ( "\nOrder Name: "+row['order__item_name']+"\n")
                print ( "\nOrder By: "+row['order_by']+"\n")
                print ( "\nOrder Item: "+row['order_item']+"\n")
                print ( "\nOrder Qty: "+row['order_qty']+"\n")
                print ( "\nOrder Amount: "+row['order_amount']+"\n")
                print ( "\nOrder Date: "+row['order_date']+"\n\n")
        count = model.sum(list_amount)
        plt.plot(list_amount,list_item)
        plt.xlabel("Amount")
        plt.ylabel("Item Name")
        plt.title("Users Order & Amount")
        plt.show()
        print ( "\nOrder Total Amount: "+str(count)+"\n\n")
    model.back_or_exit()
def delete_order():
    get_order_all()

    select = int(input('\nSelect Order to Delete '))

    new_order =[]

    with open("order.json","r") as read:
        data = json.load(read)

    num =1    
    for i in data:

        if (num != select):
            new_order.append(i)

        num = num + 1
    with open('order.json','w') as write:
        json.dump(new_order, write)
    model.back_or_exit()

def update_order():
    get_order_all()

    select = int(input('\nSelect Order to Edit '))

    dirt = {1:"Order Name",2:"Order Date",3:"Order By"
    ,4:"Order Quantity",5:"Order Amount"}

    model.show_list(dirt)

    select_med = int(input('Select Edit Method '))

    value = input('Enter your Edit Value ')

    new_order =[]

    with open("order.json","r") as read:
        data = json.load(read)

    num =1    
    for i in data:

        if (num != select):
            new_order.append(i)
        else:
            order__item_name = i['order__item_name']
            order_by =i['order_by']
            order_item = i['order_item']
            order_qty = i['order_qty']
            order_amount = i['order_amount']
            order_date = i['order_date']
            if(select_med == 1):
                order__item_name = value
            elif(select_med == 2):
                order_date = value
            elif(select_med == 3):
                order_by = value
            elif(select_med == 4):
                order_qty = value
            elif(select_med == 5):
                order_amount = value
            order ={
                    "order__item_name":order__item_name,
                    "order_by":order_by,
                    "order_item":order_item,
                    "order_qty":order_qty,
                    "order_amount":order_amount,
                    "order_date":order_date
                    }
            new_order.append(order)
        num = num + 1
    
    with open('order.json','w') as write:
        json.dump(new_order, write,indent=4)
    model.back_or_exit()