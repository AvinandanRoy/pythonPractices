# From Avinandan Roy

def listToDict(key , value):
    return dict(zip(key,value))

k = [1001,1002,1003,1004,1005]
v= ['USA', 'Canada', 'China', 'Japan','UK']

newList = listToDict(k,v)
print(newList)