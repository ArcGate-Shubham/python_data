list1=[]
list2=[]
list3=[]
num = int(input("Enter number :"))
for x in range(num):
    data = input("Enter data :")
    if(data.startswith('a')):
        list1.append(data)
    elif(data.endswith('t')):
        list2.append(data)
    else:
        list3.append(data)
print("list1 :",list1)
print("list2 :",list2)
print("list3 :",list3)
