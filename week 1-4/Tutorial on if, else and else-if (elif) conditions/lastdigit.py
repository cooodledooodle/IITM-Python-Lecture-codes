#Problem 2
#Find weather the given number ends with 0 or 5 or any other number

num = int(input ('Enter a number: '))

if (num % 5 == 0):
    if (num % 10 == 0):
        print('0')
    else:
        print ('5')
else:
    print ('Other')