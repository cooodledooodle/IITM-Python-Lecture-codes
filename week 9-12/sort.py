#sorting a list using recursion
def mini(L):
    mini = L[0]
    for i in L:
        if i < mini:
            mini = i
    return mini

def sort(L):
    if L == [] or len(L) == 1:
        return L

    m = mini(L)
    L.remove(m)

    return [m] + sort(L)

L = [56,57,3,6,854,78,54,2,7,2,8,8,54,3,74,6]
print(sort(L))