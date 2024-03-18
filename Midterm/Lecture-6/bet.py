list1 = [x for x in range(1,16)]
list2 = [x**2 for x in range(1,16)]


def listToDict(key ,val):
    return dict(zip(key,val))
myDict = listToDict(list1,list2)
print(myDict)

    