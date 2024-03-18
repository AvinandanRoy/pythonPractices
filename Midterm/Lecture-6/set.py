set1 = {1,2,3,4,5,6,7,8,9}
set2 = {4,5,9,234,6786}
print(set1|set2)
print(set1 & set2)
print(set1 - set2)
print(set2 - set1)

set1.add(122)
set1.add(123)
print(set1)
set1.remove(122)
print(set1)

# set1.clear()
# print(set1)
print(set1.intersection(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))