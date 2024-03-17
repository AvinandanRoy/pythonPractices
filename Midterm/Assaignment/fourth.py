
tempList = [22,18,25,20,17,23,21]

def swap(list,i,j):
    list[i] , list[j] = list[j] , list[i]
    return list

def minTemp(tempList):
    min = tempList[0]
    for i in tempList :
        if min > i :
            min = i
    return tempList.index(min)


def maxTemp(tempList):
    max = 0 
    for i in tempList:
        if i > max :
            max = i
    return tempList.index(max)

max = maxTemp(tempList)
min = minTemp(tempList)

print(f'Previous List is : {tempList}')
print(f'New list after swapping is :',swap(tempList,max, min))

