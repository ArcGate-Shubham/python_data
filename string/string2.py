list1 = []
list2 = []
list3 = []
list4 = []
num=int(input("Enter number fot append in a list element :"))
for x in range(num):
    value = input("Enter data :")
    if(value.isnumeric()):
        list1.append(value)
    elif(value.isdecimal()):
        list2.append(value)
    elif(value.islower()):
        list3.append(value)
    elif(value.isupper()):
        list4.append(value)
    else:
        print("Value is not valid")

print(list1)
print(list2)
print(list3)
print(list4)
