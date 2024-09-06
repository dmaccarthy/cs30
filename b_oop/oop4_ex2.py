"""
CSE 3120: Object-Oriented Programming 1
Inheritance — Example 2
"""

class MyClass:
    myStr = "Hello!"
    myInt = 7


# Main program...
myInstance = MyClass()
myInstance.myStr = "Goodbye!"
print(MyClass.myStr, MyClass.myInt)         # Hello! 7
print(myInstance.myStr, myInstance.myInt)   # Goodbye! 7
print(myInstance.myStr is MyClass.myStr)    # False