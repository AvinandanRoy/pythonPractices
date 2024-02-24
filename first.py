
# nested for loop
print("Using Nested for Loop:")
x =[ 1, 2]
y =[3, 4 ]
for i in x :
    for j in y :
        print(i,j)

# we can use the while loop to replace the for loop :
print("Using While loop:")
a = [ 5,6]
b  = [7,8]
i = 0
while i < len(a):
    j= 0
    while j < len(b):
        print(a[i],b[j])
        j += 1
    i+=1

# multiplication Table using nested for loop 1 t0 10 multiplication table number :
