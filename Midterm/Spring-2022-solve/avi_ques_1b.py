# From Avinandan Roy

def waiver(result, fees):
    if result > 3.50:
        return fees -((fees*20)/100)
    elif result >=3.00 and result <= 3.50:
        return fees-((fees*10)/100)
    else:
        return fees-((fees*5)/100)

result = float(input('Enter Your Result : '))
semesterFees = float(input("Enter Your Semester Fees : "))

totalPayable = waiver(result , semesterFees)
print(f'Your totat payable ammount for this semester is : {totalPayable}')
