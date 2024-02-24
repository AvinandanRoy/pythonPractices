# multiplication table with your need  :
a = int(input("What number multiplication table did you need ? "))

for i in range(1,11):
    print(a*i)

# multiplication Table using nested for loop 1 t0 10 multiplication table number :

for i in range(1,11):
    print(f"{i} Notation Multiplication Table :")
    for j in range(1 , 11 ):

        print(f"{i} x {j} = {i*j}")