# braek
print('Beak Example : ', end=' ')
for number in range(1,15):
    if(number == 10):
        break
    print(number,end=' ')
# --------------------------------------------------
print(end='\n')
# --------------------------------------------------

# continue
print("Continue Example : ", end=' ')
for number in range( 1, 15):
    if(number == 5 ):
        continue
    if(number == 12 ):
        continue
    print(number , end='->')