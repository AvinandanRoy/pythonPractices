
myDict = dict()
print(myDict)

myDict = {
    "name": 'Avinandan Roy',
    'homeTwon' : 'Lohagara, Narail',
    'studentId' : 4899,
    'phNumbr' : '01776890663'
}

print(myDict)

print(myDict['name'])

city = ['Dhaka','Jashore','Khulna','Chittagong','Narail']
year = [2021,2018,2021,2022,2002]
mySecondDict = dict(zip(city,year))
print(mySecondDict['Narail'])

# update dict value :---->
mySecondDict['Ashulia']= 2024
print(mySecondDict)

for k,v in mySecondDict.items():
    print(k,v)

cityName = input('Enter Your City name : ')
cityYear = int(input("Enter year : "))
mySecondDict.update({cityName:cityYear})
print(mySecondDict)

l = int(input("Enter 1 for next func"))

if l == 1 :
    del mySecondDict[cityName]
    print(mySecondDict)