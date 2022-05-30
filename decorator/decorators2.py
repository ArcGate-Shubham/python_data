def data(dataset):
    def various():
        print("This is udaipur city")
        dataset()
    return various
@data
def value():
    print(" and also called a lake city")

@data
def value1():
    print(" and this is best for every one!!")

value()
value1()
