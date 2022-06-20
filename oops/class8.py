import datetime
print("Welcome to Bank of Udaipur, Udaipur")
class Bank:
    minBalance = 1000
    def __init__(self,_balance):
        print("your current balance is 1000")
        self._balance = _balance
    
    def depositMoney(self):
        depositAmount = int(input("Enter Deposit Amount :"))
        if(depositAmount<=0):
            print("Amount should be greater than zero!!")
        else:
            self._balance = self._balance + depositAmount
            print("Updated Balnace is ",self._balance)
            x = datetime.date.today()
            print(x)

    def withdrawlMoney(self):
        withdrawlAmount = int(input("Enter withdrawl Amount :"))
        if(self._balance-withdrawlAmount < self.minBalance):
            print(f"Sorry, You can't withdraw money\nMinimum balance should be {self.minBalance}")
        else:
            self._balance = self._balance - withdrawlAmount
            print(self._balance)
            x = datetime.date.today()
            print(x)

    def stop(self):
        print("Thank you for visit in our Bank !!")

b = Bank(1000)
v=1
while(v):
    s = int(input("Enter 1 for Deposit\nEnter 2 for withrawal\nEnter 3 for stop :"))
    if(s==1):
        b.depositMoney()
    elif(s==2):
        b.withdrawlMoney()
    elif(s==3):
        b.stop()
        v=0
    else:
        print("This service not available")
        