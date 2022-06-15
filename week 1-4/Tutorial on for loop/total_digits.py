#Problem 2
#Find the number of digits in a given number

num = abs(int(input('Enter a number: ')))
strNum = str(num)
digits = 0
for c in strNum:
    digits = digits + 1
print(digits)