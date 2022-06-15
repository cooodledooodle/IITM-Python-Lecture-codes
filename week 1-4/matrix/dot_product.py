x = [1,3,5,8,5,3]
y = [3,7,9,4,2,5]

sum = 0
for i in range(len(x)):
    sum += x[i] * y[i]

print(sum)