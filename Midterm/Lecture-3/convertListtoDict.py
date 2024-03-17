

def listTodict(key , val):
    return dict(zip(key,val))

k = [1001,1002,1003,1004,1005]
v= ['USA','Canada','Chaina','Japan','UK']
dictionary = listTodict(k,v)
print(dictionary)