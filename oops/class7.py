class college:
    def __init__(self):
        print("Welcome to Engineering College, Ajmer")

    def addstudent(self):
        self.name = input("Enter Name :")
        self.id = int(input("Enter id :"))
        self.contact = int(input("Enter contact :"))

    def showstudent(self):
        print("Student detail here :")
        print("Name   :",self.name)
        print("ID     :",self.id)
        print("Contact:",self.contact)

    def stop(self):
        print("Apllication stop now !!")


c1 = college()
list1 =[]
num = int(input("Enter number :"))
v=1
while(v):
    s = int(input("Enter 1 for addstudent :\nEnter 2 for showstudent :\nEnter 3 for stop :"))
    if(s==1):
        c1.addstudent()
    elif(s==2):
        c1.showstudent()
    elif(s==3):
        c1.stop()
        break
    else:
        print("This service not for this time!!")
    