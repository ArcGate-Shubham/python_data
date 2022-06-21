#from configparser import ConfigParser
#import configparser
import mysql.connector as c
#object1 = configparser.ConfigParser()
con = c.connect(host     = "localhost",
                user     = "shubham",
                password = "shubham",
                database = "college")
class ValidSet:
    cursor = con.cursor()

    # def write_in_file(self,fromUpdate = False,*args):
    #     print("inside write_file",args)
    #     print(fromUpdate)
    #     with open('config2.ini','a') as conf:
    #         if(len(args)==3):
    #             id, name, password = args
    #             conf.write(f",{id},{name},{password}")
    #             conf.write("\n")
    #         elif(fromUpdate):
    #             name,id= args
    #             conf.write(f"{name}, {id}")
    #         # elif(fromUpdate):
    #         #     result = args
    #         #     conf.write(f'{result}')
    #         else:
    #             name,password = args
    #             conf.write(f"{name},{password}")


    def validation_data(self):
        flag = 1
        while(flag):
            try:
                id = input("Enter id :")
                flag = 0
                name = input("Enter name :")
                password = input("Enter password :")
                flag = 0
                if(id.isnumeric() and name.isalpha() and password.isnumeric()):
                    query = "insert into various values({},'{}',{})".format(id, name, password)
                    self.cursor.execute(query)
                    con.commit()
                    print("Data inserted successfully")
                    #self.write_in_file("Student Data :",id,name,password)
                else:
                    print("name or password doesn't exist!!")
                
            except:
                print("Data is proper not valid")
            flag = 1
            while(flag):
                step = int(input("Enter 1 for one more choice :\nEnter 2 for Exit :\nEnter Choice :"))
                if(step == 2):
                    print("Exit")
                    flag = 0

    def login(self):
        name = input("Enter name :")
        password = int(input("Enter password :"))
        checkData = f"select id from various where name = '{name}' and password = {password}"
        self.cursor.execute(checkData)
        result = self.cursor.fetchall()
        
        if(not result):
            print("not matched")
        else:
            print("inside login",result)
            #self.write_in_file(name,password)
            

    def update_data(self):
        name = input("Enter updated name :")
        id = int(input("Enter id :"))
        query = "update various set name ='{}' where id ='{}'".format(name,id)
        self.cursor.execute(query)
        con.commit()
        #self.write_in_file(True,id,name)

    def delete_data(self):
        id = int(input("Enter id :"))
        query = "delete from various where id = {}".format(id)
        self.cursor.execute(query)
        con.commit()


    def fetch_all(self):
        query = "select * from various"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print("ID       :",row[0])
            print("name     :",row[1])
            print("password :",row[2])
            print()
        #self.write_in_file(True,result)

    def value_data(self):
        id = input("Enter id :")
        position = input("Enter position :")
        if(id.isnumeric() and position.isalpha()):
            queries ="insert into value values({},'{}')".format(id, position)
            self.cursor.execute(queries)
            con.commit()
            print("Data inserted successfully")
        else:
            print("id and position does not callable")

    def fetch_all_data(self):
        query = "select * from value"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print("ID       :",row[0])
            print("Position :",row[1])
            print("\n")

    def left_join(self):
        query = "select id,name,password,position from various left join value on various.id = value.cid;"        
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print("ID        :",row[0])
            print("Name      :",row[1])
            print("Password  :",row[2])
            print("position  :",row[3])
            print("\n")

v = ValidSet()
s = 1
while(s):
    try:
        flag=1
        while(flag):
            validation_process = int(input("Enter 1 for Validation_data :\nEnter 2 for login :\nEnter 3 for update_data :\nEnter 4 for delete_data :\nEnter 5 for fetch_all :\nEnter 6 for value_data :\nEnter 7 for fetch_all_data :\nEnter 8 for left_join :\nEnter 9 for stop :" ))
            flag=0
            if(validation_process == 1):
                v.validation_data()
            elif(validation_process == 2):
                v.login()
            elif(validation_process == 3):
                v.update_data()
            elif(validation_process == 4):
                v.delete_data()
            elif(validation_process == 5):
                v.fetch_all()
            elif(validation_process == 6):
                v.value_data()
            elif(validation_process == 7):
                v.fetch_all_data()
            elif(validation_process == 8):
                v.left_join()
            elif(validation_process == 9):
                print("This service stop now")
                s= 0
            else:
                print("This service not available for this time")
    except:
        print("This data not valid for this time")
