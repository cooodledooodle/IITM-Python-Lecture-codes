#generates random mobile numbers
import random

f = open("output.txt", "a")
for i in range(10000):
    no = []
    no.append(random.randint(6, 9))

    for i in range(1, 10):
        no.append(random.randint(0, 9))

    for i in no:
        print(i, end="", file=f)
    print("", file=f)
f.close()