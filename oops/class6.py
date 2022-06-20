global counter
counter = 1
class Login:
    print("Welcome to our login page!!!")
    def __init__(self,username,password):
        global counter
        list1 = ["data","value"]
        list2 = ["int","float"]
        user = input("Enter value :")
        password = input("Enter password :")
        if(user in list1 and password in list2):
            print("valid user","Welcome of",counter)
        else:
            print("invalid user","Welcome of",counter)
        counter+=1

num =int(input("Enter number :"))        
for x in range(num):
        u1 =Login("data","float")
