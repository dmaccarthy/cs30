"""
CSE 3120: Object-Oriented Programming 1
Special Methods — Example 5
"""

class Person:
    "A class to represent data about an individual person"

    def __init__ (self, name):
        self._name = name


# Main program...
myFriend = Person("John Q. Doe")
print(myFriend)   # <__main__.Person object at 0x02BF0970>
