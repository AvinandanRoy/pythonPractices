#Loop Through a Dictionary

myInfo= {
    'name' : 'Avinandan Roy',
    'age' : 22 ,
    "isHeGood" : True,
    'isHeBad' : False,
    'favouriteCode' : ['C','JAVA', 'JavaScript','Python']
}

for i in myInfo:
    print(i)

for i in myInfo:
    print(myInfo[i])

for i in myInfo.values():
    print(i)

for i in myInfo.keys():
    print(i)

for i,j in myInfo.items():
    print(i,j)