import datetime
print("welcome to our Apllication!!")


class BankingSystem:
    updated_balance = 1000

    def __init__(self, balance):
        print("Your Updated Balance is 1000")
        self.balance = balance

    def deposit_amount(self):
        v = 1
        while(v):
            try:
                deposit = int(input("Enter deposit amount :"))
                v = 0
            except:
                print("Amount is given on always number !!")
            else:
                if(deposit <= 0):
                    print("amount should be greater than zero!!")
                else:
                    self.balance = self.balance + deposit
                    print(self.balance)
                    date = datetime.date.today()
                    print(date)

    def withdrawal_amount(self):
        v = 1
        while(v):
            try:
                withdrawal = int(input("Enter withdrwal amount :"))
                v = 0
            except:
                print("Amount is always given on number !!")
            else:
                if(self.balance - withdrawal < self.updated_balance):
                    print("minimum balance is always required")
                    print("1000 is minimum balance!!")
                else:
                    self.balance = self.balance - withdrawal
                    print(self.balance)
                    date = datetime.date.today()
                    print(date)

    def stop(self):
        print("Application stop now!!!")


b = BankingSystem(1000)
v = 1
while(v):
    try:
        switch_case_type = int(input("Enter 1 for deposit :\nEnter 2 for withdrawal :\nEnter 3 for stop :"))  
        if(switch_case_type == 1):
            b.deposit_amount()
        elif(switch_case_type == 2):
            b.withdrawal_amount()
        elif(switch_case_type == 3):
            b.stop()
            v=0
        else:
            print("This service is not available")
    except:
        print("data is always gives a number!!")
