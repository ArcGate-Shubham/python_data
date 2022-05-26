set1 = set()
set2 = set()
set3 = set()
num = int(input("Enter a number :"))
for x in range(num):
    data = input("Enter a value :")
    if(data.isnumeric()):
        set1.add(data)
    elif(data.isupper()):
        set3.add(data)
    elif(data.isalpha()):
        set2.add(data)
    else:
        print("Value is not valid")

print(set1)
print(set2)
print(set3)
