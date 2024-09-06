"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 10
"""

class MyXClass:
    x = 0
    w = 3

class MyYClass:
    y = 1
    w = 4

class MyClass (MyXClass, MyYClass):
    z = 2


# Main program...
obj = MyClass()
print(obj.w)