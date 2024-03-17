# Write a Python program that accepts an employee's ID, total worked hours of a month and the amount S/he received per hour. Print the employee's ID and salary (with two decimal places) of a particular month. S/he has day off on Friday and Saturday. 

employeeDict = dict()

def displayEmployeeSalary(employeeDict):
    for key , value in employeeDict.items() :
        print(f'Employee {key} salary is {value}')

def employeeSalary(id,hours,ammount):
    salary = round(hours*ammount,2)
    return {id:salary}

empId = input("Enter Your Id : ")
hours = float(input("Enter Your total work hour of a month : "))
ammout = float(input('Enter Per hout payment : '))

displayEmployeeSalary(employeeSalary(empId,hours,ammout))