class Person:
    print("Welcome to Engineering College, Udaipur !!")

    def addstudent(self):
        self.name = input("Enter name :")
        self.year = int(input("Enter year :"))
        self.branch = input("Enter branch :")

    def addfaculty(self):
        self.Uname = input("Enter faculty name :")
        self.id = int(input("Enter year :"))

    def showstudent(self):
        print("Student Details Here :")
        print("Student Name   :", self.name)
        print("Student Year   :", self.year)
        print("Student Branch :", self.branch)

    def showfaculty(self):
        print("Faculty Details Here :")
        print("Faculty name   :", self.Uname)
        print("Faculty ID     :", self.id)


class Update(Person):
    def addstudentU(self):
        self.addstudent()
        self.section = input("Enter section :")
        self.semester = int(input("Enter semester :"))

    def showstudentU(self):
        self.showstudent()
        print("Student Section :", self.section)
        print("student Semester:", self.semester)

    def addfacultyU(self):
        self.addfaculty()
        self.salary = int(input("Enter salary :"))

    def showfacultyU(self):
        self.showfaculty()
        print("Faculty salary  :", self.salary)


u1 = Update()
v = 1
while(v):
    s = int(input("Enter 1 for addstudent :\nEnter 2 for showstudentb :\nEnter 3 for addfaculty :\nEnter 4 for showfaculty :\nEnter 5 for addstudentU :\nEnter 6 for showstudentU :\nEnter 7 for addfacultyU :\nEnter 8 for showfacultyU :\nEnter 9 for exit :"))
    if(s == 1):
        u1.addstudent()
    elif(s == 2):
        u1.showstudent()
    elif(s == 3):
        u1.addfaculty()
    elif(s == 4):
        u1.showfaculty()
    elif(s == 5):
        u1.addstudentU()
    elif(s == 6):
        u1.showstudentU()
    elif(s == 7):
        u1.addfacultyU()
    elif(s == 8):
        u1.showfacultyU()
    elif(s == 9):
        print("Application stop now !!!")
        v = 0
    else:
        print("This service not available!!")
