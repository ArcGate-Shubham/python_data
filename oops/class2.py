class Add:
    def get(self):
        self.a=int(input("Enter first Number  :"))
        self.b=int(input("Enter second Number :"))

    def add(self):
        self.c = self.a + self.b

    def show(self):
        print("Addition of",self.a,"and",self.b,"is",self.c)

a1 = Add()
a1.get()
a1.add()
a1.show()
