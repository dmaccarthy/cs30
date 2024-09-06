"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 5
"""

class MyClass:
    count = 0

    @classmethod
    def advanceCounter(cls):
        cls.count = cls.count + 1


# Main program...
inst1 = MyClass()
inst2 = MyClass()
print(inst1.count)      # 0
inst2.advanceCounter()
print(inst1.count)      # 1