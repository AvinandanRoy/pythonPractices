def summationTwoNumbers(a,b):
    print(f'First Number is {a}')
    print(f'Second Number is {b}')
    return a+b

a , b = map(int, input("Enter Number : ").split())
sum = summationTwoNumbers(a,b)
print(sum)