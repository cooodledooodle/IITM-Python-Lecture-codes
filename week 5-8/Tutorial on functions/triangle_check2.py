#Problem3
#Write a Python code using functions which checks whether the input coordinates form a triangle or not
#using slopes

import math

def slope(xi, yi, xj, yj):
    if xi == xj:
        return math.inf
    else:
        return (yi - yj) / (xi - xj)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


s1 = slope(x1, y1, x2, y2)   
s2 = slope(x2, y2, x3, y3)

if s1 != s2:
    print("\nTriangle")
else:
    print("\nNot a Triangle")