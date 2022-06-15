#Problem 4
#Find weather the entered number is a palindrome or not

num = int(input('Enter a number: '))
absStrNum = str(abs(num))
rev = ''
for c in absStrNum:
    rev = c + rev
if (num < 0):
    rev = '-' + rev
if(num == int(rev)):
    print('Palindrome')
else:
    print('Not a palindrome')