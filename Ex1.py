# list1 = ['I am ', 'You are ']
# list2 = ['healthy', 'fine', 'geek']

# showing down/print  :

# start outer for loop
# I am  healthy
# I am  fine
# I am  Avinandan Roy
#
# end for loop
#
# start outer for loop
#
# You are  healthy
# You are  fine
# You are  Avinandan Roy
#
# end for loop

list1 = ['I am ', 'You are ']
list2 = ['Avinandan Roy','healthy','fine']

for item in list1:
    print("Start outer for loop")
    i =0
    while i < len(list1):
        for j in list2:
            print(item,j)
        i += 1