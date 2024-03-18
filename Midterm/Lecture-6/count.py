

def create(string):
    mydict ={}
    for char in string:
        if char in mydict:
            mydict[char] += 1 
        else:
            mydict[char] = 1 
    return mydict

myidct = create('w3resource')
print(myidct)

print(create("Avinandan Roy"))