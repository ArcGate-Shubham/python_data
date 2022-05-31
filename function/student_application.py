print("Welcome student login page")
student = []


def addstud():
    num = int(input("Enter number :"))
    for x in range(num):
        name = input("Enter name :")
        if(name in student):
            print("student is already Registered!!")
        else:
            student.append(name)
    print(student)


def showstud():
    name = input("Enter value :")
    if(name == 'ASCE'):
        student.sort()
        print(student)
    elif(name == 'DSCE'):
        student.sort()
        student.reverse()
        print(student)
    else:
        print("given data not valid !")


def stop():
    print("Application stop now")


v = 1
while(v):
    s = int(input("Enter 1 for addstud\nEnter 2 for showstud\nEnter 3 for stop\n"))
    if(s == 1):
        addstud()
    elif(s == 2):
        addstud()
        showstud()
    elif(s == 3):
        v = stop()
    else:
        print("This service not available ")
