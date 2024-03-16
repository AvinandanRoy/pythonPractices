
# finding 1 to 100 odd and even nmbr ...>!

mainList = [item for item in range(1,101)]

oddList = list()
evenList = list()

for item in mainList:
    if item %2 == 0 :
        evenList.append(item)
    else:
        oddList.append(item)

def printList(list):
    for i in list :
        print(item, end= ' ')

print('Odd Numbers is : ', end=' ')
print(oddList)
print('\n')
print('Even List is : ', end=' ')
print(evenList)