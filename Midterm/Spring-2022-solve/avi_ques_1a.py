# From Avinandan Roy

value = [1,2,3,4,5,6,7,8,9]
value1 = [1,2,3]

for item in value:
    if(item == 5):
        continue
    print('break')

    for item1 in value1:
        print(item,item1)