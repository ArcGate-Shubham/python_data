Add=[]
for x in range(5):
    data = input("Enter Value :")
    if(data.isnumeric()):
        Add.append(data)
    else:
        print("Value is not numeric")
print(Add)