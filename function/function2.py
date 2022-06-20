print("Welcome to our Application!!")

def data():
    list1 = ["Shubham","Kartik","Priya"]
    list2 = [12,13,14,15]
    num = int(input("Enter number :"))
    for x in range(num):
        name = input("Enter Name :")
        if(name in list1):
            print("Name is already present in this application")
        elif(name.isalpha()):
            list1.append(name)
        elif(name.isnumeric()):
            list2.append(name)
        else:
            print("number is already present in this list2")
    print(list1)
    print(list2)
data()
    