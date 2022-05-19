course =("java","python","Dotnet","c/c++","angular")
print(course)
name=input("Enter element name")
for x in range(len(course)):
    if(name == course[x]):
       print("Index are",x) 
    else:
        print("value is not present in this list")
