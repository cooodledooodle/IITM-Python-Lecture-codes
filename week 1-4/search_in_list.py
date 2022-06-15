import random

l = []

for i in range(10000):
    l.append((random.randint(1, 30000)))

n = 0
while(n > -1):
    print("Enter a number, type -1 to exit:")
    n = int(input())

    flag =  0

    for i in range(len(l)):
        if l[i] == n:
            print("Hip Hip hooray, element", n, "is in the list")
            flag = 1
            break
    if flag == 0:
        print("Element", n, "is not in the list")