print("Welcome to Divine Public School, Udaipur")

# {'student':{101:{'name':'shubham','class':5}
# , 102:{}},
# 'employee':{201:{'name':'vijay'}}}

# lib = {'student':[101,102],
# 'employee':[201]}

# lib['student'].append(103)


# student 1
# emp  2

# sid in lib['studen




class StudentData:
    add_student_list = []
    add_student_roll_No = []
    add_employee_data = {}

    def student_data(self):
        v = 1
        while(v):
            try:

                self.number_of_student = int(input("Enter no. of student :"))
                v = 0
                for student in range(self.number_of_student):
                    self.student_name = input("Enter student name :")
                    self.student_roll_No = input("Enter Roll No :")
                    if(self.student_name in self.add_student_list):
                        print("Data is already in present in this add student list")
                    elif(self.student_name.isalpha()):
                        self.add_student_list.append(self.student_name)
                    if(self.student_roll_No in self.add_student_roll_No):
                        print("Data is already in present in this add student list")
                    elif(self.student_roll_No.isnumeric()):
                        self.add_student_roll_No.append(self.student_roll_No)
                    else:
                        print(
                            "Data is already present in this add student Roll No list")

            except:
                print("This is not valid given user data")
        print(self.add_student_list)
        print(self.add_student_roll_No)

    def Employee_data(self):
        v = 1
        while(v):
            try:
                self.number_of_employee = int(
                    input("Enter number of employee :"))
                v = 0
                self.employee_id = 100
                for employee in range(self.number_of_employee):
                    self.employee_name = input("Enter Employee data :")

                    if(self.employee_name):
                        self.employee_id += 1
                        self.add_employee_data[self.employee_id] = self.employee_name

                    else:
                        print("data is not calable in various path")
            except:
                print("various data always not callable")
            print(self.add_employee_data)

    def library_system(self):
        v = 1
        for student_employee in range(v):
            try:
                flag = 1
                while(flag):
                    employee_student = int(
                        input("Enter 1 for student :\nEnter 2 for employee :"))
                    flag = 0
                    if(employee_student == 1):
                        self.student_name = input("Enter student name :")
                        v = 0
                        if(self.student_name in self.add_student_list):
                            print("given detail is valid and issued book")
                        elif(self.student_name not in self.add_student_list):
                            print("given detail is not valid and book not issued")
                        else:
                            print("This service not avaialable!")
                    elif(employee_student == 2):
                        self.employee_name = input("Enter employee name :")
                        v = 0
                        if(self.employee_name in self.add_employee_data.values()):
                            print("given detail is valid and issued book")
                        elif(self.employee_name not in self.add_employee_data):
                            print("given detail is not valid and book not issued")
                        else:
                            print("This service not avaialable!")
                    else:
                        print("This service not available!!")
            except:
                print("This data is not available")


s = StudentData()
v = 1
while(v):
    try:
        flag = 1
        while(flag):
            system = int(input(
                "Enter 1 for student_data :\nEnter 2 for Employee_data :\nEnter 3 for library_system :\nEnter 4 for stop :"))
            v = 0
            if(system == 1):
                s.student_data()
            elif(system == 2):
                s.Employee_data()
            elif(system == 3):
                s.library_system()
            elif(system == 4):
                print("This School website is terminate of this time!!!")
                flag = 0
            else:
                print("This service is not available")
    except:
        print("This concept is not valuable in various proceduce")
