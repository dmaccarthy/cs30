"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 4
"""

class MyClass:
    count = 0

    def __init__(self):
        self.count = self.count + 1


# Main program...
inst1 = MyClass()
inst2 = MyClass()
print(inst1.count)       # 1
print(inst2.count)       # 1
print(MyClass.count)     # 0