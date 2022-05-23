print("Welcone in our login form")
username = ["Python"]
password = ["Shubham"]
def login():
    user     = input("Enter username :")
    passw    = input("Enter password :")
    if(user in username and passw in password):
        print("login successfully!!")
        return True
    elif(user not in username and passw not in password):
        print("Please signup")
        registeration()
        return False

def registeration():
    num = int(input("Enter a number :"))
    for x in range(num):
        name     = input("Enter username :")
        passwords = input("Enter password :")
        if(name == username and passwords == password):
            print("This user already present!!")
        else:
            username.append(name)
            password.append(passwords)
    print(username)
    print(password)

def stop():
    print("Application stop now")
    return 0
        

c=0
v=1
while(v):
    s=int(input("Enter 1 for login\nEnter 2 for stop\n"))
    if(s==1):
        if(c<3):
            c+=1
            print(c)
            if(login()):
                break
        else:
            print("Try after sometime")
            break   
    elif(s==2):
        v=stop()
    else:
        print("This sevice is not available")