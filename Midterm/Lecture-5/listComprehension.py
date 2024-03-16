
myList = [item for item in range(1,20,2)]
print(myList)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


myList2 = [item*3 for item in range(1,6)]
print(myList2)
# [3, 6, 9, 12, 15]

myList3 = [item for item in range(1,11) if item % 2 == 0]
print(myList3)
# [2, 4, 6, 8, 10]

