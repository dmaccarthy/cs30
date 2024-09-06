"""
CSE 3120: Object-Oriented Programming 1
Special Methods — Example 3
"""

class Person:
    "A class to represent data about an individual person"

    def __init__ (self, name):
        "Initializer (called automatically by the constructor)"
        self._name = name

    def name (self):
        "Accessor method"
        return self._name


# Main program...
myFriend = Person("John Q. Doe")
print(myFriend.name())
