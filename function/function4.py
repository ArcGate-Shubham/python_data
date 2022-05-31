print("Welcome to College of Engineering, Udaipur")
Roll_NO = []
Name = []


def Validation():
    num = int(input("Enter number :"))
    for x in range(num):
        id = int(input("Enter Roll no. :"))
        names = input("Enter name :")
        if(id in Roll_NO and names in Name):
            print("This student already in college data")
            return 1
        elif(id not in Roll_NO and names not in Name):
            Roll_NO.append(id)
            Name.append(names)

        else:
            print("This is not valid !!")
    print(Roll_NO)
    print(Name)


def show():
    roll = int(input("Enter number :"))
    data = input("Enter name :")
    if(roll in Roll_NO and data in Name):
        print("Login successfully")
        return 0
    elif(roll not in Roll_NO and data not in Name):
        print("Invalid data")
        return 1
    else:
        print("This is not valid")


def stop():
    print("This Application stop now!!")


c = 0
v = 1
while(v):
    s = int(input("Enter 1 for Validation\nEnter 2 for show\nEnter 3 for stop\n"))
    if(s == 1):
        Validation()
    elif(s == 2):
        Validation()
        if(c < 3):
            c += 1
            if(show()):
                break
        else:
            print("Please try again later")
    elif(s == 3):
        v = stop()
    else:
        print("This service not available !!")
