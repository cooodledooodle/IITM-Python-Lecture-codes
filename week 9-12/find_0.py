#noob approach

def check0(L):
    if len(L)==0:
        return 0
    if L[0] == 0:
        return 1
    else:
        return check0(L[1:len(L)])

print(check0([3,5,6,2,6,4]))