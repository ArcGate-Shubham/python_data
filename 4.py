v=True
while(v):
    data = input("Enter value :")
    if(data.islower()):
        print("Success")
        v=False
    else:
        print("Please, Re-Enter data")