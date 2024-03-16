print('1 to 10 all number is : ', end = ' ')
for i in range(1,10+1):
    print(i , end=' ')

print('\n')
#finding the sum of 1 to 1000 number ::::------>
sum= 0
for i in range(1, 1000+1 ):
    print(i,end=' ')
    sum += i

print(f'Increment 1 times : {sum}')

# make it with increment 2 ....means i = i + 2

sum2 = 0
for i in range(1,1000+1 ,2 ):
    print(i,end=' ')
    sum2 += i
print(f'Increment 2 times : {sum2}')