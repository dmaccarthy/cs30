"""
CSE 3120: Object-Oriented Programming 1
Special Methods — Example 6
"""

class Person:
    "A class to represent data about an individual person"

    def __init__ (self, name):
        self._name = name

    def __repr__ (self):
        return 'Person("{}")'.format(self._name)


# Main program...
myFriend = Person("John Q. Doe")
print(myFriend)       # Person("John Q. Doe")
