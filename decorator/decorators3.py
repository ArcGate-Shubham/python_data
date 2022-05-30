list1=[]
list2=[]
def data(datavalue):
    
    def value():
        print("This is udaipur city")
        datavalue()
    return value

@data
def valuable():
        num = int(input("Enter number :"))
        for x in range(num):
            name = input("Enter name :")
            if(name.isalpha()):
                list1.append(name)
            elif(name.isnumeric()):
                list2.append(name)
            else:
                print("They are not reliable path!!")
        print(list1)
        print(list2)

@data
def show():
    name = input("Enter data :")
    if(name == 'ASCE'):
        list1.sort()
        print(list1)
    elif(name == 'DSCE'):
        list1.sort()
        list1.reverse()
        print(list1)
    elif(name == 'ASCE1'):
        list2.sort()
        print(list2)
    elif(name == 'DSCE1'):
        list2.sort()
        list2.reverse()
        print(list2)
    else:
        print("Data is not valid every list")

     
    
@data
def stop():
    print("Application stop now ")

v=1
while(v):
    s=int(input("Enter 1 for valuable\nEnter 2 for show\nEnter 3 for stop\n"))
    if(s==1):
        valuable()
        break
    elif(s==2):
        valuable()
        show()
    elif(s==3):
        s=stop()
        break
    else:
        print("This service not avialable this time!!")
