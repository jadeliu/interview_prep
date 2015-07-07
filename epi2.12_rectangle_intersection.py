__author__ = 'qiong'

class Rectangle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def is_intersect(a, b):
    return a.x<=b.x+b.w and a.x+a.w>=b.x and  a.y<=b.y+b.h and a.y+a.h>=b.y

def get_intersect_rectangle(a, b):
    if is_intersect(a, b):
        return Rectangle(max(a.x, b.x), max(a.y, b.y),
                         min(a.x+a.w, b.x+b.w)-max(a.x, b.x),
                         min(a.y+a.h, b.y+b.h)-max(a.y, b.y))
    else:
        return None

a = Rectangle(0, 0, 1, 4)
b = Rectangle(2, 0, 1, 5)
print get_intersect_rectangle(a, b)