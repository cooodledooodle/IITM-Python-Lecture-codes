#add first 'n' natural numbers
def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)


#calculate compound interest by assumng the interest to be 10%
def comp(p,n):
    if n==1:
        return p*1.1
    else:
        return (comp(p, n-1))*1.1


#calculate the factorial of a number
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
