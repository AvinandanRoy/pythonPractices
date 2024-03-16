
myList = [1,2,3,4,5,6,7,8,9,10]
print(len(myList)) # 10

reversedMyList = [i for i in reversed(myList)]
print(reversedMyList)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# make a list that reversed and also 2 times 

reversedMyList1 = [i*2 for i in reversed(myList)]
print(reversedMyList1)
# [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

