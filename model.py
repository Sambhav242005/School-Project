import os
def show_list(data):
    for i in range(1,len(data)+1):
        print('\n{'+ str(i)+'} '+data[i]+'\n')
def sum(data):
    count = 0
    for i in range(len(data)):
        count += int(data[i])
    return count
def check(file):
    empty = True
    if (os.path.exists(file)):
        if( os.path.getsize(file) > 0):
            with open(file, 'r') as f:
                data = str(f.read())
                if(data.isspace() == False ):
                    empty = False
        else:
            print("File is Empty")
    else:
        print("File is Dont Exits")
    return empty