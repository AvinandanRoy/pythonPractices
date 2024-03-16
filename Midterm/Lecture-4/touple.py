myTouple = ('Avinandan','4899','Lohagara')

print(myTouple)
print(myTouple[2])
print(myTouple[-3])

# repalcing touple element aren't possible
# myTouple[-3] = 'Avinandan Roy'
# print(myTouple)

for el in myTouple:
    print(el , end=' ')

# inserting into touple
print('\n')

myTouple += ("Krishna Roy",)
print(myTouple)

# slicing 
print(myTouple[1:len(myTouple)+1])

print(myTouple[:])