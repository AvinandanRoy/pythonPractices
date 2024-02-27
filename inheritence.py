

class Person :
    def __init__(self,fName , lName , age):
        self.fName = fName
        self.lName = lName
        self.age = age
    def wellcome(self):
        print('Wellcome',self.fName,self.lName,'to the first class of',self.gradu)

class Student(Person):
    def __init__(self, fName , lName , age ,gradu):
        super().__init__(fName,lName,age)
        self.gradu = gradu



s1 = Student("Avinandan" ,'Roy',22,2025)
s1.wellcome()


