#Problem 2
#Find the number of digits in a given number

num = abs(int(input('Enter a number: ')))
digits = 1
while(num > 9):
    num = num // 10
    digits = digits + 1
print(digits)