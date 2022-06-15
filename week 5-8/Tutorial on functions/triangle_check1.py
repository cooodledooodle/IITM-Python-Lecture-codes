#Problem3
#Write a Python code using functions which checks whether the input coordinates form a triangle or not
#using distance

def distance(xi, yi, xj, yj):
    return (((xj - xi) ** 2) + ((yi - yj) ** 2)) ** 0.5

def isTriangle(max, a, b):
    if max > (a + b):
        print("\nTriangle")
    else:
        print("\nNot a Triangle")



x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

d1 = distance(x1, y1, x2, y2)
d2 = distance(x2, y2, x3, y3)
d3 = distance(x3, y3, x1, y1)

if  d1 > d2:
    if d1 > d3:
        isTriangle(d1, d2, d3)
    else:
        isTriangle(d3, d1, d2)
elif d2 > d3:
    isTriangle(d2, d1, d3)
else:
    isTriangle(d3, d1, d2)