
# __iter__() ans __next__()

myTuple = ('Apple','Orange','Banana','Berry','Coconut')

myit = iter(myTuple)

# simple print
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# While loop print
i= 0
while i< len(myTuple):
    print(next(myit))
    i += 1

# for loop print
for i in range(len(myTuple)):
    print(next(myit))

