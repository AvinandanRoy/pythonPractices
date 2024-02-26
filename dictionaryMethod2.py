# Accessing items

myInfo= {
    'name' : 'Avinandan Roy',
    'age' : 22 ,
    "isHeGood" : True,
    'isHeBad' : False,
    'favouriteCode' : ['C','JAVA', 'JavaScript','Python']
}

# get() method for accessing item from a list
x = myInfo.get('name')
print(x) #Avinandan Roy
y = myInfo.get('favouriteCode')
print(y) #['C', 'JAVA', 'JavaScript', 'Python']

# GetKeys -----> keys() method
# The keys() method will return a list of all the keys in the dictionary.
x = myInfo.keys()
print(x) #dict_keys(['name', 'age', 'isHeGood', 'isHeBad', 'favouriteCode'])

myInfo['color']= 'blueviolet'
print(myInfo.keys()) #dict_keys(['name', 'age', 'isHeGood', 'isHeBad', 'favouriteCode', 'color'])


# Get Values---->values()
print(myInfo.values()) #dict_values(['Avinandan Roy', 22, True, False, ['C', 'JAVA', 'JavaScript', 'Python'], 'blueviolet'])

myInfo['name']= "Krishna Kanta Roy"
print(myInfo.values())

# Get Items ----->items()
print(myInfo.items()) #dict_items([('name', 'Krishna Kanta Roy'), ('age', 22), ('isHeGood', True), ('isHeBad', False), ('favouriteCode', ['C', 'JAVA', 'JavaScript', 'Python']), ('color', 'blueviolet')])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Check if "color" is present in the dictionary:

if 'color' in myInfo:
    print("YEs this a key of this dictionary")
else:
    print("This is not a key of this dictionary")