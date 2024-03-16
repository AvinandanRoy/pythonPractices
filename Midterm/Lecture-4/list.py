
myList = [10,20,30,40,50,'Avinandan','Pranta','Kishore']

myList[5] = 'Avinandan Roy'

print(myList[5])

print("Iterable")

for ele in myList:
    print(ele, end=' ')

print("\nusing break statement : " , end=' ')

for ele in myList :
    if ele == 'Avinandan Roy':
        break
    print(ele , end=' ')

print("\nusing continue statement : " , end=' ')

for ele in myList:
    if ele == 'Avinandan Roy':
        continue
    print(ele, end=' ')