dim = 3

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [4,2,7]
s2 = [2,6,8]
s3 = [2,7,1]

A = []
A.append(r1)
A.append(r2)
A.append(r3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] += A[i][k] * B[k][j]

print(C)