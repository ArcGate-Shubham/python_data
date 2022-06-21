class Person:
    def __init__(self,name,address,id):
        print("This is student application")
        self.name    = name
        self.address = address
        self.id      = id
list1 = []
num = int(input("Enter Number :"))
for x in range(num):
        p1 = Person('shubham','bhopal',101)
        print(p1.name)
        print(p1.address)
        print(p1.id)
