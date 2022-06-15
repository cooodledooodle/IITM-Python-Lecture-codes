#Problem 3
#Find the day wise total rainfall for the entered duration of time e.g. week, month, etc.

days = int(input('Enter the number of days: '))
for i in range(1, days + 1):
    total = 0
    rainfall = int(input('Enter the rainfall: '))
    while(rainfall != -1):
        total += rainfall
        rainfall = int(input('Enter the rainfall: '))
    print('Total rainfall for day {0} is {1}'.format(i, total))