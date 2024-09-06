"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 3
"""

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count = MyClass.count + 1


# Main program...
inst1 = MyClass()
inst2 = MyClass()
print(inst1.count)       # 2
print(inst2.count)       # 2
print(MyClass.count)     # 2