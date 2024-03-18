# From Avinandan Roy(221-15-4899)-01776890663

sunday = float(input("Your Sunday expense : "))
monday = float(input("Your Monday expense : "))
tuesday = float(input("Your Tuesday expense : "))
wednessday = float(input("Your wednesday expense : "))
thusday = float(input("Your Thusday expense : "))
friday = float(input("Your Friday expense : "))
saturday = float(input("Your Saturday expense : "))
weakEx = sunday+monday+tuesday+wednessday+thusday+friday+saturday ;

print(f'Weakly Expense : ${weakEx}')
print(f'Average :${weakEx/7}')

myDict = {
    'Sunday' : sunday,
    "Monday" : monday,
    'Tuesday' : tuesday,
    'wednesday' : wednessday,
    'Thusday' : thusday,
    'Friday' : friday,
    'Saturday' : saturday
}

def exceedBuudget(mydict):
    newDict ={}
    for key , val in myDict.items():
        if val > 2000:
            newDict.update({key: val})
    return newDict

def printDict(myDict):
    for key,val in myDict.items():
        print(f"{key} : ${val}")

print("Days where expenses execeed the daily budget : ")
printDict(exceedBuudget(myDict))