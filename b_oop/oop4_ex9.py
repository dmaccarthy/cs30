"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 9
"""

class MyXClass:
    x = 0

class MyYClass:
    y = 1

class MyClass (MyXClass, MyYClass):
    z = 2


# Main program...
obj = MyClass()
print(obj.x, obj.y, obj.z)
