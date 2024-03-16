# let there is a student who got 74 marks .Now your task is find out the grade that he achieved
# step-1 : Taking a input as a total marks that he got his examination
# step-2: Using consitional statement for finding his grade
# step-3 : Display his grade

marks = int(input("Enter Your Marks : "))


if(marks <= 100 and marks >= 80):
    print('Your got \'A+\'' )
elif(marks < 80 and marks >= 75):
    print('Your got \'A\'')
elif(marks < 75 and marks >= 70):
    print('Your got \'A-\'')
elif(marks < 70 and marks >= 65):
    print('Your got \'B\'')
elif(marks < 65 and marks >= 60):
    print('Your got \'B+\'')
elif(marks < 60 and marks >= 55):
    print('Your got \'B-\'')
elif(marks < 55 and marks >= 50):
    print('Your got \'C\'')
elif(marks < 50 and marks >= 45):
    print('Your got \'D\'')
elif(marks < 45 and marks >=40):
    print('Your got \'E\'')
else:
    print("You Fail in the Examination.Please Try Again!")