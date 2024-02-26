myInfo ={
    'name' : 'Shanto Roy',
    'age': 22,
    "isHeGood": True,
    'isHeBad': False,
    'favouriteCode': ['C', 'JAVA', 'JavaScript', 'Python']
}

# update() ---->to changing a key value
print(myInfo) #{'name': 'Shanto Roy', 'age': 22, 'isHeGood': True, 'isHeBad': False, 'favouriteCode': ['C', 'JAVA', 'JavaScript', 'Python']}
myInfo.update({'name' : 'Avinandan Roy'})
print(myInfo) #{'name': 'Avinandan Roy', 'age': 22, 'isHeGood': True, 'isHeBad': False, 'favouriteCode': ['C', 'JAVA', 'JavaScript', 'Python']}


