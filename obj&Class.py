
class Employee :
    def __init__(self,name , age):
        self.name =  name
        self.age = age

    def displayInfo(self):
        print(f"My name is {self.name}, I am {self.age} years odl")

class Owners(Employee) :
    def __init__(self,name , age , salary):
        super().__init__(self,name ,age )
        self.salry = salary



name =input("Enter ur name : ")
age = input("Enter ur age : ")
salary = input("Enter ur salary : ")

employee1 = Employee(name , age)
employee1.displayInfo()

own1 = Owners(name , age , salary)
own1.displayInfo()
