class Person:
    def __init__(self):
        print("Person data is upto date")

    def add(self):
        self.Rollno = int(input("Enter roll no. :"))
        self.name = input("Enter name :")
        self.Branch = input("Enter Branch :")
        self.address = input("Enter Address :")
        self.Mobile = int(input("Enter Mobile no."))
    
    def show(self):
        print("Person Details here :-")
        print("Roll NO.   :",self.Rollno)
        print("Name       :",self.name)
        print("Branch     :",self.Branch)
        print("Address    :",self.address)
        print("Mobile     :",self.Mobile)

p1= Person()
p1.add()
p1.show()

