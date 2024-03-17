# From Avinandan Roy

def listConstructor(dataset):
    return [int(x) for x in dataset.split(',')]

dataset = '1,2,3,4,5,6,7,8,9'
myList = listConstructor(dataset)
print(myList)