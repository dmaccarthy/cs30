"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 8
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

print(type(sq))                   # <class '__main__.Square'>
print(isinstance(sq, Square))     # True
print(isinstance(sq, Rectangle))  # True
print(isinstance(sq, int))        # False
