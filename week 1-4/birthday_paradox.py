import random

l = []

for i in range(20):
    l.append(random.randint(1, 365))


l.sort()
print(l)
i = 0
flag = 0


while (i < len(l) - 1):
    if l[i] == l[i+1]:
        print(l[i], "is repeating")
        flag = 1
        break
    i += 1


if flag == 0:
    print("There is no repetition")


