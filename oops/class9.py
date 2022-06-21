class Product:
    def __init__(self,name,model,price):
        self.name  = name
        self.model = model
        self.price = price
list1 =[]
num = int(input("Enter number :"))
for x in range(num):
        P = Product("Honda","Baleno",524125)
        list1.append(P.__dict__)
print(list1)