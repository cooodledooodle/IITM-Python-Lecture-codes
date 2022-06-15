#Problem 2
#Write a Python code using functions to calculate area and perimeter of circle and rectangle

def rect_area(l, b):
    return l * b


def circle_area(r):
    return 3.14 * r ** 2


def rect_para(l, b):
    return 2 * (l+b)


def circle_para(r):
    return 2 * 3.14 * r


a = ""

while a != "exit":
    a = input()
    
    if a == "circle":
        b = input()
        if b == "area":
            r = int(input())
            print(circle_area(r))
        if b == "parimeter":
            r = int(input())
            print(circle_para(r))

    if a == "rectangle":
        b = input()
        if b == "area":
            l = int(input())
            b = int(input())
            print(rect_area(l, b))
        if b == "parimeter":
            l = int(input())
            b = int(input())
            print(rect_para(l, b))