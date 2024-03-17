# Write a program to print the roll number and average marks of 8 students in three subjects (each out of 100). The marks are entered by user.
marksList = list()

def rollAndMarksDisplay():
    for i in range(8):
        print(f'Student {i+1} average marks is : {marksList[i]}')

for student in range(8):
    print(f"Enter Student {student+1} marks")
    totalMarks = 0 
    for marks in range(3):
        mark = float(input(f'Enter Subject {marks+1} mark :'))
        totalMarks += mark

    averageMark = round(totalMarks / 3 , 2)
    marksList.append(averageMark)

rollAndMarksDisplay()