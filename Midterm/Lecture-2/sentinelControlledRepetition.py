# The algorithm for solving this problem must:
# -Keep a running total of the grades.
# -Calculate the average the total of the grades divided by the number of grades.
# -Display the result.

totalGrade = 0
counter =  0

grade = int(input("Enter -1 if All students grade Was done : "))

while grade != -1 :
    totalGrade += grade
    counter += 1
    grade = int(input("Enter -1 if All students grade Was done : "))

if counter != 0 :
    averageGrade = totalGrade / counter
    print(f'The average grade is : {averageGrade}')
else:
    print('Enter Students Grade..!')

# [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]