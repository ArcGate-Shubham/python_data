names=[]
for x in range(5):
    data = input("Enter value")
    if(data.isalpha()):
        names.append(data)
        
    else:
        print("This data is not alphabet")
print(names)