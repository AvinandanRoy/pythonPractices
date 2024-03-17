
animals = ['Lion','Tiger','Elephant','Giraffe','Zebra']

def firstThreeAnimals(list):
    firstThreeElementList = []
    for animal in range(3) :
        firstThreeElementList.append(list[animal])
    return firstThreeElementList

def lastTwoAnimal(list):
    lastTwoAnimalList =[]
    for animal in range(3,5):
        lastTwoAnimalList.append(list[animal])
    return lastTwoAnimalList

def replaceValue(i,j,list):
    list[i],list[j] = list[j], list[i]
    return list

print('The main list is :', animals)
print('The first Three Animal list is :',firstThreeAnimals(animals))
print('The last two animal list is :',lastTwoAnimal(animals))
print('After replacing the value the list is :',replaceValue(2,4,animals))
    