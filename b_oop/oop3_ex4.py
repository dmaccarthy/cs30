"""
CSE 3120: Object-Oriented Programming 1
Special Methods — Example 4
"""

class Person:

    def setName (self, name):
        "Modifier method"
        self._name = name

    # Create a duplicate reference...
    __init__ = setName

    def name (self):
        "Accessor method"
        return self._name


# Main program...
myFriend = Person("John Q. Doe")
print(myFriend.name())