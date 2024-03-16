# From Avinandan Roy

def printOddNumbersList(list):
    for item in list :
        print(item , end=' ')

number = 1 
numbersList = list()


while number<= 100:
    if(number %2 != 0):
        numbersList.append(number)
    number += 1 

printOddNumbersList(numbersList)