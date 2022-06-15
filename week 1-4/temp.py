import random

no_repetation = 0
repetition = 0

no_of_lists = 50000
no_of_bdays = 75

for i in range(no_of_lists):
    l = []
	for i in range(no_of_bdays):
        l.append(random.randint(1, 365))

    l.sort()
    i = 0
    flag = 0
    
    while (i < len(l) - 1):
        if l[i] == l[i+1]:
            flag = 1
            break
        i += 1

    if flag == 1:
        repetition += 1
    if flag == 0:
        no_repetation += 1

print("There are", no_repetation, "no repetitions")
print("There are", repetition, "repetitions")
p = (repetition / no_of_lists) * 100
print("{0:.2f} %".format(p))
