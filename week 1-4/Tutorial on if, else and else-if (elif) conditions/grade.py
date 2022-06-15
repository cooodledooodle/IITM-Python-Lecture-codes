#Problem 3
#Find the grade of student based on the given marks from 0 to 100

marks = int(input ('Enter marks: '))

if (marks >= 0 and marks <= 100):
    if (marks >= 90):
        print ('A')
    elif (marks >= 80):
        print ('B')
    elif (marks >= 70):
        print ('C')
    elif (marks >= 60):
        print ('D')
    else:
        print ('E')
else:
    print ('Invalid input')