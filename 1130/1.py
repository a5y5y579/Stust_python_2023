class Student:
    def __init__(self, SchoolName, SchoolAddress, Chairman, StuName, StuID, Email, Credit, GPA):
        self.SchoolName = SchoolName
        self.SchoolAddress = SchoolAddress
        self.Chairman = Chairman
        self.StuName = StuName
        self.StuID = StuID
        self.Email = Email
        self.Credit = Credit
        self.GPA = GPA

    def getSchoolName(self):
        print(self.SchoolName)

    def setSchoolName(self, SchoolName):
        self.SchoolName = SchoolName
        print(SchoolName)

    def getSchoolAddress(self):
        print(self.SchoolAddress)

    def setSchoolAddress(self, SchoolAddress):
        self.SchoolAddress = SchoolAddress
        print(SchoolAddress)
    
    def getChairman(self):
        print(self.Chairman)

    def setChairman(self, Chairman):
        self.Chairman = Chairman
        print(Chairman)
    
    def getStuName(self):
        print(self.StuName)

    def setStuName(self, StuName):
        self.StuName = StuName
        print(StuName)

    def getStuID(self):
        print(self.StuID)

    def setStuID(self, StuID):
        self.StuID = StuID
        print(StuID)
    
    def getEmail(self):
        print(self.Email)

    def setEmail(self, Email):
        self.Email = Email
        print(Email)
    
    def getCredit(self):
        print(self.Credit)

    def setCredit(self, Credit):
        self.Credit = Credit
        print(Credit)
    
    def getGPA(self):
        print(self.GPA)

    def setGPA(self, GPA):
        self.GPA= GPA
        print(GPA)



student = Student("ABC 大學", "123 主街", "張主任", "小明", "A123456", "john.doe@email.com", 60, 3.5)

student.getSchoolName()
student.setSchoolName("XYZ 大學")

student.getSchoolAddress()
student.setSchoolAddress("456 大街")

student.getChairman()
student.setChairman("李主任")

student.getStuName()
student.setStuName("小華")

student.getStuID()
student.setStuID("B789012")

student.getEmail()
student.setEmail("jane.doe@email.com")

student.getCredit()
student.setCredit(75)

student.getGPA()
student.setGPA(3.8)

