class Person:
    def addstudent(self):
        self.name = input("Enter Name :")
        self.id   = int(input("Enter id :"))

    def showstudent(self):
        print("Name      :",self.name)
        print("ID        :",self.id)

class student(Person):
    def addstudentU(self):
        super().addstudent()
        self.address = input("Enter Address :")

    def showstudentU(self):
        super().showstudent()
        print("Address   :",self.address)

s1 = student()
s1.addstudentU()
s1.showstudentU()