
def show_list(data):
    for i in range(1,len(data)+1):
        print('\n{'+ str(i)+'} '+data[i]+'\n')
def back_or_exit():
    print('\n\n')
    dist ={1:"Back To Main",2:"Exit"}
    show_list(dist)
    select = int(input("Select Option "))
    if(select==1):
        import main 
        main.main()
def sum(data):
    count = 0
    for i in range(len(data)):
        count += int(data[i])
    return count