# The algorithm for solving this problem must:
# -Keep a running total of the grades.
# -Calculate the average the total of the grades divided by the number of grades.
# -Display the result.

grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
totalGrades = 0
counter = 0

for grade in grades:
    totalGrades += grade
    counter += 1

averageGrade = totalGrades / counter
print(f'The average grade is : {averageGrade}')