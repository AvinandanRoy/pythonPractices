
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

myInfo= {
    'name' : 'Avinandan Roy',
    'age' : 22 ,
    "isHeGood" : True,
    'isHeBad' : False,
    'favouriteCode' : ['C','JAVA', 'JavaScript','Python']
}
print(myInfo)

#using copy()  method
myInfoCpy = myInfo.copy()
myInfoCpy.update({'uni': 'DIU'})
myInfo = myInfoCpy.copy()
if myInfo == myInfoCpy:
    print('yes matching')
else:
    print('NO match')

#using dict() method
myInfo.clear()
myInfoCpy.clear()
print(myInfo)
print(myInfoCpy)

myInfo.update({'name' : 'Avinandan Roy' , 'age' : 22 , 'fatherName' : 'Krishna Kanta Roy', 'motherName' : 'Lipika Rani Roy'} )

myInfoCpy = dict(myInfo)
print(myInfoCpy)

if myInfoCpy == myInfo :
    print('YES matching')
else:
    print("NO matching")


# Nested dictionary
myFamily ={
    'father' : {
        'name' : 'Krishna Kanta Roy',
        'bYear' : 1972
    },
    'moher':{
        'name' : 'Lpika Rani Roy',
        'bYear' : 1979
    },
    'me':{
        'name' : 'Avinandan Roy',
        'bYear' : 2002
    },
    'brother' :{
        'name' : 'Pranta Roy',
        'bYear' : 2006
    }
}
# accessing nestes dictionary
print(myFamily['father']['name'])

# make a tree dict and then create a single dict that willl contain these three dict
# firstly making three individual dict
father ={
    'name' : 'Krishna Kanta Roy',
    'age' : 52
}
mother ={
    'name' : 'Lipika Rani Roy',
    'age' : 45
}
mySelf = {
    'name' : 'Avinandan Roy',
    'age' : 22
}
brother ={
    'name' : 'Pranta Roy',
    'age' : 18
}
# added a single dictionary
myFamilyList = {
    'father' : father,
    'mother': mother,
    'mySelf' : mySelf,
    'brother' : brother
}

print(myFamilyList['mother']['name'])

