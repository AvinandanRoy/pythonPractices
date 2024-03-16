# From Avinandan Roy

list1 = [1,2,3,4]
list2 = [3,4,5]
commonNewList = list()

for item in list1 :
    if item in list2:
        commonNewList.append(item)

if(len(commonNewList) != 0):
    print(commonNewList)
else:
    print("No common List")