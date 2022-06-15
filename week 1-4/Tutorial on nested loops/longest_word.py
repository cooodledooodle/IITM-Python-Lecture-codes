#Problem 4
#Find the length of longest word from the set of words entered by the user

word = input('Enter a word: ')
max_len = 0
while(word != '-1'):
    count = 0
    for i in word:
        count += 1
    if(count > max_len):
        max_len = count
    word = input('Enter a word: ')
print(f'The longest word is {max_len} characters long')