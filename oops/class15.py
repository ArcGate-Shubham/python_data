v=1
while(v):
    try:
        age = int(input("Enter age :"))
        v=0
    except ValueError:
        print("This type of data is not valid ,try again!!")
    except:
        print("Invalid input")
    else:
        print("Given data is valid for any cases")
    finally:
        print("This data is any how condition run !!!")


if(age<20):
    print("your age is not valid for cast voting")
else:
    print("your age is valid for cast voting")
