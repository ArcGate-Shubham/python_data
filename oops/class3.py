class student:
    def get(self):
        self.name = input("Enter name :")
        self.id = int(input("Enter id :"))
        self.address = input("Enter address :")

    def show(self):
        print("Details Here :")
        print("Name    :",self.name)
        print("ID      :",self.id)
        print("Address :",self.address)

list1 = []
num = int(input("Enter number for student :"))
for i  in range(num):
    s1 = student()
    s1.get()
    list1.append(s1)
print(list1)
for x in list1:
    x.show()
        