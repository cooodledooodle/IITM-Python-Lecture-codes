#Problem 1
#Find the factorial of the given number

num = int(input('Enter a number: '))
fact = 1
if(num < 0):
    print('Not defined')
else:
    for i in range(num, 1, -1):
        fact = fact * i
    print(fact)