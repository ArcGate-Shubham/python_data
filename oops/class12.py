from abc import ABC, abstractmethod


class data(ABC):
    @abstractmethod
    def states(self):
        print("This is  Rajasthan states")


class data1(data):
    def states(self):
        print("This is Delhi")


class data2(data):
    def states(self):
        print("This is Madhyapradesh")


d1 = data1()
d2 = data2()
v=1
while(v):
    s=int(input("Enter 1 for data1 :\nEnter 2 for data2 :\nEnter 3 for stop :"))
    if(s==1):
        d1.states()
    elif(s==2):
        d2.states()
    elif(s==3):
        print("Terminate our App!!")
        v=0
    else:
        print("This service can't available")
