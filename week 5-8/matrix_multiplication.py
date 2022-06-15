def initialize_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C

def dot_product(u,v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans += u[i] * v[i]
    return ans

def row(M,i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l

def column(M,j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append((M[i][j]))
    return l

def mat_mul(A,B):
    dim = len(A)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A,i), column(B,j))
    return C