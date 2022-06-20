global Arcgate
class Machine:
    print("Welcome to our Refreshment system")
    def Tea(self):
        print("1 cup tea price is 10 rupees only")
        num = int(input("Enter number of tea :"))
        self.price = num * 10
        print(self.price)

    def Coffee(self):
        print("1 cup coffee price is 25 rupees only")
        num = int(input("Enter number of coffee :"))
        self.price = num * 25
        print(self.price)

    def stop(self):
        print("Application stop now!!")

M = Machine()
v=1
while(v):
    s = int(input("Enter 1 for Tea :\nEnter 2 for coffee :\nEnter 3 for stop :"))
    if(s==1):
        M.Tea()
        #break
    elif(s==2):
        M.Coffee()
        #break
    elif(s==3):
        v=M.stop()
    else:
        print("This service not available")
