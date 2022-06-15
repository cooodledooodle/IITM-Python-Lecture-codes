import random

l = []

for i in range(20):
    l.append((random.randint(1, 1000)))
print(l)

sortedL = []

while(len(l) > 0):
    min = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    sortedL.append(min)
    l.remove(min)

print(sortedL)