num=[]
n = int(input("Enter a number"))
for x in range(n):
    data = input("Enter data")
    if(data.isnumeric()):
        num.append(data)
    else:
        print("Value is not valid ")

print(num)