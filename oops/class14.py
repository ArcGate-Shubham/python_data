import datetime
print("Welcome to Bank of Udaipur")
class Bank:
    __minvalue =  2000
    def __init__(self,balance):
        print("your updated balance is 1000")
        self.balance = balance

    def depositAmount(self):
        Deposit = int(input("Enter Deposit Amount :"))
        if(Deposit<0):
            print("Amount should be greater than 0")
        else:
            self.balance = self.balance + Deposit
            print(self.balance)
            x = datetime.date.today()
            print(x)

    def withdrawalAmount(self):
        Withdrawal = int(input("Enter withdrwal Amount :"))
        if(self.balance - Withdrawal<self.__minvalue):
            print("Mininum balance are required in Account!!")
        else:
            self.balance = self.balance - Withdrawal
            print(self.balance)
            x = datetime.date.today()
            print(x)


    def stop(self):
        print("Thank you for visit in Banking system")

b=Bank(1000)
v=1
while(v):
    s=int(input("Enter 1 for deposit amount :\nEnter 2 for Withdrawal amount :\nEnter 3 for stop :"))
    if(s==1):
        b.depositAmount()
    elif(s==2):
        b.withdrawalAmount()
    elif(s==3):
        b.stop()
        v=0
    else:
        print("This service not available for this banking system !!")
