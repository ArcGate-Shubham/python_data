class Person:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

    def add(self):
        self.name = input("Enter name :")
        self.id = int(input("Enter id :"))
        self.address = input("Enter address :")

    def show(self):
        print("Details here :")
        print("Name     :", self.name)
        print("ID       :", self.id)
        print("Address  :", self.address)


class student(Person):
    def addp(self):
        self.add()
        self.phone = int(input("Enter phone no. :"))

    def showp(self):
        self.show()
        print("Phone No.:", self.phone)

    def stop(self):
        print("Appllication stop now !!!")


p1 = student("shubham", 101, "bhopal")
v = 1
while(v):
    s = int(input("Enter 1 for addp :\nEnter 2 for showp :\nEnter 3 for stop :"))
    if(s == 1):
        p1.addp()
    elif(s == 2):
        p1.showp()
    elif(s == 3):
        p1.stop()
        v = 0
    else:
        print("This service not available for this time !!!")
        v = 0
