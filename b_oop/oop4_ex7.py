"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 7
"""

class Rectangle:

    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * (self.base + self.height)


class Square (Rectangle):

    def __init__(self, s):
        self.base = s
        self.height = s


sq = Square(3.0)
print(sq.area(), sq.perimeter())
