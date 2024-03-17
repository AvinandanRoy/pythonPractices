# From Avinandan Roy
def constractList(dataset):
    return [int(x) for x in dataset.split(',')]

def reverseSorted(myList):
    myList.reverse()
    myList.sort()
    return myList

li = "9,8,7,6,5,4,3,2,1"
print(reverseSorted(constractList(li)))