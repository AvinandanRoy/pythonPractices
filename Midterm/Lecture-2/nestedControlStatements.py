# 1.The program must process 10 test results. We’ll use a for statement and the range function to control repetition.
# 2.Each test result is a number either a 1 or a 2. Each time the program reads a testresult, the program must determine if the number is a 1 or a 2. We test for a 1 in our
# algorithm. If the number is not a 1, we assume that it’s a 2.
# 3.We’ll use two counters one to count the number of students who passed the examand one to count the number of students who failed.
# 4.After the script processes all the results, it must decide if more than eight studentspassed the exam so that it the instructor can get bonus.

passes = 0 
fail = 0 

for student in range(1 , 10+1):
    grade = int(input('If pass then enter 1 and if fail then enter 2 : '))
    if(grade == 1):
        passes += 1
    else:
        fail += 1 

print(f'The number of sudent who passes : {passes}')
print(f'The number of sudent who fail : {fail}')

if(passes > 8):
    print('Instructor can get bonus!')