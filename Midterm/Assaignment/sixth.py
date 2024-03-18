
list1 = [x for x in range(11,24,2)]
list2 = [x for x in range(3,16,3)]

def commonElement(list1,list2):
    commonList = []
    for item in list1:
        for match in list2:
            if item == match:
                commonList.append(item)
    return commonList

def createListToDict(list):
    myDict = {}
    for item in list :
        myDict.update({item : item**3})
    return myDict 

commonElementList = commonElement(list1,list2)
print('The common elemt list is : ',commonElementList)
print('Result Dictionary : ', createListToDict(list1))