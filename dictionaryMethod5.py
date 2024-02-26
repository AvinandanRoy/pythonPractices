
# Python - Remove Dictionary Items

myInfo= {
    'name' : 'Avinandan Roy',
    'age' : 22 ,
    "isHeGood" : True,
    'isHeBad' : False,
    'favouriteCode' : ['C','JAVA', 'JavaScript','Python']
}

myInfo.update({'fatherName' : 'Krishna Kanta Roy'})
myInfo.update({'motherName' : 'Lipika Rani Roy'})
print(myInfo)

myInfo.update({'broName' : 'Pranta Roy','uniname':'Daffodil International University'})
print(myInfo)

myInfo.pop('broName')
print(myInfo) #delete 'broName': 'Pranta Roy'

myInfo.popitem() # delete last item from my dictionary
print(myInfo)

del myInfo['favouriteCode'] #delete favouriteCode item
print(myInfo)

myInfo.clear() #all items from dictionary are deleted
print(myInfo)