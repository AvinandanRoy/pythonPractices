
# let a student information reserve a stuInformation variable

stuInformation = {
    'name' : 'Avinandan Roy',
    'sId' : '221-15-4899',
    'section' :'61_Q',
    'cgpa' : '3.89'
}
print(f"{stuInformation['name']} student id is {stuInformation['sId']}.{stuInformation['name']} is from {stuInformation['section']} section.He got {stuInformation['cgpa']} cgpa in previous semester.")
#output :  Avinandan Roy student id is 221-15-4899.Avinandan Roy is from 61_Q section.He got 3.89 cgpa in previous semester.

print(stuInformation)
#Output : {'name': 'Avinandan Roy', 'sId': '221-15-4899', 'section': '61_Q', 'cgpa': '3.89'}


# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key:
myCar = {
    'brand' : 'Mercedis',
    'model' : 'sedan',
    'year' : '2020',
    'year' : '2024'
}
print(myCar)
# output : {'brand': 'Mercedis', 'model': 'sedan', 'year': '2024'}
# here 'year' : '2020' not running

# Dictionary Length ---len()
print(len(stuInformation))
# output : 4
print(len(myCar))
# output : 3


#           Dictionary Items - Data Types::::::
# String, int, boolean, and list data types:
myInfo= {
    'name' : 'Avinandan Roy',
    'age' : 22 ,
    "isHeGood" : True,
    'isHeBad' : False,
    'favouriteCode' : ['C','JAVA', 'JavaScript','Python']
}

# type()-----we can define the type of a dictionary
print(type(stuInformation)) # output :<class 'dict'>
print(type(myCar))# output :<class 'dict'>
print(type(myInfo)) # output :<class 'dict'>

print(type(myInfo['favouriteCode'])) #<class 'list'>
print(type(myInfo['favouriteCode'][1])) #<class 'str'>

#The dict() Constructor------Using the dict() method to make a dictionary:
thisDict = dict( name = "Avinandan Roy" , age = 22 , cgpa = 3.89)
print(thisDict) #{'name': 'Avinandan Roy', 'age': 22, 'cgpa': 3.89}