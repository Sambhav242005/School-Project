import item
import model
import order
import user

def back():
    n = input("Please Enter Continue If Not Enter Anything ")
    if(n == "" or n.isspace()):
        try:
           main()
        except:
           print('Error ')
           main()
def item_list():
    item_menu ={1:"Add Item In List",
        2:"Get Item In List"
        ,3:"Edit Item In List"
        ,4:"Delete Item In List",5:"Back"}
        
    model.show_list(item_menu)
    menu_item = int(input('Select Option '))
    print()
    print("------------------------------------------------")
    if( menu_item==1):
        item.add_item()
    elif(menu_item==2):
        item.get_list()
    elif(menu_item==3):
        item.update_item()
    elif(menu_item==4):
        item.delete_item()
    else:
        main()

def order_item():
    order_menu = {1:"Get All Order List"
        ,2:"Get Order By Someone"
        ,3:"Add Order"
        ,4:"Delete Order"
        ,5:"Update Order"
        ,6:"Back"}
        
    model.show_list(order_menu)

    menu_order = int(input('Select Option '))
    print()
    print("------------------------------------------------")
    if(menu_order ==1):
        order.get_order_all()
    elif(menu_order ==2):
        name = input('Enter Name Which Show Order ')
        order.get_order_of_name(name)
    elif(menu_order ==3):
        order.add_order()  
    elif(menu_order ==4):
        order.delete_order()
    elif(menu_order ==5):
        order.update_order()
    else:
        main() 

def users():
    add_dist = {1:'Get Users Data',
        2:"Enter Users Data",3:"Delete User Data"
        ,4:"Update User Data",5:"Back"}
    
    model.show_list(add_dist)
    
    menu_add = int(input('Select Option'))
    
    print()
    print("------------------------------------------------")
    if(menu_add == 1):
        user.get_user()
        
    elif(menu_add == 2):
        user.add_user()
    
    elif(menu_add == 3):
        user.delete_user()    
    elif(menu_add == 4):
        user.update_user()
    else:
        main()

def main():
    
    dist = {1:'Users',2:'List Order',
    3:'List Of Item',4:'Adout',5:"Exit"}


    model.show_list(dist)

    menu = int(input('Select Option '))
    print("------------------------------------------------")
    if(menu == 1):
        users()
        back()
    elif(menu == 2):
        order_item()
        back()
    elif(menu == 3):
        item_list()
        back()
    elif( menu==4):
        print()
        print()
        print("\nMade By Sambhav\n")
        back()
    
    
    
main()
