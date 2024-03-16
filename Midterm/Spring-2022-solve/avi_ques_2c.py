# From Avinandan Roy

def createList(n):
    myList = list()
    for i in range(n):
        element = int(input(f'Enter {i+1} element : '))
        myList.append(element)
    return myList

element= int(input("Enter the number of element : "))
prevList = createList(element)

if len(prevList)< 3:
    print("Not possible....!")
else:
    prevList.remove(prevList[0])
    prevList.remove(prevList[len(prevList)-1])
    newList = prevList.copy()
    print(newList)