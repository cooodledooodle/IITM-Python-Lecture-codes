#Problem 1
#Write a Python code using functions which calculates the number of upper case letters, lower case letters, total number of characters and number of words

def upper(s):
    upper = 0
    for c in s:
        if c.isupper():
            upper += 1
    return upper


def lower(s):
    lower = 0
    for c in s:
        if c.islower():
            lower += 1
    return lower


def lc(s):
    lc = 0
    for c in s:
        lc += 1
    return lc


def words(s):
    words = 1
    for i in s:
        if i == " ":
            words += 1
    return words


sentence = input("Enter a sentence: ")
print(upper(sentence), lower(sentence), lc(sentence), words(sentence), end=" ") 