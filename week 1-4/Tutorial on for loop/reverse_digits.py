#Problem 3
#Reverse the digits of a number

num = int(input('Enter a number: '))
absStrNum = str(abs(num))
rev = ''
for c in absStrNum:
    rev = c + rev
if (num >= 0):
    print(rev)
else:
    print('-' + rev)